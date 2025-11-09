NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Set up the MGN Connector

In order to set up your MGN connector, take the following steps:

1. Make sure your account have the required permissions as defined [here](mgn-connector-permissions.md "mgn-connector-permissions.md").
2. If the MGN connector manages source servers from multiple accounts, set up the global view feature and set up your AWS Organization, following the instructions [here](global-view.md "global-view.md").

After you set up your AWS Organization, configure the CloudFormation StackSet in order to create the required role per management account. Use the template "Enable Application Migration Service Connector access". Full instructions are available [here](setting-up-stacksets.md "setting-up-stacksets.md"). 3. If the MGN connector manages source servers from a single account,
and both the MGN connector and the source servers belong to the same account:

    1. After replacing **ACCOUNT-ID** with your account number,
     create a role using the following trust policy:




    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "AWS": "arn:aws:iam::`111122223333`:role/AWSApplicationMigrationConnectorManagementRole"
     },
     "Action": "sts:AssumeRole"
     }
     ]
    }`

    ```
    2. Attach the **AWSApplicationMigrationAgentInstallationPolicy** policy
     to the Permission policies.
    3. Name the role
     **AWSApplicationMigrationConnectorSharingRole\_ACCOUNT-ID**
     (replace **ACCOUNT-ID** with your account number).

4. [Create a new MGN connector](add-connector.md "add-connector.md")
   on the MGN connectors page.
