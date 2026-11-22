

# Best practices design patterns: optimizing Amazon S3 performance

Your applications can easily achieve thousands of transactions per second in request performance when uploading and retrieving storage from Amazon S3. Amazon S3 supports at least 3,500 PUT/COPY/POST/DELETE or 11,000 GET/HEAD requests per second per partitioned prefix and automatically scales to higher request rates as your traffic grows. A partition is a unit of resource that S3 attaches to a prefix to serve higher request rates. A partitioned prefix is a prefix whose keys Amazon S3 has assigned to their own partition as traffic to those keys grows. You influence this through how you name your keys: spreading requests across many prefixes helps Amazon S3 partition more of them in parallel.

Scaling of partitioned prefixes happens gradually and is not instantaneous. While Amazon S3 is scaling to your new higher request rate, you might see some 503 (Slow Down) errors. These errors resolve when the scaling is complete. Amazon S3 scales for the prefixes that receive a high request rate. When your application sends a high request rate to keys with a prefix that previously received little or no traffic, requests might receive 503 (Slow Down) errors until Amazon S3 scales for it.

A prefix is the set of leading characters in an object key name. Amazon S3 does not treat the forward slash (`/`) as a special character, and a prefix does not need to end in `/`, so organizing keys into folder-like paths does not by itself increase your request rate. To get the highest request rates, distribute your requests across many prefixes rather than concentrating them on one. Key naming patterns that keep traffic spread across a stable set of prefixes, such as adding a character from a hash of the key name to the start of the name, let Amazon S3 scale for those prefixes once and continue serving them.

Some data lake applications on Amazon S3 scan millions or billions of objects for queries that run over petabytes of data. These data lake applications achieve single-instance transfer rates that maximize the network interface use for their [Amazon EC2](https://docs.aws.amazon.com/ec2/index.html) instance, which can be up to 100 Gb/s on a single instance. These applications then aggregate throughput across multiple instances to get multiple terabits per second. 

Other applications are sensitive to latency, such as social media messaging applications. These applications can achieve consistent small object latencies (and first-byte-out latencies for larger objects) of roughly 100–200 milliseconds.

Other AWS services can also help accelerate performance for different application architectures. For example, if you want higher transfer rates over a single HTTP connection or single-digit millisecond latencies, use [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/index.html) or [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache/index.html) for caching with Amazon S3.

Additionally, if you want fast data transport over long distances between a client and an S3 bucket, use [Configuring fast, secure file transfers using Amazon S3 Transfer Acceleration](transfer-acceleration.md). Transfer Acceleration uses the globally distributed edge locations in CloudFront to accelerate data transport over geographical distances. If your Amazon S3 workload uses server-side encryption with AWS KMS, see [AWS KMS Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the AWS Key Management Service Developer Guide for information about the request rates supported for your use case. 

The following topics describe best practice guidelines and design patterns for optimizing performance for applications that use Amazon S3. Refer to the [Performance guidelines for Amazon S3](optimizing-performance-guidelines.md) and [Performance design patterns for Amazon S3](optimizing-performance-design-patterns.md) for the most current information about performance optimization for Amazon S3. 

**Note**  
For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone) and [Working with directory buckets](directory-buckets-overview.md).

**Topics**
+ [Performance guidelines for Amazon S3](optimizing-performance-guidelines.md)
+ [Performance design patterns for Amazon S3](optimizing-performance-design-patterns.md)

  
