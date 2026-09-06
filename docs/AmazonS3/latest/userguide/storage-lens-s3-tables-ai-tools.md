

# Using AI assistants with S3 Storage Lens tables
<a name="storage-lens-s3-tables-ai-tools"></a>

You can use AI assistants and conversational AI tools to interact with your S3 Storage Lens data exported to S3 Tables using natural language. By leveraging the Model Context Protocol (MCP) and the MCP Server for Amazon S3 Tables, you can query, analyze, and gain insights from your storage data without writing SQL queries.

## Overview
<a name="storage-lens-s3-tables-ai-tools-overview"></a>

Model Context Protocol (MCP) is a standardized way for AI applications to access and utilize contextual information. The MCP Server for Amazon S3 Tables provides tools that enable AI assistants to interact with your S3 Tables data using natural language interfaces. This democratizes data access and enables individuals across technical skill levels to work with S3 Storage Lens metrics.

With the MCP Server for S3 Tables, you can use natural language to:
+ List S3 table buckets, namespaces, and tables
+ Query S3 Storage Lens metrics and get insights
+ Analyze storage trends and patterns
+ Identify cost optimization opportunities
+ Generate reports and visualizations

## Supported AI assistants
<a name="storage-lens-s3-tables-ai-tools-supported"></a>

The MCP Server for S3 Tables works with various AI assistants that support the Model Context Protocol, including:
+ **Kiro** - An AI coding assistant with built-in MCP support
+ **Amazon Q Developer** - AWS's AI-powered assistant for developers
+ **Cline** - An AI coding assistant with MCP integration
+ **Claude Desktop** - Anthropic's desktop application with MCP support
+ **Cursor** - An AI-powered code editor

**Important**  
AI-generated SQL queries and recommendations should be reviewed and validated before use. Verify that queries are appropriate for your data structure, use case, and performance requirements. Always test recommendations in a non-production environment before implementing them in production.

## Setting up Kiro with S3 Storage Lens tables
<a name="storage-lens-s3-tables-ai-tools-kiro-setup"></a>

Kiro is an AI coding assistant that provides seamless integration with S3 Tables through the MCP Server. Kiro can help you install and configure the MCP Server directly through its interface, simplifying the setup process.

