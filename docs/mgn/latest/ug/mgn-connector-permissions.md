NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# IAM roles needed for the MGN connector

To use MGN connector you must have these required IAM roles for individual accounts and AWS Organizations networks:

- **AWSApplicationMigrationConnectorManagementRole**
- **AWSApplicationMigrationConnectorSharingRole\_management-account-id**

* Needed in _every_ account that contains source servers on which the connector installs agents. MGN supports cross-account scenarios. In an individual account setup this is the connector's own account. In an organization, the role is needed on _every_ account, including the management account. _management-account-id_ is the ID of the account in which the connector is created.

###### Note

The **MGNConnectorInstallerRole** is no longer required. Its permissions are now included in the **AWSApplicationMigrationConnectorManagementRole**, whose credentials the connector installer obtains from the AWS Systems Manager agent through the SSM hybrid activation. If you created the **MGNConnectorInstallerRole** previously, it is no longer used.

You can create these roles in the following ways:

- **Using the AWS Transform MGN console (recommended):** When you add a connector using the MGN console, the service can create the required roles for you, in an individual account or across all member accounts of your AWS Organization. For details about the roles the console creates, see [Create roles using the MGN console](create-permissions-console.md "create-permissions-console.md").
- **Manually, for an individual account:** For an MGN connector in an individual account, create these roles as described in
  [Create roles manually](create-permissions-manually.md "create-permissions-manually.md").
- **With a CloudFormation StackSet, for multiple accounts:** If the MGN connector manages source servers from multiple accounts,
  set up the global view feature and set up your AWS Organization, as described in [Manage large-scale migrations with global view](global-view.md "global-view.md"). After you set up your AWS Organization, configure the CloudFormation StackSet to create the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role in member accounts. For instructions, see [Deploy role using a CloudFormation template](CloudFormation_Template.md "CloudFormation_Template.md").
