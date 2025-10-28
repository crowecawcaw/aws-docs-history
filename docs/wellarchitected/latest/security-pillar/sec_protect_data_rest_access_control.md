# SEC08-BP04 Enforce access control

To help protect your data at rest, enforce access control using
mechanisms such as isolation and versioning. Apply least privilege
and conditional access controls. Prevent granting public access to
your data.

**Desired outcome:** You verify that
only authorized users can access data on a need-to-know basis. You
protect your data with regular backups and versioning to prevent
against intentional or inadvertent modification or deletion of data.
You isolate critical data from other data to protect its
confidentiality and data integrity.

**Common anti-patterns:**

- Storing data with different sensitivity requirements or classification together.
- Using overly permissive permissions on decryption keys.
- Improperly classifying data.
- Not retaining detailed backups of important data.
- Providing persistent access to production data.
- Not auditing data access or regularly reviewing permissions.
  **Level of risk exposed if this best practice is not
  established:** High

## Implementation guidance

Protecting data at rest is important to maintain data integrity,
confidentiality, and compliance with regulatory requirements. You
can implement multiple controls to help achieve this, including
access control, isolation, conditional access, and versioning.

You can enforce access control with the principle of least
privilege, which provides only the necessary permissions to users
and services to perform their tasks. This includes access to
encryption keys. Review your
[AWS Key Management Service (AWS KMS) policies](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") to verify that
the level of access you grant is appropriate and that relevant
conditions apply.

You can separate data based on different classification levels by
using distinct AWS accounts for each level, and manage these
accounts using
[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"). This isolation can help prevent unauthorized
access and minimizes the risk of data exposure.

Regularly review the level of access granted in Amazon S3 bucket
policies. Avoid using publicly readable or writeable buckets
unless absolutely necessary. Consider using
[AWS Config](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") to detect publicly available buckets and Amazon CloudFront to serve content from Amazon S3. Verify that buckets
that should not allow public access are properly configured to
prevent it.

Implement versioning and object locking mechanisms for critical
data stored in Amazon S3.
[Amazon S3 versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") preserves previous versions of objects to
recover data from accidental deletion or overwrites.
[Amazon S3 Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") provides mandatory access control for
objects, which prevents them from being deleted or overwritten,
even by the root user, until the lock expires. Additionally,
[Amazon Glacier Vault Lock](../../../amazonglacier/latest/dev/vault-lock.md "../../../amazonglacier/latest/dev/vault-lock.md") offers a similar feature for archives
stored in Amazon Glacier.

### Implementation steps

1. **Enforce access control with the
   principle of least privilege**:
   - Review the access permissions granted to users and
     services, and verify that they have only the necessary
     permissions to perform their tasks.
   - Review access to encryption keys by checking the
     [AWS Key Management Service (AWS KMS) policies](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

2. **Separate data based on different
   classification levels**:
   - Use distinct AWS accounts for each data classification
     level.
   - Manage these accounts using
     [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

3. **Review Amazon S3 bucket and object
   permissions**:
   - Regularly review the level of access granted in Amazon S3 bucket policies.
   - Avoid using publicly readable or writeable buckets
     unless absolutely necessary.
   - Consider using
     [AWS Config](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") to detect publicly available buckets.
   - Use Amazon CloudFront to serve content from Amazon S3.
   - Verify that buckets that should not allow public access
     are properly configured to prevent it.
   - You can apply the same review process for databases and
     any other data sources that use IAM authentication, such
     as SQS or third-party data stores.

4. **Use AWS IAM Access Analyzer**:
   - You can configure [AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md")
     to analyze Amazon S3 buckets and generate findings when
     an S3 policy grants access to an external entity.

5. **Implement versioning and object
   locking mechanisms**:
   - Use
     [Amazon S3 versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") to preserve previous versions of
     objects, which provides recovery from accidental
     deletion or overwrites.
   - Use
     [Amazon S3 Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") to provide mandatory access
     control for objects, which prevents them from being
     deleted or overwritten, even by the root user, until the
     lock expires.
   - Use
     [Amazon Glacier Vault Lock](../../../amazonglacier/latest/dev/vault-lock.md "../../../amazonglacier/latest/dev/vault-lock.md") for archives stored in
     Amazon Glacier.

6. **Use Amazon S3 Inventory**:
   - You can use
     [Amazon S3 Inventory](../../../AmazonS3/latest/dev/storage-inventory.md "../../../AmazonS3/latest/dev/storage-inventory.md") to audit and report on the
     replication and encryption status of your S3 objects.

7. **Review Amazon EBS and AMI sharing
   permissions**:
   - Review your sharing permissions for
     [Amazon EBS](../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md "../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md") and
     [AMI
     sharing](../../../AWSEC2/latest/UserGuide/sharing-amis.md "../../../AWSEC2/latest/UserGuide/sharing-amis.md") to verify that your images and volumes
     are not shared with AWS accounts that are external to
     your workload.

8. **Review AWS Resource Access Manager
   Shares periodically**:
   - You can use
     [AWS Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") to share resources, such
     as AWS Network Firewall policies, Amazon Route 53
     resolver rules, and subnets, within your Amazon VPCs.
   - Audit shared resources regularly and stop sharing
     resources that no longer need to be shared.

## Resources

**Related best practices:**

- [SEC03-BP01 Define access requirements](sec_permissions_define.md "sec_permissions_define.md")
- [SEC03-BP02 Grant least privilege access](sec_permissions_least_privileges.md "sec_permissions_least_privileges.md")

**Related documents:**

- [AWS KMS Cryptographic Details Whitepaper](../../../kms/latest/cryptographic-details/intro.md "../../../kms/latest/cryptographic-details/intro.md")
- [Introduction
  to Managing Access Permissions to Your Amazon S3
  Resources](../../../AmazonS3/latest/dev/intro-managing-access-s3-resources.md "../../../AmazonS3/latest/dev/intro-managing-access-s3-resources.md")
- [Overview
  of managing access to your AWS KMS resources](../../../kms/latest/developerguide/control-access-overview.md "../../../kms/latest/developerguide/control-access-overview.md")
- [AWS Config Rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md")
- [Amazon S3 + Amazon CloudFront: A Match Made in the Cloud](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/ "https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/")
- [Using
  versioning](../../../AmazonS3/latest/dev/Versioning.md "../../../AmazonS3/latest/dev/Versioning.md")
- [Locking
  Objects Using Amazon S3 Object Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md")
- [Sharing
  an Amazon EBS Snapshot](../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md "../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md")
- [Shared
  AMIs](../../../AWSEC2/latest/UserGuide/sharing-amis.md "../../../AWSEC2/latest/UserGuide/sharing-amis.md")
- [Hosting
  a single-page application on Amazon S3](../../../prescriptive-guidance/latest/patterns/deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront.md "../../../prescriptive-guidance/latest/patterns/deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront.md")
- [AWS Global Condition Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")
- [Building
  a Data Perimeter on AWS](../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md "../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md")

**Related videos:**

- [Securing Your
  Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8 "https://youtu.be/Y1hE1Nkcxs8")
