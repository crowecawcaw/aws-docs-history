# Create keys and certificates for data encryption with Amazon EMR

Before you specify encryption options using a security configuration, decide on
the provider you want to use for keys and encryption artifacts. For example, you can
use AWS KMS or a custom provider that you create. Next, create the keys or key
provider as described in this section.

## Providing keys for encrypting data

at rest

You can use AWS Key Management Service (AWS KMS) or a custom key provider for at-rest data
encryption in Amazon EMR. When you use AWS KMS, charges apply for the storage and use
of encryption keys. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

This topic provides key policy details for a KMS key to be used with Amazon EMR,
as well as guidelines and code examples for writing a custom key provider class
for Amazon S3 encryption. For more information about creating keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

### Using AWS KMS keys for

encryption

The AWS KMS encryption key must be created in the same Region
as your Amazon EMR cluster instance and the Amazon S3 buckets used with EMRFS. If the key that you specify is in a different account from the one that you use to configure a cluster, you must specify the key using its ARN.

The role for the Amazon EC2 instance profile must have permissions to use
the KMS key you specify. The default role for the instance profile in Amazon EMR is
`EMR_EC2_DefaultRole`. If you use a different role for the instance
profile, or you use IAM roles for EMRFS requests to Amazon S3, make sure that each role is added as a key user as appropriate. This gives
the role permissions to use the KMS key. For more information, see [Using
Key Policies](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the _AWS Key Management Service Developer Guide_ and [Configure IAM roles for EMRFS requests to Amazon S3](emr-emrfs-iam-roles.md "emr-emrfs-iam-roles.md").

You can use the AWS Management Console to add your instance profile or EC2 instance profile to the list of key
users for the specified KMS key, or you can use the AWS CLI or an AWS SDK to
attach an appropriate key policy.

Note that Amazon EMR supports only [symmetric KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks"). You
cannot use an [asymmetric KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks "../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks") to encrypt data at rest in an Amazon EMR cluster.
For help determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md").

The procedure below describes how to add the default Amazon EMR instance profile,
`EMR_EC2_DefaultRole` as a _key user_
using the AWS Management Console. It assumes that you have already created a KMS key. To
create a new KMS key, see [Creating
Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

###### To add the EC2 instance profile for Amazon EMR to the list of encryption

key users

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Select the alias of the KMS key to modify.
4. On the key details page under **Key Users**,
   choose **Add**.
5. In the **Add key users** dialog box, select the appropriate role. The name of the default role is `EMR_EC2_DefaultRole`.
6. Choose **Add**.

### Enabling EBS encryption by

providing additional permissions for KMS keys

Beginning with Amazon EMR version 5.24.0, you can encrypt EBS root device and
storage volumes by using a security configuration option. To enable such
option, you must specify AWS KMS as your key provider. Additionally, you must
grant the service role `EMR_DefaultRole` with permissions to use
the AWS KMS key that you specify.

You can use the AWS Management Console to add the service role to the list of key users
for the specified KMS key, or you can use the AWS CLI or an AWS SDK to
attach an appropriate key policy.

The following procedure describes how to use the AWS Management Console to add the
default Amazon EMR service role `EMR_DefaultRole` as a _key
user_. It assumes that you have already created a KMS key.
To create a new KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
in the _AWS Key Management Service Developer Guide_.

###### To add the Amazon EMR service role to the list of encryption key

users

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Choose **Customer managed keys** in the left
   sidebar.
4. Select the alias of the KMS key to modify.
5. On the key details page under **Key Users**,
   choose **Add**.
6. In the **Add key users** section, select the
   appropriate role. The name of the default service role for Amazon EMR is
   `EMR_DefaultRole`.
7. Choose **Add**.

### Creating a custom key provider

When using a security configuration, you must specify a different provider
class name for local disk encryption and Amazon S3 encryption. The requirements for custom key provider
depend on whether you use local disk encryption and Amazon S3 encryption, as well as
the Amazon EMR release version.

Depending on the type of encryption you use when creating a custom key provider, the application must also implement different EncryptionMaterialsProvider interfaces.
Both interfaces are available in the AWS SDK for Java version 1.11.0 and later.

- To implement Amazon S3 encryption, use the [com.amazonaws.services.s3.model.EncryptionMaterialsProvider interface](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/EncryptionMaterialsProvider.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/EncryptionMaterialsProvider.md").
- To implement local disk encryption, use the [com.amazonaws.services.elasticmapreduce.spi.security.EncryptionMaterialsProvider interface](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/spi/security/EncryptionMaterialsProvider.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/spi/security/EncryptionMaterialsProvider.md").

You can use any strategy to provide encryption materials for the implementation. For example,
you might choose to provide static encryption materials or integrate with a more complex key management system.

If you’re using Amazon S3 encryption, you must use the encryption algorithms **AES/GCM/NoPadding** for custom encryption materials.

If you’re using local disk encryption, the encryption algorithm to use for custom encryption materials varies by EMR release.
For Amazon EMR 7.0.0 and lower, you must use **AES/GCM/NoPadding**. For Amazon EMR 7.1.0 and higher, you must use **AES**.

The EncryptionMaterialsProvider class gets encryption materials by encryption
context. Amazon EMR populates encryption context information at runtime to help the caller
determine the correct encryption materials to return.

###### Example: Using a custom key provider for

Amazon S3 encryption with EMRFS

When Amazon EMR fetches the encryption materials from the
EncryptionMaterialsProvider class to perform encryption, EMRFS optionally
populates the materialsDescription argument with two fields: the Amazon S3 URI
for the object and the JobFlowId of the cluster, which can be used by the
EncryptionMaterialsProvider class to return encryption materials
selectively.

For example, the provider may return different keys for different Amazon S3 URI prefixes. It
is the description of the returned encryption materials that is eventually
stored with the Amazon S3 object rather than the materialsDescription value that
is generated by EMRFS and passed to the provider. While decrypting an Amazon S3
object, the encryption materials description is passed to the
EncryptionMaterialsProvider class, so that it can, again, selectively return
the matching key to decrypt the object.

An EncryptionMaterialsProvider reference implementation is provided below.
Another custom provider, [EMRFSRSAEncryptionMaterialsProvider](https://github.com/awslabs/emr-sample-apps/tree/master/emrfs-plugins/EMRFSRSAEncryptionMaterialsProvider "https://github.com/awslabs/emr-sample-apps/tree/master/emrfs-plugins/EMRFSRSAEncryptionMaterialsProvider"), is available from GitHub.

```
import com.amazonaws.services.s3.model.EncryptionMaterials;
import com.amazonaws.services.s3.model.EncryptionMaterialsProvider;
import com.amazonaws.services.s3.model.KMSEncryptionMaterials;
import org.apache.hadoop.conf.Configurable;
import org.apache.hadoop.conf.Configuration;

import java.util.Map;

/**
 * Provides KMSEncryptionMaterials according to Configuration
 */
public class MyEncryptionMaterialsProviders implements EncryptionMaterialsProvider, Configurable{
  private Configuration conf;
  private String kmsKeyId;
  private EncryptionMaterials encryptionMaterials;

  private void init() {
    this.kmsKeyId = conf.get("my.kms.key.id");
    this.encryptionMaterials = new KMSEncryptionMaterials(kmsKeyId);
  }

  @Override
  public void setConf(Configuration conf) {
    this.conf = conf;
    init();
  }

  @Override
  public Configuration getConf() {
    return this.conf;
  }

  @Override
  public void refresh() {

  }

  @Override
  public EncryptionMaterials getEncryptionMaterials(Map<String, String> materialsDescription) {
    return this.encryptionMaterials;
  }

  @Override
  public EncryptionMaterials getEncryptionMaterials() {
    return this.encryptionMaterials;
  }
}

```

## Providing certificates for

encrypting data in transit with Amazon EMR encryption

With Amazon EMR release version 4.8.0 or later, you have two options for specifying
artifacts for encrypting data in transit using a security configuration:

- You can manually create PEM certificates, include them in a .zip file,
  and then reference the .zip file in Amazon S3.
- You can implement a custom certificate provider as a Java class. You
  specify the JAR file of the application in Amazon S3, and then provide the
  full class name of the provider as declared in the application. The
  class must implement the [TLSArtifactsProvider](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/spi/security/TLSArtifactsProvider.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/spi/security/TLSArtifactsProvider.md") interface available beginning with the
  AWS SDK for Java version 1.11.0.

Amazon EMR automatically downloads artifacts to each node in the cluster and later
uses them to implement the open-source, in-transit encryption features. For more
information about available options, see [Encryption in transit](emr-data-encryption-options.md#emr-encryption-intransit "emr-data-encryption-options.md#emr-encryption-intransit").

### Using PEM

certificates

When you specify a .zip file for in-transit encryption, the security
configuration expects PEM files within the .zip file to be named exactly as
they appear below:

| In-transit encryption certificates | File name | Required/optional                                                                                                                                                                                                                                                                                                                 | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| privateKey.pem                     | Required  | Private key                                                                                                                                                                                                                                                                                                                       |
| certificateChain.pem               | Required  | Certificate chain                                                                                                                                                                                                                                                                                                                 |
| trustedCertificates.pem            | Optional  | We recommend that you provide a certificate that isn't signed by the the Java default trusted root certification authority (CA) or an intermediate CA that can link to the Java default trusted root CA. We don't reocmmend that you use public CAs when you use wildcard certificates or when you disable hostname verification. | You likely want to configure the private key PEM file to be a wildcard certificate that enables access to the Amazon VPC domain in which your cluster instances reside. For example, if your cluster resides in us-east-1 (N. Virginia), you could specify a common name in the certificate configuration that allows access to the cluster by specifying `CN=*.ec2.internal` in the certificate subject definition. If your cluster resides in us-west-2 (Oregon), you could specify `CN=*.us-west-2.compute.internal`. If the provided PEM file in the encryption artifact doesn't have a wildcard character in the for the domain in the common name, you must change the value of `hadoop.ssl.hostname.verifier` to `ALLOW_ALL`. To do so in Amazon EMR releases 7.3.0 and higher, add the `core-site` classification when you submit configurations to a cluster. In releases lower than 7.3.0, add the configuration `"hadoop.ssl.hostname.verifier": "ALLOW_ALL"` directly into the `core-site.xml` file. This change is required because the default hostname verifier requires a hostname without the wildcard because all hosts in the cluster use it. For more information about EMR cluster configuration within an Amazon VPC, see [Configure networking in a VPC for Amazon EMR](emr-plan-vpc-subnet.md "emr-plan-vpc-subnet.md"). The following example demonstrates how to use [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to generate a self-signed X.509 certificate with a 2048-bit RSA private key. The key allows access to the issuer's Amazon EMR cluster instances in the `us-west-2` (Oregon) Region as specified by the `*.us-west-2.compute.internal` domain name as the common name. Other optional subject items, such as country (C), state (S), and Locale (L), are specified. Because a self-signed certificate is generated, the second command in the example copies the `certificateChain.pem` file to the `trustedCertificates.pem` file. The third command uses `zip` to create the `my-certs.zip` file that contains the certificates. ###### Important This example is a proof-of-concept demonstration only. Using self-signed certificates is not recommended and presents a potential security risk. For production systems, use a trusted certification authority (CA) to issue certificates. `$ openssl req -x509 -newkey rsa:2048 -keyout privateKey.pem -out certificateChain.pem -days 365 -nodes -subj '/C=US/ST=Washington/L=Seattle/O=MyOrg/OU=MyDept/CN=*.us-west-2.compute.internal' $ cp certificateChain.pem trustedCertificates.pem $ zip -r -X my-certs.zip certificateChain.pem privateKey.pem trustedCertificates.pem` |
