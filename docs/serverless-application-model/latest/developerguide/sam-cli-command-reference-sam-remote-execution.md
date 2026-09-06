

# sam remote execution
<a name="sam-cli-command-reference-sam-remote-execution"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote execution` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam remote execution` command allows you to manage and inspect remote durable function executions running in AWS Lambda.

**Note**  
These commands require access to AWS credentials.

## Usage
<a name="sam-cli-command-reference-sam-remote-execution-usage"></a>

```
$ sam remote execution {{<subcommand>}} {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-remote-execution-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-remote-execution-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-remote-execution-subcommands"></a>

`get`  <a name="sam-cli-command-reference-sam-remote-execution-subcommands-get"></a>
Get details of a durable execution. For more information, see [sam remote execution get](sam-cli-command-reference-sam-remote-execution-get.md).

`history`  <a name="sam-cli-command-reference-sam-remote-execution-subcommands-history"></a>
Get execution history of a durable function execution. For more information, see [sam remote execution history](sam-cli-command-reference-sam-remote-execution-history.md).

`stop`  <a name="sam-cli-command-reference-sam-remote-execution-subcommands-stop"></a>
Stop a durable function execution. For more information, see [sam remote execution stop](sam-cli-command-reference-sam-remote-execution-stop.md).