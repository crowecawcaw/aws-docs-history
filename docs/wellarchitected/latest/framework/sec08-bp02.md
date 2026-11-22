

# SEC08-BP02 Enforce encryption at rest

 Encrypting data at rest keeps it confidential even when the storage layer is exposed. Because storage is easy to create and misconfigure, make encryption the default for new resources and keep an inventory of any unencrypted data. 

 **Desired outcome:** 
+  Your private data is encrypted by default whenever it is at rest. 
+  You maintain an inventory of unencrypted data and know the controls that protect it. 
+  Your encryption keys map to data classifications rather than a single key protecting everything. 
+  You monitor the use of encryption and decryption keys for unexpected access. 

 **Common anti-patterns:** 
+  Teams create storage without encrypt-by-default configurations. 
+  Administrators grant overly permissive access to decryption keys. 
+  Teams do not monitor the use of encryption and decryption keys. 
+  Teams store data unencrypted. 
+  Teams use one encryption key for all data, regardless of its usage, type, or classification. 

 **Benefits of establishing this best practice:** 
+  Your data stays confidential even if an unauthorized party reaches the underlying storage. 
+  A single exposed key affects only the data in its classification, not your entire estate. 
+  Encrypt-by-default removes the human error of forgetting to turn encryption on. 
+  Detective controls give you an auditable record of which resources remain unencrypted. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Manual, per-resource encryption fails at scale because people can eventually forget, and one unencrypted volume or bucket is enough to expose sensitive data. Encrypt-by-default settings make encryption the default for new resources. Pair that with detective controls that flag any unencrypted resource, so you catch both deliberately-provisioned resources and resources that appear through automation or drift. 

 Using a single key, or a handful of keys, for all data means any principal that can decrypt one thing can often decrypt everything. This collapses the access boundaries you are building. Map keys to classification levels so the scope of impact of an exposed or over-shared key is limited to data at that level. Data classification is a prerequisite for this mapping. 

 Managed keys reduce operational work, while customer managed keys give you control over rotation and access policy for data that needs fine-grained restriction. Choose customer managed keys when a data classification demands that you own the policy that governs decryption. 

 Server-side encryption covers most workloads, but some data must be protected before it reaches storage. Client-side encryption addresses cases where the storage service must never see plaintext, or where regulations require encryption to happen in your environment. With envelope encryption and a client-side toolkit, your application encrypts each object under a unique data key wrapped by a key you control. A single-tenant hardware security module fits specialized cases, such as protecting a private certificate authority key or enabling transparent data encryption for databases. These options add development and operational effort, so reserve them for data with a sensitivity that justifies the cost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map keys to your data classifications:** Create separate keys for different classification levels, and write [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) that limit each key to the principals allowed to access that level. For example, use one key for production data and a different key for development or test data. Where a production account must decrypt artifacts produced in a development account, grant that cross-account access explicitly in the key policy. 

1.  **Enable default encryption for object storage:** Confirm [Amazon S3 default bucket encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) is in effect so new objects are encrypted on write. 

1.  **Enable default encryption for block storage:** Turn on [default encryption for new Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) so every new volume is encrypted, using either the default AWS managed key or a customer managed key. 

1.  **Encrypt machine images:** Create [encrypted Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html) by copying an existing AMI with encryption configured, which encrypts root volumes and snapshots. 

1.  **Encrypt managed databases:** Enable [Amazon RDS encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) for your database clusters, instances, and snapshots at rest. 

1.  **Add detective controls for unencrypted resources:** Use [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to check encryption status for [Amazon EBS volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html), [Amazon RDS instances](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html), and [Amazon S3 buckets](https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html), and to build your inventory of unencrypted data. 

1.  **Encrypt data client-side where required:** For data that must be encrypted before upload, use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) for envelope encryption, or [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) when you need a single-tenant hardware security module. 

1.  **Extend encryption to remaining services:** For every other service in your workload, review its [security documentation](https://docs.aws.amazon.com/security/) to confirm and configure its encryption options. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP01 Implement secure key management](sec08-bp01.md) 
+  [SEC08-BP03 Automate data at rest protection](sec08-bp03.md) 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md) 

 **Related documents:** 
+  [Choosing an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/guide.html) 
+  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) 
+  [AWS Key Management Service cryptographic details](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html) 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) 
+  [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) 
+  [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) 
+  [Protecting data using encryption in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) 

 **Related videos:** 
+  [Amazon S3 data encryption options explained](https://aws.amazon.com/video/watch/07d5a9abf3d/) 
+  [AWS Encryption and Authorization for Security](https://aws.amazon.com/video/watch/22b31d63959/) 