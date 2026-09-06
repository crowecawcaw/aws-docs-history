# Working with nodes

Nodes are the building blocks of a flow in agentic CX designer.

Each node represents a specific action in the conversation, such as sending a
message, collecting a user response, calling a Data request, generating AI output,
routing to another flow, transforming data, escalating to a human agent, or ending
the application session.

A flow is created by placing nodes on the Canvas and connecting them in the order
the conversation should follow.

###### To add a node to the Canvas

1. Open a flow.
2. Select the **Add node** option from the Canvas toolbar, or right-click the Canvas and
   choose **Add node**.
3. Choose the node type you want to add.
4. Place the node on the Canvas.
5. Connect it to the appropriate previous or next node.
6. Save the flow.
   Every flow includes a Start node. Connect the Start node to the first node in your
   flow so the conversation knows where to begin.

## Connecting nodes

Nodes are connected through paths. A node may have one path or multiple paths
depending on what can happen after the node runs.

###### To connect nodes

1. Select a node path.
2. Drag the connector line to the next node.
3. Release to connect the path.

Connected lines show the direction of the conversation. You can also stack nodes
together by dragging one node above or below another. When stacked, the path
turns into an arrow that shows the conversation direction.

To disconnect nodes, select the connecting line or move a stacked node away from
the group.

## Node side panel

Selecting a node opens its side panel.

The side panel lets you configure that node's messages, settings, paths, tools,
variables, and added functionality. The available options depend on the node type.

Every node has a non-editable node ID that can be referenced across the
workspace. To view the node ID, open the three-dot menu in the upper-right corner
of the node side panel.

## Node messages

Many nodes can send messages to the user.

###### To add a message

1. Select a node.
2. Choose **Add message** from the side panel.
3. Enter the message text.
4. Save the flow.

You can add multiple messages to a single node. This breaks longer responses into
smaller messages, which can make the experience easier to read in chat or hear in
voice.

