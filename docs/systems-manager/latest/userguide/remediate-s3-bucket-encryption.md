

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Changing to an AWS KMS customer managed key to encrypt S3 resources
<a name="remediate-s3-bucket-encryption"></a>

During the onboarding process for the unified Systems Manager console, Quick Setup creates an Amazon Simple Storage Service (Amazon S3) bucket in the delegated administrator account. This bucket is used to store the diagnosis output data generated during remediation runbook executions. By default, the bucket uses server-side encryption with Amazon S3 managed keys (SSE-S3).

You can review the content of these policies in [S3 bucket policies for the unified Systems Manager console](remediate-s3-bucket-policies.md).

However, you can instead use server-side encryption with AWS KMS keys (SSE-KMS) using a customer managed key as an alternative to an AWS KMS key.

Complete the following tasks to configure Systems Manager to use your KMS key.

## Task 1: Add a tag to an existing KMS key
<a name="remediate-s3-bucket-encryption-add-kms-tag"></a>

AWS Systems Manager uses your KMS key only if it is tagged with the following key-value pair:
+ Key: `SystemsManagerManaged`
+ Value: `true`

Use the following procedure to provide access for encrypting the S3 bucket with your KMS key.

**To add a tag to your existing KMS key**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. In the left navigation, choose **Customer managed keys**.

1. Select the AWS KMS key to use with AWS Systems Manager.

1. Choose the **Tags** tab, and then choose **Edit**.

1. Choose **Add tag**.

1. Do the following:

   1. For **Tag key**, enter **SystemsManagerManaged**.

   1. For **Tag value**, enter **true**.

1. Choose **Save**.

## Task 2: Modify an existing KMS key policy
<a name="remediate-s3-bucket-encryption-update-kms-policy"></a>

Use the following procedure to update the [KMS key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) of your KMS key to allow AWS Systems Manager roles to encrypt the S3 bucket on your behalf.

**To modify an existing KMS key policy**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. In the left navigation, choose **Customer managed keys**.

1. Select the AWS KMS key to use with AWS Systems Manager.

1. On the **Key policy** tab, choose **Edit**.

1. Add the following JSON statement to the `Statement` field, and replace the {{placeholder values}} with your own information.

   Make sure that you add all AWS account IDs that are onboarded in your organization to AWS Systems Manager in the `Principal` field.

   To locate the correct bucket name in the Amazon S3 console, in the delegated administrator account, locate the bucket in the format `do-not-delete-ssm-{{operational-account-id}}-{{home-region}}-{{disambiguator}}`.

   ```
   {
        "Sid": "EncryptionForSystemsManagerS3Bucket",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "{{account-id-1}}",
                "{{account-id-2}}",
                ...
            ]
        },
        "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
            },
            "StringLike": {
                "kms:ViaService": "s3.*.amazonaws.com"
            },
            "ArnLike": {
                "aws:PrincipalArn": "arn:aws:iam::*:role/AWS-SSM-*"
            }
        }
    }
   ```

**Tip**  
Alternatively, you can update the KMS key policy using the [aws:PrincipalOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid) condition key to grant AWS Systems Manager access to your KMS key.

## Task 3: Specify the KMS key in Systems Manager settings
<a name="remediate-s3-bucket-encryption-update-setting"></a>

After completing the previous two tasks, use the following procedure to change the S3 bucket encryption. This change ensures that the associated Quick Setup configuration process can add permissions for Systems Manager to accept your KMS key.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**.

1. On the **Diagnose and remediate** tab, in the **Update S3 bucket encryption** section, choose **Edit**.

1. Select the **Customize encryption settings (advanced)** check box.

1. In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, choose the ID of an existing key, or paste the ARN of an existing key.

1. Choose **Save**.