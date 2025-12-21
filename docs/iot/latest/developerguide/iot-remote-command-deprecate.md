# Deprecate a command resource

Deprecate commands to indicate they are outdated and should not be used. For example, deprecate commands no longer actively maintained or when creating newer commands with the same ID but different payloads.

## Key

considerations

Important considerations when deprecating commands:

- Deprecating a command does not delete it. You can retrieve the command using its ID and restore it for reuse.
- Attempting to start new executions on deprecated commands generates an error, preventing use of outdated commands.
- To execute a deprecated command, first restore it. After restoration, the command becomes available for regular use and execution on target devices.
- If you deprecate a command while executions are in progress, they continue running until completion. You can still retrieve execution status.

## Deprecate a command resource

(console)

To deprecate a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and perform
the following steps.

1. Choose the command that you want to deprecate, and then under
   **Actions**, choose
   **Deprecate**.
2. Confirm that you want to deprecate the command and then choose
   **Deprecate**.

## Deprecate a command resource

(CLI)

Mark commands as deprecated using the `update-command` CLI. You must deprecate a command before deletion. To use a deprecated command, restore it first.

```
aws iot update-command \
    --command-id `<command-id>` \
    --deprecated
```

For example, if you deprecated the
`ACSwitch` command that you updated in the
example above, the following code shows a sample output of running the
command.

```
{
    "commandId": "turnOffAc",
    "deprecated": true,
    "lastUpdatedAt": "2024-05-09T23:16:51.370000-07:00"
}
```

## Check deprecation time and

status

Use the `GetCommand` API to determine if a command is deprecated and when it was last deprecated.

```
aws iot get-command --command-id `<turnOffAC>`
```

This command generates a response containing command information, including creation and deprecation timestamps from the last updated field. This helps determine command lifetime and whether to delete or reuse it. The following shows a sample response for the `turnOffAc` command:

```
{
    "commandId": "turnOffAC",
    "commandArn": "arn:aws:iot:us-east-1:123456789012:command/turnOffAC",
    "namespace": "AWS-IoT",
    "payload": {
        "content": "testPayload.json",
        "contentType": "application/json"
    },
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "lastUpdatedAt": "2024-05-09T23:16:51.370000-07:00",
    "deprecated": false
}
```

## Restore a command resource

To use or send the `ACSwitch` command to your device, restore it first.

To restore a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console, choose the
command that you want to restore, and then under **Actions**,
choose **Restore**.

To restore a command using the AWS IoT Core API or the AWS CLI, use the
`UpdateCommand` API operation or the `update-command` CLI.
The following code shows a sample request and response.

```
aws iot update-command \
    --command-id `<command-id>`
    --no-deprecated
```

The following code shows a sample output.

```
{
    "commandId": "ACSwitch",
    "deprecated": false,
    "lastUpdatedAt": "2024-05-09T23:17:21.954000-07:00"
}
```
