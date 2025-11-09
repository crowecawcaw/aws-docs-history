|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# createQualificationType

## Description

The `createQualificationType` command creates a Qualification that can be used
for your HITs. You can use the arguments to specify files that contain the
Qualification test and the answers for the test. You can also create a Qualification that does not require
a test. For more information about Qualifications, see the
[Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

## Arguments

The following table describes the arguments for the `createQualificationType` command.

| Name                     | Description                                                                                                                                                                                                                                                                                                                                                                       | Required |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-answer [filename]`     | Specifies the file that contains the answers for the Qualification test. If this argument is omitted,<br>you create a Qualification that does not require a test. For information about this file, see<br>\*The Qualification answer file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-answer qualification.answers` | No       |
| `-help` or `-h`          | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                         | No       |
| `-noretry`               | Specifies that Workers can only request the Qualification once.<br>Example: `-noretry`                                                                                                                                                                                                                                                                                            | No       |
| `-properties [filename]` | Specifies the Qualification properties file. For information about this file, see<br>\*The Qualification properties file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-properties qualification.properties`                                                                                                           | Yes      |
| `-question [filename]`   | Specifies the Qualification question file that contains the Qualification test. For<br>information about this file, see<br>\*The Qualification question file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example:`-question qualification.question`                                                                            | No       |
| `-sandbox`               | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                         | No       |

## Example

The following examples for Unix and Windows show how to use the `createQualificationType`
command. The examples use the property file `qualification.properties` and the question file
`qualification.question`. These examples create the qualification in the test environment.

### Unix

The following example demonstrates how to call this command from Unix.

```

.createQualificationType.sh -properties qualification.properties -question qualification.question -noretry -sandbox

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

createQualificationType -properties qualification.properties -question qualification.question -noretry -sandbox

```

## Output

If this command completes successfully, it creates a `.success` file
with the name specified in the `-properties` argument. For this
example, the file is named `qualification.properties.success`. This
file contains the Qualification Type ID of the newly created Qualification. This command
also produces output similar to the following.

```

Created qualification type: KYJ4GZZ5G3M6TDCEWYF0
You can take the test here:
http://workersandbox.mturk.com/mturk/requestqualification?qualificationId=KYJ4GZZ5G3M6TDCEWYF0

```

## Related Commands

- [getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md "CLTReference_GetQualificationRequestsCommand.md")
