# Setup CSE-CUSTOM

To use CSE-CUSTOM, you must create a custom key provider by implementing
the [Keyring](../../../encryption-sdk/latest/developer-guide/choose-keyring.md "../../../encryption-sdk/latest/developer-guide/choose-keyring.md") interface. Here's a sample implementation:

```
public class CustomKeyring implements Keyring {
  public CustomKeyring()  {
    // custom code
  }

  @Override
  public EncryptionMaterials onEncrypt(EncryptionMaterials encryptionMaterials) {
    // custom code
  }

  @Override
  public DecryptionMaterials onDecrypt(DecryptionMaterials decryptionMaterials,
      List`EncryptedDataKey` list) {
    // custom code
  }
```

You can enable Client-Side Encryption Custom Keys (CSE-CUSTOM) in two primary scopes:

- The first scope is cluster-wide configuration:

```
[
  {
    "Classification":"core-site",
    "Properties": {
       "fs.s3a.encryption.algorithm": "CSE-CUSTOM",
       "fs.s3a.cse.customKeyringProvider.uri":"`S3 path of custom jar`",
       "fs.s3a.encryption.cse.custom.keyring.class.name":"`fully qualified class name`"
    }
  }
]
```

- The second is job or application-specific configuration. CSE-CUSTOM can be setup for a specific Spark application as
  follows:

```
spark-submit --conf spark.hadoop.fs.s3a.encryption.algorithm=CSE-CUSTOM --conf spark.hadoop.fs.s3a.encryption.cse.custom.keyring.class.name=`fully qualified class name`
```

###### Note

Ensure that the required custom jar for generating encryption/decryption keys is present in the class path.
