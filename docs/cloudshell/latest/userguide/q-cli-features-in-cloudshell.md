

# Using Kiro CLI in CloudShell

With Kiro CLI, you can interact with Kiro from the command line. For more information, see [Kiro CLI](https://kiro.dev/docs/cli/) on the Kiro website.

In CloudShell, you can use Kiro CLI to have natural language conversations, ask questions, and get responses in your terminal. Kiro CLI can also use the pre-installed tools in CloudShell, such as the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), the [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html), and the [Amazon ECS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI.html). You don't need to remember syntax or search for the right command. For more information, see [Pre-installed software](vm-specs.md#pre-installed-software).

This topic explains how you can use Kiro CLI features in CloudShell.

## Using Kiro chat in CloudShell
<a name="q-chat-in-cloudshell"></a>

You can ask questions in plain language and get answers in the terminal. Answers can include shell commands you can run. For more information, see [Chatting with Kiro CLI](https://kiro.dev/docs/cli/chat/) on the Kiro website.

Start a chat session.

```bash
kiro-cli
```

Display the version of Kiro CLI.

```bash
kiro-cli --version
```

List the available commands and options.

```bash
kiro-cli --help
```

Because CloudShell already has the AWS CLI installed and uses the credentials of the signed-in console user, Kiro CLI can run AWS CLI commands on your behalf to answer questions about your AWS account and resources. Kiro CLI can only perform actions that your permissions allow.

For example, you can ask questions like the following:
+ "Show me which AMIs in my account are shared with other AWS accounts. Include all enabled regions."
+ "Show me all console login events for the past 48 hours."
+ "Make a CSV file of EBS snapshots in us-east-2 that are older than 1 year and have newer snapshots."

To end a chat session, run `/quit`.

## Signing in to Kiro CLI in CloudShell
<a name="sign-in-kiro-cli"></a>

You must sign in before you can use Kiro CLI in CloudShell. The first time you run `kiro-cli`, it starts the sign-in process for you.

Kiro CLI prompts you to finish signing in from a browser. You can sign in with Google, GitHub, AWS Builder ID, AWS IAM Identity Center, or your organization's identity provider. For more information, see [Sign in to Kiro](https://kiro.dev/docs/getting-started/authentication/#sign-in-to-kiro) on the Kiro website.

**Note**  
During sign-in, the progress indicator refreshes the display while the sign-in URL is shown, which can make the URL difficult to select. To copy the URL, select it with your pointing device and continue to hold the selection while you press Ctrl\+C or Cmd\+C to copy the URL to your clipboard. Then paste the URL in your browser to complete the sign-in.

To check which sign-in method you are using, run the following command.

```bash
kiro-cli whoami
```

To sign out, run the following command.

```bash
kiro-cli logout
```

To sign in with a different method, sign out first, and then run the following command. If you are still signed in, Kiro CLI returns an error.

```bash
kiro-cli login
```

## Configuring the AWS MCP Server for Kiro CLI in CloudShell
<a name="configure-aws-mcp"></a>

You can configure the AWS MCP Server (`aws-mcp`) for Kiro CLI in CloudShell so that Kiro can use AWS tools through the Model Context Protocol (MCP). The server signs its requests with your CloudShell session credentials, so its tools act with the same permissions that you have in the console.

For more information about the AWS MCP Server, see [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in the *Agent Toolkit for AWS* documentation.

To configure the server, run the following commands in CloudShell.

```bash
curl -fsS "https://docs.aws.amazon.com/cloudshell/latest/userguide/samples/kiro-cloudshell-aws-mcp.zip" -o "kiro-cloudshell-aws-mcp.zip"
unzip -q -o kiro-cloudshell-aws-mcp.zip
chmod +x kiro-cloudshell-aws-mcp.sh
./kiro-cloudshell-aws-mcp.sh
```

You can also download [kiro-cloudshell-aws-mcp.zip](samples/kiro-cloudshell-aws-mcp.zip) directly.

The script configures only the `aws-mcp` server for Kiro CLI. It doesn't install, update, or launch Kiro CLI, and it works with the pre-installed version. You don't need to sign in to Kiro CLI before you run the script. To verify the configuration, run `kiro-cli`, and then enter `/mcp` to confirm that `aws-mcp` is running.

You can run the script again at any time. It updates only the `aws-mcp` entry in your configuration and leaves any other MCP servers in place. CloudShell keeps a separate home directory in each AWS Region, so run the script one time in each AWS Region where you use Kiro CLI.

**Note**  
The script installs `uv` in a virtual environment in your home directory and writes the `aws-mcp` configuration to `~/.kiro/settings/mcp.json`. It keeps the larger `uv` cache and downloaded files in temporary storage to conserve space in your home directory.  
When you restart your CloudShell environment, the configuration and virtual environment persist, and the temporary files download again the next time the server starts. When you delete your CloudShell environment, run the script again.  
For more information about the script, see `kiro-cloudshell-aws-mcp-README.md` in the zip file.

## Using the latest version of Kiro CLI in CloudShell
<a name="install-latest-kiro-cli"></a>

CloudShell includes a pre-installed version of Kiro CLI, which might not be the latest release. To get the latest version, run the following commands in CloudShell.

```bash
curl -fsS "https://docs.aws.amazon.com/cloudshell/latest/userguide/samples/kiro-cloudshell-latest.zip" -o "kiro-cloudshell-latest.zip"
unzip -q -o kiro-cloudshell-latest.zip
chmod +x kiro-cloudshell-latest.sh
./kiro-cloudshell-latest.sh
```

You can also download [kiro-cloudshell-latest.zip](samples/kiro-cloudshell-latest.zip) directly.

Any arguments you add after the script name are passed through to Kiro CLI after the update completes.

Update Kiro CLI and then launch it with a list of previous chats to resume.

```bash
./kiro-cloudshell-latest.sh --resume-picker
```

**Note**  
The script downloads the latest installer from `https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-x86_64-linux.zip`.  
The script then extracts the archive and runs the bundled installer with `sudo KIRO_CLI_INSTALL_GLOBAL=1 KIRO_CLI_NO_MODIFY_PATH=1 "/tmp/kirocli-update.XXXXXX/kirocli/install.sh"`, where `XXXXXX` is a temporary folder name that the script generates.  
The script puts the latest version in a temporary location. When you restart your CloudShell environment, Kiro CLI resets to the pre-installed version. Run the script again to update. Your data, such as chat history, settings, and sign-in, is saved in your home directory and persists across restarts.  
For more information about the script, see `kiro-cloudshell-latest-README.md` in the zip file.