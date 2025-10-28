# Amazon Quick Suite Microsoft

Teams extension user guide

As a user, you can access Quick Suite directly within Microsoft
Teams to get AI-powered assistance without leaving your workspace. The
extension integrates seamlessly into your Microsoft Teams
environment, providing instant access to knowledge bases and intelligent
responses.

###### Topics

- [Add a Microsoft Teams
  Extension to your Microsoft Teams](#teams-extension-add-setup "#teams-extension-add-setup")
- [Microsoft Teams extension use
  cases](#teams-use-cases "#teams-use-cases")
- [Amazon Quick Suite Microsoft
  Teams extension usage guidelines](#teams-users-guidelines "#teams-users-guidelines")
- [Microsoft
  Teams extension known limitations](#teams-extension-known-limitations "#teams-extension-known-limitations")

## Add a Microsoft Teams

Extension to your Microsoft Teams

Install the Quick Suite app in your Microsoft Teams
workspace to enable AI-powered assistance. This one-time setup makes
Quick Suite accessible throughout your Microsoft Teams
environment.

###### Add a Microsoft Teams Extension to your Microsoft

Teams

1. Open and login to the Microsoft Teams workspace for
   your company.
2. Choose **Apps** in the left navigation and search for
   **Quick Suite**.
3. Choose **Quick Suite**.
4. On the top bar, Quick Suite icon is now available. You can
   select it to access and chat with Quick Suite.

###### Note

For more information, see [Chat with a bot in Microsoft Teams](https://support.microsoft.com/en-us/office/chat-with-a-bot-in-microsoft-teams-a94e8b26-9ee9-42a3-aa05-955974c6aa42 "https://support.microsoft.com/en-us/office/chat-with-a-bot-in-microsoft-teams-a94e8b26-9ee9-42a3-aa05-955974c6aa42") from
Microsoft support.

## Microsoft Teams extension use

cases

With Amazon Quick Suite integrated into Microsoft Teams, you can
search and access your organization's knowledge bases directly from your
conversations. This allows you to find relevant information, get answers to
questions, and enhance your communications without leaving
Team.

###### Search your organization’s knowledge without leaving

Teams

1. Start a chat with Quick Suite after adding it from the
   **Apps** section.
2. Ask Quick Suite a question about its knowledge from your spaces
   and connected knowledge bases.
3. To personalize your conversation using your data, use the gear icon
   (visible after sending your first message to Quick Suite) within
   your conversation to select an agent or a space to respond from.

###### Get Quick Suite’s in-context help in Teams posts

1. Navigate to a Teams post of your choice.
2. Type **@Amazon Quick Suite** and ask any question about the
   messages in that thread or its knowledge from your spaces and your
   organization's knowledge bases.
3. If Quick Suite is not already added to the channel, you will be
   prompted to add it before receiving a response.

###### \*\*Perform actions in external

applications\*\*

1. Start a direct message (DM) with Quick Suite.
2. Ask it to perform an action of your choice in an external application
   using [action connectors](action-connectors.md "action-connectors.md") configured by your
   organization.

## Amazon Quick Suite Microsoft

Teams extension usage guidelines

As a user, you are responsible for keeping company information safe. The
following guidance helps you use Amazon Quick Suite apps securely while maintaining
data privacy and compliance.

### Conversation retention policy

and accuracy

Amazon Quick Suite automatically deletes conversations after 30 days of
inactivity. Teams conversation retention follows your company's specific
history rules. Teams retention periods may exceed Amazon Quick Suite's 30-day
limit. To start fresh, begin a new conversation by using the
`/new_conv` command

Users can review past conversations in Teams or all
conversations from all channels (Teams, browser extensions,
etc.) in your Amazon Quick Suite chat instance.

###### Note

Deleting conversations or messages in Teams does not
remove them from Amazon Quick Suite. To manage your conversation history, use
the Amazon Quick Suite chat instance.

### Security

considerations

When Amazon Quick Suite is invoked by a user in a public Teams
channel, it generates responses based on the invoking user's permissions,
which may include content that other channel members aren't authorized to
access. To prevent unintended exposure of sensitive information, carefully
evaluate the use of Amazon Quick Suite in public channels.

**File upload behavior in Amazon Quick Suite Teams
Extension:**

- Responses will be limited to the uploaded file content.
- General knowledge access depends on admin settings.
- Start a new chat to access company knowledge again.

### Data privacy and conversation

behavior

Amazon Quick Suite does not use customer data for service improvement or for
improving its underlying large language models (LLMs). Also, none of the
data you include in your Teams conversations will be indexed
into your company's Amazon Quick Suite instance.

The Amazon Quick Suite Teams app will have access to the same
knowledge available in the corresponding Amazon Quick Suite web experience.

Closing the Amazon Quick Suite bot for Teams side panel will end
the current conversation. Users can review past conversations in
Teams or all conversations from all channels
(Teams, browser extensions, etc.) in your Amazon Quick Suite
web experience. You can access all the history of previous conversations
including, the names of the attachments in those conversations.

## Microsoft

Teams extension known limitations

The following are known limitations of the Amazon Quick Suite Microsoft
Teams extension:

- The Microsoft Teams extension isn't supported for
  Amazon Quick Suite accounts that use IAM Identity Center for
  authentication.
- The Microsoft Teams extension doesn't have access to
  all your Microsoft Teams conversations. It only has
  access to the messages in Microsoft Teams posts where it
  is mentioned.
- The Microsoft Teams extension isn't accessible in group
  direct messages or in direct messages with other teammates.
- You can filter Amazon Quick Suite agents and spaces only in direct messages
  with the Microsoft Teams extension. The Microsoft
  Teams extension will use the default assistant and all
  spaces available to you when invoked in public, such as in channels and
  Microsoft Teams posts.
- The Microsoft Teams extension can't render visuals for
  prompts about your structured data.
- Web search is not supported in the Microsoft Teams
  extension.
- The Microsoft Teams extension can't be configured to
  automatically reply to messages in channels or posts.
- The Microsoft Teams extension isn't available for your
  Microsoft Teams meetings.
- You cannot review your conversation history in Microsoft
  Teams. To review and manage your conversation history, go to
  your Amazon Quick Suite chat instance.
- [Actions](action-connectors.md "action-connectors.md") (using your action
  integrations) can only be performed in direct messages with the
  Microsoft Teams extension.
- Actions that require file uploads as inputs are not supported by the
  Microsoft Teams extension at this time.
- [Flows](flows.md "flows.md") are not supported in the
  Microsoft Teams extension at this time.
- File upload limitations are the same as those in the web experience.
  For more information see [Upload files and chat](using-quick-chat.md#file-uploads "using-quick-chat.md#file-uploads").
