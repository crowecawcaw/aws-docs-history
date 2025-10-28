# Optimizing S3 Express One Zone performance

Amazon S3 Express One Zone is a high-performance, single Availability Zone (AZ) S3 storage class
that's purpose-built to deliver consistent, single-digit millisecond data access for your
most latency-sensitive applications. S3 Express One Zone is the first S3 storage class that gives
you the option to co-locate high-performance object storage and AWS compute resources,
such as Amazon Elastic Compute Cloud, Amazon Elastic Kubernetes Service, and Amazon Elastic Container Service, within a single Availability Zone. Co-locating
your storage and compute resources optimizes compute performance and costs and provides
increased data-processing speed.

S3 Express One Zone provides similar performance elasticity to other S3 storage classes, but with
consistent single-digit millisecond first-byte read and write request latencies—up to 10x
faster than S3 Standard. S3 Express One Zone is designed from the ground up to support burst
throughput up to very high aggregate levels. The S3 Express One Zone storage class uses a custom-built
architecture to optimize for performance and deliver consistently low request latency by
storing data on high-performance hardware. The object protocol for S3 Express One Zone has been
enhanced to streamline authentication and metadata overhead.

To further reduce latency and support up to 2 million reads and up to 200,000 writes per
second, S3 Express One Zone stores data in an Amazon S3 directory bucket.
By default, each directory bucket supports up to 200,000 reads and up to 100,000 writes
per second. If your workload requires higher than the default TPS limits, you can request an
increase through [AWS Support](https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

The combination of high-performance, purpose-built hardware and software that delivers
single-digit millisecond data access speed and directory buckets that scale for large
numbers of transactions per second makes S3 Express One Zone the best Amazon S3 storage class for
request-intensive operations or performance-critical applications.

The following topics describe best practice guidelines and design patterns for optimizing
performance with applications that use the S3 Express One Zone storage class.

###### Topics

- [Best practices to optimize S3 Express One Zone performance](s3-express-optimizing-performance-design-patterns.md "s3-express-optimizing-performance-design-patterns.md")
