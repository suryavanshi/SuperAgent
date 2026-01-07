# Autonomous Agent Loop Specification

## Overview
This document describes the required loop for an autonomous agent that operates with a stable system prompt, a static tool registry, an append-only deterministic transcript, filesystem memory with reversible compression, a sandboxed code/shell tool, strict error handling, and periodic objective recitation.

## Core Loop Requirements

### 1) Stable System Prompt + Static Tool Registry
- The system prompt **must not change** during execution.
- The tool registry **must be static** for the entire run.
- Any tool metadata updates require a **new run**, not a hot reload.

### 2) Append-Only Deterministic Transcript
- Maintain an **append-only** transcript of all inputs, outputs, tool calls, tool results, and errors.
- The transcript must be **deterministic**: identical inputs and tool outputs produce identical transcript entries in the same order.
- Never delete or reorder transcript entries.

### 3) Filesystem Memory with Reversible Compression
- Persist long-term memory on the filesystem.
- Compression must be **reversible**:
  - Store the **full original text**.
  - Store **compressed representations** (summaries/embeddings/diffs) as **pointers** to the full text.
  - The pointer must allow a deterministic retrieval of the original content.

### 4) Sandboxed Code/Shell Tool
- All code execution and shell commands must run in a **sandboxed** environment.
- Sandbox must prevent data exfiltration and restrict filesystem scope to approved paths.
- The agent must treat the sandbox as **non-interactive** and capture outputs deterministically.

### 5) Error Handling with Context Append
- Any tool error (non-zero exit, runtime exception, timeout) **must be appended into context**.
- Errors must be recorded **verbatim** in the transcript and must not be suppressed.
- If a tool fails, the agent must:
  1. Append the error to context.
  2. Evaluate recovery steps.
  3. Continue or stop based on policy, never silently retry.

### 6) Objective Recitation in todo.md
- Maintain a `todo.md` file with the current objective and progress.
- Update the objective recitation **every few steps** (recommend: every 3–5 loop iterations).
- Each update should include:
  - The current objective (verbatim)
  - The last completed step
  - The next intended step

## Definition of Done
- [ ] System prompt is stable for the entire run.
- [ ] Tool registry is static and never hot-reloaded.
- [ ] Transcript is append-only and deterministic.
- [ ] Filesystem memory stores full text plus reversible compressed pointers.
- [ ] All code/shell execution is sandboxed.
- [ ] Tool errors are always appended into context verbatim.
- [ ] `todo.md` objective recitation is updated every few steps.

## Smoke-Test Tasks (5)
1. **Transcript determinism**: Run the same input twice; verify identical transcript order and entries.
2. **Error append test**: Invoke a failing tool and confirm the error is appended verbatim to context.
3. **Memory reversibility**: Compress and store a long note, then restore the exact original text via pointer.
4. **Sandbox enforcement**: Attempt to access a disallowed path from the shell tool and confirm denial.
5. **Objective recitation cadence**: Run 6 loop steps and verify `todo.md` updated at least twice.
