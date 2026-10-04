

# Getting started with AWS Startup Advisor
<a name="getting-started"></a>

You can get started with AWS Startup Advisor on the web, in a supported IDE, or in Claude Code. Choose the entry point that fits your workflow. The same curated skills are available across all access methods, so you get the same guidance no matter which one you choose.

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Get started on the web](#getting-started-web)
+ [Install the Claude Code plugin](#getting-started-claude-code)
+ [Install the IDE extension](#getting-started-ide)
+ [Install the AWS Startup Advisor skills in other coding agents (npx)](#getting-started-npx)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before you begin, review the prerequisites in [Setting up AWS Startup Advisor](setting-up.md). An AWS account is recommended, and you need one to deploy and build on AWS. A submitted AWS Activate Credit application is optional. If you submit one, AWS Startup Advisor can use it to tailor its guidance to your startup. The same curated skills are available across all access methods.

## Get started on the web
<a name="getting-started-web"></a>

You can start using AWS Startup Advisor on the web. No install is required.

1. Open [https://startups.aws.com/](https://startups.aws.com/).

1. Answer a few questions about your startup.

 AWS Startup Advisor uses your AWS Activate Credit application to pick up your stack and stage.

## Install the Claude Code plugin
<a name="getting-started-claude-code"></a>

You can install the AWS Startup Advisor plugin for Claude Code. To install the plugin, run the following command in your terminal:

```
claude plugin install aws-startup-advisor@claude-plugins-official
```

The plugin works on macOS, Windows, and Linux. For the plugin’s marketplace listing, see [the AWS Startup Advisor Claude Code Plugin Marketplace page](https://claude.com/plugins/aws-startup-advisor). To download Claude Code, see [the Claude Code page](https://claude.com/claude-code).

## Install the IDE extension
<a name="getting-started-ide"></a>

You can install the AWS Startup Advisor extension for Cursor, VS Code, or Kiro. Other VS Code-based IDEs can install the extension from the [Open VSX Registry](https://open-vsx.org/extension/amazonwebservices/aws-startup-advisor).

Install the tool you want to use before you install the extension. For more information, see the official download site for each tool.

The simplest way to install is from within your IDE. Search for ** AWS Startup Advisor** in your IDE’s Extensions view and choose **Install**. The per-IDE command-line and marketplace options follow.

**Note**  
 **Requirements**: VS Code 1.85 or later (or Kiro or Cursor), an AWS account, and an AWS CLI profile, an IAM Identity Center (SSO) start URL, or IAM access keys. A read-only profile is sufficient, because the extension never writes to your account.

### Install the extension for Cursor
<a name="getting-started-ide-cursor"></a>

To download Cursor, see [the Cursor downloads page](https://cursor.com/downloads).

The Cursor extension is available from the Open VSX Registry. For the marketplace listing, see [AWS Startup Advisor on the Open VSX Registry](https://open-vsx.org/extension/amazonwebservices/aws-startup-advisor).

To install the extension from the command line, run the following command:

```
cursor --install-extension amazonwebservices.aws-startup-advisor
```

This command requires the `cursor` CLI command on your PATH. To add it in Cursor, open the Command Palette and choose **Install 'cursor' command in PATH**.

Alternatively, you can install the extension from within Cursor:

1. Open Extensions ( Cmd Shift X  on macOS, or  Ctrl Shift X  on Windows and Linux).

1. Search for ** AWS Startup Advisor**.

1. Choose **Install**.

### Install the extension for VS Code
<a name="getting-started-ide-vscode"></a>

To download VS Code, see [the VS Code downloads page](https://code.visualstudio.com/download).

The VS Code extension is available from the Visual Studio Marketplace. For the marketplace listing, see [AWS Startup Advisor on the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-startup-advisor).

To install the extension from the command line, run the following command:

```
code --install-extension AmazonWebServices.aws-startup-advisor
```

This command requires the `code` CLI command on your PATH. To add it in VS Code, open the Command Palette and choose **Shell Command: Install 'code' command in PATH**.

Alternatively, you can install the extension from the Visual Studio Marketplace listing by choosing **Install**, which uses the `vscode:extension/AmazonWebServices.aws-startup-advisor` deep link.

### Install the extension for Kiro
<a name="getting-started-ide-kiro"></a>

To download Kiro, see [the Kiro downloads page](https://kiro.dev/downloads).

The Kiro extension is available from the Open VSX Registry. For the marketplace listing, see [AWS Startup Advisor on the Open VSX Registry](https://open-vsx.org/extension/amazonwebservices/aws-startup-advisor).

To install the extension from the command line, run the following command:

```
kiro --install-extension amazonwebservices.aws-startup-advisor
```

This command requires the `kiro` CLI command on your PATH. To add it in Kiro, open the Command Palette and choose **Install 'kiro' command in PATH**.

### Sign in
<a name="getting-started-ide-signin"></a>

After you install the extension, sign in to connect it to your AWS account. Signing in enables the extension’s alerts, because you give the extension permission to read your account. You can sign in using one of the following methods: AWS IAM Identity Center (SSO) (recommended), an AWS CLI profile, or IAM access keys.

1. Choose the AWS Startup Advisor icon in the activity bar.

1. Choose one of the following sign-in options:
   +  **Sign in with SSO** – Paste your IAM Identity Center start URL and follow the browser flow.
   +  **Sign in with AWS profile** – Choose a profile.
   +  **Sign in with IAM access keys** – Enter your IAM access key ID and secret access key.

After you sign in, the extension takes a few seconds to read your account. The sidebar then populates with alerts.

## Install the AWS Startup Advisor skills in other coding agents (npx)
<a name="getting-started-npx"></a>

For agents beyond the IDE extension and Claude Code, for example Codex or GitHub Copilot, you can install just the skills with the skills CLI. This path requires Node.js. To download Node.js, see [the Node.js downloads page](https://nodejs.org).

To install the skills, run the following command:

```
npx skills add https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-startup-advisor --skill '*'
```

If you get an npm authentication or registry error, retry against the public registry:

```
npx --registry https://registry.npmjs.org skills add https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-startup-advisor --skill '*'
```

Installing the skills requires no AWS credentials. This path installs the skills, but it does not configure MCP servers. For more information, see [Configure live data with MCP servers (optional)](mcp-servers.md).

## Next steps
<a name="getting-started-next-steps"></a>

How you get the AWS Startup Advisor skills depends on how you installed AWS Startup Advisor:
+  **Claude Code plugin** – The skills are included when you install the plugin. You can start using them right away.
+  **IDE extension (VS Code, Cursor, or Kiro)** – Installing the extension provides alerts and prompts, but not the skills. To add the skills, choose **Install AWS Startup Advisor skills** in the banner that the extension displays. After the skills install, they are available in your coding agent, which invokes them when they are relevant to your request.
+  **Other coding agents (npx)** – The `npx skills add` command installs the skills directly, as described in the previous section.

For more information, see [Using AWS Startup Advisor skills](using-skills.md).