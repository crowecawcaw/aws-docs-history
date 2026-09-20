

# DSSEC08-BP02 Control jurisdiction, access, and auditability of data-at-rest encryption keys
<a name="dssec08-bp02"></a>

 Carefully manage keys that protect data at rest throughout their lifecycle. This includes storage, rotation, and controlling access to key material required to secure data at rest. Monitor and log key usage. Where regulatory requirements mandate specific technical or operational controls, adhere to those requirements. 

 **Desired outcome:** 
+  You maintain full ownership and jurisdictional control of cryptographic keys that protect data at rest. 
+  Key creation, storage, and usage remain within authorized Regions and accounts. 
+  You can demonstrate through audit logs who accessed which keys, from where, and for what purpose. 

 **Common anti-patterns:** 
+  Sharing cryptographic keys across multiple accounts and workloads in a way that doesn't match data classification levels. 
+  Replicating cryptographic key material to other AWS Regions in foreign jurisdictions without considering data localization implications. 
+  Using cryptographic keys that a third party can access without authorization. 

 **Benefits of establishing this best practice:** 
+  Key ownership and usage stay restricted to authorized parties within authorized jurisdictions. 
+  Encryption key material remains within the Regions you select, supporting data localization requirements. 
+  Audit logs provide verifiable evidence of key access patterns for regulators and compliance teams. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Review AWS Key Management Service (AWS KMS) [best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/introduction.html). 

 Consider the following aspects to derive how you manage cryptographic keys. 
+  **Data classification attributes**: Classify data and attach sovereignty attributes as described in [DSSEC06-BP01](dssec06-bp01.html). Consider using separate encryption keys for each class of data. 
+  **Data localization requirements**: Several regulators mandate that specific data types, such as identity, payment, or healthcare data, are processed and stored within their jurisdictional boundaries. Verify that the encryption keys protecting this data also reside within those same boundaries. 
+  **Data residency scenarios**: Review the [navigating data residency scenarios](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/navigating-data-residency-scenarios.html) section of the Data Residency and Hybrid Cloud Lens. It describes constraints that might affect where you create, store, and replicate encryption keys. 
+  **Data sovereignty requirements**: Beyond data localization and data residency, consider data privacy legislation applicable to your workloads. These laws might affect key ownership and who can access keys. Review the questions outlined in [Strategizing for global expansion](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/global-expansion.html) in the AWS Privacy Reference Architecture (AWS PRA). 

 AWS KMS uses [FIPS 140-3 Level 3](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) validated hardware security modules to protect encryption keys. By choosing to create and manage your own keys within AWS KMS (that is, [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key)), you have full control over key policies, rotation, lifecycle, and usage. 

 Where possible, delegate cryptographic operations to the AWS service that handles your data. For example, configure Amazon S3 to encrypt data once it receives it from you, using a customer managed key under your control. The service performs encryption and decryption on your behalf, but AWS operators can't access your key or independently encrypt or decrypt your data. This adds an authorization step to every request: each request needs permission to access both the underlying resource and the key that protects it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Separate key usage roles from key management roles:** When deploying workloads using a multi-account strategy, we recommend placing AWS KMS keys in a different account than the workload that uses them for cryptographic operations. This separation verifies that no one with root access to the workload account can modify key permissions or accidentally delete keys. You can give permissions to use keys for cryptographic operations to IAM principals in other accounts, but management APIs (for example, kms:ScheduleKeyDeletion or kms:PutKeyPolicy) can only be given to principals in the [same account](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) as the key. 

    For stronger isolation, verify that IAM principals who manage keys have no direct access to the underlying AWS resources encrypted under those keys. This protects against a key administrator escalating their privileges to decrypt data. For example, an administrator for an AWS KMS key who grants themselves kms:Decrypt permission must not also have permission to make a s3:GetObject request on an object in an S3 bucket. Both permissions are required to read objects in the bucket, and the key administrator most likely should not have the ability to read that data. These steps assist in protecting the privacy of PII, PHI, and other confidential data. The following example IAM [Permission Boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) restricts the KMS key administrator to management actions only. It further restricts these actions to the eu-central-1 and eu-west-1 Regions to implement geographic controls supporting sovereignty goals. For example, to block administrators creating keys in unacceptable Regions. 
**Note**  
 The code snippet shown here is for illustration only and may not be accurate. Validate against your own environment and requirements unique to your workload. 

   ```
   {
   "Version": "2012-10-17",
   "Statement": [
       {
           "Sid": "AllowKMSManagementOnly",
           "Effect": "Allow",
           "Action": [
               "kms:CreateKey",
               "kms:EnableKey",
               "kms:DisableKey",
               "kms:ScheduleKeyDeletion",
               "kms:CancelKeyDeletion",
               "kms:PutKeyPolicy",
               "kms:TagResource",
               "kms:CreateAlias",
               "kms:DescribeKey",
               "kms:GetKeyPolicy",
               "kms:GetKeyRotationStatus",
               "kms:ListAliases",
               "kms:ListKeys"
           ],
           "Resource": "*",
           "Condition": {"StringEquals": 
               {"aws:RequestedRegion": ["eu-central-1", "eu-west-1"]}
           }
       }
       ]
   }
   ```

