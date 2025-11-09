|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# getBalance

## Description

The `getBalance` command retrieves the available balance in your Amazon Mechanical
Turk account. This amount is your current balance minus any outstanding payments, fees, or bonuses you owe.

## Arguments

The following table describes the arguments for the `getBalance` command.

| Name            | Description                                                                                                                                                                                                                                                             | Required |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `‑help` or `‑h` | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                               | No       |
| `‑sandbox`      | Runs this command in the Amazon Mechanical Turk sandbox and gets your sandbox<br>account balance. This amount is always $10000.00. This argument takes precedence even<br>if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox` | No       |

## Example

The following examples for Unix and Windows show how to use the `getBalance`
command.

### Unix

The following example demonstrates how to call this command from Unix.

```

./getBalance.sh

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

getBalance

```

## Output

This example produces output similar to the following.

```

Your account balance: $819.45

```
