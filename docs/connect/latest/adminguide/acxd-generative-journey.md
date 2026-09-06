# Using the Generative Journey agent node

Generative Journey is an agent node that uses a large language model to complete
a task through natural conversation, data capture, and tool use.

Use a Generative Journey node when a conversation needs more flexibility than a
strictly deterministic path, but still needs clear instructions, controlled tools, and
defined outcomes.

For example, a hotel application might use Generative Journey to collect travel
dates, ask follow-up questions, check availability, present room options, and exit
the node once the user has selected a room or needs help from an agent.

Use a Generative Journey node when the application needs to handle a multi-step
task that may not happen in the exact same order every time.

Common use cases include:

- Scheduling or rescheduling an appointment
- Troubleshooting a customer issue
- Collecting several required details
- Searching a knowledge base during a broader task
- Calling Data requests as needed
- Presenting modalities such as cards or carousels
- Routing to another flow when a deterministic process is required
- Completing a task with several possible outcomes
  Generative Journey is useful when the user may provide information out of order,
  ask clarifying questions, or need the AI to decide which tool to call next.

A Generative Journey node automatically:

1. Reads the user's latest utterance and the system transcript.
2. Follows the prompt instructions you provide.
3. Collects required or optional slot values defined.
4. Uses assigned tools, such as Data requests, flows, modalities, or knowledge bases.
5. Decides when the task has reached one of the defined exit conditions.
6. Continues the flow through the path linked to that outcome.
   The node stays in control of the task until it exits through one of its configured exit
   paths, calls a handover flow tool, fails, or times out.

## Pathways

Generative Journey uses pathways to determine where the conversation should go
after the agent completes, fails, or times out.

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Exit conditions**       | Outcomes you define that tell the agent when to leave the node and continue the flow.              |
| **Data capture complete** | An automatic path triggered when required slots are collected and *_Auto-advance_<br>• is enabled. |
| **Failure**               | Runs when the agent or one of its required tools fails.                                            |
| **Timeout**               | Runs when the agent does not respond within the configured timeout period.                         |

Always connect each path to the next appropriate node so the flow can continue
predictably.

## Prompt

The prompt tells the agent what task it is responsible for completing.

A strong prompt should include:

- The agent's role
- The task it should complete
- Any runtime variables or critical information it should review every turn (e.g., context attributes, etc.)
- What information it must collect
- What tools it can use
- Rules or limitations it must follow
- Brand voice or tone guidance
- What counts as completion
- When to exit through each exit condition

## Exit conditions

Exit conditions define the acceptable outcomes that can end the Generative
Journey node.

Each exit condition should have:

- A short name
- A clear description
- A connected path to the next node in the flow

Examples:

|                          |                                                                     |
| ------------------------ | ------------------------------------------------------------------- |
| **Room selected**        | The guest selected a room and is ready to continue to confirmation. |
| **No availability**      | No matching rooms were available for the requested dates.           |
| **Escalation requested** | The guest asked to speak with a person.                             |
| **User cancelled**       | The user decided not to continue.                                   |
| **Task complete**        | The requested task was completed successfully.                      |

###### To add an exit condition

1. Select the Generative Journey node.
2. Choose **Add exit condition**.
3. Enter a clear name.
4. Add a brief description of when the agent should use it.
5. Connect the new path to the next node in the flow.

Use specific exit condition names so the flow is easy to understand on the Canvas.

## Data capture

Data capture lets the agent collect slot values from the user during the task.

You can configure:

|                    |                                                                                 |
| ------------------ | ------------------------------------------------------------------------------- |
| **Required slots** | Values the agent must collect before the task can complete.                     |
| **Optional slots** | Values the agent should collect or use if the user provides them.               |
| **Auto-advance**   | Creates an automatic path that triggers after all required slots are collected. |

Only slots attached to the current flow are available for selection.

Example required slots for a hotel booking task:

- Check-in date
- Checkout date
- Number of guests
- Number of rooms

Example optional slots:

- Preferred room type
- Accessibility needs
- Pet preference
- Loyalty number

Use **Auto-advance** when the main purpose of the node is to collect a set of
values, then continue to the next deterministic step.

