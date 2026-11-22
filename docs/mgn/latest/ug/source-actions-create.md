

# Creating source actions

Source actions are created in the member account where your source servers reside. Once created, they are available for execution by the MGN connector account.

## Creating a source action in the console
<a name="source-actions-create-overview"></a>

To create a new source action:

1. Navigate to **Settings** > **Source actions**

1. Choose **Create action**

1. Enter an **Action name** (required, unique within the account)

1. Enter an **Action description** (optional, helps identify the action's purpose)

1. Select the **Operating system**: Linux, Windows, or Both

1. Provide your script — either by choosing the **SSM Parameter Store parameter** that contains your script or by providing the script content directly
**Note**  
AWS Transform MGN supports only SSM parameters whose names start with `ManagedByAWSApplicationMigrationService`.  
If you create a source action in the delegated admin account for one of your member accounts, the **Script content** option is not available. The SSM parameter must exist in the member account, and the delegated admin account doesn't have permission to create SSM parameters in the member account through the AWS Transform MGN console. If you only have the script content, create the SSM parameter in the member account first, and then return to the delegated admin account and choose that parameter.

   When you provide the script content, AWS Transform MGN creates the SSM parameter for you from that content. The parameter name uses the following structure:

   `ManagedByAWSApplicationMigrationService-RemoteSourceAction-{{name}}-{{date}}`

   You can reuse the same SSM parameter in multiple source actions. To use a parameter across accounts, share it by using AWS Resource Access Manager and reference it by its ARN. For more information, see [Working with shared parameters in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the *AWS Systems Manager User Guide*.

   When you provide the script content, AWS Transform MGN creates the SSM parameter in your account's default parameter tier. The default tier is Standard unless you changed it, so by default a script larger than 4 KB is rejected. To use a larger script, up to 8 KB, either set your account's default parameter tier to Advanced or Intelligent-Tiering, or create an Advanced parameter in Parameter Store and choose it in the source action. For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the *AWS Systems Manager User Guide*.

1. Set the **Timeout** in seconds (default: 3,600 seconds, minimum: 60 seconds, maximum: 5,400 seconds)

1. (Optional) Add **Tags** to the source action. Each tag consists of a key and an optional value

1. Choose **Create**

The action is now created and available for execution by the MGN connector account.

You can use tags to search for and manage your source actions. On the **Source actions** page, filter the list by tag key or value.

## Editing a source action
<a name="source-actions-edit"></a>

To modify an existing source action:

1. Navigate to **Settings** > **Source actions**

1. Select the action from the list

1. Choose **Edit**

1. Modify the action details (name, description, operating system, timeout, tags, or script)

1. Choose **Save**

If you created the source action by providing script content, the edit page doesn't show the script content. It shows the SSM parameter that AWS Transform MGN created for you from that content. To change the script, provide new script content.

**Note**  
Editing an action does not affect jobs that are already running. The changes apply to new executions only.

## Deleting a source action
<a name="source-actions-delete"></a>

To delete a source action:

1. Navigate to **Settings** > **Source actions**

1. Select the action from the list

1. Choose **Delete**

1. Confirm the deletion

**Warning**  
Deleting a source action removes it from the account. This action cannot be undone. Running executions will continue, but the action will not be available for new executions.