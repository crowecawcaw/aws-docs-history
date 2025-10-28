# Data protection in Amazon Kinesis Data Streams

Server-side encryption using AWS Key Management Service (AWS KMS) keys makes it easy for you to meet strict
data management requirements by encrypting your data at rest within Amazon Kinesis Data Streams.

###### Note

If you require FIPS 140-2 validated cryptographic modules when accessing AWS through
a command line interface or an API, use a FIPS endpoint. For more information about the
available FIPS endpoints, see [Federal
Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

###### Topics

- [What is server-side encryption for Kinesis Data Streams?](what-is-sse.md "what-is-sse.md")
- [Costs, Regions, and performance
  considerations](costs-performance.md "costs-performance.md")
- [How do I get started with server-side
  encryption?](getting-started-with-sse.md "getting-started-with-sse.md")
- [Create and use user-generated
  KMS keys](creating-using-sse-master-keys.md "creating-using-sse-master-keys.md")
- [Permissions to use user-generated
  KMS keys](permissions-user-key-KMS.md "permissions-user-key-KMS.md")
- [Verify and Troubleshoot KMS key
  permissions](sse-troubleshooting.md "sse-troubleshooting.md")
- [Use Amazon Kinesis Data Streams with interface VPC endpoints](vpc.md "vpc.md")
