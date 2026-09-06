

# Appendix A: Best practice reference
<a name="appendix-a"></a>

This appendix provides a complete reference of all best practices defined in the Agentic AI Lens, organized by pillar and focus area.

## Operational excellence
<a name="appendix-a-operational-excellence"></a>

### AGENTOPS01: How do you establish operational practices for agentic AI systems?
<a name="appendix-a-agentops01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS01-BP01](agentops01-bp01.html) | Establish well-defined agent roles, responsibilities, and success criteria | High | 
| [AGENTOPS01-BP02](agentops01-bp02.html) | Design multi-agent handoff procedures with human-in-the-loop escalation | High | 
| [AGENTOPS01-BP03](agentops01-bp03.html) | Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes | High | 

### AGENTOPS02: How do you manage prompt and configuration lifecycle?
<a name="appendix-a-agentops02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS02-BP01](agentops02-bp01.html) | Evolve agent prompts, tool calls, and configurations to reflect evolving business needs | High | 
| [AGENTOPS02-BP02](agentops02-bp02.html) | Implement configuration drift detection and remediation | High | 
| [AGENTOPS02-BP03](agentops02-bp03.html) | Implement agent behavior versioning and rollback capabilities | High | 
| [AGENTOPS02-BP04](agentops02-bp04.html) | Maintain feedback control loops for continuous improvement | Medium | 

### AGENTOPS03: How do you manage agent lifecycle and deployment processes?
<a name="appendix-a-agentops03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS03-BP01](agentops03-bp01.html) | Define an agent lifecycle with clear SME ownership, testing, and governance | High | 
| [AGENTOPS03-BP02](agentops03-bp02.html) | Implement CI/CD pipelines tailored to agentic system deployment (AgentOps) | High | 
| [AGENTOPS03-BP03](agentops03-bp03.html) | Implement agent-specific scaling policies and capacity planning | Medium | 
| [AGENTOPS03-BP04](agentops03-bp04.html) | Implement organizational agent portfolio management and governance at scale | High | 

### AGENTOPS04: How do you establish tool integration and management practices?
<a name="appendix-a-agentops04"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS04-BP01](agentops04-bp01.html) | Implement tool registry and catalog management | Medium | 
| [AGENTOPS04-BP02](agentops04-bp02.html) | Establish standardized tool integration protocols (MCP, A2A) | High | 
| [AGENTOPS04-BP03](agentops04-bp03.html) | Develop fallback behavior and error handling for tool invocations | Medium | 

### AGENTOPS05: How do you implement comprehensive observability and monitoring for agentic systems?
<a name="appendix-a-agentops05"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS05-BP01](agentops05-bp01.html) | Establish end-to-end tracing and telemetry for agent operations | High | 
| [AGENTOPS05-BP02](agentops05-bp02.html) | Monitor agent behavior patterns and detect anomalies | High | 
| [AGENTOPS05-BP03](agentops05-bp03.html) | Implement structured logging and comprehensive audit trails | High | 
| [AGENTOPS05-BP04](agentops05-bp04.html) | Define and track KPIs for agent workflows | Medium | 
| [AGENTOPS05-BP05](agentops05-bp05.html) | Create workflow-specific dashboards for operational health | Medium | 

### AGENTOPS06: How do you implement testing, evaluation, and validation frameworks?
<a name="appendix-a-agentops06"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS06-BP01](agentops06-bp01.html) | Design multi-layered testing frameworks | High | 
| [AGENTOPS06-BP02](agentops06-bp02.html) | Evaluate and track ongoing agent performance | High | 
| [AGENTOPS06-BP03](agentops06-bp03.html) | Establish SME-driven validation and business approval workflows | High | 

### AGENTOPS07: How do you establish operational recovery and consumption monitoring?
<a name="appendix-a-agentops07"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTOPS07-BP01](agentops07-bp01.html) | Implement automated response and recovery mechanisms | High | 
| [AGENTOPS07-BP02](agentops07-bp02.html) | Establish operational knowledge management systems | Medium | 
| [AGENTOPS07-BP03](agentops07-bp03.html) | Augment change management to accommodate technical improvements and business requirements | Medium | 
| [AGENTOPS07-BP04](agentops07-bp04.html) | Implement break-glass operational runbooks | High | 

