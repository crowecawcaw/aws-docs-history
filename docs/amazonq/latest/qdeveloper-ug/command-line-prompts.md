# Manage prompts

The Amazon Q Developer CLI provides comprehensive prompt management capabilities for both local prompts and Model Context Protocol (MCP) prompts. This system allows you to create, edit, organize, and use reusable prompts across your development workflow.

## About prompt types

The prompt system supports three types of prompts:

- **Local prompts**: Project-specific prompts stored in your workspace
- **Global prompts**: User-wide prompts available across all projects
- **MCP prompts**: Prompts provided by MCP servers with enhanced functionality

## Commands

All prompt management is accessed through the `/prompts` command with various subcommands.

### List prompts

```
/prompts list
```

Displays all available prompts in a three-column layout showing names, descriptions, and sources. Shows prompt counts and indicates which prompts come from local storage, global storage, or MCP servers.

### Create prompts

```
/prompts create --name name [--content content]
```

Creates a new local prompt in the current workspace.

###### Parameters

`name` (required)

Prompt name (maximum 50 characters)

`--content `content`` (optional)

Direct content specification

**Behavior:**

- If `--content` is provided, creates prompt with specified content
- If no content provided, opens your default editor for content creation
- Prompts are saved to `.amazonq/prompts/` in the current workspace

### Edit prompts

```
/prompts edit name
```

Opens an existing prompt in your default editor for modification.

**Supported prompts:**

- Local workspace prompts
- Global user prompts
- MCP prompts (where supported by the server)

### View prompt details

```
/prompts details name
```

Shows comprehensive information about a prompt including:

- Metadata and argument details
- Complete prompt content before AI processing
- Parameter requirements and examples
- Source information (local, global, or MCP server)

## Using prompts

Once you've created prompts, invoke them in chat using the @ prefix:

```
@prompt-name
```

For prompts that accept arguments:

```
@prompt-name arg1 arg2 "argument with spaces"
```

### Examples

```
@code-review
# Uses the code-review prompt you created
```

```
@debug-help "connection timeout error"
# Passes the error message as an argument to the debug-help prompt
```

## Working with prompt arguments

Many prompts accept arguments to customize their behavior. Understanding how to discover, provide, and troubleshoot prompt arguments is essential for effective prompt usage.

### Argument syntax

Prompt arguments follow a simple positional syntax:

```
@prompt-name <required-arg> [optional-arg]
```

###### Argument conventions

`<required-arg>`
Arguments that must be provided

`[optional-arg]`
Arguments that can be omitted

`"quoted arguments"`
Use quotes for arguments containing spaces

#### Quoting and special characters

```
# Arguments with spaces require quotes
@debug-help "connection timeout error"

# Multiple word arguments
@code-review "src/main.py" "security review"

# Single quotes also work
@generate-docs 'API Reference' 'markdown'

# Mix quoted and unquoted arguments
@analyze-logs error "last 24 hours" --verbose
```

### Discovering prompt arguments

Use the `/prompts details` command to see what arguments a prompt accepts:

```
/prompts details prompt-name
```

This shows:

- Required and optional arguments
- Argument descriptions and purposes
- Usage examples with proper syntax
- Validation requirements

#### Example: Discovering arguments

```
/prompts details code-review

# Output:
# Name: code-review
# Server: development-tools
#
# Usage: @code-review <file-path> [review-type]
#
# Arguments:
#   (required) file-path - Path to the file to review
#   (optional) review-type - Type of review (security, performance, style)
```

### Argument validation and errors

The CLI validates prompt arguments and provides helpful error messages:

#### Missing required arguments

```
# Calling prompt without required arguments
@code-review

# Error output:
# Error: Missing required arguments for prompt code-review
# Usage: @code-review <file-path> [review-type]
# Arguments:
#   (required) file-path - Path to the file to review
#   (optional) review-type - Type of review (security, performance, style)
```

#### Invalid argument values

```
# Providing invalid argument values
@validate-email "not-an-email"

# Error output:
# Error: Invalid arguments for prompt validate-email:
#   - email: Must be a valid email ending in .com
# Use '/prompts details validate-email' for usage information.
```

