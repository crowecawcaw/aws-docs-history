# Mandatory controls

Mandatory controls are owned by AWS Control Tower, and they apply to every OU on your landing zone,
with some exceptions for the **Security OU**. These controls are
applied to your OUs by default when you set up your , and they can't be deactivated, because they protect AWS Control Tower resources.

Following, you'll find a reference for each of the mandatory controls available in
AWS Control Tower today. Please note that with AWS Control Tower Landing Zone 4.0, there have been several
changes to the mandatory controls.

###### Topics

- [Changes in Landing Zone 4.0 controls](#changes-in-landing-zone-40 "#changes-in-landing-zone-40")
- [Mandatory controls for the Security OU](#mandatory-on-security-ou "#mandatory-on-security-ou")
- [Mandatory controls for all OUs](#mandatory-on-all-ous "#mandatory-on-all-ous")

## Changes in Landing Zone 4.0 controls

- AWS Control Tower will no longer deploy the below controls from 4.0 because these protect the account trails which were deployed
  in 2.9 and below. These controls would still be applied for versions below 4.0 and would be deleted once customers
  upgrade to versions 4.0 and above.
  - [Disallow Configuration Changes to
    CloudTrail](#cloudtrail-configuration-changes "#cloudtrail-configuration-changes")Disallow Configuration Changes to CloudTrail
  - [Integrate CloudTrail Events with Amazon
    CloudWatch Logs](#cloudtrail-integrate-events-logs "#cloudtrail-integrate-events-logs")Integrate CloudTrail Events with Amazon CloudWatch Logs
  - [Enable CloudTrail in All Available Regions](#cloudtrail-enable-region "#cloudtrail-enable-region")Enable CloudTrail in All Available Regions
  - [Enable Integrity Validation for CloudTrail Log
    File](#cloudtrail-enable-validation "#cloudtrail-enable-validation")Enable Integrity Validation for CloudTrail Log File

- The following detective mandatory control will be removed:
  - [Detect whether shared accounts
    under the Security organizational unit have AWS CloudTrail or CloudTrail Lake
    enabled](#ensure-cloudtrail-enabled-mandatory "#ensure-cloudtrail-enabled-mandatory")Detect whether shared accounts under the Security organizational unit have AWS CloudTrail or CloudTrail Lake enabled

- The following controls will be removed if the customer has AWS Config integration enabled and are upgrading to 4.0 and above
  (Note: Customers on versions below 4.0 have AWS Config integration enabled by default). These controls are related to legacy
  AWS Config aggregators and are no longer required for Service-Linked Config Aggregator. Read more on the Service-linked Config aggregator
  [here](../../../prescriptive-guidance/latest/designing-control-tower-landing-zone/config-mgmt.md "../../../prescriptive-guidance/latest/designing-control-tower-landing-zone/config-mgmt.md").
  - [Disallow Changes to Tags Created by
    AWS Control Tower for AWS Config Resources](#cloudwatch-disallow-config-changes "#cloudwatch-disallow-config-changes")
  - [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](#config-aggregation-authorization-policy "#config-aggregation-authorization-policy")
  - [Disallow Changes to AWS Config Rules Set Up by
    AWS Control Tower](#config-rule-disallow-changes "#config-rule-disallow-changes")

- The AWS CloudTrail integration tied to the manifest `centralizedLogging` configuration has two new controls
  starting 4.0
  - Disallow changes to Amazon SNS subscriptions and topics managed by AWS Control Tower

  ```

  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "CTSNSPV1",
              "Effect": "Deny",
              "NotAction": [
                  "sns:ConfirmSubscription",
                  "sns:Get*",
                  "sns:List*",
                  "sns:Publish",
                  "sns:PutDataProtectionPolicy",
                  "sns:Subscribe",
                  "sns:TagResource",
                  "sns:Unsubscribe",
                  "sns:UntagResource"
              ],
              "Resource": "arn:*:sns:*:*:aws-controltower-CentralizedLoggingNotifications*",
              "Condition": {
                   "ArnNotLike": {
                          "aws:PrincipalARN": [
                          "arn:*:iam::*:role/AWSControlTowerExecution"
                      ]
                   }
              }
          }
      ]
  }

  ```

  - Disallow modifications to Amazon S3 buckets managed by AWS Control Tower

  ```

  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "CTS3PV8",
              "Effect": "Deny",
              "NotAction": [
                  "s3:DeleteObject",
                  "s3:DeleteObjectTagging",
                  "s3:DeleteObjectVersion",
                  "s3:DeleteObjectVersionTagging",
                  "s3:Get*",
                  "s3:List*",
                  "s3:PutBucketTagging",
                  "s3:PutObject",
                  "s3:PutObjectAcl",
                  "s3:PutObjectLegalHold",
                  "s3:PutObjectRetention",
                  "s3:PutObjectTagging",
                  "s3:PutObjectVersionAcl",
                  "s3:PutObjectVersionTagging",
                  "s3:RestoreObject"
              ],
              "Resource": [
                  "arn:*:s3:::aws-controltower-access-logs-*",
                  "arn:*:s3:::aws-controltower-cloudtrail-*",
                  "arn:*:s3:::aws-controltower-logs-*"
              ],
              "Condition": {
                  "ArnNotLike": {
                      "aws:PrincipalARN": [
                          "arn:*:iam::*:role/AWSControlTowerExecution"
                      ]
                  }
              }
          }
      ]
  }

  ```

- The AWS Config integration has a new control starting 4.0
  - Disallow modifications to AWS Config recorder Amazon S3 buckets managed by AWS Control Tower

  ```

  {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "CTS3PV7",
               "Effect": "Deny",
               "NotAction": [
                   "s3:DeleteObject",
                   "s3:DeleteObjectTagging",
                          "s3:DeleteObjectVersion",
                          "s3:DeleteObjectVersionTagging",
                          "s3:Get*",
                          "s3:List*",
                          "s3:PutBucketTagging",
                          "s3:PutObject",
                          "s3:PutObjectAcl",
                          "s3:PutObjectLegalHold",
                          "s3:PutObjectRetention",
                          "s3:PutObjectTagging",
                          "s3:PutObjectVersionAcl",
                          "s3:PutObjectVersionTagging",
                          "s3:RestoreObject"
               ],
               "Resource": "arn:*:s3:::aws-controltower-config-*",
               "Condition": {
                   "ArnNotLike": {
                       "aws:PrincipalARN": [
                          "arn:*:iam::*:role/AWSControlTowerExecution"
                      ]
                  }
              }
          }
      ]
  }

  ```

- On 4.0, AWS Control Tower will disable the following controls as they are replaced with a single unified
  preventive control for AWS Config integration. The security governance boundary remains the same,
  but with reduced SCP space.
  - [Disallow Changes to Encryption
    Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-changes-s3-buckets-created "#disallow-changes-s3-buckets-created")
  - [Disallow Changes to
    Logging Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-logging-changes-s3-buckets-created "#disallow-logging-changes-s3-buckets-created")
  - [Disallow Changes to Bucket
    Policy for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-policy-changes-s3-buckets-created "#disallow-policy-changes-s3-buckets-created")
  - [Disallow Changes to
    Lifecycle Configuration for AWS Control Tower Created Amazon S3 Buckets in Log
    Archive](#disallow-lifecycle-changes-s3-buckets-created "#disallow-lifecycle-changes-s3-buckets-created")
  - [Disallow Deletion of Log
    Archive](#disallow-audit-bucket-deletion "#disallow-audit-bucket-deletion")
  - [Detect Public Write Access Setting for Log
    Archive](#log-archive-public-write "#log-archive-public-write")
  - [Detect Public Read Access Setting for Log
    Archive](#log-archive-public-read "#log-archive-public-read")

- AWS Control Tower is updating the following controls for all versions, this change will take place when customers
  update/reset their existing setup.
  - [Disallow Changes to Amazon SNS Set Up by
    AWS Control Tower](#sns-disallow-changes "#sns-disallow-changes")

  The change is to specify three explicit SNS topic ARNs in the Resource section instead
  of using a wildcard pattern

  ```

  {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "GRSNSTOPICPOLICY",
               "Effect": "Deny",
               "Action": [
                   "sns:AddPermission",
                   "sns:CreateTopic",
                   "sns:DeleteTopic",
                   "sns:RemovePermission",
                   "sns:SetTopicAttributes"
               ],
               "Resource": [
                   "arn:*:sns:*:*:aws-controltower-AggregateSecurityNotifications*",
                   "arn:*:sns:*:*:aws-controltower-AllConfigNotifications*",
                   "arn:*:sns:*:*:aws-controltower-SecurityNotifications*"
               ],
               "Condition": {
                   "ArnNotLike": {
                       "aws:PrincipalARN": "arn:*:iam::*:role/AWSControlTowerExecution"
                   }
               }
           }
       ]
  }

  ```

## Mandatory controls for the Security OU

When you set up your landing zone, the following eight controls are applied only to
the Security OU.

###### Topics

- [Disallow Changes to Encryption
  Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-changes-s3-buckets-created "#disallow-changes-s3-buckets-created")
- [Disallow Changes to
  Logging Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-logging-changes-s3-buckets-created "#disallow-logging-changes-s3-buckets-created")
- [Disallow Changes to Bucket
  Policy for AWS Control Tower Created Amazon S3 Buckets in Log Archive](#disallow-policy-changes-s3-buckets-created "#disallow-policy-changes-s3-buckets-created")
- [Disallow Changes to
  Lifecycle Configuration for AWS Control Tower Created Amazon S3 Buckets in Log
  Archive](#disallow-lifecycle-changes-s3-buckets-created "#disallow-lifecycle-changes-s3-buckets-created")
- [Disallow Deletion of Log
  Archive](#disallow-audit-bucket-deletion "#disallow-audit-bucket-deletion")
- [Detect Public Read Access Setting for Log
  Archive](#log-archive-public-read "#log-archive-public-read")
- [Detect Public Write Access Setting for Log
  Archive](#log-archive-public-write "#log-archive-public-write")
- [Detect whether shared accounts
  under the Security organizational unit have AWS CloudTrail or CloudTrail Lake
  enabled](#ensure-cloudtrail-enabled-mandatory "#ensure-cloudtrail-enabled-mandatory")

### Disallow Changes to Encryption

Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive

This control prevents changes to encryption for the Amazon S3 buckets that AWS Control Tower creates
in the log archive account. This is a preventive control with mandatory guidance. By
default, this control is enabled on the **Security OU**. It cannot be enabled on additional
OUs.

The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCTAUDITBUCKETENCRYPTIONCHANGESPROHIBITED",
 "Effect": "Deny",
 "Action": [
 "s3:PutEncryptionConfiguration"
 ],
 "Resource": ["arn:aws:s3:::aws-controltower*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to

Logging Configuration for AWS Control Tower Created Amazon S3 Buckets in Log Archive

This control prevents changes to logging configuration for the Amazon S3 buckets that
AWS Control Tower creates in the log archive account. This is a preventive control with mandatory
guidance. By default, this control is enabled on the **Security OU**. It cannot be enabled
on additional OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCTAUDITBUCKETLOGGINGCONFIGURATIONCHANGESPROHIBITED",
 "Effect": "Deny",
 "Action": [
 "s3:PutBucketLogging"
 ],
 "Resource": ["arn:aws:s3:::aws-controltower*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to Bucket

Policy for AWS Control Tower Created Amazon S3 Buckets in Log Archive

This control prevents changes to bucket policy for the Amazon S3 buckets that AWS Control Tower
creates in the log archive account. This is a preventive control with mandatory
guidance. By default, this control is enabled on the **Security OU**. It cannot be enabled
on additional OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCTAUDITBUCKETPOLICYCHANGESPROHIBITED",
 "Effect": "Deny",
 "Action": [
 "s3:PutBucketPolicy",
 "s3:DeleteBucketPolicy"
 ],
 "Resource": ["arn:aws:s3:::aws-controltower*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to

Lifecycle Configuration for AWS Control Tower Created Amazon S3 Buckets in Log
Archive

This control prevents lifecycle configuration changes for the Amazon S3 buckets that
AWS Control Tower creates in the log archive account. This is a preventive control with mandatory
guidance. By default, this control is enabled on the **Security OU**. It cannot be enabled
on additional OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCTAUDITBUCKETLIFECYCLECONFIGURATIONCHANGESPROHIBITED",
 "Effect": "Deny",
 "Action": [
 "s3:PutLifecycleConfiguration"
 ],
 "Resource": ["arn:aws:s3:::aws-controltower*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Deletion of Log

Archive

This control prevents deletion of Amazon S3 buckets created by AWS Control Tower in the log archive
account. This is a preventive control with mandatory guidance. By default, this control
is enabled on the **Security OU**.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRAUDITBUCKETDELETIONPROHIBITED",
 "Effect": "Deny",
 "Action": [
 "s3:DeleteBucket"
 ],
 "Resource": [
 "arn:aws:s3:::aws-controltower*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Detect Public Read Access Setting for Log

Archive

This control detects whether public read access is enabled to the Amazon S3 buckets in the
log archive shared account. This control does not change the status of the account. This
is a detective control with mandatory guidance. By default, this control is enabled on
the **Security OU**.

The artifact for this control is the following AWS Config rule.

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure AWS Config rules to check that your S3 buckets do not allow public access
Parameters:
  ConfigRuleName:
    Type: 'String'
    Description: 'Name for the Config rule'
Resources:
  CheckForS3PublicRead:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: !Sub ${ConfigRuleName}
      Description: Checks that your S3 buckets do not allow public read access. If an S3 bucket policy or bucket ACL allows public read access, the bucket is noncompliant.
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
      Scope:
        ComplianceResourceTypes:
          - AWS::S3::Bucket
```

### Detect Public Write Access Setting for Log

Archive

This control detects whether public write access is enabled to the Amazon S3 buckets in the
log archive shared account. This control does not change the status of the account. This
is a detective control with mandatory guidance. By default, this control is enabled on
the **Security OU**.

The artifact for this control is the following AWS Config rule.

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure AWS Config rules to check that your S3 buckets do not allow public access
Parameters:
  ConfigRuleName:
    Type: 'String'
    Description: 'Name for the Config rule'
Resources:
  CheckForS3PublicWrite:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: !Sub ${ConfigRuleName}
      Description: Checks that your S3 buckets do not allow public write access. If an S3 bucket policy or bucket ACL allows public write access, the bucket is noncompliant.
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
      Scope:
        ComplianceResourceTypes:
          - AWS::S3::Bucket

```

### Detect whether shared accounts

under the Security organizational unit have AWS CloudTrail or CloudTrail Lake
enabled

This control detects whether shared accounts under the Security organizational unit
have AWS CloudTrail or CloudTrail Lake enabled. The rule is NON_COMPLIANT if either CloudTrail or CloudTrail
Lake is not enabled in a shared account. This is a detective control with mandatory
guidance. By default, this control is enabled on the **Security OU**.

The artifact for this control is the following AWS Config rule.

```

     AWSTemplateFormatVersion: 2010-09-09
	 Description: Configure AWS Config rules to detect whether an account has AWS CloudTrail or CloudTrail Lake enabled.

	 Parameters:
	   ConfigRuleName:
	     Type: 'String'
	     Description: 'Name for the Config rule'

	 Resources:
	   CheckForCloudtrailEnabled:
	     Type: AWS::Config::ConfigRule
	     Properties:
	       ConfigRuleName: !Sub ${ConfigRuleName}
	       Description: Detects whether an account has AWS CloudTrail or CloudTrail Lake enabled. The rule is NON_COMPLIANT if either CloudTrail or CloudTrail Lake is not enabled in an account.
	       Source:
	         Owner: AWS
	         SourceIdentifier: CLOUD_TRAIL_ENABLED
```

## Mandatory controls for all OUs

The following 15 mandatory controls are enabled by default on all OUs, when you set up your landing zone.

###### Note

The four mandatory controls with `"Sid": "GRCLOUDTRAILENABLED"` are
identical by design. The sample code is correct.

###### Topics

- [Disallow Changes to Amazon CloudWatch Logs
  Log Groups set up by AWS Control Tower](#log-group-deletion-policy "#log-group-deletion-policy")
- [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](#config-aggregation-authorization-policy "#config-aggregation-authorization-policy")
- [Disallow Configuration Changes to
  CloudTrail](#cloudtrail-configuration-changes "#cloudtrail-configuration-changes")
- [Integrate CloudTrail Events with Amazon
  CloudWatch Logs](#cloudtrail-integrate-events-logs "#cloudtrail-integrate-events-logs")
- [Enable CloudTrail in All Available Regions](#cloudtrail-enable-region "#cloudtrail-enable-region")
- [Enable Integrity Validation for CloudTrail Log
  File](#cloudtrail-enable-validation "#cloudtrail-enable-validation")
- [Disallow Changes to Amazon CloudWatch Set Up by
  AWS Control Tower](#cloudwatch-disallow-changes "#cloudwatch-disallow-changes")
- [Disallow Changes to Tags Created by
  AWS Control Tower for AWS Config Resources](#cloudwatch-disallow-config-changes "#cloudwatch-disallow-config-changes")
- [Disallow Configuration Changes to AWS Config](#config-disallow-changes "#config-disallow-changes")
- [Enable AWS Config in All Available Regions](#config-enable-regions "#config-enable-regions")
- [Disallow Changes to AWS Config Rules Set Up by
  AWS Control Tower](#config-rule-disallow-changes "#config-rule-disallow-changes")
- [Disallow Changes to AWS IAM Roles Set Up by
  AWS Control Tower and AWS CloudFormation](#iam-disallow-changes "#iam-disallow-changes")
- [Disallow Changes to AWS Lambda Functions Set
  Up by AWS Control Tower](#lambda-disallow-changes "#lambda-disallow-changes")
- [Disallow Changes to Amazon SNS Set Up by
  AWS Control Tower](#sns-disallow-changes "#sns-disallow-changes")
- [Disallow Changes to Amazon SNS
  Subscriptions Set Up by AWS Control Tower](#sns-subscriptions-disallow-changes "#sns-subscriptions-disallow-changes")

### Disallow Changes to Amazon CloudWatch Logs

Log Groups set up by AWS Control Tower

This control prevents changes to the retention policy for Amazon CloudWatch Logs log groups
that AWS Control Tower created in the log archive account when you set up your landing zone. It
also prevents modifying the log retention policy in customer accounts. This is a
preventive control with mandatory guidance. By default, this control is enabled on all
OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRLOGGROUPPOLICY",
 "Effect": "Deny",
 "Action": [
 "logs:DeleteLogGroup",
 "logs:PutRetentionPolicy"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:*aws-controltower*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::*:role/AWSControlTowerExecution"
 ]
 }
 }
 }
 ]
}`

```

### Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower

This control prevents deletion of AWS Config aggregation authorizations that AWS Control Tower
created in the audit account when you set up your landing zone. This is a preventive
control with mandatory guidance. By default, this control is enabled on all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCONFIGAGGREGATIONAUTHORIZATIONPOLICY",
 "Effect": "Deny",
 "Action": [
 "config:DeleteAggregationAuthorization"
 ],
 "Resource": [
 "arn:aws:config:*:*:aggregation-authorization*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::*:role/AWSControlTowerExecution"
 },
 "StringLike": {
 "aws:ResourceTag/aws-control-tower": "managed-by-control-tower"
 }
 }
 }
 ]
}`

```

### Disallow Configuration Changes to

CloudTrail

This control prevents configuration changes to CloudTrail in your landing zone. This is a
preventive control with mandatory guidance. By default, this control is enabled on all
OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCLOUDTRAILENABLED",
 "Effect": "Deny",
 "Action": [
 "cloudtrail:DeleteTrail",
 "cloudtrail:PutEventSelectors",
 "cloudtrail:StopLogging",
 "cloudtrail:UpdateTrail"
 ],
 "Resource": ["arn:aws:cloudtrail:*:*:trail/aws-controltower-*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Integrate CloudTrail Events with Amazon

CloudWatch Logs

This control performs real-time analysis of activity data by sending CloudTrail events to
CloudWatch Logs log files. This is a preventive control with mandatory guidance. By default, this
control is enabled on all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCLOUDTRAILENABLED",
 "Effect": "Deny",
 "Action": [
 "cloudtrail:DeleteTrail",
 "cloudtrail:PutEventSelectors",
 "cloudtrail:StopLogging",
 "cloudtrail:UpdateTrail"
 ],
 "Resource": ["arn:aws:cloudtrail:*:*:trail/aws-controltower-*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Enable CloudTrail in All Available Regions

This control enables CloudTrail in all available AWS Regions. This is a preventive control
with mandatory guidance. By default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCLOUDTRAILENABLED",
 "Effect": "Deny",
 "Action": [
 "cloudtrail:DeleteTrail",
 "cloudtrail:PutEventSelectors",
 "cloudtrail:StopLogging",
 "cloudtrail:UpdateTrail"
 ],
 "Resource": ["arn:aws:cloudtrail:*:*:trail/aws-controltower-*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Enable Integrity Validation for CloudTrail Log

File

This control enables integrity validation for the CloudTrail log file in all accounts and
OUs. It protects the integrity of account activity logs using CloudTrail log file validation,
which creates a digitally signed digest file that contains a hash of each log that CloudTrail
writes to Amazon S3. This is a preventive control with mandatory guidance. By default, this
control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCLOUDTRAILENABLED",
 "Effect": "Deny",
 "Action": [
 "cloudtrail:DeleteTrail",
 "cloudtrail:PutEventSelectors",
 "cloudtrail:StopLogging",
 "cloudtrail:UpdateTrail"
 ],
 "Resource": ["arn:aws:cloudtrail:*:*:trail/aws-controltower-*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to Amazon CloudWatch Set Up by

AWS Control Tower

This control disallows changes to Amazon CloudWatch; as it was configured by AWS Control Tower when you
set up your landing zone. This is a preventive control with mandatory guidance. By
default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCLOUDWATCHEVENTPOLICY",
 "Effect": "Deny",
 "Action": [
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "events:DisableRule",
 "events:DeleteRule"
 ],
 "Resource": [
 "arn:aws:events:*:*:rule/aws-controltower-*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to Tags Created by

AWS Control Tower for AWS Config Resources

This control prevents changes to the tags that AWS Control Tower created when you set up your
landing zone, for AWS Config resources that collect configuration and compliance data. It
denies any `TagResource` and `UntagResource` operation for
aggregation authorizations tagged by AWS Control Tower. This is a preventive control with
mandatory guidance. By default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCONFIGRULETAGSPOLICY",
 "Effect": "Deny",
 "Action": [
 "config:TagResource",
 "config:UntagResource"
 ],
 "Resource": ["*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:aws:iam::*:role/AWSControlTowerExecution"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "aws-control-tower"
 }
 }
 }
 ]
}`

```

### Disallow Configuration Changes to AWS Config

This control prevents configuration changes to AWS Config. It ensures that AWS Config records
resource configurations in a consistent manner by disallowing AWS Config settings changes.
This is a preventive control with mandatory guidance. By default, this control is
enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCONFIGENABLED",
 "Effect": "Deny",
 "Action": [
 "config:DeleteConfigurationRecorder",
 "config:DeleteDeliveryChannel",
 "config:DeleteRetentionConfiguration",
 "config:PutConfigurationRecorder",
 "config:PutDeliveryChannel",
 "config:PutRetentionConfiguration",
 "config:StopConfigurationRecorder"
 ],
 "Resource": ["*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Enable AWS Config in All Available Regions

This control enables AWS Config in all available AWS Regions. This is a preventive control
with mandatory guidance. By default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCONFIGENABLED",
 "Effect": "Deny",
 "Action": [
 "config:DeleteConfigurationRecorder",
 "config:DeleteDeliveryChannel",
 "config:DeleteRetentionConfiguration",
 "config:PutConfigurationRecorder",
 "config:PutDeliveryChannel",
 "config:PutRetentionConfiguration",
 "config:StopConfigurationRecorder"
 ],
 "Resource": ["*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to AWS Config Rules Set Up by

AWS Control Tower

This control disallows changes to AWS Config Rules that were implemented by AWS Control Tower when the
landing zone was set up. This is a preventive control with mandatory guidance. By
default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRCONFIGRULEPOLICY",
 "Effect": "Deny",
 "Action": [
 "config:PutConfigRule",
 "config:DeleteConfigRule",
 "config:DeleteEvaluationResults",
 "config:DeleteConfigurationAggregator",
 "config:PutConfigurationAggregator"
 ],
 "Resource": ["*"],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:aws:iam::*:role/AWSControlTowerExecution"
 },
 "StringEquals": {
 "aws:ResourceTag/aws-control-tower": "managed-by-control-tower"
 }
 }
 }
 ]
}`

```

### Disallow Changes to AWS IAM Roles Set Up by

AWS Control Tower and AWS CloudFormation

This control disallows changes to the AWS IAM roles that AWS Control Tower created when the
landing zone was set up. This is a preventive control with mandatory guidance. By
default, this control is enabled in all OUs.

#### Control update

An updated version has been released for the mandatory control
`AWS-GR_IAM_ROLE_CHANGE_PROHIBITED`.

This change to the control is required because accounts in OUs that are being enrolled
into AWS Control Tower must have the `AWSControlTowerExecution` role enabled. The previous
version of the control prevents this role from being created.

AWS Control Tower updated the existing control to add an exception so that AWS CloudFormation StackSets
can create the `AWSControlTowerExecution` role. As a second measure, this new
control protects the
StackSets
role to prevent principals in the child account from gaining access.

The new control version performs the following actions, in addition to all actions
provided in the previous version:

- Allows the `stacksets-exec-*` role (owned by AWS CloudFormation) to perform
  actions on IAM roles that were created by AWS Control Tower.
- Prevents changes to any IAM role in child accounts, where the IAM role name
  matches the pattern `stacksets-exec-*`.

###### The update to the control version affects your OUs and accounts as follows:

- If you extend governance to an OU, that incoming OU receives the updated version
  of the control as part of the registration process. You do not need to update your
  landing zone to get the latest version for this OU. AWS Control Tower applies the latest version
  automatically to OUs that register.
- If you update or repair your landing zone at any time after this release, your
  control will be updated to this version for future provisioning.
- OUs created in or registered with AWS Control Tower before this release date, and which are
  part of a landing zone that has not been repaired or updated after the release date, will
  continue to operate with the old version of the control, which blocks the creation
  of the `AWSControlTowerExecution` role.
- One consequence of this control update is that your OUs can be functioning with
  different versions of the control. Update your landing zone to apply the updated
  version of the control to your OUs uniformly.

The artifact of the updated control is the following SCP.

```

{
  "Version": "2012-10-17",
  "Statement": [
     {
        "Sid": "GRIAMROLEPOLICY",
        "Effect": "Deny",
        "Action": [
          "iam:AttachRolePolicy",
          "iam:CreateRole",
          "iam:DeleteRole",
          "iam:DeleteRolePermissionsBoundary",
          "iam:DeleteRolePolicy",
          "iam:DetachRolePolicy",
          "iam:PutRolePermissionsBoundary",
          "iam:PutRolePolicy",
          "iam:UpdateAssumeRolePolicy",
          "iam:UpdateRole",
          "iam:UpdateRoleDescription"
        ],
        "Resource": [
          "arn:aws:iam::*:role/aws-controltower-*",
          "arn:aws:iam::*:role/*AWSControlTower*",
          "arn:aws:iam::*:role/stacksets-exec-*"    #this line is new
        ],
        "Condition": {
          "ArnNotLike": {
            "aws:PrincipalArn": [
                "arn:aws:iam::*:role/AWSControlTowerExecution",
                "arn:aws:iam::*:role/stacksets-exec-*"    #this line is new
         ]
       }
      }
    }
  ]
}

```

The former artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRIAMROLEPOLICY",
 "Effect": "Deny",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:DeleteRolePermissionsBoundary",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:PutRolePermissionsBoundary",
 "iam:PutRolePolicy",
 "iam:UpdateAssumeRolePolicy",
 "iam:UpdateRole",
 "iam:UpdateRoleDescription"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-controltower-*",
 "arn:aws:iam::*:role/*AWSControlTower*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to AWS Lambda Functions Set

Up by AWS Control Tower

This control disallows changes to AWS Lambda functions set up by AWS Control Tower. This is a
preventive control with mandatory guidance. By default, this control is enabled in all
OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRLAMBDAFUNCTIONPOLICY",
 "Effect": "Deny",
 "Action": [
 "lambda:AddPermission",
 "lambda:CreateEventSourceMapping",
 "lambda:CreateFunction",
 "lambda:DeleteEventSourceMapping",
 "lambda:DeleteFunction",
 "lambda:DeleteFunctionConcurrency",
 "lambda:PutFunctionConcurrency",
 "lambda:RemovePermission",
 "lambda:UpdateEventSourceMapping",
 "lambda:UpdateFunctionCode",
 "lambda:UpdateFunctionConfiguration"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:function:aws-controltower-*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to Amazon SNS Set Up by

AWS Control Tower

This control disallows changes to Amazon SNS set up by AWS Control Tower. It protects the integrity
of Amazon SNS notification settings for your landing zone. This is a preventive control with
mandatory guidance. By default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRSNSTOPICPOLICY",
 "Effect": "Deny",
 "Action": [
 "sns:AddPermission",
 "sns:CreateTopic",
 "sns:DeleteTopic",
 "sns:RemovePermission",
 "sns:SetTopicAttributes"
 ],
 "Resource": [
 "arn:aws:sns:*:*:aws-controltower-*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```

### Disallow Changes to Amazon SNS

Subscriptions Set Up by AWS Control Tower

This control disallows changes to Amazon SNS subscriptions set up by AWS Control Tower. It protects
the integrity of Amazon SNS subscriptions settings for your landing zone, to trigger
notifications for AWS Config Rules compliance changes. This is a preventive control with mandatory
guidance. By default, this control is enabled in all OUs.

The artifact for this control is the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRSNSSUBSCRIPTIONPOLICY",
 "Effect": "Deny",
 "Action": [
 "sns:Subscribe",
 "sns:Unsubscribe"
 ],
 "Resource": [
 "arn:aws:sns:*:*:aws-controltower-SecurityNotifications"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN":"arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```
