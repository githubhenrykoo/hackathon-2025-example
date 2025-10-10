---
trigger: always_on
---

# Python Virtual Environment Rules for Local RAG Project

## Overview

This document outlines the standard practices for Python virtual environment management in our Local RAG (Retrieval-Augmented Generation) project using Ollama. These guidelines ensure consistency, reproducibility, and maintainability across development environments.

## Technology Choices

- **Package Manager**: `uv` instead of traditional `pip`
- **Virtual Environment**: Local `.venv` directory
- **Python Version**: 3.10+ (required for compatibility with all dependencies)
- **Dependency Management**: Requirements files with pinned versions

## Environment Setup

### Initial Setup

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Unix/macOS:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### Daily Development

- Always work within the activated virtual environment
- Run `uv pip sync` after pulling updates to ensure dependencies are current
- Use `deactivate` command to exit the virtual environment when done

## Dependency Management

### Adding New Dependencies

```bash
# Activate virtual environment first
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install new package
uv pip install package_name

# Update requirements file
uv pip freeze > requirements.txt
```

### Production vs. Development Dependencies

- `requirements.txt`: Core dependencies needed for production
- `requirements-dev.txt`: Additional development/testing dependencies
- Install development dependencies: `uv pip install -r requirements-dev.txt`

### Version Pinning Rules

- Production dependencies: Use exact pins (`==`) for deterministic builds
- Development dependencies: Use compatible release specifiers (`~=`) if appropriate
- Generate hashes for security: `uv pip freeze --hash > requirements.txt`

## Project-Specific Considerations

### Ollama Compatibility

- Ensure all LLM-related packages are compatible with Ollama's API
- Test model loading with minimal RAM requirements before adding dependencies

### Vector Database Dependencies

- Choose dependencies that support local persistence
- Prefer packages with Python 3.10+ compatibility

### Document Processing Libraries

- Separate document processing dependencies into modular requirements files
- Example: `requirements-doc-processors.txt` for PDF, DOCX, etc. support

## Best Practices

1. **Isolation**: Never install project packages globally
2. **Reproducibility**: Keep requirements files updated
3. **Performance**: Use `uv pip sync` for faster dependency resolution
4. **Cleanup**: Periodically run `uv pip cache purge` to clean up disk space
5. **Documentation**: Document any special installation steps in README.md

## Troubleshooting

### Common Issues

- If experiencing package conflicts, try: `uv pip sync --python=3.10 requirements.txt`
- For ARM64 architecture (e.g., Apple Silicon), use: `UV_NATIVE_TOOLCHAIN=1 uv pip install ...`
- If a package fails to install, check if a pre-built wheel is available or if you need additional system dependencies

## Updating This Document

This document should be reviewed and updated when:
- Major Python version upgrades occur
- New dependency management tools are adopted
- Project requirements change significantly

Last updated: July 3, 2025
