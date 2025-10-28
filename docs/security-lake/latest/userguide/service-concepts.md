# Concepts and terminology

This section describes the key concepts and terms to help you use Amazon Security Lake.

**Contributing Region**

One or more AWS Regions that contribute data to a rollup Region.

**Data lake**

Your persistent data that is stored in Amazon Simple Storage Service (Amazon S3) and managed by Security Lake.
Security Lake uses AWS Glue to send newly written data to the Data Catalog. Security Lake also creates a AWS Lake Formation table for each source that
contributes data to the data lake. A data lake
typically stores the following:

- Structured and unstructured data
- Raw and transformed data

Security Lake is a data lake service that's designed to collect security-related logs and events.

**Open Cybersecurity Schema Framework (OCSF)**

A standardized [open-source schema](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") for security logs and events. It was developed by AWS and
other security industry leaders across various security domains. Security Lake automatically converts the logs and events that it collects from AWS services into the OCSF schema.
Custom sources convert their logs and events into OCSF before sending them to Security Lake.

**Rollup Region**

An AWS Region that consolidates security logs and events from one or more
contributing Regions. Specifying one or more rollup Regions can help you comply
with regional compliance requirements.

**Source**

A set of logs and events generated from a single system that matches a specific
event class in [OCSF](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md").
Security Lake can collect data from a source. A source may be another AWS service
or a third-party service. For third-party sources, you must
convert the data to the OCSF schema before sending it to Security Lake.

**Subscriber**

A service that consumes logs and events from Security Lake. A subscriber may be another AWS service or a
third-party service.
