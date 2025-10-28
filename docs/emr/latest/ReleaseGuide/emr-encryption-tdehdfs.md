# Transparent encryption in HDFS on Amazon EMR

Transparent encryption is implemented through the use of HDFS _encryption
zones_, which are HDFS paths that you define. Each encryption zone has its
own key, which is stored in the key server specified using the `hdfs-site`
configuration classification.

Beginning with Amazon EMR release version 4.8.0, you can use Amazon EMR security configurations
to configure data encryption settings for clusters more easily. Security configurations
offer settings to enable security for data in-transit and data at-rest in Amazon Elastic Block Store
(Amazon EBS) storage volumes and EMRFS data in Amazon S3. For more information, see [Encrypt data in transit and at
rest](../ManagementGuide/emr-data-encryption.md "../ManagementGuide/emr-data-encryption.md") in the _Amazon EMR Management Guide_.

Amazon EMR uses the Hadoop KMS by default; however, you can use another KMS that implements
the KeyProvider API operation. Each file in an HDFS encryption zone has its own unique
_data encryption key_, which is encrypted by the encryption zone
key. HDFS data is encrypted end-to-end (at-rest and in-transit) when data is written to
an encryption zone because encryption and decryption activities only occur in the
client.

You cannot move files between encryptions zones or from an encryption zone to
unencrypted paths.

The NameNode and HDFS client interact with the Hadoop KMS (or an alternate KMS you
configured) through the KeyProvider API operation. The KMS is responsible for storing
encryption keys in the backing keystore. Also, Amazon EMR includes the JCE unlimited strength
policy, so you can create keys at a desired length.

For more information, see [Transparent encryption in HDFS](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/TransparentEncryption.html "http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/TransparentEncryption.html") in the Hadoop documentation.

###### Note

In Amazon EMR, KMS over HTTPS is not enabled by default with Hadoop KMS. For more
information about how to enable KMS over HTTPS, see the [Hadoop KMS
documentation](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html").

## Configuring HDFS

transparent encryption

You can configure transparent encryption in Amazon EMR by creating keys and adding
encryption zones. You can do this in several ways:

- Using the Amazon EMR configuration API operation when you create a
  cluster
- Using a Hadoop JAR step with command-runner.jar
- Logging in to the master node of the Hadoop cluster and using the
  `hadoop key` and `hdfs crypto` command line
  clients
- Using the REST APIs for Hadoop KMS and HDFS

For more information about the REST APIs, see the respective documentation for
Hadoop KMS and HDFS.

###### To create encryption zones and their keys at cluster creation using the

CLI

The `hdfs-encryption-zones` classification in the configuration API operation
allows you to specify a key name and an encryption zone when you create a
cluster. Amazon EMR creates this key in Hadoop KMS on your cluster and configures the
encryption zone.

- Create a cluster with the following command.

```
aws emr create-cluster --release-label `emr-7.10.0` --instance-type m5.xlarge --instance-count 2 \
--applications Name=`App1` Name=`App2` --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

`myConfig.json`:

```
[
	{
		"Classification": "hdfs-encryption-zones",
		"Properties": {
			"/myHDFSPath1": "path1_key",
			"/myHDFSPath2": "path2_key"
		}
	}
]
```

###### To create encryption zones and their keys manually on the master node

1. Launch your cluster using an Amazon EMR release greater than 4.1.0.
2. Connect to the master node of the cluster with SSH.
3. Create a key within Hadoop KMS.

```
$ hadoop key create path2_key
path2_key has been successfully created with options Options{cipher='AES/CTR/NoPadding', bitLength=256, description='null', attributes=null}.
KMSClientProvider[http://ip-x-x-x-x.ec2.internal:16000/kms/v1/] has been updated.
```

###### Important

Hadoop KMS requires your key names to be lowercase. If you use a key
that has uppercase characters, then your cluster will fail during
launch. 4. Create the encryption zone path in HDFS.

```
$ hadoop fs -mkdir /myHDFSPath2
```

5. Make the HDFS path an encryption zone using the key that you
   created.

```
$ hdfs crypto -createZone -keyName path2_key -path /myHDFSPath2
Added encryption zone /myHDFSPath2
```

###### To create encryption zones and their keys manually using the AWS CLI

- Add steps to create the KMS keys and encryption zones manually with the
  following command.

```
aws emr add-steps --cluster-id j-2AXXXXXXGAPLF --steps Type=CUSTOM_JAR,Name="Create First Hadoop KMS Key",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hadoop key create path1_key\""] \
Type=CUSTOM_JAR,Name="Create First Hadoop HDFS Path",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hadoop fs -mkdir /myHDFSPath1\""] \
Type=CUSTOM_JAR,Name="Create First Encryption Zone",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hdfs crypto -createZone -keyName path1_key -path /myHDFSPath1\""] \
Type=CUSTOM_JAR,Name="Create Second Hadoop KMS Key",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hadoop key create path2_key\""] \
Type=CUSTOM_JAR,Name="Create Second Hadoop HDFS Path",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hadoop fs -mkdir /myHDFSPath2\""] \
Type=CUSTOM_JAR,Name="Create Second Encryption Zone",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[/bin/bash,-c,"\"hdfs crypto -createZone -keyName path2_key -path /myHDFSPath2\""]

