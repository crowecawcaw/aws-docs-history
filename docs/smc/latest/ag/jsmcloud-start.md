

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Prerequisites for AWS Service Management Connector for Jira Service Management Cloud
<a name="jsmcloud-start"></a>

Before installing the AWS Service Management Connector for Atlassian's Jira Service Management Cloud, you must have an AWS account and an Atlassian site with [Jira Service Management pre-installed](https://support.atlassian.com/jira-service-management-cloud/). You must also verify that you have the necessary permissions in your AWS account and on the Jira Service Management website.

## AWS prerequisites
<a name="aws-prereqs"></a>

To start, use the following integrations:
+ **Service Catalog** 

  You need an AWS account to configure your AWS portfolios and products. For details, refer to [Setting up for Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/setup.html). 
+ **AWS Security Hub CSPM**

  You must enable the service in all Regions and accounts where you want to sync Findings. For details, refer to [Setting up Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html). We recommend you connect Jira Service Management with the primary (main) AWS account for AWS Security Hub CSPM. For more information, refer to [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html).
+ **AWS Systems Manager Incident Manager**

  You must enable Incident Manager in all AWS Regions and accounts from which you want to sync incidents. For more information, refer to [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/incident-manager.html). 
+ **AWS Systems Manager Automation with the Connector**

  This feature requires no setup in AWS. AWS provides a number of automation documents (runbooks). If you want additional runbooks, you can retrieve them in the Connector. For more information, see [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) in the *AWS Systems Manager user guide*.
+ **Support with the Connector**

  Your account must have a Business or Enterprise Support plan to use support integration with the Connector. 

## Jira Service Management Cloud prerequisites
<a name="jsmcloud-prereqs"></a>

In addition to the AWS account, you must have an existing Jira Project, or create a new Project. The initial installation should occur in either an enterprise sandbox or a [Atlassian Jira Service Management](https://www.atlassian.com/software/jira/service-management) site, depending on your organization’s technology governance requirements. 

The Jira administrator must have the Admin role to install the Connector for Jira Service Management Cloud.

For details about Jira Service Management agent onboarding, refer to the [Quick Start Guide](https://www.atlassian.com/software/jira/service-management/product-guide/getting-started/service-request-management). 