

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Managing a default VPC connection for a space
<a name="managing-vpcs.default"></a>

You can set a default VPC connection for a space. If you choose to set a default VPC connection, all workflow runs and Dev Environments in your space will run connected to the default VPC connection. You can override this by associating a different VPC connection in your workflow action or Dev Environment.

You must have the **Space administrator** role or **Power user** role to manage VPC connections at the space level.

**Topics**
+ [Setting a default VPC connection](#managing-vpcs.default.set)
+ [Removing a default VPC connection](#managing-vpcs.default.remove)

## Setting a default VPC connection
<a name="managing-vpcs.default.set"></a>

Use the following procedure to set a default VPC connection.

**To set a default VPC connection**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space.
**Tip**  
If you belong to more than one space, choose a space in the top navigation bar.

1. Choose **Settings**, and then choose **VPC connections**.

   The page lists all VPC connections in your space. You can view the **VPC connection name** name, the **VPC ID**, and the associated **AWS account connection**.

1. Choose the VPC connection name that you want to set as default.
**Note**  
If your VPC connection is associated with a project-restricted AWS account, your VPC connection will only have access to specific projects and cannot be set as default. For more information, see [Enabling or disabling project-restricted account connections](managing-accounts-restriction.md).

1. Choose **Manage default**, choose **Set as default** from the drop-down menu, then choose **Confirm**.

## Removing a default VPC connection
<a name="managing-vpcs.default.remove"></a>

Use the following procedure to remove a default VPC connection.

**To remove a default VPC connection**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space.
**Tip**  
If you belong to more than one space, choose a space in the top navigation bar.

1. Choose **Settings**, and then choose **VPC connections**.

   The page lists all VPC connections in your space. You can view the **VPC connection name** name, the **VPC ID**, and the associated **AWS account connection**.

1. Choose the default VPC connection name.

1. Choose **Manage default**, choose **Remove as default** from the drop-down menu, then choose **Confirm**.