# sam remote test-event

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote test-event` command.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam remote test-event` command, see
  [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md "using-sam-cli-remote-test-event.md").
  The `sam remote test-event` command interacts with shareable test events in the Amazon EventBridge schema registry.

## Usage

```
`$` `sam remote test-event `<options> <subcommand>``
```

## Options

`--help, -h`

Show the help message and exit.

## Subcommands

`delete`

Delete a shareable test event from the EventBridge schema registry. For more reference information, see [sam remote test-event delete](sam-cli-command-reference-remote-test-event-delete.md "sam-cli-command-reference-remote-test-event-delete.md").

`get`

Get a shareable test event from the EventBridge schema registry. For more reference information, see [sam remote test-event get](sam-cli-command-reference-remote-test-event-get.md "sam-cli-command-reference-remote-test-event-get.md").

`list`

List existing shareable test events for an AWS Lambda function. For more reference information, see [sam remote test-event list](sam-cli-command-reference-remote-test-event-list.md "sam-cli-command-reference-remote-test-event-list.md").

`put`

Save an event from a local file to the EventBridge schema registry. For more reference information, see [sam remote test-event put](sam-cli-command-reference-remote-test-event-put.md "sam-cli-command-reference-remote-test-event-put.md").
