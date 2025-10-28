# Using Amazon Q CLI in CloudShell

###### Important

AWS CloudShell has temporarily disabled Amazon Q chat functionality due to an internal issue.
We're actively investigating and will restore this functionality as soon as possible. In the
meantime, you can continue using Q chat in the AWS Management Console.

The Amazon Q CLI is a command-line interface that allows you to interact with Amazon Q. For
more information, see [Using Amazon
Q Developer on the command line](../../../amazonq/latest/qdeveloper-ug/command-line.md "../../../amazonq/latest/qdeveloper-ug/command-line.md") in the _Amazon Q Developer User
Guide_.

Amazon Q CLI in CloudShell allows you to interact in natural language conversations, ask
questions, and receive responses from Amazon Q all from your terminal. You can get the related
shell command that reduces the need to search for, remember syntax, and receive command
suggestions as you type in the terminal.

###### Note

Currently, Amazon Q CLI features in CloudShell are not available in your CloudShell
VPC environment.

If you don’t see Amazon Q CLI features in CloudShell, contact your administrator to provide
you IAM permissions. For more information, see [Identity-based policy examples for Amazon Q Developer](../../../en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.md "../../../en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.md") in the _Amazon Q Developer User Guide_.

This chapter explains how you can use Amazon Q CLI features in CloudShell.

## Using Amazon Q inline suggestions in

CloudShell

The Amazon Q inline suggestions in CloudShell provide you with command suggestions as you
type in the terminal. For more information, see [Amazon Q inline on the command line](../../../amazonq/latest/qdeveloper-ug/command-line-inline.md "../../../amazonq/latest/qdeveloper-ug/command-line-inline.md") in the _Amazon Q
Developer User Guide_.

**To use Amazon Q inline suggestions in
CloudShell**

1. From the AWS Management Console, Choose **CloudShell**.
2. On the CloudShell terminal, switch to Z shell, and start typing. To switch to Z
   shell, type `zsh` in the terminal, and then press
   **Enter**.

###### Note

Currently, Amazon Q inline is only supported in Z shell.

When you start typing your command, Amazon Q will make suggestions based on your
current input and previous commands. Inline suggestions are automatically enabled.

To disable the inline suggestions, run the following command:

`q inline disable`

To enable the inline suggestions, run the following command:

`q inline enable`

## Using Q chat command in CloudShell

The `q chat` command allows you to ask questions and receive responses from
Amazon Q all from your terminal. To initiate a conversation with Amazon Q, run `q
 chat` command in the CloudShell terminal. For more information, see [Chatting with Amazon Q in the CLI](../../../en_us/amazonq/latest/qdeveloper-ug/command-line-chat.md "../../../en_us/amazonq/latest/qdeveloper-ug/command-line-chat.md") in the _Amazon Q Developer
User Guide_.

## Using Q translate command in

CloudShell

The `q translate` command allows you to write natural language instruction. To
translate with Amazon Q, run `q translate` command in the CloudShell terminal.
For more information, see [Translating from natural language to bash](../../../en_us/amazonq/latest/qdeveloper-ug/command-line-conversation.md "../../../en_us/amazonq/latest/qdeveloper-ug/command-line-conversation.md") in the _Amazon Q
Developer User Guide_.

## CLI command completion in CloudShell

CLI completion in CloudShell provides suggestions for commands and options as you type
in the terminal. For more information, see [Generating command line completion](../../../amazonq/latest/qdeveloper-ug/command-line-autocomplete.md "../../../amazonq/latest/qdeveloper-ug/command-line-autocomplete.md") in _Amazon Q Developer
User Guide_.

## Enable or disable Amazon Q CLI

You can enable or disable Amazon Q CLI by choosing **Preferences**,
**Enable Amazon Q CLI** and **Disable Amazon Q CLI**. Amazon Q
CLI allows you to interact with natural language instructions, ask questions, and get answers
from Amazon Q all from your terminal. It also provide you with command suggestions as you type
in the terminal. As you start typing in the terminal, Amazon Q suggests relevant options to
complete your command.

## Identity-based policy for Amazon Q CLI in

CloudShell

To use Amazon Q CLI in CloudShell, make sure you have the required IAM permissions.
For more information, see [Identity-based policy examples for Amazon Q Developer](../../../en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.md "../../../en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.md") in the _Amazon Q Developer User Guide_.
