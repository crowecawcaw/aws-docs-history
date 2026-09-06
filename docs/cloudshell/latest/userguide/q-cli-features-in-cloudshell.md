

# Using Kiro CLI in CloudShell
<a name="q-cli-features-in-cloudshell"></a>

With Kiro CLI, you can interact with Kiro from the command line. For more information, see [Core Features of Kiro CLI](https://kiro.dev/docs/cli/#core-features) on the Kiro website.

In CloudShell, you can use Kiro CLI to have natural language conversations, ask questions, and get responses in your terminal. Kiro CLI can also use the pre-installed tools in CloudShell, such as the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), the [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html), and the [Amazon ECS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI.html). You don't need to remember syntax or search for the right command. For more information, see [Pre-installed software](vm-specs.md#pre-installed-software).

This topic explains how you can use Kiro CLI features in CloudShell.

## Using Kiro chat in CloudShell
<a name="q-chat-in-cloudshell"></a>

Run `kiro-cli` in the CloudShell terminal to start a chat session. You can ask questions in plain language and get answers in the terminal. Answers can include shell commands you can run. For more information, see [Chatting with Kiro in the CLI](https://kiro.dev/docs/cli/chat/) on the Kiro website.

By default, chat uses the terminal UI, which shows code with syntax highlighting and displays tool progress. For more information, see [Terminal UI](https://kiro.dev/docs/cli/terminal-ui/) on the Kiro website.

Start a chat session with the default terminal UI.

```
kiro-cli
```

Start a chat session with the classic interface for a single session.

```
kiro-cli --classic
```

To change the default interface, run one of the following commands. Use `tui` for the terminal UI, or `classic` for the classic interface.

```
kiro-cli settings chat.ui "tui"
```

```
kiro-cli settings chat.ui "classic"
```

You can resume a chat session in either interface. For more information about switching interfaces, see [Switching back to classic](https://kiro.dev/docs/cli/terminal-ui/comparison/#switching-back-to-classic), and for a comparison of the two interfaces, see [Terminal UI vs classic](https://kiro.dev/docs/cli/terminal-ui/comparison/) on the Kiro website.

Because CloudShell already has the AWS CLI installed and uses the credentials of the signed-in console user, Kiro CLI can run AWS CLI commands on your behalf to answer questions about your AWS account and resources. Kiro CLI can only perform actions that your permissions allow.

For example, you can ask questions like the following:
+ "Show me which AMIs in my account are shared with other AWS accounts. Include all enabled regions."
+ "Show me all console login events for the past 48 hours."
+ "Make a CSV file of EBS snapshots in us-east-2 that are older than 1 year and have newer snapshots."

To end a chat session, run `/quit`.

## Signing in to Kiro CLI in CloudShell
<a name="sign-in-kiro-cli"></a>

You must sign in before you can use Kiro CLI in CloudShell. The first time you run `kiro-cli`, it starts the sign-in process for you.

Kiro CLI prompts you to finish signing in from a browser. You can sign in with Google, GitHub, AWS Builder ID, AWS IAM Identity Center, or your organization's identity provider. For more information, see [Sign in to Kiro CLI](https://kiro.dev/docs/cli/authentication/#sign-in-to-kiro-cli) on the Kiro website.

**Note**  
During sign-in, the progress indicator refreshes the display while the sign-in URL is shown, which can make the URL difficult to select. To copy the URL, select it with your pointing device and continue to hold the selection while you press Ctrl\+C or Cmd\+C to copy the URL to your clipboard. Then paste the URL in your browser to complete the sign-in.

To check which sign-in method you are using, run the following command.

```
kiro-cli whoami
```

To sign out, run the following command.

```
kiro-cli logout
```

To sign in with a different method, sign out first, and then run the following command. If you are still signed in, Kiro CLI returns an error.

```
kiro-cli login
```

## CLI command completion in CloudShell
<a name="cli-completion"></a>

CLI completion in CloudShell provides suggestions for commands and options as you type in the terminal. For more information, see [Generating command line completion](https://kiro.dev/docs/cli/autocomplete/) on the Kiro website.

## Using Kiro inline suggestions in CloudShell
<a name="q-inline-suggestions"></a>

Kiro inline suggestions in CloudShell provide command suggestions as you type in the terminal. For more information, see [Inline suggestions](https://kiro.dev/docs/cli/autocomplete/#inline-suggestions) on the Kiro website.

In the CloudShell terminal, run `zsh` to open Z shell, and then start typing a command. Kiro makes suggestions based on your current input and previous commands. Inline suggestions are automatically enabled.

**Note**  
Kiro inline suggestions are supported only in Z shell.

## Using the latest version of Kiro CLI in CloudShell
<a name="install-latest-kiro-cli"></a>

CloudShell includes a pre-installed version of Kiro CLI, which might not be the latest release. To get the latest version, run the following commands in CloudShell.

```
curl -s "https://docs.aws.amazon.com/cloudshell/latest/userguide/samples/kiro-cloudshell-latest.zip" -o "kiro-cloudshell-latest.zip"
unzip -q -o kiro-cloudshell-latest.zip
chmod +x kiro-cloudshell-latest.sh
./kiro-cloudshell-latest.sh --classic
```

You can also download [kiro-cloudshell-latest.zip](samples/kiro-cloudshell-latest.zip) directly.

Any arguments you add after the script name are passed through to Kiro CLI after the update completes.

Update Kiro CLI and then launch it with a list of previous chats to resume.

```
./kiro-cloudshell-latest.sh --resume-picker
```

Update Kiro CLI and then launch it with the classic interface.

```
./kiro-cloudshell-latest.sh --classic
```

**Note**  
The script downloads the latest installer from `https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-x86_64-linux.zip`.  
The script then extracts the archive and runs the bundled installer with `sudo Q_INSTALL_GLOBAL=1 Q_SKIP_SETUP=1 "/tmp/kirocli-update.{{XXXXXX}}/kirocli/install.sh"`.  
The script puts the latest version in a temporary location. When you restart your CloudShell environment, Kiro CLI resets to the pre-installed version. Run the script again to update. Your data, such as chat history, settings, and sign-in, is saved in your home directory and persists across restarts.  
For more information about the script, see `kiro-cloudshell-latest-README.md` in the zip file.