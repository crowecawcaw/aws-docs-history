# Configure consistent view

You can configure additional settings for consistent view by providing them using configuration properties for `emrfs-site` properties. For example, you can choose a different default
DynamoDB throughput by supplying the following arguments to the CLI
`--emrfs` option, using the emrfs-site configuration classification (Amazon EMR release version 4.x and later only), or a bootstrap action to configure the emrfs-site.xml file on the master node:

###### Example Changing default metadata read and write values at cluster launch

```
aws emr create-cluster --release-label `emr-7.11.0` --instance-type `m5.xlarge` \
--emrfs Consistent=`true`,Args=[fs.s3.consistent.metadata.read.capacity=`600`,\
fs.s3.consistent.metadata.write.capacity=`300`] --ec2-attributes KeyName=`myKey`
```

Alternatively, use the following configuration file and save it
locally or in Amazon S3:

```
[
    {
      "Classification": "emrfs-site",
      "Properties": {
        "fs.s3.consistent.metadata.read.capacity": "600",
        "fs.s3.consistent.metadata.write.capacity": "300"
      }
    }
 ]
```

Use the configuration you created with the following syntax:

```
aws emr create-cluster --release-label `emr-7.11.0` --applications Name=Hive \
--instance-type m5.xlarge --instance-count 2 --configurations file://./myConfig.json
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

The following options can be set using configurations or AWS CLI
`--emrfs` arguments. For information about those arguments, see
the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

`emrfs-site.xml` Properties for consistent
view| Property | Default value | Description |
| --- | --- | --- |
| `fs.s3.consistent` | `false` | When set to `true`, this property<br>configures EMRFS to use DynamoDB to provide<br>consistency. |
| `fs.s3.consistent.retryPolicyType` | `exponential` | This property identifies the policy to use when retrying<br>for consistency issues. Options include: exponential, fixed,<br>or none. |
| `fs.s3.consistent.retryPeriodSeconds` | `1` | This property sets the length of time to wait between<br>consistency retry attempts. |
| `fs.s3.consistent.retryCount` | `10` | This property sets the maximum number of retries when<br>inconsistency is detected. |
| `fs.s3.consistent.throwExceptionOnInconsistency` | `true` | This property determines whether to throw or log a<br>consistency exception. When set to<br>`true`, a<br>`ConsistencyException` is thrown. |
| `fs.s3.consistent.metadata.autoCreate` | `true` | When set to `true`, this property<br>enables automatic creation of metadata tables. |
| `fs.s3.consistent.metadata.etag.verification.enabled` | `true` | With Amazon EMR 5.29.0, this property is enabled by default. When enabled, EMRFS uses S3 ETags to<br>verify that objects being read are the latest available version.<br>This feature is helpful for read-after-update use cases in which<br>files on S3 are being overwritten while retaining the same name.<br>This ETag verification capability currently does not work with S3<br>Select. |
| `fs.s3.consistent.metadata.tableName` | `EmrFSMetadata` | This property specifies the name of the metadata table in<br>DynamoDB. |
| `fs.s3.consistent.metadata.read.capacity` | `500` | This property specifies the DynamoDB read capacity to<br>provision when the metadata table is created. |
| `fs.s3.consistent.metadata.write.capacity` | `100` | This property specifies the DynamoDB write capacity to<br>provision when the metadata table is created. |
| `fs.s3.consistent.fastList` | `true` | When set to `true`, this property<br>uses multiple threads to list a directory (when necessary).<br>Consistency must be enabled in order to use this<br>property. |
| `fs.s3.consistent.fastList.prefetchMetadata` | `false` | When set to `true`, this property<br>enables metadata prefetching for directories containing more<br>than 20,000 items. |
| `fs.s3.consistent.notification.CloudWatch` | `false` | When set to `true`, CloudWatch metrics are<br>enabled for FileSystem API calls that fail due to Amazon S3<br>eventual consistency issues. |
| `fs.s3.consistent.notification.SQS` | `false` | When set to `true`, eventual<br>consistency notifications are pushed to an Amazon SQS<br>queue. |
| `fs.s3.consistent.notification.SQS.queueName` | `EMRFS-Inconsistency-<jobFlowId>` | Changing this property allows you to specify your own SQS<br>queue name for messages regarding Amazon S3 eventual consistency<br>issues. |
| `fs.s3.consistent.notification.SQS.customMsg` | `none` | This property allows you to specify custom information<br>included in SQS messages regarding Amazon S3 eventual consistency<br>issues. If a value is not specified for this property, the<br>corresponding field in the message is empty. |
| `fs.s3.consistent.dynamodb.endpoint` | `none` | This property allows you to specify a custom DynamoDB<br>endpoint for your consistent view metadata. |
| `fs.s3.useRequesterPaysHeader` | `false` | When set to `true`, this property allows Amazon S3 requests to buckets with the request payer option enabled. |
