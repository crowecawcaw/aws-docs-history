

# Using AWS Startup Advisor skills
<a name="using-skills"></a>

 AWS Startup Advisor bundles 11 skills that a coding agent uses. The same skills are available across the supported agents, so you get the same guidance no matter which agent you use. The skills fall into three groups: skills that help you start and grow on AWS, skills that build AI agents on AWS, and skills that migrate workloads to AWS.

To use a skill, prompt your coding agent with what you want to do. Each skill in the following sections includes an example prompt.

**Topics**
+ [Start and grow on AWS](#using-skills-start-grow)
+ [Build AI agents on AWS](#using-skills-agents)
+ [Migrate to AWS](#using-skills-migrate)

## Start and grow on AWS
<a name="using-skills-start-grow"></a>

This group scaffolds new projects, tailors architecture guidance to your stage, and provides reference material and prompts.

### start-building-for-startups
<a name="skill-start-building"></a>

The `start-building-for-startups` skill is an interactive discovery workflow. It scans your codebase, asks about your goals and constraints through picker questions, and then writes an AWS architectural scaffold directly into your project.

 **Example prompt**: "Scaffold a serverless API for my startup."

### architect-for-startups
<a name="skill-architect"></a>

The `architect-for-startups` skill provides stage-aware AWS architecture guidance. It adjusts recommendations based on your startup stage (pre-revenue, seed, Series A, or Series B and later), team size, runway, and timeline.

 **Example prompt**: "Recommend an architecture for my seed-stage SaaS."

### knowledge-base-for-startups
<a name="skill-knowledge-base"></a>

The `knowledge-base-for-startups` skill is an AWS Startups knowledge base. It includes the AWS Activate FAQ, a credits guide, programs, partner offers, sample architectures, and learn articles. It is a read-only reference that is searchable and available offline after install.

 **Example prompt**: "Do my AWS Activate credits expire?"

### prompt-library-for-startups
<a name="skill-prompt-library"></a>

The `prompt-library-for-startups` skill provides about 30 AWS-curated, copy-paste prompts, for example MVP scaffolding, a RAG chatbot, a security baseline, cost anomaly detection, EKS deployment, and a Well-Architected review. It also provides downloadable installable agents: Migration, Multi-Account Transition Advisor, Bill Shock Preventer, and Service Quota.

 **Example prompt**: "Give me a prompt for an MVP on AWS."

### contextual-offers-for-startups
<a name="skill-contextual-offers"></a>

The `contextual-offers-for-startups` skill is an offer layer that runs after another skill produces a recommendation, plan, or build. When a genuinely relevant AWS Activate partner offer exists for what you’re building or migrating, it appends one quiet, dismissible line with a redeem link. It never changes the technical advice, and it adds at most one offer for each response.

## Build AI agents on AWS
<a name="using-skills-agents"></a>

This group helps you choose a runtime and build AI agents on AWS.

### agent-advisor
<a name="skill-agent-advisor"></a>

The `agent-advisor` skill helps you pick an AWS runtime for AI agents, such as Amazon Bedrock AgentCore, ECS, EKS, Lambda, or Lambda MicroVMs. It can generate a migration plan for existing agent workloads and build a deployable proof of concept, and it also covers Temporal workers. Runtime recommendations and design-backed proofs of concept work standalone. The full migration-plan step additionally needs the `gcp-to-aws` skill installed, and it degrades gracefully without it: the step is skipped, not broken.

 **Example prompt**: "Which AWS runtime should I use for my AI agent?"

## Migrate to AWS
<a name="using-skills-migrate"></a>

The migration skills plan and run moves from other cloud providers and AI providers to AWS.

### gcp-to-aws
<a name="skill-gcp-to-aws"></a>

The `gcp-to-aws` skill plans a migration from Google Cloud, and from AI providers such as OpenAI, Gemini, and LangChain, to AWS through a guided multi-phase workflow. It discovers resources from Terraform and other infrastructure as code, application code, and Google Cloud billing exports. It then designs an AWS architecture, estimates cost, and generates migration artifacts, including Terraform.

 **Example prompt**: "Help me migrate from GCP to AWS."

### azure-to-aws
<a name="skill-azure-to-aws"></a>

The `azure-to-aws` skill plans a migration from Microsoft Azure to AWS through a guided six-phase workflow: discover, clarify, design, estimate, generate artifacts, and gather feedback. It discovers resources from Terraform (`azurerm_*`), a read-only, consent-gated live capture from the Azure CLI (`az`), application code, and billing exports. Bicep and Azure Resource Manager (ARM) templates aren’t supported yet. After the estimate, you can run an optional what-if repricing workshop, and generating artifacts is opt-in.

 **Example prompt**: "Help me migrate from Azure to AWS."

### heroku-to-aws
<a name="skill-heroku-to-aws"></a>

The `heroku-to-aws` skill plans a Heroku-to-AWS migration. By default it maps Dynos to Elastic Beanstalk, with Fargate or EKS overrides available. It maps Postgres to RDS or Aurora, Redis to ElastiCache, and Kafka to MSK, and it handles common add-ons. After the estimate, you can run an optional what-if repricing workshop.

 **Example prompt**: "Plan a migration of my Heroku app to AWS."

### llm-to-bedrock
<a name="skill-llm-to-bedrock"></a>

The `llm-to-bedrock` skill runs an OpenAI, Gemini, or Anthropic to Amazon Bedrock SDK rewrite. It assesses the codebase, rewrites call sites, evaluates output quality against Amazon Bedrock, and delivers a ready-to-merge git branch. This skill requires the `gcp-to-aws` skill installed alongside it, because it delegates the assessment step to that skill.

 **Example prompt**: "Move my OpenAI app to Amazon Bedrock."

### tf-best-practices
<a name="skill-tf-best-practices"></a>

The `tf-best-practices` skill provides best-practice authoring guidance and a read-only policy gate for the AWS Terraform that the migration skills generate.

 **Example prompt**: "Review my generated Terraform against AWS best practices."

**Note**  
The skills are cross-aware. They consult each other and route migration and agent intent to the matching skill.