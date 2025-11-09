|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# assignQualification

## Description

The `assignQualification` command assigns a Qualification to a Worker without the
Worker requesting the Qualification. There are two ways to use this operation:

- Bulk Operation—
  If you want to assign multiple Qualifications, use this command with a file that contains
  the Qualification Type ID and the list of Workers to be assigned the Qualfication.
- Single Assignmentn—
  You can specify the Qualification Type ID, the Worker, and the assigned
  Qualification score on the command line.

## Arguments

The following table describes the arguments for the `assignQualification` command.

| Name                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-donotnotify`                        | Specifies not to notify Workers when you have assigned them the Qualification.<br>Example: `-donotnotify`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No          |
| `-help` or `-h`                       | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No          |
| `-input [filename]`                   | Specifies the file that contains the Qualification ID you want to assign to Workers. This file<br>contains a single Qualification ID. You can find this ID in the `.success` file<br>generated after you create the Qualification with the<br>[createQualificationType](CLTReference_CreateQualificationTypeCommand.md "CLTReference_CreateQualificationTypeCommand.md")<br>operation. For information about this file, see \*The Qualification ID file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if the `qualtypeid` argument is not specified.<br>Example: `-input qualification.properties.success` | Conditional |
| `-qualtypeid [Qualification Type ID]` | Specifies the Qualification Type ID of the Qualification you want to assign to the Worker. This ID can<br>be found in the `.success` file generated after you create the Qualification with the<br>`>` operation.<br>Condition: Required if the `input` argument is not specified.<br>Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ`                                                                                                                                                                                                                                                                                                                                               | Conditional |
| `-sandbox`                            | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your `mturk.properties`<br>file.<br>Example:`-sandbox`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No          |
| `-score [integer]`                    | Specifies the default Qualification score to assign to Workers. This argument can be used with both the<br>bulk operation and the single assignment. If this argument is not specified, and the score<br>has not been defined in the scorefile, a default score of `1` is used.<br>Example: `-score 100`                                                                                                                                                                                                                                                                                                                                                                        | No          |
| `-scorefile [filename]`               | Specifies a file which contains a tab delimited list of Worker IDs and optional Qualification scores to<br>assign to each Worker. If the score is not specified, a default value of `1` is assigned.<br>For information about this file, see \*The score file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if the `-workerid` argument is not specified.<br>Example: `-scorefile workerstoassign.txt`                                                                                                                                                                                                     | Conditional |
| `-workerid [Worker ID]`               | Specifies the ID of the Worker you want to assign the Qualification to.<br>Condition: Required if the `scorefile` argument is not specified.<br>Example: `-workerid A3C4G8DMXFG5PQ`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Conditional |

## Example

The following examples for Unix and Windows show how to use the `AssignQualification`
command. The examples demonstrate a single assignment.

### Unix

The following example demonstrates how to call this command from Unix.

```

./assignQualification.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -score 100

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

assignQualification -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -score 100

```

## Output

These examples produce the following output.

```

Assigned qualification RWFZTKZ55ZPZXN1C8TDZ to A3C4G8DMXFG5PQ with value 100

```

## Related Commands

- [createQualificationType](CLTReference_CreateQualificationTypeCommand.md "CLTReference_CreateQualificationTypeCommand.md")
