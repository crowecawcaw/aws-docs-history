

# Supported agents, frameworks, and LLMs
<a name="agent-access-agents-llms"></a>

You choose which agent to use with agent access. You can run a coding agent on your local computer, or build your own agent that runs in the cloud. In both cases, the agent connects to the managed Model Context Protocol (MCP) server and uses it to operate the desktop.

AWS provides a sample agent to help you get started. For the sample code, see [Sample code for WorkSpaces Applications agent access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access) on GitHub.

## Agents and frameworks
<a name="agent-access-agents-llms-agents"></a>

You can use a ready-to-run coding agent, build your own agent with a framework, or build and run an agent with a managed service. The following options work with agent access.


| Option | Examples | 
| --- | --- | 
| Coding agents that run on your local computer | Claude Code, Kiro, Cursor, Codex | 
| Frameworks for building your own agent | LangChain, CrewAI, Strands Agents SDK | 
| Managed services for building and running agents | Amazon Bedrock AgentCore, LangGraph Platform | 

## Large language models
<a name="agent-access-agents-llms-models"></a>

You bring your own large language model. Agent access does not require a specific one and works with any computer-use model. A computer-use model can operate a computer through vision and actions.

Computer-use models are available from multiple providers, including Anthropic, Google Gemini, and OpenAI. Because you select the model, you can match it to your task, cost, and quality needs.