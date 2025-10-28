# Using chat on the command line

The Amazon Q Developer CLI provides an interactive chat experience directly in your terminal. You
can ask questions, get help with AWS services, troubleshoot issues, and generate code
snippets without leaving your command line environment.

## Starting a chat session

To start a chat session with Amazon Q, use the `chat` subcommand:

```
$ q chat
```

This opens an interactive chat session where you can type questions or
commands.

To exit the chat session, type `/quit` or press
**Ctrl**
**+D**
.

## Entering multi-line statements

To enter multi-line statements in Amazon Q Developer CLI, use the `/editor` command:

```
/editor
```

This opens your default editor (defaults to vi) where you can compose longer,
multi-line prompts. After you save and close the editor, the content will be
sent as your message to Amazon Q Developer CLI.

You can also:

- Use the `/reply` command to open your editor with the most recent
  assistant message quoted for reply, which is useful for multi-line responses to
  previous messages.
- Type your statement into a text editor and cut-paste it into Amazon Q Developer CLI.
