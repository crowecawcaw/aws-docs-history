# Amazon EC2 Image Builder in AWS GovCloud (US)

Amazon Elastic Compute Cloud Image Builder is a fully managed AWS service that makes it easier to automate the creation, management and deployment of customized, secure and up-to-date “golden” server images that are pre-installed and pre-configured with software and settings to meet specific IT standards. You can use the AWS Management Console, AWS CLI or APIs to create “golden” images in your AWS account. The images you build are created in your account and you can configure them for operating system patches on an ongoing basis.

## How Amazon EC2 Image Builder differs for AWS GovCloud (US)

The implementation of Amazon EC2 Image Builder is different for AWS GovCloud (US) Regions in the following ways:

- Image Builder doesn’t support Dedicated Instances or Dedicated Hosts.
- Image Builder doesn’t support macOS images.

The following Image Builder features are not supported in AWS GovCloud (US) Regions:

- Image lifecycle policies
- AWS Marketplace Software components
- ISO disk file import

## Documentation for Amazon EC2 Image Builder

For more information about Amazon EC2 Image Builder, see the [Amazon EC2 Image Builder documentation](../../../imagebuilder/latest/userguide.md "../../../imagebuilder/latest/userguide.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- EC2 Image Builder metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your images, components, image recipes, distribution configurations and infrastructure configurations.

Do not enter export-controlled data in the following console fields:

    + Names
    + Description
    + Resource tags
