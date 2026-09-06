

# Installing Amazon SageMaker AI skills
<a name="remote-access-install-skills"></a>

This Amazon SageMaker AI plugin is available on the [AWSLabs GitHub page](https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai) and brings deep AWS AI/ML expertise directly into your coding assistant, covering the surface area of [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/); currently, skills are provided to assist with the following capability areas:
+ **Model Customization** — End-to-end guided workflows for fine-tuning foundation models, from use case definition through data preparation, training, evaluation, and deployment on Amazon SageMaker AI.
+ **HyperPod Cluster Operations** — Remote command execution on nodes via SSM, version checking, and diagnostic reporting for Amazon SageMaker AI HyperPod training clusters.

## Agent Skills
<a name="remote-access-install-skills-list"></a>

The following skills are installed by the plugin:


**Amazon SageMaker AI agent skills**  

| Skill | Description | Documentation | 
| --- | --- | --- | 
| planning | Builds a dynamic, step-by-step plan tailored to your intents | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/planning/SKILL.md) | 
| directory-management | Manages project directory setup, artifact organization, and plan association for new or existing projects | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/directory-management/SKILL.md) | 
| use-case-specification | Guided, conversational process to define your model customization use case goals, key stakeholders, and success criteria | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/use-case-specification/SKILL.md) | 
| dataset-evaluation | Dataset quality validation, format detection, and data requirements analysis | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/dataset-evaluation/SKILL.md) | 
| dataset-transformation | Dataset format conversion and preparation for SageMaker AI-compatible training formats | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/dataset-transformation/SKILL.md) | 
| finetuning-setup | Fine-tuning technique selection (SFT, DPO, RLVR, etc.) and base model selection | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/finetuning-setup/SKILL.md) | 
| finetuning | Hyperparameter configuration and training job execution | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/finetuning/SKILL.md) | 
| model-evaluation | Evaluation design, benchmark selection, LLM-as-a-judge, and model comparison | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/model-evaluation/SKILL.md) | 
| model-deployment | Deployment configuration and endpoint setup (SageMaker AI or Amazon Bedrock) | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/model-deployment/SKILL.md) | 
| hyperpod-ssm | Remote command execution and file transfer on HyperPod cluster nodes via SSM | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/hyperpod-ssm/SKILL.md) | 
| hyperpod-version-checker | Check and compare software component versions across HyperPod cluster nodes | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/hyperpod-version-checker/SKILL.md) | 
| hyperpod-issue-report | Generate diagnostic reports for HyperPod troubleshooting and support cases | [SKILL.md](https://github.com/awslabs/agent-plugins/blob/main/plugins/sagemaker-ai/skills/hyperpod-issue-report/SKILL.md) | 

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
  npx skills add https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai/skills --all --agent claude-code --copy
  ```
+ **Cursor**:

  ```
  npx skills add https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai/skills --all --agent cursor --copy
  ```
+ **Kiro**:

  ```
  npx skills add https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai/skills --all --agent kiro-cli --copy
  ```

If you have configured other agents, use:

```
npx skills add https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai/skills --all --agent 
```