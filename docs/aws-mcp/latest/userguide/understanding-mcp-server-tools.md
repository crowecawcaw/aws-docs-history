# Understanding the MCP Server tools

AWS MCP Server (Preview) provides the following tools to help you complete AWS tasks through natural language interactions.

## AWS Knowledge Tools

- `aws___retrieve_agent_sop` - Retrieve the complete workflow for a specific Agent SOP.
  When called with an SOP name, returns the full step-by-step instructions. When called without
  arguments, provides guidance on using `aws___search_documentation` to discover
  available SOPs.
- `aws___search_documentation` - Search across all AWS documentation, including API references,
  best practices, service guides, and Agent SOPs. Use the topic filter to search Agent SOPs exclusively,
  or see SOPs alongside general knowledge search results. Find relevant information from multiple AWS
  knowledge sources.
- `aws___read_documentation` - Retrieve and convert AWS documentation pages to markdown format
  for easy consumption by AI assistants.
- `aws___recommend` - Get content recommendations for AWS documentation pages based on related
  topics and commonly viewed content.
- `aws___list_regions` - Retrieve a list of all AWS regions, including their
  identifiers and names.
- `aws___get_regional_availability` - Check AWS regional availability information
  for services, features, SDK APIs, and CloudFormation resources.

## AWS API Tools

- `aws___call_aws` - Execute authenticated AWS API calls with proper syntax validation and error handling.
  Supports most of the 15,000+ AWS APIs with automatic credential management.

###### Note

APIs that require filesystem access or stream responses are not reliably supported.

- `aws___suggest_aws_commands` - Get descriptions and syntax help for relevant AWS APIs, including
  newly released APIs that may not be in the AI model's training data.

These tools work together to provide comprehensive AWS task completion: Agent SOPs guide the workflow, knowledge
tools provide current information and best practices, and API tools execute the actual AWS operations with proper
authentication and authorization.
