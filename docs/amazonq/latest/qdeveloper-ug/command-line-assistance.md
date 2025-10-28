# Command line assistance features

The Amazon Q CLI provides two distinct AI-powered assistance features to help you work more efficiently in your terminal:

- **Autocomplete Dropdown Menu**: A graphical menu that appears to the right of your cursor showing available command options you can select with arrow keys
- **Inline Suggestions**: Gray "ghost text" that appears directly on your command line as you type
  These features work independently - you can use either one without the other, and they have separate configuration options.

## Autocomplete dropdown menu

The autocomplete dropdown menu appears to the right of your cursor when typing commands, showing available options, subcommands, and arguments that you can select using arrow keys. This graphical menu supports theming and works with hundreds of popular command line tools including git, npm, docker, and aws.

### Using the autocomplete dropdown

The autocomplete dropdown is automatically enabled after you install the Amazon Q CLI.

**To use the autocomplete dropdown**

1. [Install the Amazon Q CLI.](command-line-installing.md "command-line-installing.md")
2. Open your terminal or command prompt.
3. Start typing a command, and a graphical menu will appear to the right of your cursor showing available options.
4. Use arrow keys to navigate the suggestions, then press Tab or Enter to select an option.

The dropdown menu works with hundreds of command line tools, making it easier to remember command options and syntax.

### Configuring the autocomplete dropdown

You can customize the autocomplete dropdown behavior and appearance:

- **Enable/disable**: `q settings autocomplete.disable false` (to enable) or `q settings autocomplete.disable true` (to disable)
- **Change theme**: `q theme dark`, `q theme light`, or `q theme system`
- **View current theme**: `q theme`
- **List available themes**: `q theme --list`

For a complete list of autocomplete configuration options, see [Configure Amazon Q settings](command-line-settings.md "command-line-settings.md")
.

## Inline suggestions

Inline suggestions appear as "ghost text" directly on your command line as you type. This feature is separate from the autocomplete dropdown menu and can be enabled or disabled independently.

### Using inline suggestions

Inline suggestions are enabled by default after installation. As you type commands, gray ghost text will appear showing potential completions.

**To use inline suggestions**

1. [Install the Q CLI.](command-line-installing.md "command-line-installing.md")
2. Open your terminal or command prompt.
3. Start typing a command, and gray ghost text will appear showing suggested completions.
4. Press the right arrow key or Tab to accept the suggestion, or continue typing to ignore it.

### Managing inline suggestions

You can control inline suggestions using the `q inline` command:

- **Enable**: `q inline enable`
- **Disable**: `q inline disable`
- **Check status**: `q inline status`
- **Set customization**: `q inline set-customization [ARN]`
- **Show available customizations**: `q inline show-customizations`

For complete command reference, see [q inline](command-line-reference.md#command-line-reference-inline "command-line-reference.md#command-line-reference-inline")
.

## Supported tools

The autocomplete dropdown menu supports a wide range of command line tools, including:

- AWS CLI
- Git
- Docker
- npm
- kubectl
- terraform
- And many more standard Unix/Linux commands
