# Experimental features

Amazon Q Developer CLI includes experimental features that provide advanced functionality for enhanced productivity. These features are in active development and must be explicitly enabled before use.

###### Important

Experimental features may change or be removed at any time. Use at your own discretion in production workflows.

## Managing experimental features

Use the `/experiment` command to view and toggle experimental features:

```
/experiment
```

This displays an interactive menu where you can:

- View the current status of each experiment (ON/OFF)
- Toggle experiments by selecting them
- View descriptions of what each experiment does

## Knowledge management

The knowledge management feature provides persistent context storage and retrieval across chat sessions. Enable it with:

```
q settings chat.enableKnowledge true
```

### Basic usage

Once enabled, use `/knowledge` commands within your chat session:

/knowledge add <name> <path>

Add files or directories to your knowledge base

/knowledge show

Display all entries in your knowledge base

/knowledge remove <identifier>

Remove entries by name, path, or context ID

/knowledge update <path>

Update existing knowledge base entry with new content

/knowledge clear

Remove all entries from your knowledge base (requires confirmation)

/knowledge status

View status of background indexing operations

### Index types

Choose between two indexing approaches when adding content:

Fast (--index-type Fast)

Lexical search using BM25. Lightning-fast indexing and instant keyword-based search. Perfect for logs, configs, and large codebases.

Best (--index-type Best)

Semantic search using AI embeddings. Intelligent search that understands context and meaning. Perfect for documentation and research.

Example usage:

```
/knowledge add "project-docs" /path/to/docs --index-type Best
/knowledge add "log-files" /path/to/logs --index-type Fast
```

### Agent-specific knowledge bases

Each agent maintains its own isolated knowledge base, ensuring that knowledge contexts are scoped to the specific agent you're working with. When you switch between agents, your knowledge commands automatically work with that agent's specific knowledge base.

## Tangent mode

Tangent mode creates conversation checkpoints, allowing you to explore side topics without disrupting your main conversation flow. Enable it with:

```
q settings chat.enableTangentMode true
```

### Using tangent mode

Once enabled, use `/tangent` or **Ctrl\*\***+T\*\* to toggle tangent mode:

1. **Enter tangent mode:** Creates a conversation checkpoint

```
/tangent
Created a conversation checkpoint (↯). Use ctrl + t or /tangent to restore the conversation later.
```

2. **In tangent mode:** You'll see a yellow `↯` symbol in your prompt

```
↯ > What is the difference between async and sync functions?
```

3. **Exit tangent mode:** Returns to your main conversation

```
↯ > /tangent
Restored conversation from checkpoint (↯). - Returned to main conversation.
```

### Best practices

Use tangent mode for:

- Asking clarifying questions about the current topic
- Exploring alternative approaches before deciding
- Getting help with Q Developer CLI commands or features
- Testing understanding of concepts

Avoid using tangent mode for completely unrelated topics or long, complex discussions.

## Checkpointing

Checkpointing enables session-scoped snapshots for tracking file changes using Git CLI commands. This feature creates a shadow bare git repository to manage file state across your chat session.

Enable checkpointing with:

```
q settings chat.enableCheckpoint true
```

### Features

- Snapshots file changes into a shadow bare git repository
- List, expand, diff, and restore to any checkpoint
- Conversation history unwinds when restoring checkpoints
- Auto-enables in git repositories (ephemeral, cleaned on session end)
- Manual initialization available for non-git directories

### Basic usage

Once enabled, use `/checkpoint` commands within your chat session:

/checkpoint init

Manually enable checkpoints (required if not in a git repository)

/checkpoint list [--limit N]

Show turn-level checkpoints with file statistics

/checkpoint expand <tag>

Show tool-level checkpoints under a specific turn

/checkpoint diff <tag1> [tag2|HEAD]

Compare checkpoints or compare with current state

/checkpoint restore [<tag>] [--hard]

Restore to checkpoint (shows interactive picker if no tag specified)

/checkpoint clean

Delete session shadow repository

### Restore options

**Default restore behavior:**

- Reverts tracked changes and deletions
- Keeps files created after the checkpoint

**Hard restore (`--hard` flag):**

- Makes workspace exactly match the checkpoint state
- Deletes tracked files created after the checkpoint

###### Important

Checkpointing creates temporary git repositories that are cleaned up when the session ends. Use caution with `--hard` restore as it permanently deletes files.

## Context usage percentage

Context usage percentage displays your current context window consumption as a percentage in the chat prompt, helping you monitor how much of the available context window is being used.

Enable context usage percentage with:

```
q settings chat.enableContextUsageIndicator true
```

