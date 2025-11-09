|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# approveQualificationRequests

## Description

The `approveQualificationRequests` command approves a list of Qualification requests. You
can obtain the list from a call to
[getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md "CLTReference_GetQualificationRequestsCommand.md").

For information about Qualifications and Qualification requests, see the
[Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

## Arguments

The following table describes the arguments for the `approveQualificationRequests` command.

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                  | Required    |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `-approvefile [filename]`                 | Specifies a tab delimited text file that contains the list of Qualification requests to approve. For<br>information about this file, see \*The Qualification approve file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Condition: Required if the `qualRequest` argument is not specified.<br>Example: `-approvefile qualification_requests_toapprove.txt` | Conditional |
| `-force`                                  | Specifies \*not<br>• to prompt for manual confirmation before approving the requests.<br>Only advanced developers should use this argument.<br>Example: `-force`                                                                                                                                                                                                                                             | No          |
| `-help` or `-h`                           | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                                    | No          |
| `-qualRequest [Qualification request ID]` | The Qualification request IDs to approve. Multiple Qualification request IDs are comma separated.<br>Condition: Required if the `approvefile` argument is not specified.<br>Example: `-qualRequest TA3ZJBYP2Y7ZJSX2BBN0TZ8ZTM4F6H4ZVQ4DE8FZ`                                                                                                                                                                 | Conditional |
| `-sandbox`                                | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                                                    | No          |
| `-score [value]`                          | The default score to assign for each approved Qualification request. Any scores defined in the<br>`approvefile` override this default.<br>Example: `-score 100`                                                                                                                                                                                                                                              | No          |

## Example

The following examples for Unix and Windows show how to use the
`approveQualificationRequests` command.
The examples use a file named
`qualifications.txt` that contains 10 requests. Each request in the file gets
a score of 100.

### Unix

The following example demonstrates how to call this command from Unix.

```

./approveQualificationRequests.sh -approvefile qualifications.txt -score 100

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

approveQualificationRequests -approvefile qualifications.txt -score 100

```

## Output

These examples produce output similar to the following, but all 10 requests are listed.

```

You are about to grant 10 qual request(s).
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

[TA3ZJBYP2Y7ZJSX2BBN0TZ8ZTM4F6H4ZVQ4DE8FZ] QualRequest successfully approved with value (100)

```

## Related Commands

- [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md "CLTReference_RejectQualificationRequestsCommand.md")
- [revokeQualification](CLTReference_RevokeQualificationCommand.md "CLTReference_RevokeQualificationCommand.md")
