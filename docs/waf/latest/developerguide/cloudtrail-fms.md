**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS Firewall Manager information in CloudTrail

AWS Firewall Manager supports logging the following actions as events in CloudTrail log files:

- [AssociateAdminAccount](../../../fms/2018-01-01/APIReference/API_AssociateAdminAccount.md "../../../fms/2018-01-01/APIReference/API_AssociateAdminAccount.md")
- [DeleteNotificationChannel](../../../fms/2018-01-01/APIReference/API_DeleteNotificationChannel.md "../../../fms/2018-01-01/APIReference/API_DeleteNotificationChannel.md")
- [DeletePolicy](../../../fms/2018-01-01/APIReference/API_DeletePolicy.md "../../../fms/2018-01-01/APIReference/API_DeletePolicy.md")
- [DisassociateAdminAccount](../../../fms/2018-01-01/APIReference/API_DisassociateAdminAccount.md "../../../fms/2018-01-01/APIReference/API_DisassociateAdminAccount.md")
- [PutNotificationChannel](../../../fms/2018-01-01/APIReference/API_PutNotificationChannel.md "../../../fms/2018-01-01/APIReference/API_PutNotificationChannel.md")
- [PutPolicy](../../../fms/2018-01-01/APIReference/API_PutPolicy.md "../../../fms/2018-01-01/APIReference/API_PutPolicy.md")
- [GetAdminAccount](../../../fms/2018-01-01/APIReference/API_GetAdminAccount.md "../../../fms/2018-01-01/APIReference/API_GetAdminAccount.md")
- [GetComplianceDetail](../../../fms/2018-01-01/APIReference/API_GetComplianceDetail.md "../../../fms/2018-01-01/APIReference/API_GetComplianceDetail.md")
- [GetNotificationChannel](../../../fms/2018-01-01/APIReference/API_GetNotificationChannel.md "../../../fms/2018-01-01/APIReference/API_GetNotificationChannel.md")
- [GetPolicy](../../../fms/2018-01-01/APIReference/API_GetPolicy.md "../../../fms/2018-01-01/APIReference/API_GetPolicy.md")
- [ListComplianceStatus](../../../fms/2018-01-01/APIReference/API_ListComplianceStatus.md "../../../fms/2018-01-01/APIReference/API_ListComplianceStatus.md")
- [ListPolicies](../../../fms/2018-01-01/APIReference/API_ListPolicies.md "../../../fms/2018-01-01/APIReference/API_ListPolicies.md")
  Every event or log entry contains information about who generated the request. The
  identity information helps you determine the following:

- Whether the request was made with root user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Firewall Manager log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of
the public API calls, so they do not appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `GetAdminAccount`--> action.

```

	{
                "eventVersion": "1.05",
                "userIdentity": {
                                "type": "AssumedRole",
                                "principalId": "1234567890987654321231",
                                "arn": "arn:aws:sts::123456789012:assumed-role/Admin/SampleUser",
                                "accountId": "123456789012",
                                "accessKeyId": "1AFGDT647FHU83JHFI81H",
                                "sessionContext": {
                                                "attributes": {
                                                                "mfaAuthenticated": "false",
                                                                "creationDate": "2018-04-14T02:51:50Z"
                                                              },
                                                "sessionIssuer": {
                                                                "type": "Role",
                                                                "principalId": "1234567890987654321231",
                                                                "arn": "arn:aws:iam::123456789012:role/Admin",
                                                                "accountId": "123456789012",
                                                                "userName": "Admin"
                                                                 }
                                                  }
                                },
                "eventTime": "2018-04-14T03:12:35Z",
                "eventSource": "fms.amazonaws.com",
                "eventName": "GetAdminAccount",
                "awsRegion": "us-east-1",
                "sourceIPAddress": "72.21.198.65",
                "userAgent": "console.amazonaws.com",
                "requestParameters": null,
                "responseElements": null,
                "requestID": "ae244f41-3f91-11e8-787b-dfaafef95fc1",
                "eventID": "5769af1e-14b1-4bd1-ba75-f023981d0a4a",
                "eventType": "AwsApiCall",
                "apiVersion": "2018-01-01",
                "recipientAccountId": "123456789012"
     }


```
