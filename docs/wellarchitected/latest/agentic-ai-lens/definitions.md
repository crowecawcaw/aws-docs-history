

# Definitions
<a name="definitions"></a>

This section defines key terms used throughout the AWS Well-Architected Agentic AI Lens. These definitions establish a shared vocabulary for discussing agentic AI architecture and are used consistently across all pillars and best practices.

**Agent**  
An autonomous software system that uses a large language model (LLM) as its reasoning engine to perceive context, plan actions, execute tasks, and adapt its behavior in pursuit of a defined goal. Agents differ from conventional AI applications in their ability to take multi-step actions, invoke external tools, maintain state across interactions, and make decisions without explicit human instruction at each step.

**Agentic AI system**  
A software system composed of one or more agents that collaborate to accomplish complex, multi-step tasks. Agentic AI systems might include single agents with multiple tools, multi-agent architectures where specialized agents collaborate under orchestration, or hybrid systems that combine agentic and conventional software components.

**Agentic RAG**  
A retrieval-augmented generation pattern where the agent actively controls the retrieval process as part of its reasoning loop, deciding when to retrieve, what to retrieve, which retrieval tool to use, and whether the retrieved context is sufficient before proceeding. Unlike standard RAG where retrieval is a static preprocessing step, agentic RAG treats retrieval as a dynamic reasoning action that the agent invokes iteratively based on its evolving understanding of the task. Agentic RAG patterns include iterative retrieval, query decomposition, retrieval sufficiency evaluation, and tool-augmented retrieval.

**Agent cognition**  
The reasoning process by which an agent perceives its context, formulates a plan, selects actions, and evaluates outcomes. Agent cognition is powered by LLM inference and encompasses context retrieval, prompt construction, model inference, output parsing, and action selection.

**Agent memory**  
The mechanisms by which agents store and retrieve information across interactions. Agent memory is typically organized into tiers:  
+ **Short-term (session) memory**: Transient context scoped to the current task or conversation, typically stored in fast in-memory stores with TTL-based expiration.
+ **Long-term (persistent) memory**: Durable knowledge that persists across sessions, including learned preferences, historical outcomes, and domain knowledge.
+ **Episodic memory**: Records of specific past interactions that can be retrieved to inform current decisions.
+ **Semantic memory**: General domain knowledge stored as vector embeddings for semantic retrieval.
+ **Procedural memory**: Learned patterns for task execution that inform how agents approach recurring task types.