## Security
<a name="appendix-a-security"></a>

### AGENTSEC01: How do you secure agentic memory and securely manage state between agents?
<a name="appendix-a-agentsec01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC01-BP01](agentsec01-bp01.html) | Implement memory isolation and integrity controls | High | 
| [AGENTSEC01-BP02](agentsec01-bp02.html) | Validate and sanitize memory inputs | High | 
| [AGENTSEC01-BP03](agentsec01-bp03.html) | Monitor for hallucination propagation | Medium | 

### AGENTSEC02: How do you control and secure agent tool usage?
<a name="appendix-a-agentsec02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC02-BP01](agentsec02-bp01.html) | Implement tool authorization | High | 
| [AGENTSEC02-BP02](agentsec02-bp02.html) | Validate tool inputs and outputs | High | 
| [AGENTSEC02-BP03](agentsec02-bp03.html) | Maintain approved tool registry with security assessments | Medium | 

### AGENTSEC03: How do you manage agent identities, permissions, and prevent privilege escalation?
<a name="appendix-a-agentsec03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC03-BP01](agentsec03-bp01.html) | Implement strong authentication for agent identities | High | 
| [AGENTSEC03-BP02](agentsec03-bp02.html) | Separate agent and human user permission | High | 
| [AGENTSEC03-BP03](agentsec03-bp03.html) | Implement least privilege with dynamic boundaries | High | 
| [AGENTSEC03-BP04](agentsec03-bp04.html) | Regular permission audits and access reviews | Medium | 

### AGENTSEC04: How do you support agent goal alignment and prevent manipulation?
<a name="appendix-a-agentsec04"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC04-BP01](agentsec04-bp01.html) | Implement guardrails and alignment controls | High | 
| [AGENTSEC04-BP02](agentsec04-bp02.html) | Human-in-the-loop for critical decisions | High | 

### AGENTSEC05: How do you implement observability and prevent repudiation?
<a name="appendix-a-agentsec05"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC05-BP01](agentsec05-bp01.html) | Implement comprehensive logging and decision artifact storage | High | 
| [AGENTSEC05-BP02](agentsec05-bp02.html) | Implement distributed tracing for agent interactions | Medium | 

### AGENTSEC06: How do you secure multi-agent orchestration and coordination?
<a name="appendix-a-agentsec06"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC06-BP01](agentsec06-bp01.html) | Encrypt and sign inter-agent messages | High | 
| [AGENTSEC06-BP02](agentsec06-bp02.html) | Implement workflow orchestration security controls | High | 
| [AGENTSEC06-BP03](agentsec06-bp03.html) | Establish trust boundaries between agents | High | 
| [AGENTSEC06-BP04](agentsec06-bp04.html) | Monitor and detect coordination anomalies | Medium | 

### AGENTSEC07: How do you protect human oversight from manipulation and detect rogue agents?
<a name="appendix-a-agentsec07"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC07-BP01](agentsec07-bp01.html) | Implement cognitive load management | Medium | 
| [AGENTSEC07-BP02](agentsec07-bp02.html) | Clear confidence indicators and manipulation warnings | Medium | 
| [AGENTSEC07-BP03](agentsec07-bp03.html) | Multiple reviewers for critical operations | Medium | 
| [AGENTSEC07-BP04](agentsec07-bp04.html) | Behavioral anomaly detection and agent containment | High | 
| [AGENTSEC07-BP05](agentsec07-bp05.html) | Regular security assessments and red teaming | Medium | 

### AGENTSEC08: How do you validate and secure agent inputs and outputs?
<a name="appendix-a-agentsec08"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC08-BP01](agentsec08-bp01.html) | Multi-layer input validation and prompt injection defense | High | 
| [AGENTSEC08-BP02](agentsec08-bp02.html) | Output filtering for sensitive information | High | 

