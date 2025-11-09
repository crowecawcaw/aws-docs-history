|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# blockWorker

## Description

The `blockWorker` command blocks a Worker from working on your HITs.

## Arguments

The following table describes the arguments for the `blockWorker` command.

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                                        | Required |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-help` or `-h`         | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                          | No       |
| `-reason [string]`      | The reason why the Worker is being blocked. This reason is logged in our system for auditing<br>purposes and can be used to determine if corrective action against the Worker is necessary.<br>Enclose the reason string in quotation marks.<br>Example: `-reason "After several warnings, the Worker continued to submit answers without<br>reading the instructions carefully."` | Yes      |
| `-sandbox`              | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                          | No       |
| `-workerid [Worker ID]` | The ID of the Worker you want to block.<br>Example: `-workerid A3C4G8DMXFG5PQ`                                                                                                                                                                                                                                                                                                     | Yes      |

## Example

The following examples for Unix and Windows show how to use the `blockWorker` command.

### Unix

The following example demonstrates how to call this command from Unix. You must
write this command on a single line. It is divided into multiple lines in this example for readability.

```

./blockWorker.sh -workerid A3C4G8DMXFG5PQ -reason "After several warnings, the Worker continued to
submit answers without reading the instructions carefully."

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows. You should
write this command on a single line. It is divided into multiple lines in this example for readability.

```

blockWorker -workerid A3C4G8DMXFG5PQ -reason "After several warnings, the Worker continued to
submit answers without reading the instructions carefully."

```

## Output

These examples produce the following output.

```

Blocked A3C4G8DMXFG5PQ with reason: After several warnings, the Worker continued to submit answers without reading the instructions carefully.

```

## Related Commands

- [unblockWorker](CLTReference_UnblockWorkerCommand.md "CLTReference_UnblockWorkerCommand.md")
