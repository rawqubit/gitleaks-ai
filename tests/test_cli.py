"""
Tests for gitleaks-ai.
CLI: main.py scan <TARGET> [--ai-review] [--min-entropy] [--output] [--no-fp]
"""
import sys
import os
import subprocess
import tempfile
import pytest


def run(*args):
    env = os.environ.copy()
    env.setdefault('OPENAI_API_KEY', 'sk-dummy')
    return subprocess.run(
        [sys.executable, "main.py"] + list(args),
        capture_output=True, text=True, env=env
    )


def test_root_help():
    r = run("--help")
    assert r.returncode == 0
    assert "scan" in r.stdout or "usage" in r.stdout.lower()


def test_scan_help():
    r = run("scan", "--help")
    assert r.returncode == 0
    assert "--min-entropy" in r.stdout


def test_scan_clean_directory():
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "clean.py"), "w") as f:
            f.write('def hello():\n    return "hello world"\n')
        r = run("scan", d)
        assert r.returncode in (0, 1)


def test_scan_output_json():
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "file.py"), "w") as f:
            f.write('x = 1\n')
        r = run("scan", d, "--output", "json")
        assert r.returncode in (0, 1)


def test_module_compiles():
    r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
