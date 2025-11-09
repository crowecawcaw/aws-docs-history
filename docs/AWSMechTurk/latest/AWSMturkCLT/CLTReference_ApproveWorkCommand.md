|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# approveWork

## Description

The `approveWork` command approves assignments Workers have submitted to
Amazon Mechanical Turk. To specify the assignments to approve you can:

- Obtain the assignment IDs from a call to
  [getResults](CLTReference_GetResultsCommand.md "CLTReference_GetResultsCommand.md") then call the
  `approveWork` command and use the
  `assignment` argument to list the IDs. When you use this argument,
  you are prompted to provide optional comments that the Worker can see in the **Status**
  section of the web site.
- Use the file that a call the
  `getResults` returns as the
  `approvefile` argument.
  You can provide optional comments for Workers in this file. For information about the format of this file, see
  [Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").
- Provide a path to the `.success` file that a call to
  [loadHITs](CLTReference_LoadHITsCommand.md "CLTReference_LoadHITsCommand.md") returns. The
  `approveWork` command attempts to approve all assignments for all HITs in the
  `.success` file.

When you use this command, it initiates two payments from your Requester account. Amazon Mechanical
Turk pays the reward specified in the HIT to the Worker who submitted the assignment, and also debits
your account for any fees. If your Requester account does not have adequate funds for these payments,
this command returns an error.

## Arguments

The following table describes the arguments for the `approveWork` command.

| Name                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required    |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-approvefile [filename]`     | The name of a text file that contains a list of assignment IDs and, optionally, approval comments.<br>For information about this file, see \*The approve file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if neither the `-assignment` argument nor the<br>`-successfile` argument is specified.<br>Example: `-approvefile helloworld_approve.txt`                                                                                                                       | Conditional |
| `-assignment [assignment ID]` | The assignment to approve. Multiple assignments IDs are comma separated.<br>Condition: Required if neither the `-approvefile` argument nor the<br>`-successfile` argument is specified.<br>Example: `-assignment SYSZH6HTMKFG2ZDECWS0`                                                                                                                                                                                                                                                                                                          | Conditional |
| `-force`                      | Specifies \*not<br>• to prompt for manual confirmation before performing the operation.<br>Only advanced developers should use this argument.<br>Example: `-force`                                                                                                                                                                                                                                                                                                                                                                              | No          |
| `-help` or `-h`               | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No          |
| `-sandbox`                    | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                                                                                                                                                                                       | No          |
| `-successfile [path]`         | The path to the `.success` file that a call to<br>[loadHITs](CLTReference_LoadHITsCommand.md "CLTReference_LoadHITsCommand.md") returned. This argument<br>attempts to approve all assignments for all HITs in the file. For information about this file, see<br>\*The success file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if neither the `-approvefile` argument nor the<br>`-assignment` argument is specified.<br>Example: `-approvefile helloworld_approve.txt` | Conditional |

## Example

The following examples for Unix and Windows show how to use the
`approveWork` command. The examples
approve one assignment in the file `approval.txt`.

### Unix

The following example demonstrates how to call this command from Unix.

```

./approveWork.sh -approvefile approval.txt

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

approveWork -approvefile approval.txt

```

## Output

These examples produce the following output.

```

--- Starting approval ---
[62145TS44X94HHYGW0PZK2CP0E1K9T1PR8Z42WEZ] Assignment successfully approved
for HIT 62145TS44X94HHYGW0PZ
--- Finished approval ---
  1 assignments approved.
  0 assignments failed to be approved.

```

## Related Commands

- [rejectWork](CLTReference_RejectWorkCommand.md "CLTReference_RejectWorkCommand.md")
