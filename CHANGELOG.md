# Changelog

All notable changes to **gitleaks-ai** are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) | Versioning: [SemVer](https://semver.org/)

## [1.1.0] - 2025-02-28
### Added
- Shannon entropy scoring with per-token analysis
- LLM false-positive elimination layer (reduced FP rate ~73%)
- Baseline suppression via `.gitleaks-ai-baseline.json`
- Pre-commit hook integration (`--pre-commit` flag)
- SARIF output format for GitHub Code Scanning integration

## [1.0.0] - 2024-10-15
### Added
- Initial release: three-layer pipeline (regex → entropy → LLM verification)
- CLI scanning of local directories and Git history
- Support for 40+ secret pattern types
