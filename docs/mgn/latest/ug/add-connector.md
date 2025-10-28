NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Add MGN connector

To add an MGN connector, click **Add MGN connector**, to open the Add MGN connector page. Set up your MGN connector by providing the following:

- Connector name: The MGN connector name is used to identify the connector. This field is mandatory, and limited to 256 characters. The name must be unique (case-insensitive) per account per Region.
- Obtain the SSM hybrid activation parameters (installation key and ID), which is required in order install the SSM agent on the MGN connector. For more information on SSM activation parameters see [here](../../../systems-manager/latest/userguide/sysman-managed-instance-activation.md "../../../systems-manager/latest/userguide/sysman-managed-instance-activation.md").
  - In the SSM hybrid activation set the **AWSApplicationMigrationConnectorManagementRole** in the management account.
  - Activation setting → select an existing IAM role → **AWSApplicationMigrationConnectorManagementRole**
  - See the [permissions](mgn-connector-permissions.md "mgn-connector-permissions.md") page for the required permissions of **AWSApplicationMigrationConnectorManagementRole**.

- Temporary IAM credentials of the **MGNConnectorInstallerRole** role that you created
  [here](mgn-connector-permissions.md "mgn-connector-permissions.md").

      + Request temporary security credentials
       [through AWS STS](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md")
       through the
       [AssumeRole API](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md").
      + [Learn more about how temporary credentials work.](Agent-Related-FAQ.md#temporary-credentials-operation "Agent-Related-FAQ.md#temporary-credentials-operation")

  To download the MGN connector software, use the following commands:

- **Download the installer command** - Copy and paste the command into the command prompt of the server you’ve designated for the MGN connector. This will download the AWS MGN installer.
- **Copy and paste this command into the command line on your MGN connector** - Copy and paste the command into the command prompt of the same server. This will install the AWS MGN connector software.
  After the MGN connector is installed it automatically begins communicating with the console and appears in the MGN connectors list.

Next, you must register source servers to the MGN connector.

You may install multiple MGN connectors to handle large amount of source servers or multiple data centers. Each MGN connector is able to handle up to 500 source servers. AWS MGN supports up to 50 MGN connectors per account per region.

The MGN connector installation is facilitated through the SSAF client, which is publicly accessible from the S3 bucket `aws-application-migration-service-{{region}}`.
The most recent installer can be found at `/latest/source-automation-client/linux/ssaf-client/`,
with a corresponding signature file at `/latest/source-automation-client/linux/ssaf-client/ssaf_client.sig` for binary validation.
For user convenience, these technical aspects are handled automatically when using either the console or the SSM document _"AWSMigration-RunSourceServerAction"_ to perform the installation.
