# ADVPERF03-BP02 Use object storage to store and analyze raw data from ad servers, DSPs, and DMP

Object storage can be used to store massive amounts of data while
balancing cost and performance. Customers can use object storage
services to build data lakes and analyze this data to uncover
valuable insights and achieve business goals.

## Implementation guidance

[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") is a highly scalable and durable object
storage service that can store and protect any amount of data for a range of use cases. It
is ideal for storing and serving static content, such as images, videos, and other media
assets used in advertising campaigns. Amazon S3 also supports data lakes, which you can use to
store and analyze vast amounts of raw data from various sources, including ad servers,
demand-side platforms (DSPs), and data management platforms (DMPs). 

- **[Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/ "https://aws.amazon.com/s3/storage-classes/express-one-zone/"):** A powerful storage class for
  performance-critical applications, including advertising model training. Its low
  latency, high throughput, and cost efficiency makes it an ideal choice for real-time ad
  placement, machine learning for ad personalization, and interactive analytics.
- **Data partitioning:** Use
  multiple prefixes to partition your data, which distributes
  the load and improves performance. For example, instead of
  storing all objects under a single prefix, use multiple
  prefixes like `s3://bucket-name/prefix1/` and
  `s3://bucket-name/prefix2/`.
- **Data transfer:** Use Amazon S3 Transfer Acceleration to speed up data transfers over
  long distances, improving the performance of data ingestion
  and distribution processes.
- **Monitoring and auditing:**
  Use AWS CloudTrail and Amazon CloudWatch to monitor S3
  access and performance metrics.
- **Storage tiering and
  class:** Each object in Amazon S3 has a
  [storage
  class](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") associated with it. Choosing a storage class
  designed for your use case lets you optimize storage costs,
  performance, and availability for your objects. Use the S3
  Intelligent-Tiering storage class, which is designed to
  optimize storage costs by automatically moving data to the
  most cost-effective access tier when access patterns change,
  without operational overhead or impact on performance. S3
  Intelligent-Tiering monitors access patterns and
  automatically moves objects that have not been accessed to
  lower-cost access tier.

## Resources

- [Getting
  started with S3 Express One Zone](../../../AmazonS3/latest/userguide/s3-express-getting-started.md "../../../AmazonS3/latest/userguide/s3-express-getting-started.md")
- [Setting
  an S3 Lifecycle configuration on a bucket](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md")
- [Protecting
  data with server-side encryption](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.md "Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.md")
- [Monitoring
  metrics with Amazon CloudWatch](../../../AmazonS3/latest/userguide/cloudwatch-monitoring.md "../../../AmazonS3/latest/userguide/cloudwatch-monitoring.md")
- [Manage
  Amazon S3 storage costs granularly and at scale using S3 Intelligent-Tiering](https://aws.amazon.com/blogs/storage/manage-amazon-s3-storage-costs-granularly-and-at-scale-using-s3-intelligent-tiering/ "https://aws.amazon.com/blogs/storage/manage-amazon-s3-storage-costs-granularly-and-at-scale-using-s3-intelligent-tiering/")
