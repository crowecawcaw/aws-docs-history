# Project rules

Rules allow you to define project-specific guidelines, coding standards, and behavioral rules for Amazon Q Developer CLI through markdown files. These rules are automatically integrated into agent contexts, ensuring consistent behavior across your development workflow.

## Overview

Rules are markdown files stored in the `.amazonq/rules/` directory that define how Q Developer should behave in your project. They can cover coding standards, architecture patterns, team conventions, security guidelines, and any other project-specific requirements.

## File structure

```
project/
├── .amazonq/
│   └── rules/
│       ├── coding-standards.md
│       ├── architecture-guidelines.md
│       ├── security-policies.md
│       └── team-conventions.md
└── src/
    └── main.py
```

## Storage location

- **Path**: `.amazonq/rules/**/*.md`
- **Scope**: Workspace-specific (rules only apply to the current project)
- **Format**: Standard markdown files
- **Pattern**: All `.md` files in the rules directory and subdirectories

## Agent integration

### Automatic inclusion

The default agent automatically includes all rules using the resource pattern:

```
{
  "resources": [
    "file://.amazonq/rules/**/*.md"
  ]
}
```

### Custom agent integration

Custom agents can explicitly include rules in their configuration:

```
{
  "name": "my-custom-agent",
  "resources": [
    "file://.amazonq/rules/**/*.md",
    "file://./docs/**/*.md"
  ]
}
```

### Context loading

Rules are loaded as agent resources and become part of the agent's context, influencing all interactions and responses.

## Rule types and examples

### Coding standards

Define language-specific style guidelines and best practices:

```
# Python Coding Standards

## Style Guidelines
- Use Black for code formatting
- Maximum line length: 88 characters
- Use type hints for all function parameters and return values
- Follow PEP 8 naming conventions

## Error Handling
- Always use specific exception types
- Include meaningful error messages
- Log errors at appropriate levels
```

### Architecture patterns

Specify architectural constraints and design patterns:

```
# Architecture Guidelines

## Service Architecture
- Use microservices pattern for new features
- Implement circuit breaker pattern for external API calls
- All services must expose health check endpoints

## Database Access
- Use repository pattern for data access
- No direct database queries in controllers
- Implement proper connection pooling
```

### Security policies

Define security requirements and constraints:

```
# Security Guidelines

## Authentication
- All API endpoints must require authentication
- Use JWT tokens with 1-hour expiration
- Implement proper session management

## Data Handling
- Never log sensitive information
- Encrypt all PII data at rest
- Use parameterized queries to prevent SQL injection
```

### Team conventions

Establish team-specific workflows and practices:

```
# Team Conventions

## Code Review Process
- All changes require at least 2 approvals
- Include tests for new functionality
- Update documentation for API changes

## Commit Messages
- Use conventional commit format
- Include ticket numbers in commit messages
- Keep commits focused and atomic
```

## Markdown formatting

Rules should be written in standard markdown format:

- **Headers**: Use `#`, `##`, `###` for organization
- **Code blocks**: Include examples with proper syntax highlighting
- **Lists**: Use bullet points or numbered lists for guidelines
- **Emphasis**: Use `**bold**` or `*italic*` for important points
- **Links**: Reference external documentation when helpful

## Best practices

### Organization

- Create separate files for different types of rules
- Use descriptive filenames that reflect content
- Organize rules hierarchically with headers
- Keep individual files focused on specific topics

### Content guidelines

- Write clear, actionable guidelines
- Include examples where helpful
- Explain the reasoning behind rules when not obvious
- Keep rules up-to-date with project evolution

### Maintenance

- Review rules regularly for relevance
- Update rules when team practices change
- Remove outdated or conflicting guidelines
- Ensure rules are consistent across files

## Scope and precedence

### Workspace-specific

- Rules only apply to the current project directory and subdirectories
- No global rules system - all rules are local to the workspace
- Different projects can have completely different rule sets

### Agent-dependent

- Rules only apply when using agents that include them in their resources
- Default agent automatically includes all rules
- Custom agents must explicitly include rules to use them

### No inheritance

- Rules don't inherit from parent directories
- Each project maintains its own independent rule set
- No system-wide or user-wide rules

## Use cases

### Team standardization

Ensure all team members follow the same coding standards and practices:

- Consistent code formatting and style
- Shared architectural patterns
- Common error handling approaches
- Unified testing strategies

### Project-specific requirements

Define requirements unique to your project:

- Domain-specific business rules
- Integration patterns for specific services
- Performance requirements and constraints
- Compliance and regulatory requirements

### Onboarding assistance

Help new team members understand project conventions:

- Development workflow guidelines
- Code review expectations
- Testing requirements
- Documentation standards

### Quality assurance

Maintain code quality through automated guidance:

- Security best practices
- Performance optimization guidelines
- Maintainability standards
- Documentation requirements

## Getting started

1. **Create rules directory**: `mkdir -p .amazonq/rules`
2. **Add your first rule**: Create a markdown file with your guidelines
3. **Test integration**: Ask Q Developer about your project standards to verify rules are loaded
4. **Iterate and improve**: Refine rules based on team feedback and project needs

## Example workflow

```
# Create rules directory
mkdir -p .amazonq/rules

# Create coding standards
cat > .amazonq/rules/coding-standards.md << 'EOF'
# Coding Standards

## Python Style
- Use Black for formatting
- Type hints required
- Maximum line length: 88 characters
EOF

# Test rules integration
q chat
# Ask: "What are our coding standards for Python?"
# Q will reference the rules you've defined
```
