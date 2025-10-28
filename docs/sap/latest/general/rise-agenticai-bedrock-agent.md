# Amazon Bedrock Agent

Amazon Bedrock Agent acts as the intelligent orchestrator that uses the reason-and-act (ReAct) pattern to fulfil complex user requests. It uses the reasoning of foundation models (FMs), APIs, and data to break down user requests, gathers relevant information, and efficiently completes tasks—freeing teams to focus on high-value work. You can refer to [this link](../../../bedrock/latest/userguide/agents-how.md "../../../bedrock/latest/userguide/agents-how.md") on how to implement Amazon Bedrock Agent.

- **User request**: The process begins with a natural language request from a user, such as "Generate a sales report and share it with the finance team".
- **Reasoning and planning**: The Bedrock Agent’s orchestration prompt and the underlying FM interpret the request and break it down into logical, multi-step actions.
- **Tool execution**: The agent executes the plan by invoking "tools"—action groups that are defined with API schemas. These tools can call backend services within the SAP system via the Generative AI Hub. For example, the agent might:

      + **Call an API** to fetch sales data from SAP
      + **Access a knowledge base** in Bedrock via a Retrieval Augmented Generation (RAG) tool to pull relevant business documents.
      + **Leverage code interpreter or browser** in AgentCore for data analysis or to interact with a web-based SAP User Interface.
      + **Utilize memory** to maintain context across multiple user interactions. This is essential for multi-step processes like filling out a complex purchase order over several turns of conversation.

  Bedrock Agents fully supports multi-agent collaboration, allowing you to build and deploy systems of specialized AI agents that work together to accomplish complex, multi-step workflows. Instead of a single agent attempting to handle every part of a difficult task, a team of agents can be orchestrated to contribute their specific expertise, improving efficiency, accuracy, and overall performance. The core of [multi-agent collaboration in Bedrock](../../../bedrock/latest/userguide/agents-multi-agent-collaboration.md "../../../bedrock/latest/userguide/agents-multi-agent-collaboration.md") is a hierarchical model consisting of a supervisor agent and one or more collaborator agents.
