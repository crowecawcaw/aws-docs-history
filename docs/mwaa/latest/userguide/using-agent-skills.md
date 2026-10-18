

# Using agent skills with Amazon MWAA
<a name="using-agent-skills"></a>

Agent skills are instruction packages that guide an AI coding assistant through Amazon Managed Workflows for Apache Airflow operations. The AWS Data Analytics plugin (`aws-data-analytics`) in the open-source Agent Toolkit for AWS provides a set of skills that follow the open Agent Skills standard. After you install the skills, you describe what you want to do in natural language, and your assistant uses the matching skill to do the work. This guide describes the Amazon MWAA skills, how to install them for several assistants, and example prompts that you can use.

**Topics**
+ [Overview](#using-agent-skills-overview)
+ [Installing the skills](#using-agent-skills-install)
+ [Example prompts](#using-agent-skills-examples)
+ [Related resources](#using-agent-skills-resources)

## Overview
<a name="using-agent-skills-overview"></a>

The [AWS Data Analytics plugin](https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-data-analytics) (`aws-data-analytics`) in the open-source [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website provides agent skills for Amazon Managed Workflows for Apache Airflow.

A skill is an instruction package that guides an AI coding assistant (such as Kiro, Claude Code, Amazon Q, Cursor, or Codex) through a common Amazon MWAA operation. These skills follow the open [Agent Skills standard](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) on the Anthropic website, so you can use them across assistants that support the standard.

The Amazon MWAA skills work with both Amazon MWAA provisioned environments and Amazon MWAA Serverless, except where noted. In provisioned environments, you author workflows as Python directed acyclic graphs (DAGs). In Amazon MWAA Serverless, you author workflows as YAML.

The plugin includes the following four Amazon MWAA skills.
+ `authoring-mwaa-workflow` authors and deploys Apache Airflow DAGs for provisioned environments and YAML workflows for Amazon MWAA Serverless.
+ `debugging-mwaa-workflow` finds the root cause of failed runs and task instances, DAGs that do not appear, import errors, worker out-of-memory errors, and IAM permission errors.
+ `testing-mwaa-workflow` triggers a deployed DAG or workflow, monitors it to completion, and retests after fixes.
+ `upgrading-mwaa-environments` upgrades a provisioned environment to a newer Apache Airflow version, including 2.x to 3.x, by using a blue-green or in-place strategy. This skill supports provisioned environments only, not Amazon MWAA Serverless.

The skills run AWS Command Line Interface (AWS CLI) commands to interact with your AWS resources. We recommend that you also install the AWS Model Context Protocol (MCP) Server. The skills use the [AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) to fetch current AWS documentation at runtime and to run AWS CLI commands with sandboxed execution and audit logging.

## Installing the skills
<a name="using-agent-skills-install"></a>

The Amazon MWAA skills are part of the `aws-data-analytics` plugin in the Agent Toolkit for AWS. To install the AWS MCP Server and set up your coding assistant, such as Kiro, Claude Code, Codex, Cursor, or the AWS CLI, follow [Getting started](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html) in the Agent Toolkit for AWS User Guide. When you install plugins or skills, choose the `aws-data-analytics` plugin, which provides the Amazon MWAA skills.

### Prerequisites
<a name="using-agent-skills-install-prereqs"></a>

Complete the prerequisites in Getting started. In addition, grant your AWS Identity and Access Management (IAM) principal permissions for the Amazon MWAA action namespaces that you use, scoped to the resources that you use. Use the `airflow` namespace for Amazon MWAA environments and the Apache Airflow REST API, and the `airflow-serverless` namespace for Amazon MWAA Serverless workflows and runs.

### Installing the aws-data-analytics plugin
<a name="using-agent-skills-install-plugin"></a>

Install the `aws-data-analytics` plugin for your assistant. For example, in Claude Code, run the following command:

```
/plugin install aws-data-analytics@claude-plugins-official
```

For Kiro, Codex, Cursor, and other assistants, install the `aws-data-analytics` plugin or its skills as described in Getting started. To install the skills directly from the repository, run the following command:

```
npx skills add aws/agent-toolkit-for-aws/skills
```

## Example prompts
<a name="using-agent-skills-examples"></a>

After you install the skills, you can give your assistant natural-language prompts to complete Amazon MWAA operations. The following examples are grouped by skill.

Use the following prompts to author and deploy workflows with the `authoring-mwaa-workflow` skill.
+ "Create an Apache Airflow DAG that runs a daily data export and deploy it to my environment"
+ "Build a YAML workflow for Amazon MWAA Serverless"
+ "Write a pipeline that orchestrates three tasks and schedule it to run every hour"

Use the following prompts to test workflows with the `testing-mwaa-workflow` skill.
+ "Test my DAG and watch it until it finishes"
+ "Trigger a test run of my workflow and report whether it succeeded"
+ "Smoke-test the pipeline I just deployed"

Use the following prompts to debug workflows with the `debugging-mwaa-workflow` skill.
+ "Find the root cause of my failed DAG"
+ "My DAG isn't showing up in the Airflow UI"
+ "Why is my worker running out of memory?"

Use the following prompts to upgrade environments with the `upgrading-mwaa-environments` skill.
+ "Upgrade my environment from Apache Airflow 2 to 3"
+ "Plan a blue-green upgrade that preserves my run history"
+ "Migrate my MWAA environment to a newer Apache Airflow version"

You don't need to name a skill in your prompt. Your assistant selects the matching skill automatically based on your request.

## Related resources
<a name="using-agent-skills-resources"></a>

For more information about the AWS agent skills for Amazon MWAA, see the following resources.
+ [Getting started](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html) in the Agent Toolkit for AWS User Guide.
+ The [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website.
+ The [AWS Data Analytics plugin](https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-data-analytics) on the GitHub website, which provides the Amazon MWAA skills.
+ The [AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) documentation.
+ The [Agent Skills open standard](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) on the Anthropic website.