# Amazon Quick Suite in AWS GovCloud (US)

Amazon Quick Suite is a comprehensive business intelligence and analytics platform that combines traditional BI capabilities
with advanced AI-powered features. The service includes the core Amazon QuickSight functionality—cloud-scale business intelligence
tools for creating dashboards, visualizations, and data analysis—along with new AI-driven capabilities for enhanced insights and automation.
Quick Suite connects to your data in the cloud and combines data from many different sources, allowing you to include AWS data, third-party data,
big data, spreadsheet data, SaaS data, B2B data, and more in a single data dashboard. **In AWS GovCloud (US), only the
traditional QuickSight capabilities (dashboards, visualizations, and data analysis) are currently supported.** As a fully managed
cloud-based service, the supported features provide enterprise-grade security, global availability, and built-in redundancy, along with
user-management tools that scale from 10 users to 10,000, all with no infrastructure to deploy or manage.

The supported QuickSight capabilities in AWS GovCloud (US) give decision-makers the opportunity to explore and interpret information in an interactive visual environment. They have secure access to dashboards from any device on your network and from mobile devices.

## How Amazon Quick Suite differs for AWS GovCloud (US)

Amazon Quick Suite (formerly Amazon QuickSight) is supported in AWS GovCloud (US) regions with limitations. Only the core business intelligence capabilities are available, including dashboards, visualizations, data analysis, and reporting features. AI-powered features and functionality introduced as part of Amazon Quick Suite are not supported in AWS GovCloud (US) regions.

Below listed are the differences between the AWS GovCloud (US) and the standard AWS Regions.

- Email based user provisioning is not supported in AWS GovCloud (US).
- Using geospatial visualizations is not supported in AWS GovCloud (US).
- Using Amazon SageMaker AI integration is not supported in AWS GovCloud (US).
- The Q AI assistant is not supported in AWS GovCloud (US).
- Amazon Quick Suite and interface VPC endpoints (AWS PrivateLink) are not supported in AWS GovCloud (US).
- The mobile app is not supported for AWS GovCloud (US-East).

Amazon Quick Suite in AWS GovCloud (US) supports user authorization for federated users only. Quick Suite
directly supports authentication through AWS Identity and Access Management (IAM), AWS IAM Identity Center (IAM Identity Center), and
AWS Directory Service for Microsoft Active Directory. For more information, see [Identity federation in
AWS](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/").

If you're a Amazon Quick Suite administrator, make sure to allow-list the following domains
within your organization's network.

| User type                                            | Domain to allow-list                 |
| ---------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Native Amazon Quite Suite and Active Directory users | awsapps.com and amazonaws-us-gov.com |
| IAM users                                            | amazonaws-us-gov.com                 | Specialized configurations that allow users to authenticate with a different identity service can also work, even if not directly supported from inside Amazon Quick Suite. For example, you can use Amazon Cognito as is described in the [Embedded Analytics Tutorial](https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/ "https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/"). This authentication method works because it is compatible and transparent to Amazon Quick Suite. For more information on Amazon Quick Suite authentication, see [Identity and Access Management in Amazon Quick Suite](../../../quicksight/latest/user/identity.md "../../../quicksight/latest/user/identity.md"). ###### Note If you are using the [Embedded Analytics Tutorial](https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/ "https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/"), you can point to AWS GovCloud (US) ARNs and URLs for your resources, but in the step for the static website that uses Amazon CloudFront and Amazon S3, you need to point to a classic AWS Region, for example US East (N. Virginia), for the tutorial to work. This is not necessary outside the tutorial. For more information and additional examples, see [Developing with Amazon Quick Suite](../../../quicksight/latest/user/quicksight_dev.md "../../../quicksight/latest/user/quicksight_dev.md") in the Amazon Quick Suite User Guide. ## Documentation for Amazon Quick Suite [Amazon Quick Suite documentation](../../../quicksuite.md "../../../quicksuite.md"). ## Export-controlled content For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions. <br>• No data will leave the AWS GovCloud (US) Regions for this service. |
