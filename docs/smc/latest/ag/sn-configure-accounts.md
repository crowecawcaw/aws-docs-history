# Configuring AWS accounts to synchronize in

the Connector

Learn how to configuring AWS accounts to synchronize in
the Connector.

1. Log in as the system administrator.
2. Enter `AWS` in the navigator. Choose the
   **AWS Service Management** scoped app.
3. In the **Accounts** menu, create one entry for every AWS
   account. Use the keys and secret keys from the users you created in AWS.

###### To create an account entry

1. Enter the name as an account entry identifier, such as
   **Connector_Demo** (for Commercial Region), or
   **Connector_Demo_GovCloud** (for GovCloud
   Region).
2. Enter the access key and secret access key from the AWS account
   _sync user_ IAM
   configurations.
3. Enter the access key and secret access key from the AWS account
   _end user_ IAM configurations.
4. Choose the visible AWS service integrations for this AWS
   account. The choices include:
   - Integrate with Service Catalog (including AppRegistry)
   - Integrate with AWS Config

   Choose AWS Config if you plan to integrate AWS Config cloud resources per each
   AWS account or through the latest AWS Config aggregator integration
   feature. The Connector for ServiceNow includes an AWS Config aggregator
   feature that enables ServiceNow administrators to align aggregated
   AWS Config details into one AWS account.

   If you plan to view AppRegistry related resources details, choose
   **AWS Config** with **AWS Service Catalog**.
   - Integrate with AWS Systems Manager Automation

   Choose AWS Systems Manager Automation if you want to execute automation
   documents (runbook) to remediate incidents from OpsItems.
   - Integrate with AWS Systems Manager OpsCenter
   - Integrate with AWS Security Hub CSPM
   - Integrate with Support
   - Integrate with AWS Systems Manager Change Manager
   - Integrate with AWS Health
   - Integrate with AWS Systems Manager Incident Manager

5. Choose **Account Regions**. Select the **Commercial** or **GovCloud
   Region**. To see the AWS account Regions, double-click
   **Insert a new row…**.

###### Note

AWS Support API uses a specific GovCloud endpoint for GovCloud
accounts to enable Support integration for GovCloud accounts.
Choose a GovCloud Region in Account Regions when you onboard the account
in ServiceNow. 6. Repeat the step above to insert additional Regions. 7. Save or update the account entries. 8. Validate AWS account connectivity by following the steps in [Validating connectivity to AWS
Regions](validate-regions.md "validate-regions.md"). Note that in this Connector for ServiceNow,
**Validate Accounts** only appears once
after you submit or update the account entry.

###### Note

AWS Service Management Connector allows synchronization of updated
keys using any automation or integration through a REST endpoint. For more
information, see [Syncing updated keys programatically in ServiceNow](sn-sync-keys.md "sn-sync-keys.md").
