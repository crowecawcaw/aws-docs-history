

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Getting Started with the Amazon EKS MCP Server
<a name="eks-mcp-getting-started"></a>

This guide walks you through the steps to set up and use the EKS MCP Server with your AI code assistants. You’ll learn how to configure your environment, connect to the server, and start managing your EKS clusters through natural language interactions.

**Note**  
The Amazon EKS MCP Server is in preview release for Amazon EKS and is subject to change.

## Prerequisites
<a name="_prerequisites"></a>

Before you start, make sure you have performed the following tasks:
+  [Create an AWS account with access to Amazon EKS](https://aws.amazon.com/resources/create-account/) 
+  [Install and configure the AWS CLI with credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) 
+  [Install Python 3.10\+](https://www.python.org/downloads/release/python-3100/) 
+  [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/) 

## Setup
<a name="_setup"></a>

### 1. Verify prerequisites
<a name="_1_verify_prerequisites"></a>

```
# Check that your Python version is 3.10 or higher
python3 --version

# Check uv installation
uv --version

# Verify CLI configuration
aws configure list
```

### 2. Setup IAM permissions
<a name="_2_setup_iam_permissions"></a>

To connect to the EKS MCP server, your [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) must have the following policies attached: ** `eks-mcp:InvokeMcp` ** (required permissions for initialization and retrieving information about available tools), ** `eks-mcp:CallReadOnlyTool` ** (required permissions for usage of read-only tools), and ** `eks-mcp:CallPrivilegedTool` ** (required permissions for usage of full access (write) tools). These `eks-mcp` permissions are included in the read-only and full-access AWS managed policies provided, below.
+ Open the [IAM console](https://console.aws.amazon.com/iam/).
+ In the left navigation pane, choose **Users**, **User groups**, or **Roles** depending on the identity you want to attach the policy to, then the name of the specific user, group, or role.
+ Choose the **Permissions** tab.
+ Choose **Attach policies** (or **Add permissions** if it’s the first time).
+ In the policy list, search for and select the managed policy you want to attach:
+  **Read-only operations**: AmazonEKSMCPReadOnlyAccess
+ Choose **Attach policies** (or **Next** and then **Add permissions** to confirm).

This attaches the policy, and the permissions take effect immediately. You can attach multiple policies to the same identity, and each can contain various permissions. To learn more about these policies, see [AWS managed policies for Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-awsmanpol.html).

### 3. Choose an AI assistant
<a name="_3_choose_an_ai_assistant"></a>

Choose one of the following MCP-compatible AI assistants or any MCP-compatible tool:
+  [Install Amazon Q Developer CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) 
+  [Install Kiro](https://kiro.dev/docs/getting-started/installation/) 
+  [Install Cursor](https://cursor.com/download) 
+  [Install Cline VS Code Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) 

## Step 1: Configure your AI assistant
<a name="_step_1_configure_your_ai_assistant"></a>

Choose from any one of the following options to setup your AI code assistant. Completing this step sets up your AI code assistant to use the MCP Proxy for AWS, which is required for secure, authenticated access to the Amazon EKS MCP Server. This involves adding or editing the MCP configuration file (e.g., `~/.aws/amazonq/mcp.json` for Amazon Q Developer CLI). The proxy acts as a client-side bridge, handling AWS SigV4 authentication using your local AWS credentials and enabling dynamic tool discovery for interacting with backend AWS MCP servers like the EKS MCP Server. To learn more, see the [*MCP Proxy for AWS repository*](https://github.com/aws/mcp-proxy-for-aws).

### Option A: Amazon Q Developer CLI
<a name="_option_a_amazon_q_developer_cli"></a>

The Q Developer CLI provides the most integrated experience with the EKS MCP Server.

#### 1. Locate MCP Configuration File
<a name="_1_locate_mcp_configuration_file"></a>
+  **macOS/Linux**: `~/.aws/q/mcp.json` 
+  **Windows**: `%USERPROFILE%\.aws\q\mcp.json` 

#### 2. Add MCP Server Configuration
<a name="_2_add_mcp_server_configuration"></a>

Create the configuration file if it doesn’t exist. Be sure to replace the region (`{region}`) placeholder with your desired region.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **Security note**: `--read-only` can be used to only allow read-only tool operations.

#### 3. Verify Configuration
<a name="_3_verify_configuration"></a>

Restart Q Developer CLI, then check available tools:

```
q /tools
```

### Option B: Kiro IDE
<a name="_option_b_kiro_ide"></a>

Kiro is an AI-first coding workspace with built-in [MCP support](https://kiro.dev/docs/mcp/).

#### 1. Open Kiro Settings
<a name="_1_open_kiro_settings"></a>
+ Open Kiro
+ Go to **Kiro** → **Settings** and search for "MCP Config"
+ Or press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for "MCP Config"

#### 2. Add MCP Server Configuration
<a name="_2_add_mcp_server_configuration_2"></a>
+ Click "Open Workspace MCP Config" or "Open User MCP Config" to edit the MCP configuration file directly.

Be sure to replace the region (`{region}`) placeholder with your desired region.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **Security note**: `--read-only` can be used to only allow read-only tool operations.

### Option C: Cursor IDE
<a name="_option_c_cursor_ide"></a>

Cursor provides built-in MCP support with a graphical configuration interface.

#### 1. Open Cursor Settings
<a name="_1_open_cursor_settings"></a>
+ Open Cursor
+ Go to **Settings** → **Cursor Settings** → **Tools & MCP** 
+ Or press `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows) and search for "MCP"

#### 2. Add MCP Server Configuration
<a name="_2_add_mcp_server_configuration_3"></a>
+ Click "New MCP Server"

Create the configuration file if it doesn’t exist. Be sure to replace the region (`{region}`) placeholder with your desired region.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **Security note**: `--read-only` can be used to only allow read-only tool operations.

#### 3. Restart Cursor
<a name="_3_restart_cursor"></a>

Close and reopen Cursor for the changes to take effect.

#### 4. Verify in Cursor chat
<a name="_4_verify_in_cursor_chat"></a>

Open the chat panel and try:

```
What EKS MCP tools are available?
```

You should see a list of available EKS management tools.

### Option D: Cline (VS Code Extension)
<a name="_option_d_cline_vs_code_extension"></a>

Cline is a popular VS Code extension that brings AI assistance directly into your editor.

#### 1. Open Cline Settings
<a name="_1_open_cline_settings"></a>
+ Open Cline
+ Press `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows) and search for "MCP"

#### 2. Add MCP Server Configuration
<a name="_2_add_mcp_server_configuration_4"></a>
+ Click "Add Server"
+ Click "Open User Configuration"

Create the configuration file if it doesn’t exist. Be sure to replace the region (`{region}`) placeholder with your desired region.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.{region}.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "default",
        "--region",
        "{region}"
      ]
    }
  }
}
```

 **Security note**: `--read-only` can be used to only allow read-only tool operations.

#### 3. Reload VS Code
<a name="_3_reload_vs_code"></a>

Press `Cmd+Shift+P` / `Ctrl+Shift+P` and select "Developer: Reload Window"

#### 4. Verify configuration
<a name="_4_verify_configuration"></a>

Open Cline and ask:

```
List the available MCP tools for EKS
```

## Step 2: (Optional) Create a "write" policy
<a name="_step_2_optional_create_a_write_policy"></a>

Optionally, you can create a [customer-managed IAM policy](https://docs.aws.amazon.com/privateca/latest/userguide/auth-CustManagedPolicies.html) that provides full access to the Amazon EKS MCP server. This policy grants permissions to use all tools in the EKS MCP server, including both privileged tools that may involve write operations and read-only tools. Note that high-risk permissions (anything with Delete\*, or unrestricted IAM resource) are included in this policy, as they’re required for setup/teardown of the cluster resources in the **manage\_eks\_stacks** tool.

```
aws iam create-policy \
 --policy-name EKSMcpWriteManagementPolicy \
 --policy-document "{\"Version\": \"2012-10-17\", \"Statement\": [{\"Effect\": \"Allow\", \"Action\": [\"eks:DescribeCluster\", \"eks:ListClusters\", \"eks:DescribeNodegroup\", \"eks:ListNodegroups\", \"eks:DescribeAddon\", \"eks:ListAddons\", \"eks:DescribeAccessEntry\", \"eks:ListAccessEntries\", \"eks:DescribeInsight\", \"eks:ListInsights\", \"eks:AccessKubernetesApi\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"eks:CreateCluster\", \"eks:DeleteCluster\", \"eks:CreateAccessEntry\", \"eks:TagResource\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"iam:GetRole\", \"iam:ListRolePolicies\", \"iam:ListAttachedRolePolicies\", \"iam:GetRolePolicy\", \"iam:GetPolicy\", \"iam:GetPolicyVersion\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"iam:TagRole\", \"iam:CreateRole\", \"iam:AttachRolePolicy\", \"iam:PutRolePolicy\", \"iam:DetachRolePolicy\", \"iam:DeleteRole\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"iam:PassRole\"], \"Resource\": \"*\", \"Condition\": {\"StringEquals\": {\"iam:PassedToService\": [\"eks.amazonaws.com\", \"ec2.amazonaws.com\"]}}}, {\"Effect\": \"Allow\", \"Action\": [\"ec2:CreateVpc\", \"ec2:CreateSubnet\", \"ec2:CreateRouteTable\", \"ec2:CreateRoute\", \"ec2:CreateInternetGateway\", \"ec2:CreateNatGateway\", \"ec2:CreateSecurityGroup\", \"ec2:AttachInternetGateway\", \"ec2:AssociateRouteTable\", \"ec2:ModifyVpcAttribute\", \"ec2:ModifySubnetAttribute\", \"ec2:AllocateAddress\", \"ec2:CreateTags\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"ec2:DeleteVpc\", \"ec2:DeleteSubnet\", \"ec2:DisassociateRouteTable\", \"ec2:DeleteRouteTable\", \"ec2:DeleteRoute\", \"ec2:DetachInternetGateway\", \"ec2:DeleteInternetGateway\", \"ec2:DeleteNatGateway\", \"ec2:ReleaseAddress\", \"ec2:DeleteSecurityGroup\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"ec2:DescribeVpcs\", \"ec2:DescribeSubnets\", \"ec2:DescribeRouteTables\", \"ec2:DescribeInternetGateways\", \"ec2:DescribeNatGateways\", \"ec2:DescribeAddresses\", \"ec2:DescribeSecurityGroups\", \"ec2:DescribeAvailabilityZones\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"cloudformation:CreateStack\", \"cloudformation:UpdateStack\", \"cloudformation:DeleteStack\", \"cloudformation:DescribeStacks\", \"cloudformation:TagResource\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"sts:GetCallerIdentity\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"logs:StartQuery\", \"logs:GetQueryResults\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"cloudwatch:GetMetricData\"], \"Resource\": \"*\"}, {\"Effect\": \"Allow\", \"Action\": [\"eks-mcp:*\"], \"Resource\": \"*\"}]}"
```

## Step 3: Verify your setup
<a name="_step_3_verify_your_setup"></a>

### Test connection
<a name="_test_connection"></a>

Ask your AI assistant a simple question to verify the connection:

```
List all EKS clusters in my {aws} account
```

You should see a list of your EKS clusters.

## Step 4: Run your first tasks
<a name="_step_4_run_your_first_tasks"></a>

### Example 1: Explore your clusters
<a name="_example_1_explore_your_clusters"></a>

```
Show me all EKS clusters and their status
What insights does EKS have about my production-cluster?
Show me the VPC configuration for my staging cluster
```

### Example 2: Check Kubernetes resources
<a name="_example_2_check_kubernetes_resources"></a>

```
Get the details of all the kubernetes resources deployed in my EKS cluster
Show me pods that are not in Running state or pods with any restarts
Get the logs from the aws-node daemonset in the last 30 minutes
```

### Example 3: Troubleshoot issues
<a name="_example_3_troubleshoot_issues"></a>

```
Why is my nginx-ingress-controller pod failing to start?
Search the EKS troubleshooting guide for pod networking issues
Show me events related to the failed deployment in the staging namespace
```

### Example 4: Create resources (if "write" mode is enabled)
<a name="_example_4_create_resources_if_write_mode_is_enabled"></a>

```
Create a new EKS cluster named demo-cluster with VPC and Auto Mode
Deploy my containerized app from ECR to the production namespace with 3 replicas
Generate a Kubernetes deployment YAML for my Node.js app running on port 3000
```

## Common configurations
<a name="_common_configurations"></a>

### Scenario 1: Multiple AWS profiles
<a name="scenario_1_multiple_shared_aws_profiles"></a>

If you work with multiple AWS accounts, create separate MCP server configurations.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp-prod": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "production",
        "--region",
        "us-west-2"
      ]
    },
    "eks-mcp-dev": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-east-1.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "development",
        "--region",
        "us-east-1"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp-prod": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "production",
        "--region",
        "us-west-2"
      ]
    },
    "eks-mcp-dev": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.us-east-1.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "development",
        "--region",
        "us-east-1"
      ]
    }
  }
}
```

### Scenario 2: Read-only for production
<a name="_scenario_2_read_only_for_production"></a>

Create a read-only configuration for production environments.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp-prod-readonly": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "production",
        "--region",
        "us-west-2",
        "--read-only"
      ],
      "autoApprove": [
        "list_k8s_resources",
        "get_pod_logs",
        "get_k8s_events"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp-prod-readonly": {
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "production",
        "--region",
        "us-west-2",
        "--read-only"
      ],
      "autoApprove": [
        "list_k8s_resources",
        "get_pod_logs",
        "get_k8s_events"
      ]
    }
  }
}
```

### Scenario 3: Development with full access
<a name="_scenario_3_development_with_full_access"></a>

For development environments with full write access.

 **For Mac/Linux:** 

```
{
  "mcpServers": {
    "eks-mcp-dev-full": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-east-1.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "development",
        "--region",
        "us-east-1"
      ]
    }
  }
}
```

 **For Windows:** 

```
{
  "mcpServers": {
    "eks-mcp-dev-full": {
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://eks-mcp.us-east-1.api.aws/mcp",
        "--service",
        "eks-mcp",
        "--profile",
        "development",
        "--region",
        "us-east-1"
      ]
    }
  }
}
```

## Considerations
<a name="_considerations"></a>

### Security
<a name="_security"></a>

Do not pass secrets or sensitive information via allowed input mechanisms:
+ Do not include secrets or credentials in YAML files applied with apply\_yaml.
+ Do not pass sensitive information directly in the prompt to the model.
+ Do not include secrets in CloudFormation templates or application manifests.
+ Avoid using MCP tools for creating Kubernetes Secrets, as this would require providing the secret data to the model.
+ Avoid logging sensitive information in application logs within Kubernetes pods.

YAML content security:
+ Only use YAML files from trustworthy sources.
+ The server relies on Kubernetes API validation for YAML content and does not perform its own validation.
+ Audit YAML files before applying them to your cluster.

Instead of passing secrets through MCP:
+ Use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) or [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) to store sensitive information.
+ Configure proper Kubernetes RBAC for service accounts.
+ Use IAM roles for service accounts (IRSA) for AWS service access from pods.

Redaction of sensitive data:
+ The EKS MCP Server automatically redacts common patterns for security tokens, certificates, and other sensitive information in tool responses.
+ Redacted values are replaced with `HIDDEN_FOR_SECURITY_REASONS` to avoid accidentally exposing data to the model.
+ This redaction applies to all tool responses including logs, resource descriptions, and configuration data.

## Next up
<a name="_next_up"></a>

For configuration options, see [Amazon EKS MCP Server Configuration Reference](eks-mcp-tool-configurations.md). For a complete list of tools, see [Amazon EKS MCP Server Tools Reference](eks-mcp-tools.md).