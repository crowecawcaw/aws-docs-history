# Using the Amazon Q Business Slack App

The Amazon Q Business Slack app is available to all Amazon Q Business users.

###### Topics

- [Prerequisites](#slack-using-prerequisites "#slack-using-prerequisites")
- [Install and configure the Amazon Q Business App in Slack](#slack-using-install "#slack-using-install")
- [Features of the Amazon Q Business Slack App](#slack-using-features "#slack-using-features")
- [Considerations for using the Amazon Q Business App for Slack](#slack-considerations "#slack-considerations")
- [Troubleshooting the Amazon Q Business App for Slack](#slack-troubleshooting "#slack-troubleshooting")

## Prerequisites

- Your Amazon Q admin must connect the Amazon Q Business Slack app to your Slack
  workspace.

## Install and configure the Amazon Q Business App in Slack

The following are instructions on how to install the Amazon Q Business App in
Slack:

1. Open and login to the Slack workspace for your company.
2. Choose **More** in the left navigation, then select
   **Automations**.
3. Choose **Apps**.
4. Choose **+ Add apps**
5. Search for "Amazon Q Business" and choose
   **Amazon Q Business**
6. This will take you to the **About** page. Choose the
   3 vertical dots (that say "more actions") to the right of the New Chat
   button.
7. Choose **add assistant to top bar**
8. You will now see a **Q** icon/logo on the top bar on
   the right where you can **access and chat with
   Amazon Q Business**

For more information, see [Understand AI apps in Slack](https://slack.com/help/articles/33076000248851-Understand-AI-apps-in-Slack#find-apps "https://slack.com/help/articles/33076000248851-Understand-AI-apps-in-Slack#find-apps") in the Slack help center.

## Features of the Amazon Q Business Slack App

Following are some of the features supported by the Amazon Q Slack App:

- In direct messages (DMs) to the Amazon Q Business contact, it responds to all
  messages and queries.
- In channels it responds only to @mentions, and always replies in
  thread.
- Thumbs up and down buttons to track feedback and help improve
  performance over time.
- Provides Source Attribution - see references to sources used by
  Amazon Q Business.
- It tracks the conversation and applies context.
- Process up to 5 attached files for contextual question answering,
  summaries, etc.

###### Important

The Amazon Q Business Slack integration does not support [actions or plugins](actions.md "actions.md").

## Considerations for using the Amazon Q Business App for Slack

1. When Amazon Q is invoked by a user in a public Slack channel, it
   generates responses based on the invoking user's permissions, which may
   include content that other channel members aren't authorized to access.
   To prevent unintended exposure of sensitive information, carefully
   evaluate the use of Amazon Q in public channels.
2. Amazon Q Business does not use customer data for service improvement or for
   improving its underlying large language models (LLMs). Also, none of the
   data you include in your browser extension conversations will be indexed
   into your company's Amazon Q Business instance. For more information, see
   [Amazon Q Business Service improvement](service-improvement.md "service-improvement.md").
3. The Amazon Q Business Slack app will have access to the same knowledge
   available in the corresponding Amazon Q Business web experience.
4. To reset, start new conversation, direct message as a _New
   chat_.
5. When you upload a file, the Amazon Q Slack app will only be able to
   respond from the file (and general knowledge if your Amazon Q admin has
   enabled it). Start a new chat if you want to return to getting answers
   from company knowledge.
6. Closing the Amazon Q Business Slack app side panel will end the current
   conversation. Users can review past conversations in Slack or all
   conversations from all channels (Slack, browser extensions, etc.) in
   your Amazon Q Business web experience. You can access all the history of
   previous conversations including, the names of the attachments in those
   conversations.
7. All conversations in Amazon Q Business are deleted after 30 days of
   inactivity. Slack may store conversations for longer depending on your
   company's Slack conversation history rules.
8. Amazon Q may provide inaccurate responses at times. For more
   information, see [Hallucination](concepts-terms.md#hallucination "concepts-terms.md#hallucination") in the topic Key concepts of
   Amazon Q Business.

## Troubleshooting the Amazon Q Business App for Slack

My admin has enabled the Amazon Q Business app for Slack, but I'm unable to
login.

Try having a conversation on your Amazon Q web experience first and
then try Slack again. If this doesn't work, then contact your Amazon Q
admin or IT department.

I am getting a "Can't access document" error.

This happens when a document uses an unsupported format from which
Amazon Q app is unable to pull relevant data to provide a helpful
response. If you encounter this error and would like your file
format to be supported, please submit feedback via the feedback
button in the browser extension.

Amazon Q doesn't respond helpfully or doesn't use the context of the
document I added.

Try starting a new chat and adding the document again. If it still
does not work, contact your Amazon Q Business admin for further
support.
