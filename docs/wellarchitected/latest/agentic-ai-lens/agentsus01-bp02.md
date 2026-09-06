

# AGENTSUS01-BP02 Implement reusable workflow patterns
<a name="agentsus01-bp02"></a>

 When every team rebuilds data retrieval, validation, and transformation workflows from scratch, each rebuild costs development time and pays for its own separate optimization cycle. A library of parameterized patterns shifts that cost into a one-time investment and makes subsequent projects compose from tested building blocks instead of starting over. 

 **Desired outcome:** 
+  You have a catalog of parameterized workflow patterns for recurring agent tasks (retrieval, validation, transformation, and decision-making) that teams can discover and instantiate. 
+  Teams compose new agent systems from existing patterns before writing new implementations. 
+  Each pattern has a documented interface, version history, and declared resource profile, and a single pattern serves many callers through a shared tool layer. 
+  You monitor pattern invocation frequency and failure rates so optimizations to a pattern propagate to every caller. 

 **Common anti-patterns:** 
+  Building single-use workflows for each new project without considering reuse, duplicating effort across teams and accumulating technical debt as similar capabilities are reimplemented with slight variations. 
+  Hardcoding workflow logic and decision points into individual implementations instead of parameterizing them, making reuse of proven patterns impractical. 
+  Developing reusable components without a central catalog or documentation, so teams rebuild workflows that already exist elsewhere in the organization. 
+  Treating workflows as disposable code rather than maintained assets, skipping the testing, documentation, and versioning that keeps patterns usable past their first deployment. 

 **Benefits of establishing this best practice:** 
+  Each new agent project starts from proven, tested building blocks instead of rebuilding from scratch, reducing the redundant development and test cycles that dominate early adoption. 
+  Behavior stays consistent across teams because every caller of a pattern gets the same validated implementation. 
+  A single optimization to a shared pattern improves every caller at once, amortizing future tuning work across the whole fleet. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A pattern only becomes reusable when its parameters, inputs, outputs, and failure modes are explicit. The recurring workflows in agent systems, a retrieval chain with source selection, a validation pipeline with schema checks, and a transformation stage with format conversion, look the same across projects because the shape of the work is the same. The part that varies is narrow. It's which source, which schema, and which format. Making those parameters part of the interface, rather than hardcoding them into each implementation, allows one implementation to serve many callers. 

 Discovery has to work at two different times. At design time, a team evaluating whether to build something new needs to find out what already exists. That is a documentation repository problem. At runtime, an orchestrating agent needs to resolve a capability to a concrete endpoint. That is a registry problem. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes patterns as MCP tools with well-defined interfaces, so runtime discovery is built in. The design-time catalog (a wiki page, a service catalog, or a README) has to be maintained alongside the registry so teams can browse capabilities, limitations, and resource requirements before writing code. 

 Access controls and versioning keep shared patterns from being forked silently by every team. Apply [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and Gateway policies so pattern usage has a known footprint. Keep pattern versions explicit so consumers can adopt a new version deliberately. Deploy the underlying implementations on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) so each pattern has the same operational baseline. 

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes invocation frequency, execution duration, and failure rates per pattern in Amazon CloudWatch, so owners can tell which patterns are heavily used (and therefore worth investing in) and which are sitting unused (and are probably the wrong abstraction or undiscoverable). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify and extract recurring patterns:** Audit existing agent workflows for repeated sequences and pull each one out into a parameterized template with a documented interface. Common sequences include: 
   +  Retrieval 
   +  Validation 
   +  Transformation 
   +  Decision 

1.  **Deploy patterns as reusable components:** Implement each pattern on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) and publish it through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) as an MCP tool so orchestrating agents can discover and invoke it at runtime. 

1.  **Maintain a design-time catalog:** Keep a documentation repository alongside the Gateway registry where teams can browse the following before writing new code: 
   +  Pattern purpose 
   +  Parameters 
   +  Resource profile 
   +  Usage examples 

1.  **Govern pattern access and versions:** Apply [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and Gateway policies to control who can invoke each pattern, and publish new versions alongside old ones so consumers migrate deliberately. 

1.  **Monitor usage and feed improvements back:** Track the following for each pattern through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html): 
   +  Invocation frequency 
   +  Duration 
   +  Failure rates 

    Use the telemetry to find heavily used patterns worth investing in and stagnant patterns worth retiring. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSUS01-BP01 Design specialized agents with explicit resource boundaries](agentsus01-bp01.html) 
+  [AGENTSUS01-BP03 Optimize resource utilization through shared services](agentsus01-bp03.html) 
+  [SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html) 
+  [OPS11-BP03 Iterate to improve](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_iterate_to_improve.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) 
+  [AWS Step Functions - State machine templates](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-templates.html) 
+  [Strands Agents](https://strandsagents.com/) 
+  [Guidance for Multi-Agent Orchestration on AWS](https://aws.amazon.com/solutions/guidance/multi-agent-orchestration-on-aws/) 

 **Related videos:** 
+  [AWS 2025 - Building AI Agents with Serverless, Strands, and MCP (NTA405)](https://www.youtube.com/watch?v=LwubRSoJcIM) 

 **Related examples:** 
+  [GitHub: aws-samples/aws-stepfunctions-examples](https://github.com/aws-samples/aws-stepfunctions-examples) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 