

# sam local execution
<a name="sam-cli-command-reference-sam-local-execution"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local execution` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam local execution` command allows you to manage and inspect local durable function executions during development and testing.

**Note**  
These commands may not require access to AWS credentials.

## Usage
<a name="sam-cli-command-reference-sam-local-execution-usage"></a>

```
$ sam local execution {{<subcommand>}} {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-local-execution-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-local-execution-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-local-execution-subcommands"></a>

`get`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-get"></a>
Get details of a durable function execution. For more information, see [sam local execution get](sam-cli-command-reference-sam-local-execution-get.md).

`history`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-history"></a>
Get execution history of a durable function execution. For more information, see [sam local execution history](sam-cli-command-reference-sam-local-execution-history.md).

`stop`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-stop"></a>
Stop a durable function execution. For more information, see [sam local execution stop](sam-cli-command-reference-sam-local-execution-stop.md).