# sam local execution

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam local execution` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

The `sam local execution` command allows you to manage and inspect local durable function executions during development and testing.

###### Note

These commands may not require access to AWS credentials.

## Usage

```
`$` `sam local execution `<subcommand>` `<options>``
```

## Options

`--help, -h`

Show this message and exit.

## Subcommands

`get`

Get details of a durable function execution. For more information, see
[sam local execution get](sam-cli-command-reference-sam-local-execution-get.md "sam-cli-command-reference-sam-local-execution-get.md").

`history`

Get execution history of a durable function execution. For more information, see
[sam local execution history](sam-cli-command-reference-sam-local-execution-history.md "sam-cli-command-reference-sam-local-execution-history.md").

`stop`

Stop a durable function execution. For more information, see
[sam local execution stop](sam-cli-command-reference-sam-local-execution-stop.md "sam-cli-command-reference-sam-local-execution-stop.md").
