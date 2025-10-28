# Amazon S3 client-side encryption with S3A

Starting with Amazon Elastic Map Reduce (EMR) release version 7.6.0, the S3A filesystem connector now supports Amazon S3 client-side
encryption. This means that encryption and decryption of Amazon S3 data occurs directly within the S3A client on your computing
cluster. When using this feature, files are automatically encrypted before being uploaded to Amazon S3 and decrypted upon download. For
comprehensive details about the encryption methodology and its implementation, users can refer to [Protecting data using client-side
encryption](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md") in the _Amazon Simple Storage Service User Guide_.

When enabling Client-Side Encryption (CSE) with S3A in Amazon EMR, you have two key
management system options:

- **CSE-KMS** – This approach utilizes an AWS Key Management Service (KMS) key configured with policies
  specifically designed for Amazon EMR. For detailed information about key requirements, refer to the [Using AWS KMS keys for
  encryption](../ManagementGuide/emr-encryption-enable.md#emr-awskms-keys "../ManagementGuide/emr-encryption-enable.md#emr-awskms-keys") documentation.
- **CSE-CUSTOM** – This method allows you to integrate a custom Java class that
  provides the client-side root key responsible for encrypting and decrypting data.

###### Note

S3A Client-Side Encryption in EMR is inherently compatible with EMRFS Client-Side Encryption, meaning objects encrypted using EMRFS CSE can be
read through S3A CSE.

###### Topics

- [Setup CSE-KMS](emr-s3a-cse-kms.md "emr-s3a-cse-kms.md")
- [Setup CSE-CUSTOM](emr-s3a-cse-custom.md "emr-s3a-cse-custom.md")
- [Properties for Amazon S3 client-side encryption with S3A](emr-encryption-s3a-properties.md "emr-encryption-s3a-properties.md")
