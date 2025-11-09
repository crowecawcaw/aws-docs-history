# Context management

## Choosing the right context approach

Amazon Q offers three ways to provide context, each optimized for different use cases:

| Approach            | Context Window Impact           | Persistence                | Best For                                    |
| ------------------- | ------------------------------- | -------------------------- | ------------------------------------------- |
| **Agent Resources** | Always active (consumes tokens) | Persistent across sessions | Essential project files, standards, configs |
| **Session Context** | Always active (consumes tokens) | Current session only       | Temporary files, quick experiments          |
| **Knowledge Bases** | Only when searched              | Persistent across sessions | Large codebases, extensive documentation    |

### Decision flowchart

Use this decision tree to choose the appropriate context approach:

1. **Is your content larger than 10MB or contains thousands of files?**
   - **Yes** → Use Knowledge Bases
   - **No** → Continue to step 2

2. **Do you need this context in every conversation?**
   - **Yes** → Use Agent Resources
   - **No** → Use Session Context

**Quick reference:**

- Essential project files (README, configs, standards) → Agent Resources
- Large codebases or documentation sets → Knowledge Bases
- Temporary files for current task → Session Context

## Understanding context window impact

Context files and agent resources consume tokens from your context window on every request, whether referenced or not. Use `/context show` to monitor token usage:

```
q chat
> /context show
Total: ~1100 tokens
```

**Token limits**: Context files are limited to 75% of your model's context window. Files exceeding this limit are automatically dropped.

**Knowledge bases** don't consume context window space until searched, making them ideal for large reference materials. For more information, see [Knowledge base context (for large datasets)](#command-line-context-knowledge-bases "#command-line-context-knowledge-bases").

## Managing context

Context files contain information you want Amazon Q to consider during your conversations. These can include project requirements, coding standards, development rules, or any other information that helps Amazon Q provide more relevant responses.

### Configuring persistent context with agent resources

The recommended way to configure context is through the `resources` field in your agent configuration file. This creates persistent context that is available every time you use the agent.

Add file paths or glob patterns to the `resources` array in your agent config:

```
{
  "name": "my-agent",
  "description": "My development agent",
  "resources": [
    "file://README.md",
    "file://.amazonq/rules/**/*.md",
    "file://docs/**/*.md",
    "file://src/config.py"
  ]
}
```

Resources must be prefixed with `file://` to be included as context files. These files will be automatically available in all chat sessions using this agent.

### Adding temporary session context

You can temporarily add files to your current chat session using the `/context add` command. These additions are only available for the current session and will not persist when you start a new chat session.

```
q chat
> /context add README.md
Added 1 path(s) to context.
Note: Context modifications via slash command is temporary.
```

You can also add multiple files at once using glob patterns:

```
q chat
> /context add docs/*.md
Added 3 path(s) to context.
Note: Context modifications via slash command is temporary.
```

To make context changes permanent, add the files to your agent's `resources` field instead. For more information, see [Configuring persistent context with agent resources](#command-line-context-agent-resources "#command-line-context-agent-resources").

### Knowledge base context (for large datasets)

For large codebases, documentation sets, or reference materials that would exceed context window limits, use knowledge bases. Knowledge bases provide semantic search capabilities without consuming context window space until searched.

Enable knowledge bases:

```
q settings chat.enableKnowledge true
```

Add content to a knowledge base:

```
q chat
> /knowledge add /path/to/large-codebase --include "**/*.py" --exclude "node_modules/**"
```

Knowledge bases are searched on-demand by Amazon Q when relevant information is needed, making them ideal for large reference materials.

### Viewing context

To view your current context, use the `/context show` command:

