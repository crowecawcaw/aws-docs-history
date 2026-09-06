

# Document History
<a name="history"></a>

The following table describes the important changes to the documentation for AWS Service Catalog. For notification about updates to this documentation, you can subscribe to an RSS feed.
+ **API version**: 2014-11-12
+ **Latest documentation update**: August 4, 2026

| Change | Description | Date | 
| --- |--- |--- |
| [Security IAM update](#history) | The `AWSServiceCatalogEndUserFullAccess` managed policy now includes the `cloudformation:UntagResource` permission. For more information about AWS managed policies for AWS Service Catalog, see [AWS managed policies for AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | August 4, 2026 | 
| [Security IAM update](#history) | The `AWSServiceCatalogAdminFullAccess` managed policy now includes the `cloudformation:UntagResource` permission. For more information about AWS managed policies for AWS Service Catalog, see [AWS managed policies for AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | August 4, 2026 | 
| [External Engines for AWS Service Catalog](#history) | AWS Service Catalog adds new documentation for external engines. External engines are represented through an `EXTERNAL` product type. The `EXTERNAL` product type allows for the integration of third-party provisioning engines, such as Terraform. You can use external engines to extend the capabilities of Service Catalog beyond the native AWS CloudFormation templates, enabling the use of other instructure as code (IaC) tools. For more information, see [External Engines for AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/external-engine.html). | May 16, 2024 | 
| [Security IAM update](#history) | AWS Service Catalog updates the `AWSServiceCatalogSyncServiceRolePolicy` policy to change `codestar-connections` to `codeconnections`. For more information, see [AWS managed policies for AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | May 7, 2024 | 

## Earlier Updates
<a name="document-history-archive"></a>

The following table describes the documentation release history of AWS Service Catalog prior to April 25, 2024.


| Feature | Description | Release date | 
| --- | --- | --- | 
| AWS Service Catalog | To learn about Hashicorp's changes to Terraform licensing and updating to the External product type, review [Updating existing Terraform Open Source products and provisioned products to the External product type](update_terraform_open_source_to_external.md).  | October 20, 2023 | 
| AWS Service Catalog | To learn about [Sharing a portfolio with AWS Organizations](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html) and allowing AWS Service Catalog to sync with AWS Organizations, see the [AWSServiceCatalogOrgsDataSyncServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceCatalogOrgsDataSyncServiceRolePolicy) policy and [AWSServiceRoleForServiceCatalogOrgsDataSync](using-service-linked-roles.md#slr-permissions2) service-linked role.  | April 14, 2023 | 
| AWS Service Catalog | To learn about [managing git-connected products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/git-synced-sc-products) and allowing AWS Service Catalog to sync templates in an external repository to your AWS Service Catalog products, see the [AWSServiceCatalogSyncServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceCatalogSyncServiceRolePolicy) policy and [AWSServiceRoleForServiceCatalogSync](using-service-linked-roles.md) service-linked role.  | November 18, 2022 | 
| AWS Service Catalog AppRegistry | To learn about how AppRegistry helps to store your AWS applications, their associated resource collections, and application attribute groups, see [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html). | June 15, 2022 | 
| AWS Service Management Connector | To learn about Connectors for Jira Service Management and ServiceNow, see [AWS Service Management Connector](https://docs.aws.amazon.com/servicecatalog/latest/smcguide/overview.html). | June 9, 2022 | 
| Connector for Jira Service Management | To learn about the updates to the Connector for Jira Service Management, see [AWS Service Management Connector for Jira Service Management.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-jiraservicedesk.html) | May 25, 2021 | 
| Connector for ServiceNow | To learn about the updates to the Connector for ServiceNow, see [AWS Service Management Connector for ServiceNow.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-servicenow.html) | April 7, 2021 | 
| Connector for ServiceNow | To learn about the updates to the Connector for ServiceNow, see [AWS Service Management Connector for ServiceNow.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-servicenow.html) | September 24, 2020 | 
| AWS Service Quotas | To learn about how AWS Service Catalog works with AWS Service Quotas, see [AWS Service Catalog default service quotas.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/limits.html) | March 24, 2020 | 
|  Getting Started Library  |  To learn about the library of well-architected product templates offered by AWS Service Catalog, see [Getting Started Library](getstarted-library.md)  | March 10, 2020 | 
| Version guidance | To learn about product version guidance, see [Version Guidance](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/managing-versions.html#version-guidance). | December 17, 2019 | 
| Connector for Jira Service Desk | To begin using the Connector for Jira Service Desk, see [AWS Service Management Connector for Jira Service Desk.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-jiraservicedesk.html) | November 21, 2019 | 
| Connector for ServiceNow | To learn about the updates to the Connector for ServiceNow, see [AWS Service Management Connector for ServiceNow.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-servicenow.html) | November 18, 2019 | 
| New security chapter | To learn about security in AWS Service Catalog, see [Security in AWS Service Catalog.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security.html) | October 31, 2019 | 
| Changing provisioned product owner | To learn about how to change the owner of provisioned products, see [Changing Provisioned Product Owner.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/change-pp-owner.html) | October 31, 2019 | 
| New resource update constraint | To learn about how to use the RESOURCE\_UPDATE constraint to update tags in provisioned products, see [AWS Service Catalog Tag Update Constraints.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-resourceupdate.html) | April 17, 2019 | 
| Connector for ServiceNow | To begin using the Connector for ServiceNow, see [AWS Service Management Connector for ServiceNow.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-servicenow.html) | March 19, 2019 | 
| Support for AWS CloudFormation StackSets | To begin using AWS CloudFormation StackSets, see [Using AWS CloudFormation StackSets.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html) | November 14, 2018 | 
| Self-service actions | To begin using self-service actions, see [AWS CloudFormation Service Actions.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-actions.html) | October 17, 2018 | 
| Amazon CloudWatch metrics | To learn about Amazon CloudWatch metrics, see [AWS Service CatalogAmazon CloudWatch.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/cloudwatch-metrics.html) | September 26, 2018 | 
| Support for TagOptions | To manage tags, see [AWS Service Catalog TagOption Library.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html) | June 28, 2017 | 
| Importing a portfolio | To import a portfolio that is shared from another AWS account, see [Importing a Portfolio.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html#catalogs_portfolios_sharing_importing) | February 16, 2016 | 
| Updates to permissions information | To grant access to the end user console view, see [Console access for end users.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html#permissions-end-users-console) | February 16, 2016 | 
| Initial release | This is the initial release of the AWS Service Catalog Administrator Guide. | July 9, 2015 | 