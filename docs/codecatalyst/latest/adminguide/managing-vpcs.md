Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Editing VPC connections for a space

You can edit the configuration for a VPC connection, such as the associated subnets or security groups.

You must have the **Space administrator** role or **Power user** role to
manage VPC connections at the space level.

###### Warning

While VPC-connected workflows are in progress, we recommended that you do not edit your VPC connection or your VPC role. If
the associated VPC is edited while your workflow is in progress, your workﬂow will continue to run with the initial VPC connection. If
a VPC role is edited to remove necessary permissions while your workflow is in progress, you will not be able to cleanup your resources.

###### To edit VPC connections

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space.

###### Tip

If you belong to more than one space, choose a space in the top
navigation bar. 3. Choose **Settings**, and then choose
**VPC connections**.

The page lists all VPC connections in your space. You can view the
**VPC connection name** name, the **VPC ID**, and
the associated **AWS account connection**. 4. Choose the VPC connection name that you want to manage, and then choose
**Edit**. 5. Edit your VPC connection as needed, and then choose **Update VPC connection**.
