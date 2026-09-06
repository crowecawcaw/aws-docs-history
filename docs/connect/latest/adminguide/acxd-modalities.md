# Modalities

Modalities are reusable structured UI components that bring richer interaction into
agentic CX designer conversations.

A modality complements a text response by sending structured data that your
frontend can render as an interactive experience. For example, a modality can
display a carousel of options, show a confirmation card, open a date picker, render
an image, or support a custom UI pattern built for your application.

Modalities are rendered by the application frontend via the Touchpoint SDK.

To access modalities, select **Resources** from your workspace menu, then choose
**Modalities**.

A modality is a structured payload that helps the user take action or view richer
content during a conversation.

Instead of sending only a message, the application can send data that the frontend
knows how to display.

For example:

- A hotel assistant can show resort options in a carousel.
- A banking assistant can show a card summary for a selected transaction.
- A scheduling assistant can show a date picker.
- A shopping assistant can show product cards with images and labels.
- A support assistant can show a custom troubleshooting interface.
  Modalities are useful when the user needs to select, confirm, compare, review, or
  interact with information visually.

Use modalities when text alone is not the best way to guide the user.

Modalities can be added to supported node types, including:

- Basic nodes
- User choice nodes
- User input nodes
- Agent nodes, such as Generative Journey and Live Sync nodes
  For Basic, User choice, and User input nodes, modalities are added from the node's
  functionality options.

For agent nodes, modalities can be attached as tools so the agent can choose
when to use them during a task.

## Predefined modalities

Agentic CX designer includes predefined modalities that can be reused across flows.

Predefined modalities are designed to work with the agentic CX designer
Touchpoint SDK, without requiring you to create a custom frontend component.
They behave like reusable UI blocks and can be attached to supported nodes.

The predefined modalities include:

|                |                                                                 |
| -------------- | --------------------------------------------------------------- |
| **Carousel**   | Shows multiple options in a horizontally browsable card layout. |
| **Card**       | Shows a single focused item, summary, confirmation, or preview. |
| **Date input** | Lets users select a date through a date picker.                 |

### Carousel

Use a Carousel modality when users need to browse or select from multiple options.

Best for:

- Product selections
- Resort or hotel options
- Appointment times
- Credit card or plan options
- Search results
- Return or exchange options

Example carousel schema:

```
[
  {
    "id": "uuid",
    "thumbnail": "imageUrl",
    "label": "Label text",
    "value": "Value text"
  }
]
```

A carousel can be powered by static values, values entered directly in the node, or
dynamic data returned from a Data request.

### Card

Use a Card modality when users need to review one focused item.

Best for:

- Confirmation summaries
- Selected item previews
- Reservation details
- Payment or billing summaries
- Account or profile previews
- Important next-step information

Example card schema:

```
{
  "id": "uuid",
  "thumbnail": "imageUrl",
  "label": "Label text",
  "value": "Value text"
}
```

A card is useful when you want to visually reinforce the information the user is
about to confirm or act on.

### Date input

Use a Date input modality when users need to select a date.

Best for:

- Scheduling appointments
- Choosing a reservation date
- Selecting a service date
- Confirming an existing date
- Capturing a date for a downstream Data request

The Date input modality does not require a custom schema. It opens a date selector
and returns the selected date to the conversation.

## Custom modalities

Create a custom modality when your use case requires a visual or interaction
pattern beyond the predefined options.

A custom modality is a reusable resource with its own schema and frontend
rendering behavior.

When the conversation reaches a supported node with a custom modality attached,
agentic CX designer sends the structured payload to the frontend for rendering.

|                        |                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Schema**             | Defines the structure of data the modality accepts, such as text, image URLs, links, IDs, or metadata. |
| **Frontend rendering** | Defines how the frontend displays that data through Touchpoint SDK or your own custom UI.              |

###### To create a custom modality

1. Open **Resources**.
2. Select **Modalities**.
3. Select **Create modality**.
4. Enter a clear name.
5. Open the **Schema** tab.
6. Add the schema manually or use auto-generate from sample JSON, if available.
7. Add descriptions for schema properties (if intended to be used by an agent node).
8. Save the modality.

Add property descriptions when the modality may be used by an agent node.
Descriptions help the agent understand what each field means and how the
modality should be populated.

Custom modality properties may include a **Sensitive** setting.

Enable **Sensitive** for fields that may contain:

- Personally identifiable information
- Account details
- Protected customer data
- Payment-related information
- Any value your organization treats as private

Sensitive fields help prevent those values from appearing in conversation logs
where supported.

The **Generated code** tab lets you retrieve schema output for use in your frontend codebase.

Depending on what is available in your workspace, this may include formats such as:

- JSON schema
- TypeScript schema

Use generated code to help validate modality payloads and support type-safe
rendering in your frontend.

## Using a predefined modality

###### To use a predefined modality

1. Open a flow in the Canvas.
2. Add or select a supported node, such as User choice, User input, or an agent node.
3. Select Add functionality on the node.
4. Select **Modality**.
5. Choose the predefined modality.
6. Map or enter any required values.
7. Save the flow.
8. Create a new build before testing or deployment, if the change should be
   included in the application experience.

For agent nodes, attach the modality as a tool and provide instructions for when the
agent should use it.

## Using a custom modality

###### To use a custom modality

1. Open a flow in the Canvas.
2. Add or select a supported node, such as User choice or User input.
3. Open the node's functionality options.
4. Select **Modality**.
5. Choose the custom modality.
6. Enter payload values manually or use dynamic placeholders.
7. Save the flow.

You can populate modality fields with values from:

- Slots
- Context variables
- System variables
- Data request outputs
- Other values already available in the conversation

Type { in supported fields to select available placeholders.

For agent nodes, attach the custom modality as a tool and provide clear
instructions for when the agent should use it. You can provide explicit variables to
the fields or provide agent instructions on what fields it should populate.

## Modalities with dynamic data

Modalities are often powered by dynamic data returned from a Data request.

For example:

1. A user asks to book an appointment.
2. A Data request retrieves available appointment times.
3. A Transform, Loop, or Define step reshapes the returned data.
4. A carousel modality displays the available times.
5. The user selects one.
6. The selected value is used in the next step of the flow.

This pattern helps turn real-time API responses into interactive UI elements.

A Data request response may not match the schema a modality expects.

When that happens, use transformation tools to reshape the data before sending it
to the modality.

|                       |                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Generative map**    | Uses generative AI to reshape data into the target schema. Helpful for prototyping or variable response structures. |
| **Deterministic map** | Maps each item in a list into the expected list-item schema. Useful for carousels and repeated cards.               |
| **Morph**             | Deterministically builds structured payloads from complex or nested data. Useful when you need precise control.     |

Use generative transformation when speed and flexibility are important. Use
deterministic transformation when structure, predictability, or compliance matters more.
