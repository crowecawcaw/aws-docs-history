

# Using the Live Sync agent node
<a name="acxd-live-sync"></a>

Live Sync enables bidirectional web or mobile conversations where the AI can respond to the user and coordinate actions on the frontend experience.

Use Live Sync when your application should do more than exchange messages. A Live Sync experience can help users navigate pages, fill forms, select options, trigger custom UI behavior, and understand what the user is currently viewing.

For example, a user might say "I'd like to check out on Saturday and pick the Ocean View room." With Live Sync, the agent can understand the request, use the current page context it's provided, fill the checkout date field, select the matching room option, and continue the conversation hands-free.

Live Sync is a bidirectional experience between your agentic CX designer application and your frontend.

It allows an AI-powered conversation to:
+ Understand user speech or text
+ Receive real-time frontend context
+ Navigate pages
+ Fill form fields
+ Trigger custom frontend actions
+ Return structured action payloads to your application

Live Sync is used with the Touchpoint SDK and Context API, which connects the conversational experience to your web or mobile frontend.

## Live Sync components
<a name="acxd-live-sync-components"></a>

A Live Sync experience usually includes:


|  |  | 
| --- |--- |
| **Agent flow** | Contains the Live Sync node that manages the conversation and tools. | 
| **Custom actions** | Define what the agent can ask the frontend to do. | 
| **Touchpoint SDK** | Renders the conversation and listens for bidirectional commands. | 
| **Command handlers** | Execute actions such as navigating, selecting an item, opening a modal, or filling a form. | 
| **Context API** | Sends current page and UI context back to the agent. | 

The frontend and the Live Sync agent work together. The agent decides what action should happen, and the frontend performs the action through registered command handlers.

## Creating a Live Sync flow
<a name="acxd-live-sync-create"></a>

**To create a Live Sync flow**

1. Open **Flows** from the workspace menu.

1. Select **Canvas**.

1. Create a new flow or open an existing flow.

1. Add the Live Sync node that will power the Live Sync experience.

1. Configure the node prompt, tools, actions, and paths.

1. Save the flow.

The agent node should be responsible for the Live Sync task, such as helping the user update a reservation, complete a form, or choose from available options.

## Agent prompt
<a name="acxd-live-sync-prompt"></a>

The agent prompt should clearly explain what the agent is responsible for and how it should behave.

A strong Live Sync prompt should include:
+ The agent's role and persona
+ The task or tasks the agent can complete
+ What the agent should not do
+ Tone and brevity expectations
+ When to use tools
+ When to trigger frontend actions
+ How to handle multimodal or page-aware interactions
+ Any context variables the agent should consider

## Tools
<a name="acxd-live-sync-tools"></a>

Tools extend what the Live Sync agent can do.

Use tools when the agent needs to retrieve information, answer grounded questions, execute structured workflows, or collect data.

Supported tool patterns may include:


|  |  | 
| --- |--- |
| **Data requests** | Retrieve, send, or update data through a configured custom integration. | 
| **Knowledge bases** | Answer questions from approved Q&A or document content. | 
| **Flows** | Run a structured workflow as a handover or MCP-enabled tool. | 
| **Data capture** | Collect required or optional slot values from the user. | 
| **Modalities** | Present structured UI, such as cards, carousels, or date input, when supported. | 

Add only the tools the agent needs for the Live Sync task.

For example, do not create a Data request if the frontend already has the information and only needs the agent to pass a selected value. In that case, configure a Live Sync custom action and let the frontend handle the behavior.

Use a Data request when the agent needs to call an external system that the frontend does not already handle, such as checking availability, retrieving a customer profile, or submitting a backend update.

Each tool should include a short description that explains when and how the agent should use it.

A clear tool prompt helps the agent decide:
+ Whether the tool is relevant
+ What information to collect first
+ What values to pass
+ What the tool returns
+ What to do if the tool fails or returns no results

Example knowledge base tool prompt:

```
Use this knowledge base to answer questions about hotel policies,
cancellation rules, check-in requirements, and room upgrade
eligibility. If no answer is found, do not guess.
```

Use **Data capture** when the agent needs to collect structured slot values from the user for use with other tools.

Examples:
+ Name
+ Email address
+ Confirmation number
+ Checkout date
+ Room preference
+ Appointment date
+ Account identifier

Before adding slots to Data capture, attach the slots to the flow in the flow settings.

In the agent instructions, refer to slot names in plain text rather than placeholder syntax.

Good example:

```
Collect customerEmail before calling the newsletterSignup tool.
```

Avoid using placeholder syntax when simply telling the agent what to collect:

```
Collect {firstName}, {lastName}, and {customerEmail}.
```