```
q chat
> /context show
👤 Agent (my-agent):
    README.md (1 match)
    .amazonq/rules/**/*.md (3 matches)
    docs/**/*.md (5 matches)

💬 Session (temporary):
    <none>

5 matched files in use:
👤 README.md (~250 tkns)
👤 .amazonq/rules/security.md (~180 tkns)
👤 .amazonq/rules/coding-standards.md (~320 tkns)
👤 docs/architecture.md (~150 tkns)
👤 docs/best-practices.md (~200 tkns)

Total: ~1100 tokens
```

The output shows:

- **👤 Agent**: Persistent context from your agent's `resources` field
- **💬 Session**: Temporary context added during the current session

### Removing context

To remove files from your current session context, use the `/context rm` command:

```
q chat
> /context rm src/temp-file.py
Removed 1 path(s) from context.
Note: Context modifications via slash command is temporary.
```

To clear all session context, use the `/context clear` command:

```
q chat
> /context clear
Cleared context
Note: Context modifications via slash command is temporary.
```

**Note:** You cannot remove agent-defined context using `/context` commands. To permanently remove context, edit your agent's `resources` field.

## Common use cases

Here are some common use cases for context management:

### Using project rules

Amazon Q supports project-level rules that can define security guidelines and restrictions. These rules are defined in Markdown files in the `.amazonq/rules` directory of your project.

For example, you can create rules that specify:

- Which directories Amazon Q should avoid accessing
- Security requirements for generated code
- Coding standards and best practices

The recommended way to include project rules is through your agent configuration:

```
{
  "name": "my-project-agent",
  "resources": [
    "file://.amazonq/rules/**/*.md",
    "file://README.md",
    "file://docs/architecture.md"
  ]
}
```

You can also temporarily add project rules to your current session:

```
q chat
> /context add .amazonq/rules/*.md
Added 3 path(s) to context.
Note: Context modifications via slash command is temporary.
```

For more information about creating and using project rules, see [Creating project rules for use with Amazon Q Developer chat](context-project-rules.md "context-project-rules.md") in the IDE documentation.

### Migrating from session context to agent resources

If you find yourself repeatedly adding the same context files using `/context add` commands, consider moving them to your agent's `resources` field for persistence:

1. Note the files you frequently add with `/context add`
2. Edit your agent configuration file using `/agent edit` or by directly modifying the file
3. Add the file paths to the `resources` array with `file://` prefix
4. Save the agent configuration

Example migration:

```
# Instead of running these commands every session:
> /context add README.md
> /context add docs/*.md
> /context add .amazonq/rules/*.md

# Add them to your agent config once:
{
  "resources": [
    "file://README.md",
    "file://docs/**/*.md",
    "file://.amazonq/rules/**/*.md"
  ]
}
```

### When to use knowledge bases

Consider knowledge bases when:

- Your context files exceed the token limit (75% of context window)
- You have large codebases or documentation sets
- You need semantic search across extensive materials
- You want to avoid constant context window consumption

Example: Instead of adding a large codebase as context files:

```
# This would consume too many tokens:
> /context add src/**/*.py

# Use knowledge base instead:
> /knowledge add src/ --include "**/*.py" --exclude "__pycache__/**"
```

### Setting a default agent with context

You can configure a default agent that includes your preferred context files:

```
q settings chat.defaultAgent my-project-agent
```

This ensures your context is automatically available in new chat sessions without needing to specify the agent each time.

## Best practices

### Context file organization

- Keep context files focused and relevant to avoid token limits
- Use descriptive filenames that indicate their purpose
- Organize rules and documentation in logical directory structures
- Consider file size - very large files may consume significant tokens

### Performance considerations

- Monitor token usage with `/context show` to stay within limits
- Use specific glob patterns rather than overly broad ones
- Remove unused context files from agent configurations
- Consider splitting large context files into smaller, focused files
- Use knowledge bases for large datasets to avoid context window consumption

### Security considerations

- Avoid including sensitive information in context files
- Use `.gitignore` to prevent accidental commits of sensitive context
- Review context files regularly to ensure they don't contain outdated information
- Be mindful of what information is shared when using context in conversations
