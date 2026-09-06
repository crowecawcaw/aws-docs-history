

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Tutorial: Creating chat applications policies in Amazon Q Developer in chat applications
<a name="org-policy-tutorial"></a>

In this tutorial, you use the Amazon Q Developer in chat applications console to create a chat applications policy that:
+ Restricts chat client access to Slack
+ Specifies usable Slack workspaces
+ Restricts usage to private channels
+ Requires user-level roles

Subsequently, all Amazon Q Developer in chat applications configurations in your organization must adhere to these specifications.

**Topics**
+ [Prerequisites](#org-policy-tutorial-prq)
+ [Step 1: Create a new chat applications policy](#org-policy-tutorial-s1)
+ [(Optional) Step 2: Testing your chat applications policy](#org-policy-tutorial-s2)

## Prerequisites
<a name="org-policy-tutorial-prq"></a>

You must have already created an organization using AWS Organizations. For more information, see [Managing an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.

## Step 1: Create a new chat applications policy
<a name="org-policy-tutorial-s1"></a>

**To create a new chat applications policy**

1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/).

1. In the left sidebar menu, choose **Organization settings**. 

1. Choose **Chat applications policies**. 

1. Choose **Create chat applications policies**. 

1. 

   1. 

**Enable Amazon Q Developer in chat applications Orgs policies:**
**Note**  
Before you can create and attach a policy to your organization, you must enable that policy type for use. This is a one-time task on the organization root. You can enable a policy type from only the organization’s management account. For more information, see [Enabling and disabling policy types](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html) in the *AWS Organizations User Guide*. 

     On the Chat applications policies page, choose **Enable**. 

1. 

   1. 

**Enter your policy **Details**:**

      Enter a policy name. 

   1. (Optional) Enter a policy description. 

1. (Optional) Add tags. 

1. 

   1. 

**Configure chat client access:**

      In **Set Amazon Chime chat client access**, choose **Deny Chime access**. 

   1. In **Set Microsoft Teams client access**, choose **Deny access to all Teams**. 

   1. In **Set Slack chat client access**, choose **Restrict access to named Slack workspaces**: 

      1. Enter a Slack workspace ID. 
**Tip**  
You can find your workspace ID in the Amazon Q Developer in chat applications console by choosing the configured client in the left sidebar and looking under **Workspace details**.

      1. (Optional) Choose **Add new workspace ID** to add another Slack workspace. 

      1. Choose **Add**. 

   1. Select **Enable usage to only private Slack channels**. 

1. 

   1. 

**Set IAM permission types:**

     Select **Enable User level IAM role**. 

1. Choose **Create policy**. 

## (Optional) Step 2: Testing your chat applications policy
<a name="org-policy-tutorial-s2"></a>

If you already have an Amazon Q Developer in chat applications configuration, you can sign in as a user in any of your member accounts and try to perform any of the following actions:
+ Create an Amazon Q Developer in chat applications configuration for Microsoft Teams
+ Create a Slack Amazon Q Developer in chat applications configuration for a workspace you didn't specify in your policy
+ Create a Slack Amazon Q Developer in chat applications configuration that uses a channel role

When you try to perform these actions, you should receive an error message that explains why you’re disallowed.