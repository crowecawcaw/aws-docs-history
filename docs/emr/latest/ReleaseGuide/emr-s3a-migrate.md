

# Migration Guide: EMRFS to S3A Filesystem
<a name="emr-s3a-migrate"></a>

Starting with the EMR-7.10.0 release, S3A Filesystem is the default filesystem/s3 connector for EMR clusters for all S3 file schemes, including the following:
+ **s3://**
+ **s3n://**
+ **s3a://**

This change applies across all EMR deployments, including EC2, EKS, and EMR Serverless.

**Performance tuning for HBase on S3**  
If you use HBase on Amazon S3, for performance tuning guidance on affected versions, see [Configuring S3A read policy for HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-s3.html#emr-hbase-s3a-read-policy).

If you want to continue using EMRFS, you can configure this by adding the following property to the `core-site.xml` configuration file:

```
<property>
  <name>fs.s3.impl</name>
  <value>com.amazon.ws.emr.hadoop.fs.EmrFileSystem</value>
</property>
<property>
  <name>fs.s3n.impl</name>
  <value>com.amazon.ws.emr.hadoop.fs.EmrFileSystem</value>
</property>
```

## Migration of Existing EMRFS Configurations to S3A Configurations
<a name="emr-s3a-migration-of-existing-emrfs-configurations"></a>

**Note**  
Amazon EMR implements automatic configuration mapping between EMRFS and S3A when specific conditions are met. The mapping process automatically occurs when S3A configurations are undefined while corresponding EMRFS configurations are present. This automatic mapping functionality extends to bucket-level configurations, enabling seamless integration between EMRFS and S3A settings. As an illustration, when you configure a bucket-specific encryption setting in EMRFS using 'fs.s3.bucket.amzn-s3-demo-bucket1.serverSideEncryption.kms.keyId' with a value of "XYZ", the system automatically maps this to the equivalent S3A configuration by setting 'fs.s3a.encryption.key' to "XYZ" for the specified bucket amzn-s3-demo-bucket1.

The following predefined set of EMRFS configurations will be automatically translated to their corresponding S3A configuration equivalents. Any configurations currently implemented through cluster or job overrides will seamlessly transition to the S3A filesystem without requiring additional manual configuration or modifications.

By default, this configuration mapping feature is automatically activated. Users who wish to disable this automatic translation can do so by adding the following property to the core-site.xml configuration file.

```
<property>
  <name>fs.s3a.emrfs.compatibility.enable</name>
  <value>false</value>
</property>
```

**Note**  
The encryption key mapping from EMRFS (fs.s3.serverSideEncryption.kms.keyId or fs.s3.cse.kms.keyId) to S3A (fs.s3a.encryption.key) occurs only when either SSE-KMS or CSE-KMS encryption is enabled on either file system.


**EMRFS to S3A Configuration Mapping**  

| EMRFS Configuration Name | S3A Configuration Name | 
| --- | --- | 
| fs.s3.aimd.adjustWindow | fs.s3a.aimd.adjustWindow | 
| fs.s3.aimd.enabled | fs.s3a.aimd.enabled | 
| fs.s3.aimd.increaseIncrement | fs.s3a.aimd.increaseIncrement | 
| fs.s3.aimd.initialRate | fs.s3a.aimd.initialRate | 
| fs.s3.aimd.maxAttempts | fs.s3a.aimd.maxAttempts | 
| fs.s3.aimd.minRate | fs.s3a.aimd.minRate | 
| fs.s3.aimd.reductionFactor | fs.s3a.aimd.reductionFactor | 
| fs.s3.sts.endpoint | fs.s3a.assumed.role.sts.endpoint | 
| fs.s3.sts.sessionDurationSeconds | fs.s3a.assumed.role.session.duration | 
| fs.s3.authorization.roleMapping | fs.s3a.authorization.roleMapping | 
| fs.s3.authorization.ugi.groupName.enabled | fs.s3a.authorization.ugi.groupName.enabled | 
| fs.s3.credentialsResolverClass | fs.s3a.credentials.resolver | 
| fs.s3n.multipart.uploads.enabled | fs.s3a.multipart.uploads.enabled | 
| fs.s3n.multipart.uploads.split.size | fs.s3a.multipart.size | 
| fs.s3.serverSideEncryption.kms.customEncryptionContext | fs.s3a.encryption.context | 
| fs.s3.enableServerSideEncryption | fs.s3a.encryption.algorithm | 
| fs.s3.serverSideEncryption.kms.keyId / fs.s3.cse.kms.keyId | fs.s3a.encryption.key | 
| fs.s3.cse.kms.region | fs.s3a.encryption.cse.kms.region | 
| fs.s3.authorization.audit.enabled | fs.s3a.authorization.audit.enabled | 
| fs.s3.buckets.create.enabled | fs.s3a.bucket.probe | 
| fs.s3.delete.maxBatchSize | fs.s3a.bulk.delete.page.size | 
| fs.s3.filestatus.metadata.enabled | fs.s3a.metadata.cache.enabled | 
| fs.s3.maxConnections | fs.s3a.connection.maximum | 
| fs.s3.maxRetries | fs.s3a.retry.limit | 
| fs.s3.metadata.cache.expiration.seconds | fs.s3a.metadata.cache.expiration.seconds | 
| fs.s3.buffer.dir | fs.s3a.buffer.dir | 
| fs.s3.canned.acl | fs.s3a.acl.default | 
| fs.s3.positionedRead.optimization.enabled | fs.s3a.positionedRead.optimization.enabled | 
| fs.s3.readFullyIntoBuffers.optimization.enabled | fs.s3a.readFullyIntoBuffers.optimization.enabled | 
| fs.s3.signerType | fs.s3a.signing-algorithm | 
| fs.s3.storageClass | fs.s3a.create.storage.class | 
| fs.s3.threadpool.maxSize | fs.s3a.threads.max | 
| fs.s3.useRequesterPaysHeader | fs.s3a.requester.pays.enabled | 
| fs.s3n.block.size | fs.s3a.block.size | 
| fs.s3n.endpoint | fs.s3a.endpoint | 
| fs.s3n.ssl.enabled | fs.s3a.connection.ssl.enabled | 
| fs.s3.open.acceptsFileStatus | fs.s3a.open.acceptsFileStatus | 
| fs.s3.connection.maxIdleMilliSeconds | fs.s3a.connection.idle.time | 
| fs.s3.s3AccessGrants.enabled | fs.s3a.access.grants.enabled | 
| fs.s3.s3AccessGrants.fallbackToIAM | fs.s3a.access.grants.fallback.to.iam | 

### Considerations and Limitations
<a name="emr-s3a-migration-considerations-and-limitations"></a>
+ All the EMR engines – Spark, MapReduce, Flink, Tez, Hive etc will use S3A as the default S3 connector except for Trino and Presto engine.
+ EMR S3A does not support integration with EMR Ranger. Consider migrating to AWS Lake Formation.
+ AWS Lake Formation Support With RecordServer For EMR Spark with S3A is not supported - Consider using Spark Native FGAC.
+ AWS S3 Select is not supported.
+ Option to Periodically Clean Up Of Incomplete Multi Part Upload (MPU) is not available with S3A - Consider configuring [S3 bucket life cycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to clean up dangling MPUs.
+ Inorder to migrate from EMRFS to S3A while using S3 CSE-CUSTOM encryption, The custom key provider needs to be rewritten from [EMRFSRSAEncryptionMaterialsProvider](https://github.com/awslabs/emr-sample-apps/tree/master/emrfs-plugins/EMRFSRSAEncryptionMaterialsProvider) interface to [Keyring interface](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/choose-keyring.html). Refer to setting up S3A [CSE-CUSTOM](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-cse-custom.html) for more information.
+ Amazon S3 directories created using EMRFS are marked with a '\_$folder$' suffix, while directories created using S3A file system end with a '/' suffix, which is consistent with directories created through the AWS S3 console.
+ To use a custom S3 credential provider, set the S3A configuration property `fs.s3a.aws.credentials.provider` with the same credential provider class that was previously used in the EMRFS configuration `fs.s3.customAWSCredentialsProvider`.

### Unsupported EMRFS Configurations
<a name="emr-s3a-migration-unsupported"></a>

The following EMRFS configurations have been identified as unsupported or obsolete, and consequently, no direct mapping will be provided to their S3A configuration counterparts. These specific configurations will not be automatically translated or carried over during the migration to the S3A filesystem.


**Unsupported EMRFS Configurations and Reasons**  
<a name="unsupported-emrfs-configs"></a>
<table>
<thead>
  <tr><th>EMRFS Config Name</th><th>Reason For Not Supporting</th></tr>
</thead>
<tbody>
  <tr><td>fs.s3.consistent</td><td rowspan="30">Amazon S3 delivers <a href="https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/">strong read-after-write consistency</a> and hence EMRFS consistent view feature is not required.</td></tr>
  <tr><td>fs.s3.consistent.dynamodb.endpoint</td></tr>
  <tr><td>fs.s3.consistent.fastFirstRetrySeconds</td></tr>
  <tr><td>fs.s3.consistent.fastList</td></tr>
  <tr><td>fs.s3.consistent.fastList.batchSize</td></tr>
  <tr><td>fs.s3.consistent.fastList.prefetchMetadata</td></tr>
  <tr><td>fs.s3.consistent.metadata.accessKey</td></tr>
  <tr><td>fs.s3.consistent.metadata.autoCreate</td></tr>
  <tr><td>fs.s3.consistent.metadata.capacity.autoIncrease</td></tr>
  <tr><td>fs.s3.consistent.metadata.capacity.autoIncrease.factor</td></tr>
  <tr><td>fs.s3.consistent.metadata.capacity.autoIncrease.maxRead</td></tr>
  <tr><td>fs.s3.consistent.metadata.capacity.autoIncrease.maxWrite</td></tr>
  <tr><td>fs.s3.consistent.metadata.conditional</td></tr>
  <tr><td>fs.s3.consistent.metadata.delete.ttl.enabled</td></tr>
  <tr><td>fs.s3.consistent.metadata.delete.ttl.expiration.seconds</td></tr>
  <tr><td>fs.s3.consistent.metadata.etag.verification.enabled</td></tr>
  <tr><td>fs.s3.consistent.metadata.read.capacity</td></tr>
  <tr><td>fs.s3.consistent.metadata.read.capacity.limit</td></tr>
  <tr><td>fs.s3.consistent.metadata.secretKey</td></tr>
  <tr><td>fs.s3.consistent.metadata.tableName</td></tr>
  <tr><td>fs.s3.consistent.metadata.write.capacity</td></tr>
  <tr><td>fs.s3.consistent.metadata.write.capacity.limit</td></tr>
  <tr><td>fs.s3.consistent.notification.CloudWatch</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS.batchSize</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS.customMsg</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS.pathReportLimit</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS.pullWaitTimeSeconds</td></tr>
  <tr><td>fs.s3.consistent.notification.SQS.queueName</td></tr>
  <tr><td>fs.s3.consistent.retryCount</td></tr>
  <tr><td>fs.s3.cse.cryptoStorageMode</td><td rowspan="4">Unlike EMRFS which uses AWS SDK V1. S3A uses AWS SDK V2 where these options are not supported.</td></tr>
  <tr><td>fs.s3.cse.cryptoStorageMode.deleteInstructionFiles.enabled</td></tr>
  <tr><td>fs.s3.cse.encryptionV2.enabled</td></tr>
  <tr><td>fs.s3.cse.materialsDescription.enabled</td></tr>
  <tr><td>fs.s3.multipart.clean.age.threshold</td><td rowspan="2">Periodically Clean Up Of Incomplete Multi Part Upload (MPU) is not available with S3A - Instead configure S3 <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html">bucket life cycle policy</a> to clean up dangling MPUs.</td></tr>
  <tr><td>fs.s3.multipart.clean.enabled</td></tr>
  <tr><td>fs.s3.multipart.clean.jitter.max</td><td rowspan="4">The feature was added to avoid multi-part upload threads getting stuck or slow. S3A does not exihit similar issue and hence not required.</td></tr>
  <tr><td>fs.s3.multipart.fraction.part.avg.completion.time</td></tr>
  <tr><td>fs.s3.multipart.part.attempts</td></tr>
  <tr><td>fs.s3.multipart.th.fraction.parts.completed</td></tr>
  <tr><td>fs.s3.instanceProfile.retryCount</td><td rowspan="31">These are EMRFS specific configuartions which are not required in S3A due to functionality and architectural differences.</td></tr>
  <tr><td>fs.s3.instanceProfile.retryPeriodSeconds</td></tr>
  <tr><td>fs.s3.externalStagedFiles.maxActiveTasks</td></tr>
  <tr><td>fs.s3.folderObject.autoAction.disabled</td></tr>
  <tr><td>fs.s3.folderObject.autoInsert</td></tr>
  <tr><td>fs.s3.getObject.initialSocketTimeoutMilliseconds</td></tr>
  <tr><td>fs.s3.listFiles.incrementalFetch.enabled</td></tr>
  <tr><td>fs.s3.listFilesInOrder.includeDescendantsOfFiles</td></tr>
  <tr><td>fs.s3.listObjects.encodingType</td></tr>
  <tr><td>fs.s3.buckets.create.region</td></tr>
  <tr><td>fs.s3.configuration.load.enablebled</td></tr>
  <tr><td>fs.s3.create.allowFileNameEndsWithFolderSuffix</td></tr>
  <tr><td>fs.s3.open.lazyConnection.enabled</td></tr>
  <tr><td>fs.s3.region.fallback</td></tr>
  <tr><td>fs.s3.region.retryCount</td></tr>
  <tr><td>fs.s3.region.retryPeriodSeconds</td></tr>
  <tr><td>fs.s3.rename.algorithm.version</td></tr>
  <tr><td>fs.s3.requestHandler.classNames</td></tr>
  <tr><td>fs.s3.requestStatistics.enabled</td></tr>
  <tr><td>fs.s3.requestStatistics.sinks</td></tr>
  <tr><td>fs.s3.retryPeriodSeconds</td></tr>
  <tr><td>fs.s3.seekStrategy</td></tr>
  <tr><td>fs.s3.threadpool.buffer.size</td></tr>
  <tr><td>fs.s3.threadpool.maxSize</td></tr>
  <tr><td>fs.s3.useDirectoryHeaderAsFolderObject</td></tr>
  <tr><td>fs.s3n.filestatuscache.enable</td></tr>
  <tr><td>fs.s3.delete.retryCount</td></tr>
  <tr><td>fs.s3.s3AccessGrants.cacheSize</td></tr>
  <tr><td>fs.s3.s3AccessGrants.retryDelayBase</td></tr>
  <tr><td>fs.s3.s3AccessGrants.throttledRetryDelayBase</td></tr>
  <tr><td>fs.s3.s3AccessGrants.maxRetries</td></tr>
</tbody>
</table>
