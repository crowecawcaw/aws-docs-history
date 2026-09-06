

# Getting started
<a name="agent-tools-skills-getting-started"></a>

Install the ElastiCache skill using the following command:

```
npx skills add aws/agent-toolkit-for-aws/skills/specialized-skills/database-skills/amazon-elasticache -g -a <agent-id> --full-depth
```

Replace `<agent-id>` in the install command with the identifier for your coding agent. The following table lists identifiers for supported coding agents. The installer adds the ElastiCache skill from the AWS Agent Toolkit repository to the global skills directory used by your coding agent, making it available for all your projects.


| Agent | `<agent-id>` | Global skills path | Project skills path | 
| --- | --- | --- | --- | 
| Claude Code | claude-code | \~/.claude/skills/ | .claude/skills/ | 
| Cursor | cursor | \~/.cursor/skills/ | .agents/skills/ | 
| GitHub Copilot | github-copilot | \~/.copilot/skills/ | .agents/skills/ | 
| Codex | codex | \~/.codex/skills/ | .agents/skills/ | 
| Gemini CLI | gemini-cli | \~/.gemini/skills/ | .agents/skills/ | 
| Kiro CLI | kiro-cli | \~/.kiro/skills/ | .kiro/skills/ | 
| Cline | cline | \~/.agents/skills/ | .agents/skills/ | 
| Goose | goose | \~/.config/goose/skills/ | .goose/skills/ | 
| Windsurf | windsurf | \~/.codeium/windsurf/skills/ | .windsurf/skills/ | 

To install the skill locally for a single project instead, omit the `-g` flag. The skill installs to the project skills path listed in the preceding table.

**Note**  
The skill runs locally with your agent. For tasks that create or modify AWS resources, your agent needs AWS credentials configured through the AWS Command Line Interface, environment variables, or your IDE's AWS plugin.

## Examples of usage
<a name="agent-tools-skills-examples"></a>

After installation, you can prompt your agent to build with the ElastiCache skill.

The following examples use "Use the Amazon ElastiCache skill to..." as a prefix:
+ **Evaluate a workload**: `Use the Amazon ElastiCache skill to decide whether ElastiCache is right for my FastAPI app. The app reads heavily from Aurora PostgreSQL and has latency spikes during peak traffic.`
+ **Create a secure cache**: `Use the Amazon ElastiCache skill to create a Valkey cache in us-east-1 for my ECS service. Use TLS and recommend the right authentication model.`
+ **Connect an application**: `Use the Amazon ElastiCache skill to connect my Lambda function to an existing Valkey cache. Show the VPC, security group, and client code changes.`
+ **Build a rate limiter**: `Use the Amazon ElastiCache skill to build an API rate limiter with Valkey. I need per-user limits and atomic updates.`
+ **Add semantic caching for GenAI**: `Use the Amazon ElastiCache skill to add semantic caching for Amazon Bedrock responses. Include embedding storage, similarity lookup, thresholding, and fallback behavior.`
+ **Troubleshoot performance**: `Use the Amazon ElastiCache skill to pinpoint the cause of high CPU utilization on my cache cluster.`

**Note**  
Some agents auto-load the ElastiCache skill when your prompt describes a relevant workload such as caching, sessions, or rate limiting. If your agent does not load the skill automatically, include "use the ElastiCache skill" in your prompt.