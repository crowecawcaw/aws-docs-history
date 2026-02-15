# Chatting with Amazon Q Developer about AWS

###### Introducing generative AI-based Q artifacts

Amazon Q can now provide answers to questions with table and chart visualizations. A prompt library makes it
easier to find example prompts. The Q experience is now more usable and useful. The Q icon has been relocated to the
navigation bar. The Q chat panel now opens on the left side.

Chat with Amazon Q in the AWS Management Console, AWS Console Mobile Application, AWS website, AWS Documentation website, and
chat applications to learn about AWS services.

You can ask Amazon Q about best practices, recommendations, step-by-step instructions
for AWS tasks, and architecting your AWS resources and workflows. You can also ask
about your AWS resources and account costs. Amazon Q additionally generates short
scripts or code snippets to help you get started using the AWS SDKs and AWS CLI.

The following topics describe how to use Amazon Q chat and topics you can chat about.

###### Topics

- [Using Q artifacts in Amazon Q](chat-artifacts.md "chat-artifacts.md")
- [Add permissions](#add-permissions-chat "#add-permissions-chat")
- [Start a conversation](#start-conversation "#start-conversation")
- [Manage conversations in the console](#manage-conversations-console "#manage-conversations-console")
- [Navigate the Amazon Q chat panel](#navigate-amazon-q-chat-panel "#navigate-amazon-q-chat-panel")
- [Chat settings](#chat-settings "#chat-settings")
- [Example prompts](#example-questions "#example-questions")
- [Chatting about your resources with Amazon Q Developer](chat-actions.md "chat-actions.md")
- [Asking Amazon Q to troubleshoot your
  resources](chat-actions-troubleshooting.md "chat-actions-troubleshooting.md")
- [Chatting about your costs](chat-costs.md "chat-costs.md")
- [Chatting about your network security](chat-network-security.md "chat-network-security.md")
- [Chatting about email sending](chat-email.md "chat-email.md")
- [Chatting about your telemetry and operations](chat-ops.md "chat-ops.md")

## Add permissions

For an IAM policy that grants permissions needed for chatting with Amazon Q, see
[Allow users to chat with
Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").

## Start a conversation

To open up the Amazon Q chat panel in the AWS Management Console, choose the Amazon Q icon in the top left in the Unified
Navigation bar. To open up the panel on the AWS website or any AWS service’s documentation page,
choose the Amazon Q icon in the bottom right corner.

To ask Amazon Q a question, enter your question into the text bar in the Amazon Q
panel. Amazon Q generates a response to your question with a sources section that
links to its references.

After you receive a response, you can optionally leave feedback by using the
thumbs-up and thumbs-down icons. You can also copy the response to your clipboard by
choosing the copy icon.

###### To start a new conversation in the console:

1. You can start a new conversation by choosing the plus icon in the top right corner of the chat panel.
2. To name or rename a conversation, choose the text at the top of the chat panel and enter your conversation name.

## Manage conversations in the console

You can view, switch to, and delete your past conversations in Amazon Q.

Amazon Q maintains the history of previously asked questions and responses within a
given conversation to use as context to inform responses. You can save up to 1,000
separate conversations with Amazon Q chat in the AWS console.

When you start a conversation, it’s automatically saved as a new conversation. You
can title the conversation, or Amazon Q will generate a title based on the example prompt you
select or the first few questions in the conversation.

You can switch between conversations to continue chatting with Amazon Q about
previous topics. Inactive conversations, in which you don’t ask a
new question, will be deleted after 90 days of inactivity. Messages older than 90 days will be
deleted, even if a conversation is still active.

###### To switch conversations:

1. Choose the clock icon on the top right of the chat panel. The **Conversations** pop-up opens.
2. Choose the name of the conversation you want to resume. All previous messages from that conversation appear
   in the chat panel where you can continue chatting with Amazon Q.

###### To delete conversations:

1. Choose the clock icon on the top right of the chat panel. The **Conversations** pop-up opens.
2. Choose the delete icon next to the name of the conversation you want to
   delete.

If you’re using Amazon Q in the console, your current conversation and
associated context are maintained when you navigate to another place in the
console or to another browser or tab. If you’re using Amazon Q on the AWS
website, Documentation website, or Console Mobile Application, a new conversation starts without any
context when you navigate to a new page, browser, or tab.

## Navigate the Amazon Q chat panel

Note: You can switch between the Amazon Q chat panel and service consoles at any time:

1. To expand the Q chat panel in full-screen mode, choose the maximize icon in the top-right corner. To toggle full-screen mode, choose the resize icon.
2. To close the Q chat panel, choose < in the top-right corner. To close the panel with visualizations, choose X in the top-right corner.
3. To adjust the chat panel size, use the divider.
4. To reopen the chat panel, choose the Q icon in the Unified Navigation bar.
5. Your work is automatically saved when switching between views.

## Chat settings

To view your chat settings in Amazon Q, choose the gear icon in the top
right of the chat panel.

- **Region** — Amazon Q defaults to the
  AWS Region set in the AWS Management Console when you open the chat panel. To
  update the Region used by Amazon Q, change your console Region.

## Example prompts

You can ask Amazon Q questions about AWS and AWS services, such as finding the
right service, understanding best practices or reviewing the state of your resources.
If Amazon Q determines a visual interface would be helpful, it automatically displays
a new panel with either a table or chart visualization.

You can also ask about software development with the AWS SDKs and AWS CLI. Amazon Q
in the console can generate short scripts or code snippets to help you get started
using the AWS SDKs and AWS CLI.

The following are example questions that demonstrate how Amazon Q can help you build
on AWS:

- List RDS databases without CloudWatch alarms
- What's the maximum runtime for a Lambda function?
- When should I put my resources in a VPC?
- List S3 buckets with tag value `<tag value>`
- Create a chart showing my cost per GB for different S3 storage classes
- Graph EC2 cost per vCPU hour over the last 3 weeks
- What's the best container service to use to run my workload if I need to
  keep my costs low?
- Show me a bar chart of potential savings by optimization recommendation

To help you get started, Q recommends prompts when you start a new conversation. You can also view the list of supported prompts in the prompt library.
To view prompts in the prompt library, choose the book icon in the top right of the chat panel.
