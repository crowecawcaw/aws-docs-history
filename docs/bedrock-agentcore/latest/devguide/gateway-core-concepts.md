# Core concepts for Amazon Bedrock AgentCore

Gateway

Amazon Bedrock AgentCore Gateway provides a standardized way for AI agents to discover and
interact with tools. Understanding the core concepts of Gateway will help you design and
implement effective tool integration strategies for your AI agents.

## Key concepts

**Gateway**

An AgentCore Gateway acts like an MCP server, providing a single access point for an agent to interact with its tools. A Gateway can have multiple targets, each representing a different tool or set of tools.

**Gateway Target**

A target defines the APIs or Lambda function that a Gateway will provide as tools to an agent. Targets can be Lambda functions, OpenAPI specifications, Smithy models, or other tool definitions.

**AgentCore Gateway Authorizer**

Since MCP only supports OAuth, each Gateway must have an attached OAuth authorizer. If you don’t have an OAuth authorization server already, you will be able to create one in this guide using Cognito.

**AgentCore Credential Provider**

When Gateway makes calls to your APIs or Lambda function it must use some credentials to access those functionalities. When you create a Smithy or Lambda target, Gateway uses the attached execution role
to make calls to those targets. When you create an OpenAPI target, you must attach an AgentCore credential provider which stores the API Key or OAuth credentials that Gateway will use to access the OpenAPI target.

## Tool types

Gateway supports several types of tools and integration methods:

**OpenAPI specifications**

Transform existing REST APIs into MCP-compatible tools by providing an OpenAPI
specification. The gateway automatically handles the translation between MCP and REST
formats.

**Lambda functions**

Connect Lambda functions as tools, allowing you to implement custom business logic in
your preferred programming language. The gateway invokes the Lambda function and
translates the response into the MCP format.

**Smithy models**

Use Smithy models to define your API interfaces and generate MCP-compatible tools. Smithy
is a language for defining services and SDKs that can be used with AWS services. The gateway
can use Smithy models to generate tools that interact with AWS services or custom APIs.

**MCP servers**

Use remote MCP servers to connect tools to your agent runtime. Only MCP tools
capabilities are supported. For both control plane and data plane operations, if tools
are not available the operations will fail.
