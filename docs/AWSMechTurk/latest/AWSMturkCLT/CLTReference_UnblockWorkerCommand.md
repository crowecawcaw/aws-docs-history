|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# unblockWorker

## Description

The `unblockWorker` command unblocks a Worker who has been blocked from working on
your HITs.

## Arguments

The following table describes the arguments for the `unblockWorker` command.

| Name                    | Description                                                                                                                                                                                                             | Required |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-help` or `-h`         | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                               | No       |
| `-reason`               | The reason why you are unblocking the Worker. This reason is logged in our system for auditing<br>purposes. Enclose this string in quotation marks.<br>Example: `-reason "Made a mistake. Blocked the wrong Worker ID"` | Yes      |
| `-sandbox`              | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`               | No       |
| `-workerid [worker ID]` | The ID of the Worker to unblock.<br>Example: `-workerid A3C4G8DMXFG5PQ`                                                                                                                                                 | Yes      |

## Example

The following examples for Unix and Windows show how to use the
`unblockWorker` command. These examples unblock a
specified Worker.

### Unix

The following example demonstrates how to call this command from Unix.

```

./unblockWorker.sh -workerid A3C4G8DMXFG5PQ -reason "Made a mistake. Blocked the wrong Worker ID."

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

unblockWorker -workerid A3C4G8DMXFG5PQ -reason "Made a mistake. Blocked the wrong Worker ID."

```

## Output

These examples produce the following output.

```

Unblocked A3C4G8DMXFG5PQ with reason:  Made a mistake. Blocked the wrong Worker ID.

```
