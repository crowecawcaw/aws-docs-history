

# Bring your own Amazon S3 bucket for log delivery

When you set up or update a landing zone (version 4.0 or later), you can use your own Amazon S3 bucket for log delivery instead of the default bucket that AWS Control Tower creates and manages.

You can use a custom logging bucket for either of the following integrations:
+ The AWS CloudTrail integration uses the AWS CloudTrail organization trail.
+ The AWS Config integration uses AWS Config delivery.

Each integration can use a custom logging bucket or a bucket that AWS Control Tower creates and manages. You can use the same bucket for both integrations. When you use your own bucket, AWS Control Tower does not create a logging bucket or access logging bucket for that integration.

**Important**  
When you use a custom logging bucket, you manage its configuration. AWS Control Tower controls do not cover your bucket, so you are responsible for protecting it. For more information, see [Protecting a custom logging bucket](#custom-logging-bucket-protect).

## Prerequisites for a custom logging bucket
<a name="custom-logging-bucket-prerequisites"></a>

Before you set up a custom logging bucket, make sure your bucket meets the following requirements:
+ Your landing zone must be version 4.0 or later.
+ The bucket must exist in the home Region of your landing zone.
+ The bucket must be owned by an AWS account in your organization, except the management account. The account ID that you specify in `bucketAccountId` must identify the bucket owner.
+ Use a standard Amazon S3 bucket ARN: `arn:aws:s3:::bucket-name`. Access point ARNs are not supported.
+ The bucket name can't begin with `aws-controltower-`, which is reserved for AWS Control Tower.
+ The bucket must have a policy that grants log delivery access. For more information about the policy requirements, see [Required bucket policy](#custom-logging-bucket-policy).

## Configuring a custom logging bucket with the API
<a name="custom-logging-bucket-configure-api"></a>

In the `CreateLandingZone` or `UpdateLandingZone` API call, add a `customLoggingBucket` object to the `configurations` object for the `centralizedLogging` integration, the `config` integration, or both. Specify these required fields:

`bucketArn`  
The ARN of the existing Amazon S3 bucket.

`bucketAccountId`  
The 12-digit account ID of the account that owns the bucket.

For more information about using a custom logging bucket in a complete landing zone manifest, see [Example: Using a custom logging bucket](lz-api-launch.md#lz-api-custom-logging-bucket).

The following restrictions apply:
+ You can't specify `customLoggingBucket` together with `loggingBucket` or `accessLoggingBucket` for the same integration. The `loggingBucket` and `accessLoggingBucket` objects apply only to buckets that AWS Control Tower creates and manages.

## Configuring a custom logging bucket in the console
<a name="custom-logging-bucket-configure-console"></a>

The following steps describe how to configure a custom logging bucket when you update an existing landing zone.

1. Open the [AWS Control Tower **Landing zone settings** page](https://console.aws.amazon.com/controltower/home/settings).

1. Choose **Landing zone settings**.

1. Choose **Modify settings**.

1. Choose the **AWS Config for detective controls** or **AWS CloudTrail centralized logging** section.

1. Expand **Amazon S3 bucket preferences for logs**. For **Select S3 logging bucket**, choose **Use custom logging bucket**. Enter the **Custom logging bucket ARN** and **Custom logging bucket Account ID**.

1. To use a custom logging bucket for both integrations, repeat the previous two steps for the other integration.

1. Review your changes and choose **Update landing zone**.

**Note**  
If you are setting up AWS Control Tower for the first time, you can configure a custom logging bucket during initial setup. In the **Configure Service integrations** step, choose the **AWS Config for detective controls** or **AWS CloudTrail centralized logging** section. Expand **Amazon S3 bucket preferences for logs**, and choose **Use custom logging bucket**. Enter the **Custom logging bucket ARN** and **Custom logging bucket Account ID**.

## Protecting a custom logging bucket
<a name="custom-logging-bucket-protect"></a>

AWS Control Tower controls do not cover your custom logging bucket. Use these recommendations to protect it:
+ Follow the Amazon S3 best practices for configuring and protecting your bucket, such as S3 Block Public Access, versioning, encryption, lifecycle rules, and access logging. For more information, see [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) in the *Amazon S3 User Guide*.
+ The required bucket policy examples include the `AllowSSLRequestsOnly` statement, which denies non-HTTPS connections.
+ Apply the recommended service control policies (SCPs) to protect the bucket. For more information, see [Recommended service control policies](#custom-logging-bucket-scps).

## Switching or deleting a custom logging bucket
<a name="custom-logging-bucket-switch-delete"></a>

Use this information to plan bucket changes.

**Important**  
Before you delete the previous custom logging bucket for AWS Config, update the enabled baselines for the affected accounts so they deliver to the newly configured bucket.

Switching buckets for AWS Config  
After you change the custom logging bucket for AWS Config, accounts whose enabled baselines use the previous bucket need an update to switch to the new bucket. In the AWS Control Tower console, these accounts show **Update available** on the **Organization** page.  
In the API, this is reported as source drift. Call `GetEnabledBaseline` for an account's enabled baseline, or call `ListEnabledBaselines` with `includeChildren`. The status is returned in `driftStatusSummary.types.source.status`. To filter the results, set `sourceDriftStatuses` to `IN_SYNC` or `DRIFTED`.  
To apply the current landing zone settings, choose the OU for the account on the **Organization** page. The **OU details** page shows the available action.  
If `AWSControlTowerBaseline` is enabled, choose **Re-Register OU** under **Actions**. If `ConfigBaseline` is enabled, choose **Reset AWS Config baseline** under **Actions**.  
To apply the current landing zone settings programmatically, call `ResetEnabledBaseline` for the enabled baseline on the OU.

Switching buckets for AWS CloudTrail  
Changing only the custom logging bucket for AWS CloudTrail does not cause source drift on enabled baselines.

## Required bucket policy
<a name="custom-logging-bucket-policy"></a>

AWS CloudTrail and AWS Config require permissions to verify the bucket and deliver logs. The following JSON bucket policies grant the required access.

**Note**  
Make sure your bucket policy always includes the required log delivery permissions. Removing these permissions interrupts AWS CloudTrail and AWS Config log delivery.

In these policies, the organization ID is the Amazon S3 key prefix for delivered logs and the value of `aws:SourceOrgID`. Replace `{{amzn-s3-demo-bucket}}` with your bucket name. Replace `{{o-exampleorgid}}` with your organization ID everywhere it appears.

### Example: Custom bucket for the AWS CloudTrail integration only
<a name="custom-logging-bucket-policy-cloudtrail"></a>

Use the following JSON bucket policy when the bucket receives logs only from the AWS CloudTrail integration.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSSLRequestsOnly",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowBucketPermissionsCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "s3:GetBucketAcl",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowBucketExistenceCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "controltower.amazonaws.com",
          "cloudtrail.amazonaws.com"
        ]
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowCloudTrailDelivery",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{o-exampleorgid}}/AWSLogs/*/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceOrgID": "{{o-exampleorgid}}"
        }
      }
    }
  ]
}
```

### Example: Custom bucket for the AWS Config integration only
<a name="custom-logging-bucket-policy-config"></a>

Use the following JSON bucket policy when the bucket receives logs only from the AWS Config integration.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSSLRequestsOnly",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowBucketPermissionsCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Action": "s3:GetBucketAcl",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowBucketExistenceCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "controltower.amazonaws.com",
          "config.amazonaws.com"
        ]
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowConfigDelivery",
      "Effect": "Allow",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{o-exampleorgid}}/AWSLogs/*/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceOrgID": "{{o-exampleorgid}}"
        }
      }
    }
  ]
}
```

