

# Recommend third-party applications in agent assist
<a name="agent-assist-recommend-3p-apps"></a>

Agent assist can recommend the third-party application that best solves the customer problem, such as an order management system or a ticketing tool. The recommendation appears as a button, and agents choose it to open the application in the agent workspace.

## How it works
<a name="agent-assist-recommend-3p-apps-how"></a>

During a contact, the AI agent follows the conversation. When it decides that an application could help, it uses the `get_app_catalog` tool to list the applications available to the agent. The agent doesn't need to ask. The AI agent compares the customer's request with each application's name and description, and recommends the best match.

The AI agent can recommend an application only when all of the following are true:
+ The application is a **Standard application** integration that is associated with your instance.
+ The application's **{{Application name}} - Access** permission is on a security profile assigned to the AI agent.
+ The same permission is on a security profile assigned to the agent who is handling the contact.

To recommend applications, use a custom AI agent. You can add a security profile to a custom AI agent so that you can set which applications it can recommend. You can assign security profiles only to custom AI agents, not to the system AI agent, **AgentAssistanceOrchestrator**.

## Prerequisites
<a name="agent-assist-recommend-3p-apps-prereqs"></a>
+ Interactive responses set up with a custom AI agent, with the **Button** component allowed. For more information, see [Step 5 (optional): Create a custom AI agent](agent-assist-interactive-responses.md#agent-assist-interactive-responses-custom).
+ Third-party applications added to your instance. For more information, see [Integrate third-party applications in the agent workspace](3p-apps.md).

## Step 1: Describe your applications
<a name="agent-assist-recommend-3p-apps-step1"></a>

The AI agent chooses an application by its name and description. An application with no description, or a vague one, is less likely to be recommended.

On each application's integration page, enter a description that says what the application is for and what agents can do in it. For example, for a shipment tracker: "Look up a customer's order status, track shipments, and start returns or refunds."

## Step 2: Give the AI agent access to your applications
<a name="agent-assist-recommend-3p-apps-step2"></a>

1. In the security profile assigned to your custom AI agent, under **Agent Applications**, enable **{{Application name}} - Access** for each application that you want the AI agent to recommend. For more information, see [Create a security profile in Connect Customer](create-security-profile.md).

1. If the AI agent doesn't have that security profile yet, open the AI agent's **Agent builder** page. In **Security Profiles**, select the profile, and then choose **Save**.

## Step 3: Give agents access to your applications
<a name="agent-assist-recommend-3p-apps-step3"></a>

Enable the same **{{Application name}} - Access** permissions on your agents' security profiles. The AI agent leaves out any application that only one of them can access. For more information, see [Assign permissions to use third-party applications](assign-security-profile-3p-apps.md).

## Step 4: Check the AI agent's tools
<a name="agent-assist-recommend-3p-apps-step4"></a>

On the AI agent's **Agent builder** page, check that **Tools** includes `get_app_catalog`. AI agents copied from AgentAssistanceOrchestrator include it. If it's missing, add it from the **Amazon Connect** namespace. For more information, see [Add a tool](agent-assist-interactive-responses.md#agent-assist-interactive-responses-add-tool).

The tool's **Instructions** tell the AI agent when to use it. To change when the AI agent recommends applications, edit the instructions. For example: "When the customer's request maps to a task done in a specific application, call get\_app\_catalog and recommend the matching application by name."

Then publish the AI agent and use it for agent assistance. For more information, see [Publish and use the AI agent](agent-assist-interactive-responses.md#agent-assist-interactive-responses-publish).

## Troubleshooting
<a name="agent-assist-recommend-3p-apps-troubleshoot"></a>


| Issue | Likely cause | Fix | 
| --- | --- | --- | 
| An application is never recommended. | The application isn't a Standard application, isn't associated with your instance, or is missing Access on the AI agent's or the agent's security profile. | Check the integration type and association, and enable the permission on both security profiles. | 
| No application is ever recommended. | The contact uses the system AI agent, or the custom AI agent has no security profile. | Select your custom AI agent for agent assistance, and assign it a security profile. | 
| The AI agent recommends the wrong application. | The application descriptions are missing or vague. | Describe what each application is for and what agents can do in it. | 
| A new application or permission doesn't take effect. | A newly associated application takes up to 10 minutes to appear in security profiles. The AI agent's list of applications updates up to 5 minutes after a change. | Wait up to 15 minutes after a change. | 
| get\_app\_catalog isn't in the list of tools. | The AI agent isn't an orchestration AI agent. | Create an AI agent with the Orchestration type. | 
| The AI agent reports Error: Failed to retrieve application catalog. | The tool call failed. | Refresh the agent workspace and try again. If the error continues, contact AWS Support. | 