

# sam local callback
<a name="sam-cli-command-reference-sam-local-callback"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local callback` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam local callback` command allows you to send callbacks to local durable function executions during development and testing.

## Usage
<a name="sam-cli-command-reference-sam-local-callback-usage"></a>

```
$ sam local callback {{<subcommand>}} {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-local-callback-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-local-callback-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-local-callback-subcommands"></a>

`succeed`  <a name="sam-cli-command-reference-sam-local-callback-subcommands-succeed"></a>
Send a success callback to a durable function execution. For more information, see [sam local callback succeed](sam-cli-command-reference-sam-local-callback-succeed.md).

`fail`  <a name="sam-cli-command-reference-sam-local-callback-subcommands-fail"></a>
Send a failure callback to a durable function execution. For more information, see [sam local callback fail](sam-cli-command-reference-sam-local-callback-fail.md).

`heartbeat`  <a name="sam-cli-command-reference-sam-local-callback-subcommands-heartbeat"></a>
Send a heartbeat callback to a durable function execution. For more information, see [sam local callback heartbeat](sam-cli-command-reference-sam-local-callback-heartbeat.md).