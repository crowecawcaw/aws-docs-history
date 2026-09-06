

# Agentic CX designer
<a name="acxd"></a>

Agentic CX designer is a feature within Amazon Connect Customer and works with flows in Connect Customer for delivering AI-powered customer experiences.

You may hear these experiences described as "bots," but in agentic CX designer, we refer to them as conversational applications because they can do more than respond to simple user messages. A conversational application can guide structured workflows, answer questions from trusted knowledge, connect to APIs, reason through multi-step tasks, and escalate to human agents.

Agentic CX designer gives teams one workspace to create conversational experiences that are structured enough for business control and flexible enough for natural AI-powered interaction.

## What you can build
<a name="acxd-what-you-can-build"></a>

With agentic CX designer, you can build conversational AI applications for experiences such as:
+ Customer service automation
+ Appointment scheduling
+ Order lookup and updates
+ Account support
+ Knowledge base Q&A
+ Troubleshooting flows
+ Agentic task completion
+ Human handoff and escalation

These applications can combine deterministic workflow logic with generative AI, integrations, knowledge bases, and guardrails.

## How agentic CX designer works with Connect Customer flows
<a name="acxd-how-it-works-with-connect"></a>

Connect Customer flows provide the customer entry point. Agentic CX designer provides the conversational AI application layer.


| Connect Customer flows | Agentic CX designer | 
| --- | --- | 
| Manages the customer entry point into the experience. | Designs and runs the conversational AI experience. | 
| Handles contact flows, routing, queues, and channel setup. | Handles applications, flows, nodes, prompts, integrations, knowledge bases, guardrails, and analytics. | 
| Routes the customer into the selected agentic CX designer application and environment. | Executes the selected application logic and returns the next response or action. | 
| Supports escalation into the contact center experience. | Determines when and how the conversation should escalate based on the application design. | 

In a typical setup, a customer enters through a Connect Customer flow. That flow uses an Agentic CX block to invoke the selected conversational AI application and deployed environment. Agentic CX designer then handles the conversation experience, including flow routing, user responses, API calls, knowledge retrieval, generative AI behavior, guardrails, and monitoring.

## Build, deploy, observe, and improve
<a name="acxd-lifecycle"></a>

Agentic CX designer brings the full conversational AI lifecycle into one workspace.


| Capability | What it helps you do | 
| --- | --- | 
| Build | Create applications, flows, nodes, prompts, slots, variables, integrations, knowledge bases, and guardrails. | 
| Test | Validate routing, flow behavior, variables, state, tools, and troubleshooting details before deployment. | 
| Deploy | Package application changes into builds and deploy them to the appropriate environment. | 
| Observe | Review conversation history, transcripts, evaluations, analytics, guardrails, and performance after deployment. | 
| Optimize | Use analytics, tags, A/B tests, and conversation review to improve the experience over time. | 

## Core capabilities
<a name="acxd-core-capabilities"></a>

Agentic CX designer helps teams create conversational AI applications with:


| Capability | Description | 
| --- | --- | 
| Visual workflow design | Build structured conversation paths using a no-code Canvas. | 
| Deterministic logic | Guide users through predictable steps, decisions, user choices, API calls, and controlled handoffs. | 
| Generative AI nodes | Generate dynamic responses, classify user intent, transform data, and support more flexible interactions. | 
| Agentic experiences | Use agent nodes to reason through multi-step tasks, call tools, collect information, and complete goals. | 
| Knowledge bases | Ground responses in trusted content. | 
| Integrations and Data requests | Connect conversations to managed services, custom APIs, and external systems. | 
| Guardrails | Apply safety, brand, compliance, and policy controls to user inputs and application outputs. | 
| Testing and debugging | Test applications and flows, inspect event logs, and troubleshoot variables, state, tools, and routing behavior. | 
| Analytics and monitoring | Observe live performance, review transcripts, track tags, analyze flow traversal, and improve deployed applications. | 

## How conversations run
<a name="acxd-how-conversations-run"></a>

At runtime, agentic CX designer orchestrates the conversation between the user, the application, and any connected systems.

During a conversation, agentic CX designer can:

1. Receive a user message or event.

1. Determine the appropriate flow or next step.

1. Maintain conversation state across turns.

1. Collect user inputs through slots and variables.

1. Apply deterministic logic or generative AI behavior.

1. Retrieve information from knowledge bases.

1. Call APIs or managed integrations.

1. Apply guardrails to inputs and outputs.

1. Return the next response, action, or handoff.

1. Record activity for testing, troubleshooting, analytics, and monitoring.

This lets builders create experiences that feel natural to users while still giving teams control over business logic, compliance requirements, and operational behavior.

## Built-in AI and model flexibility
<a name="acxd-built-in-ai"></a>

Agentic CX designer includes built-in generative AI capabilities that can be used across different parts of a conversational application.

Examples include:


| AI capability | Use | 
| --- | --- | 
| Text generation | Create dynamic responses, summaries, reformatted messages, or user-facing explanations. | 
| Intent classification | Route user utterances to the right flow using AI descriptions. | 
| Slot capture | Collect multiple pieces of information naturally, even when users provide details out of order. | 
| Generative conditions | Route conversations based on semantic meaning instead of only exact values. | 
| Data transformation | Filter, map, sort, or reshape information before presenting it to the user. | 
| Agentic reasoning | Let an agent node use tools, knowledge, and user input to complete a multi-step task. | 
| MCP-enabled flows | Allow flows to be used as tools by an agent when structured workflow execution is needed. | 

Teams may use native model capabilities or connect supported model providers through bring-your-own-key configurations, depending on workspace setup and organizational requirements.

## Why use agentic CX designer
<a name="acxd-why-use"></a>

Agentic CX designer helps reduce the need to stitch together separate systems for conversation design, AI behavior, orchestration, testing, deployment, and monitoring.


| Without agentic CX designer | With agentic CX designer | 
| --- | --- | 
| Conversational logic, APIs, AI prompts, testing, and analytics may be spread across several tools. | Builders manage applications, flows, tools, testing, deployment, and monitoring from one workspace. | 
| Changes may require updates across multiple systems. | Updates can be made in the application and deployed through the build and deployment process. | 
| Debugging may require reviewing disconnected logs. | Test chat and debugger details help inspect conversation turns and state. | 
| AI behavior may be difficult to govern consistently. | Guardrails, roles, permissions, audit, and versioning support governance and control. | 
| Multi-step agentic logic may require custom engineering. | Agent nodes and tool-enabled flows support complex task completion. | 
| Performance insights may be fragmented. | Observe, analytics dashboards, conversation history, and In-Canvas analytics support ongoing improvement. | 

## In simple terms
<a name="acxd-in-simple-terms"></a>

Agentic CX designer is where you build and manage the conversational AI application.

Amazon Connect Customer is where the customer enters the experience and where contact center routing, channels, and escalation are handled.

Together, they let teams create conversational AI experiences that can be designed visually, powered by AI and business data, governed with guardrails, deployed into customer channels, and improved using real conversation performance.