### Example: Shared bucket for both integrations
<a name="custom-logging-bucket-policy-shared"></a>

Use the following JSON bucket policy when the same bucket receives logs from both the AWS CloudTrail integration and the AWS Config integration.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSSLRequestsOnly",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowBucketPermissionsCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "cloudtrail.amazonaws.com",
          "config.amazonaws.com"
        ]
      },
      "Action": "s3:GetBucketAcl",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowBucketExistenceCheck",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "controltower.amazonaws.com",
          "cloudtrail.amazonaws.com",
          "config.amazonaws.com"
        ]
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "AllowCloudTrailDelivery",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{o-exampleorgid}}/AWSLogs/*/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceOrgID": "{{o-exampleorgid}}"
        }
      }
    },
    {
      "Sid": "AllowConfigDelivery",
      "Effect": "Allow",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{o-exampleorgid}}/AWSLogs/*/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceOrgID": "{{o-exampleorgid}}"
        }
      }
    }
  ]
}
```

## Recommended service control policies
<a name="custom-logging-bucket-scps"></a>

Use the following service control policies (SCPs) to protect your custom logging bucket.

### Deny bucket deletion and policy changes
<a name="custom-logging-bucket-scps-deny-deletion"></a>

This SCP prevents anyone in the bucket account from deleting the bucket or changing its policy. It denies `s3:DeleteBucket`, `s3:DeleteBucketPolicy`, and `s3:PutBucketPolicy` on the bucket. Replace `{{amzn-s3-demo-bucket}}` with your bucket name.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyBucketDeletionAndPolicyModification",
      "Effect": "Deny",
      "Action": [
        "s3:DeleteBucket",
        "s3:DeleteBucketPolicy",
        "s3:PutBucketPolicy"
      ],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    }
  ]
}
```

### Prevent the bucket account from leaving the organization
<a name="custom-logging-bucket-scps-prevent-removal"></a>

Consider applying an SCP that prevents the bucket account from leaving your organization. AWS Control Tower verifies during landing zone setup and update that the bucket account belongs to the organization. This SCP denies `organizations:LeaveOrganization` for the account that owns the bucket. Replace `{{111122223333}}` with the ID of that account. SCPs do not prevent the management account from removing a member account from the organization.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyRemoveBucketAccountFromOrganization",
      "Effect": "Deny",
      "Action": [
        "organizations:LeaveOrganization"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalAccount": "{{111122223333}}"
        }
      }
    }
  ]
}
```

## Related resources
<a name="custom-logging-bucket-related"></a>

For more information about related topics, see the following:
+ [Logging and monitoring in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/logging-and-monitoring.html)
+ [CreateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html) in the *AWS Control Tower API Reference*
+ [UpdateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html) in the *AWS Control Tower API Reference*
+ [Amazon S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) in the *Amazon S3 User Guide*