In the main prompt, refer to slot names in plain language, as the placeholder syntax
is empty until a value is given by the user.

Good examples:

```
Collect the checkInDate, checkoutDate, and preferred roomType. Only
collect one at a time.

If the user provides a different customerEmail, confirm it once before
using.
```

Use placeholders when you need to pass a resolved value into a tool input or field
that supports variables.

## Tools

Tools give the agent controlled capabilities it can use while completing the task.

Generative Journey can use tools such as:

|                     |                                                                 |
| ------------------- | --------------------------------------------------------------- |
| **Data requests**   | Call external systems to retrieve, send, or update data.        |
| **Knowledge bases** | Search approved Q&A or document content for grounded answers.   |
| **Modalities**      | Present structured UI, such as a card, carousel, or date input. |
| **Flows**           | Invoke another flow as a handover or structured tool via MCP.   |

Add only the tools the agent needs for the task. Too many tools can make the agent
harder to control and test.

Each tool should include a short prompt that explains when and how the agent
should use it.

A good tool prompt should explain:

- When to call the tool
- What information is required first
- What the tool returns or does
- Any rules for using the result
- What to do if the tool fails or returns no data

Example Data request tool prompt:

```
Use this tool only after the user has provided an appointment date and
location. It returns available appointment times. If no times are
returned, tell the user there are no available times for that date and
ask whether they want to try another date.
```

Example knowledge base tool prompt:

```
Use this knowledge base to answer questions about cancellation policy,
refund eligibility, and reservation changes. If the answer is not
found, do not guess. Exit through Escalation requested if the user
needs policy confirmation from an agent.
```

Example modality tool prompt:

```
Use this carousel to show available appointment times after the
availability Data request returns results. Each card should represent
one available time.
```

Some tools require input values.

For each input field, you can choose how the value should be provided. Simply
switch the input option by selecting the icon to the right of the field:

|                          |                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **LLM prompt**           | Let the agent infer or collect the value from the conversation.                                                          |
| **Explicit value**       | Provide a fixed value that should always be sent.                                                                        |
| **Placeholder variable** | Pass an existing value from the conversation, such as a slot, context variable, system variable, or Data request result. |

Use _Placeholder variable_ when a value already exists and should be passed directly into a tool.

Examples:

- {CustomerProfile.id}
- {CustomerEmail}
- {AppointmentDate}
- {SelectedLocation.id}
- {System.conversationId}
- {System.utterance}

