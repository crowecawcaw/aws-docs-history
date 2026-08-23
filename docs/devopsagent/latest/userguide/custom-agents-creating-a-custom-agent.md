# Creating a custom agent

You can create a custom agent in two ways: using the form in the DevOps Agent web app, or through a guided conversation in Chat. Both methods result in the same custom agent configuration stored in your Agent Space.

Before creating a custom agent, you must have an Agent Space with at least one connected integration. For more information, see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md").

## Creating a custom agent using the form

The form lets you quickly create a custom agent by specifying a name, system prompt, and optional skills. To assign MCP tools to the agent, use Chat after creating the agent.

**To create a custom agent using the form:**

1. Navigate to the **Agents** page in your DevOps Agent web app.
2. In the **Custom Agents** section, choose **Create agent**.
3. In the dialog, choose **Form**.
4. Fill out the form:

   - **Name** – A unique identifier for your agent. Use lowercase letters, numbers, and hyphens only (maximum 64 characters). Must not start or end with a hyphen. Example: `weekly-health-report`
   - **System prompt** – Instructions that define what the agent does and how it operates, written in Markdown (minimum 10 characters, maximum 50,000 characters). For guidance on writing effective prompts, see [Writing a system prompt](#writing-a-system-prompt "#writing-a-system-prompt").
   - **Skills** (optional) – Select skills from your Agent Space that provide additional domain knowledge or capabilities to the agent. Use the search field to find skills by name.

5. Choose **Create agent**.

After creation, you are redirected to the agent's detail page where you can view the configuration, run the agent, or set up triggers.

## Creating a custom agent using Chat

Chat provides a guided, conversational experience for creating custom agents. This method is recommended when you want to assign MCP tools to the agent, or when you want assistance writing the system prompt.

**To create a custom agent using Chat:**

1. Navigate to the **Agents** page in your DevOps Agent web app.
2. In the **Custom Agents** section, choose **Create agent**.
3. In the dialog, choose **Chat**. The dialog closes and a new conversation opens in the Chat panel with a pre-composed message.
4. Chat guides you through a collaborative process:

   - **Intent clarification** – Confirms the purpose and scope of your agent.
   - **Duplicate check** – Verifies no similar agent already exists in your Agent Space.
   - **Tool and skill selection** – Proposes which MCP tools and skills the agent needs, and asks you to confirm.
   - **Output type** – Determines whether the agent should produce text responses, artifacts, or recommendations.
   - **System prompt draft** – Writes a system prompt and presents it for your review. You can iterate until you are satisfied.
   - **Confirmation** – Suggests a name and confirms all settings before creating the agent.

You can also create a custom agent by asking Chat directly at any time. For example:

```
Create an agent that generates a weekly report of all investigations from the past week.
```

```
Create a custom agent for checking certificate expiration across all accounts.
```

```
Make me an agent that audits DynamoDB table configurations daily.
```

## Importing a custom agent from a repository

You can import a custom agent's system prompt directly from a Markdown file in a GitHub repository. The file contents become the agent's system prompt. You can manage agent prompts in version control and import them with a single action.

**Prerequisites:**

- A GitHub account associated with your Agent Space. To connect a GitHub account, see [Connecting GitHub](connecting-to-cicd-pipelines-connecting-github.md "connecting-to-cicd-pipelines-connecting-github.md"). Any GitHub account connection enables importing from public repositories. For private repositories, the associated account must have read access to the repository. GitHub Enterprise Server and GitHub Enterprise Cloud with data residency connections are also supported.
- A Markdown file (`.md`) in a GitHub repository containing the system prompt.

**To import a custom agent from a repository:**

1. Navigate to the **Agents** page in your DevOps Agent web app.
2. In the **Custom Agents** section, choose **Create agent**.
3. In the dialog, choose **Import**. The dialog changes to the **Import from GitHub** view.
4. Fill out the form:

   - **Name** – A unique identifier for your agent. Use lowercase letters, numbers, and hyphens only (maximum 64 characters). Must not start or end with a hyphen.
   - **Repository URL** – A link to a single Markdown (`.md`) file containing the agent's system prompt. For example: `https://github.com/my-org/my-repo/blob/main/my-agent.md`. For GitHub Enterprise Server or GitHub Enterprise Cloud with data residency, use your instance URL instead. For example: `https://github.example.com/my-org/my-repo/blob/main/my-agent.md`. If the URL does not end in `.md`, a warning appears. The import fails if the file is not Markdown.
   - **Skills** (optional) – Select skills from your Agent Space to provide additional domain knowledge or capabilities to the agent.

5. Choose **Import agent**.

The repository file supplies only the system prompt. The name and skills come from the form.

After creation, you are redirected to the agent's detail page where you can view the configuration, run the agent, or set up triggers.

**Viewing imported agents:**

An imported agent displays a **Synced from GitHub** badge next to its name on the agent detail page, along with a **Last synced** timestamp and a link to the source file on GitHub. In the **Custom Agents** list, imported agents include a link to their source file.

If you edit an imported agent, the system prompt displays a **Read-only** label with a hint linking to the source file. The name and skills remain editable.

**Syncing imported agents:**

When you update the Markdown file in your repository, open the imported agent's detail page and choose **Sync** to pull the latest system prompt.

**Constraints:**

- **URL format** – Only GitHub URLs are accepted, including GitHub Enterprise Server and GitHub Enterprise Cloud with data residency. The connected GitHub account must match the URL host. For example, a `github.example.com` connection can only import from `github.example.com` URLs, not from `github.com` URLs.
- **Markdown file required** – The URL must point to a single `.md` file.
- **Maximum file size** – The file must not exceed 1 MB (GitHub API limit).
- **GitHub account required** – Your Agent Space must have an associated GitHub account to import agents. For private repositories, the account must have read access.

## Community custom agents

The [AWS DevOps Agent Tools repository](https://github.com/aws/tools-for-devops-agent "https://github.com/aws/tools-for-devops-agent") includes pre-built custom agent configurations for recurring operational tasks such as health reports, operational reviews, and service quota monitoring. The repository is maintained by the AWS DevOps Agent service team, and all contributions go through the same security review bar before being added. To browse what's available, see the [custom agents catalog](https://aws.github.io/tools-for-devops-agent/custom-agents/ "https://aws.github.io/tools-for-devops-agent/custom-agents/") on the GitHub website.

To use a community custom agent, import it from the repository using the **Import from repository** flow on the **Agents** page. Copy the URL of the agent's Markdown file and paste it as the repository URL. For details, see [Importing a custom agent from a repository](#importing-a-custom-agent-from-a-repository "#importing-a-custom-agent-from-a-repository").

## Writing a system prompt

The system prompt is the most important part of your custom agent. It defines the agent's purpose, approach, constraints, and expected output. A well-written prompt produces consistent, reliable results.

**Structure your system prompt with these sections:**

- **Goal** – What the agent should accomplish in a single sentence or short paragraph.
- **Approach** – Step-by-step procedures the agent should follow, referencing specific tool names it should call and in what order.
- **Constraints** – Boundaries on what the agent should and should not do. For example, read-only access, time ranges to consider, or services to exclude.
- **Output** – What the agent should produce and in what format. Specify whether it should generate text, create an artifact, or create a recommendation.

**Example system prompt:**

```
You are a DevOps reporting agent specializing in summarizing investigation activity.

## Goal
Generate a concise weekly report of all investigations from the past 7 days.

## Approach
1. Call `list_investigations` to fetch investigations from the last 7 days.
2. For each investigation, retrieve its title, status, root cause, and resolution time.
3. Group investigations by status and root cause category.
4. Identify trends: services most affected, average resolution time, recurring root causes.

## Constraints
- Only include investigations from the past 7 days.
- Read-only access — do not modify, close, or reassign investigations.

## Output
Produce a single artifact titled "Weekly Investigation Report" containing:
- A table listing each investigation with title, status, and resolution time.
- A chart showing investigation counts by root cause category.
- A summary paragraph with key trends and recommendations.
```

**Tips for effective system prompts:**

- **Be specific about tools** – Reference tool names directly (for example, `list_investigations`, `use_aws`, `query_cloudwatch_logs`) so the agent knows which tools to call.
- **Define success criteria** – Describe what a good output looks like so the agent knows when it is done.
- **Set boundaries** – Explicitly state what the agent should not do to prevent unintended actions.
- **Use Markdown formatting** – Headers, lists, and code blocks make the prompt easier for the agent to parse and follow.

## Configuring tools

MCP tools determine what actions your custom agent can perform during invocation. You select tools from the full set available in your Agent Space, including tools from connected AWS accounts, observability platforms, CI/CD pipelines, ticketing systems, and custom MCP servers.

Tools can only be configured through Chat. To assign tools when creating an agent, use the Chat creation method. To add or change tools on an existing agent, ask Chat to update the agent. For example:

```
Add the query_cloudwatch_logs and use_aws tools to my weekly-health-report agent.
```

```
Update certificate-checker to also use the list_resources tool.
```

```
Remove the use_kubectl tool from cluster-audit-agent.
```

When selecting tools, follow the principle of least privilege — assign only the tools the agent needs to accomplish its task. This reduces the risk of unintended actions and keeps the agent focused.

## Release Manager tools

Custom agents have access to Release Manager tools. These tools let your agent create, list, get, and cancel Release Manager tasks. Your agent can also analyze a release readiness review report to surface findings and recommended actions.

To use Release Manager tools, assign them to your custom agent through Chat. For example:

```
Add the release manager tools to my release-pipeline-agent.
```

For more information about release management capabilities, see [Release management](working-with-devops-agent-release-management-index.md "working-with-devops-agent-release-management-index.md").

## Configuring skills

Skills provide your custom agent with additional domain knowledge, investigation procedures, or specialized capabilities. When a custom agent runs, it loads its assigned skills and can reference their instructions during invocation.

You can assign skills during creation (using either the form or Chat) or add them later by editing the agent. Skills assigned to a custom agent must already exist in your Agent Space. For more information about creating skills, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md "about-aws-devops-agent-devops-agent-skills.md").

Custom agents also have built-in capabilities for creating artifacts and recommendations that do not require skill assignment. For more information, see [Custom agent outputs](custom-agents-custom-agent-outputs.md "custom-agents-custom-agent-outputs.md").

You can assign up to 200 skills per custom agent. Choose skills that are relevant to the agent's purpose to reduce context consumption and improve agent focus.
