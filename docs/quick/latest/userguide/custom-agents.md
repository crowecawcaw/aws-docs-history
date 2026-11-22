

# Create and configure agents

You can create an agent by describing it in chat, or by importing an agent definition file. You need permission to create agents. If you don't see the option to create an agent, contact your administrator. A new agent is private. Only you can use it until you publish and share it.

**Topics**
+ [Create an agent](#create-agent)
+ [Configure an agent](#configure-agent)
+ [How agents use resources](#how-agents-use-resources)
+ [Test and publish an agent](#test-publish-agent)
+ [Best practices for agent context](#agent-knowledge-sources-best-practices)

## Create an agent
<a name="create-agent"></a>

You can create an agent from chat or from an agent definition file.

------
#### [ From chat ]

**To create an agent from chat**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Choose **Create**, and then choose **From chat**. You can also start a chat and ask Quick to create an agent.

1. Describe what you want the agent to do. Include its goal, who uses it, and what it produces.

1. Review the draft configuration. Quick suggests a name, description, and instructions.

1. Refine the draft through conversation, or edit the fields directly.

1. Test and publish the agent. For more information, see [Test and publish an agent](#test-publish-agent).

------
#### [ From file ]

**To create an agent from a file**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Choose **Create**, and then choose **From file**.

1. Select the agent definition file.

1. Review and refine the draft, and then publish it.

------

## Configure an agent
<a name="configure-agent"></a>

The agent editor organizes configuration into two tabs, **Instructions** and **Capabilities**.

------
#### [ Instructions ]

The **Instructions** tab holds the following fields:

**Name**  
The name people use to find and mention the agent.

**Description**  
A short summary of what the agent does.

**Instructions**  
The agent's goals, behavior, workflow, and boundaries.

**Welcome message and starter prompts**  
What people see when they start a chat with the agent.

Instructions support rich formatting, including headings, lists, emphasis, code, and quotes. You can enter up to 50,000 characters. In the **Instructions** field, enter @ to reference a space, connector, skill, or another agent. Referencing another agent lets this agent hand work to it. For more information, see [Multi-agent orchestration](use-agents.md#multi-agent-orchestration).

------
#### [ Capabilities ]

The **Capabilities** tab holds the following settings:

**Web search**  
Allows the agent to search the web.

**Skills**  
The skills the agent can use. By default, an agent can use all skills. If you add specific skills, the agent is limited to those skills. Remove them to allow all skills again. For more information, see [Teach agents with skills](working-with-skills.md).

**Spaces**  
The spaces the agent uses as its primary knowledge sources.

**Connectors**  
The connectors and actions the agent can use.

**Reference documents**  
Files that give the agent fixed context. You can add up to 10 reference documents, up to 50 MB in total, and up to 100,000 characters of extracted text. The supported file types are `.pdf`, `.txt`, `.html`, `.md`, `.csv`, `.doc`, and `.docx`.

------

## How agents use resources
<a name="how-agents-use-resources"></a>

The spaces and connectors you add to an agent are its primary sources, and the agent uses them first. When a request needs it, the agent can also use other spaces and connectors you have access to. Adding spaces or connectors focuses the agent. It doesn't prevent the agent from using other resources you can access. An agent never goes beyond your access.

Skills work differently. If you add specific skills, the agent is limited to those skills.

## Test and publish an agent
<a name="test-publish-agent"></a>

Agents are versioned. Changes are saved as a draft. Other people use the published version, and routines run the published version.

**To test and publish an agent**

1. Open the draft.

1. Test the agent in chat, and then refine it.

1. Choose **Publish**.

1. (Optional) Add release notes.

Publishing replaces the version that others use. To remove unpublished changes, discard the draft. To switch between the published and draft versions, use **Manage versions**.

## Best practices for agent context
<a name="agent-knowledge-sources-best-practices"></a>

An agent uses three types of context, and each type is best suited to a different kind of content:

**Instructions**  
Goals, behavior, and when to use each source. Instructions apply to every conversation.

**Reference documents**  
Exact wording, templates, procedures, and rules. The agent uses them as written, and they are always available.

**Spaces**  
Business content that changes, such as documents, dashboards, and datasets. The agent searches spaces when needed, and respects each user's permissions.

We recommend the following practices:
+ Use instructions to set the agent's role and goals.
+ Use reference documents for content that must not change.
+ Use spaces for knowledge that changes over time.
+ Add only the capabilities the agent needs.