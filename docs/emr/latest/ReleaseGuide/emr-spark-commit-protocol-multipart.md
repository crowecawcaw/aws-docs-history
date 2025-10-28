# The EMRFS S3-optimized

commit protocol and multipart uploads

To use make use of the optimization for dynamic partition overwrite in the
EMRFS S3-optimized commit protocol, multipart uploads must be enabled in Amazon EMR .
Multipart uploads are enabled by default. You can re-enable it if required. For
more information, see [Configure
multipart upload for Amazon S3](../ManagementGuide/emr-plan-upload-s3.md#Config_Multipart "../ManagementGuide/emr-plan-upload-s3.md#Config_Multipart") in the
_Amazon EMR Management Guide_.

During dynamic partition overwrite, the EMRFS S3-optimized commit protocol
uses the transaction-like characteristics of multipart uploads to ensure files
written by task attempts only appear in the job's output location upon job
commit. By using multipart uploads in this way, the commit protocol improves job
commit performance over the default
`SQLHadoopMapReduceCommitProtocol`. When using the EMRFS
S3-optimized commit protocol, there are some key differences from traditional
multipart upload behavior to consider:

- Multipart uploads are always performed regardless of the file size.
  This differs from the default behavior of EMRFS, where the
  `fs.s3n.multipart.uploads.split.size` property controls
  the file size at which multipart uploads are triggered.
- Multipart uploads are left in an incomplete state for a longer period
  of time until the task commits or aborts. This differs from the default
  behavior of EMRFS where a multipart upload completes when a task
  finishes writing a given file.
  Because of these differences, if a Spark Executor JVM crashes or is killed
  while tasks are running and writing data to Amazon S3, or a Spark Driver JVM crashes
  or is killed while a job is running, incomplete multipart uploads are more
  likely to be left behind. For this reason, when you use the EMRFS S3-optimized
  commit protocol, be sure to follow the best practices for managing failed
  multipart uploads. For more information, see [Best
  practices](../ManagementGuide/emr-plan-upload-s3.md#emr-bucket-bestpractices "../ManagementGuide/emr-plan-upload-s3.md#emr-bucket-bestpractices") for working with Amazon S3 buckets in the
  _Amazon EMR Management Guide_.
