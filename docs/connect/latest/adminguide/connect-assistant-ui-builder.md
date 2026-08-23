# Use the Connect assistant in the UI builder

The Connect assistant is integrated within the UI builder, enabling you to
create and modify view resources using natural language. Instead of manually
dragging components, configuring properties, and navigating complex panel settings,
you can describe what you need in conversational prompts, and the Connect assistant
generates the corresponding UI components on the canvas.

For example, you can type "Create a customer feedback form with fields for
rating, comments, and contact preference" and the Connect assistant builds the view for you
to inspect and refine before publishing.

The Connect assistant supports the following capabilities:

- **Create views from descriptions** —
  Describe a complete view in natural language, and the Connect assistant generates
  all necessary components.
- **Modify existing views** — Request
  changes to views through conversation, such as "add a dropdown for order
  status" or "make the comments field required."
- **Configure component properties** — Set
  properties, validations, dynamic fields, and styling without navigating
  the Customize panel.
- **Apply conditional logic** — Describe
  conditions in natural language, such as "only show the Other text field
  if Other is selected in the dropdown."
- **Get recommendations** — Ask the
  Connect assistant for suggestions on available components, best practices, and
  how to improve your views.

## Prerequisites

Before using the Connect assistant in the UI builder, verify the
following:

- You are using Connect Customer and you have access to the Connect Customer admin
  workspace.
- Your security profile includes the **Channels
  and flows - Views** permission.
- Your security profile includes the **AI agent
  designer – AI agents** permission.
- Your Connect Customer instance has the Connect assistant feature enabled at the
  instance level.

## Access the Connect assistant

1. Log in to the Connect Customer admin workspace at
   https://`instance name`.my.connect.aws/.
   Use an Admin account, or an account that has **Channels and flows - Views** & **AI agent designer - AI agents** permission
   in its security profile.
2. In the navigation pane, choose **Views** inside
   the **UI Management** navigation menu.
3. Create a new view or open an existing view in the UI
   builder.
4. If opening an existing view, locate the **Connect
   Assistant** button in the toolbar. Choose it to expand
   the chat panel. The chat panel opens on the side of the UI builder
   canvas. You can collapse or expand the panel at any time.
5. Type your request in the chat input field and press Enter to send
   your message to the Connect assistant.

## Create a view using the Connect assistant

The following procedure describes how to create a new view from a natural
language description.

1. Open the UI builder with an empty canvas (or an existing view you
   want to add components to).
2. In the chat panel, describe the view you want to create. For
   example: "Create an order return form with customer name, order
   number, return reason dropdown, and a notes section."
3. The Connect assistant processes your request and prepares the view
   components. When the view is ready, the Connect assistant responds with a
   description of the components it created and applies the generated
   components to the UI builder canvas.
4. Review the components on the canvas. You can continue the
   conversation to refine the view or manually adjust components using
   the standard UI builder tools.

### Specify layout preferences

You can include layout requirements in your request. For
example:

- "Create a two-column form with customer information on the
  left and order details on the right."
- "Add an attribute bar at the top with customer name and
  account number, then a form below it."

### Request specific component types

Ask for specific UI components by name or function. For
example:

- "Add a date picker for the appointment date."
- "Include a toggle for newsletter subscription."
- "Add a submit button at the bottom of the form."

The Connect assistant uses components from the Connect Customer UI component library. If
a requested component is not available, the Connect assistant explains the
limitation and suggests alternatives.

## Modify an existing view

You can request changes to views already on the canvas through natural
language.

1. With a view open in the UI builder and the chat panel expanded,
   describe the change you want. For example: "Make the comments field
   required" or "Change the submit button color to green with white
   text."
2. The Connect assistant processes the request and presents the updated
   components directly on the canvas.
3. If the Connect assistant needs clarification about which component you
   are referring to or what property to change, it asks a follow-up
   question before making the modification.

### Undo changes and revert

To undo recent changes made by the Connect assistant, type a request such
as:

- "Undo the last change."
- "Remove the dropdown you just added."

To revert to a prior view generated by the Connect assistant, find the
confirmation message in the session and choose the revert button. All
of the changes will be overwritten back to that point in time.

## Configure dynamic fields

You can use the Connect assistant to set up fields that populate at runtime
with data from contact attributes or other sources.

1. In the chat panel, describe dynamic behavior. For example: "Add
   a read-only field that shows the customer's name from contact
   attributes."
2. The Connect assistant configures the component by setting the component's
   property to dynamic, adding a sample reference (for example,
   $.CustomerName\_Sample), and creating sample data for the relevant
   input.
3. Review the configuration in the **Customize**
   panel to verify the dynamic field references are correct for your
   flow.
4. To pass data into the view and use output data, configure the
   ShowView block in your flow separately.

## Create conditional UIs using the Connect assistant

Instead of manually configuring conditions in the UI conditions tab, you
can describe conditional logic in natural language.

1. In the chat panel, describe the condition. For example: "Only
   show the Other text field if Other is selected in the reason
   dropdown."
2. The Connect assistant creates the appropriate UI condition on the target
   component, including the trigger component, evaluation criteria, and
   the resulting visibility or property change.
3. Components with conditions applied are outlined in dashed lines
   on the canvas, consistent with manually created conditions.

For more information about UI conditions, see [Build conditional UIs with Views](ui-conditions-on-views.md "ui-conditions-on-views.md").

## Get recommendations and explanations

The Connect assistant can provide guidance while you build views:

- Ask about available components: "What types of input fields are
  available?"
- Request recommendations: "What additional fields would you
  recommend for a customer complaint form?"
- Get configuration help: "How do I make this field populate
  dynamically?"
- Validate your view: "Check if this form has all required fields
  configured correctly."

The Connect assistant responds with explanations, component options, and best
practices based on the Connect Customer UI component library.

## Conversation management

The Connect assistant preserves your conversation history within a session so
you can reference previous requests and changes.

- **Session continuity** — Your
  conversation history is maintained while you work on a view. You can
  reference earlier requests in follow-up messages.
- **Resume conversations** — When you
  return to a view, you can continue a previous conversation about
  modifications.
- **Conversation context** — The
  Connect assistant maintains context across messages, so you can build
  incrementally. For example, you can create a form in one message,
  then add validation rules in the next.

## Best practices

- Be specific in your descriptions. Include component names, field
  labels, and layout preferences for more accurate results.
- Iterate in small steps. Start with a base layout and refine with
  follow-up messages rather than describing an entire complex view in
  a single prompt.
- Review before publishing. Always review the generated components
  on the canvas and test the view before publishing it for agent or
  customer use.
- Use the revert button if you ever want to go back to a prior
  build that the Connect assistant generated.
- Use the Connect assistant for explanations. If you are unsure about a
  component or configuration, ask the Connect assistant before making changes
  manually.
- Combine manual and Connect assistant workflows. You can use the Connect assistant to
  generate the base layout, then fine-tune using the standard UI
  builder drag-and-drop and property panels.

## Limitations

- The Connect assistant generates components available in the Connect Customer UI
  component library. It cannot create custom components outside this
  library.
- Multi-step guide workflows (views that span multiple steps)
  require creating each view separately. You can maintain context
  across views by referencing prior conversations using the same
  session.
- The Connect assistant does not have yet access to your existing flow
  configurations. Dynamic field references might need manual
  verification to match your specific flow setup.
