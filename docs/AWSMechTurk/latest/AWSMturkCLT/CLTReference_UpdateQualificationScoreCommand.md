|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# updateQualificationScore

## Description

The `updateQualificationScore` command updates the Qualification scores for Workers.

## Arguments

The following table describes the arguments for the `updateQualificationScores` command.

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                          | Required    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-help` or `-h`                      | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                            | No          |
| `-input [filename]`                  | Specifies the file that contains the Worker IDs and desired Qualification scores to assign.<br>For information about this file, see \*The Worker ID file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if the `workerid` argument is not specified.<br>Example: `-input worker_qual_scores.txt` | Conditional |
| `-qualtypeid [Qualification Type ID` | The Qualification Type ID to update the Qualification scores for.<br>Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ`                                                                                                                                                                                                                                                     | Yes         |
| `-sandbox`                           | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                         | No          |
| `-score [integer value]`             | The score to assign to each Worker for the specified Qualification Type ID.<br>Condition: Required if the score is not defined in the `input` file<br>Example: `-score 50`                                                                                                                                                                                           | Conditional |
| `-workerid [Worker ID]`              | The ID of the Worker you want to assign the score to.<br>Conditions: Required if the `input` argument is not specified.<br>Example: `-workerid A3C4G8DMXFG5PQ`                                                                                                                                                                                                       | Conditional |

## Example

The following examples for Unix and Windows show how to use the `updateQualificationScore`
command. These examples update the score for one Worker.

### Unix

The following example demonstrates how to call this command from Unix.

```

./updateQualificationScore.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ score 50 -workerid A3C4G8DMXFG5

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

updateQualificationScore -qualtypeid RWFZTKZ55ZPZXN1C8TDZ score 50 -workerid A3C4G8DMXFG5

```

## Output

These examples produce the following output.

```

Successfully updated A3C4G8DMXFG5 score to 50

```
