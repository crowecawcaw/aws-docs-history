

# Properties for Amazon S3 client-side encryption with S3A
<a name="emr-encryption-s3a-properties"></a>

To configure client-side encryption with S3A, there are several configuration properties that must be set in your core-site.xml settings. For more information about custom configuration settings, see [Configure applications](emr-configure-apps.html).


| Property | Default value | Description | 
| --- | --- | --- | 
| fs.s3a.encryption.algorithm | N/A | When set to CSE-KMS or CSE-CUSTOM, objects stored in Amazon S3 are encrypted using client-side encryption. | 
| fs.s3a.encryption.key | N/A | Applies when using CSE-KMS. The value of the KeyId, ARN, or alias of the KMS key used for encryption. | 
| fs.s3a.encryption.cse.kms.region | N/A | Applies when using CSE-KMS. The region where AWS KMS key is generated. By default the KMS region is set to values same as the S3 bucket/EMR cluster region. | 
| fs.s3a.encryption.cse.custom.keyring.class.name | N/A | Applies when using CSE-KMS. The fully qualified class name of custom key provider. | 
| fs.s3a.cse.customKeyringProvider.uri | N/A | Applies when using CSE-CUSTOM. The Amazon S3 URI where the JAR with the Custom implementation of Keyring is located. When you provide this URI, Amazon EMR automatically downloads the JAR to all nodes in the cluster. | 
| fs.s3a.encryption.cse.v1.compatibility.enabled | 'true' | This provides backward compatibility with older SDK clients like the one used with EMRFS. Turn this off, when there is no such dependency, for better performance. | 