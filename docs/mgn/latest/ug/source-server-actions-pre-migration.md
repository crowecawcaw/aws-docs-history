

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Actions before migration
<a name="source-server-actions-pre-migration"></a>

After installing the AWS Replication Agent and before initiating a test or cutover launch, you can perform the following actions on your source servers to prepare them for migration.

## Edit replication settings
<a name="source-server-actions-edit-replication-settings"></a>

You can customize the replication settings for each source server individually, or apply settings to multiple servers at once. Replication settings control how data is replicated from the source server to the staging area in AWS, including the replication server instance type, replication subnet, and encryption options.

To edit replication settings for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Replication**, then choose **Edit replication settings**.

1. Modify the settings as needed and choose **Save**.

**Note**  
Changes to replication settings take effect on the next replication cycle. Modifying settings while initial sync is in progress may cause the sync to restart.

## Edit launch settings
<a name="source-server-actions-edit-launch-settings"></a>

Launch settings control how the migrated server will be launched as an Amazon EC2 instance in AWS. You can configure instance type, subnet, security groups, IAM instance profile, and other launch parameters before initiating a test or cutover launch.

To edit launch settings for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Choose the source server name to open the **Server details** view.

1. Choose the **Launch settings** tab.

1. Modify the settings as needed and choose **Save**.

[Learn more about launch settings](launch-settings.md).

## Add or manage tags
<a name="source-server-actions-add-tags"></a>

You can add, edit, or remove tags on source servers at any time. Tags help you organize and identify servers, and can be used to filter the source servers list.

To manage tags for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Choose the source server name to open the **Server details** view.

1. Choose the **Tags** tab.

1. Choose **Manage tags** to add, edit, or remove tags. Choose **Save** when done.

## Configure post-launch actions
<a name="source-server-actions-configure-post-launch"></a>

Post-launch actions are scripts or SSM documents that run automatically on the launched instance after a test or cutover launch. You can configure post-launch actions before migration to automate tasks such as software installation, configuration changes, or validation checks.

To configure post-launch actions for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Choose the source server name to open the **Server details** view.

1. Choose the **Post-launch settings** tab.

1. Configure the desired post-launch actions and choose **Save**.

[Learn more about post-launch settings](post-launch-settings.md).

## Assign server to an application
<a name="source-server-actions-assign-application"></a>

You can group source servers into applications to manage and migrate related servers together. Assigning servers to an application before migration helps you coordinate test and cutover launches across multiple servers.

To assign a source server to an application:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Assign to application**.

1. Select an existing application or create a new one. Choose **Assign**.

[Learn more about applications](applications.md).