1.  **Record and control encryption context:** Each AWS KMS cryptographic operation with symmetric encryption KMS keys accepts an [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html). This is an optional set of non-secret key-value pairs that act as additional authenticated data (AAD). The encryption context is used primarily to verify integrity and authenticity. But you can also use the encryption context to control access to symmetric encryption AWS KMS keys in key policies and IAM policies. 

    Using the [kms:EncryptionContext:context-key](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context) condition key you can control which workloads are allowed to use your symmetric encryption KMS keys and for what purpose. The following example KMS key policy statement allows principals who can assume the role `RoleForShippingAddressValidation` to use the KMS key in a `GenerateDataKey` request, only when the encryption context in the request includes the `CustomerType:EU-Citizen` pair. 
**Note**  
 The code snippet shown here is for illustration only and may not be accurate. Validate against your own environment and requirements unique to your workload. 

   ```
   {
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:aws:iam::111122223333:role/RoleForShippingAddressValidation"
       },
       "Action": "kms:GenerateDataKey",
       "Resource": "*",
       "Condition": {
           "StringEquals": {
           "kms:EncryptionContext:CustomerType": "EU-Citizen"
           }
       }
   }
   ```

    The `kms:EncryptionContext:context-key` condition key is used to evaluate both the key and the value in the encryption context pair. You can also use variables in the encryption context. For example, "kms:EncryptionContext:user": "${aws:username}". 

    To evaluate only the key in each encryption context pair use the [kms:EncryptionContextKeys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context-keys). Be aware that this encryption context isn't secret and not encrypted, and appears in plaintext in [AWS CloudTrail Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for auditing purposes. 

1.  **Use AWS KMS Regional keys and Multi-Region Keys appropriately:** By default, a customer managed key is a Single-Region key. This means the key material can only be used within the AWS Region where it was created and can't be replicated. Single-Region KMS keys are inherently aligned to data localization requirements. Because the key material never leaves the Region where it was created, data encrypted with that key can only be decrypted in that same Region. 

    It is possible to create a replicated Multi-Region customer managed key with AWS KMS within the same [AWS partition](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). When you do so, AWS KMS creates a replica key in the other Regions you specify, copying the same key ID and other [shared properties](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-sync-properties). The result is two related Multi-Region keys (a primary key and a replica key) that can be used interchangeably by your applications that refer to the same AWS KMS key ARN. 

    You should decide whether a key is Single-Region or Multi-Region when you create it. You can't convert a Single-Region key into a Multi-Region key or the other way around. Use an AWS KMS Multi-Region key only when your code performs the cryptographic operation on data that you replicate yourself between Regions. A common use case is disaster recovery, where data you replicate to other AWS Regions can be decrypted in the future by the same code referencing the same AWS KMS key ARN as the primary key in the primary Region. 

    If you delegate encryption and decryption of your data to an AWS service as part of a cross-Region replication activity, you don't strictly need a Multi-Region key. For example, with AWS Backup, when you create a backup vault using a customer managed key and set up a cross-Region copy job, the data copy to another AWS Region is re-encrypted using the [key of the destination vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html#copy-encryption) you define. Each vault can use its own independent, single-Region customer managed key. Multi-Region keys are not required and offer no efficiency improvement. 

    [Carefully consider](https://docs.aws.amazon.com/kms/latest/developerguide/mrk-when-to-use.html) the security, data localization, and data residency implications of multi-Region keys to verify their use meets your digital sovereignty goals. Multi-Region keys increase security risk by replicating key material across Regions. Use Single-Region keys unless you have a specific technical requirement for Multi-Region keys (for example, disaster recovery with client-side encryption). Never use Multi-Region keys solely for convenience. For most use cases, including cross-Region replication by AWS services, Single-Region keys are more secure. 

1.  **Validate key policies**: Overly permissive key policies might grant unintended access. Validate key policies using [IAM Access Analyzer custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) before deployment. Review key policies regularly for overly permissive access. Never use wildcard principals such as (`"Principal": "*"`) in key policies without explicit deny conditions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 

 **Related documents:** 
+  [Using IAM policies with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html) 
+  [Key policies in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) 
+  [Establishing a European trust service provider for the AWS European Sovereign Cloud](https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/) 
+  [How to Protect the Integrity of Your Encrypted Data by Using AWS Key Management Service and EncryptionContext](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - KMS over the decade: How architecture evolved to earn customer trust-SEC218](https://www.youtube.com/watch?v=zW88_RNxNvw) 
+  [AWS re:Invent 2022 - Protecting secrets, keys, and data: Cryptography for the long term](https://www.youtube.com/watch?v=9vr3oMODIUE) 

 **Related services:** 
+  [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 