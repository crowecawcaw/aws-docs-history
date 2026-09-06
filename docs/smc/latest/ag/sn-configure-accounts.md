

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS accounts to synchronize in the Connector
<a name="sn-configure-accounts"></a>

 Learn how to configuring AWS accounts to synchronize in the Connector. 

1. Log in as the system administrator. 

1. Enter **AWS** in the navigator. Choose the **AWS Service Management** scoped app.

1. In the **Accounts** menu, create one entry for every AWS account. Use the keys and secret keys from the users you created in AWS. 

**To create an account entry**

1. Enter the name as an account entry identifier, such as **Connector\_Demo** (for Commercial Region), or **Connector\_Demo\_GovCloud** (for GovCloud Region).

1. Enter the access key and secret access key from the AWS account *sync user *IAM configurations.

1. Enter the access key and secret access key from the AWS account *end user* IAM configurations.

1. Choose the visible AWS service integrations for this AWS account. The choices include:
   + Integrate with Service Catalog (including AppRegistry)
   + Integrate with AWS Config

     Choose AWS Config if you plan to integrate AWS Config cloud resources per each AWS account or through the latest AWS Config aggregator integration feature. The Connector for ServiceNow includes an AWS Config aggregator feature that enables ServiceNow administrators to align aggregated AWS Config details into one AWS account.

     If you plan to view AppRegistry related resources details, choose **AWS Config **with **AWS Service Catalog**.
   + Integrate with AWS Systems Manager Automation

     Choose AWS Systems Manager Automation if you want to execute automation documents (runbook) to remediate incidents from OpsItems. 
   + Integrate with AWS Systems Manager OpsCenter
   + Integrate with AWS Security Hub CSPM
   + Integrate with Support
   + Integrate with AWS Systems Manager Change Manager
   + Integrate with AWS Health
   + Integrate with AWS Systems Manager Incident Manager

1. Choose **Account Regions**. Select the **Commercial** or **GovCloud Region**. To see the AWS account Regions, double-click **Insert a new row…**. 
**Note**  
AWS Support API uses a specific GovCloud endpoint for GovCloud accounts to enable Support integration for GovCloud accounts. Choose a GovCloud Region in Account Regions when you onboard the account in ServiceNow. 

1. Repeat the step above to insert additional Regions.

1. Save or update the account entries.

1. Validate AWS account connectivity by following the steps in [Validating connectivity to AWS Regions](validate-regions.md). Note that in this Connector for ServiceNow, **Validate Accounts** only appears once after you submit or update the account entry. 
**Note**  
AWS Service Management Connector allows synchronization of updated keys using any automation or integration through a REST endpoint. For more information, see [Syncing updated keys programatically in ServiceNow](sn-sync-keys.md). 