**Agent orchestration**  
The coordination of multiple agents or agent components to accomplish a complex task. Orchestration might be implemented by a dedicated orchestrator agent, a workflow engine (such as AWS Step Functions), or a combination of both. Orchestration patterns range from static workflows (fully defined at design time) to dynamic graph orchestration (where the agent's reasoning determines the next step at runtime).

**Agent portfolio**  
The complete set of agents deployed across an organization, managed as organizational assets with tracked ownership, capabilities, dependencies, lifecycle state, cost profiles, and business value. Agent portfolio management enables organizations to help prevent agent sprawl, identify redundancy, manage cross-team dependencies, and make informed decisions about investment, consolidation, and retirement.

**Arbiter agent**  
A specialized orchestration agent that resolves conflicts between specialized agents, manages resource contention, and helps keep the collective behavior of a multi-agent system aligned with the overall task objective.

**Atomic task**  
A discrete, well-defined unit of work that an agent can execute independently with clear inputs, outputs, and success criteria. Atomic tasks are the building blocks of modular agent architectures.

**Automatic cutoff (fail-fast)**  
A reliability pattern that detects when a downstream component is experiencing elevated error rates or latency and temporarily stops requests to that component, allowing it to recover without being overwhelmed. Automatic cutoffs operate in three modes: normal (requests flow), blocked (requests halted after failure threshold), and probing (periodic test requests to detect recovery). Also known as the circuit breaker pattern.

**Capability taxonomy**  
A structured classification of agent capabilities that documents each agent's skills, limitations, resource requirements, and operational constraints. Capability taxonomies enable orchestration systems to make informed routing decisions and implement fallback strategies.

**Context window**  
The maximum amount of text (measured in tokens) that a large language model can process in a single inference call. Context window utilization is a key performance and reliability metric for agent systems, as exceeding the context window causes inference failures.

**Dead-letter queue (DLQ)**  
A message queue that captures messages that fail repeated processing attempts, helping prevent poison-pill messages from blocking healthy workflow execution. DLQs are a critical component of resilient agent messaging architectures.

**Graceful degradation**  
The ability of an agent system to maintain partial functionality when components fail or performance degrades, rather than experiencing complete system failure. Graceful degradation involves detecting degraded conditions, activating fallback behaviors, and communicating reduced capabilities to users.

**Guardrail**  
A control mechanism that constrains agent behavior within defined boundaries. Guardrails might be implemented at the model level (Amazon Bedrock Guardrails), the application level (input/output validation), or the infrastructure level (IAM policies, and network controls).

**Hallucination**  
A phenomenon where a large language model generates plausible-sounding but factually incorrect or fabricated information. Hallucination is a key reliability risk in agentic AI systems, particularly when agents make decisions based on model-generated information rather than retrieved facts.

**Human-in-the-loop (HITL)**  
An operational pattern where human judgment is incorporated into agent workflows at defined decision points. HITL workflows range from notification-only (humans are informed but don't intervene) to approval-required (agents can't proceed without explicit human authorization).

**Idempotency**  
The property of an operation that produces the same result when executed multiple times with the same input. Idempotent operations can be safely retried after failures without risk of duplicate side effects.

**Large language model (LLM)**  
A deep learning model trained on large text corpora that can generate, summarize, translate, and reason about text. LLMs serve as the reasoning engines for AI agents, enabling them to interpret instructions, plan actions, and generate responses.

**Model Context Protocol (MCP)**  
An open standard protocol for connecting AI agents to external tools, data sources, and services. MCP defines a standardized interface for tool discovery, invocation, and result handling that enables agents to interact with a wide range of tools without custom integration code.

**Multi-agent system**  
An architecture in which multiple specialized agents collaborate to accomplish tasks that exceed the capabilities of any single agent. Multi-agent systems might use hierarchical orchestration (supervisor-worker), peer-to-peer coordination, swarm-based collaboration, pipeline processing, dynamic graph orchestration, or hybrid patterns that combine multiple models within a single workflow.

**Orchestrator agent**  
An agent responsible for decomposing complex tasks into subtasks, delegating subtasks to specialized agents, coordinating the flow of information between agents, and synthesizing results into a final output.

**Prompt injection**  
A class of issue in which content in an agent's input attempts to override the agent's system prompt or cause it to perform actions outside its defined scope. Prompt injection is a key security consideration in agentic AI systems that process untrusted input.

**Retrieval-augmented generation (RAG)**  
A technique that enhances LLM outputs by retrieving relevant information from external knowledge sources and including it in the model's context. RAG reduces hallucination rates and improves factual accuracy by grounding model reasoning in retrieved real-world information.

**Saga pattern**  
A distributed transaction pattern that coordinates a sequence of local transactions across multiple services, with compensating transactions defined for each step to enable rollback when downstream steps fail. The saga pattern is commonly used in multi-agent workflows to maintain data consistency across agent boundaries.

**Specialized agent**  
An agent designed to perform a single, well-defined capability with atomic operations. Specialized agents are the building blocks of multi-agent systems, each responsible for one discrete task within the larger workflow.

**Stochasticity**  
The inherent randomness in LLM outputs that causes the same input to produce different outputs across invocations. Stochasticity is a fundamental characteristic of LLM-powered agents that must be accounted for in reliability and testing strategies.

**Swarm**  
A multi-agent collaboration pattern where multiple agents work independently on overlapping aspects of a problem, sharing intermediate findings through a common workspace, without centralized supervision. Swarm patterns are effective for tasks that benefit from parallel exploration of a solution space, diverse perspectives, or emergent problem-solving. Swarm implementations require controls for redundant work prevention, convergence detection, and resource budgets to help prevent unbounded consumption.

**Time-to-first-token (TTFT)**  
The elapsed time between a user submitting a request and receiving the first output token from the agent. TTFT is the primary perceived-performance metric for interactive agent interactions, as users perceive agents with low TTFT as dramatically faster even when total processing time is identical. TTFT is composed of pre-stream latency (input processing, context retrieval, and prompt construction) and inference TTFT (time from model invocation to first generated token).

**Token**  
The basic unit of text processed by large language models. Tokens roughly correspond to word fragments, with approximately 750 words equaling 1,000 tokens. Token consumption is the primary cost driver for LLM-based agent systems.

**Tool**  
A function or API that an agent can invoke to interact with external systems, retrieve information, or perform actions. Tools extend agent capabilities beyond text generation to include web search, database queries, code execution, API calls, and other operations.

**Workflow**  
A structured sequence of agent actions, tool invocations, and decision points that accomplishes a complex task. Workflows might be implemented as Step Functions state machines, agent reasoning loops, or combinations of both.