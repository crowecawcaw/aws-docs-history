AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Getting help from Amazon Q Developer in chat applications

You can ask Amazon Q Developer in chat applications for help by entering `@Amazon Q help`. You can choose any of the following buttons to receive additional information about their respective topics.

###### Topics

- [Home (🏠)](#home "#home")
- [Commands](#cmnds "#cmnds")
- [Aliases](#com-aliases "#com-aliases")
- [Built-ins](#built-ins "#built-ins")
- [Q&A](#questansw "#questansw")
- [More help](#more-help "#more-help")

## Home (🏠)

Choosing the home icon (🏠) returns you to the main menu.

## Commands

Provides helpful tips about CLI command syntax and parameters.

For example, you don't have to remember parameters to use CLI commands with Amazon Q Developer in chat applications.
Amazon Q Developer in chat applications prompts you for all required prameters for a CLI command. Commands with one parameter don't require a parameter flag and unique AWS service operations don't require
you to enter a service name. For more information, see [Running AWS CLI commands from chat channels using Amazon Q Developer in chat applications](chatbot-cli-commands.md "chatbot-cli-commands.md").

## Aliases

Provides helpful tips about command aliases. Command aliases are short-hand representations of CLI commands.
For more information, see [Creating and using command aliases in chat channels](creating-aliases.md "creating-aliases.md").

## Built-ins

Lists and provides details about Amazon Q Developer in chat applications commands.

### Setting preferences

To manage Amazon Q Developer in chat applications preferences for your chat channel, enter `@Amazon Q set preferences`.

You can manage your threading preferences and communication preferences after running this command.
This includes where Amazon Q Developer in chat applications notifications are displayed, how frequently new threads are created, and what Amazon Q Developer in chat applications related updates you want to receive.

### AWS accounts

To see a list of AWS accounts configured for this channel or select a new account to use for commands, enter `@Amazon Q set-default account`.

If you would like to add an account to the channel, sign-in to the Amazon Q Developer in chat applications console with that account and configure Amazon Q Developer in chat applications for your channel.
For more information, see [Setting up Amazon Q Developer in chat applications](getting-started.md#setting-up "getting-started.md#setting-up").

### Providing feedback

To provide feedback to Amazon Q Developer in chat applications, enter `feedback `your comment``.

### Switching user roles

To access a link for mapping user roles, enter `@Amazon Q switch-roles`.

If your current user role doesn’t have the right permissions, you can switch roles directly from your chat channel. For more information, see [Switching user roles from a chat channel using Amazon Q Developer in chat applications](cm-container.md#cm-switch-role "cm-container.md#cm-switch-role").

## Q&A

Provides additional information about the types of questions Amazon Q Developer in chat applications can answer and how to use Amazon Q Developer with Amazon Q Developer in chat applications. For more information, see [Chatting with Amazon Q Developer in chat channels](asking-questions.md "asking-questions.md").

## More help

To get help with services or operations, use the `--help` parameter. For example, you can enter `@Amazon Q ec2 --help` to get help with EC2. For more information, see [Running AWS CLI commands from chat channels using Amazon Q Developer in chat applications](chatbot-cli-commands.md "chatbot-cli-commands.md").
