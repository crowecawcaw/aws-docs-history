# Splunk

Splunk helps make organizations more resilient. Leading organizations use
Splunk’s unified security and observability platform to keep their
digital systems secure and reliable. Organizations trust Splunk to prevent
security, infrastructure, and application issues from becoming major incidents, absorb
shocks from digital disruptions and accelerate digital transformation.

## AWS AppFabric audit log ingestion considerations

The following sections describe the AppFabric output schema, output formats, and output
destinations to use with Splunk.

### Schema and format

Splunk supports the following AppFabric output schema and formats:

- Raw - JSON
  - AppFabric outputs data in the original schema used by the source
    application in the JSON format.

- OCSF - JSON
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in the JSON format.

- OCSF - Parquet
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in the Apache
    Parquet format.

### Output locations

Splunk supports the following AppFabric output locations:

- Amazon Data Firehose
  - To configure Splunk to receive audit logs from the
    Firehose stream that contains your audit logs, follow the instructions
    in [Splunk Add-on for Amazon Data Firehose](https://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureFirehose "https://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureFirehose") on the
    Splunk website.

- Amazon Simple Storage Service (Amazon S3)
  - To configure Splunk to receive data from the Amazon S3
    bucket that contains your audit logs, follow the instructions in
    [Configure SQS-based S3 inputs for the Splunk
    Add-on for AWS](https://docs.splunk.com/Documentation/AddOns/released/AWS/SQS-basedS3 "https://docs.splunk.com/Documentation/AddOns/released/AWS/SQS-basedS3") on the Splunk
    website.
