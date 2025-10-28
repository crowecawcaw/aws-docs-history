AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Creating a custom action using Amazon Q Developer in chat applications

You can create custom actions using AWS CLI commands, Automation runbooks and Lambda functions in your account, or by using the [Amazon Q Developer in chat applications in chat applications API](../APIReference/Welcome.md "../APIReference/Welcome.md"). AWS CLI command Shortcuts function similarly to [Command aliases](creating-aliases.md "creating-aliases.md").

Automation action

###### To create an Automation action

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.
2. In **Manage actions**, choose **Create**.
3. Enter a custom action name. This name is a unique identifier for your custom action.
4. Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis.
5. For **Custom action type**, select **Automation runbook action**.
6. Choose **Next**.
7. Select an AWS account.
8. Select a Region.

###### Note

The available Automation runbooks are populated from this account and Region. 9. Select an Automation runbook owner. This value defaults to **Owned by me**.

###### Note

You can filter runbooks by owner. For more information about owner types, see
[Editing an existing Systems Manager automation document](../../../cloud9/latest/user-guide/systems-manager-automation-docs.md#systems-manager-open "../../../cloud9/latest/user-guide/systems-manager-automation-docs.md#systems-manager-open") in the _AWS Cloud9 User Guide_. 10. Choose **Load Automation runbooks**. 11. In **Define Automation runbook**, select an Automation runbook. 12. Enter your input parameters.

###### Note

We expose predefined variables from your custom notifications as useable variables. 13. (Optional) Add more variables by choosing **+ Add more variables**. 14. Choose **Next**. 15. (Optional) Add additional display criteria:

    1. Select a variable.
    2. Select a condition.
    3. Choose **Add**.

16. Choose **Save**.

When you run a runbook, you're prompted to select the IAM role used to run it. You can select from assumable roles in the account configured with your chat channel.
If you don't select a role, the runbook runs using your channel role.

CLI action

###### To create an AWS CLI command action

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.
2. In **Manage actions**, choose **Create**.
3. Enter a custom action name. This name is a unique identifier for your custom action.
4. Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis.
5. For **Custom action type**, select **CLI action**.
6. Enter a command.

###### Note

We expose predefined variables from your custom notifications as useable variables. 7. (Optional) Add more variables by choosing **+ Add more variables**. 8. Choose **Next**. 9. (Optional) Add additional display criteria:

    1. Select a variable.
    2. Select a condition.
    3. Choose **Add**.

10. Choose **Save**.

Lambda action

###### To create a Lambda action

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.
2. In **Manage actions**, choose **Create**.
3. Enter a custom action name. This name is a unique identifier for your custom action.
4. Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis.
5. For **Custom action type**, select **Lambda action**.
6. Choose **Next**.
7. Select an AWS account.
8. Select a Region.

###### Note

The available Lambda functions are populated from this account and Region. 9. Choose **Load Lambdas**. 10. In **Define Lambda Function**, select a Lambda function. 11. Enter your payload.

###### Note

We expose predefined variables from your custom notifications as useable variables. 12. (Optional) Add more variables by choosing **+ Add more variables**. 13. Choose **Next**. 14. (Optional) Add additional display criteria:

    1. Select a variable.
    2. Select a condition.
    3. Choose **Add**.

15. Choose **Save**.