### AGENTSEC09: How do you perform vulnerability scanning and penetration testing for agentic AI systems?
<a name="appendix-a-agentsec09"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSEC09-BP01](agentsec09-bp01.html) | Integrate AI-powered vulnerability scanning across the development lifecycle | High | 
| [AGENTSEC09-BP02](agentsec09-bp02.html) | Conduct context-aware penetration testing with multi-agent attack simulation | High | 
| [AGENTSEC09-BP03](agentsec09-bp03.html) | Implement continuous security validation with automated remediation | Medium | 
| [AGENTSEC09-BP04](agentsec09-bp04.html) | Establish scoped and controlled testing environments for agent security assessments | Medium | 
| [AGENTSEC09-BP05](agentsec09-bp05.html) | Implement runtime threat detection, security event correlation, and automated remediation for agents | High | 

## Reliability
<a name="appendix-a-reliability"></a>

### AGENTREL01: How do I develop reliable agentic systems?
<a name="appendix-a-agentrel01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL01-BP01](agentrel01-bp01.html) | Implement a resilient messaging layer | High | 
| [AGENTREL01-BP02](agentrel01-bp02.html) | Establish modular, fault-isolated layers | High | 
| [AGENTREL01-BP03](agentrel01-bp03.html) | Design specialized agents following actor model principles | Medium | 
| [AGENTREL01-BP04](agentrel01-bp04.html) | Standardize communication protocols | Medium | 
| [AGENTREL01-BP05](agentrel01-bp05.html) | Implement adaptive provisioning | Medium | 

### AGENTREL02: How do you develop agentic systems that reliably execute tasks with predictable outcomes?
<a name="appendix-a-agentrel02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL02-BP01](agentrel02-bp01.html) | Design agents for specific and atomic tasks | Medium | 
| [AGENTREL02-BP02](agentrel02-bp02.html) | Limit agent permissions to minimum required access | High | 
| [AGENTREL02-BP03](agentrel02-bp03.html) | Implement behavioral anomaly detection and monitoring | High | 
| [AGENTREL02-BP04](agentrel02-bp04.html) | Develop clear instruction protocols for agents | Medium | 
| [AGENTREL02-BP05](agentrel02-bp05.html) | Establish tiered human oversight and approval workflows | High | 

### AGENTREL03: How do you support agent memory and state remaining reliably accessible throughout the agent lifecycle?
<a name="appendix-a-agentrel03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL03-BP01](agentrel03-bp01.html) | Design an information classification model to identify short-term and long-term memories | Medium | 
| [AGENTREL03-BP02](agentrel03-bp02.html) | Architect fault-tolerant memory stores with redundancy and failover | High | 
| [AGENTREL03-BP03](agentrel03-bp03.html) | Implement comprehensive state management and checkpoint-based recovery | High | 
| [AGENTREL03-BP04](agentrel03-bp04.html) | Implement graceful degradation for memory and state operations | Medium | 

### AGENTREL04: How do you orchestrate multi-agent systems to reliably execute tasks?
<a name="appendix-a-agentrel04"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL04-BP01](agentrel04-bp01.html) | Implement the arbiter agent pattern for coordinated multi-agent systems | High | 
| [AGENTREL04-BP02](agentrel04-bp02.html) | Classify agents with a comprehensive capability taxonomy | Medium | 
| [AGENTREL04-BP03](agentrel04-bp03.html) | Implement fallback mechanisms and graceful degradation for collaborative workflows | High | 
| [AGENTREL04-BP04](agentrel04-bp04.html) | Implement resilient control planes for agent coordination | High | 

### AGENTREL05: How do you implement reliable agent cognition that accesses the right data at the right time?
<a name="appendix-a-agentrel05"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL05-BP01](agentrel05-bp01.html) | Design modular, fault-tolerant agentic reasoning components | Medium | 
| [AGENTREL05-BP02](agentrel05-bp02.html) | Facilitate reliable adaptation through evaluation-driven improvement cycles | Medium | 
| [AGENTREL05-BP03](agentrel05-bp03.html) | Ground agent cognition in real information | High | 

