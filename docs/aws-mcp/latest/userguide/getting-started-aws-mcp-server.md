# Setting up your AWS MCP Server

This section outlines how you can set up your AWS MCP Server.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Set up your AWS MCP Server](#mcp-set-up-process "#mcp-set-up-process")

## Prerequisites

Before you begin, you must ensure that you have set up an AWS account.

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Set up your AWS MCP Server

To set up AWS MCP Server, use the steps in the following sections.

###### Topics

- [Step 1: (If applicable) Remove conflicting MCP servers](#step-1-remove-conflicting-servers "#step-1-remove-conflicting-servers")
- [Step 2: Configure AWS credentials](#step-2-configure-aws-credentials "#step-2-configure-aws-credentials")
- [Step 3: Configure your MCP client](#step-3-configure-mcp-client "#step-3-configure-mcp-client")
- [Step 4: Configure IAM permissions](#step-4-configure-iam "#step-4-configure-iam")
- [Step 5: Test your connection](#step-5-test-connection "#step-5-test-connection")

### Step 1: (If applicable) Remove conflicting MCP servers

If you currently have AWS API MCP Server or AWS Knowledge MCP Server installed, we recommend removing
them before setting up the AWS MCP Server to avoid tool conflicts that can confuse AI agents and reduce performance.

###### To remove existing AWS MCP servers:

1. Open your MCP client configuration file.
2. Remove any entries for these servers:
   - `aws-api-mcp-server`
   - `aws-knowledge-mcp-server`

3. Save the configuration file.
4. Restart your MCP client to apply the changes.

### Step 2: Configure AWS credentials

Before connecting to AWS MCP Server, you need to configure AWS credentials on your local machine.
The server uses these credentials to authenticate your requests.

You can use the SigV4 via Proxy to authenticate the AWS MCP Server. SigV4 via Proxy uses your available
AWS credentials and requires the [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws "https://github.com/aws/mcp-proxy-for-aws").

1. Install the AWS CLI by following the instructions at
   [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Configure your AWS credentials using one of these methods:

###### For users with AWS Management Console credentials (Recommended)

From the AWS CLI, run the following command:

```
aws login
```

###### Note

AWS Management Console credentials means that you have a username and password that allows you to sign in to the
console. To use this method, you need the AWS CLI version `2.32.0` or later.

###### For SSO users

```
aws configure sso
```

Follow the prompts to set up your SSO configuration.

###### For IAM users

```
aws configure
```

Enter your Access Key ID, Secret Access Key, default region, and output format. 3. Test your configuration:

```
aws sts get-caller-identity
```

4. Install uv (if not already installed)

###### On macOS and Linux

```
curl -LsSf https://astral.sh/uv/install.sh | less
```

###### Windows

```
powershell -c "irm https://astral.sh/uv/install.ps1 | more“
```

### Step 3: Configure your MCP client

Set your default AWS Region by adding the `--metadata` parameter with `AWS_REGION`. Without
this setting, all AWS operations default to `us-east-1`.

###### Note

Replace `us-west-2` with your preferred default AWS Region.

**Region behavior:**

- Without `--metadata` and `AWS_REGION`: Operations default to `us-east-1`
- With `--metadata` and `AWS_REGION`: Operations use your specified Region
- In queries: You can override by specifying a Region (example: "list my EC2 instances in eu-west-1")

Amazon Kiro CLI

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "timeout": 100000,
      "transport": "stdio",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

Cursor IDE

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

Claude Desktop

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

### Step 4: Configure IAM permissions

If you're not using an administrator role, you must add specific permissions for AWS MCP Server access.

###### Note

Skip this step if you're using an administrator role.

###### To configure IAM permissions

1. Open the IAM console at https://console.aws.amazon.com/iam/
2. Choose the user or role you configured in Step 2
3. Add this policy to grant AWS MCP Server access:

```
{
   "Version": "2012-10-17",
   "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-mcp:InvokeMCP",
                "aws-mcp:CallReadOnlyTool",
                "aws-mcp:CallReadWriteTool"
            ],
            "Resource": "*"
        }
    ]
}

```

### Step 5: Test your connection

1. Start your MCP client (Kiro CLI, Cursor, Claude Desktop, etc.).
2. Wait for the MCP server to initialize (this may take a few minutes on first connection).
3. Test the connection by asking your AI assistant:

_Example: What AWS Regions are available?_ 4. Verify that tools are loaded by running (in Kiro CLI):

`/tools`

Or to see installed MCP servers:

`/mcp`

You should see tools like `aws___search_documentation` and `retrieve_agent_sop` listed. For
more information about the tools, see [Understanding the MCP Server tools](understanding-mcp-server-tools.md "understanding-mcp-server-tools.md").
