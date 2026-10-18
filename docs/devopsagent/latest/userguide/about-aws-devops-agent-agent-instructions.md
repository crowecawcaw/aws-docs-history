

# Agent instructions
<a name="about-aws-devops-agent-agent-instructions"></a>

Use agent instructions to provide always-on guidance that AWS DevOps Agent applies to every session. A session is a single conversation or investigation with an agent.

Unlike [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md), which load on demand when the agent matches a skill description to the current task, agent instructions are always present from the start of every session, regardless of what the agent is working on.

You set agent instructions from each [Managed agents](working-with-devops-agent-managed-agents.md) on the **Agents** page in your [What is a DevOps Agent Web App?](about-aws-devops-agent-what-is-a-devops-agent-web-app.md). There you set both the shared global instructions that apply to every agent and the instructions specific to that agent. Instructions are stored as an AGENTS.md file.

## What are agent instructions
<a name="what-are-agent-instructions"></a>

Agent instructions provide unconditional, always-on guidance for your agents. At the start of every session, the agent service retrieves the instructions configured for your Agent Space and injects their content directly into the agent system prompt. The agent does not decide whether to load them; they are always present.

Agent instructions are stored as AGENTS.md files and differ from [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md) in several important ways:


| Aspect | Skill | Agent instructions (AGENTS.md) | 
| --- | --- | --- | 
| Name and description | Required | Not applicable | 
| Content format | Markdown or ZIP bundle | Markdown only | 
| Resource files | Supported | Not supported | 
| Context injection | On demand (agent decides via skill description matching) | Always (unconditional, every session) | 
| Uniqueness | Multiple per Agent Space | One global set plus one set per managed agent | 

Agent instructions have no name or description field. The underlying AGENTS.md file contains only markdown with no frontmatter, no ZIP bundle support, and no resource files.

## Why use agent instructions
<a name="why-use-agent-instructions"></a>

Agent instructions give you a reliable way to ensure certain guidance is always in context, without depending on the agent's skill-loading decisions.

**Key benefits:**
+ **Predictability:** Instructions are always present, regardless of what task the agent is working on. No description matching is required, and the agent cannot skip the content.
+ **Guaranteed coverage:** Unlike Skills, which the agent may or may not load depending on task relevance, agent instructions are always injected at the start of every session.
+ **Standing policies:** Use agent instructions for standing operational policies, security guidelines, coding standards, or any guidance that must apply to every session without exception.
+ **Targeted scope:** You can apply instructions to all agent types at once using global instructions, or restrict instructions to a specific agent type when the guidance is relevant only to that agent's work.

## How agent instructions work
<a name="how-agent-instructions-work"></a>

When a session starts, the agent service retrieves the instructions configured for your Agent Space and injects their content into the agent system prompt before the session begins. This happens automatically for every session. The agent does not evaluate whether to load them; it always injects the content.

Each new session loads the instructions fresh at startup. If you update your instructions, the change takes effect immediately for sessions that start after you save. Sessions that are already in progress continue using the content that was loaded when they started.

Scoping determines which instructions a session receives. Global instructions apply to all agent types in your Agent Space, so every session receives them. Agent-specific instructions apply only to sessions of that particular agent type. A session receives instructions from both the global instructions and the relevant agent-specific instructions.

## Agent type scoping
<a name="agent-type-scoping"></a>

Scoping controls which agent sessions receive a given set of instructions. There are two scoping options:
+ **Global instructions:** Applies to all agent types in your Agent Space. Every agent session receives this content.
+ **Agent-specific:** Applies only to sessions of the selected agent type.

The managed agents available for agent-specific instructions are:
+ **Chat** - Ad-hoc questions and requests during chat sessions.
+ **Incident triage** - Alarm filtering, severity classification, and initial scoping.
+ **Incident RCA** - Root cause analysis with evidence collection and validation.
+ **Incident mitigation** - Short-term remediation and long-term fix recommendations.
+ **Incident UI** – Generation of an investigation's outputs, including those posted to other platforms.
+ **Evaluation** - Agent performance scoring and policy compliance checks.
+ **Grader** – Quality assessment of a completed investigation. This is the agent behind a Review. For more information, see [Reviewing investigations](working-with-devops-agent-reviewing-investigations.md).
+ **Release testing** – Automated UI and API testing against deployed web applications and REST APIs.
+ **Learning** - Produces and refreshes managed knowledge by reviewing your agent space's past investigations, pipelines, and dependencies. It covers skills, monitor memories, and topology understanding.

