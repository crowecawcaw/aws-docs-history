# Netskope

Netskope, a global cybersecurity leader, is redefining cloud, data, and
network security to help organizations apply zero trust principles to protect data. Fast and
easy to use, the Netskope platform provides optimized access and zero trust
security for people, devices, and data anywhere they go. Netskope helps
customers reduce risk, accelerate performance, and get unrivaled visibility into any cloud,
web, and private application activity. Thousands of customers, including more than 25 of the
Fortune 100, trust Netskope and its powerful NewEdge network to address
evolving threats, new risks, technology shifts, organizational and network changes, and new
regulatory requirements. Learn how Netskope helps customers be ready for
anything on their SASE journey, visit [netskope.com](https://www.netskope.com/ "https://www.netskope.com/").

## AWS AppFabric audit log ingestion

considerations

The following sections describe the AppFabric output schema, output formats, and output
destinations to use with Netskope.

### Schema and format

Netskope supports the following AppFabric output schema and
formats:

- Raw - JSON
  - AppFabric outputs data in the original schema used by the source
    application in the JSON format.

- OCSF - JSON
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in the JSON format.

### Output locations

Netskope supports the following AppFabric output location:

- Amazon Simple Storage Service (Amazon S3)
  - To configure Netskope to receive data from the Amazon S3
    bucket that contains your audit logs, follow the instructions in
    [Data Protection for Amazon Web Services S3](https://docs.netskope.com/en/data-protection-for-amazon-web-services-s3.html "https://docs.netskope.com/en/data-protection-for-amazon-web-services-s3.html") on the
    Netskope website.
