# Remediating a potentially compromised S3 bucket

When GuardDuty generates [GuardDuty S3 Protection finding types](guardduty_finding-types-s3.md "guardduty_finding-types-s3.md"), it indicates that your Amazon S3 buckets
have been compromised. If the behavior that caused the finding was expected in your
environment, then consider creating [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md"). If this behavior was not
expected, then follow these recommended steps to remediate a potentially compromised
Amazon S3 bucket in your AWS environment:

1. **Identify the potentially compromised S3
   resource.**

A GuardDuty finding for S3 will list the associated S3 bucket, its Amazon Resource
Name (ARN), and its owner in the finding details. 2. **Identify the source of the suspicious activity and the
API call used.**

The API call used will be listed as `API` in the finding details.
The source will be an IAM principal (either an IAM role, user, or account) and
identifying details will be listed in the finding. Depending on the source type,
Remote IP address or source domain info will be available and can help you
evaluate whether the source was authorized. If the finding involved credentials
from an Amazon EC2 instance the details for that resource will also be
included. 3. **Determine whether the call source was authorized to
access the identified resource.**

For example consider the following:

    * If an IAM user was involved, is it possible that their credentials
     have been potentially compromised? For more information, see [Remediating potentially compromised AWS
     credentials](compromised-creds.md "compromised-creds.md").
    * If an API was invoked from a principal that has no prior history of
     invoking this type of API, does this source need access permissions for
     this operation? Can the bucket permissions be further restricted?
    * If the access was seen from the **user name**
    `ANONYMOUS_PRINCIPAL` with **user type** of
     `AWSAccount` this indicates the bucket is public and was
     accessed. Should this bucket be public? If not, review the security
     recommendations below for alternative solutions to sharing S3 resources.
    * If the access was though a successful `PreflightRequest`
     call seen from the **user name** `ANONYMOUS_PRINCIPAL` with **user type** of `AWSAccount` this
     indicates the bucket has a cross-origin resource sharing (CORS) policy
     set. Should this bucket have a CORS policy? If not, ensure the bucket is
     not inadvertently public and review the security recommendations below
     for alternative solutions to sharing S3 resources. For more information
     on CORS see [Using cross-origin
     resource sharing (CORS)](../../../AmazonS3/latest/userguide/cors.md "../../../AmazonS3/latest/userguide/cors.md") in the S3 user guide.

4. **Determine whether the S3 bucket contains sensitive
   data.**

Use [Amazon Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md") to determine whether the S3 bucket contains sensitive
data, such as personally identifiable information (PII), financial data, or
credentials. If automated sensitive data discovery is enabled for your Macie
account, review the S3 bucket's details to gain a better understanding of your
S3 bucket's contents. If this feature is disabled for your Macie account, we
recommend turning it on to expedite your assessment. Alternatively, you can
create and run a sensitive data discovery job to inspect the S3 bucket's objects
for sensitive data. For more information, see [Discovering sensitive data
with Macie](../../../macie/latest/user/data-classification.md "../../../macie/latest/user/data-classification.md").
If the access was authorized, you can ignore the finding. The [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/")
console allows you to set up rules to entirely suppress individual findings so that they
no longer appear. For more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

If you determine that your S3 data has been exposed or accessed by an unauthorized
party, review the following S3 security recommendations to tighten permissions and
restrict access. Appropriate remediation solutions will depend on the needs of your
specific environment.

## Recommendations based on

specific S3 bucket access needs

**The following list provides recommendations based on
specific Amazon S3 bucket access needs:**

- For a centralized way to limit public access to your S3 data use, S3 block
  public access. Block public access settings can be enabled for access
  points, buckets, and AWS Accounts through four different settings to
  control granularity of access. For more information see [Block public access settings](../../../AmazonS3/latest/userguide/access-control-block-public-access.md#access-control-block-public-access-options "../../../AmazonS3/latest/userguide/access-control-block-public-access.md#access-control-block-public-access-options") in the _Amazon S3 User Guide_.
- AWS Access policies can be used to control how IAM users can access
  your resources or how your buckets can be accessed. For more information see
  [Using bucket policies
  and user policies](../../../AmazonS3/latest/userguide/security_iam_service-with-iam.md "../../../AmazonS3/latest/userguide/security_iam_service-with-iam.md") in the _Amazon S3 User Guide_.

Additionally you can use Virtual Private Cloud (VPC) endpoints with S3
bucket policies to restrict access to specific VPC endpoints. For more
information see [Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md")
in the _Amazon S3 User Guide_

- To temporarily allow access to your S3 objects to trusted entities outside
  your account you can create a Presigned URL through S3. This access is
  created using your account credentials and depending on the credentials used
  can last 6 hours to 7 days. For more information see [Using presigned URLs
  to download and upload objects](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md") in the _Amazon S3 User Guide_.
- For use cases that require that sharing of S3 objects between different
  sources you can use S3 Access Points to create permission sets that restrict
  access to only those within your private network. For more information see
  [Managing access to shared datasets with access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md")
  in the _Amazon S3 User Guide_.
- To securely grant access to your S3 resources to other AWS Accounts you
  can use an access control list (ACL), for more information see [Access control list (ACL) overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon S3 User Guide_.

For more information about S3 security options, see [Security best practices for
Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") in the _Amazon S3 User Guide_.
