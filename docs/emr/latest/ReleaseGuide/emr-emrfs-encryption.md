# Specifying Amazon S3 encryption using EMRFS properties

###### Important

Beginning with Amazon EMR release version 4.8.0, you can use security configurations to apply encryption settings more easily and with more options. We recommend using security configurations. For information, see [Configure data encryption](../ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption "../ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption"). The console instructions described in this section are available for release versions earlier than 4.8.0. If you use the AWS CLI to configure Amazon S3 encryption both in the cluster configuration and in a security configuration in subsequent versions, the security configuration overrides the cluster configuration.

When you create a cluster, you can specify server-side
encryption (SSE) or client-side encryption (CSE) for EMRFS data in Amazon S3 using the console or using `emrfs-site`
classification properties through the AWS CLI or EMR SDK. Amazon S3 SSE and CSE are mutually exclusive; you can choose either but
not both.

For AWS CLI instructions, see the appropriate section for your encryption type below.

###### To specify EMRFS encryption options using the AWS Management Console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Choose a **Release** of 4.7.2 or earlier.
4. Choose other options for **Software and Steps** as appropriate for your application, and then choose **Next**.
5. Choose settings in the **Hardware** and **General Cluster Settings** panes as appropriate for your application.
6. On the **Security** pane, under **Authentication and encryption**, select the **S3 Encryption (with EMRFS)** option to use.

###### Note

**S3 server-side encryption with KMS Key Management** (SSE-KMS) is not available when using Amazon EMR release version 4.4 or earlier.

    * If you choose an option that uses **AWS Key Management**, choose an **AWS KMS Key ID**. For more information, see [Using AWS KMS keys for EMRFS encryption](#emr-emrfs-awskms "#emr-emrfs-awskms").
    * If you choose **S3 client-side encryption with custom materials provider**, provide the **Class name** and the **JAR location**. For more information, see [Amazon S3 client-side
     encryption](emr-emrfs-encryption-cse.md "emr-emrfs-encryption-cse.md").

7. Choose other options as appropriate for your application and then choose **Create Cluster**.

## Using AWS KMS keys for EMRFS encryption

The AWS KMS encryption key must be created in the same Region
as your Amazon EMR cluster instance and the Amazon S3 buckets used with EMRFS. If the key that you specify is in a different account from the one that you use to configure a cluster, you must specify the key using its ARN.

The role for the Amazon EC2 instance profile must have permissions to use
the KMS key you specify. The default role for the instance profile in Amazon EMR is
`EMR_EC2_DefaultRole`. If you use a different role for the instance
profile, or you use IAM roles for EMRFS requests to Amazon S3, make sure that each role is added as a key user as appropriate. This gives
the role permissions to use the KMS key. For more information, see [Using
Key Policies](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the _AWS Key Management Service Developer Guide_ and [Configure IAM roles for EMRFS requests to Amazon S3](../ManagementGuide/emr-emrfs-iam-roles.md "../ManagementGuide/emr-emrfs-iam-roles.md").

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

## Amazon S3 server-side

encryption

All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded to an S3 bucket are automatically encrypted at rest, Amazon S3 encrypts data at the object level as it writes
the data to disk and decrypts the data when it is accessed. For more information
about SSE, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the
_Amazon Simple Storage Service User Guide_.

You can choose between two different key management systems when you specify
SSE in Amazon EMR:

- **SSE-S3** – Amazon S3 manages keys for
  you.
- **SSE-KMS** – You use an AWS KMS key to set up with policies suitable for Amazon EMR. For more information about key requirements for Amazon EMR,
  see [Using AWS KMS keys for encryption](../ManagementGuide/emr-encryption-enable.md#emr-awskms-keys "../ManagementGuide/emr-encryption-enable.md#emr-awskms-keys").

SSE with customer-provided keys (SSE-C) is not available for use with
Amazon EMR.

###### To create a cluster with SSE-S3 enabled using the AWS CLI

- Type the following command:

```
aws emr create-cluster --release-label `emr-4.7.2 or earlier` \
--instance-count 3 --instance-type m5.xlarge --emrfs Encryption=ServerSide
```

You can also enable SSE-S3 by setting the fs.s3.enableServerSideEncryption property to true in `emrfs-site` properties. See the example for SSE-KMS below and omit the property for Key ID.

###### To create a cluster with SSE-KMS enabled using the AWS CLI

###### Note

SSE-KMS is available only in Amazon EMR release version 4.5.0 and later.

- Type the following AWS CLI command to create a cluster with SSE-KMS,
  where `keyID` is an AWS KMS key, for example, `a4567b8-9900-12ab-1234-123a45678901`:

```
aws emr create-cluster --release-label `emr-4.7.2 or earlier` --instance-count `3` \
--instance-type `m5.xlarge` --use-default-roles \
--emrfs Encryption=ServerSide,Args=[fs.s3.serverSideEncryption.kms.keyId=`keyId`]
```

**--OR--**

Type the following AWS CLI command using the `emrfs-site` classification and
provide a configuration JSON file with contents as shown similar to `myConfig.json` in the example below:

```
aws emr create-cluster --release-label `emr-4.7.2 or earlier` --instance-count 3 --instance-type `m5.xlarge` `--applications Name=Hadoop` --configurations `file://myConfig.json` --use-default-roles

```

Example contents of **myConfig.json**:

```
[
  {
    "Classification":"emrfs-site",
    "Properties": {
       "fs.s3.enableServerSideEncryption": "true",
       "fs.s3.serverSideEncryption.kms.keyId":"`a4567b8-9900-12ab-1234-123a45678901`"
    }
  }
]
```

### Configuration properties for SSE-S3 and SSE-KMS

These properties can be configured using the `emrfs-site` configuration classification. SSE-KMS is available only in Amazon EMR release version 4.5.0 and later.

| Property                               | Default value | Description                                                                                                                         |
| -------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `fs.s3.enableServerSideEncryption`     | `false`       | When set to `true`, objects stored in Amazon S3 are encrypted using server-side encryption. If no key is specified, SSE-S3 is used. |
| `fs.s3.serverSideEncryption.kms.keyId` | `n/a`         | Specifies an AWS KMS key ID or ARN. If a key is specified, SSE-KMS is used.                                                         |
