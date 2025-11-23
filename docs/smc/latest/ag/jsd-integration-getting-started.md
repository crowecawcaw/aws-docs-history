# Prerequisites for Jira Service Management Data Center

Before installing the AWS Service Management Connector for Jira
Service Management, you need an AWS account and an Atlassian instance
with [Jira Service Management pre-installed](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSD_2.0.8.zip "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSD_2.0.8.zip"). Verify that you have the
necessary permissions in your AWS account and Jira Service Management
software.

For a zip file containing Connector add-on code as well as AWS
Configuration files, download and extract the [AWS Service Management Connector for JSM configuration
files](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSD_2.0.7.zip "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSD_2.0.7.zip").

## AWS prerequisites

- To use Service Catalog with the Connector, you need an AWS account to
  configure your AWS portfolios and products. For more information,
  see [Setting Up AWS Service Catalog](../../../servicecatalog/latest/adminguide/setup.md "../../../servicecatalog/latest/adminguide/setup.md").
- To see AWS Config details, configure the service settings to record
  data for the resource types of interest. We recommend including
  provisioned products and CloudFormation stacks, in addition to the major
  resource types your team uses. For more information, see [Setting Up AWS Config with the Console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md").
- To use AWS Systems Manager Automation with the Connector, you don't need
  AWS-side setup. A number of automation documents are available
  from AWS as standard. If you want to use additional automation
  documents, they are available in the Connector. For more
  information, see [Working with Automation Documents (Playbooks)](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md").
- To use AWS Systems Manager OpsCenter with the Connector, enable OpsCenter
  in the AWS Systems Manager console. For more information, see [AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md"). The Connector also
  enables viewing resources and automation documents (runbooks)
  associated to OpsItem. For more information to associate resources
  to OpsItems in AWS OpsCenter, see [Working with Related Resources](../../../systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.md#OpsCenter-working-with-OpsItems-related-resources "../../../systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.md#OpsCenter-working-with-OpsItems-related-resources") . For more information to
  associate automation documents to OpsItems in AWS OpsCenter, see
  [Remediating OpsItem issues using Systems Manager automation](../../../systems-manager/latest/userguide/OpsCenter-remediating.md "../../../systems-manager/latest/userguide/OpsCenter-remediating.md").
- To use AWS Security Hub with the Connector, you must enable the service
  in all Regions and accounts where you want to sync Findings. For
  more information, see [Setting up Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md"). We recommend you connect Jira
  Service Management with the primary AWS account for AWS Security Hub. For
  more information, see [Managing administrator and member accounts.](../../../securityhub/latest/userguide/securityhub-accounts.md "../../../securityhub/latest/userguide/securityhub-accounts.md")
- To use Support with the Connector, your account must have a [Business](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/") or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") Support plan to use support
  integration.
- To use AWS Systems Manager Incident Manager with the Connector and allow the
  Connector to synchronize Incidents for a specific Region, you must
  enable Incident Manager in that account and Region. For details on
  the service endpoint, see [AWS Systems Manager Incident Manager endpoints and quotas](../../../general/latest/gr/incident-manager.md "../../../general/latest/gr/incident-manager.md").

###### Note

AWS Service Management Connector allows AWS Managed Services (AMS) Accelerate
users to create Incidents and Service Requests through Jira Service
Management. To ensure that your account has the required permissions
to create AMS Accelerate support cases, make sure you onboard your
account to Accelerate. For more information, see [Getting Started with AMS Accelerate](../../../managedservices/latest/accelerate-guide/getting-started-acc.md "../../../managedservices/latest/accelerate-guide/getting-started-acc.md").

For each AWS account, the Connector for Jira Service Management
also requires API access with [Baseline permissions.](jsd-baseline-permissions.md "jsd-baseline-permissions.md")

## Jira Service Management prerequisites

In addition to your AWS account, you need the Jira Service
Management software installed on your Atlassian instance before you can
install the AWS Service Management Connector add-on. The Jira Service
Management administrator needs the _admin_ role to install the AWS Service Management
Connector add-on.

Before configuring your AWS connector, ensure you follow Atlassian
recommendations for securing your Jira Service Management instances. For
more information, see [Preventing Security Attacks](https://confluence.atlassian.com/adminjiraserver/preventing-security-attacks-938847893.html "https://confluence.atlassian.com/adminjiraserver/preventing-security-attacks-938847893.html").

The Connector for Jira Service Management add-on is available to
download in the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1221283/aws-service-catalog-connector-for-jsd "https://marketplace.atlassian.com/apps/1221283/aws-service-catalog-connector-for-jsd").