Use placeholders when mapping resolved values into tool input fields.

## Flow tools
<a name="acxd-live-sync-flow-tools"></a>

Live Sync agents can use flows in two ways: *handover* or *MCP-enabled*.

Use an MCP-enabled flow when the agent should stay in control while calling a structured workflow.

This is often the preferred flow-tool pattern for Live Sync because the agent can call the flow, receive the result, and continue supporting page-aware actions, navigation, form fill, and custom frontend behavior.

Use MCP-enabled flows for tasks such as:
+ Sending a confirmation message
+ Reading legal language and collecting consent
+ Retrieving disruption details
+ Running a structured eligibility check

Use a handover flow when you intentionally want a deterministic flow to take over the conversation.

While the handover flow is running, the Live Sync agent is no longer orchestrating frontend actions or page-aware behavior. The conversation follows the handover flow's nodes and messages until it returns to the agent.

To return from a handover flow to the Live Sync node, add a Redirect node at the end of the handover flow and route it back to the agent flow and node using the Live Sync's node ID (retrieved in the three-dot menu of a node).

## Live Sync actions
<a name="acxd-live-sync-actions"></a>

Live Sync actions tell the agent what it can understand about the user's current screen and what it can ask the frontend to do.

This is where Live Sync becomes bidirectional:
+ The *input schema* gives the agent structured awareness of what the user is seeing or what options are available on the page.
+ The *output schema* defines the structured command or value the agent can send back to the frontend.
+ The frontend command handler receives that output and performs the UI action.

Without an input schema, the agent does not have structured awareness of the relevant screen content for that action, such as visible form fields, selectable products, or valid navigation destinations.

Without an output schema, the agent does not have a structured way to tell the frontend what action to take or what value to use.

This gives your business control over what the agent can see, decide, and trigger. Instead of giving the agent broad control over the entire frontend, you define specific approved actions, the exact data the agent can consider, and the exact response shape the frontend will accept.

Live Sync actions include:
+ Navigate to a page
+ Fill a form field
+ Select an item
+ Open or close a modal
+ Highlight an option
+ Apply a filter
+ Update a visible UI state
+ Trigger a custom frontend behavior

When configuring a custom action, provide:


|  |  | 
| --- |--- |
| **Action name** | A stable identifier your frontend listens for, such as `select_room`. | 
| **Description** | A clear description of when the agent should use the action. | 
| **Input schema** | The structured screen context or available options the agent can consider before taking action. | 
| **Output schema** | The structured value or command the agent sends back to the frontend. | 
| **Scope tags** | Optional tags that limit when the action is available based on the current page or UI state. | 

The action name and schema must match what your frontend command handler expects.

Example: Use this action when the guest asks to select a room from available options shown on the page.


| Field | Value | 
| --- | --- | 
| Action name | select\_room | 
| Description | Use this action to select the room ID from the available options based on what the user said. | 
| Scope | room\_selection | 

Example input schema:

```
{
  "rooms": [
    {
      "id": 1,
      "roomName": "Garden Suite"
    },
    {
      "id": 2,
      "roomName": "Ocean View"
    },
    {
      "id": 3,
      "roomName": "Executive Suite"
    }
  ]
}
```

Example output schema:

```
{
  "type": "number",
  "description": "The ID of the selected room."
}
```

If the user says "I'd like the Ocean View," the agent can return:

```
2
```

The frontend can then use that value to highlight or select the correct room.

Scope tags help prevent actions from being used in the wrong place.

For example, a `select_room` action should only be available when the user is on the room selection page. A `modify_checkout_date` action may only apply when the user is on a checkout or stay modification screen.

Example scope tag:

```
{
  "scopes": ["room_selection"]
}
```

Use scope tags when different pages or UI states support different actions.

## Paths and exit conditions
<a name="acxd-live-sync-paths"></a>

A Live Sync agent node can route to different paths depending on how the agent session ends.

Common paths include:


|  |  | 
| --- |--- |
| **Exit conditions** | Routes the user when the conversation reaches a defined outcome. | 
| **Timeout** | Runs when the agent does not respond within the configured timeout period. | 
| **Failure** | Runs when the agent or its tools cannot complete as configured. | 
| **Return** | Used when scripted or predefined steps continue back into the flow, if supported. | 
| **Escalation** | Used when the experience should route to a human handoff or escalation path. | 

Exit conditions define meaningful outcomes that allow the agent to leave the node and continue through the flow.

Examples:


|  |  | 
| --- |--- |
| **Goodbye** | The user clearly indicates they are done or wants to end the conversation. | 
| **Escalation requested** | The user asks to speak with a human agent. | 
| **Task complete** | The requested frontend task was completed successfully. | 
| **Unable to help** | The agent cannot complete the requested action. | 