```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

## Considerations for

HDFS transparent encryption

A best practice is to create an encryption zone for each application where they
may write files. Also, you can encrypt all of HDFS by using the
hdfs-encryption-zones classification in the configuration API and specify the root
path (/) as the encryption zone.

## Hadoop key management server

[Hadoop
KMS](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html") is a key management server that provides the ability to implement
cryptographic services for Hadoop clusters, and can serve as the key vendor for
[Transparent encryption in HDFS on Amazon EMR](emr-encryption-tdehdfs.md "emr-encryption-tdehdfs.md").
Hadoop KMS in Amazon EMR is installed and enabled by default when you select the Hadoop
application while launching an EMR cluster. The Hadoop KMS does not store the keys
itself except in the case of temporary caching. Hadoop KMS acts as a proxy between
the key provider and the client trustee to a backing keystore—it is not a
keystore. The default keystore that is created for Hadoop KMS is the Java
Cryptography Extension KeyStore (JCEKS). The JCE unlimited strength policy is also
included, so you can create keys with the desired length. Hadoop KMS also supports a
range of ACLs that control access to keys and key operations independently of other
client applications such as HDFS. The default key length in Amazon EMR is 256 bit.

To configure Hadoop KMS, use the hadoop-kms-site classification to change
settings. To configure ACLs, you use the classification kms-acls.

For more information, see the [Hadoop KMS
documentation](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html"). Hadoop KMS is used in Hadoop HDFS transparent encryption.
To learn more about HDFS transparent encryption, see the [HDFS transparent encryption](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/TransparentEncryption.html "http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/TransparentEncryption.html") topic in the Apache Hadoop
documentation.

###### Note

In Amazon EMR, KMS over HTTPS is not enabled by default with Hadoop KMS. To learn
how to enable KMS over HTTPS, see the [Hadoop KMS
documentation](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html").

###### Important

Hadoop KMS requires your key names to be lowercase. If you use a key that has
uppercase characters, then your cluster will fail during launch.

### Configuring Hadoop KMS in

Amazon EMR

Using Amazon EMR release version 4.6.0 or later, the `kms-http-port` is
9700 and `kms-admin-port` is 9701.

You can configure Hadoop KMS at cluster creation time using the configuration
API for Amazon EMR releases. The following are the configuration object
classifications available for Hadoop KMS:

| Hadoop KMS configuration classifications | Classification                                                            | Filename                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------- |
| hadoop-kms-site                          | `kms-site.xml`                                                            |
| hadoop-kms-acls                          | `kms-acls.xml`                                                            |
| hadoop-kms-env                           | `kms-env.sh`                                                              |
| hadoop-kms-log4j                         | `kms-log4j.properties`                                                    | ###### To set Hadoop KMS ACLs using the CLI <br>• Create a cluster with Hadoop KMS with ACLs using the following command: ``aws emr create-cluster --release-label `emr-7.10.0` --instance-type m5.xlarge --instance-count 2 \ --applications Name=`App1` Name=`App2` --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json`` ###### Note Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^). `myConfig.json`: `[ { "Classification": "hadoop-kms-acls", "Properties": { "hadoop.kms.blacklist.CREATE": "hdfs,foo,myBannedUser", "hadoop.kms.acl.ROLLOVER": "myAllowedUser" } } ]` ###### To disable Hadoop KMS cache using the CLI <br>• Create a cluster with Hadoop KMS `hadoop.kms.cache.enable` set to `false`, using the following command: ``aws emr create-cluster --release-label `emr-7.10.0` --instance-type m5.xlarge --instance-count 2 \ --applications Name=`App1` Name=`App2` --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json`` ###### Note Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^). `myConfig.json`: `[ { "Classification": "hadoop-kms-site", "Properties": { "hadoop.kms.cache.enable": "false" } } ]` ###### To set environment variables in the `kms-env.sh` script using the CLI <br>• Change settings in `kms-env.sh` via the `hadoop-kms-env` configuration. Create a cluster with Hadoop KMS using the following command: ``aws emr create-cluster --release-label `emr-7.10.0` --instance-type m5.xlarge --instance-count 2 \ --applications Name=`App1` Name=`App2` --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json`` ###### Note Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^). `myConfig.json`: ``[ { "Classification": "hadoop-kms-env", "Properties": {}, "Configurations": [ { "Classification": "export", "Properties": { "JAVA_LIBRARY_PATH": "`/path/to/files`", "KMS_SSL_KEYSTORE_FILE": "`/non/Default/Path/`.keystore", "KMS_SSL_KEYSTORE_PASS": "`myPass`" }, "Configurations": [] } ] } ]`` For information about configuring Hadoop KMS, see the [Hadoop KMS documentation](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html"). ## HDFS transparent encryption on EMR clusters with multiple master nodes [Apache Ranger](http://hadoop.apache.org/docs/current/hadoop-kms/index.html "http://hadoop.apache.org/docs/current/hadoop-kms/index.html") KMS is used in an Amazon EMR cluster with multiple primary nodes for transparent encryption in HDFS. Apache Ranger KMS stores its root key and Encryption Zone (EZ) keys in your Amazon RDS for an Amazon EMR cluster with multiple primary nodes. To enable transparent encryption in HDFS on an Amazon EMR cluster with multiple primary nodes, you must provide the following configurations. <br>• Amazon RDS or your own MySQL server connection URL to store the Ranger KMS root key and EZ key <br>• User name and password for MySQL <br>• Password for Ranger KMS root key <br>• Certificate Authority (CA) PEM file for SSL connection to MySQL server. You can download the certificate bundle for your AWS Region from [Download certificate bundles for Amazon RDS](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload"). You can provide these configurations by using `ranger-kms-dbks-site` classification and `ranger-kms-db-ca` classification, as the following example demonstrates. ``[ { "Classification": "ranger-kms-dbks-site", "Properties": { "ranger.ks.jpa.jdbc.url": "`jdbc:log4jdbc:mysql://mysql-host-url.xx-xxx-1.xxx.amazonaws.com:3306/rangerkms`", "ranger.ks.jpa.jdbc.user": "`mysql-user-name`", "ranger.ks.jpa.jdbc.password": "`mysql-password`", "ranger.db.encrypt.key.password": "`password-for-encrypting-a-master-key`" } }, { "Classification": "ranger-kms-db-ca", "Properties": { "ranger.kms.trust.ca.file.s3.url": "<S3-path-of-downloaded-pem-file>" } } ]`` The following are configuration object classifications for Apache Ranger KMS. Hadoop KMS configuration classifications | Classification | Description |
| ---                                      | ---                                                                       |
| ranger-kms-dbks-site                     | Change values in dbks-site.xml file of Ranger KMS.                        |
| ranger-kms-site                          | Change values in ranger-kms-site.xml file of Ranger KMS.                  |
| ranger-kms-env                           | Change values in the Ranger KMS environment.                              |
| ranger-kms-log4j                         | Change values in kms-log4j.properties file of Ranger KMS.                 |
| ranger-kms-db-ca                         | Change values for CA file on S3 for MySQL SSL connection with Ranger KMS. | **Considerations** <br>• It is highly recommended that you encrypt your Amazon RDS instance to improve security. For more information, see [Overview of encrypting Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/Overview.md#Overview.Encryption.Overview "../../../AmazonRDS/latest/UserGuide/Overview.md#Overview.Encryption.Overview"). <br>• It is highly recommended that you use separate MySQL database for each Amazon EMR cluster with multiple primary nodes for high security bar. <br>• To configure transparent encryption in HDFS on an Amazon EMR cluster with multiple primary nodes, you must specify the `hdfs-encryption-zones` classification while creating the cluster. Otherwise, Ranger KMS will not be configured or started. Reconfiguring `hdfs-encryption-zones` classification or any of the Hadoop KMS configuration classifications on a running cluster is not supported on Amazon EMR cluster with multiple primary nodes. <br>• The PEM certificate bundle that you downlaod from [Download certificate bundles for Amazon RDS](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload") groups multiple certificates into one file. Amazon EMR 7.3.0 and higher supports importing multiple certificates from the PEM file with the configuration `ranger.kms.trust.ca.file.s3.url`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