### Server-specific prompts

When multiple MCP servers provide prompts with the same name, specify the server:

```
# Ambiguous prompt error
@analyze

# Error: Prompt analyze is ambiguous. Use one of the following:
# - @dev-tools/analyze
# - @security-tools/analyze

# Use server-specific syntax
@dev-tools/analyze "performance issues"
@security-tools/analyze "vulnerability scan"
```

## Creating prompts with arguments

You can create both file-based and MCP prompts that accept arguments for dynamic content generation.

### File-based prompts with arguments

File-based prompts (local and global) receive arguments as contextual information when invoked. The arguments are provided to the AI model along with the prompt content, but file-based prompts do not have built-in templating or argument substitution.

#### Example: Creating a parameterized prompt

```
# Create a code review prompt
/prompts create --name code-review --content "Please review this code for best practices, security issues, and potential improvements. Pay special attention to the specific aspects mentioned in the arguments."

# Usage with arguments
@code-review "src/auth.py" "security focus"
# The AI receives both the prompt content and the arguments as context
```

**Note:** File-based prompts pass arguments as additional context to the AI model. The model interprets how to use the arguments based on the prompt content and the provided argument values.

### MCP prompt arguments

MCP servers can define structured argument schemas with validation, descriptions, and type information. These provide the richest argument experience with automatic validation and help text.

#### Understanding MCP argument schemas

MCP prompts define arguments with:

- **Name**: The argument identifier
- **Description**: What the argument is for
- **Required**: Whether the argument is mandatory
- **Validation**: Rules for valid values

```
# Example MCP prompt schema (shown via /prompts details)
/prompts details aws-troubleshoot

# Output:
# Name: aws-troubleshoot
# Server: aws-tools
#
# Usage: @aws-troubleshoot <service> <error-message> [region]
#
# Arguments:
#   (required) service - AWS service name (e.g., ec2, s3, lambda)
#   (required) error-message - The error message you're seeing
#   (optional) region - AWS region (defaults to us-east-1)
```

### Best practices for prompt arguments

- **Use descriptive names**: `file-path` instead of `f`
- **Provide clear descriptions**: Explain what each argument does
- **Make optional arguments truly optional**: Provide sensible defaults
- **Order arguments logically**: Most important/common arguments first
- **Use validation**: Help users provide correct values

## Storage locations

### Local prompts (workspace-specific)

- **Location**: ``project`/.amazonq/prompts/`
- **Scope**: Available only within the current project
- **Priority**: Highest (overrides global and MCP prompts with same name)

### Global prompts (user-wide)

- **Location**: `~/.aws/amazonq/prompts/`
- **Scope**: Available across all projects
- **Priority**: Medium (overrides MCP prompts with same name)

### MCP prompts

- **Source**: Provided by configured MCP servers
- **Scope**: Depends on server configuration
- **Priority**: Lowest (overridden by local and global prompts)

## Priority system

When multiple prompts have the same name, the system uses this priority order:

1. **Local prompts** (highest priority)
2. **Global prompts**
3. **MCP prompts** (lowest priority)

This allows you to override MCP or global prompts with project-specific versions when needed.

## Enhanced features

### Content preview

The system displays the complete prompt content before sending it to the AI model, eliminating confusion about what information was actually processed.

### Improved error handling

- MCP server errors are converted to user-friendly messages
- Helpful usage examples are generated from prompt metadata
- Clear guidance for invalid parameters or missing requirements

### Visual formatting

- Consistent terminal styling across all prompt operations
- Proper content display for all prompt message types
- Three-column layout for improved readability in listings

## MCP integration

The prompt system seamlessly integrates with MCP servers:

- **Automatic discovery**: MCP prompts are automatically discovered from configured servers
- **Enhanced UX**: Improved user experience for MCP prompt management
- **Error translation**: Raw JSON errors are converted to actionable messages
- **Content preview**: Full content preview for MCP prompts before execution

## Comprehensive examples

These examples demonstrate various prompt argument patterns and real-world usage scenarios.

### Basic prompt creation and usage

```
# Create a simple prompt without arguments
/prompts create --name code-review --content "Please review this code for best practices, security issues, and potential improvements:"

# Use the prompt
@code-review
```

