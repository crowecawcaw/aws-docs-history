# Analyze best practices with the `managing-amazon-msk` skill

The `managing-amazon-msk` skill is an open-source [Agent Skill](https://agentskills.io/home "https://agentskills.io/home") on the Agent Skills website from the [AWS Agent Toolkit](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws") on GitHub that provides domain expertise for operating Amazon MSK Provisioned clusters. After you install the skill in an MCP-compatible AI coding agent (such as Kiro, Cursor, Claude Code, and others), the skill enables the AI agent to help you assess your cluster and clients against best practices, diagnose operational issues, and implement recommended configurations for Standard and Express brokers and Kafka clients. The skill encodes MSK-specific operational knowledge that general-purpose AI models frequently misapply or omit.

## Capabilities

The skill covers the following areas, each of which maps to best practices documented in this guide.

|     | Best practice area                                                                                                          | What the skill helps you do                                                                                                                                                                                         |
| --- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | [Best practices for Standard brokers](bestpractices.md "bestpractices.md") (Standard)                                       | Assess partition counts per broker, recommend instance sizes, evaluate `num.io.threads` and `num.network.threads` tuning for m5.4xl+ and m7g.4xl+ instances                                                         |
| 2   | [Best practices for Express brokers](bestpractices-express.md "bestpractices-express.md") (Express)                         | Calculate required broker count based on per-broker throughput limits, recommend Express instance types for target ingress/egress, evaluate partition counts against Express quotas                                 |
| 3   | [Monitor CPU usage](bestpractices.md#bestpractices-monitor-cpu "bestpractices.md#bestpractices-monitor-cpu")                | Diagnose broker resource saturation, differentiate between broker-side and client-side root causes and misconfigurations, and determine when scaling is needed                                                      |
| 4   | [Monitor disk space](bestpractices.md#bestpractices-monitor-disk-space "bestpractices.md#bestpractices-monitor-disk-space") | Assess storage usage for Standard brokers, identify high-growth topics, recommend EBS expansion or retention adjustments. For Express, monitor storage utilization (storage is fully managed) for cost optimization |
| 5   | [Connect to an Amazon MSK Provisioned cluster](client-access.md "client-access.md")                                         | Audit producer/consumer settings, configure authentication, tune for high availability and fault tolerance                                                                                                          |
| 6   | [Build highly available clusters](bestpractices.md#ensure-high-availability "bestpractices.md#ensure-high-availability")    | Verify high availability configurations and multi-AZ deployment for Standard brokers, and client failover configuration                                                                                             |
| 7   | [Monitor an Amazon MSK Provisioned cluster](monitoring.md "monitoring.md")                                                  | Create CloudWatch dashboards and alarms for key metrics critical to Amazon MSK observability and operations                                                                                                         |
| 8   | [Amazon MSK key features and concepts](operations.md "operations.md")                                                       | Assess cluster readiness for updates, understand patching behavior between Standard and Express, understand broker restart impact on clients                                                                        |

## How it works

When you ask your AI coding agent a question about Amazon MSK — such as "Why is my MSK cluster CPU high?" or "Help me set up monitoring for my Express cluster" — the skill activates and provides the agent with:

- **Diagnostic workflows** — Structured troubleshooting steps that check the most likely root causes first (for example, verifying `linger.ms` before recommending broker scaling for CPU issues).
- **Broker-type-aware guidance** — The skill determines whether your cluster uses Standard or Express brokers and applies the correct metrics, thresholds, and recommendations for that broker type.
- **AWS CLI commands** — Ready-to-run commands for describing clusters, expanding storage, creating configurations, and querying CloudWatch metrics.
- **Best practice validation** — Checks your cluster configuration against documented recommendations and flags deviations.

## Installation

### Option 1: AWS CLI

Requires AWS CLI version 2.35.0 or later.

```
# Interactive setup (installs default skills + configures AWS MCP Server)
aws configure agent-toolkit

# Or install the skill individually
aws agent-toolkit add-skill --skill-name managing-amazon-msk
```

For full CLI documentation, see [Managing skills with the AWS CLI](../../../agent-toolkit/latest/userguide/aws-cli.md "../../../agent-toolkit/latest/userguide/aws-cli.md").

### Option 2: AWS MCP Server

Connect your AI coding agent to the AWS MCP Server, which provides the skill along with sandboxed AWS API execution capabilities.

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws==1.6.2",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-east-1"
      ]
    }
  }
}
```

For full setup instructions, see [Setting up the AWS MCP Server](../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md "../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md").

## Use cases and examples

### Assess Standard broker best practices

**Prompt:** "I have an MSK Standard cluster using kafka.m5.2xlarge brokers with 2,500 partitions per broker. Am I following best practices?"

The skill:

- Check your partition count against the [recommended limit of 2,000 partitions per broker](bestpractices.md#partitions-per-broker "bestpractices.md#partitions-per-broker") for m5.2xlarge.
- Warn that you exceed the recommended count and are approaching the 3,000 maximum that supports update operations.
- Recommend either reducing partitions or upgrading to m5.4xlarge (which supports 4,000 partitions per broker).
- Check your `num.io.threads` and `num.network.threads` settings and recommend tuning if undersized.

### Diagnose Express broker performance

**Prompt:** "My Express cluster has 3 express.m7g.large brokers and I'm seeing throttling. What's wrong?"

The skill:

- Identify that `express.m7g.large` supports [15.6 MBps ingress and 31.2 MBps egress per broker](limits.md#msk-express-quota "limits.md#msk-express-quota").
- Ask about your current throughput or run a CloudWatch query to check `BytesInPerSec` and `BytesOutPerSec`.
- If throughput exceeds per-broker limits, recommend scaling to `express.m7g.xlarge` or adding brokers.
- Check `ProduceThrottleTime` and `FetchThrottleTime` metrics.

### Audit client configuration

**Prompt:** "Review my Kafka producer configuration for best practices on MSK"

The skill:

- Check critical configurations such as `linger.ms`, `acks`, `batch.size`, `buffer.memory`, and more for performance and durability considerations.
- Provide recommendations for your scenario to tune configurations, improve performance, and ensure high availability.

### Set up monitoring and alarms

**Prompt:** "Help me set up CloudWatch monitoring for my MSK cluster following best practices"

The skill:

- Create alarms for critical metrics like CPU utilization (`CpuUser + CpuSystem`), `RequestHandlerAvgIdlePercent`, and others to monitor broker saturation.
- For Standard: add `KafkaDataLogsDiskUsed > 85%` alarm and `UnderReplicatedPartitions > 0` alarm.
- For Express: add `StorageUsed` monitoring for cost optimization.
- Set up per-broker, per-topic, and per-consumer-group dashboards.

## Source code and contributions

The `managing-amazon-msk` skill is open source. You can review the source code, suggest improvements, or contribute new features.

- **GitHub:** [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/managing-amazon-msk "https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/managing-amazon-msk") on GitHub

Feedback on additional best practice scenarios, new use cases, or corrections is welcome via GitHub issues or pull requests.
