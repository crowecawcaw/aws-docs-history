# AwsCloudTrail resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsCloudTrail` resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsCloudTrailTrail

The `AwsCloudTrailTrail` object provides details about a AWS CloudTrail
trail.

The following is an example `AwsCloudTrailTrail` finding in the AWS
Security Finding Format (ASFF). To view descriptions of `AwsCloudTrailTrail`
attributes, see [AwsCloudTrailTrailDetails](../../1.0/APIReference/API_AwsCloudTrailTrailDetails.md "../../1.0/APIReference/API_AwsCloudTrailTrailDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsCloudTrailTrail": {
    "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:CloudTrail/regression:*",
    "CloudWatchLogsRoleArn": "arn:aws:iam::866482105055:role/CloudTrail_CloudWatchLogs",
    "HasCustomEventSelectors": true,
    "HomeRegion": "us-west-2",
    "IncludeGlobalServiceEvents": true,
    "IsMultiRegionTrail": true,
    "IsOrganizationTrail": false,
    "KmsKeyId": "kmsKeyId",
    "LogFileValidationEnabled": true,
    "Name": "regression-trail",
    "S3BucketName": "cloudtrail-bucket",
    "S3KeyPrefix": "s3KeyPrefix",
    "SnsTopicArn": "arn:aws:sns:us-east-2:123456789012:MyTopic",
    "SnsTopicName": "snsTopicName",
    "TrailArn": "arn:aws:cloudtrail:us-west-2:123456789012:trail"
}
```
