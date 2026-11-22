

# Command Reference

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
| -n | --transformation-name | <name or ARN> | The name of a transformation definition in your registry, or the ARN of a transformation definition shared with your account | 
| -x | --non-interactive | - | Runs the transformation with no user assistance | 
| -t | --trust-all-tools | - | Trusts all tools (no tool prompts) | 
| -d | --do-not-learn | - | Opt out of lesson extraction from this execution. Has no other effect for shared transformation definitions, whose runs don't add lessons to your account. Can't be used with --share-learnings. | 
| - | --share-learnings | - | For a shared transformation definition only: contribute lessons from this run to the owner's transformation definition. Needs the ExecuteWithLearningsAndContribution permission. Can't be used with -d. | 
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

The **Category** column shows whether each transformation definition is an `analysis` or a `remediation` transformation. A transformation definition without a category shows `—`. In `--json` output, the category appears in the `category` field. This field is omitted when no category is set.

Transformation definitions shared with your account appear in a separate **Shared with you** section, which shows the owner account. In `--json` output, they are in a separate `sharedTransformations` array. For more information, see [Accept, run, and download a shared transformation definition](custom-sharing-consumer.md).

**atx custom def get**

Get details of a specific transformation definition.


| Option | Long Form | Parameter | Description | 
| --- | --- | --- | --- | 
| -n | --transformation-name | <name> | The name of the transformation definition, or the ARN of a shared transformation definition. A shared transformation definition can be downloaded only if its share has the ExecuteWithLearningsAndPackageDownload permission. | 
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
| --category | --category | <category> | The category of the transformation definition. Use analysis for transformations that read code and report findings, or remediation for transformations that change code. If you don't specify a category when you publish a new version, the previous version's category is kept. Not applicable with --transformation-version. | 
| --json | --json | - | Output response in JSON format | 
| -h | --help | - | Display help for command | 

**atx custom def save-draft**

Save a transformation definition as a draft in the registry. Drafts expire after 30 days and do not show up in the registry. This command returns the version number of the draft. You must execute and retrieve drafts explicitly using the transformation name and version number.

```
atx custom def save-draft -n <transformation-name> --description "Description" --sd <directory>
```

To set the category of the transformation definition, add `--category analysis` or `--category remediation`.

## Lesson Commands
<a name="custom-knowledge-item-commands"></a>

**atx custom def learnings**

Open an interactive session to view and manage the lessons a transformation definition has learned from previous runs. Browse lessons by category, view lesson detail, and archive, restore, or delete lessons.

```
atx custom def learnings -n {{<transformation-name>}}
```

## Share Commands
<a name="custom-share-commands"></a>

Share transformation definitions with other AWS accounts, OUs, or your organization through AWS RAM. Share commands use the Region from `AWS_REGION` or your AWS profile. No share command takes `--region`. For more information, see [Sharing transformation definitions across AWS accounts](custom-sharing.md).

**atx custom def share create**

Share a published transformation definition with one target.

```bash
atx custom def share create -n {{transformation-name}} --target {{target}} [--managed-policy {{name}}]
```

The following table describes the options for `share create`.


| Option | Description | 
| --- | --- | 
| -n, --transformation-name | The name of a published transformation definition in your account | 
| --target | A 12-digit AWS account ID, an organization ARN, or an OU ARN | 
| --managed-policy | The AWS RAM managed permission for the share: Execute (default), ExecuteWithLearnings, ExecuteWithLearningsAndContribution, or ExecuteWithLearningsAndPackageDownload | 
| --json | Output response in JSON format | 

**atx custom def share list**

List the shares that you own, or the shares and invitations for your account.

```bash
atx custom def share list --outgoing    # Shares you own
atx custom def share list --incoming    # Invitations and accepted shares
```

The following table describes the options for `share list`.


| Option | Description | 
| --- | --- | 
| --outgoing | List the shares that you own. One of --outgoing or --incoming is required. | 
| --incoming | List invitations waiting for you and the shares that you accepted. One of --outgoing or --incoming is required. | 
| --json | Output response in JSON format | 

**atx custom def share update**

Change the managed permission of a share that you own.

```bash
atx custom def share update {{share-id}} --managed-policy {{name}}
```

The following table describes the options for `share update`.


| Option | Description | 
| --- | --- | 
| --managed-policy | Required. The new AWS RAM managed permission for the share. | 
| --json | Output response in JSON format | 

**atx custom def share revoke**

Revoke a share that you own. The consumer loses access.

```bash
atx custom def share revoke {{share-id}} [--yes]
```

**atx custom def share accept**

Accept an invitation to a share.

```bash
atx custom def share accept {{share-id}} [--yes]
```

**atx custom def share decline**

Decline an invitation to a share.

```bash
atx custom def share decline {{share-id}} [--yes]
```

The `revoke`, `accept`, and `decline` commands take the following options. `{{share-id}}` can be the share ID (a UUID) or the share ARN.


| Option | Description | 
| --- | --- | 
| --yes | Skip the confirmation prompt | 
| --json | Output response in JSON format | 

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