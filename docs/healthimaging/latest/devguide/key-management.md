

# Key management
<a name="key-management"></a>

AWS KMS keys (KMS keys) are the primary resource in AWS Key Management Service. You can also generate data keys for use outside of AWS KMS.

## AWS owned KMS key
<a name="AWS-owned-cmk"></a>

HealthImaging uses these keys by default to automatically encrypt potentially sensitive information such as personally identifiable or Private Health Information (PHI) data at rest. AWS owned KMS keys aren't stored in your account. They're part of a collection of KMS keys that AWS owns and manages for use in multiple AWS accounts. AWS services can use AWS owned KMS keys to protect your data. You can't view, manage, use AWS owned KMS keys, or audit their use. However, you don't need to do any work or change any programs to protect the keys that encrypt your data.

You're not charged a monthly fee or a usage fee if you use AWS owned KMS keys, and they don't count against AWS KMS quotas for your account. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*.

## Customer managed KMS keys
<a name="customer-owned-cmk"></a>

If you want full control over AWS KMS lifecycle and usage, HealthImaging supports the use of a symmetric customer-managed KMS key that you create, own, and manage. Because you have full control of this layer of encryption, you can perform such tasks as:
+ Establishing and maintaining key policies, IAM policies, and grants
+ Rotating key cryptographic material
+ Enabling and disabling key policies
+ Adding tags
+ Creating key aliases
+ Scheduling keys for deletion

You can also use CloudTrail to track the requests that HealthImaging sends to AWS KMS on your behalf. Additional AWS KMS charges apply. For more information, see [ Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.