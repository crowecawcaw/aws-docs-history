**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Logging AWS Shield network security director API calls with AWS CloudTrail

AWS Shield network security director integrates with AWS CloudTrail to record all API calls as events. This integration captures calls made from the network security director console, programmatic calls to network security director APIs, and calls made from other AWS services.

With CloudTrail, you can view recent events in the Event history or create a trail to deliver ongoing logs to an Amazon Simple Storage Service bucket. These logs provide details about each request, including the identity of the caller, the time, the request parameters, and the response.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## network security director information in CloudTrail

CloudTrail is automatically enabled on your AWS account. When activity occurs in network security director, it's recorded as an event in CloudTrail. For an ongoing record of events, create a trail that delivers log files to an Amazon S3 bucket.

For more information about creating and managing trails, see:

- [Creating a Trail for Your AWS Account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS Service Integrations with CloudTrail Logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Receiving CloudTrail Log Files from Multiple Regions and Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## network security director API operations logged by CloudTrail

All network security director API operations are logged by CloudTrail and documented in the API Reference. The following operations are included:

- _StartNetworkSecurityScan_: Initiates a network security scan
- _GetNetworkSecurityScan_: Retrieves information about a network security scan
- _ListResources_: Lists resources available in the service
- _GetResource_: Retrieves detailed information about a specific resource
- _ListFindings_: Lists security findings
- _GetFinding_: Retrieves detailed information about a specific finding
- _UpdateFinding_: Updates the status or other attributes of a finding
- _ListRemediations_: Lists remediation recommendations for a finding
- _ListInsights_: Lists insights based on findings and resources

## Understanding network security director log file entries

CloudTrail log entries contain information about who made the request, when it was made, and what parameters were used. Here's an example of a StartNetworkSecurityScan action:

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/janedoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "janedoe"
    },
    "eventTime": "2023-11-28T22:02:58Z",
    "eventSource": "network-director.amazonaws.com",
    "eventName": "StartNetworkSecurityScan",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.9.19 Python/3.9.11 Linux/5.15.0-1031-aws botocore/2.4.5",
    "requestParameters": {},
    "responseElements": {
        "scan": {
            "state": "RESCANNING",
            "startTime": "2023-11-28T22:02:58Z"
        }
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

And here's an example of a GetNetworkSecurityScan action:

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/janedoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "janedoe"
    },
    "eventTime": "2023-11-28T22:03:15Z",
    "eventSource": "network-director.amazonaws.com",
    "eventName": "GetNetworkSecurityScan",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.9.19 Python/3.9.11 Linux/5.15.0-1031-aws botocore/2.4.5",
    "requestParameters": {},
    "responseElements": {
        "scan": {
            "state": "COMPLETE",
            "startTime": "2023-11-28T22:02:58Z",
            "completionTime": "2023-11-28T22:03:15Z"
        }
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

## Monitoring CloudTrail logs with Amazon CloudWatch

You can use Amazon CloudWatch to monitor and alert on specific API activity in CloudTrail logs. This helps you detect unauthorized access attempts, configuration changes, or unusual activity patterns.

To set up CloudWatch monitoring:

1. Configure your CloudTrail trail to send logs to CloudWatch Logs
2. Create metric filters to extract specific information from log events
3. Create alarms based on these metrics

For detailed instructions, see [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md").

## Best practices for CloudTrail with network security director

To maximize security and auditability with CloudTrail:

- _Enable CloudTrail in all regions_ for comprehensive coverage
- _Enable log file integrity validation_ to detect unauthorized modifications
- _Use IAM to control access to CloudTrail logs_ following least privilege principles
- _Set up alerts for critical events_ using CloudWatch alarms
- _Regularly review CloudTrail logs_ to identify unusual activity
