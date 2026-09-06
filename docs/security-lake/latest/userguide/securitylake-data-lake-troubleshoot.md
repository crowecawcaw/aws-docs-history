

# Troubleshooting data lake status
<a name="securitylake-data-lake-troubleshoot"></a>

The **Issues** page of the Security Lake console shows you a summary of issues that are affecting your data lake. For example, Security Lake can't enable log collection for AWS CloudTrail management events if you haven't created a CloudTrail trail for your organization. The **Issues** page covers issues that have occurred in the last 14 days. You can see a description of each issue and the suggested remediation steps.

To programmatically access a summary of issues, you can use the [ListDataLakeExceptions](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakeExceptions.html) operation of the Security Lake API. If you're using the AWS CLI, run the [list-data-lake-exceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lake-exceptions.html) command. For the `regions` parameter, you can specify one or more Region codes—for example, `us-east-1` for the US East (N. Virginia) Region—to see the issues affecting those Regions. If you don't include the `regions` parameter, issues affecting all Regions are returned. For a list of Region codes, see [Amazon Security Lake endpoints](https://docs.aws.amazon.com/general/latest/gr/securitylake.html) in the *AWS General Reference*.

For example, the following AWS CLI command lists issues that are affecting the `us-east-1` and `eu-west-3` Regions. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securitylake list-data-lake-exceptions \
--regions "{{us-east-1}}" "{{eu-west-3}}"
```

To notify a Security Lake user about an issue or error, use the [CreateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeExceptionSubscription.html) operation of the Security Lake API. The user can be notified through email, delivery to an Amazon Simple Queue Service (Amazon SQS) queue, delivery to an AWS Lambda function, or another supported protocol.

For example, the following AWS CLI command sends notifications of Security Lake exceptions to the specified account by SMS delivery. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securitylake create-data-lake-exception-subscription \
--notification-endpoint "{{123456789012}}" \
--exception-time-to-live {{30}} \
--subscription-protocol "{{sms}}"
```

To view details about an exception subscription, you can use the [GetDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeExceptionSubscription.html) operation. To update an exception subscription, you can use the [UpdateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLakeExceptionSubscription.html) operation. To delete an exception subscription and stop notifications, you can use the [DeleteDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeExceptionSubscription.html) operation.