For more information about Kiro, see [Kiro AI](https://kiro.ai/).

### Prerequisites
<a name="storage-lens-s3-tables-ai-tools-kiro-prerequisites"></a>

Before you begin, ensure that you have:
+ Kiro installed on your system. Download from [https://kiro.ai/](https://kiro.ai/)
+ AWS CLI configured with appropriate credentials
+ An S3 Storage Lens configuration with S3 Tables export enabled
+ Permissions to query S3 Tables. For more information, see [Permissions for S3 Storage Lens tables](storage-lens-s3-tables-permissions.md).

### Step 1: Install the S3 Tables MCP Server
<a name="storage-lens-s3-tables-ai-tools-kiro-step1"></a>

You can install the S3 Tables MCP Server in two ways:

**Option 1: Using Kiro's built-in MCP server management**  
Kiro can help you discover and install MCP servers directly through its interface:

1. Open Kiro

1. Access the MCP server management interface (typically through settings or command palette)

1. Search for "S3 Tables" or "awslabs.s3-tables-mcp-server"

1. Follow Kiro's prompts to install and configure the server

**Option 2: Manual installation using uvx**  
Alternatively, you can manually install the MCP Server using `uvx`, a Python package runner:

```
uvx awslabs.s3-tables-mcp-server@latest
```

For more information about installing the MCP Server, see the [AWS S3 Tables MCP Server documentation](https://awslabs.github.io/mcp/servers/s3-tables-mcp-server).

### Step 2: Configure Kiro MCP settings
<a name="storage-lens-s3-tables-ai-tools-kiro-step2"></a>

Create or update your Kiro MCP configuration file at `~/.kiro/settings/mcp.json` with the following content:

```
{
  "mcpServers": {
    "awslabs.s3-tables-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.s3-tables-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

Replace `your-aws-profile` with your AWS CLI profile name and `us-east-1` with your AWS Region.

### Step 3: Verify the configuration
<a name="storage-lens-s3-tables-ai-tools-kiro-step3"></a>

After configuring the MCP Server, restart Kiro and verify that the S3 Tables tools are available. You can check the available MCP servers in Kiro's settings or by asking Kiro to list available tools.

## Example use cases with AI assistants
<a name="storage-lens-s3-tables-ai-tools-examples"></a>

The following examples demonstrate how to use natural language prompts with AI assistants to interact with S3 Storage Lens data.

### Example 1: Query top storage consumers
<a name="storage-lens-s3-tables-ai-tools-examples-consumers"></a>

**Prompt:** "Show me the top 10 buckets by storage consumption from my S3 Storage Lens data."

The AI assistant will use the MCP Server to query your S3 Storage Lens tables and return the results, including bucket names, storage classes, and storage amounts.

### Example 2: Analyze storage growth
<a name="storage-lens-s3-tables-ai-tools-examples-growth"></a>

**Prompt:** "Analyze my storage growth over the last 30 days and show me the trend."

The AI assistant will query the storage metrics table, calculate daily storage totals, and present the growth trend.

### Example 3: Identify cost optimization opportunities
<a name="storage-lens-s3-tables-ai-tools-examples-optimization"></a>

**Prompt:** "Find buckets with incomplete multipart uploads older than 7 days that are wasting storage."

The AI assistant will query the storage metrics table for incomplete multipart uploads and provide a list of buckets with potential cost savings.

### Example 4: Find cold data candidates
<a name="storage-lens-s3-tables-ai-tools-examples-cold-data"></a>

**Prompt:** "Identify prefixes with no activity in the last 100 days that are stored in hot storage tiers."

The AI assistant will analyze both storage and activity metrics to identify data that could be moved to colder storage tiers for cost optimization.

### Example 5: Generate storage reports
<a name="storage-lens-s3-tables-ai-tools-examples-reports"></a>

**Prompt:** "Create a summary report of my S3 storage showing total storage, object counts, and request patterns for the last week."

The AI assistant will query multiple tables, aggregate the data, and generate a comprehensive report.

## Best practices for using AI assistants
<a name="storage-lens-s3-tables-ai-tools-best-practices"></a>

Follow these best practices when using AI assistants with S3 Storage Lens data:
+ **Be specific in your prompts** - Provide clear, specific instructions about what data you want to analyze and what insights you're looking for.
+ **Verify AI-generated queries** - Always review and validate the SQL queries and recommendations that the AI assistant generates before executing them or taking action. AI assistants may occasionally produce incorrect queries or recommendations that need to be verified against your specific use case and data.
+ **Use appropriate permissions** - Ensure that the IAM credentials used by the AI assistant have only the necessary permissions. For read-only analysis, grant only SELECT permissions.
+ **Monitor usage** - Track the queries executed by AI assistants using AWS CloudTrail to maintain audit trails.
+ **Start with simple queries** - Begin with straightforward queries to understand how the AI assistant interprets your prompts, then progress to more complex analysis.

## Logging and traceability
<a name="storage-lens-s3-tables-ai-tools-logging"></a>

When using the S3 Tables MCP Server with AI assistants, you have multiple ways to audit operations:
+ **Local logs** - The MCP Server logs requests and responses locally. You can specify a log directory using the `--log-dir` configuration option.
+ **AWS CloudTrail** - All S3 Tables operations via the MCP Server using PyIceberg will have `awslabs/mcp/s3-tables-mcp-server/<version>` as the user agent string. You can filter CloudTrail logs by this user agent to trace actions performed by AI assistants.
+ **AI assistant history** - AI assistants like Kiro and Cline maintain history logs that record natural language requests, LLM responses, and instructions provided to the MCP Server.

## Security considerations
<a name="storage-lens-s3-tables-ai-tools-security"></a>

When using AI assistants with S3 Storage Lens data, follow these security best practices:
+ **Use least privilege access** - Grant AI assistants only the minimum permissions required for their tasks.
+ **Enable MFA** - Use multi-factor authentication for AWS accounts that AI assistants access.
+ **Review permissions regularly** - Periodically audit the permissions granted to AI assistants and revoke unnecessary access.
+ **Use separate credentials** - Consider using separate AWS credentials for AI assistant access to facilitate tracking and auditing.
+ **Avoid sharing sensitive data** - Be cautious about sharing sensitive information in prompts to AI assistants, especially when using cloud-based AI services.

## Troubleshooting
<a name="storage-lens-s3-tables-ai-tools-troubleshooting"></a>

### AI assistant cannot connect to S3 Tables
<a name="storage-lens-s3-tables-ai-tools-troubleshooting-connection"></a>

**Problem:** The AI assistant reports that it cannot connect to S3 Tables or the MCP Server is not responding.

**Solution:**
+ Verify that the MCP Server is correctly installed using `uvx awslabs.s3-tables-mcp-server@latest --version`
+ Check that your AWS credentials are configured correctly
+ Ensure that the MCP configuration file has the correct AWS profile and region

### Access denied errors
<a name="storage-lens-s3-tables-ai-tools-troubleshooting-access"></a>

**Problem:** The AI assistant receives access denied errors when querying S3 Storage Lens tables.

**Solution:**
+ Verify that analytics integration is enabled on the `aws-s3` table bucket
+ Check that Lake Formation permissions are correctly configured
+ Ensure that the AWS credentials have the necessary IAM permissions

### Incorrect or unexpected results
<a name="storage-lens-s3-tables-ai-tools-troubleshooting-results"></a>

**Problem:** The AI assistant returns incorrect or unexpected results.

**Solution:**
+ Review the SQL query generated by the AI assistant
+ Verify that you're using the correct namespace name for your Storage Lens configuration
+ Check that data is available by querying the latest report\_time
+ Refine your prompt to be more specific about what you want to analyze

## Additional resources
<a name="storage-lens-s3-tables-ai-tools-resources"></a>

For more information about using AI assistants with S3 Tables, see the following resources:
+ [Kiro AI](https://kiro.ai/) - AI coding assistant with built-in MCP support
+ [Implementing conversational AI for S3 Tables using Model Context Protocol (MCP)](https://aws.amazon.com/blogs/storage/implementing-conversational-ai-for-s3-tables-using-model-context-protocol-mcp/) - AWS Storage Blog
+ [AWS S3 Tables MCP Server documentation](https://awslabs.github.io/mcp/servers/s3-tables-mcp-server)
+ [Model Context Protocol specification](https://modelcontextprotocol.io/)