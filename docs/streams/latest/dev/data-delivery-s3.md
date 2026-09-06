# Amazon S3 general purpose delivery

Amazon S3 general purpose delivery writes streaming data from a Amazon Kinesis Data Streams stream directly
to a general purpose Amazon S3 bucket. Records are delivered in their original source format
with no transformation applied, batched into optimally sized objects with configurable
compression and an S3 key structure you define. This is ideal for use cases such as raw
log archival, event replay, and downstream batch processing.

###### Topics

- [How Amazon S3 delivery works](data-delivery-s3-about.md "data-delivery-s3-about.md")
- [Getting started with S3 general purpose delivery](data-delivery-s3-getting-started.md "data-delivery-s3-getting-started.md")
- [Manage Amazon S3 general purpose deliveries](data-delivery-s3-manage.md "data-delivery-s3-manage.md")
- [S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md "data-delivery-s3-key-template.md")
