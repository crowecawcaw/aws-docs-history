# Amazon Quick Slack

extension user guide

As a user, you can access Amazon Quick directly within Slack to get
AI-powered assistance without leaving your workspace. The extension integrates
seamlessly into your Slack environment, providing instant access to
knowledge bases and intelligent responses.

###### Topics

- [Add a Slack
  Extension to your Slack](#slack-extension-setup-users "#slack-extension-setup-users")
- [Access Quick in your
  Slack side panel at any time](#access-slack-side-panel "#access-slack-side-panel")
- [Slack extension use cases](#slack-use-cases "#slack-use-cases")
- [Amazon Quick Slack
  extension usage guidelines](#slack-usage-guidelines "#slack-usage-guidelines")
- [Slack
  extension known limitations](#slack-extension-known-limitations "#slack-extension-known-limitations")

## Add a Slack

Extension to your Slack

Install the Amazon Quick app in your Slack workspace to enable
AI-powered assistance. This one-time setup makes Quick accessible
throughout your Slack environment.

###### Add a Slack Extension to your Slack

1. Open and login to the Slack workspace for your
   company.
2. Choose **More** in the left navigation, then select
   **Automations**.
3. Choose **Apps**.
4. Choose **+ Add apps**.
5. Search for **Quick** and choose
   Quick.
6. Select your Slack profile picture in the bottom left of
   Slack.
7. Navigate to **Preferences** >
   **Navigation** > **AI Apps and
   Agents** > select **Show app agents** >
   and select **Quick**.
8. Quick is now available to access anywhere in
   Slack through an icon in the top right of your
   Slack window.

###### Note

For more information, see [Understand AI apps in Slack](https://slack.com/help/articles/33076000248851-Understand-AI-apps-in-Slack "https://slack.com/help/articles/33076000248851-Understand-AI-apps-in-Slack") in the
Slack help center.

## Access Quick in your

Slack side panel at any time

Once you've added Quick to your Slack workspace,
you can access it conveniently through the side panel for quick assistance
without interrupting your workflow. The side panel provides persistent access to
Quick while you work in Slack channels and direct
messages.

###### Access Quick in your Slack side panel at any

time

1. Click on your Slack profile picture in the bottom left
   of Slack.
2. Navigate to **Preferences** >
   **Navigation** > **AI Apps and
   Agents** and select
   **Amazon Quick**.
3. Quick will now be available to access anywhere in
   Slack through an icon in the top right of your
   Slack window.

## Slack extension use cases

With Quick integrated into Slack, you can search
and access your organization's knowledge bases directly from your conversations.
This allows you to find relevant information, get answers to questions, and
enhance your communications without leaving Slack.

###### Search your organization's knowledge wherever you are

1. Open the Quick side panel from the top right of your
   Slack window or start a DM with Quick
   under **Apps**.
2. Ask Quick a question about its knowledge from your spaces
   and connected knowledge bases.
3. To personalize your conversation using your data, use the gear icon
   (visible after sending your first message to Quick) within
   your conversation to select an agent or a space to respond from.

###### Get Quick's in-context help in Slack

conversation threads

1. Navigate to a Slack conversation thread of your
   choice.
2. Type **@Amazon Quick** and ask any question about the
   messages in that thread or its knowledge from your spaces and
   Quick knowledge bases.
3. If Quick is not already added to the channel, you will be
   prompted to add it before receiving a response.

###### \*\*Perform actions in external

applications\*\*

1. Start a direct message (DM) with Quick.
2. Ask it to perform an action of your choice in an external application
   using [action connectors](../../../quicksuite/latest/userguide/action-connectors.md "../../../quicksuite/latest/userguide/action-connectors.md") configured by your
   organization.

###### Upload and analyze images

1. In any Slack channel or direct message, upload an image
   by dragging and dropping it or using the attachment button.
2. Mention **@Amazon Quick** and ask questions about the
   uploaded image, such as requesting analysis, descriptions, or
   insights.
3. Quick will analyze the image and provide relevant
   information based on your request.

## Amazon Quick Slack

extension usage guidelines

As a user, you are responsible for keeping company information safe. The
following guidance helps you use Amazon Quick apps securely while maintaining
data privacy and compliance.

### When using the Slack

extension

To start fresh, begin a new conversation by selecting **New
chat** in direct messages. Closing the side panel ends your
current conversation. You can access conversation history through
Slack message history or the Amazon Quick chat instance,
which includes conversations from all channels. You can view complete
conversation details, including attachment names, and access the same
knowledge base available in your Amazon Quick chat instance.

###### Note

Users can access conversation history in Slack.
Deleting the conversation in Slack will not delete from
conversation history in Amazon Quick. However, users need to visit the
Amazon Quick chat instance to manage their conversations.

### Conversation retention policy

and accuracy

Amazon Quick automatically deletes conversations after 30 days of
inactivity. Slack conversation retention follows your
company's specific history rules, and Slack retention periods
may exceed Amazon Quick's 30-day limit.

Users can access conversation history in Slack through the
AI App History tab. Deleting the conversation in Slack will
not delete from conversation history in Amazon Quick. However, users need to
visit the Amazon Quick chat instance to manage their conversations.

### Security

considerations

When you use Amazon Quick in public channels, remember that responses
reflect individual user permissions and content may include information not
accessible to all channel members. It may generate responses that contain
sensitive data that can't be publicly shared.

To protect your organization's data, carefully evaluate public channel
usage, consider the security implications, and plan deployment with data
privacy in mind. Amazon Quick maintains strict data privacy by not using
customer data for service improvements, not using customer data to enhance
language models, and not indexing Slack conversations into
your company's Amazon Quick instance.

## Slack

extension known limitations

The following are known limitations of the Amazon Quick Slack
extension:

- The Slack extension doesn't have access to all your
  Slack conversations. It only has access to the
  messages in Slack conversation threads where it is
  mentioned.
- The Slack extension doesn't have access to previous
  messages when mentioned in a Slack channel or in group
  message.
- The Slack extension isn't accessible in group direct
  messages or in direct messages with teammates unless it is explicitly
  added to the conversation as a member.
- You can filter Amazon Quick agents and spaces only in direct messages
  with the Slack extension. The Slack
  extension will use the default assistant and all spaces available to you
  when invoked in public such as in channels or group messages.
- The Slack extension can't render visuals for prompts
  about your structured data.
- Web search isn't supported in the Slack
  extension.
- The Slack extension can't be configured to
  automatically reply to messages in channels or posts.
- The Slack extension will not respond when invoked by
  Slack's workflow bot as it is not able to
  authenticate the user who made the query in these situations.
- The Slack extension isn't available in huddles.
- [Actions](../../../quicksuite/latest/userguide/action-connectors.md "../../../quicksuite/latest/userguide/action-connectors.md") (using your action
  integrations) can only be performed in direct messages with the
  Slack extension.
- Actions that require file uploads as inputs are not supported by the
  Slack extension.
- [Flows](../../../quicksuite/latest/userguide/flows.md "../../../quicksuite/latest/userguide/flows.md") are not supported in the
  Slack extension at this time.
- File upload limitations are the same within Amazon Quick chat. For
  more information, see [Upload files and chat](../../../quicksuite/latest/userguide/using-quick-chat.md#file-uploads "../../../quicksuite/latest/userguide/using-quick-chat.md#file-uploads").
