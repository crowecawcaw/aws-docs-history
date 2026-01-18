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

**Non-Interactive/Headless Mode**

Use `atx custom def exec -n <transformation-name> -p <path> -x -t` for full automation. The `-x` flag enables non-interactive mode, and the `-t` flag automatically trusts all tools without prompting.

This mode is designed for CI/CD pipeline integration and bulk execution where no human intervention is available or desired.

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

The `-t` or `--trust-all-tools` flag automatically approves all tool executions without prompting and bypasses all security guardrails. This is required for a fully autonomous experience but not required to execute the transformation. Use with caution in production environments.

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

**ATX_SHELL_TIMEOUT**

Override the default timeout for shell commands (900 seconds/15 minutes).

```
export ATX_SHELL_TIMEOUT=1800  # 30 minutes
```

This is useful for large codebases or long-running build processes.

**ATX_DISABLE_UPDATE_CHECK**

Disable automatic version checks and update notifications during command execution.

```
export ATX_DISABLE_UPDATE_CHECK=true
```

### Trust Settings

Trust settings allow you to pre-approve specific tools and commands to execute without prompts. These settings are configured in the `~/.aws/atx/trust-settings.yaml` file.

The file contains two lists:

- `trustedTools` - Tools that can execute without prompting
- `trustedShellCommands` - Shell commands that can execute without prompting

**Default trusted tools:**

- `file_read`
- `get_transformation_from_registry`
- `list_available_transformations_from_registry`

**Editing trust settings:**

You can manually edit the trust-settings.yaml file to add or remove trusted tools and commands. The `trustedShellCommands` list supports wildcard patterns using `*` for flexible command matching.

Examples:

- `cd *` - Matches compound commands starting with cd
- `*&&*` - Trusts all commands with && operators

**Session-level trust:**

During interactive prompts, you can choose:

- `(y)es` - Execute once
- `(n)o` - Deny
- `(t)rust` - Trust for the current session only

Session-level trust settings are temporary and reset when the CLI restarts, providing temporary approval without permanently modifying trust-settings.yaml.

### Model Context Protocol (MCP) Servers

The AWS Transform CLI supports Model Context Protocol (MCP) servers, which extend its functionality with additional tools.

**Configuration:**

Configure MCP servers in the `~/.aws/atx/mcp.json` file.

**Managing MCP servers:**

View list of configured MCP servers:

```
atx mcp tools
```

List available tools offered by a specific MCP server:

```
atx mcp tools --server <server-name>
```

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

AWS Transform CLI maintains two types of logs for troubleshooting and debugging.

**Conversation logs:**

Location: `~/.aws/atx/custom/<conversation_id>/logs/<timestamp>-conversation.log`

These logs contain the full conversation history for a specific session.

**Developer debug logs:**

Locations:

- `~/.aws/atx/logs/debug*.log`
- `~/.aws/atx/logs/error.log`

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

You can provide reference files to AWS Transform custom by specifying file paths during the conversation.

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
