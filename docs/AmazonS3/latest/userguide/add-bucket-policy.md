# Adding a bucket policy by using the Amazon S3 console

You can use the [AWS Policy
Generator](https://aws.amazon.com/blogs/aws/aws-policy-generator/ "https://aws.amazon.com/blogs/aws/aws-policy-generator/") and the Amazon S3 console to add a new bucket policy or edit an existing bucket policy.
A bucket policy is a resource-based AWS Identity and Access Management (IAM) policy. You add a bucket policy to a
bucket to grant other AWS accounts or IAM users access permissions for the bucket and
the objects in it. Object permissions apply only to the objects that the bucket owner
creates. For more information about bucket policies, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").

Make sure to resolve security warnings, errors, general warnings, and suggestions from
AWS Identity and Access Management Access Analyzer before you save your policy. IAM Access Analyzer runs policy checks to validate
your policy against IAM [policy
grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") and [best
practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"). These checks generate findings and provide actionable recommendations
to help you author policies that are functional and conform to security best practices. To
learn more about validating policies by using IAM Access Analyzer, see [IAM Access Analyzer policy
validation](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_. To view a
list of the warnings, errors, and suggestions that are returned by IAM Access Analyzer, see [IAM Access Analyzer policy
check reference](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md").

For guidance on troubleshooting errors with a policy, see [Troubleshoot access denied (403
Forbidden) errors in Amazon S3](troubleshoot-403-errors.md "troubleshoot-403-errors.md").

###### To create or edit a bucket policy

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.
3.  In the list of buckets, choose the name of the bucket that you
    want to create a bucket policy for or whose bucket policy you want to edit.
4.  Choose the **Permissions** tab.
5.  Under **Bucket policy**, choose **Edit**. The
    **Edit bucket policy** page appears.
6.  On the **Edit bucket policy** page, do one of the following:

        * To see examples of bucket policies, choose **Policy
         examples**. Or see [Examples of Amazon S3 bucket policies](example-bucket-policies.md "example-bucket-policies.md") in the
         *Amazon S3 User Guide*.
        * To generate a policy automatically, or edit the JSON in the
         **Policy** section, choose **Policy
         generator**.

    If you choose **Policy generator**, the AWS Policy Generator
    opens in a new window.

        1. On the **AWS Policy Generator** page, for
         **Select Type of Policy**, choose **S3 Bucket
         Policy**.
        2. Add a statement by entering the information in the provided fields, and
         then choose **Add Statement**. Repeat this step for as many
         statements as you would like to add. For more information about these
         fields, see the [IAM JSON
         policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
         *IAM User Guide*.


        ###### Note

        For your convenience, the **Edit bucket policy** page
         displays the **Bucket ARN** (Amazon Resource Name) of
         the current bucket above the **Policy** text field. You
         can copy this ARN for use in the statements on the **AWS
         Policy Generator** page.
        3. After you finish adding statements, choose **Generate
         Policy**.
        4. Copy the generated policy text, choose **Close**, and
         return to the **Edit bucket policy** page in the Amazon S3
         console.

7.  In the **Policy** box, edit the existing policy or paste the
    bucket policy from the AWS Policy Generator. Make sure to resolve security
    warnings, errors, general warnings, and suggestions before you save your
    policy.

###### Note

Bucket policies are limited to 20 KB in size. 8. (Optional) Choose **Preview external access** in the lower-right corner to
preview how your new policy affects public and cross-account access to your resource. Before you save your policy, you can check whether
it introduces new IAM Access Analyzer findings or resolves existing findings. If you don’t see an active analyzer, choose
**Go to Access Analyzer** to [create an account analyzer](../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling "../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling") in IAM Access Analyzer. For more information, see
[Preview access](../../../IAM/latest/UserGuide/access-analyzer-access-preview.md "../../../IAM/latest/UserGuide/access-analyzer-access-preview.md") in the
_IAM User Guide_. 9. Choose **Save changes**, which returns you to the
**Permissions** tab.
