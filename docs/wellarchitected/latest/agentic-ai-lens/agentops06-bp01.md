

# AGENTOPS06-BP01 Design multi-layered testing frameworks
<a name="agentops06-bp01"></a>

 Traditional software testing, like exact-match assertions and green-or-red unit tests, can miss important failure modes in agentic systems. A testing pyramid that covers unit, integration, end-to-end tests, and shadow layers helps teams catch behavioral regressions before they reach users. 

 **Desired outcome:** 
+  Agent systems are covered by a testing pyramid that includes unit tests, integration tests, end-to-end tests, and shadow tests in production environments. 
+  Automated testing pipelines run on every code and configuration change, providing rapid feedback on regressions. 
+  Test coverage metrics are tracked and maintained above defined thresholds for all agent capabilities. 
+  Tests use semantic quality assessment rather than exact-match comparison, so non-deterministic outputs don't break the suite. 

 **Common anti-patterns:** 
+  Testing only the happy path without covering edge cases, error conditions, and adversarial inputs. 
+  Relying exclusively on unit tests without integration and end-to-end tests, missing failures that only emerge when components interact with real tools and services. 
+  Treating agent testing as equivalent to traditional software testing without accounting for non-deterministic LLM outputs, using exact string matching instead of semantic equivalence checks. 
+  Running tests only in isolated environments without shadow testing in production, missing environment-specific behaviors that only manifest with real data and traffic patterns. 
+  Failing to maintain test datasets as capabilities evolve, so tests become stale and lose regression-detection value. 

 **Benefits of establishing this best practice:** 
+  A thorough testing framework provides the empirical evidence needed to validate each behavioral iteration, enabling confident deployment. 
+  Standardized testing procedures help validate every change consistently, regardless of who made it or how urgent the timeline. 
+  Semantic evaluation accepts legitimate output variation while still catching regressions. 
+  Shadow testing validates behavioral changes against real traffic without exposing users to the new version. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Four layers cover the testing surface for most agent systems. 

 Unit tests, the base layer, test individual components in isolation: prompt templates, tool invocation logic, memory retrieval, decision routing. LLM responses can be mocked where determinism is needed, so unit tests stay fast and reproducible. 

 Integration tests, the second layer, validate agent-tool and agent-to-agent interactions in a staging environment with real endpoints, which is where many of the interesting failures emerge. 

 End-to-end tests, the third layer, validate complete workflows, and this is where semantic evaluation matters more than exact matching. [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) handle the semantic quality assessment that end-to-end tests need. AgentCore Evaluations' 13 built-in evaluators provide standardized quality gates in CI/CD pipelines (correctness, helpfulness, safety, and tool selection accuracy), so regressions in output quality are detectable without requiring bit-exact comparison. Custom evaluators cover business-specific requirements. 

 Shadow tests, the top layer, run new versions in parallel with production on real traffic using traffic mirroring, comparing outputs without serving the new version's responses. This catches environment-specific behavior that staging can't reproduce. The cost is the infrastructure to run parallel inferences, and the value is catching issues before users ever encounter them. For teams developing agents with Kiro, hooks can trigger test runs on file save and before deployment. 

 Integrate automated testing into CI/CD pipelines so every layer blocks deployment on failure. Maintain test datasets with versioning, and review them regularly to add new use cases and failure modes discovered in production. The pyramid gets stronger over time only if the suite grows with the system. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the four testing layers:** Scope, tooling, and success criteria for unit, integration, end-to-end, and shadow tests. 

1.  **Implement unit and integration tests:** Mock dependencies at the unit layer. Use real staging endpoints for integration tests. 

1.  **Create end-to-end scenarios with semantic evaluation:** Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) for quality assessment rather than exact-match assertions. 

1.  **Add shadow testing with traffic mirroring:** Validate behavioral changes against real-world inputs without exposing users. 

1.  **Integrate tests into CI/CD:** Run the full suite on every commit and block deployment on failures. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS06-BP02 Evaluate and track ongoing agent performance](agentops06-bp02.html) 
+  [AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows](agentops06-bp03.html) 
+  [AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)](agentops03-bp02.html) 
+  [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 
+  [LLM-as-a-judge on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/) 
+  [Evaluate models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) 
+  [Evaluating AI agents for production: A practical guide to Strands Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/) 
+  [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent) 
+  [Kiro Hooks](https://kiro.dev/docs/hooks/) 

 **Related videos:** 
+  [AWS 2025 - Strands Agents Observability, Evaluation, & Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples, Evaluations tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations) 
+  [GitHub: awslabs/amazon-bedrock-agent-samples, RAGAS evaluation](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/ragas_evaluation_bedrock_agents) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation) 
+  [Diving Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 