

# Configuring registered installation details
<a name="github-configuration"></a>

**Amazon Q Developer for GitHub: end of support**  
On January 30, 2027, AWS will discontinue support for the Amazon Q Developer for GitHub App. New app installations will no longer be available starting November 18, 2026.  
For capabilities similar to the Amazon Q Developer for GitHub App, explore Kiro and the Kiro GitHub App to access the latest models and features, including agentic coding, chat and MCP support. For more information, see [Kiro GitHub App on the Kiro website](https://kiro.dev/docs/web/github).  
For more information about the end of support, see [Amazon Q Developer end-of-support announcement](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) on the AWS DevOps Blog.

After you create an Amazon Q Developer profile and register the app installation in GitHub, you can do the following from the Amazon Q Developer console:
+ Enable or disable the use of code reviews. Feature development configuration cannot currently be modified.
+ Add tags to search and filter your resources or track AWS costs.
+ Delete a GitHub app installation registration.

## Editing features for Amazon Q Developer in GitHub
<a name="github-edit-features"></a>

The features available for Amazon Q Developer in GitHub are enabled by default when you install the app in GitHub and provide authorization to access your organization. You can choose to disable a feature if you no longer want to use the feature in GitHub.

**To enable or disable a feature for Amazon Q Developer in GitHub**

1. Navigate to the [Amazon Q Developer console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github).

1. In the navigation pane, under **Amazon Q Developer in GitHub**, choose **Registered installations**.

1. Under the **Name** column, choose the registration name for the installation you want to enable or disable a feature.

1. Under **Features**, choose **Edit** to configure the feature availability.

1. In the modal, choose the toggle for the feature you want to enable or disable, and then choose **Save** to confirm the changes.

After enabling or disabling a feature in the [Amazon Q Developer console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github), the changes are reflected in GitHub. Attempting to assign an issue to a Amazon Q Developer label after disabling the feature will lead to an error. Code reviews will no longer take place in new pull requests if the feature is disabled.

## Deleting Amazon Q Developer GitHub app installation registration
<a name="github-delete-app-install"></a>

You can delete a registration for one or more of your GitHub app installation through the Amazon Q Developer console. After permanently deleting your registration, all data associated with the registration is also deleted. The action can't be undone.

**To delete your GitHub app installation**

1. Navigate to the [Amazon Q Developer console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github).

1. In the navigation pane, under **Amazon Q Developer in GitHub**, choose **Registered installations**.

1. Do one of the following:
   + Under the **Actions** column, choose **Delete registration** for the installation you want to delete.
   + Under the **Name** column, choose the registration name for the installation you want to delete, and the choose **Delete**.

   Under the **Actions** column, choose **Delete registration** for registered installation you want to delete.

1. In the modal, review the details for deleting registration.

1. In the text input field, enter **confirm**, and then choose **Delete** to confirm the changes.

Once you delete a GitHub app installation, you can choose to register a new installation.