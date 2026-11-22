

# Identity and access management for AWS Key Management Service

AWS Identity and Access Management (IAM) helps you securely control access to AWS resources. Administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS KMS resources. For more information, see [Using IAM policies with AWS KMS](iam-policies.md).

[Key policies](key-policies.md) are the primary mechanism for controlling access to KMS keys in AWS KMS. Every KMS key must have a key policy. You can also use [IAM policies](iam-policies.md) and [grants](grants.md), along with key policies, to control access to your KMS keys. For more information, see [KMS key access and permissions](control-access.md).

You can also share a customer managed key with other AWS accounts through AWS Resource Access Manager (AWS RAM). A shared KMS key has a second key policy, named `AWS_RAM`, which AWS RAM creates and manages. Consumers of the resource share get the permissions in its managed permission. You control who can share your KMS keys with AWS RAM permissions, such as `ram:CreateResourceShare`, and with `kms:PutKeyPolicy` permission on the KMS key. For more information about controlling and monitoring shared KMS keys, see [Security best practices for sharing KMS keys](key-sharing-ram.md#key-sharing-ram-security).

If you are using an Amazon Virtual Private Cloud (Amazon VPC), you can [create an interface VPC endpoint](kms-vpc-endpoint.md) to AWS KMS powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/). You can also use VPC endpoint policies to determine which principals can access your AWS KMS endpoint, which API calls they can make, and which KMS key they can access.

**Topics**
+ [AWS managed policies for AWS Key Management Service](security-iam-awsmanpol.md)
+ [Using service-linked roles for AWS KMS](using-service-linked-roles.md)