

# sam remote callback
<a name="sam-cli-command-reference-sam-remote-callback"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote callback` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam remote callback` command allows you to send callbacks to remote durable function executions running in AWS Lambda.

**Note**  
These commands require access to AWS credentials.

## Usage
<a name="sam-cli-command-reference-sam-remote-callback-usage"></a>

```
$ sam remote callback {{<subcommand>}} {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-remote-callback-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-remote-callback-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-remote-callback-subcommands"></a>

`succeed`  <a name="sam-cli-command-reference-sam-remote-callback-subcommands-succeed"></a>
Send a callback success to a remote durable function execution. For more information, see [sam remote callback succeed](sam-cli-command-reference-sam-remote-callback-succeed.md).

`fail`  <a name="sam-cli-command-reference-sam-remote-callback-subcommands-fail"></a>
Send a callback failure to a remote durable function execution. For more information, see [sam remote callback fail](sam-cli-command-reference-sam-remote-callback-fail.md).

`heartbeat`  <a name="sam-cli-command-reference-sam-remote-callback-subcommands-heartbeat"></a>
Send a callback heartbeat to a remote durable function execution. For more information, see [sam remote callback heartbeat](sam-cli-command-reference-sam-remote-callback-heartbeat.md).