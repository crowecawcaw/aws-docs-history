# Parquet modular encryption in

Hive

Parquet modular encryption provides columnar level access control and encryption
to enhance privacy and data integrity for data stored in Parquet file format. This
feature is available in Amazon EMR Hive starting with release 6.6.0.

Previously supported solutions for security and integrity, which include
encrypting files or encrypting the storage layer, are described in [Encryption
Options](../ManagementGuide/emr-data-encryption-options.md "../ManagementGuide/emr-data-encryption-options.md") in the Amazon EMR Management Guide. These solutions can be used for Parquet
files, but leveraging the new features of the integrated Parquet encryption
mechanism provides granular access to the column level, as well as improvements in
performance and security. Learn more about this feature on the Apache github page
[Parquet Modular Encryption](https://github.com/apache/parquet-format/blob/master/Encryption.md "https://github.com/apache/parquet-format/blob/master/Encryption.md").

Users pass configurations to Parquet readers and writers using Hadoop
configurations. The detailed configurations for users to configure readers and
writers to enable encryption as well as toggle advanced features are documented at
[PARQUET-1854: Properties-driven Interface to Parquet Encryption
Management](https://docs.google.com/document/d/1boH6HPkG0ZhgxcaRkGk3QpZ8X_J91uXZwVGwYN45St4/edit "https://docs.google.com/document/d/1boH6HPkG0ZhgxcaRkGk3QpZ8X_J91uXZwVGwYN45St4/edit")

## Usage examples

The following example covers creating and writing to a Hive table using AWS KMS
for managing encryption keys.

1. Implement a KmsClient for the AWS KMS service as described in the
   document [PARQUET-1373: Encryption Key Management Tools](https://docs.google.com/document/d/1bEu903840yb95k9q2X-BlsYKuXoygE4VnMDl9xz_zhk/edit "https://docs.google.com/document/d/1bEu903840yb95k9q2X-BlsYKuXoygE4VnMDl9xz_zhk/edit"). The
   following sample shows an implementation snippet.

```
package org.apache.parquet.crypto.keytools;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.kms.AWSKMS;
import com.amazonaws.services.kms.AWSKMSClientBuilder;
import com.amazonaws.services.kms.model.DecryptRequest;
import com.amazonaws.services.kms.model.EncryptRequest;
import com.amazonaws.util.Base64;
import org.apache.hadoop.conf.Configuration;
import org.apache.parquet.crypto.KeyAccessDeniedException;
import org.apache.parquet.crypto.ParquetCryptoRuntimeException;
import org.apache.parquet.crypto.keytools.KmsClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class AwsKmsClient implements KmsClient {

    private static final AWSKMS AWSKMS_CLIENT = AWSKMSClientBuilder
            .standard()
            .withRegion(Regions.US_WEST_2)
            .build();
    public static final Logger LOG = LoggerFactory.getLogger(AwsKmsClient.class);

    private String kmsToken;
    private Configuration hadoopConfiguration;

    @Override
    public void initialize(Configuration configuration, String kmsInstanceID, String kmsInstanceURL, String accessToken) throws KeyAccessDeniedException {
        hadoopConfiguration = configuration;
        kmsToken = accessToken;

    }

    @Override
    public String wrapKey(byte[] keyBytes, String masterKeyIdentifier) throws KeyAccessDeniedException {
        String value = null;
        try {
            ByteBuffer plaintext = ByteBuffer.wrap(keyBytes);

            EncryptRequest req = new EncryptRequest().withKeyId(masterKeyIdentifier).withPlaintext(plaintext);
            ByteBuffer ciphertext = AWSKMS_CLIENT.encrypt(req).getCiphertextBlob();

            byte[] base64EncodedValue = Base64.encode(ciphertext.array());
            value = new String(base64EncodedValue, Charset.forName("UTF-8"));
        } catch (AmazonClientException ae) {
            throw new KeyAccessDeniedException(ae.getMessage());
        }
        return value;
    }

    @Override
    public byte[] unwrapKey(String wrappedKey, String masterKeyIdentifier) throws KeyAccessDeniedException {
        byte[] arr = null;
        try {
            ByteBuffer ciphertext  = ByteBuffer.wrap(Base64.decode(wrappedKey.getBytes(StandardCharsets.UTF_8)));
            DecryptRequest request = new DecryptRequest().withKeyId(masterKeyIdentifier).withCiphertextBlob(ciphertext);
            ByteBuffer decipheredtext = AWSKMS_CLIENT.decrypt(request).getPlaintext();
            arr = new byte[decipheredtext.remaining()];
            decipheredtext.get(arr);
        } catch (AmazonClientException ae) {
            throw new KeyAccessDeniedException(ae.getMessage());
        }
        return arr;
    }
}

```

2. Create your AWS KMS encryption keys for the footer as well the columns
   with your IAM roles having access as described in [Creating
   keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_. The
   default IAM role is EMR_ECS_default.
3. On the Hive application on an Amazon EMR cluster, add the client above
   using the `ADD JAR` statement, as described in the [Apache Hive Resources documentation](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli#LanguageManualCli-HiveResources "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli#LanguageManualCli-HiveResources"). The following is an
   example statement:

```
ADD JAR 's3://location-to-custom-jar';
```

An alternative method is to add the JAR to the `auxlib` of
Hive using a bootstrap action. The following is an example line to be
added to the boostrap action:

```
aws s3 cp 's3://location-to-custom-jar' /usr/lib/hive/auxlib
```

4. Set the following configurations:

```
set parquet.crypto.factory.class=org.apache.parquet.crypto.keytools.PropertiesDrivenCryptoFactory;
set parquet.encryption.kms.client.class=org.apache.parquet.crypto.keytools.AwsKmsClient;
```

5. Create a Hive table with Parquet format and specify the AWS KMS keys in
   SERDEPROPERTIES and insert some data to it:

```
CREATE TABLE my_table(name STRING, credit_card STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe’
WITH SERDEPROPERTIES (
  'parquet.encryption.column.key’=<aws-kms-key-id-for-column-1>: credit_card’,
  'parquet.encryption.footer.key’='<aws-kms-key-id-for-footer>’)
STORED AS parquet
LOCATION “s3://<bucket/<warehouse-location>/my_table”;

INSERT INTO my_table SELECT
java_method ('org.apache.commons.lang.RandomStringUtils','randomAlphabetic',5) as name,
java_method ('org.apache.commons.lang.RandomStringUtils','randomAlphabetic',10) as credit_card
from (select 1) x lateral view posexplode(split(space(100),' ')) pe as i,x;

select * from my_table;
```

6. Verify that when you create an external table at the same location
   with no access to AWS KMS keys (for example, IAM role access denied),
   you cannot read the data.

```
CREATE EXTERNAL TABLE ext_table (name STRING, credit_card STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe’
STORED AS parquet
LOCATION “s3://<bucket>/<warehouse-location>/my_table”;

SELECT * FROM ext_table;
```

7. The last statement should throw the following exception:

```
Failed with exception java.io.IOException:org.apache.parquet.crypto.KeyAccessDeniedException: Footer key: access denied
```
