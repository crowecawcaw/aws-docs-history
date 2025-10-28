# Selecting a model for chat on the command line

You can select the model you want Amazon Q to use to respond to your requests during chat sessions. A
default model is set when you start a chat session, and you can either change the model Amazon Q uses
for a given session or set a default model for all sessions.

At the time of writing, the following models are available for chat sessions:

- Anthropic Claude Sonnet 4.5
- Anthropic Claude Sonnet 4 (default)
- Anthropic Claude Sonnet 3.5
  The following sections describe how to change the model Amazon Q uses for chat sessions.

## Change the model for a chat session

To change the model Amazon Q uses for a chat session you've already started, use the
`/model` command.

The model that's currently being used is indicated on the list of supported models. To change
the model, use arrow keys to move through the list, and choose enter on your keyboard to select
one.

The model you select persists for the duration of the chat session, or until you change it. When
you start a new session, Amazon Q uses the default model again.

## Launch a chat session with a specific model

You can start a chat session with a specific model using a single command. Add the
`--model` option with the name of a supported model to use that model for the
session:

```
q chat --model <model name>
```

You must supply the model name in the following format:

- claude-sonnet-4.5
- claude-sonnet-4
- claude-3.5-sonnet

The model you select persists for the duration of the chat session, or until you change it. When
you start a new session, Amazon Q uses the default model again.

Models marked with `experimental` indicate they are still being evaluated by the
Q CLI development team to make sure they work as expected.

## Set a default model for chat sessions

You can change the default model that Amazon Q uses when you start chat sessions with the
following command:

```
q settings chat.defaultModel <model name>
```

You must supply the model name in the following format:

- claude-sonnet-4.5
- claude-sonnet-4
- claude-3.5-sonnet

Amazon Q will use the model you set as the default model for all future chat sessions. You still
have the option to set a different model for a given chat session using the previously described
methods.
