

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Step 2: Create a Systems Manager Cloud Connector
<a name="cloud-connector-create-ssm-connector"></a>

After the AWS Config connector is set up, create the Systems Manager Cloud Connector. The Systems Manager Cloud Connector stores the Azure tenant and subscription configuration and links it to the AWS Config connector.

**To create a Systems Manager Cloud Connector**

1. Run the following command. Replace the placeholder values with your Azure tenant ID, the Systems Manager application (client) ID, subscription IDs, the Systems Manager Azure federation role ARN, and the AWS Config connector ARN from Step 1.
**Create the federation role before you run this command**  
Before you run this command, the Systems Manager Azure federation role that `--role-arn` identifies must already exist. Its trust policy must also allow the Systems Manager service principal (`ssm.amazonaws.com`) to assume it. The AWS CLI and API do not create this role for you. If either requirement is not met, the command fails. The error message is `ValidationException: Nonexistent role or missing ssm service principal in trust policy`. Create the role first with the trust and permissions policies in [Azure federation role](cloud-connector-azure-federation-role.md). Use the same role name and ARN that you used for the federated identity credential subject in [Azure prerequisites](cloud-connector-prereqs-azure.md).

   ```
   aws ssm create-cloud-connector \
       --display-name "{{MyAzureConnector}}" \
       --configuration '{
           "AzureConfiguration": {
               "TenantId": "{{TENANT_ID}}",
               "ApplicationId": "{{SSM_APP_CLIENT_ID}}",
               "Targets": {
                   "Subscriptions": [
                       {"Id": "{{SUBSCRIPTION_ID}}"}
                   ]
               }
           }
       }' \
       --role-arn "arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-AzureRole-{{CONNECTOR_NAME}}" \
       --config-connector-arn {{CONFIG_CONNECTOR_ARN}}
   ```

   To target all subscriptions in the tenant (tenant-level setup), omit the `Targets` field from the configuration.

   The response returns the `CloudConnectorId`. Note this value for future operations.

1. Verify the Cloud Connector was created successfully:

   ```
   aws ssm get-cloud-connector \
       --cloud-connector-id {{CLOUD_CONNECTOR_ID}}
   ```