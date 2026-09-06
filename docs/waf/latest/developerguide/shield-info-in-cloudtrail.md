

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# AWS Shield Advanced information in CloudTrail
<a name="shield-info-in-cloudtrail"></a>

AWS Shield Advanced supports logging the following actions as events in CloudTrail log files:
+ [ListAttacks](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListAttacks.html)
+ [DescribeAttack](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttack.html)
+ [CreateProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateProtection.html)
+ [DescribeProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtection.html)
+ [DeleteProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteProtection.html)
+ [ListProtections](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtections.html)
+ [CreateSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateSubscription.html)
+ [DescribeSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeSubscription.html)
+ [GetSubscriptionState](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_GetSubscriptionState.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root user credentials 
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Example: Shield Advanced log file entries
<a name="understanding-service-name-entries-shield"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `DeleteProtection` and `ListProtections` actions.

```
 
 [
  {
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "IAMUser",
      "principalId": "1234567890987654321231",
      "arn": "arn:aws:iam::123456789012:user/SampleUser",
      "accountId": "123456789012",
      "accessKeyId": "1AFGDT647FHU83JHFI81H",
      "userName": "SampleUser"
    },
    "eventTime": "2018-01-10T21:31:14Z",
    "eventSource": "shield.amazonaws.com",
    "eventName": "DeleteProtection",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "aws-cli/1.14.10 Python/3.6.4 Darwin/16.7.0 botocore/1.8.14",
    "requestParameters": {
      "protectionId": "12345678-5104-46eb-bd03-agh4j8rh3b6n"
    },
    "responseElements": null,
    "requestID": "95bc0042-f64d-11e7-abd1-1babdc7aa857",
    "eventID": "85263bf4-17h4-43bb-b405-fh84jhd8urhg",
    "eventType": "AwsApiCall",
    "apiVersion": "AWSShield_20160616",
    "recipientAccountId": "123456789012"
  },
  {
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "IAMUser",
      "principalId": "123456789098765432123",
      "arn": "arn:aws:iam::123456789012:user/SampleUser",
      "accountId": "123456789012",
      "accessKeyId": "1AFGDT647FHU83JHFI81H",
      "userName": "SampleUser"
    },
    "eventTime": "2018-01-10T21:30:03Z",
    "eventSource": "shield.amazonaws.com",
    "eventName": "ListProtections",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "aws-cli/1.14.10 Python/3.6.4 Darwin/16.7.0 botocore/1.8.14",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "6accca40-f64d-11e7-abd1-1bjfi8urhj47",
    "eventID": "ac0570bd-8dbc-41ac-a2c2-987j90j3h78f",
    "eventType": "AwsApiCall",
    "apiVersion": "AWSShield_20160616",
    "recipientAccountId": "123456789012"
  }
]
```