## Content size guidance
<a name="content-size-guidance"></a>

Every time you start a conversation or investigation, the agent reads your entire instructions before doing anything else. The agent has a fixed amount of working memory per session, and your instructions use some of it. The larger the file, the less room remains for your questions, investigations, the logs the agent reads, and its own reasoning. Shorter, focused instructions give the agent more capacity to solve your problem.

**Note:** The hard limit is 25 KB. A recommended size of about 120 lines works well for most configurations.

Focus your instructions on guidance that must be present in every session. For specialized investigation procedures that apply only to specific tasks, consider using [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md) instead.

## Example
<a name="example"></a>

The following example shows well-formed agent instructions with investigation guidance, response formatting standards, and security requirements that apply to every agent session.

```
# Agent Instructions

## Investigation approach
- Always check CloudWatch alarms and recent deployments before proposing a root cause.

## Response format
- Lead with a one-sentence summary of findings before listing details.
- Include the AWS region and resource identifier for any resource you reference.
- Use bullet points for lists of findings or recommendations.

## Security
- Never log, display, or suggest storing credentials or secrets in plaintext.
- When recommending IAM changes, follow least-privilege principles.
```

## Setting agent instructions
<a name="setting-agent-instructions"></a>

Before setting agent instructions, you must have an Agent Space. For more information, see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md).

**Important:** Agent instructions have moved from the **Knowledge** page to the **Agents** page. The **Instructions** tab on the **Knowledge** page no longer lists the agents; it shows a notice pointing to the **Agents** page.

Each agent has exactly one set of instructions. When you save new content, it overwrites the existing content for that agent.

Set instructions from each managed agent's page on the **Agents** page. Open a managed agent to see its **Agent definition** tab, which contains two sets of instructions:
+ **Global instructions (AGENTS.md)** - Shared across all managed agents. Every agent session in your Agent Space receives this content in addition to its own agent-specific instructions. Because a change here affects every agent, saving global instructions asks you to confirm first.
+ **Agent instructions (AGENTS.md)** - Owned by the managed agent whose page you are on. Only sessions of that agent receive this content.

**To set global instructions (applies to all agents):**

1. Navigate to the **Agents** page in your Agent Space Operator Web App and find the **Managed agents** section.

1. Choose a managed agent to open its page.

1. On the **Agent definition** tab, edit the **Global instructions (AGENTS.md)** section.

1. Choose **Save** and confirm. The global instructions apply to all agent types in your Agent Space.

The updated global instructions take effect for every agent session that starts after you save.

**To set instructions for a specific agent:**

1. On the **Agents** page, open the managed agent from the **Managed agents** section.

1. On the **Agent definition** tab, edit the **Agent instructions (AGENTS.md)** section for that agent.

1. Choose **Save**.

Only that agent's sessions receive this content.

## Managing agent instructions
<a name="managing-agent-instructions"></a>

AWS DevOps Agent provides management capabilities for agent instructions through the Operator Web App.

**Viewing instructions:** Open the managed agent's page from the **Agents** page and go to the **Agent definition** tab. Each instructions section shows the current content. Use the **Preview** view to see the rendered markdown or the **Code** view to see the raw markdown.

**Editing instructions:** Open the agent as described above, modify the content in the editor, and choose **Save**.

**Uploading instructions from a file:** Open the agent, then choose the **Upload** button in the editor to upload a markdown file from your computer.

**Downloading instructions:** Open the agent, then choose the **Download** button in the editor to download the current content as a file.

**Deleting instructions:** Open the agent, choose the **Delete** button in the editor, and confirm the deletion. This action cannot be undone. Consider downloading the content first if you may need it again.