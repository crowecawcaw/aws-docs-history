# Customizations for AWS Control Tower (CfCT) overview

_Customizations for AWS Control Tower_ (CfCT) helps you customize
your AWS Control Tower landing zone and stay aligned with AWS best practices. Customizations are
implemented with AWS CloudFormation templates and service control policies (SCPs).

This CfCT capability is integrated with AWS Control Tower lifecycle events, so that your resource
deployments remain synchronized with your landing zone. For example, when a new account is
created through account factory, all resources attached to the account are deployed
automatically. You can deploy the custom templates and policies to individual accounts and
organizational units (OUs) within your organization.

###### Note

The target organizational unit (OU) configured in CfCT must have AWSControlTowerBaseline enabled
in AWS Control Tower.

The following video describes best practices for deploying a scalable CfCT pipeline and
common CfCT customizations.

The following section provides architectural considerations and configuration steps for
deploying Customizations for AWS Control Tower (CfCT). It includes a link to the [AWS CloudFormation](https://aws.amazon.com/cloudformation "https://aws.amazon.com/cloudformation") template that launches,
configures, and runs the required AWS services, in alignment with AWS best practices for
security and availability.

_This topic is intended for IT infrastructure architects and
developers who have practical experience architecting in the AWS
Cloud._

For information about the latest updates and changes to Customizations for AWS Control Tower
(CfCT), refer to the [CHANGELOG.md file](https://github.com/aws-solutions/aws-control-tower-customizations/blob/master/CHANGELOG.md "https://github.com/aws-solutions/aws-control-tower-customizations/blob/master/CHANGELOG.md") in the GitHub repository.
