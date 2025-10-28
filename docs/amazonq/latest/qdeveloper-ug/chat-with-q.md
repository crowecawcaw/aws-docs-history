# Chatting with Amazon Q Developer about AWS

Chat with Amazon Q in the AWS Management Console, AWS Console Mobile Application, AWS website, AWS Documentation website, and
chat applications to learn about AWS services.

You can ask Amazon Q about best practices, recommendations, step-by-step instructions
for AWS tasks, and architecting your AWS resources and workflows. You can also ask
about your AWS resources and account costs. Amazon Q additionally generates short
scripts or code snippets to help you get started using the AWS SDKs and AWS CLI.

The following topics describe how to use Amazon Q chat and topics you can chat about.

###### Topics

- [Add permissions](#add-permissions-chat "#add-permissions-chat")
- [Start a conversation](#start-conversation "#start-conversation")
- [Manage conversations in the console](#manage-conversations-console "#manage-conversations-console")
- [Set chat settings](#chat-settings "#chat-settings")
- [Example questions](#example-questions "#example-questions")
- [Chatting about your resources with Amazon Q Developer](chat-actions.md "chat-actions.md")
- [Asking Amazon Q to troubleshoot your
  resources](chat-actions-troubleshooting.md "chat-actions-troubleshooting.md")
- [Chatting about your costs](chat-costs.md "chat-costs.md")
- [Chatting about your network security](chat-network-security.md "chat-network-security.md")
- [Chatting about your telemetry and operations](chat-ops.md "chat-ops.md")

## Add permissions

For an IAM policy that grants permissions needed for chatting with Amazon Q, see
[Allow users to chat with
Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").

## Start a conversation

To open up the Amazon Q chat panel in the AWS Management Console, choose the Amazon Q icon in the right
sidebar. To open up the panel on the AWS website or any AWS service’s documentation page,
choose the Amazon Q icon in the bottom right corner.

To ask Amazon Q a question, enter your question into the text bar in the Amazon Q
panel. Amazon Q generates a response to your question with a sources section that
links to its references.

After you receive a response, you can optionally leave feedback by using the
thumbs-up and thumbs-down icons. You can also copy the response to your clipboard by
choosing the copy icon.

###### To start a new conversation in the console:

1. From the welcome screen, choose **New conversation** at the bottom of the chat
   panel.
2. From an active conversation, you can start a new conversation by choosing the plus icon in the top right corner of the chat panel. From the welcome screen, choose **New conversation** at the bottom of the chat
   panel.
3. To name or rename a conversation, choose the text at the top of the chat panel and enter your conversation name.

## Manage conversations in the console

Amazon Q maintains the history of previously asked questions and responses within a
given conversation to use as context to inform responses. You can save up to 1,000
separate conversations with Amazon Q chat in the AWS console.

When you start a conversation, it’s automatically saved as a new conversation. You
can title the conversation, or Amazon Q will generate a title based on the first few
questions in the conversation.

You can switch between conversations to continue chatting with Amazon Q about
previous topics you’ve asked about. Inactive conversations, in which you don’t ask a
new question, will be deleted after 90 days. Messages older than 90 days will be
deleted, even if a conversation is still active.

###### To switch conversations:

1. Choose the menu icon on the top left of the chat panel. The **Conversations** page opens in the chat panel.
2. Choose the name of the conversation you want to resume. You are redirected
   to the chat panel where you can continue chatting with Amazon Q.

###### To delete conversations:

1. Choose the menu icon on the top left of the chat panel. The **Conversations** page opens in the chat panel.
2. Choose the delete icon next to the name of the conversation you want to
   delete. Confirm you want to delete the conversation by choosing **Delete** on
   the pop-up that appears.

If you’re using Amazon Q in the console, your current conversation and
associated context are maintained when you navigate to another place in the
console or to another browser or tab. If you’re using Amazon Q on the AWS
website, Documentation website, or Console Mobile Application, a new conversation starts without any
context when you navigate to a new page, browser, or tab.

## Set chat settings

To update your chat settings in Amazon Q, choose the gear icon in the top
right corner of the chat panel.

You can specify the following settings:

- **Region** — Amazon Q defaults to the
  AWS Region set in the AWS Management Console when you open the chat panel. To
  update the Region used by Amazon Q, change your console Region.

## Example questions

You can ask Amazon Q questions about AWS and AWS services, such as finding the
right service or understanding best practices.

You can also ask about software development with the AWS SDKs and AWS CLI. Amazon Q
in the console can generate short scripts or code snippets to help you get started
using the AWS SDKs and AWS CLI.

The following are example questions that demonstrate how Amazon Q can help you build
on AWS:

- What's the maximum runtime for a Lambda function?
- When should I put my resources in a VPC?
- What's the best container service to use to run my workload if I need to
  keep my costs low?
- How do I list my Amazon S3 buckets?
- How do I create and host a website on AWS?