### Single argument prompts

```
# Create a debug help prompt
/prompts create --name debug-help --content "Help me debug this error. Provide potential causes and solutions."

# Usage examples
@debug-help "connection timeout"
@debug-help "null pointer exception in line 42"
@debug-help "AWS S3 access denied error"
```

### Multiple argument prompts

```
# Create a comprehensive code review prompt
/prompts create --name detailed-review --content "Review the specified code focusing on the requested aspects. Consider the provided context and provide specific recommendations."

# Usage with multiple arguments
@detailed-review "src/auth.py" "security" "authentication module"
@detailed-review "api/handlers.js" "performance" "high-traffic endpoint"
@detailed-review "utils/parser.go" "maintainability" "legacy code refactor"
```

### Required and optional arguments

Example MCP prompt with mixed argument types:

```
# Using an MCP prompt with required and optional arguments
/prompts details aws-deploy

# Output shows:
# Usage: @aws-deploy <service> <environment> [region] [options]
# Arguments:
#   (required) service - Service name to deploy
#   (required) environment - Target environment (dev, staging, prod)
#   (optional) region - AWS region (defaults to us-east-1)
#   (optional) options - Additional deployment options

# Usage examples
@aws-deploy "my-api" "staging"
@aws-deploy "my-api" "prod" "us-west-2"
@aws-deploy "my-api" "prod" "eu-west-1" "--force --no-rollback"
```

### Complex argument scenarios

```
# Arguments with spaces and special characters
@generate-docs "API Reference Guide" "markdown format" "--include-examples"

# File paths and URLs
@analyze-logs "/var/log/app.log" "ERROR" "last 1 hour"
@fetch-data "https://api.example.com/users" "json" "authentication required"

# Multiple quoted arguments
@create-test "user authentication" "integration test" "should validate JWT tokens"
```

### Server-specific prompts

```
# When multiple servers provide the same prompt name
@dev-tools/analyze "performance bottleneck" "cpu usage"
@security-tools/analyze "vulnerability scan" "web application"
@data-tools/analyze "query performance" "database optimization"
```

### Error handling examples

```
# Missing required arguments
@aws-deploy
# Error: Missing required arguments for prompt aws-deploy
# Usage: @aws-deploy <service> <environment> [region] [options]

# Too many arguments for a simple prompt
@code-review "extra" "arguments" "provided"
# Warning: Extra arguments ignored for prompt code-review

# Invalid argument values (MCP validation)
@validate-email "invalid-email-format"
# Error: Invalid arguments for prompt validate-email:
#   - email: Must be a valid email address
# Use '/prompts details validate-email' for usage information.
```

### Complete discovery workflow

```
# 1. List available prompts
/prompts list

# Output shows prompts with argument indicators:
# Name              Description                    Arguments (* = required)
# code-review       Code review template
# debug-help        Debugging assistance          error_message*
# aws-deploy        AWS deployment helper         service*, environment*, region, options

# 2. Get detailed information about a specific prompt
/prompts details aws-deploy

# 3. Use the prompt with discovered arguments
@aws-deploy "my-service" "production" "us-west-2"
```

### Global vs local prompt arguments

```
# Create a global prompt for team use
/prompts create --name team-standup --global --content "Generate standup update covering the specified topics and time period"

# Create a local project-specific override
/prompts create --name team-standup --content "Project-specific standup update for the current feature work"

# Usage (local version takes priority)
@team-standup "Alice" "login feature" "in progress"
```

### Troubleshooting argument issues

```
# Check if prompt exists and see its arguments
/prompts details non-existent-prompt
# Error: Prompt non-existent-prompt not found. Use '/prompts list' to see available prompts.

# Resolve ambiguous prompts
@analyze
# Error: Prompt analyze is ambiguous. Use one of the following:
# - @dev-tools/analyze
# - @security-tools/analyze

# Get help with argument format
@complex-prompt
# Error: Missing required arguments for prompt complex-prompt
# Usage: @complex-prompt <input-file> <output-format> [options]
# Use '/prompts details complex-prompt' for more information.
```
