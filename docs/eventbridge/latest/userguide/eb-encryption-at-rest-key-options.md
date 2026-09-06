

# KMS key options for data encryption in Amazon EventBridge
<a name="eb-encryption-at-rest-key-options"></a>

EventBridge uses an AWS owned key to encrypt data stored in resources. For each resource, you can choose the type of KMS key EventBridge uses to encrypt the data:
+ **AWS owned key**

  By default, EventBridge encrypts data using 256-bit Advanced Encryption Standard (AES-256) under an AWS owned key, which helps secure your data from unauthorized access.

  You can't view, manage, or use AWS owned keys, or audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data.

  In general, unless you are required to audit or control the encryption key that protects your resources, an AWS owned key is a good choice. AWS owned keys are completely free of charge (no monthly fees or usage fees), and they do not count against the AWS KMS quotas for your account. You don't need to create or maintain the key or its key policy.

  For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*. 
+ **Customer managed key**

  EventBridge supports the use of a symmetric customer managed key that you create, own, and manage. Because you have full control of this type of KMS key, you can perform such tasks as: 
  + Establishing and maintaining key policies
  + Establishing and maintaining IAM policies and grants
  + Enabling and disabling key policies
  + Rotating key cryptographic material
  + Adding tags
  + Creating key aliases
  + Scheduling keys for deletion

  For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*. 

  EventBridge supports [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) and [cross account access of keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

  Customer managed keys incur a monthly fee. For details, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/), and [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the *AWS Key Management Service Developer Guide*.
**Note**  
EventBridge does not support [schema discovery](eb-schema.md) on event buses encrypted using customer managed keys.