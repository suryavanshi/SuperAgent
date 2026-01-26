from agent.tools.registry import ToolRegistry


def test_registry_runs_tool():
    registry = ToolRegistry()
    registry.register("echo", lambda text: text)
    assert registry.run("echo", "hi") == "hi"
