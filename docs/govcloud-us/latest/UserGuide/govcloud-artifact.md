# AWS Artifact in AWS GovCloud (US)

AWS Artifact provides on-demand downloads of AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and Service Organization Control (SOC) reports. You can submit the security and compliance documents (also known as audit artifacts) to your auditors or regulators to demonstrate the security and compliance of the AWS infrastructure and services that you use. You can also use AWS Artifact to review, accept, and track the status of AWS agreements such as the Business Associate Addendum (BAA). With AWS Artifact, you can accept agreements with AWS and designate AWS accounts that can legally process restricted information.

## How AWS Artifact differs for AWS GovCloud (US)

This service has no differences between AWS GovCloud (US) Regions and the standard AWS Regions.

## Documentation for AWS Artifact

[AWS Artifact documentation](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Function name
- Description
- DLQ data (can be exported through Amazon SNS and Amazon SQS)
- Memory
- Timeout
- Runtime
- Role name for service principals
- Aliases
