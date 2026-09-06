

# GitHub integration
<a name="github-integration"></a>

With GitHub integration in Amazon Quick, you can manage repositories, create and review pull requests, track issues, and collaborate on code through MCP server connectivity. This integration provides action capabilities for development workflow operations.

## What you can do
<a name="github-integration-capabilities"></a>

GitHub integration provides connector capabilities through MCP server connectivity:
+ Create and manage repositories
+ Create, review, and merge pull requests
+ Track and manage issues
+ Manage branches and commits
+ Review code and provide feedback
+ Manage project boards and milestones

## Available tools
<a name="github-integration-tools"></a>

The GitHub MCP server typically provides these tools:
+ `create_repository` - Create new repositories
+ `get_repository` - Get repository information
+ `list_issues` - List repository issues
+ `create_issue` - Create new issues
+ `create_pull_request` - Create pull requests
+ `list_pull_requests` - List pull requests
+ `get_file_contents` - Read file contents
+ `create_commit` - Create commits
+ `search_repositories` - Search for repositories

**Note**  
The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official GitHub documentation and MCP server repository.

## Setting up GitHub integration
<a name="github-integration-setup"></a>

GitHub integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](mcp-integration.md).

You'll need:
+ GitHub account with appropriate repository permissions
+ Personal access token or GitHub App credentials

## Compatibility
<a name="github-integration-compatibility"></a>

GitHub integration supports:
+ **Chat Agents:** Yes
+ **Flows:** Yes
+ **Knowledge Base:** No