Use the placeholder menu by typing { in supported fields, then select the value
you want to pass.

Use variables in the prompt when the agent needs known context.

Example with context variables:

```
#Important Customer Information
- Loyalty status: {customerTier}
- Authentication status: {authenticated}
```

Example with a prior Data request result:

```
The customer has the following active reservations: {Reservations}.
Help them choose which reservation they want to modify.
```

Use variables when they provide useful context, but keep the prompt readable. The
agent should still have clear instructions in plain language.

## Using a Data request tool

Use a Data request tool when the agent needs to call an external system.

###### When adding a Data request tool

1. Add the Data request to the Generative Journey node.
2. Expand the tool.
3. Add a tool prompt.
4. Configure any required input schema fields.
5. Choose whether each field should come from the LLM prompt, an explicit value,
   or a placeholder variable.
6. Add an optional interim message.
7. Save and test.

Example interim message:

```
One moment while I check your reservation.
```

Use interim messages for tool calls that may take more than a moment, especially
in voice experiences.

## Using a knowledge base tool

Use a knowledge base tool when the agent needs to answer questions from
approved content during the task.

###### When adding a knowledge base tool

1. Add the knowledge base to the Generative Journey node.
2. Expand the tool.
3. Add a tool prompt that explains the tool is a knowledge base and what the
   knowledge base should be used for.
4. Tell the agent what to do if no answer is found.
5. Save and test.

Example:

```
Use this knowledge base for questions about refund policy and
cancellation rules. If no answer is found, say that you do not have
enough information and exit through Escalation requested.
```

## Using a modality tool

Use a modality tool when the agent should present structured UI during the task.

###### When adding a modality tool

1. Add the modality to the Generative Journey node.
2. Expand the tool.
3. Add a tool prompt.
4. Map required payload fields.
5. Save and test.

Example:

```
Use this card after the user selects an appointment time. Populate it
with the selected date, time, location, and appointment type.
```

## Using flow tools

Generative Journey can use flows in two ways: _handover_ or _MCP-enabled_.

### Handover flows

Use a handover flow when you want the flow to take control of the conversation.

When the agent invokes a handover flow, the agent node is exited and the
conversation follows that flow's nodes and messaging exactly as designed.

Use handover when:

- A deterministic process must run
- The user must complete a controlled workflow
- A flow already exists for the task
- The experience requires precise messaging or routing

To return from a handover flow to the Generative Journey node, add a Redirect
node at the end of the handover flow and route it back to the agent flow and node
using the Generative Journey's node ID (retrieved in the three-dot menu of a node).

### MCP-enabled flows

Use an MCP-enabled flow when you want the agent to call a flow as a structured
tool while the agent remains in control of the broader conversation.

Unlike a handover flow, an MCP-enabled flow does not fully take over the
conversation. Instead, the Generative Journey node can invoke the flow as a tool,
pass in any required inputs, use the flow's result, and continue managing the task.

Use MCP-enabled flows when:

- The agent should stay in control of the conversation
- You want deterministic flow logic available as an agent tool
- The flow needs structured inputs, such as location, date, account type

For example, a restaurant recommendation agent might call an MCP-enabled flow
that takes cuisine and location as inputs, searches available recommendations,
and returns matching results to the agent.

###### To make a flow available as an MCP tool

1. Open the flow you want the agent to use.
2. Select **Settings** from the flow toolbar.
3. Open the **MCP** tab.
4. Enable the **MCP** toggle.
5. Add optional input schema, if the flow requires information from the agent.
6. Save the flow.

Input schema defines the values the agent should collect or pass into the flow.

Use input schema when the flow needs specific information to run correctly.

Examples:

| Use case                   | Input fields                                 |
| -------------------------- | -------------------------------------------- |
| Restaurant recommendations | cuisine, location, partySize                 |
| Appointment lookup         | appointmentDate, locationId, appointmentType |
| Eligibility check          | customerId, planType, state                  |
| Order lookup               | orderId, email                               |

For each input field:

1. Use a short, unique input name with no spaces or special characters.
2. Choose the appropriate property type.
3. Add a clear description so the agent understands what the value means.
4. Save the schema.

Example input schema fields:

|               |                                                                       |
| ------------- | --------------------------------------------------------------------- |
| **cuisine**   | The type of food the user wants, such as Italian, Thai, or Mexican.   |
| **location**  | The city, neighborhood, or area where the user wants recommendations. |
| **partySize** | The number of people included in the reservation or visit.            |

Clear descriptions help the agent collect the right information before calling the flow.

After you define the MCP input schema, the input values can be referenced inside
the flow.

On any supported node field, type { and select the MCP input variable you want
to use.

You can use MCP input variables in places such as:

- Messages
- Data request payload fields
- Split node conditions
- Define nodes
- Modality payload fields

Example message:

```
I'll look for {location} restaurants that match your interest in {cuisine}.
```

## LLM model selection

The LLM model determines what model powers the agent's reasoning and tool use.

Choose the model based on the task, channel, latency needs, and complexity of the
experience.

For simpler or voice-sensitive tasks, prioritize lower-latency models. For more
complex tool use or reasoning-heavy chat experiences, a more capable model may
be appropriate.

## Settings

Generative Journey includes settings that control how the agent behaves.

|                    |                                                                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Max iterations** | Limits how many times the agent can think, call a tool, reassess, and continue within<br>one turn. Use this to prevent long loops and control latency or cost. |
| **Auto-advance**   | Allows the agent to resolve required values from the latest user utterance and exit<br>automatically when possible.                                            |
| **Timeout**        | Sets how long the agent has to respond before the timeout path is triggered.                                                                                   |

Use conservative settings when latency, cost, or predictable behavior is important.
