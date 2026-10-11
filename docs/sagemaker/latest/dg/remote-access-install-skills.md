

# Installing Amazon SageMaker AI skills
<a name="remote-access-install-skills"></a>

The Agent Toolkit for AWS gives AI coding agents the tools, knowledge, and science-based best practices they need to work with AWS services. It works with the coding agents you already use, including Claude Code, Codex, Cursor, and Kiro. The toolkit bundles the AWS MCP Server configuration and a curated set of agent skills in a single install, so your agent can discover and apply AWS best practices automatically without you having to know which skill to invoke.

The toolkit includes a broad set of core skills that span many AWS services and common workflows, such as Amazon Bedrock and Amazon Elastic Compute Cloud, in addition to the AWS AI/ML skill covered on this page. Your agent loads only the skills relevant to the task at hand.

The AWS AI/ML skill (`aws-ai-ml`) brings deep AWS AI/ML expertise into your coding assistant and covers [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/). It supports the full model customization lifecycle from planning through production, and it currently assists with the following capability areas:
+ **Model selection** — Guided selection of a base model from Amazon SageMaker AI Hub, matching model family and size to your use case requirements, for either fine-tuning or off-the-shelf deployment.
+ **Model deployment** — Deployment configuration and endpoint setup on Amazon SageMaker AI or Amazon Bedrock, covering the Nova and open-source (OSS) deployment pathways.
+ **Model fine-tuning** — End-to-end guided workflows for fine-tuning foundation models, from use case definition through data preparation, training, evaluation, and deployment on Amazon SageMaker AI. Supports both serverful and serverless paths.
+ **Model evaluation** — Evaluation design, benchmark selection, LLM-as-a-judge and custom scorers, and side-by-side model comparison to measure quality before and after customization.
+ **Inference optimization** — Benchmarking and tuning of real-time endpoints to meet performance, cost, latency, and throughput goals, including instance recommendations.
+ **MLflow** — Set up, update, or delete a Amazon SageMaker AI Managed MLflow app to track experiments, parameters, and metrics across the customization lifecycle.

## Agent Skills
<a name="remote-access-install-skills-list"></a>

The following skill is installed by the plugin:


**Amazon SageMaker AI agent skills**  

| Skill | Description | Documentation | 
| --- | --- | --- | 
| aws-ai-ml | Selects, deploys, and customizes AI models on Amazon SageMaker AI. Covers the full lifecycle from planning through production: model selection, dataset preparation, fine-tuning (SFT, DPO, RLVR, RLAIF), evaluation, deployment to Amazon SageMaker AI endpoints or Amazon Bedrock, inference optimization, endpoint diagnostics, and Amazon SageMaker AI Managed MLflow. | [SKILL.md](https://github.com/aws/agent-toolkit-for-aws/blob/main/plugins/aws-core/skills/aws-ai-ml/SKILL.md) | 

## MCP Servers
<a name="remote-access-install-skills-mcp"></a>

Amazon SageMaker AI Skills requires the Amazon SageMaker AI MCP server. Add the contents of the [`.mcp.json` file](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/.mcp.json) to your platform's MCP configuration file:
+ **Claude Code**: Run `claude mcp add --transport stdio aws-mcp -- uvx mcp-proxy-for-aws@latest https://aws-mcp.us-east-1.api.aws/mcp` or manually add to `User/Project/Local` location as needed ([Claude Code Docs: What uses scopes](https://code.claude.com/docs/en/settings#what-uses-scopes)).
+ **Cursor**: `.cursor/mcp.json`
+ **Kiro**: `.kiro/settings/mcp.json`

## Install Skills with `npx skills`
<a name="remote-access-install-skills-cli"></a>

You may use the [Skills CLI](https://github.com/vercel-labs/skills) (from Vercel Labs) to install the skills into your platform:
+ **Claude Code**:

  ```
  npx skills add aws/agent-toolkit-for-aws/skills/core-skills/aws-ai-ml --all --agent claude-code --copy
  ```
+ **Cursor**:

  ```
  npx skills add aws/agent-toolkit-for-aws/skills/core-skills/aws-ai-ml --all --agent cursor --copy
  ```
+ **Kiro**:

  ```
  npx skills add aws/agent-toolkit-for-aws/skills/core-skills/aws-ai-ml --all --agent kiro-cli --copy
  ```

If you have configured other agents, substitute your agent name for `<agent>` and use:

```
npx skills add aws/agent-toolkit-for-aws/skills/core-skills/aws-ai-ml --all --agent <agent>
```

Alternatively, install the full `aws-core` plugin, which bundles the AWS MCP Server configuration and the curated core skill set in a single install:
+ **Claude Code**:

  ```
  /plugin install aws-core@claude-plugins-official
  /reload-plugins
  ```
+ **Codex**:

  ```
  codex plugin marketplace add aws/agent-toolkit-for-aws
  ```

  Then launch Codex, run `/plugins`, and install the `aws-core` plugin.
+ **AWS CLI** (version 2.35.0 or later):

  Run the interactive setup wizard, which detects your installed AI coding agents, installs default AWS skills, and configures the AWS MCP Server connection in a single command:

  ```
  aws configure agent-toolkit
  ```