

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using the Amazon Q Business Microsoft Teams app
<a name="msteams-using"></a>

**Topics**
+ [Prerequisites](#msteams-using-prerequisites)
+ [Install and configure the Amazon Q Business app in Microsoft Teams](#msteams-using-install)
+ [Features of the Amazon Q Business Microsoft Teams bot](#msteams-using-features)
+ [Considerations using the Amazon Q Business bot for Microsoft Teams (Teams)](#msteams-considerations)
+ [Troubleshooting the Amazon Q Business app for Microsoft Teams](#msteams-troubleshooting)

## Prerequisites
<a name="msteams-using-prerequisites"></a>
+ You must have an Amazon Q Business user subscription.
+ You must have a Microsoft 365 Business subscription.
+ Your Amazon Q admin must connect the Amazon Q Business App to your Microsoft Teams organization.

## Install and configure the Amazon Q Business app in Microsoft Teams
<a name="msteams-using-install"></a>

The following are instructions on how to install the Amazon Q app in Microsoft Teams (Teams):

1. Open and login to the Teams organization for your company.

1. Go to **Apps** on the left navigation and search for *Amazon Q Business*

1. Choose **Amazon Q Business**

1. You will now see a **Q** icon/logo on the top bar on the right where you can access and chat with Amazon Q Business.

For more information, see [Chat with a bot in Microsoft Teams](https://support.microsoft.com/en-us/office/chat-with-a-bot-in-microsoft-teams-9c7bab5e-b1a2-4e35-801a-80d076e26f3f) from Microsoft support.

## Features of the Amazon Q Business Microsoft Teams bot
<a name="msteams-using-features"></a>

Following are some of the features supported by the Amazon Q Microsoft Teams (Teams) App:
+ In direct messages (DMs) to the Amazon Q contact, it responds to all messages and queries.
+ In channels it responds only to @mentions, and always in replies.
+ Thumbs up and down buttons to track feedback and help improve performance over time.
+ Provides Source Attribution - see references to sources used by Amazon Q Business.
+ It tracks the conversation and applies context.
+ Process up to 5 attached files for contextual question answering, summaries, etc. JPEG/JPG image file types are not supported as file uploads in the Teams integration.

**Important**  
The Amazon Q Business Microsoft Teams integration does not support [actions or plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/actions.html).

## Considerations using the Amazon Q Business bot for Microsoft Teams (Teams)
<a name="msteams-considerations"></a>

1. When Amazon Q is invoked by a user in a public Teams channel, it generates responses based on the invoking user's permissions, which may include content that other channel members aren't authorized to access. To prevent unintended exposure of sensitive information, carefully evaluate the use of Amazon Q in public channels. 

1. Amazon Q Business does not use customer data for service improvement or for improving its underlying large language models (LLMs). Also, none of the data you include in your Teams conversations will be indexed into your company's Amazon Q Business instance. For more information, see [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html).

1. The Amazon Q Business Teams app will have access to the same knowledge available in the corresponding Amazon Q Business web experience.

1. To reset, start new conversation, using the */new\_conversation* command.

1. When you upload a file, the Amazon Q bot for Teams will only be able to respond from the file (and general knowledge if your Amazon Q admin has enabled it). Start a new chat if you want to return to getting answers from company knowledge.

1. Closing the Amazon Q Business bot for Teams side panel will end the current conversation. Users can review past conversations in Teams or all conversations from all channels (Teams, browser extensions, etc.) in your Amazon Q Business web experience. You can access all the history of previous conversations including, the names of the attachments in those conversations.

1. All conversations in Amazon Q Business are deleted after 30 days of inactivity. Teams may store conversations for longer depending on your company's Teams conversation history rules.

1. Amazon Q may provide inaccurate responses at times. For more information, see [Hallucination](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/concepts-terms.html#hallucination) in the topic Key concepts of Amazon Q Business.

## Troubleshooting the Amazon Q Business app for Microsoft Teams
<a name="msteams-troubleshooting"></a>

My admin has enabled the Amazon Q Business app for Microsoft Teams (Teams), but I'm unable to login.  
Try having a conversation on your Amazon Q web experience first and then try Teams again. If this doesn't work, then contact your Amazon Q admin or IT department.

I am getting a "Can't access document" error.  
This happens when a document uses an unsupported format from which Amazon Q app is unable to pull relevant data to provide a helpful response. If you encounter this error and would like your file format to be supported, please submit feedback via the feedback button.

Amazon Q doesn't respond helpfully or doesn't use the context of the document I added.  
Try starting a new chat and adding the document again. If it still does not work, contact your Amazon Q Business admin for further support.