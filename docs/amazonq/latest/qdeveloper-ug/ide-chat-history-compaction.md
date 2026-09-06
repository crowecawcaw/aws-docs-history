

# Chat history compaction in Amazon Q Developer
<a name="ide-chat-history-compaction"></a>

As you interact with Amazon Q Developer in your IDE, your conversation accumulates in the chat history. This history provides important context that helps Amazon Q understand your project and deliver more relevant responses. However, there are limits to how much conversation history can be included in each request to the underlying model.

## Understanding context window limits
<a name="understanding-context-window-limits"></a>

The context window represents the maximum amount of information that can be processed in a single interaction with Amazon Q. This includes:
+ Your current question or request
+ Previous messages in your conversation
+ Code snippets and files you've shared
+ System information about your project

When this context window approaches its capacity limit, Amazon Q's ability to reference earlier parts of your conversation may be affected.

## How chat history compaction works
<a name="how-chat-history-compaction-works"></a>

Chat history compaction allows you to preserve the essential information from your conversation while reducing the amount of context used. When compaction occurs:

1. Amazon Q analyzes your conversation history

1. It creates a concise summary of key points, questions, and decisions

1. This summary replaces the detailed conversation history in the context window

1. Your complete conversation remains visible in the chat interface

Compaction helps you continue your conversation without losing important context, while avoiding the need to start a completely new chat when you reach context window limits.

## Using chat history compaction
<a name="using-chat-history-compaction"></a>

You can use compaction in two ways:

### Manual compaction
<a name="manual-compaction"></a>

To manually compact your chat history:

1. Enter **/compact** in the chat input field

1. Amazon Q will process your request and display a confirmation message with a summary of the compacted conversation

Use manual compaction when you want to continue your current conversation but notice slower response times or less relevant answers.

### Automatic compaction nudge
<a name="automatic-compaction-nudge"></a>

When your context window reaches approximately 80% of its capacity, Amazon Q will display a notification suggesting compaction. This notification includes:
+ An explanation of why compaction is recommended
+ A button to trigger compaction immediately

## After compaction
<a name="after-compaction"></a>

After compaction occurs:
+ Your complete conversation history remains visible in the chat interface until the end of the current session
+ Amazon Q uses the compacted summary (not the full history) for generating responses
+ The compacted summary is included in the context window instead of the detailed history
+ The detailed chat history will reset when you restart your IDE

## Related commands
<a name="related-commands"></a>

### Clearing chat history
<a name="clearing-chat-history"></a>

As an alternative to compaction, you can completely clear your chat history using the **/clear** command:

1. Enter **/clear** in the chat input field

1. Amazon Q will remove all previous conversation history from both the display and the context window

### When to choose compaction vs. clearing history
<a name="when-to-choose-compaction-vs-clearing"></a>

Choose compaction when:
+ You want to continue your current conversation topic
+ Previous context is still relevant to your current task
+ You want to preserve the general direction and knowledge from your conversation

Choose to clear history when:
+ You're starting a completely new task or topic
+ Previous conversation is no longer relevant
+ You want to ensure no previous context influences new responses
+ You want to remove potentially sensitive information from the conversation