### AGENTREL06: How do agents integrate effectively with existing systems without impacting the reliability of established processes?
<a name="appendix-a-agentrel06"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL06-BP01](agentrel06-bp01.html) | Develop agent-based integrations with existing or legacy systems | Medium | 
| [AGENTREL06-BP02](agentrel06-bp02.html) | Establish fallback mechanisms for legacy system degradation | High | 
| [AGENTREL06-BP03](agentrel06-bp03.html) | Regularly test degraded system performance | Medium | 
| [AGENTREL06-BP04](agentrel06-bp04.html) | Implement idempotent task execution patterns | High | 
| [AGENTREL06-BP05](agentrel06-bp05.html) | Implement dynamic capability toggling | Medium | 

### AGENTREL07: How do fault tolerant agent systems recover?
<a name="appendix-a-agentrel07"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL07-BP01](agentrel07-bp01.html) | Design workflows in stages with incremental recovery | High | 
| [AGENTREL07-BP02](agentrel07-bp02.html) | Enable automatic recovery from agent execution failures | High | 
| [AGENTREL07-BP03](agentrel07-bp03.html) | Implement distributed tracing to track system dependencies and facilitate recovery | High | 

### AGENTREL08: How do agents determine when and where graceful degradation is appropriate?
<a name="appendix-a-agentrel08"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTREL08-BP01](agentrel08-bp01.html) | Establish consistent configuration management practices | Medium | 
| [AGENTREL08-BP02](agentrel08-bp02.html) | Implement agent tracing for telemetry throughout agent processing | High | 
| [AGENTREL08-BP03](agentrel08-bp03.html) | Architect agent systems with resource isolation and contention mitigation | High | 
| [AGENTREL08-BP04](agentrel08-bp04.html) | Track agent memory utilization metrics | Medium | 

## Performance efficiency
<a name="appendix-a-performance-efficiency"></a>

### AGENTPERF01: How do you plan strategically for agent performance and establish measurement practices?
<a name="appendix-a-agentperf01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF01-BP01](agentperf01-bp01.html) | Define performance-aligned success criteria for agent workloads | High | 
| [AGENTPERF01-BP02](agentperf01-bp02.html) | Implement comprehensive performance telemetry | High | 
| [AGENTPERF01-BP03](agentperf01-bp03.html) | Profile end-to-end agent latency and identify optimization targets | High | 

### AGENTPERF02: How do you optimize core agent processing and cognitive pipelines?
<a name="appendix-a-agentperf02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF02-BP01](agentperf02-bp01.html) | Design efficient reasoning pipelines | High | 
| [AGENTPERF02-BP02](agentperf02-bp02.html) | Implement task-appropriate model selection strategies | High | 
| [AGENTPERF02-BP03](agentperf02-bp03.html) | Optimize agent execution paths for reduced latency | High | 
| [AGENTPERF02-BP04](agentperf02-bp04.html) | Optimize streaming responses and time-to-first-token for agent interactions | High | 

### AGENTPERF03: How do you optimize memory management, context windows, and retrieval-augmented generation?
<a name="appendix-a-agentperf03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF03-BP01](agentperf03-bp01.html) | Implement tiered memory management systems | High | 
| [AGENTPERF03-BP02](agentperf03-bp02.html) | Optimize context window utilization and prompt management | High | 
| [AGENTPERF03-BP03](agentperf03-bp03.html) | Optimize RAG retrieval pipelines for latency and precision | High | 
| [AGENTPERF03-BP04](agentperf03-bp04.html) | Establish efficient agent caching and data access patterns | Medium | 
| [AGENTPERF03-BP05](agentperf03-bp05.html) | Implement agentic retrieval patterns for dynamic, agent-driven knowledge access | High | 

### AGENTPERF04: How do you achieve efficient communication and protocol usage across agent interactions?
<a name="appendix-a-agentperf04"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF04-BP01](agentperf04-bp01.html) | Optimize asynchronous message handling patterns | High | 
| [AGENTPERF04-BP02](agentperf04-bp02.html) | Implement efficient protocol-based agent communications | Medium | 
| [AGENTPERF04-BP03](agentperf04-bp03.html) | Design high-performing event-driven integration patterns | Medium | 

