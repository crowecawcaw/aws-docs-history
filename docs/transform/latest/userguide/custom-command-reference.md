

# Command Reference
<a name="custom-command-reference"></a>

This section provides a comprehensive reference of all AWS Transform custom CLI commands.

## Interactive Commands
<a name="custom-interactive-commands"></a>

**atx**

Start an interactive conversation with the AWS Transform CLI.

```
atx                           # Start new conversation
atx --resume                  # Resume most recent conversation
atx --conversation-id <id>    # Resume specific conversation
atx -t                        # Start with all tools trusted
```

**Interactive session commands**

The following commands can be typed at the input prompt during an interactive session:
+ `/usage` - Display the accumulated [agent minutes](https://aws.amazon.com/transform/pricing/) for the current session

## Transformation Definition Commands
<a name="custom-transformation-definition-commands"></a>

**atx custom def exec**

Execute a transformation definition on a code repository.


| Option | Long Form | Parameter | Description | 
| --- | --- | --- | --- | 
| -p | --code-repository-path | <path> | Path to the code repository to transform. For current directory, use "." | 
| -c | --build-command | <command> | Command to run when building repository | 
| -n | --transformation-name | <name> | Name of the transformation definition in the registry | 
| -x | --non-interactive | - | Runs the transformation with no user assistance | 
| -t | --trust-all-tools | - | Trusts all tools (no tool prompts) | 
| -d | --do-not-learn | - | Opt out of allowing lesson extraction from this execution | 
| -g | --configuration | <config> | Path to config file (JSON or YAML) or key=value pairs | 
| --tv | --transformation-version | <version> | Version of the transformation definition to use | 
| --limit | --limit | <limit> | Set [Agent Minutes](https://aws.amazon.com/transform/pricing/) budget limit. Transformation exits when limit is reached and can be resumed with an increased limit | 
| -h | --help | - | Display help for command | 

### atx custom def list
<a name="atx-custom-def-list"></a>

List available transformation definitions.

```
atx custom def list
atx custom def list --json    # Output in JSON format
```

**atx custom def get**

Get details of a specific transformation definition.


| Option | Long Form | Parameter | Description | 
| --- | --- | --- | --- | 
| -n | --transformation-name | <name> | The name of the transformation definition to retrieve | 
| --tv | --transformation-version | <version> | The version of the transformation definition to retrieve | 
| --td | --target-directory | <directory> | The target directory at which to save the transformation definition (default: ".") | 
| --json | --json | - | Output response in JSON format | 
| -h | --help | - | Display help for command | 

**atx custom def delete**

Delete a transformation definition permanently.

```
atx custom def delete -n <transformation-name>
```

**atx custom def publish**

Publish a transformation definition to the registry.


| Option | Long Form | Parameter | Description | 
| --- | --- | --- | --- | 
| -n | --transformation-name | <name> | The name of the transformation definition to publish | 
| --tv | --transformation-version | <version> | The version of the transformation definition to use (not applicable with --description or --source-directory) | 
| --sd | --source-directory | <directory> | The source directory from which to read the local transformation definition files (not applicable with --transformation-version) | 
| --description | --description | <description> | A description for the transformation definition (not applicable with --transformation-version) | 
| --json | --json | - | Output response in JSON format | 
| -h | --help | - | Display help for command | 

**atx custom def save-draft**

Save a transformation definition as a draft in the registry. Drafts expire after 30 days and do not show up in the registry. This command returns the version number of the draft. You must execute and retrieve drafts explicitly using the transformation name and version number.

```
atx custom def save-draft -n <transformation-name> --description "Description" --sd <directory>
```

## Lesson Commands
<a name="custom-knowledge-item-commands"></a>

**atx custom def learnings**

Open an interactive session to view and manage the lessons a transformation definition has learned from previous runs. Browse lessons by category, view lesson detail, and archive, restore, or delete lessons.

```
atx custom def learnings -n {{<transformation-name>}}
```

## Tag Commands
<a name="custom-tag-commands"></a>

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
<a name="custom-update-commands"></a>

**atx update**

Update the AWS Transform CLI.

```
atx update                    # Update to latest version
atx update --check            # Check for updates only
atx update --target-version <version>  # Update to specific version
```

## MCP Commands
<a name="custom-mcp-commands"></a>

**atx mcp tools**

Allows clients to view/confirm their MCP tool configurations. Updates to the configurations must be managed directly via the file \~/.aws/atx/mcp.json 

```
atx mcp tools     # View list of MCP servers
atx mcp tools -s    # List tools for the specified server
```