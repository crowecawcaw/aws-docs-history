|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# updateQualificationType

## Description

The `updateQualificationType` command updates the properties of your Qualification.

## Arguments

The following table describes the arguments for the `updateQualificationType` command.

| Name                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | --- |
| `-answer [filename]`     | Specifies the Qualification Answer file that contains the new AnswerKey XML for the<br>Qualification test. This file allows the Amazon Mechanical Turk system to automatically<br>evaluate and score a Qualification request. For information about this file, see<br>\*The Qualification answer file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-answer qualification.answer`                       | No                                    |
| `-help` or `-h`          | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                                                                                          | No                                    |
| `-properties [filename]` | Specifies the Qualification properties file that contains the new properties for the Qualification.<br>The Qualification is updated with all the properties defined in the file.<br>For information about this file, see \*The Qualification properties file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>NoteYou cannot modify the title of a Qualification.<br>Example: `-properties qualification.properties` | No                                    |
| `-qualtypeid`            | The Qualification Type ID of the Qualification you want to update. This ID is in the<br>`.success`file generated after you create the Qualification with the<br>[createQualificationType](CLTReference_CreateQualificationTypeCommand.md "CLTReference_CreateQualificationTypeCommand.md")<br>command.<br>Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ`                                                                                                              | Yes                                   |
| `-question [filename]`   | Specifies the Qualification question file that contains the new Qualification test.<br>For information about this file, see \*The Qualification question file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-question qualification.question`                                                                                                                                                           | No                                    |
| `-status [status value]` | Specifies whether the Qualification is active or inactive. Inactive Qualifications are no longer<br>available for Workers and cannot be used for new HITs.<br>Valid Values: Active                                                                                                                                                                                                                                                                                 | Inactive<br>Example: `-status Active` | No  |
| `-sandbox`               | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                                                                                                       | No                                    |

## Example

The following examples for Unix and Windows show how to use the `updateQualificationType`
command. These examples update the Qualification test.

### Unix

The following example demonstrates how to call this command from Unix.

```

./updateQualificationType.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -question survey.question

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

updateQualificationType -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -question survey.question

```

## Output

These examples produce the following output.

```

Updated qualification type RWFZTKZ55ZPZXN1C8TDZ

```