### AGENTPERF05: How do you optimize workflow orchestration and multi-agent collaboration for performance?
<a name="appendix-a-agentperf05"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF05-BP01](agentperf05-bp01.html) | Design efficient workflow orchestration patterns | High | 
| [AGENTPERF05-BP02](agentperf05-bp02.html) | Implement optimized multi-agent collaboration models | High | 
| [AGENTPERF05-BP03](agentperf05-bp03.html) | Optimize multi-stage AI pipeline execution | Medium | 
| [AGENTPERF05-BP04](agentperf05-bp04.html) | Implement efficient agent delegation and handoff patterns | Medium | 

### AGENTPERF06: How do you optimize tool integrations and framework usage for agent performance?
<a name="appendix-a-agentperf06"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF06-BP01](agentperf06-bp01.html) | Design optimized tool integration strategies | Medium | 
| [AGENTPERF06-BP02](agentperf06-bp02.html) | Implement efficient tool invocation patterns | Medium | 
| [AGENTPERF06-BP03](agentperf06-bp03.html) | Optimize meta-tool utilization and tool chaining | Low | 

### AGENTPERF07: How do you manage multitenant performance isolation and optimize resource utilization?
<a name="appendix-a-agentperf07"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTPERF07-BP01](agentperf07-bp01.html) | Design efficient multitenant agent deployment models | High | 
| [AGENTPERF07-BP02](agentperf07-bp02.html) | Implement tenant-aware performance isolation and throttling | High | 

## Cost optimization
<a name="appendix-a-cost-optimization"></a>

### AGENTCOST01: How do you optimize agent reasoning and execution costs?
<a name="appendix-a-agentcost01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST01-BP01](agentcost01-bp01.html) | Use the reflection pattern to design efficient agent reasoning loops | Medium | 
| [AGENTCOST01-BP02](agentcost01-bp02.html) | Optimize multi-agent collaboration cost through efficient handoff patterns | High | 
| [AGENTCOST01-BP03](agentcost01-bp03.html) | Implement cost-effective patterns like hybrid supervisor for multi-agent coordination | Medium | 
| [AGENTCOST01-BP04](agentcost01-bp04.html) | Design agent hierarchies and delegation patterns that reduce coordination overhead | Medium | 

### AGENTCOST02: How do you optimize agent model invocation and token consumption costs?
<a name="appendix-a-agentcost02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST02-BP01](agentcost02-bp01.html) | Architect tiered model selection for cost-performance optimization | High | 
| [AGENTCOST02-BP02](agentcost02-bp02.html) | Cost optimize token consumption through efficient prompt engineering | Medium | 
| [AGENTCOST02-BP03](agentcost02-bp03.html) | Use intelligent caching to reduce redundant model invocations | High | 
| [AGENTCOST02-BP04](agentcost02-bp04.html) | Implement model customization for long-term cost reduction | High | 

### AGENTCOST03: How do you manage agent memory and state costs efficiently?
<a name="appendix-a-agentcost03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST03-BP01](agentcost03-bp01.html) | Design cost-effective retrieval systems with tiered memory | Medium | 
| [AGENTCOST03-BP02](agentcost03-bp02.html) | Cost optimize through intelligent compression and pruning of context windows | High | 
| [AGENTCOST03-BP03](agentcost03-bp03.html) | Implement cost-optimized state persistence and lifecycle management | Medium | 

### AGENTCOST04: How do you optimize agent tool invocation?
<a name="appendix-a-agentcost04"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST04-BP01](agentcost04-bp01.html) | Design cost effective tool selection to minimize unnecessary invocations | High | 
| [AGENTCOST04-BP02](agentcost04-bp02.html) | Cost optimize tool serving through serverless and resource sharing | High | 
| [AGENTCOST04-BP03](agentcost04-bp03.html) | Implement intelligent caching and failure handling for tool results | High | 

### AGENTCOST05: How do you implement cost attribution?
<a name="appendix-a-agentcost05"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST05-BP01](agentcost05-bp01.html) | Establish agent-level reasoning cost tracking and attribution | Medium | 
| [AGENTCOST05-BP02](agentcost05-bp02.html) | Implement distributed cost tracing for multi-agent workflows | High | 
| [AGENTCOST05-BP03](agentcost05-bp03.html) | Design tenant-aware cost allocation for AaaS pricing models | High | 
| [AGENTCOST05-BP04](agentcost05-bp04.html) | Create chargeback and ROI reporting | Medium | 

