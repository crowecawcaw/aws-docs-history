

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Creating a custom action using Amazon Q Developer in chat applications
<a name="creating-custom-actions"></a>

 You can create custom actions using AWS CLI commands, Automation runbooks and Lambda functions in your account, or by using the [Amazon Q Developer in chat applications in chat applications API](https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html). AWS CLI command Shortcuts function similarly to [Command aliases](creating-aliases.md). 

------
#### [ Automation action ]

**To create an Automation action**

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.

1. In **Manage actions**, choose **Create**.

1.  Enter a custom action name. This name is a unique identifier for your custom action. 

1.  Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis. 

1. For **Custom action type**, select **Automation runbook action**.

1. Choose **Next**.

1. Select an AWS account.

1. Select a Region.
**Note**  
The available Automation runbooks are populated from this account and Region.

1. Select an Automation runbook owner. This value defaults to **Owned by me**.
**Note**  
You can filter runbooks by owner. For more information about owner types, see [Editing an existing Systems Manager automation document](https://docs.aws.amazon.com/cloud9/latest/user-guide/systems-manager-automation-docs.html#systems-manager-open) in the *AWS Cloud9 User Guide*.

1. Choose **Load Automation runbooks**.

1.  In **Define Automation runbook**, select an Automation runbook. 

1.  Enter your input parameters. 
**Note**  
We expose predefined variables from your custom notifications as useable variables.

1.  (Optional) Add more variables by choosing **\+ Add more variables**. 

1.  Choose **Next**. 

1.  (Optional) Add additional display criteria: 

   1. Select a variable.

   1. Select a condition.

   1. Choose **Add**.

1. Choose **Save**.

When you run a runbook, you're prompted to select the IAM role used to run it. You can select from assumable roles in the account configured with your chat channel. If you don't select a role, the runbook runs using your channel role.

------
#### [ CLI action ]

**To create an AWS CLI command action**

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.

1. In **Manage actions**, choose **Create**.

1.  Enter a custom action name. This name is a unique identifier for your custom action. 

1.  Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis. 

1. For **Custom action type**, select **CLI action**.

1.  Enter a command. 
**Note**  
We expose predefined variables from your custom notifications as useable variables.

1.  (Optional) Add more variables by choosing **\+ Add more variables**. 

1.  Choose **Next**. 

1.  (Optional) Add additional display criteria: 

   1. Select a variable.

   1. Select a condition.

   1. Choose **Add**.

1. Choose **Save**.

------
#### [ Lambda action ]

**To create a Lambda action**

1. Choose the vertical ellipsis button (**⋮**) on the bottom of a notification in your chat channel.

1. In **Manage actions**, choose **Create**.

1.  Enter a custom action name. This name is a unique identifier for your custom action. 

1.  Enter a name for your custom action button. This name is shown on a button on your notification. This name should be 20 characters or less and can incorporate emojis. 

1. For **Custom action type**, select **Lambda action**.

1. Choose **Next**.

1. Select an AWS account.

1. Select a Region.
**Note**  
The available Lambda functions are populated from this account and Region.

1. Choose **Load Lambdas**.

1.  In **Define Lambda Function**, select a Lambda function. 

1.  Enter your payload. 
**Note**  
We expose predefined variables from your custom notifications as useable variables.

1.  (Optional) Add more variables by choosing **\+ Add more variables**. 

1.  Choose **Next**. 

1.  (Optional) Add additional display criteria: 

   1. Select a variable.

   1. Select a condition.

   1. Choose **Add**.

1. Choose **Save**.

------