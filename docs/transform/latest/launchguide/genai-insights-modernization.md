# Generative AI insights for modernization pathways

Once organizations have explored or implemented a [modernization pathway](modernization-pathways.md "modernization-pathways.md"), they unlock a new class of opportunities powered by generative AI. Modernized architectures, with clean APIs, event-driven patterns, managed data stores, and containerized workloads, are inherently AI-ready. This page maps the Gen AI insights and use cases that become available as a natural next step along each pathway.

###### Note

**The modernization + AI flywheel:** Agentic AI reduces modernization costs by up to 80% and accelerates transformations 5-80x. Once complete, those modernized workloads become the foundation for Gen AI applications, creating a self-reinforcing cycle where AI enables modernization, and modernization enables more AI.

Source: [Why Agentic AI Marks an Inflection Point for Enterprise Modernization](https://aws.amazon.com/blogs/aws-insights/aws-why-agentic-ai-marks-an-inflection-point-for-enterprise-modernization/ "https://aws.amazon.com/blogs/aws-insights/aws-why-agentic-ai-marks-an-inflection-point-for-enterprise-modernization/"), Dr. Asa Kalavade, VP AWS Migration & Modernization

###### Note

**Key insight:** According to McKinsey, generative AI can reduce cloud migration time by 30-40%. But the real value emerges after migration, when modernized applications become the foundation for intelligent automation, agentic workflows, and data-driven decision-making.

Source: [Accelerating Cloud Migration with AWS Transform and Generative AI](https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/generative-ai/ "https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/generative-ai/")

## How modernization enables Gen AI

| Modernization outcome                  | Gen AI enabler                                                     |
| -------------------------------------- | ------------------------------------------------------------------ |
| Clean, well-documented APIs            | AI agents can safely invoke application functions as tools         |
| Event-driven architectures             | Real-time triggers for AI inference and autonomous actions         |
| Managed databases with structured data | RAG knowledge bases, semantic search, and analytics                |
| Containerized microservices            | Independent scaling of AI inference alongside business logic       |
| Observability and logging              | AI-powered root cause analysis and predictive operations           |
| Open-source frameworks                 | Flexibility to integrate open-weight models and custom fine-tuning |

## Gen AI insights by pathway

### Move to AI: Agentic AI and autonomous workflows

**Prerequisite modernization:** Applications with modular APIs, proper state management, and observability.

Once your portfolio is modernized, you can implement graduated AI capabilities, from basic inference to fully autonomous agents:

| AI maturity level     | Capability                                          | Example                                                                                                                                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Level 1: Inference    | Single-turn predictions and classifications         | [Auto-classify support tickets by urgency](../../../prescriptive-guidance/latest/strategy-accelerate-software-dev-lifecycle-gen-ai/generative-ai-capabilities-ops-maintenance.md "../../../prescriptive-guidance/latest/strategy-accelerate-software-dev-lifecycle-gen-ai/generative-ai-capabilities-ops-maintenance.md") |
| Level 2: RAG-enhanced | Context-aware generation using enterprise knowledge | [Maintenance request routing with contractor matching](modernization-pathways.md "modernization-pathways.md")                                                                                                                                                                                                             |
| Level 3: Agents       | Multi-step reasoning with tool use                  | [Customer onboarding agent that checks eligibility, creates accounts, and schedules follow-ups](https://aws.amazon.com/smart-business/resources-for-smb/agentic-ai-vs-generative-ai/ "https://aws.amazon.com/smart-business/resources-for-smb/agentic-ai-vs-generative-ai/")                                              |
| Level 4: Multi-agent  | Orchestrated teams of specialized agents            | Supply chain optimization with demand forecasting, inventory, and logistics agents working in concert                                                                                                                                                                                                                     |

**Insight from the field:** "By 2028, over 33% of enterprise applications will embed agentic capabilities, up from less than 1% today." (Gartner, cited in [Effectively Building AI Agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/ "https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/"))

### Move to cloud native: Intelligent microservices and event-driven AI

**Prerequisite modernization:** Decomposed services with independent deployment, event buses, and API gateways.

Cloud-native architectures are the ideal substrate for embedding AI into specific business domains without monolithic AI projects:

**Gen AI opportunities unlocked:**

- **Per-service intelligence** - Each microservice can embed its own AI capability (NLU for customer service, anomaly detection for payments, recommendations for product catalog) without coupling AI decisions across the system. (Reference: [Drive hyper-personalized customer experiences with Amazon Personalize and generative AI](https://aws.amazon.com/blogs/machine-learning/drive-hyper-personalized-customer-experiences-with-amazon-personalize-and-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/drive-hyper-personalized-customer-experiences-with-amazon-personalize-and-generative-ai/"))
- **Event-driven inference** - Trigger AI workflows automatically when business events occur (order placed, fraud check, personalized confirmation). (Reference: [Effectively Building AI Agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/ "https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/"))
- **Serverless AI agents** - Deploy autonomous agents that scale to zero when idle and burst on demand. No GPUs required for orchestration. (Reference: [Building Serverless Architectures for Agentic AI on AWS](../../../prescriptive-guidance/latest/agentic-ai-serverless/introduction.md "../../../prescriptive-guidance/latest/agentic-ai-serverless/introduction.md"))
- **Real-time personalization** - Decoupled services can each contribute context to a central personalization engine, enabling hyper-personalized experiences. (Reference: [Drive hyper-personalized customer experiences with Amazon Personalize and generative AI](https://aws.amazon.com/blogs/machine-learning/drive-hyper-personalized-customer-experiences-with-amazon-personalize-and-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/drive-hyper-personalized-customer-experiences-with-amazon-personalize-and-generative-ai/"))

### Move to containers: Scalable AI inference and model serving

**Prerequisite modernization:** Containerized workloads with CI/CD pipelines and managed orchestration.

Containerization creates a consistent packaging model that applies equally well to AI workloads:

**Gen AI opportunities unlocked:**

- **Sidecar AI patterns** - Deploy lightweight inference containers alongside application containers for real-time enrichment (for example, content moderation, sentiment analysis, translation). (Reference: [Optimizing a lift-and-shift for security](https://aws.amazon.com/blogs/architecture/optimizing-a-lift-and-shift-for-security/ "https://aws.amazon.com/blogs/architecture/optimizing-a-lift-and-shift-for-security/"))
- **Custom model hosting** - Run fine-tuned or open-weight models (Llama, Mistral) alongside your application tier for data-sensitive use cases.
- **GPU-accelerated inference** - Use GPU node pools for latency-sensitive generative tasks (image generation, real-time transcription).
- **A/B testing AI models** - Container orchestration enables canary deployments of different model versions, measuring business impact before full rollout.

### Move to managed databases: RAG, semantic search, and data intelligence

**Prerequisite modernization:** Data in managed database services with automated operations.

Managed databases are the fuel for generative AI. They provide the structured and unstructured data that makes AI responses accurate and contextual:

**Gen AI opportunities unlocked:**

- **Enterprise RAG (Retrieval-Augmented Generation)** - Connect knowledge bases directly to your data stores. The system automatically ingests, chunks, embeds, and indexes your data for semantic retrieval. (Reference: [Build generative AI applications with Amazon Aurora and Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/database/build-generative-ai-applications-with-amazon-aurora-and-amazon-bedrock-knowledge-bases/ "https://aws.amazon.com/blogs/database/build-generative-ai-applications-with-amazon-aurora-and-amazon-bedrock-knowledge-bases/"))
- **Natural language queries** - Allow business users to ask questions of databases in plain English. AI translates natural language to SQL and returns formatted answers. (Reference: [Query Amazon Aurora PostgreSQL using Amazon Bedrock Knowledge Bases structured data](https://aws.amazon.com/blogs/machine-learning/query-amazon-aurora-postgresql-using-amazon-bedrock-knowledge-bases-structured-data/ "https://aws.amazon.com/blogs/machine-learning/query-amazon-aurora-postgresql-using-amazon-bedrock-knowledge-bases-structured-data/"))
- **Automated data quality** - Use generative AI to detect anomalies, fill gaps, standardize formats, and generate data documentation automatically.
- **Knowledge graph enrichment** - Extract entities and relationships from unstructured data stored in your databases to build organizational knowledge graphs.

Reference: [How Amazon Bedrock Knowledge Bases work](../../../bedrock/latest/userguide/kb-how-it-works.md "../../../bedrock/latest/userguide/kb-how-it-works.md")

### Move to open source: Flexible model selection and fine-tuning

**Prerequisite modernization:** Applications running on open-source frameworks, databases, and runtimes.

Open-source modernization extends naturally into the AI layer, giving teams maximum control over model selection and customization:

**Gen AI opportunities unlocked:**

- **Open-weight model deployment** - Host models like Meta Llama, Mistral, or DeepSeek for full control over inference without vendor lock-in.
- **Domain-specific fine-tuning** - Fine-tune open models on your proprietary data for industry-specific accuracy (legal, medical, financial terminology). (Reference: [Automate fine-tuning of Llama 3.x models with Amazon SageMaker Pipelines](https://aws.amazon.com/blogs/machine-learning/automate-fine-tuning-of-llama-3-x-models-with-the-new-visual-designer-for-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/automate-fine-tuning-of-llama-3-x-models-with-the-new-visual-designer-for-amazon-sagemaker-pipelines/"))
- **Cost optimization** - Use smaller, specialized open models for routine tasks (classification, extraction) and reserve larger models for complex generation tasks.
- **Community-driven innovation** - Leverage open-source AI frameworks (LangChain, Strands Agents SDK, LlamaIndex) that integrate seamlessly with open-source application stacks. (Reference: [Effectively Building AI Agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/ "https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/"))

### Move to modern analytics: Generative BI and predictive insights

**Prerequisite modernization:** Analytics workloads on modern data platforms with clean data pipelines.

Modern analytics architectures create the data foundation for generative BI, where AI doesn't just report on the past but predicts the future and recommends actions:

**Gen AI opportunities unlocked:**

- **Natural language analytics** - Business users ask questions in plain language and receive charts, summaries, and insights without writing SQL or building dashboards. (Reference: [Pioneering Generative AI for Business Intelligence with Amazon Q in QuickSight](https://aws.amazon.com/careers/life-at-aws-inside-the-role-pioneering-generative-ai-for-business-intelligence-with-amazon-q-in-quicksight/ "https://aws.amazon.com/careers/life-at-aws-inside-the-role-pioneering-generative-ai-for-business-intelligence-with-amazon-q-in-quicksight/"))
- **Automated narrative generation** - Generate executive summaries, trend explanations, and anomaly reports automatically from analytics outputs.
- **Predictive recommendations** - Move from descriptive ("what happened") to prescriptive ("what should we do") by combining analytics data with LLM reasoning.
- **Data storytelling** - AI generates contextual narratives around data changes, helping non-technical stakeholders understand trends and make decisions.

### Move to modern DevOps: AI-powered operations and developer productivity

**Prerequisite modernization:** CI/CD pipelines, infrastructure as code, observability, and automated testing.

Modern DevOps practices create the automation backbone that generative AI can supercharge:

**Gen AI opportunities unlocked:**

- **Autonomous incident investigation (AWS DevOps Agent)** - A frontier AI agent that autonomously investigates production issues the moment they occur. It correlates telemetry, code, and deployment data to identify root cause, completing investigations in under 5 minutes without human intervention. (Reference: [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/ "https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/"))
- **Code generation and review** - AI-powered development assistants accelerate development with context-aware code suggestions, test generation, and security scanning.
- **Proactive incident prevention** - AWS DevOps Agent analyzes patterns across historical incidents to deliver targeted improvements across observability, infrastructure optimization, deployment pipelines, and application resilience.
- **Release readiness review** - AI reviews code changes during generation, checking policy compliance, dependency impacts, blast radius, and access controls before merge.
- **Autonomous release testing** - Generates and runs change-specific test plans targeting risk areas, catching regressions and integration failures before production.
- **Shift-left security** - Generative AI scans code, infrastructure templates, and configurations for vulnerabilities during development rather than after deployment.

**AWS DevOps Agent, key capabilities:**

| Area                         | Capability                       | How it works                                                                                                             |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Production operations        | Automated incident investigation | Begins investigating immediately from alerts/tickets; correlates telemetry, code, and deployments to identify root cause |
| Production operations        | Actionable mitigation plans      | Provides specific actions to resolve incidents; generates agent-ready instructions for implementation by tools like Kiro |
| Production operations        | Proactive prevention             | Analyzes incident patterns to recommend observability, infra, pipeline, and resilience improvements                      |
| Production operations        | Incident coordination            | Routes findings through Slack, ServiceNow, PagerDuty; creates support cases with full investigation context              |
| Production operations        | On-demand SRE tasks              | Handles SRE queries via natural language: resource health, incident patterns, deployment tracking                        |
| Release management (preview) | Release readiness review         | Reviews code changes for policy compliance, cross-repo dependencies, blast radius, and permission escalation             |
| Release management (preview) | Autonomous release testing       | Generates and runs change-specific test plans in customer environments, targeting risk areas surfaced in review          |
| Release management (preview) | Developer workflow integration   | Delivers results through PRs, coding agent IDEs, and CI/CD pipelines                                                     |

**Real-world example:** A monitoring alarm triggers due to elevated 5xx errors. AWS DevOps Agent autonomously tests hypotheses, identifies database write throttling from a recent deployment, and posts root cause analysis with mitigation recommendations to Slack, all in under 5 minutes from alarm to actionable solution. (Reference: [Resolve Application Issues Autonomously with AWS DevOps Agent and Dynatrace](https://aws.amazon.com/blogs/mt/resolve-application-issues-autonomously-with-aws-devops-agent-and-dynatrace/ "https://aws.amazon.com/blogs/mt/resolve-application-issues-autonomously-with-aws-devops-agent-and-dynatrace/"))

**References:**

- [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/ "https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/")
- [Resolve Application Issues Autonomously with AWS DevOps Agent and Dynatrace](https://aws.amazon.com/blogs/mt/resolve-application-issues-autonomously-with-aws-devops-agent-and-dynatrace/ "https://aws.amazon.com/blogs/mt/resolve-application-issues-autonomously-with-aws-devops-agent-and-dynatrace/")
- [Generative AI-powered Technology Operations](https://aws.amazon.com/blogs/machine-learning/generative-ai-powered-technology-operations/ "https://aws.amazon.com/blogs/machine-learning/generative-ai-powered-technology-operations/")

## Summary

Modernization is not the end state. It is the launchpad for generative AI. Each pathway creates specific architectural preconditions that make AI integration natural, safe, and cost-effective:

| Pathway                   | AI unlock                                       |
| ------------------------- | ----------------------------------------------- |
| Move to AI                | Agentic workflows and autonomous agents         |
| Move to cloud native      | Event-driven, per-service intelligence          |
| Move to containers        | Scalable model serving and sidecar inference    |
| Move to managed databases | Enterprise RAG and natural language data access |
| Move to open source       | Flexible model selection and domain fine-tuning |
| Move to modern analytics  | Generative BI and predictive insights           |
| Move to modern DevOps     | AI-powered operations and self-healing systems  |

Organizations that have completed modernization are uniquely positioned to embed AI into their operations, not as a separate initiative, but as a natural extension of the architecture they have already built.

For more information, contact your AWS account team.
