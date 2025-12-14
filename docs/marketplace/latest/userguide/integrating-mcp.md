# Integrating MCP

AWS MCP Server (MCP) is an open standard that enables seamless communication between AI agents and external tools. When you implement MCP in your AI agent or tool, customers can integrate your solution directly into their existing agentic workflows without complex API integration work.

MCP transforms how AI agents access external capabilities. Instead of building custom integrations for each tool, agents use a standardized protocol to discover, connect, and interact with MCP-compatible services. This approach reduces integration complexity and enables plug-and-play functionality.

For more information about implementing AWS MCP Server in your agent or tool, see Integrating MCP.

###### Topics

- [Key Benefits of AWS MCP Server integration](#mcp-benefits "#mcp-benefits")
- [AWS MCP Server Architecture and components](#mcp-architecture "#mcp-architecture")
- [Technical requirements for AWS MCP Server implementation](#mcp-implementation "#mcp-implementation")
- [Testing and validation](#mcp-testing "#mcp-testing")
- [Documentation requirements](#mcp-documentation "#mcp-documentation")
- [Additional resources](#mcp-resources "#mcp-resources")

## Key Benefits of AWS MCP Server integration

MCP integration provides advantages for both AI agent providers and end users.

### Benefits for AI agent providers

- Reach customers using popular AI development solutions that support MCP.
- Reduce customer onboarding friction with standardized integration.
- Enable discovery through MCP-compatible client applications.
- Support multiple client platforms with a single implementation.

### Benefits for end users

- Add your capabilities to existing AI workflows without custom development.
- Use familiar AWS MCP Server client interfaces they already know.
- Benefit from automatic protocol handling and error management.
- Access your tools through multiple AI platforms and applications.
- Maintain consistent authentication across AWS MCP Server-enabled services.

## AWS MCP Server Architecture and components

AWS MCP Server uses a client-server architecture where your AI agent or tool acts as an AWS MCP Server server. Customer applications (AWS MCP Server clients) connect to your server to access your capabilities.

The protocol defines the following three main types of capabilities:

- **Tools** – Functions that agents can call to perform actions.
- **Resources** – Data sources that agents can read or query.
- **Prompts** – Pre-defined prompt templates that agents can use.

## Technical requirements for AWS MCP Server implementation

Your AWS MCP Server server must implement the following core protocol specifications:

- JSON-RPC 2.0 communication protocol
- Standard AWS MCP Server message types and formats
- Capability advertisement and discovery
- Authentication and session management
- Error handling and status reporting

### Implementation steps

1. Define your capabilities (tools, resources, or prompts).
2. Implement the AWS MCP Server server interface.
3. Create capability schemas using JSON Schema.
4. Implement authentication and authorization.
5. Add error handling and logging.
6. Test with AWS MCP Server-compatible clients.
7. Document your capabilities for customers.

### Example capability definition

```
{
  "name": "search_knowledge_base",
  "description": "Search the knowledge base for relevant information",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query"
      },
      "max_results": {
        "type": "integer",
        "description": "Maximum number of results to return",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

## Testing and validation

Before listing your AWS MCP Server-compatible agent or tool on AWS Marketplace, thoroughly test your implementation:

- Verify capability discovery and schema validation
- Test authentication flows and error handling
- Validate performance under various load conditions
- Ensure compatibility with popular AWS MCP Server clients
- Document any client-specific configuration requirements

## Documentation requirements

When listing an AWS MCP Server-compatible agent or tool on AWS Marketplace, include comprehensive documentation:

- Detailed capability descriptions and examples
- Authentication and configuration instructions
- Sample code for common integration scenarios
- Troubleshooting guides and error reference
- Performance considerations and best practices

## Additional resources

For more information about implementing AWS MCP Server in your AI agent or tool, refer to these resources:

- [Model Context Protocol Specification](https://modelcontextprotocol.github.io/ "https://modelcontextprotocol.github.io/")
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/mcp "https://github.com/modelcontextprotocol/mcp")
- [AWS Marketplace Seller Operations team](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") for AWS MCP Server integration support
