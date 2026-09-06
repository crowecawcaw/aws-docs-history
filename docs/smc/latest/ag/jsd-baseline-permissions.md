

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Setting up baseline AWS users and permissions
<a name="jsd-baseline-permissions"></a>

This section provides instructions on how to set up the baseline AWS users and permissions for the AWS Service Management Connector for Jira Service Management.

**Topics**
+ [Available template for baseline permissions](#template-baseline)
+ [Creating AWS Service Management Connector Sync User](jsd-creating-sc-sync-user.md)
+ [Creating AWS Service Management Connector End User](jsd-creating-sc-end-user.md)
+ [Creating SCConnectLaunch Role](jsd-creating-scconnectlaunch-role.md)

## Available template for baseline permissions
<a name="template-baseline"></a>

To use an AWS CloudFormation template to set up the AWS configurations of the Connector for Jira Service Management, see the AWS configurations for [Connector for Jira Service Management - AWS Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSMv2.0.0-AWS_Configurations_Commercial.json ) and [Connector for Jira Service Management - AWS GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSMv2.0.0-AWS_Configurations_GovCloud.json).

**Note**  
If you use the Connector for Jira Service Management AWS Configuration template, go to the [Service Catalog Administrator Guide](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

For each AWS account, the Connector for Jira Service Management requires two sets of an access key identifier and a secret key for API access. These correspond to users in AWS Identity and Access Management (IAM). Specifically, you should set up:
+ An IAM user to sync AWS resources and to sync and manage Support cases through Jira Service Management.
+ An IAM user able to perform end user functionality to provision and execute requests exposed through Jira Service Management, including any roles required to perform the provisioning and execution. We recommend launch roles for Service Catalog to comply with IAM best practices.

These can be the same user and can be an existing user. We recommend you assign two new users for Connector.

**Note**  
To align with best practices, AWS recommends periodically rotating IAM user access keys. For more information, refer to [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys).