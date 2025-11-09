|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# reviewResults

## Description

The `reviewResults` command allows you to approve or reject multiple assignments from
a file. You use the output file from [getResults](CLTReference_GetResultsCommand.md "CLTReference_GetResultsCommand.md")
to specify which assignments to reject. All other assignments are approved.

###### To use the reviewResults command

1. Run [getResults](CLTReference_GetResultsCommand.md "CLTReference_GetResultsCommand.md").
2. Open the output file.
3. For each assignment you want to reject, type any character in the "reject" column for that assignment.
4. Specify the file in the `-resultsfile` argument for the `reviewResults` command.
5. Run the `reviewResults` command.

###### Important

Any mark in the "reject" column for an assignment causes the assignment to be rejected. Any unmarked assignments
are accepted.

## Arguments

The following table describes the arguments for the `reviewResults` command.

| Name                      | Description                                                                                                                                                                                                                                                       | Required |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-help` or `-h`           | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                         | No       |
| `-resultsfile [filename]` | Specifies the output file from<br>[getResults](CLTReference_GetResultsCommand.md "CLTReference_GetResultsCommand.md") in which<br>you have marked the assignments to reject. All unmarked assignments are approved.<br>Example: `-resultsfile helloworld.results` | Yes      |
| `-sandbox`                | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                      | No       |

## Example

The following examples for Unix and Windows show how to use the `reviewResults` command.

### Unix

The following example demonstrates how to call this command from Unix.

```

./reviewResults.sh  -resultsfile survey.results

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

reviewResults -resultsfile survey.results

```

## Output

This example produces output similar to the following:

```

[BWZZVVYNNYKZ6QZT4V00QHRZNS93BANZ7ZZ2AW50] Assignment successfully approved
[5W48WR9T5X2ZYVZYNS7Z92QZ2VYWNZ1EYSWY3X4Z] Assignment successfully approved
[JYVZ4GXZ0XYZNEZ29350XXX0VR986J4YP6ZH7WZ0] Assignment successfully approved
[M0ZZXFC0J8KP56YVNWM0A0KZSCYA3YFZPJRNGR8Z] Assignment successfully approved
[1Z0ZHS5GGYQWWA83XVE05KZ4RSY233CZ0G91XAJZ] Assignment successfully approved

Assignments approved: 5/5 (100%)
Assignments rejected: 0/5 (0%)
Assignments failed: 0/5 (0%)

```

## Related Commands

- [approveWork](CLTReference_ApproveWorkCommand.md "CLTReference_ApproveWorkCommand.md")
- [rejectWork](CLTReference_RejectWorkCommand.md "CLTReference_RejectWorkCommand.md")
