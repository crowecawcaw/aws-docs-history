# Command Reference

This section provides a comprehensive reference of all AWS Transform custom CLI commands.

## Interactive Commands

**atx**

Start an interactive conversation with the AWS Transform CLI.

```
atx                           # Start new conversation
atx --resume                  # Resume most recent conversation
atx --conversation-id <id>    # Resume specific conversation
atx -t                        # Start with all tools trusted
```

## Transformation Definition Commands

**atx custom def exec**

Execute a transformation definition on a code repository.

| Option | Long Form                  | Parameter   | Description                                                              |
| ------ | -------------------------- | ----------- | ------------------------------------------------------------------------ |
| `-p`   | `--code-repository-path`   | `<path>`    | Path to the code repository to transform. For current directory, use "." |
| `-c`   | `--build-command`          | `<command>` | Command to run when building repository                                  |
| `-n`   | `--transformation-name`    | `<name>`    | Name of the transformation definition in the registry                    |
| `-x`   | `--non-interactive`        | -           | Runs the transformation with no user assistance                          |
| `-t`   | `--trust-all-tools`        | -           | Trusts all tools (no tool prompts)                                       |
| `-d`   | `--do-not-learn`           | -           | Opt out of allowing knowledge item extraction from this execution        |
| `-g`   | `--configuration`          | `<config>`  | Path to config file (JSON or YAML) or key=value pairs                    |
| `--tv` | `--transformation-version` | `<version>` | Version of the transformation definition to use                          |
| `-h`   | `--help`                   | -           | Display help for command                                                 |

**atx custom def list**

List available transformation definitions.

```
atx custom def list
atx custom def list --json    # Output in JSON format
```

**atx custom def get**

Get details of a specific transformation definition.

| Option   | Long Form                  | Parameter     | Description                                                                        |
| -------- | -------------------------- | ------------- | ---------------------------------------------------------------------------------- |
| `-n`     | `--transformation-name`    | `<name>`      | The name of the transformation definition to retrieve                              |
| `--tv`   | `--transformation-version` | `<version>`   | The version of the transformation definition to retrieve                           |
| `--td`   | `--target-directory`       | `<directory>` | The target directory at which to save the transformation definition (default: ".") |
| `--json` | `--json`                   | -             | Output response in JSON format                                                     |
| `-h`     | `--help`                   | -             | Display help for command                                                           |

**atx custom def delete**

Delete a transformation definition permanently.

```
atx custom def delete -n <transformation-name>
```

**atx custom def publish**

Publish a transformation definition to the registry.

| Option          | Long Form                  | Parameter       | Description                                                                                                                      |
| --------------- | -------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `-n`            | `--transformation-name`    | `<name>`        | The name of the transformation definition to publish                                                                             |
| `--tv`          | `--transformation-version` | `<version>`     | The version of the transformation definition to use (not applicable with --description or --source-directory)                    |
| `--sd`          | `--source-directory`       | `<directory>`   | The source directory from which to read the local transformation definition files (not applicable with --transformation-version) |
| `--description` | `--description`            | `<description>` | A description for the transformation definition (not applicable with --transformation-version)                                   |
| `--json`        | `--json`                   | -               | Output response in JSON format                                                                                                   |
| `-h`            | `--help`                   | -               | Display help for command                                                                                                         |

**atx custom def save-draft**

Save a transformation definition as a draft in the registry.

```
atx custom def save-draft -n <transformation-name> --description "Description" --sd <directory>
```

## Knowledge Item Commands

**atx custom def list-ki**

List knowledge items for a transformation definition.

```
atx custom def list-ki -n <transformation-name>
atx custom def list-ki -n <transformation-name> --json
```

**atx custom def get-ki**

Retrieve a knowledge item from a transformation definition.

```
atx custom def get-ki -n <transformation-name> --id <id>
```

**atx custom def delete-ki**

Delete a knowledge item from a transformation definition.

```
atx custom def delete-ki -n <transformation-name> --id <id>
```

**atx custom def update-ki-status**

Update knowledge item status (ENABLED or DISABLED).

```
atx custom def update-ki-status -n <transformation-name> --id <id> --status ENABLED
```

**atx custom def update-ki-config**

Update knowledge item configuration for auto-approval.

```
atx custom def update-ki-config -n <transformation-name> --auto-enabled TRUE
```

**atx custom def export-ki-markdown**

Export all knowledge items for a transformation definition to markdown.

```
atx custom def export-ki-markdown -n <transformation-name>
```

## Tag Commands

**atx custom def list-tags**

List tags for a transformation definition.

```
atx custom def list-tags --arn <transformation-arn>
```

**atx custom def tag**

Add tags to a transformation definition.

```
atx custom def tag --arn <arn> --tags '{"env":"prod","team":"backend"}'
```

**atx custom def untag**

Remove tags from a transformation definition.

```
atx custom def untag --arn <arn> --tag-keys "env,team"
```

## Update Commands

**atx update**

Update the AWS Transform CLI.

```
atx update                    # Update to latest version
atx update --check            # Check for updates only
atx update --target-version <version>  # Update to specific version
```

## MCP Commands

**atx mcp tools**

Manage Model Context Protocol servers.

```
atx mcp tools -s    # View status
atx mcp tools -l    # List tools
atx mcp tools -r    # Refresh
```
