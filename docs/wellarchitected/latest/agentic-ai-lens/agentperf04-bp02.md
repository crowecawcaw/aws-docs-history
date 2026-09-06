

# AGENTPERF04-BP02 Implement efficient protocol-based agent communications
<a name="agentperf04-bp02"></a>

 Standardized protocols such as the Model Context Protocol (MCP) and agent-to-agent (A2A) give agents a consistent way to communicate with tools and each other, reducing per-interaction overhead and enabling interoperability. Different protocols have different performance profiles, connection establishment, serialization, streaming, multiplexing, which makes protocol selection a meaningful performance decision for high-frequency agent communication. 

 **Desired outcome:** 
+  You use MCP for tool integration, A2A for agent-to-agent coordination, and streaming protocols for real-time agent-user interactions. 
+  You have protocol overhead minimized through connection reuse and efficient serialization. 
+  You have documented protocol selection guidelines for the organization. 

 **Common anti-patterns:** 
+  Using HTTP or REST APIs with JSON serialization for all agent communications regardless of interaction pattern, paying connection establishment and verbose serialization overhead for high-frequency internal communications. 
+  Implementing custom communication protocols instead of adopting standards like MCP and A2A, creating maintenance burden and blocking interoperability with the broader agent ecosystem. 
+  Establishing new connections for every agent interaction rather than pooling and reusing them, adding unnecessary handshake latency. 

 **Benefits of establishing this best practice:** 
+  Protocol-appropriate connection management reduces per-interaction overhead. 
+  Standard protocols open interoperability with the broader agent ecosystem. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Adopt MCP as the standard protocol for agent-to-tool communication. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes tools as MCP-compatible endpoints that agents discover and invoke through a consistent interface. For agent-to-agent communication, the A2A protocol supported by AgentCore Runtime provides structured inter-agent coordination with agent card discovery, task delegation, and result collection. Frameworks such as Strands Agents and LangGraph provide MCP and A2A support. 

 For real-time agent-user interactions that need streaming, WebSocket connections through [Amazon API Gateway](https://aws.amazon.com/api-gateway/) keep a persistent channel open rather than reestablishing connections per turn. Connection pooling belongs on every protocol path, and protocol-level compression pays off once payloads exceed a few kilobytes. 

 Authentication overhead is part of the protocol performance profile. In complex multi-agent workflows, token validation, credential issuance, and policy evaluation accumulate into a measurable latency contributor. AgentCore Identity provides agent authentication with token caching, and AWS IAM roles for service-to-service authentication remove explicit credential exchange from the critical path. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt MCP for agent-to-tool communications through AgentCore Gateway:** Expose tools as MCP-compatible endpoints through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents discover and invoke tools through a consistent interface. 

1.  **Use A2A protocol through AgentCore Runtime for agent-to-agent coordination:** Use the A2A protocol supported by AgentCore Runtime for agent-to-agent coordination, with agent card discovery, task delegation, and result collection. 

1.  **Implement WebSocket connections through API Gateway for real-time streaming agent-user interactions:** Use WebSocket connections through [Amazon API Gateway](https://aws.amazon.com/api-gateway/) for real-time streaming so the channel stays open rather than reestablishing on each turn. 

1.  **Enable connection pooling and protocol-level compression for all communications:** Pool connections on every protocol path and enable compression once payloads exceed a few kilobytes. 

1.  **Budget for authentication overhead and implement token caching through AgentCore Identity:** Use AgentCore Identity with token caching for agent authentication, and use AWS IAM roles for service-to-service calls so credential exchange isn't on the critical path. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF04-BP01 Optimize asynchronous message handling patterns](agentperf04-bp01.html) 
+  [AGENTPERF06-BP01 Design optimized tool integration strategies](agentperf06-bp01.html) 
+  [AGENTPERF05-BP02 Implement optimized multi-agent collaboration models](agentperf05-bp02.html) 

 **Related documents:** 
+  [Agentic AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html) 
+  [Blog: Open Protocols for Agent Interoperability Part 1: Inter-Agent Communication on MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp) 
+  [Blog: Open Protocols for Agent Interoperability Part 4: Inter-Agent Communication on A2A](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 

 **Related videos:** 
+  [AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8) 
+  [Building Scalable, Self-Orchestrating AI Workflows with A2A and MCP (DEV415)](https://www.youtube.com/watch?v=9O9zZ1lQWiI) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 
+  [LangGraph](https://langchain-ai.github.io/langgraph/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 