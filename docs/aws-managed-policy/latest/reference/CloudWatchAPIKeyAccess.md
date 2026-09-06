

# CloudWatchAPIKeyAccess
<a name="CloudWatchAPIKeyAccess"></a>

**Description**: Grants permissions to call CloudWatch using API key authentication.

`CloudWatchAPIKeyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchAPIKeyAccess-how-to-use"></a>

You can attach `CloudWatchAPIKeyAccess` to your users, groups, and roles.

## Policy details
<a name="CloudWatchAPIKeyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 08, 2026, 08:57 UTC 
+ **Edited time:** June 04, 2026, 20:42 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchAPIKeyAccess`

## Policy version
<a name="CloudWatchAPIKeyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchAPIKeyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CloudWatchMetricsAPIs",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:CallWithBearerToken",
        "cloudwatch:PutMetricData"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "KMSDecryptForCMKDatasets",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt"
      ],
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "cloudwatch.*.amazonaws.com",
          "kms:EncryptionContext:aws:cloudwatch:arn" : "arn:aws:cloudwatch:*:*:dataset/*"
        }
      }
    }
  ]
}
```

## Learn more
<a name="CloudWatchAPIKeyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)