# Source management in Security Lake

Sources are logs and events generated from a single system that match a specific event
class in the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") schema. Amazon Security Lake can collect
logs and events from a variety of sources, including natively supported AWS services and
third-party custom sources.

Security Lake runs extract, transform, and load (ETL) jobs on raw source data, and converts
the data to Apache Parquet format and the OCSF schema. After processing, Security Lake stores
source data in an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account in the AWS Region that the
data was generated in. Security Lake creates a different Amazon S3 bucket for each Region in which
you enable the service. Each source gets a separate prefix in your S3 bucket, and Security Lake
organizes data from each source in a separate set of AWS Lake Formation tables.

###### Topics

- [Collecting data from AWS services in Security Lake](internal-sources.md "internal-sources.md")
- [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md")
