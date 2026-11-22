

# SEC08-BP01 Implement secure key management

 Secure key management covers how you generate, store, control access to, rotate, and monitor key material across its lifecycle. Treat keys as the most sensitive asset in your workload 

 **Desired outcome:** 
+  You have an automated, repeatable key management mechanism that scales across your workloads. 
+  Your access to key material follows least privilege, and no human operator can read key material in plaintext. 
+  You monitor key usage, and you rotate key material through an automated process. 
+  Your key management balances the availability, confidentiality, and integrity of key material. 

 **Common anti-patterns:** 
+  Teams allow human operators to access unencrypted key material. 
+  Developers write custom cryptographic algorithms instead of using vetted, standard implementations. 
+  Administrators grant overly broad permissions to key material. 
+  Teams store keys without audit logging, so key operations go unreviewed. 
+  Teams schedule key deletion without a review process, and lose the data the key protected. 

 **Benefits of establishing this best practice:** 
+  Your content is protected against unauthorized access, because access to the keys is tightly scoped and monitored. 
+  You can demonstrate technical controls that align with regulatory requirements to encrypt data. 
+  Automated rotation and centralized policy reduce the manual work and human error that lead to key exposure. 
+  Audit logs of key operations give you an investigation trail for suspected misuse. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Most encryption at scale uses *envelope encryption*, where a data key encrypts the data and a separate key encrypts the data key. This guards large volumes of data with a small number of tightly controlled root keys, so the security of your data depends on how well you protect those root keys. A dedicated key management system gives you secure storage, access control, rotation, and audit logging in one place. 

 You choose between AWS managed and customer managed keys. *Managed keys*, which AWS generates and rotates, remove operational burden when you do not need direct control over the key material. *Customer managed keys* give you control over rotation, access policy, and deletion, at the cost of more administration. Choose customer managed keys when data sensitivity, data sovereignty, or regulatory obligations require you to own the key policy and rotation schedule. Otherwise, use managed keys. 

 Where you store keys is an organizational decision. In a multi-account structure, keeping keys in the same account as the workload assigns ownership to the team that runs the workload. A centralized key account fits when one key is shared across several accounts, as it requires cross-account policies and concentrates control and risk. [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) provides durable, redundant key storage backed by hardware security modules, and [many AWS services integrate with it](https://aws.amazon.com/kms/features/#integration) so encryption is transparent to the workload. There is no mechanism to export a KMS key in plaintext. 

 [Key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) are the primary access control for a KMS key, alongside IAM policies and grants that let services encrypt and decrypt on your behalf. Overly broad key permissions negate the value of encryption, so review the [guidance for access control to your keys](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html) and keep grants narrow. 

 Without monitoring, a principal under unauthorized control can decrypt data without any oversight for the access pattern change. Log key operations and review them, paying particular attention to changes in volume and destruction events. 

 Deleting a key destroys every ciphertext it protected. AWS KMS enforces a mandatory [waiting period](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html#deleting-keys-how-it-works) before deletion, defaulting to 30 days with a 7-day minimum, which gives administrators time to cancel an accidental or unauthorized deletion. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose the key type for each use case:** Decide between [AWS managed and customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) based on the control, sovereignty, and rotation requirements you established in guidance. For most services, AWS owned or AWS managed keys provide encryption at rest without managing key material or policies. When you need custom key storage, evaluate [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) or the [external key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html). 

1.  **Map how each service integrates with AWS KMS:** Review the services in your workload to understand their encryption options. See [how AWS services use AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html) and the Encryption at Rest topic in each service guide. Confirm downstream artifacts inherit encryption, such as snapshots created from encrypted volumes. 

1.  **Provision keys and scope access:** Create keys in [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) and apply [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and IAM policies that grant least privilege. Follow the [best practices for access control to your keys](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html), and keep no human operator able to read key material in plaintext. 

1.  **Detect overly broad key policies:** Enable [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to review and alert on permissive key policies. Add [custom policy checks](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoPublicAccess.html) to confirm that a policy update does not grant public access to a key. 

1.  **Add client-side envelope encryption where needed:** When your application must encrypt data before it reaches storage, use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) with AWS KMS integration to implement envelope encryption. 

1.  **Enable configuration monitoring for keys:** Turn on [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html) to receive findings for misconfigured key policies, keys scheduled for deletion, and keys without automated rotation. 

1.  **Set the right logging level for key activity:** Log KMS operations in AWS CloudTrail and review them periodically. Because read-only KMS events are logged and can be voluminous, consider a [separate trail for KMS activity](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) and pay particular attention to key destruction events. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md) 
+  [SEC08-BP04 Enforce access control](sec08-bp04.md) 
+  [SEC09-BP01 Implement secure key and certificate management](sec09-bp01.md) 

 **Related documents:** 
+  [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Choosing an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/guide.html) 
+  [Protecting data using encryption in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) 
+  [Envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#enveloping) 
+  [AWS Digital Sovereignty Pledge: Control without compromise](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/) 
+  [Demystifying AWS KMS key operations, bring your own key, custom key store, and ciphertext portability](https://aws.amazon.com/blogs/security/demystifying-kms-keys-operations-bring-your-own-key-byok-custom-key-store-and-ciphertext-portability/) 
+  [AWS Key Management Service cryptographic details](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html) 

 **Related videos:** 
+  [AWS KMS: Secure cloud data encryption](https://aws.amazon.com/video/watch/e145cdc6b40/) 
+  [AWS Encryption and Authorization for Security](https://aws.amazon.com/video/watch/22b31d63959/) 