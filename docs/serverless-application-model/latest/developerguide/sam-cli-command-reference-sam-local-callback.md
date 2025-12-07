# sam local callback

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam local callback` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

The `sam local callback` command allows you to send callbacks to local durable function executions during development and testing.

## Usage

```
`$` `sam local callback `<subcommand>` `<options>``
```

## Options

`--help, -h`

Show this message and exit.

## Subcommands

`succeed`

Send a success callback to a durable function execution. For more information, see
[sam local callback succeed](sam-cli-command-reference-sam-local-callback-succeed.md "sam-cli-command-reference-sam-local-callback-succeed.md").

`fail`

Send a failure callback to a durable function execution. For more information, see
[sam local callback fail](sam-cli-command-reference-sam-local-callback-fail.md "sam-cli-command-reference-sam-local-callback-fail.md").

`heartbeat`

Send a heartbeat callback to a durable function execution. For more information, see
[sam local callback heartbeat](sam-cli-command-reference-sam-local-callback-heartbeat.md "sam-cli-command-reference-sam-local-callback-heartbeat.md").
