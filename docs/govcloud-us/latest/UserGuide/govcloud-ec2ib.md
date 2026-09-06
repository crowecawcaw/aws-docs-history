

# EC2 Image Builder in AWS GovCloud (US)
<a name="govcloud-ec2ib"></a>

Amazon Elastic Compute Cloud Image Builder is a fully managed AWS service that makes it easier to automate the creation, management and deployment of customized, secure and up-to-date “golden” server images that are pre-installed and pre-configured with software and settings to meet specific IT standards. You can use the AWS Management Console, AWS CLI or APIs to create “golden” images in your AWS account. The images you build are created in your account and you can configure them for operating system patches on an ongoing basis.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon EC2 Image Builder differs
<a name="govcloud-ec2ib-diffs"></a>

The following differences apply to Amazon EC2 Image Builder:
+  Image Builder doesn’t support macOS images.
+ The following Image Builder features are not available:
  + Image lifecycle policies
  +  AWS Marketplace Software components
  + ISO disk file import

## Documentation
<a name="govcloud-ec2ib-docs"></a>
+  [Amazon EC2 Image Builder documentation](https://docs.aws.amazon.com/imagebuilder/latest/userguide) 

## Export-controlled content
<a name="govcloud-ec2ib-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ EC2 Image Builder metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your images, components, image recipes, distribution configurations and infrastructure configurations.

  Do not enter export-controlled data in the following console fields:
  + Names
  + Description
  + Resource tags