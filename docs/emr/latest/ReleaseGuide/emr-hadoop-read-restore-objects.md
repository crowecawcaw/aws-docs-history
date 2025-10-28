# Read restored objects

With Amazon EMR release 7.2.0 and higher, you can read restored Glacier objects from the S3 location of the table
with the `S3A` protocol. Engines in previous releases don't distinguish between Glacier
and Glacier Deep Archive files, which means you would get an `AmazonS3Exception` if you tried to
access an in-progress Glacier file with `S3A`. This read operation ignores archived Glacier files
if they still in progress of being restored. To enable this behavior, use the setting
`fs.s3a.glacier.read.restored.objects`. This setting can be three values:

- **READ_ALL** – this value indicates that Amazon EMR shouldn't
  account for the storage classes retrieved from Amazon S3. This is the default behavior.
- **SKIP_ALL_GLACIER** – this value indicates that Amazon EMR
  should ignore any S3 objects that are tagged with the Glacier storage class and retrieve all other objects.
  This is the default behavior for Amazon EMR with respect to Glacier objects.
- **READ_RESTORED_GLACIER_OBJECTS** – this value indicates that Amazon EMR
  should check the restored status of the Glacier object. If Amazon EMR can restore the object, you can read them
  like a normal S3 object. Otherwise, Amazon EMR ignores the object from Amazon Glacier

## Examples

**Spark**

To read restored objects when you use Spark, use the following configuration:

```
--conf spark.hadoop.fs.s3a.glacier.read.restored.objects=`<value>`
```

If you use spark-sql, use the following configuration instead;

```
spark-sql --conf spark.hadoop.fs.s3a.glacier.read.restored.objects=`<value>`
```

**Flink**

If you use Flink, you can set the configuration in the `flink-conf.yaml` file

```
fs.s3a.glacier.read.restored.objects: `<value>`
```

You can also set the `flink-conf` classification:

```
[
	{
		"Classification": "flink-conf",
		"Properties": {
		"fs.s3a.glacier.read.restored.objects":"<value>"
		}
	}
]
```

**Hive**

If you use Hive, set the configuration in the `hive-site.xml` file.

```
<property>
	<name>fs.s3a.glacier.read.restored.objects</name>
	<value>`<value>`</value>
</property>
```

You can also use the Hive CLI to set the property `--hiveconf`:

```
hive --hiveconf fs.s3a.glacier.read.restored.objects=`<value>`
```

## Considerations

When you read restored objects from Amazon Glacier, note the following considerations:

- You can only read restored objects if you use the `S3A` scheme or the `S3AFileSystem`
  to access the data.
- When you read a restored Glacier object, Amazon EMR doesn't restore the object itself. To do so,
  you must use the AWS CLI or the AWS SDK.
