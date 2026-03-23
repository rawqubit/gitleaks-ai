"""Smoke tests for gitleaks-ai."""
import sys, subprocess, tempfile, os, pytest

def test_cli_help():
    r = subprocess.run([sys.executable, "main.py", "--help"], capture_output=True, text=True)
    assert r.returncode == 0

def test_scan_clean_dir():
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "clean.py"), "w") as f:
            f.write('print("hello world")\n')
        r = subprocess.run([sys.executable, "main.py", "--path", d, "--no-ai"],
                           capture_output=True, text=True)
        assert r.returncode in (0, 1)

def test_module_no_syntax_errors():
    r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
