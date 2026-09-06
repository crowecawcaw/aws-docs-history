NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Set up the MGN Connector

To add an MGN connector, click **Add MGN connector**, to open the Add MGN connector page. Set up your MGN connector by providing the following:

1. **Connector name**: The MGN connector name is used to identify the connector. This field is mandatory, and limited to 256 characters. The name must be unique (case-insensitive) per account per Region.
2. **IAM roles** - The MGN console will automatically create the required IAM roles in your account. For details about the roles created, see [Create roles using the MGN console](create-permissions-console.md "create-permissions-console.md").

   - **Automatic role generation:** The setup page will automatically generate these two roles in your account:

     - **AWSApplicationMigrationConnectorManagementRole** - Used during agent installation to access credentials.
     - **AWSApplicationMigrationConnectorSharingRole\_<ACCOUNT-ID>** - Contains permissions for agent installation.

   - **IAM roles deployment scope:**

     - **Individual account:** For an MGN connector in an individual account, the roles are created automatically.
     - **Multiple accounts:** If the MGN connector manages source servers from multiple accounts, set up the global view feature and set up your AWS Organization, as described in [Manage large-scale migrations with global view](global-view.md "global-view.md"). Alternatively, you can download a CloudFormation template from the setup page to deploy the IAM roles yourself.

3. **SSM Hybrid Activation** - Create a 30-day SSM Hybrid Activation for secure communication between the connector and AWS Systems Manager. This activation enables the connector to register as a managed instance.
4. **Acknowledge and create resources** - Click to generate the selected resources.
5. **Installation command** - The setup page generates a one-line installation command with all necessary credentials and configuration.
6. **Connector installation** - Install the connector on a Linux machine in your environment. For information on the required Linux machine, see [Prerequisites](mgn-connector-prerequisites.md "mgn-connector-prerequisites.md").

   1. Copy the installation link from the setup page.
   2. SSH into your chosen Linux machine.
   3. Paste and execute the installation command.
   4. Wait for installation to complete (typically 2–3 minutes).

7. **Register servers** - Go to the MGN Connector page in the AWS Transform MGN console and click on the MGN connector name. Go to "Register servers" to attach source servers with the MGN connector.
8. **Configure credentials** - Select the source servers on which you want to install the replication agent. Go to **Actions** and then **Register server credentials**. You can use an existing AWS Secrets Manager secret or create a new one. If multiple source servers share the same secret, you can select them together and apply the secret to all of them in a single operation. For more information, see [Register server credentials](connector-register-server-credentials.md "connector-register-server-credentials.md").
9. **Agent deployment** - Once credentials are configured and verified, select the source servers and go to **Actions**, then choose **Install replication agent**. You can keep track of the agent installation status in the **Agent installed** column in the console, or on the **Command history** page.

The deployment process for each server:

    1. MGN connector sends deployment commands to the connector via SSM.
    2. The connector retrieves credentials from AWS Secrets Manager.
    3. The connector connects to the source server using the configured credentials.
    4. The connector validates that the source server meets all prerequisites required to run the replication agent.
    5. The connector installs and configures the replication agent.
    6. The connector verifies successful installation and connectivity.

## Connector reuse and lifecycle

When deploying agents for subsequent waves, you can use an existing connector or create a new one. MGN connector console page lists all connectors configured in your account, showing the connector name, attached server count, and last seen date.

SSM Hybrid Activations expire after 30 days. The activation is required only for installing the connector on the Linux machine. Once the connector is installed, you can continue to use it to install replication agents on source servers even after the activation expires. If you need to install the connector on a new machine after the activation has expired, you need to create a new connector through the setup process.
