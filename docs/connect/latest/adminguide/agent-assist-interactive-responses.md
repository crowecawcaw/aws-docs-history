

# Use interactive responses in agent assist
<a name="agent-assist-interactive-responses"></a>

Agent assist can send interactive responses, not just text. During a voice or chat contact, the AI agent can respond in-line in the conversation with a view containing details from the conversation and buttons that open step-by-step guides, cases, and customer profiles. Agents can click to respond, without leaving the conversation.

## How it works
<a name="agent-assist-interactive-responses-how"></a>

Agent assist can respond in two ways:
+ **Proactively**: as soon as the customer describes an issue where agent assist can help, agent assist can respond, before the agent types.
+ **In response to a message**: when an agent asks a question, agent assist responds.

The AI agent then decides whether to respond in plain text or with an interactive response. An interactive response is a view. The AI agent uses the views that you've defined first. If no view fits the use case and you've allowed more UI components in a custom AI agent, it composes its own view, such as a card, summary, or short form. For more information, see [Step 5 (optional): Create a custom AI agent](#agent-assist-interactive-responses-custom). Otherwise, it answers in plain text.

Agent assist checks each interactive response before it appears. The check rejects unsafe links, and components or actions that don't exist or that the AI agent isn't allowed to use.

If a response doesn't pass the check, the agent sees **Unable to complete the request.** and a **Retry** button. **Retry** asks the AI agent to correct the response, up to 3 times per request.

## Prerequisites
<a name="agent-assist-interactive-responses-prereqs"></a>
+ AI agents set up for your instance, with a domain and a knowledge base. For more information, see [Initial set-up for AI agents](ai-agent-initial-setup.md).
+ A Connect assistant block in the flows that route contacts to your agents. For more information, see [Flow block in Connect Customer: Connect assistant](connect-assistant-block.md).
+ For proactive responses on voice contacts: real-time conversational analytics enabled in the flow.
+ For chat contacts: message streaming enabled for AI-powered chat. Without it, interactive responses don't appear in chat. For more information, see [Enable message streaming for AI-powered chat](message-streaming-ai-chat.md).
+ Optional: Cases and Customer Profiles enabled, for the Cases and Customer Profiles buttons. For more information, see [Enable Cases](enable-cases.md) and [Enable Customer Profiles for your instance](enable-customer-profiles.md).

## Step 1: Enable interactive responses
<a name="agent-assist-interactive-responses-step1"></a>

Interactive responses use the **AgentAssistanceOrchestrator** system AI agent. Enable it for all contacts or for one flow.
+ **All contacts**: In **AI agent designer**, choose **AI agents**. Under **Default AI Agent Configurations**, set **Answer recommendation** to **N/A**. With no answer recommendation AI agent selected, agent assist uses AgentAssistanceOrchestrator. This is the same setting that turns on proactive recommendations.
+ **One flow**: In the Connect assistant block, select the orchestration AI agent to use for agent assistance. Use this option to pilot interactive responses on one queue.

## Step 2: Make your views discoverable
<a name="agent-assist-interactive-responses-step2"></a>

The AI agent finds published views only, up to 100 per search.

1. Publish the view.

1. Name and describe the view in the words your customers use. The AI agent matches requests to the name and description.

1. Declare the view's inputs in its input schema. The AI agent fills in the inputs from the conversation. It doesn't show a view whose required inputs it can't fill.

To build a view, see [Use views to customize the user interface for agents, customers, and other user personas in Connect Customer](view-resources-sg.md).

## Step 3: Make your step-by-step guides discoverable
<a name="agent-assist-interactive-responses-step3"></a>

The AI agent finds published guides tagged `Guide` = `true` only, up to 100 per search. To tag your guides, see [Tag step-by-step guides so the AI agent can find them](integrate-guides-with-ai-agents.md#integrate-guides-tag).

## Step 4: Assign permissions to agents
<a name="agent-assist-interactive-responses-step4"></a>

Add the following permissions to your agents' security profiles:
+ **Workspace Applications**: **Connect assistant - View**, to see agent assist and its responses.
+ **Agent Applications**: **Custom views - Access**, to see views and step-by-step guides in the agent workspace.
+ **Views - View**, to see the views that you've built.
+ **Cases** and **Customer profiles** (View, Create, Edit), for the matching buttons.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

## Step 5 (optional): Create a custom AI agent
<a name="agent-assist-interactive-responses-custom"></a>

Create a custom AI agent to change what the AI agent can do, such as letting it compose its own layouts. You can't edit AgentAssistanceOrchestrator, so start from a copy.

### Create the AI agent
<a name="agent-assist-interactive-responses-create"></a>

1. In **AI agent designer**, choose **AI agents**, and then choose **Create AI agent**.

1. For **AI agent type**, choose **Orchestration**.

1. For **Copy from existing**, choose **AgentAssistanceOrchestrator**. The copy includes every tool for interactive responses, with the settings in the following table.

To build an AI agent from scratch instead, leave **Copy from existing** empty and add the tools yourself. For more information, see [Add a tool](#agent-assist-interactive-responses-add-tool).

### Tools for interactive responses
<a name="agent-assist-interactive-responses-tools"></a>


| Tool | What it does | Values set for every call (Override Input Values) | Permission the AI agent needs | 
| --- | --- | --- | --- | 
| SearchViews | Finds your views. | Published views only (SearchCriteria = {"ViewStatusCondition": "PUBLISHED"}). Up to 100 results (MaxResults = 100). | Views - View | 
| SearchGuides | Finds your step-by-step guides. | Guides tagged Guide = true only (SearchFilter). Published guides only (SearchCriteria). Up to 100 results (MaxResults = 100). | Contact Control Panel - Access Contact Control Panel | 
| SearchUICatalog | Returns the UI components and actions the AI agent can use in a response. | The views catalog (catalogId = views), limited to the components you choose. Default: Button and ViewReference. | Connect assistant - View | 
| ComposeUI | Sends the finished response to agent assist. | None. | Connect assistant - View | 
| ListUICatalog (optional) | Returns every component and action in the views catalog, including the ones you haven't allowed. | catalogId = views. | Connect assistant - View | 

### Choose the UI components
<a name="agent-assist-interactive-responses-components"></a>

By default, the AI agent uses two components:
+ **Button**: offers one-click actions. It starts a guide, opens an app, opens a case or a customer profile, or sends the agent's choice back to the AI agent.
+ **ViewReference**: shows one of your views, filled in with data from the conversation.

To let the AI agent compose its own layouts, allow more components:

1. In your AI agent's **Tools**, select **SearchUICatalog**, and then choose **Edit**.

1. In **Components**, select the components the AI agent can use, such as Card, Header, AttributeSection, and Alert. The list shows every component in the views catalog.

1. Choose **Update**. Then save and publish the AI agent.

Keep at least one component selected. The AI agent uses only the components that you select, and the check rejects any other.

### Add a tool
<a name="agent-assist-interactive-responses-add-tool"></a>

Add a tool only when you build an AI agent from scratch, or to restore a tool you removed.

1. On the AI agent's **Agent builder** page, go to **Tools**, and then choose **Add tool**.

1. In **Add AI Tool**, choose **Add existing AI Tool**.

1. For **Namespace**, choose **Amazon Connect**. For **AI Tool**, choose the tool, such as **SearchGuides**.

1. Review the settings that the console fills in. Keep them unless you have a reason to change them.
   + **Instructions**: tell the AI agent when and how to use the tool. Add to them only for guidance specific to your business.
   + **Override Input Values**: values sent on every call, which the AI agent can't change. These values limit `SearchViews` to published views and `SearchGuides` to tagged guides.
   + **Components** (`SearchUICatalog` only): the UI components the AI agent can use. Select at least one.
   + **User Confirmation**: leave off. When it's on, the agent must approve every call.

1. Choose **Add**.

### Assign security profiles to the AI agent
<a name="agent-assist-interactive-responses-ai-security"></a>

An AI agent can use only the tools that its security profiles allow. Without them, its tool calls fail.

1. On the **Agent builder** page, go to **Security Profiles**, and select profiles that grant the permissions in the tools table.

1. Check the **Permissions** column of the **Tools** table. It shows whether a profile covers each tool.

1. For the Cases and Customer Profiles buttons, add Cases and Customer profiles permissions (View, Create, Edit).

For more information, see [Assign security profile permissions to AI agents](ai-agent-security-profile-permissions.md).

### Publish and use the AI agent
<a name="agent-assist-interactive-responses-publish"></a>

1. Choose **Publish**.

1. Set the AI agent as the default for **Agent Assistance**, as in Step 1, or select it in a flow's Connect assistant block.

## Step 6: Test interactive responses
<a name="agent-assist-interactive-responses-test"></a>

In the agent workspace, open agent assist, and accept a test chat that goes through a flow with the Connect assistant block. As the customer, describe an issue that one of your views covers, and check that the view appears. Then, in agent assist, ask to see something and to do something.

## Troubleshooting
<a name="agent-assist-interactive-responses-troubleshoot"></a>


| Issue | Likely cause | Fix | 
| --- | --- | --- | 
| The AI agent doesn't show a view. | The view isn't published, its name and description don't match the request, or the agent lacks Views - View. | Publish the view, describe it in your customers' words, and check the agent's security profile. | 
| No guide button appears, or the guide doesn't open. | The guide isn't published or isn't tagged Guide = true, or the agent lacks Custom views - Access. | Publish the guide, check the tag's case, and check the agent's security profile. | 
| No proactive responses on voice contacts. | Real-time conversational analytics is off in the flow. | Add real-time conversational analytics to the flow. | 
| The agent sees Unable to complete the request. | The response didn't pass the check. | Choose Retry. Agent assist retries up to 3 times per request. | 