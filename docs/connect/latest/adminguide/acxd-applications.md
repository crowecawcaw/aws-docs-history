# Working with applications

An application is the control center for the conversational AI application your users
interact with. You might think of it as your "bot."

From the agentic CX designer application page, you can:

- Organize the flows the application can handle
- Define default behavior for entry, unknown, fallback, or escalation scenarios
- Attach guardrails to user inputs and application outputs
- Create builds for testing and deployment

## Creating an application

###### To create an application

1. Select **Applications** from the workspace menu.
2. Select **Create application**.
3. Enter a clear application name.
4. Select **Create**.

Use a name that helps teammates quickly understand the purpose of the
application.

## Adding flows to an application

Once you've designed the workflows and necessary resources in your workspace,
you can come back to the **Design** tab of your application and attach the flows your
application should use, the default behavior, and any guardrails.

To start, flows define what your application can do.

###### To add flows

1. Open the application > Select the **Design** tab.
2. Choose one or more flows from the workspace to attach.
3. Save your changes.

## Configuring default behavior

Default behavior determines which flow runs when the application needs a
standard starting point, recovery path, or escalation path.

###### To configure default behavior

1. Open the application > Select the **Design** tab.
2. Select the edit icon under the Flows section OR select the three-dot menu
   beside each attached flow to manage defaults.
3. Assign the appropriate flow for each behavior.
4. Save your changes.

You may choose to assign the same flow to one or more defaults, depending on the
user experience.

|                |                                                                                                                                                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Welcome**    | Runs when a new conversation session starts. Use this flow to greet the user, set<br>expectations, and begin the experience.                                                                                                     |
| **Unknown**    | Runs when the application cannot match the user's message to a supported flow or<br>choice AND no match pathways in your flow are not defined. Use this flow to recover,<br>ask clarifying questions, or check a knowledge base. |
| **Fallback**   | Runs when the application needs to recover from issues such as repeated<br>incomprehension, timeout, integration failure, or state-related errors.                                                                               |
| **Escalation** | Runs when the application should move the user toward human support or another<br>controlled escalation path.                                                                                                                    |

## Attaching guardrails

Guardrails help control user inputs and application outputs during conversations.

Attach guardrails when the application needs safety, compliance, brand, privacy, or
policy controls.

###### To add guardrails

1. Open the application > Select the **Design** tab.
2. Select **Add guardrail**.
3. Choose one or more guardrails from the workspace.
4. Save your changes.

Be mindful that guardrails and the number of rules within each can add latency to
your application.

Once you have attached and configured flow behavior and guardrails, you can
move to the next phase of builds and deployments for your application.

###### Topics

- [Builds and deployments](acxd-builds-deployments.md "acxd-builds-deployments.md")
- [Testing](acxd-testing.md "acxd-testing.md")
