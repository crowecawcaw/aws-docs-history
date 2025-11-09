AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Changing to an AWS KMS customer managed key to

encrypt S3 resources

During the onboarding process for the unified Systems Manager console, Quick Setup creates an
Amazon Simple Storage Service (Amazon S3) bucket in the delegated administrator account. This bucket is used to
store the diagnosis output data generated during remediation runbook executions. By
default, the bucket uses server-side encryption with Amazon S3 managed keys (SSE-S3).

You can review the content of these policies in [S3 bucket policies for the unified Systems Manager
console](remediate-s3-bucket-policies.md "remediate-s3-bucket-policies.md").

However, you can instead use server-side encryption with AWS KMS keys (SSE-KMS)
using a customer managed key (CMK) as an alternative to an AWS KMS key.

Complete the following tasks in order to configure Systems Manager to use your CMK.

## Task 1: Add a tag to an

existing CMK

AWS Systems Manager uses your CMK only if it is tagged with the following key-value
pair:

- Key: `SystemsManagerManaged`
- Value: `true`

Use the following procedure to provide access for encrypting the S3 bucket with
your CMK.

###### To add a tag to your existing CMK

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. In the left navigation, choose **Customer managed
   keys**.
3. Select the AWS KMS key to use with AWS Systems Manager.
4. Choose the **Tags** tab, and then choose
   **Edit**.
5. Choose **Add tag**.
6. Do the following:
   1. For **Tag key**, enter
      `SystemsManagerManaged`.
   2. For **Tag value**, enter
      `true`.

7. Choose **Save**.

## Task 2: Modify an

existing CMK key policy

Use the following procedure to update the [KMS key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") of your
CMK to allow AWS Systems Manager roles to encrypt the S3 bucket on your behalf.

###### To modify an existing CMK key policy

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. In the left navigation, choose **Customer managed
   keys**.
3. Select the AWS KMS key to use with AWS Systems Manager.
4. On the **Key policy** tab, choose
   **Edit**.
5. Add the following JSON statement to the `Statement` field, and
   replace the `placeholder values` with your own
   information.

Ensure that you add all AWS account IDs that are onboarded in your
organization to AWS Systems Manager in the `Principal` field.

To locate the correct bucket name in the Amazon S3 console, in the delegated
administrator account, locate the bucket in the format
`do-not-delete-ssm-`operational-account-id`-`home-region`-`disambiguator``.

```
{
     "Sid": "EncryptionForSystemsManagerS3Bucket",
     "Effect": "Allow",
     "Principal": {
         "AWS": [
             "`account-id-1`",
             "`account-id-2`",
             ...
         ]
     },
     "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
     "Resource": "*",
     "Condition": {
         "StringEquals": {
             "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`amzn-s3-demo-bucket`"
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

###### Tip

Alternatively, you can update the CMK key policy using the [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") condition key to grant AWS Systems Manager access to your
CMK.

## Task 3: Specify the

CMK in Systems Manager settings

After completing the previous two tasks, use the following procedure to change the
S3 bucket encryption. This change ensures that the associated Quick Setup configuration
process can add permissions for Systems Manager to accept your CMK.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Settings**.
3. On the **Diagnose and remediate** tab, in the
   **Update S3 bucket encryption** section, choose
   **Edit**.
4. Select the **Customize encryption settings (advanced)**
   check box.
5. In the search (
   ![The search icon](images/search-icon.png)
   ) box, choose the ID of an existing key, or paste the
   ARN of an existing key.
6. Choose **Save**.
