# Conversation persistence

Amazon Q can remember your conversations based on the directory where they take place. When you return
to a directory where you previously chatted with Amazon Q, you can tell Q to automatically load
that conversation history, allowing you to seamlessly continue your discussion.

## Directory-based persistence

If it's your first time chatting in that directory, Amazon Q will start a new conversation (taking
into consideration any designated [context](command-line-context.md "command-line-context.md")).

To explicitly resume a conversation in the current directory, use:

```
$ q chat --resume
```

## Manually saving and loading

conversations

You can also manually save and load conversations using the following commands while in a chat
session:

- `/save [path]` – Saves your current conversation to a JSON file.
  - Add `-f` or `--force` to overwrite an existing file

  Examples:

  `/save ./my-project-conversation -f`

  `/save /home/user/project/my-project-conversation.json`

  You cannot use `~` to denote your home directory.

- `/load [path]` – Loads a conversation from a previously saved JSON
  file
  - Example: `/load ./my-project-conversation.json`

###### Note

The `/save` and `/load` commands operate independently of the
directory where the conversation was originally created. When loading a conversation, be
mindful that it will replace your current conversation regardless of which directory it was
saved from.

These commands are useful for:

- Backing up important conversations
- Sharing conversations with team members
- Moving conversations between different working directories
