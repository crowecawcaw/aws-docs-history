

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Data encryption using AWS KMS
<a name="encryption"></a>

Amazon FSx File Gateway supports SMB encryption up to the latest SMB v3.1.1 specification, including AES 128 CCM and AES 128 GCM. Compatible clients will connect using encryption automatically. Additionally, FSx File Gateway uses SMB encryption when it communicates with FSx for Windows File Server in AWS. You must configure an Direct Connect link to AWS, and set appropriate policies to allow SMB traffic and management traffic to pass through to AWS.

**Encrypting a file system**  
For information see, [Data Encryption in Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption.html) in the *Amazon FSx for Windows File Server User Guide*.

**When using AWS KMS to encrypt your data, keep the following in mind:**
+ Your data is encrypted at rest in the cloud. That is, the data is encrypted in Amazon FSx.
+ IAM users must have the required permissions to call the AWS KMS API operations. For more information, see [Using IAM policies with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html) in the *AWS Key Management Service Developer Guide*.

**Important**  
When you use an AWS KMS key for server-side encryption, you must choose a symmetric key. Storage Gateway does not support asymmetric keys. For more information, see [Using symmetric and asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

For more information about AWS KMS, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)