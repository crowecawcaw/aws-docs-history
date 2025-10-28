# Deprecate a command resource

You can deprecate a command to indicate that it is out of date and should not be used.
For example, you might deprecate a command that is no longer actively maintained, or you
might want to create a newer command with the same command ID but uses different payload
information.

## Key

considerations

Following are some important considerations with deprecating a command:

- When you deprecate a command, it is not deleted. You can still retrieve
  the command using it's command ID and restore it if you want to reuse the
  command.
- If you attempt to start a new command execution on your target device for
  a command that has been deprecated, it generates an error, which prevents
  you from using out-of-date commands.
- To execute a deprecated command on your target device, you must first
  restore it. Once restored, the command becomes available and it can be used
  as a regular command and you can perform command executions on the target
  device.
- If you deprecate a command while the command executions are in progress,
  the executions will continue to run on the target device until they are
  completed. You can also retrieve the status of the command
  executions.

## Deprecate a command resource

(console)

To deprecate a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and perform
the following steps.

1. Choose the command that you want to deprecate, and and then under
   **Actions**, choose
   **Deprecate**.
2. Confirm that you want to deprecate the command and then choose
   **Deprecate**.

## Deprecate a command resource

(CLI)

You can mark a command as deprecated using the `update-command` CLI.
You must first deprecate a command before it can be deleted. Once a command has been
deprecated, if you want to use it such as for sending a command execution to the
target device, you must un-deprecate it.

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

You can use the `GetCommand` API operation to determine whether a
command has been deprecated, and when it was last deprecated.

```
aws iot get-command --command-id `<turnOffAC>`
```

Running this command generates a response that contains information about the
command. You can obtain information as to when when it was created, and when it was
deprecated using the last updated information. This information can help you
determine the lifetime of a command, and whether you want to delete the command or
reuse it. For example, in the `turnOffAc`
example above, he following code shows a sample response.

```
{
    "commandId": "turnOffAC",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/turnOffAC",
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

To use the `ACSwitch` command or to send this command to your device,
you must restore it.

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
