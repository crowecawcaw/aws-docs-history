# Using the editor command in the CLI

The Amazon Q Developer CLI provides an `/editor` command that opens your preferred text editor to compose complex prompts. This is particularly useful for multi-line prompts, code examples, or when you need to carefully structure your questions.

## Basic usage

To open your default editor with an empty prompt:

```
Amazon Q> /editor
```

To open your editor with initial text:

```
Amazon Q> /editor Write a Python function that calculates Fibonacci numbers
```

When you use the `/editor` command, Amazon Q creates a temporary file with a `.md` extension, opens your specified editor with this file, and then reads the content and submits it as your prompt when you save and close the editor.

## Setting your preferred editor

Amazon Q uses your system's `$EDITOR` environment variable to determine which editor to open. If not set, it defaults to `vi`.

### Temporary setting (current session only)

To set your editor for the current terminal session only:

```
$ export EDITOR=nano
```

### Permanent setting

To make your editor preference persistent across sessions, add the export command to your shell configuration file:

```
# For bash (add to ~/.bashrc)
export EDITOR=nano

# For zsh (add to ~/.zshrc)
export EDITOR=nano

# For fish shell (add to ~/.config/fish/config.fish)
set -x EDITOR nano
```

After editing your configuration file, either restart your terminal or source the file:

```
$ source ~/.bashrc  # or ~/.zshrc
```

### Common editor options

Here are some common editor options you can use:

- `vi` or `vim` - Vi/Vim text editor
- `nano` - Nano text editor (beginner-friendly)
- `emacs` - Emacs text editor
- `code -w` - Visual Studio Code (requires VS Code CLI to be installed)
- `subl -w` - Sublime Text (requires Sublime CLI to be installed)

###### Note

The `-w` flag for GUI editors is important as it makes the terminal wait until the file is closed.

## How it works

The `/editor` command follows this workflow:

1. When you use the `/editor` command, Amazon Q creates a temporary file with a `.md` extension
2. Your specified editor opens with this file
3. You write your prompt in the editor and save the file
4. When you close the editor
5. Amazon Q reads the content and submits it as your prompt
6. The temporary file is automatically cleaned up

## Working with code in the editor

When you write code in the editor, the entire content is sent as your prompt to Amazon Q when you close the editor. The code is not executed locally - it's treated as text input for the AI.

### Example: Writing and submitting code

1. Type `/editor` to open your editor
2. Write a Python script in the editor:

```
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# This function seems inefficient
# How can I improve it?
```

3. Save and close the editor
4. Amazon Q will receive this entire text as your prompt and respond with suggestions for improving the code

This approach is useful for:

- Getting code reviews
- Asking for optimizations
- Explaining complex code structures
- Providing context for debugging help

## Combining with other commands

The `/editor` command becomes even more powerful when combined with other Amazon Q CLI commands. Here are some practical combinations to enhance your workflow.

### Using /editor with /compact

The `/compact` command makes Amazon Q responses more concise. This combination is excellent for efficient code reviews:

```
Amazon Q> /editor
# Write in the editor:
Please review this Python function that calculates prime numbers:

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Save and close

Amazon Q> /compact
# This makes Amazon Q provide a concise code review
```

### Using /editor with /context

The `/context` command adds files to the conversation context. This combination is useful for discussing code that references other files:

```
Amazon Q> /context path/to/config.json
Amazon Q> /editor
# Write in the editor:
Given the config.json file I just shared, please help me write a Python function that:
1. Loads the configuration
2. Validates all required fields are present
3. Returns a validated config object

# Save and close
```

### Using /editor with /clear

The `/clear` command starts a new conversation. This combination helps when switching topics:

```
Amazon Q> /clear
Amazon Q> /editor
# Write in the editor:
I want to start a new discussion about AWS Lambda cold starts.
What are the best practices for minimizing cold start times for Python Lambda functions?

# Save and close
```

### Using /editor for multi-step conversations

The `/editor` command creates a fresh temporary file each time it's used. You can use it multiple times in a conversation to build on previous responses:

```
# First use of editor for initial complex question
Amazon Q> /editor
# Write in editor:
I need to design a database schema for a library management system.
Requirements:
- Track books, authors, publishers
- Handle member checkouts and returns
- Support reservations and waiting lists
- Generate overdue notices

# After getting Amazon Q's response with initial schema design

# Second use of editor for follow-up with specific implementation details
Amazon Q> /editor
# Write in editor:
Based on your proposed schema, I have some follow-up questions:
1. How would you modify the Member table to support different membership tiers?
2. What indexes would you recommend for optimizing checkout queries?
3. Can you show me SQL to create the Books and Authors tables with proper relationships?
```

The benefit of this approach is that you can carefully craft complex follow-up questions that reference the previous conversation, without having to type everything in the command line. Each editor session gives you the space and formatting control to compose detailed questions that build on Amazon Q's previous responses.

### Using /editor with /profile

Switch to a different context profile before using the editor for specialized questions:

```
Amazon Q> /profile set aws-developer
Amazon Q> /editor
# Write detailed AWS-specific questions that benefit from the AWS developer profile context
```

### Using /editor with /help

If you're unsure about command options, you can use `/help` before `/editor`:

```
Amazon Q> /help editor
# Review the help information
Amazon Q> /editor
# Use the editor with better understanding of available options
```

## Best practices for command combinations

1. Use `/context` before `/editor` when you need to reference specific files
2. Use `/editor` before `/compact` when you want concise responses to complex questions
3. Use `/clear` before `/editor` when starting a completely new topic
4. Use multiple `/editor` sessions for complex, multi-part conversations where you need to carefully craft follow-up questions
5. Consider your current profile before using `/editor` to ensure you're in the right context

## Tips for effective use

- Use the editor for complex prompts that benefit from careful structuring
- Include code examples with proper indentation
- Organize multi-part questions with clear sections
- Use Markdown formatting for better structure
- If you save an empty file, no prompt will be submitted

## Troubleshooting

- _Editor not opening_: Verify your $EDITOR environment variable is set correctly
- _"No such file or directory" error_: Ensure the editor command is installed and in your PATH
- _Terminal hanging_: For GUI editors, make sure to use the wait flag (e.g., `-w`)
- _Content not being submitted_: Check that you saved the file before closing the editor
