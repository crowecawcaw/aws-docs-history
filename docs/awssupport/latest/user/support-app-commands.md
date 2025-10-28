# AWS Support App in Slack commands

## Slack channel

commands

You can enter the following commands in the Slack channel where you invited the
AWS Support App. This Slack channel name also appears as a configured channel in the
AWS Support Center Console.

`/awssupport create` or `/awssupport create-case`

Create a support case.

`/awssupport search` or `/awssupport search-case`

Search for cases. You can search for support cases for the AWS accounts
that configured the AWS Support App for the same Slack channel.

`/awssupport quota` or `/awssupport
 service-quota-increase`

Request a service quota increase.

## Live chat channel commands

You can enter the following commands in the live chat channel.
This is the channel that the AWS Support App creates for you if you choose a new channel
for your chat with Support. Chat channels include your support case ID, such as
`awscase-1234567890`.

###### Note

The following commands are not available when using a thread in the current channel for a live chat.
Instead, use the buttons attached to the initial thread message to end a chat,
invite a new agent, or resolve the case.

`/awssupport endchat`

Remove the support agent and end the live chat session.

`/awssupport invite`

Invite a new support agent to this channel.

`/awssupport resolve`

Resolve this support case.
