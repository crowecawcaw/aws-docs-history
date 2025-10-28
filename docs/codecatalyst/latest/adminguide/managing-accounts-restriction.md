Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Enabling or disabling project-restricted account

connections

The default in CodeCatalyst is to add an AWS account connection to your space that is then
made immediately available for all projects and resources in the space. You can configure
account connections so that they are restricted to a specified set of projects. This allows
you to restrict which projects have access to connected AWS accounts. The access can be
restricted for account connections to workflows and VPC connections.

Connections are represented by a connection resource Amazon Resource Name (ARN) that is
unique to the connection between a specific AWS account and a specific space in CodeCatalyst.
The connection can be specified as restricted. The account connection will not be available
for workflows or default VPCs in CodeCatalyst.

## Considerations for

project-restricted account connections

The following considerations apply to project-restricted account connections.

- You must have the **Space administrator** or
  **Power user** role to configure account connections for
  restriction.

###### Note

With the **Power user** role, you can enable or disable
project restrictions for an account, but you can only configure access for projects
where you are a member.

- Any other projects that are using the account, such as workflows in a separate
  project, will no longer be able to use the account. Make sure to update any projects
  using the restricted account with an account that is not restricted.
- After specifying an account as enabled for restriction, you must explicity enable
  the project or projects that will have access.
- If you create a new project with an account connection that is enabled for project
  restriction, you will not be able to add the account connection to the new project's
  workflows until the project is enabled for the restricted account.

## Enabling project-restricted account

connections

Use these steps to enable an account for project restrictions and to specify projects
where access is enabled.

###### To enable project-restricted account connections

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **AWS accounts**.

The **Accounts** page displays. 3. Choose the account that you want to restrict for your space. Workflows in projects
and VPC connections for the space will not have access to the restricted accounts
available and their roles. Choose **Enable project
restrictions**.

###### Note

Only specified projects will be able to access the account connection. 4. Choose the project or projects where you want to enable access, and then choose
**Enable**. The account connection is now restricted to the selected
projects.

## Disabling project-restricted account

connections

Use these steps to remove project restrictions for a connected account.

###### To disable project-restricted account connections

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then
   choose **Account connections**.

The **Accounts** page displays. 3. Choose the project where you want to disable access, and then choose
**Disable**. 4. To completely disable project restrictions, choose **Disable project
restrictions**.

###### Note

Other projects will be able to access the account connection.
