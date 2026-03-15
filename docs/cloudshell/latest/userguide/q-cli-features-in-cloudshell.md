# Using Kiro CLI in CloudShell

The Kiro CLI is a command-line interface that allows you to interact with Kiro. For
more information, see [Core Features of Kiro CLI](https://kiro.dev/docs/cli/#core-features "https://kiro.dev/docs/cli/#core-features") in the _Kiro User
Guide_.

Kiro CLI in CloudShell allows you to interact in natural language conversations, ask
questions, and receive responses from Kiro all from your terminal. You can get the related
shell command that reduces the need to search for, remember syntax, and receive command
suggestions as you type in the terminal.

If you don't see Kiro CLI features in CloudShell, contact your administrator to provide
you IAM permissions. For more information, see [Identity-based policy examples for Kiro Developer](https://kiro.dev/docs/cli/privacy-and-security/iam-permissions/ "https://kiro.dev/docs/cli/privacy-and-security/iam-permissions/") in the _Kiro User Guide_.

This chapter explains how you can use Kiro CLI features in CloudShell.

Some Kiro CLI features require authentication. For more information, see [Authentication](https://kiro.dev/docs/cli/authentication/ "https://kiro.dev/docs/cli/authentication/") in the _Kiro User
Guide_.

## Using Kiro chat command in CloudShell

The `kiro-cli` command allows you to ask questions and receive responses from
Kiro all from your terminal. To initiate a conversation with Kiro, run `kiro-cli`
command in the CloudShell terminal. For more information, see [Chatting with Kiro in the CLI](https://kiro.dev/docs/cli/chat/ "https://kiro.dev/docs/cli/chat/") in the _Kiro
User Guide_.

## Using Kiro translate command in CloudShell

The `kiro-cli translate` command allows you to write natural language instruction. To
translate with Kiro, run `kiro-cli translate` command in the CloudShell terminal.
For more information, see [Translating from natural language to bash](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-translate "https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-translate") in the _Kiro
User Guide_.

## CLI command completion in CloudShell

CLI completion in CloudShell provides suggestions for commands and options as you type
in the terminal. For more information, see [Generating command line completion](https://kiro.dev/docs/cli/autocomplete/ "https://kiro.dev/docs/cli/autocomplete/") in _Kiro
User Guide_.

## Using Kiro inline suggestions in CloudShell

The Kiro inline suggestions in CloudShell provide you with command suggestions as you
type in the terminal. For more information, see [Kiro inline on the command line](https://kiro.dev/docs/cli/autocomplete/#inline-suggestions "https://kiro.dev/docs/cli/autocomplete/#inline-suggestions") in the _Kiro
User Guide_.

**To use Kiro inline suggestions in
CloudShell**

1. From the AWS Management Console, Choose **CloudShell**.
2. On the CloudShell terminal, switch to Z shell, and start typing. To switch to Z
   shell, type `zsh` in the terminal, and then press
   **Enter**.

###### Note

Currently, Kiro inline is only supported in Z shell.

When you start typing your command, Kiro will make suggestions based on your
current input and previous commands. Inline suggestions are automatically enabled.

To disable the inline suggestions, run the following command:

`kiro-cli inline disable`

To enable the inline suggestions, run the following command:

`kiro-cli inline enable`

## Identity-based policy for Kiro CLI in CloudShell

To use Kiro CLI in CloudShell, make sure you have the required IAM permissions.
For more information, see [Identity-based policy examples for Kiro Developer](https://kiro.dev/docs/cli/privacy-and-security/iam-permissions/ "https://kiro.dev/docs/cli/privacy-and-security/iam-permissions/") in the _Kiro User Guide_.
