Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# UpdateApplication action isn't reloading

application code

The [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action will not reload application code with the same file name if no S3 object version is specified. To reload application code with the same file name, enable versioning on your S3 bucket, and specify the new object version using the `ObjectVersionUpdate` parameter. For more information about enabling object versioning in an S3 bucket, see [Enabling or Disabling Versioning](../../../AmazonS3/latest/user-guide/enable-versioning.md "../../../AmazonS3/latest/user-guide/enable-versioning.md").
