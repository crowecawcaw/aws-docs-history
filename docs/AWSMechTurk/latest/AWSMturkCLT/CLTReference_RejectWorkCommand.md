|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# rejectWork

## Description

The `rejectWork` command rejects assignments submitted by Workers. You
can reject single assignments, or you can specify a file that contains the assignments to reject.

## Arguments

The following table describes the arguments for the `rejectWork` command.

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                               | Required    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-assignment [assignment IDs]` | Specifies the assignment ID to reject. For multiple assignments, separate each assignment ID<br>with a comma.<br>Condition: Required if the `rejectfile` argument is not specified.<br>Example: `-assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z`                                                                                                                    | Conditional |
| `-force`                       | Specifies \*not<br>• to prompt for manual confirmation before performing the reject operation.<br>Only advanced developers should use this argument.<br>Example: `-force`                                                                                                                                                                                                 | No          |
| `-help` or `-h`                | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                 | No          |
| `-rejectfile [filename]`       | Specifies a text file that contains a list of assignment IDs and optional rejection comments.<br>For information about this file, see \*The reject file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if the `assignment` argument is not specified.<br>Example: `-rejectfile helloworld_reject.txt` | Conditional |
| `-sandbox`                     | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                              | No          |

## Example

The following examples for Unix and Windows show how to use the
`rejectWork` command. These examples reject
the specified assignment with no additional comments.

### Unix

The following example demonstrates how to call this command from Unix.

```

./rejectWork.sh -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

rejectWork -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z

```

## Output

These examples produce the following output.

```

You are about to reject 1 assignment(s).
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

If you would like to supply a comment to the worker(s), please type it below then press ENTER.
If not, just hit ENTER:

[0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z] Assignment successfully rejected with comment ()

```
