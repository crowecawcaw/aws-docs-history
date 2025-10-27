# Agent Instructions

@link README.md

Please read the README for complete information about this project.

## Documentation Commit Policy

**IMPORTANT**: Do NOT commit changes to the `docs/` directory unless explicitly instructed to do so.

- Documentation updates are managed exclusively through GitHub Actions workflows
- The daily crawler workflow automatically updates and commits documentation changes
- Manual documentation commits should only be made when explicitly requested by the user
- All other code changes (scripts, tests, configuration files, workflows, etc.) should be committed normally

When making commits:
- Stage and commit code changes in the repository root and other directories
- Exclude the `docs/` directory from commits unless specifically asked to include it
- Use `git add` with appropriate paths to avoid staging documentation files
