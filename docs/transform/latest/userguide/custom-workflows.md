# Workflows

## Executing Transformations

This section describes the different ways to execute transformations and options for controlling execution behavior.

### Execution Modes

AWS Transform custom supports three execution modes to accommodate different workflows.

**Interactive Conversational Mode**

Start the CLI with `atx` and ask the agent to execute a transformation through natural language. This mode allows you to have a full conversation with the agent, interrupt execution at any point, and provide feedback during the transformation process.

Use this mode when you want maximum control and the ability to guide the agent through complex scenarios.

**Direct Interactive Execution**

Use `atx custom def exec -n <transformation-name> -p <path>` to start a specific transformation interactively. This mode allows you to review and interact with the agent at the beginning, during, or at the end of execution. The agent will pause at key decision points and ask for your input.

This is ideal for testing and refining transformations before running them autonomously.

You can run transformations in non-interactive mode or headless mode. Non-interactive mode suppresses prompts during a named transformation. Headless mode lets you run the agent with a plain-text prompt, bypassing the interactive interface entirely.

#### Non-interactive mode

Use `atx custom def exec -n <transformation-name> -p <path> -x -t` for full automation. Add `-x` to run in non-interactive mode, and `-t` to trust all tools automatically without prompting.

This mode is designed for CI/CD pipeline integration and bulk execution where no human intervention is available or desired.

#### Headless mode

To complete tasks without interacting with the agent, run `atx -x "<prompt>" -t` and provide your instruction in plain text.

##### Headless transformation execution

Use this mode to apply an existing transformation definition to your codebase. The transformation runs each step automatically without requiring your approval.

```
atx -x "apply transformation definition <transformation_definition_name> to <codebase_path>" -t
```

##### Headless transformation development

Create or modify transformation definitions.

To convert a legacy transformation definition file (transformation\_definition.md) to the new skill format (SKILL.md + references/), run the following command:

```
atx -x "convert <legacy_transformation_definition_file_path> transformation definition to skill" -t
```

To create a new transformation definition, run the following command:

```
atx -x "create a transformation definition to <description> with references docs <reference_docs_path>" -t
```

### Common Command Flags

When executing transformations with `atx custom def exec`, the following flags are commonly used:

- `-n` or `--transformation-name` - Specifies the name of the transformation to execute
- `-p` or `--code-repository-path` - Specifies the path to your codebase (use "." for current directory)
- `-c` or `--build-command` - Specifies the build or validation command to run
- `-x` or `--non-interactive` - Enables non-interactive mode (no user prompts)
- `-t` or `--trust-all-tools` - Automatically trusts all tools without prompting
- `-d` or `--do-not-learn` - Prevents knowledge item extraction from this execution
- `--tv` or `--transformation-version` - Specifies a specific version of the transformation
- `-g` or `--configuration` - Provides a configuration file or inline configuration

###### Important

The `-t` or `--trust-all-tools` flag automatically approves all tool executions without prompting and bypasses most security guardrails, (commands matching your `alwaysPromptCommands` list still require explicit permission unless overridden by `trustedShellCommands`). Passing in `--non-interactive` and `--trust-all-tools` is required for a fully autonomous experience but not required to execute the transformation. Use with caution in production environments.

### Using Configuration Files

AWS Transform custom supports optional configuration files in YAML or JSON format. Configuration files allow you to specify execution parameters and provide additional context to the agent.

**To use a configuration file:**

```
atx custom def exec --configuration file://config.yaml
```

You can also provide configuration as inline key-value pairs:

```
atx custom def exec --configuration "key=value,key2=value2"
```

**Example configuration file (config.yaml):**

```
codeRepositoryPath: ./my-project
transformationName: my-transformation
buildCommand: mvn clean install
additionalPlanContext: |
  The target Java version to upgrade to is Java 17.
  Ensure compatibility with our internal logging framework version 2.3.
validationCommands: |
  mvn test
  mvn verify
```

