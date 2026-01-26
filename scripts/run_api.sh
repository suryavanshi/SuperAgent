#!/usr/bin/env bash
set -euo pipefail

uvicorn server.api:app --host 0.0.0.0 --port 8000
