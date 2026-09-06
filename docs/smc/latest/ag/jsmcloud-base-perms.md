

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring baseline permissions for Jira Service Management Cloud
<a name="jsmcloud-base-perms"></a>

This section describes how to configure AWS Identity and Access Management (IAM) permissions, AWS Service Catalog, and other AWS services to use AWS Service Management Connector for Jira Service Management Cloud.

**Note**  
To align with best practices, AWS recommends periodically rotating IAM user access keys. For more information, refer to [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys).

**Topics**
+ [Available template for baseline permissions](#baseline-permissions-template)
+ [Creating AWS Service Management Connector Sync user](jsmcloud-scsyncuser.md)
+ [Creating AWS Service Management Connector end user](jsmcloud-scenduser.md)
+ [Creating SCConnectLaunch role](jsmcloud-scconnectlaunch.md)

## Available template for baseline permissions
<a name="baseline-permissions-template"></a>

For an CloudFormation template to configure Jira Service Management, refer to [AWS commercial Regions ](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Configurations_Commercialv7.0.0.json) and [AWS GovCloud (US) Regions](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Configurations_GovCloudv7.0.0.json). For each AWS account, the connector for Jira Service Management requires two IAM users:
+ **AWS Sync User**: An IAM user to sync AWS resources (such as portfolios, products, Incident Manager Incidents, security Findings, and Automation Documents) to Jira.
+ **AWS End User**: An IAM user who can provision products and execute automation documents as an end user. This role includes any required roles to provision and execute. 

These can be the same user, and can be an existing user. Service Management Connector recommends that you assign two new users for the Connector. 

**Note**  
The baseline CloudFormation template creates the **Sync User** and **End User** with required permissions and configures the AWS account for all available integrations. 