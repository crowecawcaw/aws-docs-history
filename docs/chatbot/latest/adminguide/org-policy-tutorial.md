AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Creating chat applications policies in Amazon Q Developer in chat applications

In this tutorial, you use the Amazon Q Developer in chat applications console to create a chat applications policy that:

- Restricts chat client access to Slack
- Specifies usable Slack workspaces
- Restricts usage to private channels
- Requires user-level roles
  Subsequently, all Amazon Q Developer in chat applications configurations in your organization must adhere to these specifications.

###### Topics

- [Prerequisites](#org-policy-tutorial-prq "#org-policy-tutorial-prq")
- [Step 1: Create a new chat applications policy](#org-policy-tutorial-s1 "#org-policy-tutorial-s1")
- [(Optional) Step 2: Testing your chat applications policy](#org-policy-tutorial-s2 "#org-policy-tutorial-s2")

## Prerequisites

You must have already created an organization using AWS Organizations. For more information, see [Managing an organization with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md")
in the _AWS Organizations User Guide_.

## Step 1: Create a new chat applications policy

###### To create a new chat applications policy

1.  Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2.  In the left sidebar menu, choose **Organization settings**.
3.  Choose **Chat applications policies**.
4.  Choose **Create chat applications policies**.
5.  1. ###### Enable Amazon Q Developer in chat applications Orgs policies:

    ###### Note

    Before you can create and attach a policy to your organization, you must enable that policy type for use.
    This is a one-time task on the organization root. You can enable a policy type from only the organization’s management account.
    For more information, see [Enabling and disabling policy types](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md") in the _AWS Organizations User Guide_.

    On the Chat applications policies page, choose **Enable**.

6.  1. ###### Enter your policy **Details**:

    Enter a policy name. 2. (Optional) Enter a policy description.

7.  (Optional) Add tags.
8.  1. ###### Configure chat client access:

    In **Set Amazon Chime chat client access**, choose **Deny Chime access**. 2. In **Set Microsoft Teams client access**, choose **Deny access to all Teams**. 3. In **Set Slack chat client access**, choose **Restrict access to named Slack workspaces**:

        1. Enter a Slack workspace ID.



        ###### Tip

        You can find your workspace ID in the Amazon Q Developer in chat applications console by choosing the configured client in the left sidebar and looking under **Workspace details**.
        2. (Optional) Choose **Add new workspace ID** to add another Slack workspace.
        3. Choose **Add**.

    4. Select **Enable usage to only private Slack channels**.

9.  1. ###### Set IAM permission types:

    Select **Enable User level IAM role**.

10. Choose **Create policy**.

## (Optional) Step 2: Testing your chat applications policy

If you already have an Amazon Q Developer in chat applications configuration, you can sign in as a user in any of your member accounts and try to perform any of the following actions:

- Create an Amazon Q Developer in chat applications configuration for Microsoft Teams
- Create a Slack Amazon Q Developer in chat applications configuration for a workspace you didn't specify in your policy
- Create a Slack Amazon Q Developer in chat applications configuration that uses a channel role

When you try to perform these actions, you should receive an error message that explains why you’re disallowed.