### AGENTCOST06: How do you optimize agent discovery registry and deployment costs?
<a name="appendix-a-agentcost06"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST06-BP01](agentcost06-bp01.html) | Implement lightweight discovery and registry for cost-effective collaboration | Medium | 
| [AGENTCOST06-BP02](agentcost06-bp02.html) | Cost optimize versioning and deployment through efficient artifact management | Medium | 
| [AGENTCOST06-BP03](agentcost06-bp03.html) | Design cost-efficient initialization through warm pools and caching | High | 

### AGENTCOST07: How do you establish agent cost governance and continuous optimization?
<a name="appendix-a-agentcost07"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTCOST07-BP01](agentcost07-bp01.html) | Implement automated cost controls with intelligent cutoffs | High | 
| [AGENTCOST07-BP02](agentcost07-bp02.html) | Establish proactive anomaly detection for agent cost patterns | High | 
| [AGENTCOST07-BP03](agentcost07-bp03.html) | Create systematic optimization feedback loops for continuous improvement | High | 

## Sustainability
<a name="appendix-a-sustainability"></a>

### AGENTSUS01: How do you build sustainable and repeatable frameworks for managing compute, memory, and other shareable agent resources?
<a name="appendix-a-agentsus01"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSUS01-BP01](agentsus01-bp01.html) | Design specialized agents with explicit resource boundaries | High | 
| [AGENTSUS01-BP02](agentsus01-bp02.html) | Implement reusable workflow patterns | Medium | 
| [AGENTSUS01-BP03](agentsus01-bp03.html) | Optimize resource utilization through shared services | Medium | 
| [AGENTSUS01-BP04](agentsus01-bp04.html) | Scale cognitive processing pathways appropriately | High | 
| [AGENTSUS01-BP05](agentsus01-bp05.html) | Adopt specification-driven tasks for frontier agents and long-running workflows | High | 

### AGENTSUS02: How do I establish sustainable frameworks for agent dependencies?
<a name="appendix-a-agentsus02"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSUS02-BP01](agentsus02-bp01.html) | Optimize context management and memory utilization | Medium | 
| [AGENTSUS02-BP02](agentsus02-bp02.html) | Establish efficient agent caching strategies | Medium | 
| [AGENTSUS02-BP03](agentsus02-bp03.html) | Appropriately scale data, networking, and compute dependencies | Medium | 
| [AGENTSUS02-BP04](agentsus02-bp04.html) | Measure and optimize the environmental footprint of agent workloads | Medium | 

### AGENTSUS03: How do I establish durable patterns for agent interactions with users and business processes?
<a name="appendix-a-agentsus03"></a>


| ID | Best practice | Risk | 
| --- | --- | --- | 
| [AGENTSUS03-BP01](agentsus03-bp01.html) | Maintain organizational skills and competencies | High | 
| [AGENTSUS03-BP02](agentsus03-bp02.html) | Build agents to mirror your organizational skills and competencies | Medium | 
| [AGENTSUS03-BP03](agentsus03-bp03.html) | Maintain comprehensive specifications for agents and agentic systems | High | 
| [AGENTSUS03-BP04](agentsus03-bp04.html) | Decommission unused agents and prevent agent sprawl | Medium | 

## Summary
<a name="appendix-a-summary"></a>


**Best practice summary by pillar**  

| Pillar | Questions | Best practices | High Risk | Medium Risk | Low Risk | 
| --- | --- | --- | --- | --- | --- | 
| Operational Excellence | 7 | 26 | 18 | 8 | 0 | 
| Security | 9 | 30 | 19 | 11 | 0 | 
| Reliability | 8 | 33 | 18 | 15 | 0 | 
| Performance Efficiency | 7 | 24 | 16 | 7 | 1 | 
| Cost Optimization | 7 | 24 | 14 | 10 | 0 | 
| Sustainability | 3 | 13 | 5 | 8 | 0 | 
| Total | 41 | 150 | 90 | 59 | 1 | 