

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# AWS Firewall Manager information in CloudTrail
<a name="cloudtrail-fms"></a>

AWS Firewall Manager supports logging the following actions as events in CloudTrail log files:
+ [AssociateAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AssociateAdminAccount.html)
+ [DeleteNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeleteNotificationChannel.html)
+ [DeletePolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html)
+ [DisassociateAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DisassociateAdminAccount.html)
+ [PutNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutNotificationChannel.html)
+ [PutPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutPolicy.html)
+ [GetAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminAccount.html)
+ [GetComplianceDetail](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetComplianceDetail.html)
+ [GetNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetNotificationChannel.html)
+ [GetPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetPolicy.html)
+ [ListComplianceStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListComplianceStatus.html)
+ [ListPolicies](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListPolicies.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root user credentials 
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Example: Firewall Manager log file entries
<a name="understanding-service-name-entries-FMS"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order.

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