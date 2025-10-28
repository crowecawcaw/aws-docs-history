AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Configuring commands support on an existing chat channel using Amazon Q Developer in chat applications

If you have existing chat channels using the Amazon Q Developer in chat applications, you can reconfigure them in a few steps
to support the AWS CLI.

1. [Open the Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients "https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients").
2. In the **Configured Clients** page, select the chat client. If you have only one, its contents (the list of chat channels) appear on
   the page.

###### Note

In this procedure, we assume use of an existing Amazon Q Developer in chat applications chat channel configuration. The
process is very similar if you need to create a new chat client configuration by choosing
**Configure new client**. 3. Choose a channel from the **Configured channels** list, and choose
**Edit**. The selected channel can be public or private. 4. Define your **Role setting** by choosing a **Channel role** or **User roles**. For more information about role types, see [Role setting](understanding-permissions.md#role-settings "understanding-permissions.md#role-settings"):

Channel role

    1. For **Role setting**, choose **Channel role**.
    2. For **Channel role**, choose **Create new role**. If you want to use an existing role instead, choose **Use an existing role**.
     To use an existing IAM role, you will
     need to modify it for use with Amazon Q Developer in chat applications. For more information, see [Configuring an IAM Role
     for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md").
    3. For **Role name**, enter a name. Valid characters: a-z, A-Z,
     0-9, .\w+=,.@-\_.
    4. For **Role policy template**, choose **Read Only command
     permissions** and **Lambda-Invoke command permissions**.


    ###### Note



    	* If you plan to have users of the role submit Support cases, also attach the **AWS
    	 Support command permissions** policy.
    	* If you want the role to allow users to manage incidents, add the
    	 **Incident Manager Permissions** policy.

User roles

    1. For **Role setting**, choose **User roles**.

5. Select the policies that will make up your [channel guardrail policies](understanding-permissions.md#channel-guardrails "understanding-permissions.md#channel-guardrails"). Your channel guardrail policies control what actions are available to your channel members.

###### Note

If you initially had permission to run Lambda invoke, it is contained in **All actions permitted**.

###### Note

To run most CLI commands from your Slack channel, ensure you select **All actions permitted**.

###### Note

You do not need to edit or change the Amazon SNS topics configuration for the chat channel. 6. Choose **Save**.

You can use the IAM console to modify an existing IAM role. By simply attaching the
three additional Amazon Q Developer in chat applications policies to the IAM role, users of that role can immediately begin
using commands in the chat channel. To do so, see [Configuring an IAM Role for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md").

###### Important

If you have a large number of chat channels and you want to have the same command
permissions across multiple channels, you can apply the configured Amazon Q Developer in chat applications role to any of your
other chat channels without further modification. The IAM policies will be consistent across
chat channels that support commands in your Amazon Q Developer in chat applications service.