The `additionalPlanContext` parameter provides extra context for the agent's execution plan. This is especially useful with AWS-managed transformations to customize their behavior for your specific needs.

### Build and Validation Commands

The build or validation command is an optional parameter that specifies how to validate your code during the transformation process. AWS Transform custom will attempt to infer the best build command based on the transformation if not specified, though it is recommended to be specific for quality.

**Examples of build and validation commands:**

- Java: `mvn clean install` or `gradle build`
- Python: `pytest` or `python -m py_compile`
- Node.js: `npm run build` or `npm test`
- Linters: `eslint .` or `pylint .`

Even for languages or transformations that don't require building, providing a command that validates the results and returns issues if validation fails is very important to improve transformation quality.

If no build or validation is needed, omit from your input.

### Controlling Learning Behavior

By default, AWS Transform custom extracts knowledge items from every transformation execution. You can prevent learning for specific executions.

**To prevent learning from an execution:**

```
atx custom def exec -n my-transformation -p ./my-project -d
```

The `-d` or `--do-not-learn` flag opts out of allowing knowledge item extraction from the current execution.

### Resuming Conversations

AWS Transform custom allows you to resume previous conversations within 30 days of creation.

**To resume the most recent conversation:**

```
atx --resume
```

**To resume a specific conversation:**

```
atx --conversation-id <conversation-id>
```

###### Important

Conversations can only be resumed within 30 days of creation. After 30 days, the conversation can no longer be resumed.

### Tracking Agent Minutes

