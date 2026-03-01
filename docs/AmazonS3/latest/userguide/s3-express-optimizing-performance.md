# Optimizing directory bucket performance

To obtain the best performance when using directory buckets, we recommend the following
guidelines.

For more information about best practices for S3 Express One Zone, see [Best practices to optimize S3 Express One Zone performance](s3-express-optimizing-performance-design-patterns.md "s3-express-optimizing-performance-design-patterns.md").

## Use session-based authentication

Directory buckets support a new session-based authorization mechanism
to authenticate and authorize requests to a directory bucket. With session-based
authentication, the AWS SDKs automatically use the `CreateSession` API
operation to create a temporary session token that can be used for low-latency authorization
of data requests to a directory bucket.

The AWS SDKs use the `CreateSession` API operation to request temporary
credentials, and then automatically create and refresh tokens for you on your behalf every 5
minutes. To take advantage of the performance benefits of directory buckets, we
recommended that you use the AWS SDKs to initiate and manage the
`CreateSession` API request. For more information about this session-based
model, see [Authorizing Zonal endpoint API operations with CreateSession](s3-express-create-session.md "s3-express-create-session.md").

## S3 additional checksum best practices

Directory buckets offer you the option to choose the checksum algorithm that is used to validate your data during upload or download. You can select one of the following Secure Hash Algorithms (SHA) or Cyclic Redundancy Check (CRC) data-integrity check algorithms: CRC32, CRC32C, SHA-1,
and SHA-256. MD5-based checksums are not supported with the S3 Express One Zone storage class.

CRC32 is the default checksum used by the AWS SDKs when transmitting data to or from
directory buckets. We recommend using CRC32 and CRC32C for the best performance with
directory buckets.

## Use the latest version of the AWS SDKs and common runtime libraries

Several of the AWS SDKs also provide the AWS Common Runtime (CRT) libraries to
further accelerate performance in S3 clients. These SDKs include the AWS SDK for Java 2.x, the
AWS SDK for C++, and the AWS SDK for Python (Boto3). The CRT-based S3 client transfers objects to and from
directory buckets with enhanced performance and reliability by automatically using the multipart
upload API operation and byte-range fetches to automate horizontally scaling connections.

To achieve the highest performance with the directory buckets, we recommend using the
latest version of the AWS SDKs that include the CRT libraries or using the AWS Command Line Interface
(AWS CLI).
