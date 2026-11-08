

# Using AWS Startup Advisor skills
<a name="using-skills"></a>

 AWS Startup Advisor bundles 12 skills that a coding agent uses. The same skills are available across the supported agents, so you get the same guidance no matter which agent you use. The skills fall into four groups: skills that help you start and grow on AWS, skills that build AI agents on AWS, skills that migrate workloads to AWS, and skills that operate workloads on AWS.

To use a skill, prompt your coding agent with what you want to do. Each skill in the following sections includes an example prompt.

**Topics**
+ [Start and grow on AWS](#using-skills-start-grow)
+ [Build AI agents on AWS](#using-skills-agents)
+ [Migrate to AWS](#using-skills-migrate)
+ [Operate on AWS](#using-skills-operate)

## Start and grow on AWS
<a name="using-skills-start-grow"></a>

This group scaffolds new projects, tailors architecture guidance to your stage, and provides reference material and prompts.

### start-building-for-startups
<a name="skill-start-building"></a>

The `start-building-for-startups` skill is an interactive discovery workflow. It scans your codebase, asks about your goals and constraints through picker questions, and then writes an AWS architectural scaffold directly into your project.

 **Example prompt**: "Scaffold a serverless API for my startup."

### architect-for-startups
<a name="skill-architect"></a>

The `architect-for-startups` skill provides stage-aware AWS architecture guidance for non-agent workloads (for AI agents, use `agent-advisor`). It adjusts recommendations based on your startup stage (pre-revenue, seed, Series A, or Series B and later), team size, runway, and timeline. It can also review an existing architecture for a fundraise or technical diligence. It gives advice rather than code changes, and hands off to `start-building-for-startups` when you’re ready to build.

 **Example prompt**: "Recommend an architecture for my seed-stage SaaS."

### knowledge-base-for-startups
<a name="skill-knowledge-base"></a>

The `knowledge-base-for-startups` skill is an AWS Startups knowledge base. It includes the AWS Activate FAQ, a credits guide, programs, partner offers, sample architectures, and learn articles. It is a read-only reference that is searchable and available offline after install. It can’t look up account-specific details such as your credits balance, AWS Activate membership, or application status. For those, see the [AWS Startups](https://aws.amazon.com/startups/) website.

 **Example prompt**: "Do my AWS Activate credits expire?"

### prompt-library-for-startups
<a name="skill-prompt-library"></a>

The `prompt-library-for-startups` skill provides about 30 AWS-curated, copy-paste prompts, for example MVP scaffolding, a Retrieval Augmented Generation (RAG) chatbot, a security baseline, cost anomaly detection, EKS deployment, and a Well-Architected review. It also provides downloadable installable agents: Multi-Account Transition Advisor, Bill Shock Preventer, Service Quota Agent, Bedrock Model Availability Agent, and AWS DB Advisor.

 **Example prompt**: "Give me a prompt for an MVP on AWS."

### contextual-offers-for-startups
<a name="skill-contextual-offers"></a>

The `contextual-offers-for-startups` skill is an offer layer that runs after another skill produces a recommendation, plan, or build. When a genuinely relevant AWS Activate partner offer exists for what you’re building or migrating, it appends one quiet, dismissible line with a redeem link. It never changes the technical advice, and it adds at most one offer for each response. You can mute it.

## Build AI agents on AWS
<a name="using-skills-agents"></a>

This group helps you choose a runtime and build AI agents on AWS.

### agent-advisor
<a name="skill-agent-advisor"></a>

The `agent-advisor` skill helps you pick an AWS runtime for AI agents, such as Amazon Bedrock AgentCore, ECS, EKS, Lambda, or Lambda MicroVMs. For an agent already on AWS, it can add AgentCore capabilities, including memory, gateway, identity, policy, and observability. It can generate a migration plan for existing agent workloads and build a deployable proof of concept. It also covers Temporal Cloud compared with self-hosted Temporal, and it never rewrites your Temporal workflow code. It requires at least one agentic component. It routes non-agent migrations to the migration skills and pure SDK rewrites to `llm-to-bedrock`. Runtime recommendations and design-backed proofs of concept work standalone. The full migration-plan step additionally needs the `gcp-to-aws` skill installed, and it degrades gracefully without it: the step is skipped, not broken.

 **Example prompt**: "Which AWS runtime should I use for my AI agent?"

## Migrate to AWS
<a name="using-skills-migrate"></a>

The migration skills plan and run moves from other cloud providers and AI providers to AWS.

The `gcp-to-aws`, `azure-to-aws`, and `heroku-to-aws` skills share a guided six-phase workflow: discover, clarify, design, estimate, generate, and feedback. The clarify phase must finish before the others, and generating artifacts is opt-in. On the infrastructure route, they also generate `baseline.tf`, an account-wide security baseline (GuardDuty, CloudTrail, IMDSv2, EBS encryption, and budget alerts). When you declare SOC 2, PCI, HIPAA, or FedRAMP, they also add AWS Config and Security Hub controls. After the estimate, you can run an optional what-if workshop that reprices Region, high availability, compute, and Graviton. Estimates are planning figures. Confirm them with the [AWS Pricing Calculator](https://calculator.aws/).

### gcp-to-aws
<a name="skill-gcp-to-aws"></a>

The `gcp-to-aws` skill plans a migration from Google Cloud, and from AI providers such as OpenAI, Gemini, and LangChain or LangGraph, to AWS. It discovers resources from Terraform and other infrastructure as code, a read-only, consent-gated live capture from the Google Cloud CLI (`gcloud`), application code, and Google Cloud billing exports. BigQuery is recorded but not yet mapped to an AWS analytics service. With your consent, it can also read AI spend from the OpenAI Admin API, OpenRouter API, or Anthropic Admin API. After the estimate, it can offer a link to apply for up to $1,500 in AWS migration credits.

 **Example prompt**: "Help me migrate from GCP to AWS."

### azure-to-aws
<a name="skill-azure-to-aws"></a>

The `azure-to-aws` skill plans a migration from Microsoft Azure to AWS. It discovers resources from Terraform (`azurerm_*`), a read-only, consent-gated live capture from the Azure CLI (`az`), a customer-supplied Resource Discovery for Azure (RDfA) report (read-only, file only), and application code. It doesn’t read Azure billing exports, Bicep, or Azure Resource Manager (ARM) templates. With your consent, it can also read AI spend from the OpenAI Admin API, OpenRouter API, or Anthropic Admin API.

 **Example prompt**: "Help me migrate from Azure to AWS."

### heroku-to-aws
<a name="skill-heroku-to-aws"></a>

The `heroku-to-aws` skill plans a Heroku-to-AWS migration. By default it maps Dynos to Elastic Beanstalk, with Fargate or EKS overrides available. It maps Postgres to RDS or Aurora, Redis to ElastiCache, and Kafka to MSK, and it handles common add-ons. It discovers resources through a read-only, consent-gated live capture from the authenticated Heroku CLI, or from your `Procfile` and `app.json`. After the estimate, it can offer a link to apply for up to $1,500 in AWS migration credits.

 **Example prompt**: "Plan a migration of my Heroku app to AWS."

### llm-to-bedrock
<a name="skill-llm-to-bedrock"></a>

The `llm-to-bedrock` skill runs an OpenAI, Gemini, or Anthropic to Amazon Bedrock SDK rewrite. It assesses the codebase, rewrites call sites, evaluates output quality against Amazon Bedrock, and delivers a ready-to-merge git branch. A full migration requires either the `gcp-to-aws` or the `azure-to-aws` skill installed alongside it (`gcp-to-aws` is preferred when both are present), because it delegates the assessment step to that skill. A separate access-only mode checks or enables Amazon Bedrock model access for the models you name, without rewriting code, and needs neither sibling skill.

 **Example prompt**: "Move my OpenAI app to Amazon Bedrock."

### tf-best-practices
<a name="skill-tf-best-practices"></a>

The `tf-best-practices` skill provides best-practice authoring guidance and a read-only policy gate for the AWS Terraform that the migration skills generate.

 **Example prompt**: "Review my generated Terraform against AWS best practices."

## Operate on AWS
<a name="using-skills-operate"></a>

This group operates a live AWS workload for startups that don’t have a dedicated DevOps or site reliability engineer.

### operate-on-aws
<a name="skill-operate-on-aws"></a>

The `operate-on-aws` skill operates a live AWS workload with [AWS DevOps Agent](https://aws.amazon.com/devops-agent/). It investigates production incidents and finds the probable root cause from your logs, metrics, alarms, and recent changes. Examples include a production outage, 5xx errors, a latency spike, a regression after your last deploy, or a fired alarm. It can also help you write a postmortem. It also runs release-readiness reviews of a pull request before you merge.

Release-readiness review is in preview, at no charge during the preview, and available only in US East (N. Virginia).

Setup runs through your coding agent. The skill detects an existing setup first and never re-onboards. It recommends AWS DevOps Agent only when there’s evidence it helps, such as a live workload or active pull requests. Before first-time setup, it asks one yes-or-no question that covers cost and the account access it needs, and nothing is enabled or charged until you say yes. Optional automated verification testing, which copies your code into an AWS managed verification environment to build and test it, stays off unless you opt in. For more information, see [Release readiness code reviews](https://docs.aws.amazon.com/devopsagent/latest/userguide/release-management-release-readiness-code-review.html) in the * AWS DevOps Agent User Guide*.

 AWS DevOps Agent recommends fixes. It doesn’t apply them. Setup doesn’t enable Directed Actions or elevated permissions, so findings and fixes stay recommendations that you review and decide whether to act on.

You can say `stop` during setup to roll back what the skill created. After setup, you can pause, stop, or check the cost of AWS DevOps Agent. Stopping cancels in-progress work but keeps your setup.

 AWS Startup Advisor is available at no additional charge, but AWS DevOps Agent is a paid AWS service. If you have AWS Activate credits, they can cover your AWS DevOps Agent usage. For pricing information, see [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/). For more information about AWS DevOps Agent, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

For the AWS Startup Advisor IDE extension equivalent, see [Operate](using-ide-extension.md#using-ide-extension-operate).

 **Example prompt**: "Our API has been returning 502s since the last deploy — what broke?"

**Note**  
The skills are cross-aware. They consult each other and route migration and agent intent to the matching skill.