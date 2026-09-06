

# Amazon Quick in AWS GovCloud (US)
<a name="govcloud-aqs"></a>

Amazon Quick is a comprehensive, generative AI-powered business intelligence service that makes it easy to analyze data, create visualizations, automate workflows, and collaborate across your organization. The service combines traditional business intelligence capabilities with modern AI assistance, requiring no machine learning expertise to use. You can connect to diverse data sources, create interactive dashboards, build intelligent automations, and get immediate insights through natural language conversations with AI agents. **In AWS GovCloud (US), Amazon Quick offers a limited deployment: in addition to the traditional Quick Sight capabilities (dashboards, visualizations, and data analysis), a subset of Amazon Quick capabilities is supported. Not all Amazon Quick features are available. For the full list of supported and unsupported features, see the differences section below.** As a fully managed cloud-based service, the supported features provide enterprise-grade security, global availability, and built-in redundancy. There is no infrastructure to deploy or manage.

With the supported Amazon Quick capabilities in AWS GovCloud (US), you can explore and interpret information in an interactive visual environment. You have secure access to dashboards from any device on your network and from mobile devices.

## Region availability
<a name="region-availability"></a>

 Amazon Quick is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-East) 
+  AWS GovCloud (US-West) 

## How Amazon Quick differs
<a name="feature-diffs"></a>

The following differences apply to Amazon Quick:
+  Amazon Quick Automate is not available.
+  Amazon Quick Flows is not available.
+  Amazon Quick Research is not available.
+ Quick Agents is not available.
+ Quick Integrations and Extensions is not available.
+ Quick Sight - Agentic experiences is not available.
+ Quick Sight - Mobile App for Dashboards is not available.
+ Quick Spaces is not available in AWS GovCloud (US-East).
+ Amazon Quick is supported in AWS GovCloud (US) regions with limitations. In addition to the core business intelligence capabilities—​dashboards, visualizations, data analysis, and reporting—​the following Amazon Quick capabilities are available in AWS GovCloud (US): Agents, Spaces, Chat, Browser extensions, Quick Sight Q&A (Dataset Q&A, Dashboard Q&A, and Explainability), Actions, and Knowledge base connectors.
+ The core Quick Sight capabilities (dashboards, visualizations, data analysis, and reporting) are available in both AWS GovCloud (US-East) and AWS GovCloud (US-West). The Amazon Quick agentic capabilities (Agents, Spaces, Chat, Browser extensions, Q&A, Actions, and Knowledge base connectors) are available only in AWS GovCloud (US-West).
+ Microsoft 365 knowledge base connectors are available only with Microsoft GCC High.
+ The Knowledge Base connector for SharePoint/OneDrive is 3LO only (3LO = Three-Legged OAuth; end user authenticates and grants application access).
+ Email-based user provisioning is not available.
+ Geospatial visualizations are not available.
+  Amazon SageMaker AI integration is not available.
+ Amazon Quick and interface VPC endpoints (AWS PrivateLink) are not available.
+ The mobile app is not available for AWS GovCloud (US-East).
+ Amazon Quick in AWS GovCloud (US) supports user authorization for federated users only. Amazon Quick directly supports authentication through AWS Identity and Access Management (IAM), AWS IAM Identity Center (IAM Identity Center), and AWS Directory Service for Microsoft Active Directory. For more information, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/).
+ If you’re an Amazon Quick administrator, make sure to allow-list the following domains within your organization’s network: awsapps.com and amazonaws-us-gov.com for native Amazon Quick and Active Directory users; amazonaws-us-gov.com for IAM users.
+ You can also use specialized configurations to authenticate with a different identity service, even if Amazon Quick does not directly support them. For example, you can use Amazon Cognito as is described in the [Embedded Analytics Tutorial](https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/). This authentication method works because it is compatible and transparent to Amazon Quick. For more information about Amazon Quick authentication, see [Identity and Access Management in Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/identity.html).
+ If you are using the [Embedded Analytics Tutorial](https://aws.amazon.com/getting-started/hands-on/embedded-analytics-tutorial-introduction/), you can point to AWS GovCloud (US) ARNs and URLs for your resources, but in the step for the static website that uses Amazon CloudFront and Amazon S3, you need to point to a classic AWS Region, for example US East (N. Virginia), for the tutorial to work. This is not necessary outside the tutorial. For more information and additional examples, see [Developing with Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/quicksight_dev.html) in the Amazon Quick User Guide.

## Documentation
<a name="documentation"></a>
+  [Amazon Quick documentation](https://docs.aws.amazon.com/quicksuite/) 

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ No data will leave the AWS GovCloud (US) Regions for this service.