For each exit condition:

1. Add the exit condition to the agent node.

1. Give it a short, clear name.

1. Add a description that tells the agent when to use it.

1. Connect the exit path to the next node in the flow.

A Goodbye exit condition might route to an Exit application node that says:

```
Thanks for contacting us. Have a great day.
```

## Touchpoint and frontend setup
<a name="acxd-live-sync-touchpoint"></a>

Touchpoint is the frontend layer that enables voice input, bidirectional Live Sync behavior, and command handling in your web or mobile application.

In your frontend setup, configure Touchpoint using the connection details from your deployed application. You can find these values in the application's settings under the Access section. Your frontend team will need details such as the application URL and API key to initialize Touchpoint and connect the frontend experience to the deployed agentic CX designer application.

Common handler categories include:


|  |  | 
| --- |--- |
| **Custom command handler** | Handles custom actions, such as selecting a room or opening a modal. | 
| **Navigation handler** | Handles page or route changes. | 
| **Form fill handler** | Handles field updates in visible forms. | 

Your frontend team should map each action returned by the Live Sync agent to the correct UI behavior.

For Live Sync actions to work, the frontend must listen for the commands the agent may send.

The command names and schemas configured in the agent node should match the frontend code.

Example setup pattern:

```
function handleCustomCommand(action, payload) {
  if (action === "select_room") {
    selectRoomById(payload);
  }
  if (action === "open_modal") {
    openModal(payload.modalName);
  }
}

function handleNavigationCommand(command) {
  if (command.destination) {
    navigateTo(command.destination);
  }
}

function handleFormFillCommand(formData) {
  Object.entries(formData).forEach(([fieldId, value]) => {
    updateFieldValue(fieldId, value);
  });
}
```

If the names or schemas do not match, the agent may send the right intent, but the frontend may not know how to execute it.


| Agent configuration | Frontend expectation | 
| --- | --- | 
| Action name: select\_room | Handler listens for select\_room. | 
| Output schema: room ID as a number | Handler expects a number. | 
| Action name: open\_modal | Handler listens for open\_modal. | 
| Output schema: modal name | Handler expects a modal name. | 

## Context API
<a name="acxd-live-sync-context-api"></a>

The Context API lets your frontend send real-time page context to the active Live Sync conversation.

This helps the agent understand:
+ Current page or route
+ Available form fields
+ Current field values
+ Valid navigation destinations
+ Available frontend actions
+ Active scope tags

Send updated context whenever the page or UI state changes.

Examples:
+ The user navigates to a new page
+ A form appears
+ Field values change
+ New actions become available
+ Scope tags change

In this example, the frontend tells the agent that the user is on the room selection page and that three rooms are available:

```
{
  "conversationId": "ACTIVE_CONVERSATION_ID",
  "context": {
    "nlx:vpContext": {
      "uri": "https://example.com/rooms",
      "scopes": ["room_selection"],
      "destinations": [
        "/rooms",
        "/checkout",
        "/spa"
      ],
      "actions": [
        {
          "action": "select_room",
          "description": "Selects one of the available rooms shown on the room selection screen.",
          "input": {
            "rooms": [
              {
                "id": 1,
                "roomName": "Garden Suite"
              },
              {
                "id": 2,
                "roomName": "Ocean View"
              },
              {
                "id": 3,
                "roomName": "Executive Suite"
              }
            ]
          },
          "schema": {
            "type": "number",
            "description": "The ID of the selected room."
          }
        }
      ]
    }
  }
}
```

When this context is active, the user can say "I'd like the Ocean View" and the agent can identify the matching room and send the correct action result to the frontend.

In this example, the frontend tells the agent which checkout form fields are available:

```
{
  "conversationId": "ACTIVE_CONVERSATION_ID",
  "context": {
    "nlx:vpContext": {
      "uri": "https://example.com/checkout",
      "scopes": ["checkout"],
      "fields": [
        {
          "id": "checkoutDate",
          "name": "Checkout Date",
          "type": "date",
          "description": "The guest's requested checkout date",
          "placeholder": "Select checkout date"
        },
        {
          "id": "roomType",
          "name": "Room Type",
          "type": "select",
          "description": "The selected hotel room type",
          "options": [
            {
              "value": "garden_suite",
              "text": "Garden Suite"
            },
            {
              "value": "ocean_view",
              "text": "Ocean View"
            }
          ]
        }
      ]
    }
  }
}
```

When this context is active, the user can say "Set checkout to Saturday and pick the Garden Suite" and the agent can use the field context to understand which values should be filled or selected.