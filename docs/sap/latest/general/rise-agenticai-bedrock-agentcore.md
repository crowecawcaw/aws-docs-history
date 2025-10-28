# Amazon Bedrock Agentcore

Bedrock AgentCore is a suite of services that enables developers to build, deploy, and operate highly capable AI agents securely and at enterprise scale. It is designed to take on the "undifferentiated heavy lifting" of developing agentic AI, allowing enterprises to move beyond proofs-of-concept and accelerate production deployment. Bedrock AgentCore provides a modular toolkit of services that can be used together or independently to create sophisticated AI agents.

- **Runtime**: A secure, serverless environment for deploying and scaling dynamic AI agents, supporting long-running and asynchronous tasks with complete session isolation.
- **Gateway**: A service that converts existing APIs and AWS Lambda functions into agent-compatible tools with minimal code. It supports tool discovery and secure communication using protocols like Model Context Protocol (MCP).
- **Memory**: Manages both short-term conversational context and long-term memory for agents, enabling more personalized and context-aware interactions without developers managing the underlying infrastructure.
- **Built-in Tools:** Enhances agent capabilities with a Code Interpreter for secure code execution and a Browser Tool for interacting with web applications.
- **Identity**: Provides a secure and scalable identity and access management service specifically for AI agents, integrating with existing identity providers to manage agent permissions.
- **Observability**: Offers tools to trace, debug, and monitor agent performance in production, with comprehensive dashboards powered by Amazon CloudWatch and support for OpenTelemetry.
  Bedrock AgentCore is explicitly designed to be model-agnostic, giving developers the flexibility to work with any foundation models (FMs) they choose, both inside and outside of the Amazon Bedrock ecosystem. These are some the FMs hosted within Bedrock, for full list you can refer to [this documentation](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md") :

- **Anthropic**: The Claude family of models, including the latest Claude models.
- **Meta**: The Llama family of models.
- **Mistral AI**: A range of Mistral models.
- **Amazon**: Amazon’s own models, including the Titan and Nova families.
- **OpenAI**: Selected open-weight models from OpenAI.
- **Other providers**: AI21 Labs, Cohere, DeepSeek, Stability AI, and others.