### Features

- Shows percentage of context window used in prompt (e.g., "[rust-agent] 6% >")
- Color-coded indicators for quick visual reference
- Helps monitor context window consumption during long conversations

### Visual indicators

The percentage display uses color coding to indicate usage levels:

Green: Less than 50% usage

Normal operation with plenty of context space available

Yellow: 50-89% usage

Moderate usage, consider context management

Red: 90-100% usage

High usage, context window nearly full

## Delegate

Delegate enables launching and managing asynchronous task processes, allowing you to run Amazon Q chat sessions with specific agents in parallel to your main conversation.

Enable delegate with:

```
q settings chat.enableDelegate true
```

### Features

- Launch background tasks using natural language
- Run parallel Amazon Q chat sessions with specific agents
- Monitor task progress independently
- Agent approval flow for secure task execution

### Usage

Use natural language to ask the model to launch a background task:

```
Can you create a background task to analyze the performance of our API endpoints?
```

Once a task is ready, check on results:

```
Check the status of my API analysis task
Show me the results from the background analysis
```

### Agent approval flow

**Tasks with agents:** Require explicit approval and show agent details before execution

**Tasks without agents:** Run with a warning about trust-all permissions

Once delegated, tasks work independently and you can:

- Check progress at any time
- Read results when complete
- Delete tasks when no longer needed

###### Important

Delegate tasks run with elevated permissions. Review agent details carefully before approving task execution.

## TODO lists

TODO lists enable Amazon Q to create and modify task lists automatically, while providing you with commands to view and manage existing TODO lists.

Enable TODO lists with:

```
q settings chat.enableTodoList true
```

### Features

- Amazon Q automatically creates TODO lists when appropriate or when asked
- View, manage, and delete TODOs using `/todos` commands
- Resume existing TODO lists stored in `.amazonq/cli-todo-lists`
- Persistent storage across chat sessions

### Basic usage

Once enabled, Amazon Q will create TODO lists automatically during conversations. Use `/todos` commands to manage them:

/todos clear-finished

Delete completed TODOs in your working directory

/todos resume

Select and resume an existing TODO list

/todos view

Select and view an existing TODO list

/todos delete

Select and delete an existing TODO list

### Workflow integration

Amazon Q creates TODO lists when:

- You ask for a task breakdown
- Complex multi-step processes are discussed
- Project planning conversations occur
- You explicitly request a TODO list

TODO lists are automatically saved to `.amazonq/cli-todo-lists` and persist across chat sessions, allowing you to resume work on long-term projects.

## Enhanced thinking mode

Thinking mode enables complex reasoning with step-by-step thought processes, providing transparency into Amazon Q's decision-making process.

Enable thinking mode with:

```
q settings chat.enableThinking true
```

### Features

- Shows AI reasoning process for complex problems
- Step-by-step thought processes for multi-step reasoning
- Helps understand how conclusions are reached
- Useful for debugging and learning
- Transparent decision-making for complex tasks

### When to use

Thinking mode is particularly valuable for:

- **Complex problem solving:** Understanding the reasoning behind solutions
- **Debugging assistance:** Seeing the analytical process for troubleshooting
- **Learning scenarios:** Understanding how concepts connect and build upon each other
- **Multi-step workflows:** Following the logic through complex procedures

## Settings integration

All experimental features integrate with the Amazon Q CLI settings system and persist across sessions. You can manage experiments through:

**Interactive experiment menu:**

```
/experiment
```

**Direct settings commands:**

```
q settings chat.enableCheckpoint true
q settings chat.enableContextUsageIndicator true
q settings chat.enableKnowledge true
q settings chat.enableTangentMode true
q settings chat.enableThinking true
q settings chat.enableDelegate true
q settings chat.enableTodoList true
```

### Fuzzy search integration

All experimental commands are available through fuzzy search (**Ctrl\*\***+S\*\*):

- `/experiment` - Manage experimental features
- `/knowledge` - Knowledge base commands (when enabled)
- `/checkpoint` - Checkpointing commands (when enabled)
- `/todos` - TODO list commands (when enabled)
- `/tangent` - Tangent mode toggle (when enabled)

This integration makes experimental features easily discoverable and accessible during your workflow.

## Additional resources

For complete details about experimental features, including advanced configuration options and troubleshooting, see the supplementary Amazon Q Developer CLI documentation:

- [Experimental features reference](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/experiments.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/experiments.md")
- [Knowledge management guide](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/knowledge-management.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/knowledge-management.md")
- [Tangent mode guide](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/tangent-mode.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/tangent-mode.md")
