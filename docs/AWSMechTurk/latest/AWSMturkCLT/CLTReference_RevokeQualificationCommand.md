|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# revokeQualification

## Description

The `revokeQualification` command revokes a Qualification from a Worker.

## Arguments

The following table describes the arguments for the `revokeQualification` command.

| Name                                  | Description                                                                                                                                                                                                  | Required |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `-help` or `-h`                       | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                    | No       |
| `-qualtypeid [Qualification Type ID]` | The Qualification Type ID of the Qualification to revoke from the Worker.<br>Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ`                                                                                     | Yes      |
| `-reason [text]`                      | The reason you are revoking the Qualification. The text must be enclosed in quotation marks.<br>Example: `-reason "I'm sorry but your work quality is below acceptable standards."`                          | No       |
| `-sandbox`                            | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your `mturk.properties`<br>file.<br>Example:`-sandbox` | No       |
| `-workerid [Worker ID]`               | The Worker ID of the Worker from whom to revoke the Qualification.<br>Example: `-workerid A3C4G8DMXFG5PQ`                                                                                                    | Yes      |

## Example

The following examples for Unix and Windows show how to use the
`revokeQualification` command. These examples revoke
a Worker's qualification and provide a reason.

### Unix

The following example demonstrates how to call this command from Unix.

```

./revokeQualification.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -reason "I'm sorry but your work quality is below acceptable standards."

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

revokeQualification -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -reason "I'm sorry but your work quality is below acceptable standards."

```

## Output

These examples produce the following output.

```

Revoked qual RWFZTKZ55ZPZXN1C8TDZ from A3C4G8DMXFG5PQ with reason:
I'm sorry but your work quality is below acceptable standards.

```