AWS Transform custom tracks the [agent minutes](https://aws.amazon.com/transform/pricing/ "https://aws.amazon.com/transform/pricing/") consumed during a transformation session. Agent minutes accumulate throughout the conversation lifecycle and are displayed when the conversation ends:

```
Agent minutes used: 12.50
```

Agent minutes persist across interruptions. If you interrupt a session with Ctrl+C and resume it later, the previously accumulated minutes carry over and continue accumulating in the resumed session.

**To check Agent Minutes during an interactive session:**

Type `/usage` at the input prompt to display the current accumulated Agent Minutes without ending the conversation.

**To set an Agent Minutes budget limit:**

```
atx custom def exec -n my-transformation -p ./my-project --limit 30
```

The `--limit` option sets a maximum [Agent Minutes](https://aws.amazon.com/transform/pricing/ "https://aws.amazon.com/transform/pricing/") budget for the session. Agent Minutes reflect active agent work time, not wall clock time. When the limit is reached, the CLI displays a message and exits with instructions to resume:

```
⚠️ Budget limit reached: 30.00 / 30.00 Agent Minutes. Exiting.
```

You can resume the conversation later with an increased limit:

```
atx --conversation-id <conversation_id> -t --limit <increased_limit>
```

## Continual Learning

This section describes how to manage knowledge items created by continual learning.

### Understanding Knowledge Items

Knowledge items are automatically extracted learnings from transformation executions. These are created asynchronously by the continual learning system based on:

- Developer feedback provided in interactive mode
- Code issues encountered during transformations

Knowledge items start in a "not approved" state and must be explicitly approved by transformation owners before they can be used in future executions. Unlike references which you provide upfront, knowledge items accumulate over time as the transformation is executed across different codebases.

### Listing Knowledge Items

View all knowledge items for a transformation definition.

**To list knowledge items:**

```
atx custom def list-ki -n my-transformation
```

This displays all knowledge items that have been extracted from executions of the specified transformation definition.

### Viewing Knowledge Item Details

View detailed information about a specific knowledge item.

**To view knowledge item details:**

```
atx custom def get-ki -n my-transformation --id <knowledge-item-id>
```

### Enabling and Disabling Knowledge Items

Control which knowledge items are applied to future transformations.

**To enable a knowledge item:**

```
atx custom def update-ki-status -n my-transformation --id <knowledge-item-id> --status ENABLED
```

**To disable a knowledge item:**

```
atx custom def update-ki-status -n my-transformation --id <knowledge-item-id> --status DISABLED
```

### Configuring Auto-Approval

You can configure whether knowledge items are automatically enabled or require manual approval.

**To enable auto-approval for all knowledge items:**

```
atx custom def update-ki-config -n my-transformation --auto-enabled TRUE
```

**To disable auto-approval:**

```
atx custom def update-ki-config -n my-transformation --auto-enabled FALSE
```

### Deleting Knowledge Items

Permanently remove knowledge items that are not useful.

**To delete a knowledge item:**

```
atx custom def delete-ki -n my-transformation --id <knowledge-item-id>
```

### Exporting Knowledge Items

Export all knowledge items for a transformation to markdown format for review or documentation.

**To export knowledge items:**

```
atx custom def export-ki-markdown -n my-transformation
```

## Advanced Configuration

This section describes advanced features and configuration options for AWS Transform custom.

### Environment Variables

You can customize CLI behavior using environment variables.

###### Note

The following examples show Linux and macOS syntax (`export`). On Windows, set environment variables in PowerShell using `$env:`NAME`="`value`"`. See the **Windows (PowerShell)** tabs for the equivalent commands.

**ATX\_SHELL\_TIMEOUT**

Override the default timeout for shell commands (900 seconds/15 minutes).

Linux and macOS

```
export ATX_SHELL_TIMEOUT=1800  # 30 minutes
```

Windows (PowerShell)

```
$env:ATX_SHELL_TIMEOUT=1800  # 30 minutes
```

This is useful for large codebases or long-running build processes.

**ATX\_DISABLE\_UPDATE\_CHECK**

Disable automatic version checks and update notifications during command execution.

Linux and macOS

```
export ATX_DISABLE_UPDATE_CHECK=true
```

Windows (PowerShell)

```
$env:ATX_DISABLE_UPDATE_CHECK="true"
```

**ATX\_GIT\_COMMITTER\_NAME and ATX\_GIT\_COMMITTER\_EMAIL**

Configure the author identity used for the checkpoint commits that AWS Transform custom creates in your repository as it applies changes during a transformation. When these variables are not set, checkpoint commits are attributed to a default identity (`ATX Bot <checkpoint@atx.bot>`). Set both variables to attribute checkpoints to a specific author.

Linux and macOS

```
export ATX_GIT_COMMITTER_NAME="Jane Developer"
export ATX_GIT_COMMITTER_EMAIL="jane@example.com"
```

Windows (PowerShell)

```
$env:ATX_GIT_COMMITTER_NAME="Jane Developer"
$env:ATX_GIT_COMMITTER_EMAIL="jane@example.com"
```

### Trust Settings

Trust settings allow you to pre-approve specific tools and commands to execute without prompts. You can also require explicit permission for specific shell commands regardless of trust level. These settings are configured in the `~/.aws/atx/trust-settings.yaml` file.

The file contains three lists:

- `trustedTools` - Tools that can execute without prompting
- `trustedShellCommands` - Shell commands that can execute without prompting
- `alwaysPromptCommands` - Shell command patterns that require explicit permission unless overridden by `trustedShellCommands`, regardless of the `-t` flag or session trust. These patterns are not enforced in non-interactive mode (`-x`).

**Default trusted tools:**

- `file_read`
- `get_transformation_from_registry`
- `list_available_transformations_from_registry`

**Editing trust settings:**

You can manually edit the trust-settings.yaml file to add or remove trusted tools and commands. Both `trustedShellCommands` and `alwaysPromptCommands` support glob wildcard patterns using `*`.

###### Note

If a command matches both lists, `trustedShellCommands` takes priority.

The following describes each command list and provides examples:

- `trustedShellCommands` - Commands matching these patterns execute without prompting, bypassing all other guardrails. Patterns are matched against the full command string.

Examples:

    + `cd *` - Matches compound commands starting with cd
    + `*&&*` - Trusts all commands with && operators

- `alwaysPromptCommands` - Commands matching these patterns require explicit permission unless overridden by `trustedShellCommands`, regardless of the `-t` flag or session trust. These patterns are not enforced in non-interactive mode (`-x`). Patterns are matched against each sub-command in compound expressions (`&&`, `||`, command substitutions).

Examples:

    + `rm -rf *` - Always prompts for recursive force-delete commands
    + `sudo *` - Always prompts for commands run with sudo
    + `find * -exec *` - Always prompts for find commands with -exec

**Session-level trust:**

During interactive prompts, you can choose:

- `(y)es` - Execute once
- `(n)o` - Deny
- `(t)rust` - Trust for the current session only

Session-level trust settings are temporary and reset when the CLI restarts, providing temporary approval without permanently modifying trust-settings.yaml.

###### Note

Session trust is not available for commands matching your `alwaysPromptCommands` list.

### Model Context Protocol (MCP) Servers

The AWS Transform CLI supports Model Context Protocol (MCP) servers, which extend its functionality with additional tools.

**Configuration:**

Configure MCP servers in the `~/.aws/atx/mcp.json` file. The AWS Transform CLI supports two types of MCP servers: local command-based servers and remote HTTP servers.

**Local command-based servers:**

Local servers run as child processes on your machine. Configure them with the `command` property:

```
{
  "mcpServers": {
    "my-local-server": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"]
    }
  }
}
```

**Remote HTTP servers:**

Remote servers connect to MCP servers hosted at an HTTP or HTTPS URL. Configure them with the `url` property:

```
{
  "mcpServers": {
    "my-remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MCP_API_TOKEN}"
      }
    }
  }
}
```

The `headers` property is optional and supports environment variable expansion using `${VAR_NAME}` syntax. This allows you to store sensitive values like API tokens in environment variables rather than in the configuration file.

**Configuration properties:**

Local command-based servers support the following properties:

- `command` (required) - The command to run the server
- `args` (optional) - Array of command-line arguments
- `env` (optional) - Environment variables to pass to the server process

Remote HTTP servers support the following properties:

- `url` (required) - The HTTP or HTTPS URL of the remote MCP server
- `headers` (optional) - HTTP headers to include in requests, with support for `${VAR_NAME}` environment variable expansion

**Managing MCP servers:**

View list of configured MCP servers:

```
atx mcp tools
```

List available tools offered by a specific MCP server:

```
atx mcp tools --server <server-name>
```

**Usage tracking:**

The CLI automatically tracks MCP tool usage during transformation executions. Usage statistics are persisted as `mcp_usage.json` in the conversation directory alongside `metadata.json`. The file records per-tool metrics for each execution, including:

- Number of invocations per tool
- Number of errors per tool
- Total execution time per tool
- Last error details (if any)

### Client-Side Skills

Client-side skills are additional capabilities that extend the agent during transformation executions. They allow you to provide custom tools, scripts, and instructions that the agent can use alongside its built-in capabilities.

**Skill discovery directories:**

Skills are discovered from four directories in precedence order. If a skill with the same name exists in multiple directories, the first directory in the list takes priority:

1. `<project>/.aws/atx/skills/` - Project-level, AWS Transform CLI-specific
2. `<project>/.agents/skills/` - Project-level, cross-client (available to any compatible agent tooling)
3. `~/.aws/atx/skills/` - User-level, AWS Transform CLI-specific
4. `~/.agents/skills/` - User-level, cross-client (available to any compatible agent tooling)

The `.aws/atx/skills/` directories are specific to the AWS Transform CLI. The `.agents/skills/` directories are cross-client, meaning skills placed there are available to any compatible agent tooling beyond the AWS Transform CLI.

**Skill directory structure:**

Each skill is a directory containing a `SKILL.md` file with YAML frontmatter:

```
~/.aws/atx/skills/
└── my-skill/
    ├── SKILL.md          # Required: frontmatter + instructions
    ├── references/       # Optional: reference docs the agent can read
    │   └── guide.md
    └── scripts/          # Optional: scripts the agent can execute
        └── validate.py
```

**SKILL.md format:**

```
---
name: my-skill
description: When to use this skill
---
# Skill Title

Instructions for the agent...
```

The `name` field must match the parent directory name.

**Disabling a skill:**

To prevent a skill from being loaded without removing its files, add `disable-model-invocation: true` to the frontmatter:

```
---
name: my-skill
description: When to use this skill
disable-model-invocation: true
---
```

When this property is set, the CLI skips the skill during discovery. The agent cannot see or use the skill unless a transformation definition explicitly instructs it to read the skill file. Use this to temporarily disable a skill, mark it as work-in-progress, or keep reference material intended for human readers only.

###### Note

A disabled skill's files remain on disk. If a transformation definition instructs the agent to read a specific file path, the agent can still access the content. The `disable-model-invocation` property prevents automatic discovery and context injection, not file-system access.

**Skill availability by execution mode:**

- **Exec mode** (`atx custom def exec` with `--code-repository-path`) - Discovers skills from both user-level and project-level directories.
- **Interactive mode** (`atx`) - Only user-level skills are discovered initially. When you provide a code repository path during the session, project-level skills are also loaded.

**Verifying skill discovery:**

Check the CLI's debug log after a run to verify which skills were discovered:

Linux and macOS

```
grep -i "skill" ~/.aws/atx/logs/debug.log | tail -20
```

Windows (PowerShell)

```
Select-String -Pattern "skill" "$env:USERPROFILE\.aws\atx\logs\debug.log" | Select-Object -Last 20
```

Skills that fail validation are skipped with a warning in the debug logs.

###### Note

Client-side skills require CLI version 2.0 or later.

#### Choosing Between Project-Level and User-Level Skills

Where you place a skill determines who benefits from it and when it activates.

**Project-level skills** (`<project>/.aws/atx/skills/`):

Commit these to version control so every team member running transformations against the repository automatically discovers them. Use project-level skills for:

- Repository-specific compliance checks (Dockerfile rules, Terraform policies, migration safety validators)
- Organization coding standards that apply to this codebase (observability patterns, error handling, naming conventions)
- Build or test scripts unique to the project (custom linters, architecture fitness functions)
- API migration guides for internal libraries used in this repository

**User-level skills** (`~/.aws/atx/skills/`):

These remain on your machine and activate during all transformations regardless of which repository you target. Use user-level skills for:

- Personal workflow tools (changelog generators, commit message formatters)
- Cross-project preferences (preferred test patterns, documentation style reminders)
- License compliance checks that your organization requires across all repositories
- Coverage thresholds or quality gates you enforce on every codebase you work with

**Tips for effective skills:**

- Write clear `description` fields in your `SKILL.md` frontmatter. The agent uses this field to decide when a skill is relevant.
- Exit validation scripts with code 0 on success and non-zero on failure. The agent interprets exit codes to determine compliance.
- Print clear, actionable error messages in scripts. The agent reads output to understand what to fix.
- Place skills in the cross-client directory (`.agents/skills/`) at either level to share them with other AI development tools beyond the AWS Transform CLI.

#### Client-Side Skill Examples

These examples show two common patterns: a script-based validation skill and a reference-only skill.

##### Example: Dockerfile Compliance Checker (Script-Based)

This skill validates Dockerfiles against security and operational best practices. It uses a validation script that the agent runs before and after making changes.

**Directory structure:**

```
.aws/atx/skills/
└── dockerfile-compliance/
    ├── SKILL.md
    ├── scripts/
    │   └── lint_dockerfile.sh
    └── references/
        └── dockerfile-best-practices.md
```

**SKILL.md:**

```
---
name: dockerfile-compliance
description: Validates Dockerfiles against security and operational best practices
---
# Dockerfile Compliance Checker

When a transformation creates or modifies Dockerfiles, run the compliance checker.

## When to use

- After creating a new Dockerfile
- After modifying FROM, RUN, USER, or EXPOSE directives
- When containerizing an application as part of a transformation

## How to use

Run: `bash scripts/lint_dockerfile.sh <path-to-Dockerfile>`

If violations are found, consult `references/dockerfile-best-practices.md`
for compliant patterns.
```

The validation script checks for unpinned base image tags, running as root, hardcoded secrets in `ENV` directives, and missing `HEALTHCHECK` definitions. The agent runs the script, fixes violations using patterns from the reference file, and re-runs the script to confirm compliance.

##### Example: API Deprecation Helper (Reference-Only)

This skill guides the agent through replacing deprecated API calls during upgrade transformations. It uses only reference files with no scripts.

**Directory structure:**

```
.aws/atx/skills/
└── api-deprecation-helper/
    ├── SKILL.md
    └── references/
        ├── aws-sdk-v2-to-v3.md
        └── react-class-to-hooks.md
```

**SKILL.md:**

```
---
name: api-deprecation-helper
description: Guides the agent through replacing deprecated API calls with modern equivalents
---
# API Deprecation Helper

When performing upgrade transformations, use this skill to identify and replace
deprecated API calls with their modern equivalents.

## When to use

- During any version upgrade transformation
- When build warnings mention deprecated APIs
- When transforming code that uses legacy patterns

## Process

1. Identify deprecated API calls in the codebase
2. For each deprecated call, find the replacement in `references/`
3. Apply the replacement, preserving the original behavior
4. Verify the replacement compiles and tests pass
```

The reference files contain before-and-after code examples. For instance, `aws-sdk-v2-to-v3.md` maps patterns like `s3.putObject(params).promise()` to the modular v3 equivalent using `S3Client` and `PutObjectCommand`.

### Tags and Organization

You can organize transformations with tags for access control and categorization.

###### Note

Some of these commands require specifying the Amazon Resource Name (ARN) for a Transformation Definition. The ARN structure is: `arn:aws:transform-custom:<region>:<account-id>:package/<td-name>`

**To list tags for a transformation:**

```
atx custom def list-tags --arn <transformation-arn>
```

**To add tags to a transformation:**

```
atx custom def tag --arn <transformation-arn> --tags '{"env":"prod","team":"backend"}'
```

**To remove tags from a transformation:**

```
atx custom def untag --arn <transformation-arn> --tag-keys "env,team"
```

Tags can be used for grouped access control in IAM policies. You can create policies that grant permissions to all transformations with specific tags (e.g., all transformations tagged with `team:frontend` or `environment:production`).

### Logs

AWS Transform CLI maintains three types of logs for troubleshooting and debugging.

**Conversation logs:**

Linux and macOS

```
~/.aws/atx/custom/<conversation_id>/logs/<timestamp>-conversation.log
```

Windows

```
%USERPROFILE%\.aws\atx\custom\<conversation_id>\logs\<timestamp>-conversation.log
```

These logs contain the full conversation history for a specific session.

**Subagent logs:**

Linux and macOS

```
~/.aws/atx/custom/<conversation_id>/logs/subagents/<name>.log
```

Windows

```
%USERPROFILE%\.aws\atx\custom\<conversation_id>\logs\subagents\<name>.log
```

These logs contain output from subagents that the main agent spawns during transformations. You do not need to manage subagents directly.

**Developer debug logs:**

Linux and macOS

```
~/.aws/atx/logs/debug*.log
~/.aws/atx/logs/error.log
```

Windows

```
%USERPROFILE%\.aws\atx\logs\debug*.log
%USERPROFILE%\.aws\atx\logs\error.log
```

These logs provide advanced troubleshooting information for the CLI itself.

###### Note

There may be multiple debug log
files in the logs directory (i.e. debug1.log, debug2.log).
Review and provide all relevant logs for example, ~/.aws/atx/custom/<conversation-id>/\* and ~/.aws/atx/logs/\*, when opening support tickets for faster resolution.

### CLI Updates

Keep your CLI up to date to access new features and improvements.

**To check for updates:**

```
atx update --check
```

**To update to the latest version:**

```
atx update
```

**To update to a specific version:**

```
atx update --target-version <version>
```

## Create Custom Transformations

This section describes how to create, modify, and manage custom transformation definitions.

### Creating a New Transformation

Use the interactive CLI to create a new transformation definition.

**To create a transformation definition**

1. Start the AWS Transform CLI:

```
atx
```

2. Tell the agent you want to create a new transformation.
3. Provide a clear, detailed description of the transformation objective. Include:

   - The source and target state (e.g., "upgrade from version X to version Y")
   - Specific changes required (e.g., "update import statements, replace deprecated methods")
   - Any special considerations or constraints

4. When the agent requests clarification or additional information, provide specific examples and reference materials.
5. Review the initial transformation definition created by the agent.
6. Test the transformation on a sample codebase.
7. Iterate by providing feedback, code fixes, or additional examples.
8. Save the transformation locally or publish it to the registry.

**Best practices for creating transformations:**

- Start with simple, well-defined transformations before attempting complex ones
- Provide comprehensive reference materials including migration guides and code samples
- Test on multiple sample codebases before publishing
- Use deterministic build or validation commands to enable continual learning
- Consider breaking complex transformations into multiple smaller steps
- Mark crucial information with "CRITICAL:" or "IMPORTANT:" in your transformation definitions to ensure the agent prioritizes these requirements
- When you need exact requirements followed (like using a specific command or string value), explicitly specify the complete string in your transformation definitions. You can wrap these in bash quotes to clearly indicate they're terminal commands or literal strings, which reduces variability and ensures consistent execution

### Providing Reference Materials

You can provide reference files to AWS Transform custom by specifying file paths during the conversation. These files are stored in the `references/` folder of the transformation definition.

Recommended types of reference files:

- Before/after example code
- Documentation for APIs, libraries, or features involved
- Human-readable migration guides

**To provide a reference file:**

```
Take a look at the documentation here: /path/to/migration-guide.md
```

You can also provide a directory containing multiple reference files:

```
Take a look at the docs we have here: /path/to/docs/
```

###### Note

Only text-based files (.md, .html, .txt, code files) are supported. Binary files, images, and
rich text files (e.g., .pdf, .png, .docx) are not currently supported. It is
often possible to extract the text content and use that as reference. If you
have many small text files, consider concatenating them into few
descriptively-named files. There is a limit of 10MB total for all
files.

### Modifying an Existing Transformation

You can modify custom transformations both before and after saving them as drafts or publishing them. You cannot modify AWS-managed transformations. If you need to customize them, you can provide additional context using the config file.

**To modify an existing transformation**

1. Start the AWS Transform CLI:

```
atx
```

2. Tell the agent you want to modify an existing transformation.
3. Choose whether to:

   - Provide a file path to a locally stored transformation (i.e. not a saved draft or published)
   - Request the list of transformations from the registry

4. If choosing from the registry, select the transformation you want to modify.
5. Work with the agent to describe the changes you want to make.
6. Test the updated transformation on a sample codebase.
7. Publish your updates to the registry if desired.

### Publishing and Managing Transformations

You can publish and manage your transformations using the interactive experience or with the following commands.

**To save a transformation as a draft:**

```
atx custom def save-draft -n my-transformation --description "Description of the transformation" --sd ./transformation-directory
```

**To publish a transformation:**

```
atx custom def publish -n my-transformation --description "Description of the transformation" --sd ./transformation-directory
```

**To list available transformations:**

```
atx custom def list
```

**To download a transformation definition:**

```
atx custom def get -n my-transformation
```

This downloads the transformation definition to your current working directory. You can specify a target directory with the `--td` flag and a version with the `--tv` flag.

**To delete a transformation definition:**

```
atx custom def delete -n my-transformation
```

###### Important

This permanently deletes the specified transformation definition from your account.

### Managing Transformation Versions

AWS Transform custom maintains versions of your transformation definitions. You can specify a version when executing or downloading a transformation.

**To execute a specific version:**

```
atx custom def exec -n my-transformation --tv v1 -p ./my-project
```

**To download a specific version:**

```
atx custom def get -n my-transformation --tv v1
```

If no version is specified, the latest version is used.
