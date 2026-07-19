# How the ElastiCache skill works

The ElastiCache skill routes your request to the appropriate workflow area based on your intent.
It loads only the reference material needed for the current task. The following table describes
the workflow areas included in the skill.

| Workflow area           | Purpose                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Solution fit            | Gathers workload requirements and recommends whether ElastiCache is the right fit for your application.           |
| Create and connect      | Helps create caches, choose engines, configure networking, set up authentication, and connect applications.       |
| Application patterns    | Helps choose key schemas, TTLs, invalidation strategies, and Redis or Valkey data structures.                     |
| AI and vector workloads | Helps implement semantic caching, agent memory, RAG, recommendation, personalization, and vector search patterns. |
| Operate and observe     | Helps configure dashboards, alarms, logs, troubleshooting, cost reporting, and security audits.                   |
| Migration               | Helps plan and run migrations from self-managed Redis, Redis OSS, or another ElastiCache deployment model.        |

## Setup and networking

The skill helps agents identify the appropriate deployment configuration for a workload
before generating setup guidance or commands. It guides agents to consider engine choice,
serverless or node-based deployment, feature compatibility, and other requirements. The
skill then guides agents through networking setup, including VPC placement, subnet and
security group configuration, and application connectivity.

For local development, the skill guides agents to use supported access patterns such as
a jump host or AWS Systems Manager Session Manager tunnel, instead of assuming direct
access to an ElastiCache endpoint from a local machine.

The skill stores ElastiCache-specific project context in a state file at
`.elasticache/requirements.json`. This file helps the agent avoid asking for the
same information repeatedly. It can include values such as engine, AWS Region, and cache
endpoints. If this file exists, the skill reads it before asking new questions.

## Cost estimation

The skill can help agents provide preliminary pricing guidance for ElastiCache workloads. The
skill includes a pricing calculator to estimate monthly costs from workload inputs such as
data size, request volume, command types, and payload size.

AWS credentials are not required to generate pricing estimates. The pricing calculator
uses publicly available AWS pricing data, so you can estimate serverless and node-based
costs before provisioning resources or connecting an AWS account. The pricing estimates
are for planning purposes only and can vary from actual costs. Before deployment, confirm
current pricing on the ElastiCache pricing page.

## Monitoring and troubleshooting

The monitoring workflow helps diagnose operational issues by starting with relevant
metrics and then recommending the smallest effective change. The skill can use bundled
scripts to collect metrics, generate dashboards, run security audits, and support cost
analysis.

Use the ElastiCache skill to investigate performance, availability, and cost issues such as
the following:

- High latency
- Low cache hit rates
- CPU or memory pressure
- Replication lag
- Connection spikes
- Hot keys and big keys
- Shard imbalance
- Slow commands
- Unexpected cost increases
- CloudWatch alarm configuration
- Log delivery

## GenAI and vector workload guidance

The skill helps agents provide guidance for AI application patterns such as semantic
caching, AI agent memory, retrieval-augmented generation (RAG), recommendation systems,
and vector search. The skill helps agents identify the user's intent, select the
appropriate workflow, and generate implementations that are aligned with ElastiCache
capabilities.

For these workloads, the skill provides detailed guidance for embedding storage, key
design, TTL strategy, similarity threshold tuning, framework integrations, and operational
considerations.
