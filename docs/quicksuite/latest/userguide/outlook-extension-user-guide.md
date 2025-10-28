# Amazon Quick Suite Microsoft

Outlook extension user guide

As a user, you can access Amazon Quick Suite directly within Microsoft
Outlook to get AI-powered assistance without leaving your email
environment. The extension integrates seamlessly into your Microsoft
Outlook workflow, providing instant access to knowledge bases and
intelligent responses.

###### Topics

- [Add a Microsoft
  Outlook Extension to your Microsoft
  Outlook](#outlook-extension-setup-users "#outlook-extension-setup-users")
- [Access Quick Suite in your
  Microsoft Outlook navigation pane at any time](#access-outlook-side-panel "#access-outlook-side-panel")
- [Microsoft Outlook extension use
  cases](#outlook-use-cases "#outlook-use-cases")
- [Amazon Quick Suite Microsoft
  Outlook extension usage guidelines](#outlook-usage-guidelines "#outlook-usage-guidelines")
- [Microsoft
  Outlook extension known limitations](#outlook-extension-known-limitations "#outlook-extension-known-limitations")

## Add a Microsoft

Outlook Extension to your Microsoft
Outlook

Install the Quick Suite app in your Microsoft Outlook
environment to enable AI-powered assistance. This one-time setup makes
Quick Suite accessible throughout your Microsoft Outlook
workflow.

###### Add a Microsoft Outlook extension to your Microsoft

Outlook

1. Open your Microsoft Outlook.
2. Go to **Add-Ins** and search for
   **Quick Suite** and choose **Quick Suite**.
3. You will now see the Amazon Quick Suite logo on the top bar on the right
   where you can access the chat assistant.
4. Once the add-in is installed, you can use your Quick Suite
   **Add-In**.

## Access Quick Suite in your

Microsoft Outlook navigation pane at any time

Once you've added Quick Suite to your Microsoft Outlook
environment, you can access it conveniently through the navigation pane for
quick assistance without interrupting your email workflow. The navigation pane
provides persistent access to Quick Suite while you work with emails and
conversations.

## Microsoft Outlook extension use

cases

With Quick Suite integrated into Microsoft Outlook, you
can search and access your organization's knowledge bases directly from your
email conversations. This allows you to find relevant information, get answers
to questions, and enhance your communications without leaving Microsoft
Outlook.

###### Get summaries and action items from lengthy email threads

1. Locate the Quick Suite icon under **add-ins**
   in your Microsoft ribbon and select the
   **summarize** shortcut.
2. Alternatively, open the Quick Suite side panel and ask any
   question of your choice about the email thread in focus.

###### Draft speedy replies to emails

1. Navigate to an email thread of your choice and locate the
   Quick Suite icon under **add-ins** in your
   Microsoft ribbon. Select the
   **reply** or **reply all**
   shortcut.
2. Quick Suite will create a draft response and open a reply window
   that is ready to send.
3. Iterate on the draft with Quick Suite and click send.

###### Incorporate Quick Suite's company knowledge and general knowledge

into your emails

1. Open an email thread of your choice and ask Quick Suite about
   its knowledge.
2. Use the **insert text** or **replace
   selection** buttons to insert Quick Suite's response
   into your email drafts.

###### \*\*Perform actions in external

applications\*\*

1. Start a direct message (DM) with Quick Suite.
2. Ask it to perform an action of your choice in an external application
   using [action connectors](action-connectors.md "action-connectors.md") configured by your
   organization.

## Amazon Quick Suite Microsoft

Outlook extension usage guidelines

As a user, you are responsible for keeping company information safe. The
following guidance helps you use Amazon Quick Suite apps securely while maintaining
data privacy and compliance.

### Conversation retention

policy and accuracy

Amazon Quick Suite automatically deletes conversations after 30 days of
inactivity. Microsoft Outlook conversation retention follows
your company's specific history rules, and Microsoft Outlook
retention periods may exceed Amazon Quick Suite's 30-day limit.

Users can review past conversations and attachments. Closing the
Quick Suite chat panel ends the current conversation. Reopen the panel
to start a new conversation. However, users need to visit the Amazon Quick Suite
chat instance to manage their conversations.

### Security

considerations

When you use Amazon Quick Suite with email content, remember that responses
reflect individual user permissions and content may include information not
accessible to all email recipients. It may generate responses that contain
sensitive data that can't be publicly shared.

To protect your organization's data, carefully evaluate email usage and
plan deployment with data privacy in mind. Amazon Quick Suite maintains strict
data privacy by not using customer data for service improvements, not using
customer data to enhance language models, and not indexing Microsoft
Outlook conversations into your company's Amazon Quick Suite
instance.

## Microsoft

Outlook extension known limitations

The following are known limitations of the Amazon Quick Suite Microsoft
Outlook extension:

- The Microsoft Outlook extension doesn't support
  Amazon Quick Suite accounts that use IAM Identity Center for authentication
  at this time.
- The Microsoft Outlook extension is only able to access
  your current selected email (which can include your email thread). It is
  unable to answer questions across all emails/calendar events in your
  inbox. To enable access to your entire inbox and calendar, configure the
  Microsoft Outlook
  [actions integration](creating-action-connectors-admin-console.md "creating-action-connectors-admin-console.md").
- The Microsoft Outlook extension can't generate visuals
  from structured data.
- Web search isn't supported in the Microsoft Outlook
  extension at this time.
- You cannot review your conversation history in Microsoft
  Outlook at this time. To review and manage your conversation
  history, use the Amazon Quick Suite chat instance.
- The Microsoft Outlook extension doesn't support [flows](flows.md "flows.md").
- The Microsoft Outlook extension supports up to 19
  uploaded files and your current email thread. For more information on
  file upload support, see [Upload files and chat](using-quick-chat.md#file-uploads "using-quick-chat.md#file-uploads").
- The Microsoft Outlook extension doesn't support
  filtering during chat based on **Recently used**
  agents. Users will have access to the full list of available agents and
  can pick agents they want to use.
- The Microsoft Outlook extension doesn't support the
  **Actions** menu, so you can't invoke actions
  explicitly. However, implicit actions are supported. For more
  information about explicit and implicit actions, see [Using Actions in Chat](int-actions-execution.md "int-actions-execution.md").
