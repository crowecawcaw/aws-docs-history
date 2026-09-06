

# Customizations for AWS Control Tower (CfCT) overview
<a name="cfct-overview"></a>

*Customizations for AWS Control Tower* (CfCT) helps you customize your AWS Control Tower landing zone and stay aligned with AWS best practices. Customizations are implemented with AWS CloudFormation templates, service control policies (SCPs), and resource control policies (RCPs).

This CfCT capability is integrated with AWS Control Tower lifecycle events, so that your resource deployments remain synchronized with your landing zone. For example, when a new account is created through account factory, all resources attached to the account are deployed automatically. You can deploy the custom templates and policies to individual accounts and organizational units (OUs) within your organization.

**Note**  
The target organizational unit (OU) configured in CfCT must have AWSControlTowerBaseline enabled in AWS Control Tower. For details of AWSControlTowerBaseline, see: [Baseline types that apply at the OU level](types-of-baselines.md#ou-baseline-types).

 The following video describes best practices for deploying a scalable CfCT pipeline and common CfCT customizations. 

[![AWS Videos](http://img.youtube.com/vi/fDtxiBW_J8I/0.jpg)](http://www.youtube.com/watch?v=fDtxiBW_J8I)


The following section provides architectural considerations and configuration steps for deploying Customizations for AWS Control Tower (CfCT). It includes a link to the [AWS CloudFormation](https://aws.amazon.com/cloudformation) template that launches, configures, and runs the required AWS services, in alignment with AWS best practices for security and availability.

*This topic is intended for IT infrastructure architects and developers who have practical experience architecting in the AWS Cloud.*

For information about the latest updates and changes to Customizations for AWS Control Tower (CfCT), refer to the [CHANGELOG.md file](https://github.com/aws-solutions/aws-control-tower-customizations/blob/master/CHANGELOG.md) in the GitHub repository.