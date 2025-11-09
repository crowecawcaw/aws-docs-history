|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# getQualificationRequests

## Description

The `getQualificationRequests` command retrieves the Qualification requests from
Workers for your Qualifications. For more information about Qualifications and Qualification requests see the
[Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

## Arguments

The following table describes the arguments for the `getQualificationRequests` command.

| Name                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-help` or `-h`                       | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No       |
| `-outputfile [filename]`              | Specifies the output file. This is a tab delimited text file that contains the details of Workers'<br>Qualification. You can then approve or reject the Qualification Requests by using<br>[approveQualificationRequests](CLTReference_ApproveQualificationRequestsCommand.md "CLTReference_ApproveQualificationRequestsCommand.md") or<br>[rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md "CLTReference_RejectQualificationRequestsCommand.md") command.<br>For information about this file, see \*The Qualification request file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-outputfile qualification_requests.txt` | Yes      |
| `-qualtypeid [Qualification Type ID]` | Specifies the Qualification Type ID of the Qualification you want to retrieve requests for.<br>This ID is in a `.success` file generated after you create the Qualification<br>with the [createQualificationType](CLTReference_CreateQualificationTypeCommand.md "CLTReference_CreateQualificationTypeCommand.md")<br>command. If this ID is not specified, all Qualification requests for Qualifications you own are<br>included in the output file.<br>Example:`-qualtypeid RWFZTKZ55ZPZXN1C8TDZ`                                                                                                                                                                                                                  | No       |
| `-sandbox`                            | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No       |

## Example

The following examples for Unix and Windows show how to use the `getQualificationRequests`
command. These examples write the requests for all Qualification types to the file
`qualrequests.txt`.

### Unix

The following example demonstrates how to call this command from Unix:

```

./getQualificationRequests.sh -outputfile qualrequests.txt

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows:

```

getQualificationRequests -outputfile qualrequests.txt

```

## Output

These examples retrieved four Qualfication requests and produced the following output.

```

Retrieved 4 Qualification Requests
Answers successfully saved to file: qualrequests.txt

```

## Related Commands

- [evaluateQualificationRequests](CLTReference_EvaluateQualificationRequestsCommand.md "CLTReference_EvaluateQualificationRequestsCommand.md")
- [approveQualificationRequests](CLTReference_ApproveQualificationRequestsCommand.md "CLTReference_ApproveQualificationRequestsCommand.md")
- [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md "CLTReference_RejectQualificationRequestsCommand.md")
