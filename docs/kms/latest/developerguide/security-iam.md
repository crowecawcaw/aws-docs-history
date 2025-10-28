# Identity and access management for AWS Key Management Service

AWS Identity and Access Management (IAM) helps you securely control access to AWS resources. Administrators
control who can be _authenticated_ (signed in) and _authorized_ (have permissions) to use AWS KMS resources. For more information, see
[Using IAM policies with AWS KMS](iam-policies.md "iam-policies.md").

[Key policies](key-policies.md "key-policies.md") are the primary mechanism for controlling
access to KMS keys in AWS KMS. Every KMS key must have a key policy. You can also
use [IAM policies](iam-policies.md "iam-policies.md") and [grants](grants.md "grants.md"),
along with key policies, to control access to your KMS keys. For more information, see [KMS key access and permissions](control-access.md "control-access.md").

If you are using an Amazon Virtual Private Cloud (Amazon VPC), you can [create an
interface VPC endpoint](kms-vpc-endpoint.md "kms-vpc-endpoint.md") to AWS KMS powered by
[AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). You can also use VPC endpoint policies to
determine which principals can access your AWS KMS endpoint, which API calls they can make, and
which KMS key they can access.

###### Topics

- [AWS managed policies for AWS Key Management Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Using service-linked roles for
  AWS KMS](using-service-linked-roles.md "using-service-linked-roles.md")
