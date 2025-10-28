# AWS Fargate Federal Information Processing Standard

(FIPS-140)

Federal Information Processing Standard (FIPS-140) is a U.S. and Canadian government
standard that specifies the security requirements for cryptographic modules that protect
sensitive information. FIPS-140 defines a set of validated cryptography functions that can be
used to encrypt data in transit and data at rest.

When you turn on FIPS-140 compliance, you can run workloads on Fargate in a manner that is
compliant with FIPS-140. For more information about FIPS-140 compliance, see [Federal Information Processing Standard
(FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

## AWS Fargate FIPS-140 Considerations

Consider the following when using FIPS-140 compliance on Fargate:

- FIPS-140 compliance is only available in the AWS GovCloud (US)
  Regions.
- Fargate supports FIPS-140 version 140.3
- FIPS-140 compliance is turned off by default. You must turn it on.
- Amazon CloudWatch doesn't support a dualstack FIPS endpoint that can be used to monitor
  Amazon ECS tasks in IPv6-only configuration that use FIPS-140 compliance.
- Your tasks must use the following configuration for FIPS-140 compliance:
  - The `operatingSystemFamily` must be
    `LINUX`.
  - The `cpuArchitecture` must be `X86_64`.
  - The Fargate platform version must be `1.4.0` or
    later.

## Use FIPS on Fargate

Use the following procedure to use FIPS-140 compliance on Fargate.

1. Turn on FIPS-140 compliance. For more information, see [AWS Fargate Federal Information Processing Standard
   (FIPS-140) compliance](ecs-account-settings.md#fips-setting "ecs-account-settings.md#fips-setting").
2. You can optionally use ECS Exec to run the following command to verify the
   FIPS-140 compliance status for a cluster.

Replace `cluster-name` with the name of your cluster,
`task-id` with the ID or ARN of your task, and
`container-name` with the name of the container in
your task you want to run the command against.

A return value of "1" indicates that you are using FIPS.

```
aws ecs execute-command \
    --cluster `cluster-name` \
    --task `task-id` \
    --container `container-name` \
    --interactive \
    --command "cat /proc/sys/crypto/fips_enabled"
```

## Use CloudTrail for Fargate FIPS-140 auditing

CloudTrail is turned on in your AWS account when you create the account. When API and
console activity occurs in Amazon ECS, that activity is recorded in a CloudTrail event along with
other AWS service events in **Event history**. You can view, search,
and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon ECS,
create a trail which CloudTrail uses to deliver log files to an Amazon S3 bucket. By default, when
you create a trail in the console, the trail applies to all regions. The trail logs
events from all Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to further
analyze and act upon the event data collected in CloudTrail logs. For more information, see
[Log Amazon ECS API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

The following example shows a CloudTrail log entry that demonstrates the
`PutAccountSettingDefault` API action:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAIV5AJI5LXF5EXAMPLE",
         "arn": "arn:aws:iam::123456789012:user/jdoe",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIPWIOFC3EXAMPLE",
    },
    "eventTime": "2023-03-01T21:45:18Z",
    "eventSource": "ecs.amazonaws.com",
    "eventName": "PutAccountSettingDefault",
    "awsRegion": "us-gov-east-1",
    "sourceIPAddress": "52.94.133.131",
    "userAgent": "aws-cli/2.9.8 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/ecs.put-account-setting",
    "requestParameters": {
        "name": "fargateFIPSMode",
        "value": "enabled"
    },
    "responseElements": {
        "setting": {
            "name": "fargateFIPSMode",
            "value": "enabled",
            "principalArn": "arn:aws:iam::123456789012:user/jdoe"
        }
    },
    "requestID": "acdc731e-e506-447c-965d-f5f75EXAMPLE",
    "eventID": "6afced68-75cd-4d44-8076-0beEXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "ecs-fips.us-gov-east-1.amazonaws.com"
    }
}
```