To insert a variable or dynamic value into a message, type { in the message field
and choose from the available placeholders.

Examples:

- {System.utterance}
- {CustomerProfile.firstName}
- {Reservation.confirmationNumber}
- {SelectedDate}

If a slot does not appear in the placeholder menu, confirm that the slot is attached
to the flow. If a Data request value does not appear, confirm that the response
model is configured and that list values are processed appropriately.

## Node functionality

Select **Add functionality** from the node side panel to add supported
enhancements.

Available functionality includes:

|                         |                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Analytics tags**      | Marks a node with system or custom tags to track user paths.                                                                                                                                  |
| **Live Sync action**    | Triggers a Live Sync action for bidirectional web conversations.                                                                                                                              |
| **Modality**            | Adds a rich interaction, such as a carousel or date input. Available for Basic, User choice,<br>User input, Generative Journey, and Live Sync nodes. Works with the Touchpoint SDK to render. |
| **Node payload**        | Triggers custom behaviors or passes custom data in the response using key-value pairs.                                                                                                        |
| **State modifications** | Applies a state change to variables during the conversation.                                                                                                                                  |
| **Voice settings**      | Overrides the selected voice settings for that node. Read below for details.                                                                                                                  |

Note that not every functionality option is available for every node type.

Use node-level Voice settings selectively. For example, you might enable
interruption at the start of the conversation then disable interruption for an
important compliance message downstream, or enable DTMF input when collecting
a numeric value by keypad.

Voice settings include two groups: Speech and DTMF.

| Speech setting            | What it controls                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| **Interruption**          | Lets the caller talk over the message.                                                            |
| **Speech input**          | Lets the caller answer by speaking.                                                               |
| **No input timeout**      | Controls how long the application waits for the user to start talking after the message.          |
| **End of speech timeout** | Controls how long a pause must last before the application decides the user has finished talking. |
| **Max speech timeout**    | Controls the maximum amount of time the user can keep speaking.                                   |

| DTMF setting         | What it controls                                                                       |
| -------------------- | -------------------------------------------------------------------------------------- |
| **DTMF input**       | Lets the user answer using the keypad.                                                 |
| **Clear key**        | Defines the key the user presses to clear all digits they entered.                     |
| **Submit key**       | Defines the key the user presses to submit immediately instead of waiting for timeout. |
| **Keypress timeout** | Controls how long to wait after the user's last key press.                             |
| **Max digits**       | Controls the maximum number of keys the user can press.                                |

Each node defaults to the name of its node type. Rename nodes to make large
flows easier to understand.

###### To rename a node

1. Select the node.
2. Click the node name in the side panel.
3. Enter a clear name.
4. Save the flow.

Color labels can help visually organize the Canvas.

###### To recolor a node

1. Right-click the node.
2. Select **Color**.
3. Choose a color.
4. Save the flow.

Use color consistently across your workspace, such as one color for API calls, one
for user inputs, one for error handling, and one for escalation.

## Start node

The _Start_ node is the beginning point of every flow or flow page.

It is created automatically and cannot be edited. Connect the Start node to the first
node that should run when the flow begins.

Connects to the first node in the flow.

## Basic node

A _Basic_ node sends a message or acts as a state processing step between other
nodes.

Use Basic nodes to:

- Greet the user
- Confirm an action
- Explain what happens next
- Add a progress message
- Clear or update variables with state modifications
- Create a simple recovery message before retrying a step

A Basic node is often used before or after nodes that do not send their own
message.

Connects to the next node in the flow.

## Exit application node

The _Exit application_ node ends the conversation session.

Use this node when the application has completed its task and should stop the
active chat or voice session. It provides a clear explicit ending point for the flow.

Use Exit application when:

- The user's task is complete
- The user chooses to end the conversation
- A voice or chat session should close after a final message

## User input node

A _User input_ node listens for an open-ended user response.

Use User input when the user should describe what they need in their own words.
The application can then attempt to recognize the user's intent and route
accordingly.

Use User input nodes to:

- Ask what the user needs help with
- Capture an open-ended response
- Collect freeform text that will be evaluated downstream
- Support broad navigation from a menu-like question

Common pattern:

1. Ask the user what they need help with.
2. Use User input to capture the user's response.
3. If a flow is recognized, connect to a Redirect node.
4. If no flow is recognized, connect to a clarification or Unknown path.

Flow recognition depends on the flows attached to the application and the routing
descriptions configured for those flows. You can connect both pathways to the
same node if simply using the system variable {System.utterance} downstream for
evaluation.

|              |                                                                  |
| ------------ | ---------------------------------------------------------------- |
| **Match**    | The user's utterance matched a flow attached to the application. |
| **No match** | The user's utterance did not match a supported flow.             |

## User choice node

A _User choice_ node asks the user to provide or select a specific value.

Use User choice when the application needs a structured answer, such as a date,
yes/no response, category, option, or value returned from a Data request.

Use User choice nodes to:

- Ask a yes/no question
- Ask the user to choose from custom slot values
- Capture a built-in slot such as date, time, email, or number
- Present options returned from a Data request
- Route based on the selected value

A User choice node can resolve values from:

- Custom slots attached to the flow
- Built-in slots attached to the flow
- Data request list responses

If the node uses values from a Data request, call the Data request before the User
choice node.

|                      |                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Match**            | The user's response matched the assigned source.                                                                          |
| **No match**         | The user's response did not match the assigned source and did not match the routing description of another eligible flow. |
| **Slot value paths** | Optional paths that correspond to individual custom slot values.                                                          |

A User choice node also participates in application-level flow routing.

When a user responds, agentic CX designer evaluates the response in the following order:

1. **Slot or source match.** The application first checks whether the
   response matches an available slot value or other configured source (via a data
   request) for the node.
2. **Flow routing.** If there is no match, the application checks flows
   that have routing enabled and an AI description configured. If the user's
   response matches one of those flow descriptions, the conversation
   automatically redirects to that flow.
3. **No match.** If the response matches neither the User choice source nor
   an eligible flow, the node follows its No match path.

## Data request node

A _Data request_ node calls a configured Data request during the conversation.

Use this node when the flow needs to send or retrieve data from an external system
at a specific point in the conversation.

Use Data request nodes to:

- Retrieve customer profile details
- Check appointment availability
- Look up an order or ticket status
- Submit a form or request
- Send a confirmation message
- Update an external record

Place Data request nodes before any downstream nodes that need to use the
returned data.

After the request succeeds, reference returned values by typing { in supported
fields and choosing the Data request output.

|                 |                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Success**     | The request completed successfully.                                                                                  |
| **Failure**     | The request failed or could not connect as configured.                                                               |
| **Timeout**     | The request did not respond before the timeout.                                                                      |
| **In progress** | Optional path used while the request is still resolving to deliver a message. Link path<br>back to the data request. |

## Knowledge base node

A _Knowledge base_ node retrieves an answer from a knowledge base.

Use this node when the flow should answer a user's question using trusted content
from a Q&A or Documents knowledge base.

Use Knowledge base nodes to:

- Answer FAQs
- Provide policy information
- Share instructions or how-to guidance
- Support Unknown behavior
- Ground answers in approved content

Common pattern:

1. Send the user's question to the Knowledge base node.
2. Store the result in an output variable.
3. Connect the Match path to a Basic or User choice node.
4. Reference the answer in the message.
5. Connect No match to clarification, fallback, or escalation.

|              |                                            |
| ------------ | ------------------------------------------ |
| **Match**    | Relevant knowledge base content was found. |
| **No match** | No confident answer was found.             |
| **Failure**  | The knowledge base request failed.         |
| **Timeout**  | The knowledge base request timed out.      |

## Generative text node

A _Generative text_ node uses a large language model to generate a text output
during the flow.

Use Generative text when the application needs to create, rewrite, summarize,
classify, or format information dynamically.

Use Generative text nodes to:

- Generate a personalized response
- Summarize prior information
- Rewrite text in a specific tone
- Format content for downstream use

The generated output is stored as an output variable and can be referenced
downstream using {.

|             |                                               |
| ----------- | --------------------------------------------- |
| **Success** | The text was generated successfully.          |
| **Failure** | The generation failed.                        |
| **Timeout** | The model did not respond before the timeout. |

## Define node

A _Define_ node creates a local value that can be used later in the same flow.

Use Define nodes when you need to set, format, transform, or name a value without
storing it globally as a context variable.

Use Define nodes to:

- Create a temporary value
- Rename a value for easier reference
- Extract part of a date
- Count or format a value
- Prepare a value for a message, condition, or payload

Defined values are local to the flow and do not persist beyond it.

Connects to the next node in the flow.

## Transform node

A _Transform_ node reshapes, filters, maps, or sorts data so it can be used later in
the flow.

Use Transform nodes when data returned from a Data request, knowledge base, or
variable does not match the structure you need.

Use Transform nodes to:

- Filter a list
- Sort items
- Reshape API data
- Map returned values into a modality schema
- Remove unavailable or irrelevant results
- Prepare data for User choice or downstream logic

Transform options include deterministic and generative methods, such as filter,
map, generative filter, generative map, morph, and sort.

Connects to the next node in the flow.

## Loop node

A _Loop_ node repeats part of a flow or iterates over items in a list.

Use Loop nodes to:

- Limit retry attempts
- Prevent infinite loops
- Iterate over returned List results from a Data request

Loop modes include:

|              |                                       |
| ------------ | ------------------------------------- |
| **Retry**    | Repeats a path a set number of times. |
| **For each** | Iterates over values in a list.       |

|              |                                                                |
| ------------ | -------------------------------------------------------------- |
| **Loop**     | Continues through the looped path.                             |
| **Complete** | Runs when the loop has finished or the retry limit is reached. |

Be sure to use state modifications with retry loops when a previous value needs to
be cleared before the user tries again.

## Split node

A _Split_ node routes the conversation based on conditions or chance.

Use Split nodes when the flow should branch based on logic, variables, user
responses, or traffic distribution.

Split modes include:

|                 |                                                                                |
| --------------- | ------------------------------------------------------------------------------ |
| **Conditional** | Routes based on defined IF statements or generative conditions.                |
| **A/B**         | Randomly distributes users across paths by percentage. Useful for A/B testing. |

|           |                                           |
| --------- | ----------------------------------------- |
| **Match** | Runs when a defined condition is met.     |
| **Else**  | Runs when none of the conditions are met. |

Use Split nodes to:

- Route by customer type
- Check whether a variable exists
- Branch by channel type
- Evaluate a user's response
- Send users through A/B test paths
- Handle additional slot values after a User choice No match path

## Redirect node

A _Redirect_ node sends the user to another flow, another page in the current flow, a
recognized flow, or another supported destination.

Use Redirect nodes to:

- Move from one flow to another
- Continue a task in a separate flow
- Route based on recognized intent
- Return to a previous redirect point
- Send control back to a parent application, when supported

If redirecting to another flow, make sure that flow is attached to the application
before building and deployment.

|            |                                                                           |
| ---------- | ------------------------------------------------------------------------- |
| **Return** | Optional path used when the redirected flow returns to the current point. |

## Escalate node

An _Escalate_ node ejects the conversation out of the Escalation path on the
Agentic CX block in your contact flow within Amazon Connect Customer.

Use Escalate nodes when:

- The user asks for a human agent
- A business rule requires human handling
- A task cannot be completed by the application
- An API failure requires a human recovery path

You can link to the same Escalate node from multiple places in your agentic CX designer flow.

|            |                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| **Return** | Runs if the conversation returns to the Agentic CX block after escalation in the Connect Customer flow. |

## Node type summary

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Basic**              | Send a simple message                                 |
| **Exit application**   | End the conversation session                          |
| **User choice**        | Ask the user to choose from options deterministically |
| **User input**         | Capture intent or a user response deterministically   |
| **Data request**       | Call an external system                               |
| **Knowledge base**     | Retrieve an answer from approved content              |
| **Generative text**    | Generate text output                                  |
| **Generative Journey** | Complete a multi-step task with tools                 |
| **Define**             | Set a temporary value                                 |
| **Transform**          | Reshape or filter data                                |
| **Loop**               | Retry or iterate through items                        |
| **Split**              | Branch based on logic or chance                       |
| **Redirect**           | Move to another flow                                  |
| **Escalate**           | Transfer to human support                             |

## Agent nodes

Agent nodes use agentic AI to manage flexible goal-based experiences.

|                        |                                                                                                                                                                                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Generative Journey** | Guide a multi-step conversation, collect information, and call tools<br>such as Data requests, knowledge bases, modalities, or other flows.<br>Learn how to configure a [Generative Journey](acxd-generative-journey.md "acxd-generative-journey.md") node. |
| **Live Sync**          | Guide a hands-free web or mobile experience where the agent can converse<br>with the user and coordinate supported frontend actions.<br>Learn how to build a [Live Sync](acxd-live-sync.md "acxd-live-sync.md") experience.                                 |
