NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Deploy role using a CloudFormation template

For multiple accounts, you can use CloudFormation StackSets to deploy the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role to member accounts. The MGN console provides templates for download, as described in [Download the CloudFormation templates](create-permissions-console.md#download-cloudformation-templates "create-permissions-console.md#download-cloudformation-templates") under "Create roles using the MGN console".

If you prefer to deploy the roles using CloudFormation StackSets manually, you can download the templates from the **Add connector** page:

1. On the **MGN connectors** page, choose **Add connector**.
2. Under **IAM Roles**, expand **View or deploy roles yourself** to access the template download options.
3. Download the **Member Account Template** (`mgn-connector-sharing-role.json`) to deploy to member accounts.
4. Using the CloudFormation console or AWS CLI, create a StackSet from the template and deploy it to the desired member accounts. For instructions, see [Getting started with AWS CloudFormation StackSets](../../../cloudformation/latest/userguide/stacksets-getting-started.md "../../../cloudformation/latest/userguide/stacksets-getting-started.md") in the _AWS CloudFormation User Guide_.
