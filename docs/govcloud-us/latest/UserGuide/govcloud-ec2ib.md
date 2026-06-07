# Amazon EC2 Image Builder in AWS GovCloud (US) Regions

Amazon EC2 Image Builder (Image Builder) is a fully managed AWS service that makes it easier to automate the creation, management, and deployment of customized, secure, and up-to-date server images that are pre-installed and pre-configured with software and settings to meet specific IT standards.

## Service differences

The following Image Builder features are not available in AWS GovCloud (US) Regions:

- ISO disk file import
- macOS images
- AWS Marketplace software components

## Documentation references

- [EC2 Image Builder User Guide](../../../imagebuilder/latest/userguide.md "../../../imagebuilder/latest/userguide.md")
- [EC2 Image Builder AWS CLI Reference](../../../cli/latest/reference/imagebuilder/index.md "../../../cli/latest/reference/imagebuilder/index.md")
- [EC2 Image Builder API Reference](../../../imagebuilder/latest/APIReference.md "../../../imagebuilder/latest/APIReference.md")
- [AWS Developer Tools](cli-and-api-access.md "cli-and-api-access.md")
- [Service endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md")

## Export-controlled content

For AWS services architected within the AWS GovCloud (US) Region, the following list explains how certain components of data may leave the AWS GovCloud (US) Region in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Region.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
