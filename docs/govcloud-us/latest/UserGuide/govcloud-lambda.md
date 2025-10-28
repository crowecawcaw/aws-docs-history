# AWS Lambda in AWS GovCloud (US)

With AWS Lambda, you can run code without provisioning or managing servers. You pay only for the compute time that you consume—there’s no charge when your code isn’t running. You can run code for virtually any type of application or backend service—all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

## How AWS Lambda differs for AWS GovCloud (US)

- Schema registry support for Kafka event sources is not available.
- AWS Lambda Function URLs is not available.
- Event source mapping (ESM) tags for AWS Lambda is not available.
- The DocumentDB event sources are not available.
- Multi-VPC connectivity for Managed Streaming for Apache Kafka event source mappings is not available.
- JSON log formatting is not available.
- Lambda integration with Infrastructure Composer is not available.
- The [Future runtime launch dates](../../../lambda/latest/dg/lambda-runtimes.md#runtimes-future "../../../lambda/latest/dg/lambda-runtimes.md#runtimes-future") are not applicable.
- The Amazon CloudWatch Logs Live Tail integration in the Lambda console is not available.
- AWS KMS customer managed key encryption for .zip deployment packages is not available.
- Lambda SnapStart for Python and .NET is not available.
- CloudWatch Application Signals for Lambda functions is not available.
- Event source mapping metrics are not available.
- Provisioned mode for event source mappings is not available.
- Amazon S3 as a destination for Kinesis, DynamoDB, and async invoke is not available.
- Monitoring Lambda function logs with Amazon S3 or Firehose is not yet available.
- AWS Lambda managed layers have different versions in AWS GovCloud (US) Regions compared to
  commercial Regions. Verify layer availability and versions when migrating
  functions between Regions.
- The deprecation schedule for the .NET 6 runtime is different from the schedule provided in the
  [Lambda Developer Guide](../../../lambda/latest/dg/lambda-runtimes.md#runtimes-supported "../../../lambda/latest/dg/lambda-runtimes.md#runtimes-supported").

Lambda will deprecate the .NET 6 runtime on July 31, 2025. We recommend that you migrate .NET 6 functions to .NET 8, which is now available. Until the deprecation date, Lambda will continue to apply patches to the .NET 6 operating system (OS), but not to the .NET 6 language runtime.

## Documentation for AWS Lambda

[AWS Lambda documentation](https://aws.amazon.com/documentation/lambda/ "https://aws.amazon.com/documentation/lambda/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following console fields:
  - Function name
  - Description
  - DLQ data (can be exported through Amazon SNS and Amazon SQS)
  - Memory
  - Timeout
  - Runtime
  - Role name for service principals
  - Aliases
  - LayerName
  - Layer Description
  - Layer Compatible Architectures
  - Layer Compatible Runtimes
  - EphemeralStorage Size
  - PackageType
  - State
  - StateReason
