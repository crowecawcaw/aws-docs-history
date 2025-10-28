# AWS CloudFormation in AWS GovCloud (US)

AWS CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products such as Amazon EC2, Amazon Elastic Block Store, Amazon SNS, Elastic Load Balancing, and Auto Scaling to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. AWS CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).

## How AWS CloudFormation differs for AWS GovCloud (US)

- KmsKeyID property is not available.
- AWS CloudFormation doesn't support the following resources:
  - `AWS::IAM::GroupPolicy`
  - `AWS::IAM::RolePolicy`
  - `AWS::IAM::UserPolicy`
  - `AWS::Organizations::Account`
  - `AWS::RolesAnywhere::TrustAnchor`

###### Note

ResourceTypes for AWS CloudFormation can vary per Region. Ensure the ResourceTypes needed are
available in AWS GovCloud (US-West) and AWS GovCloud (US-East) which can be found here
within the [Resource
Specification table](../../../AWSCloudFormation/latest/UserGuide/cfn-resource-specification.md "../../../AWSCloudFormation/latest/UserGuide/cfn-resource-specification.md").

## Documentation for AWS CloudFormation

The following documentation is based on the public AWS documentation. As you read this
documentation, you should consider how AWS CloudFormation differs for AWS GovCloud (US) Regions, as described
in this topic. Also, some features and new functionality described in this documentation might
not be available in the current release of AWS GovCloud (US) Regions. There are other differences,
such as links, endpoints, and screenshots.

- [AWS CloudFormation Documentation](../../../cloudformation.md "../../../cloudformation.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No export-controlled data may be entered, stored, or processed by AWS CloudFormation. For example,
  AWS CloudFormation metadata is not permitted to contain export-controlled data. This metadata includes
  all the configuration data that you enter when creating and maintaining your AWS CloudFormation
  templates.
