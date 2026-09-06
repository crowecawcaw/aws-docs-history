# Working with flows

Flows define the structured paths your conversational AI application follows to help
users complete a task, answer a question, or move toward the right next step.

Each flow contains the logic, messages, nodes, variables, and routing behavior
needed to support a specific user intent or process. For example, one flow may
help a user book a room, while another flow may answer policy questions,
authenticate a user, utilize agentic AI to handle most tasks, or route the user to
human support.

Flows are built visually in the agentic CX designer Canvas, where you add and
connect nodes to map out each step of the experience.

A single application can include multiple flows, and a flow can also be reused
across multiple applications in the same workspace.

After a flow is attached to an application and included in a deployed build, the
application can execute that flow during conversations.

To access flows, select **Flows** from your workspace menu, then choose
**Canvas**.

## User intent and flow routing

A user's intent is what they are trying to do.

The application can recognize that the user wants to book a room and route the
conversation to a flow designed for that purpose, such as a Room Booking flow.

Inside that flow, the application may ask for details such as check-in date, checkout
date, number of guests, and room preference. The flow defines how those details
are collected, what systems are called, and what happens next.

A flow can be triggered in several ways.

Use routing descriptions, default behavior, and Redirect nodes together to control
when and how users move through flows.

|                         |                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Default behavior**    | A flow runs when assigned as the application's Welcome, Unknown, Fallback,<br>or Escalation behavior.                                                                                            |
| **User input routing**  | A User input node captures what the user says and attempts to match it to one of the<br>flows attached to the application via provided routing data.                                             |
| **User choice routing** | A User choice node can route to another flow if the user's response does not match<br>the expected choices but does match another flow attached to the application via<br>provided routing data. |
| **Redirect**            | A flow deliberately sends the user to another flow or page.                                                                                                                                      |
| **MCP tool**            | A flow is exposed as a tool that an agent node can invoke.                                                                                                                                       |

## Creating a flow

###### To create a flow

1. Open **Flows** from the workspace menu.
2. Select **Canvas**.
3. Select **Create flow**.
4. Enter a clear flow name (no spaces or special characters).
5. Select **Create**.

## The Canvas

The Canvas is the visual builder where you create and maintain a flow.

Every flow has its own Canvas. The Canvas begins with a non-editable Start node.
Connect the Start node to the first node in the flow so the conversation knows
where to begin.

Use the Canvas to:

- Add nodes
- Connect paths
- Create branches
- Add pages
- Test the flow
- Validate flow issues
- Review in-canvas analytics after deployment
- Configure flow settings

The Canvas toolbar provides controls for building, testing, and managing a flow.

Toolbar options include:

|                          |                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Application selector** | Switch between applications where the flow is attached.                                                                                                                                                                                                                                                                                                                                    |
| **Flow selector**        | Switch between flows attached to the selected application.                                                                                                                                                                                                                                                                                                                                 |
| **Pages**                | Create or navigate between pages within the current flow. Pages organize large flows<br>into smaller sections, especially when a flow has many branches, repeated steps, or<br>subprocesses. Use *_Move to page_<br>• from the canvas shortcut menu to move<br>selected nodes into a separate page and automatically create the Redirect nodes<br>needed to connect the conversation path. |
| **Analytics**            | View traffic data for deployed applications and review user paths.                                                                                                                                                                                                                                                                                                                         |
| **Issues**               | Show issues such as disconnected paths, missing handling, or possible loops.                                                                                                                                                                                                                                                                                                               |
| **Settings**             | Configure routing, MCP, attached slots, languages, versions, and flow details.                                                                                                                                                                                                                                                                                                             |
| **Save**                 | Save changes made on the Canvas.                                                                                                                                                                                                                                                                                                                                                           |
| **Test**                 | Open the test widget to test from the current flow.                                                                                                                                                                                                                                                                                                                                        |

## Import and export

The **Advanced** tab in the flow's settings includes import and export options that
help you move or reuse flow designs. Exporting a flow creates a JSON file that
preserves the conversation path and Canvas structure so it can be imported later
into a workspace.

Use export when you want to back up a flow, share a reusable flow pattern, or
move a flow design into another workspace. Use import when you have a
previously exported JSON file and want agentic CX designer to recreate that
conversation path on the Canvas.

###### To import or export a flow

1. Open the flow.
2. Select **Settings** from the Canvas toolbar.
3. Select the **Advanced** tab.
4. Choose **Export** to download the flow as a JSON file, or choose **Import** to upload
   a previously exported JSON file.

You can also import a flow by dragging and dropping a supported exported JSON
file directly onto the Canvas. After import, review the populated nodes, paths, and
configuration before saving, testing, building, and deploying the application.

You may also duplicate a flow when you want to reuse an existing flow structure as
a starting point.

###### To duplicate a flow

1. Open the flow.
2. Select **Settings** from the Canvas toolbar.
3. Select the **Advanced** tab.
4. Choose **Duplicate**.
5. Enter a name for the duplicated flow.

You can also find the option to delete a flow from the Advanced tab of the flow's
settings.

If the flow is attached to an application, update the application, create a new build,
and deploy the change so the deployed experience no longer references the
deleted flow.

## Canvas controls

Use Canvas controls to navigate and organize your flow.

Common controls include:

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **Zoom**        | Zoom in or out of the Canvas.                    |
| **Pan**         | Move around the Canvas.                          |
| **Auto-layout** | Align nodes into a cleaner layout.               |
| **Search**      | Find nodes or trigger quick commands.            |
| **Notes**       | Add internal notes for builders.                 |
| **Undo/Redo**   | Reverse or restore recent Canvas changes.        |
| **Flags**       | Mark important nodes or areas for easier review. |

You can also right-click the Canvas or an individual node to open shortcut menu
options.

## Flow settings

Flow settings define how a flow is recognized, reused, translated, and configured
for use in an application or agentic experience.

###### To access flow settings

1. Open a flow.
2. Select **Settings** from the Canvas toolbar.
3. Choose the tab you want to configure.

Settings include:

- Routing
- MCP
- Attached slots
- Languages
- Versions
- Advanced settings

## Routing

Routing helps agentic CX designer understand when a user's intent should match a
flow.

The most important routing field is the _AI description_.

Use the AI description to explain what the flow does and when it should be used.

Example:

```
Use this flow when the user wants to update, modify, or cancel an
existing hotel reservation.
```

A strong AI description should be:

- Concise
- Specific
- Action-oriented
- Written from the user's intent
- Distinct from other flow descriptions

Good examples:

```
Use this flow when the user wants to check the status of an order.

Use this flow when the user wants to book, reschedule, or cancel an
appointment.

Use this flow when the user has a billing question or needs help
understanding a charge.
```

If a flow is only assigned as default behavior or only reached through a Redirect
node, routing can be left blank.

## MCP

MCP lets you make a flow available as a tool that an agent can invoke.

Use MCP when a Generative Journey or Live Sync agent should call the flow as
part of completing a larger task.

###### To enable MCP on a flow

1. Open the flow.
2. Select **Settings** from the Canvas toolbar.
3. Open the **MCP** tab.
4. Enable the **MCP** toggle.
5. Add an input schema, if the flow requires values from the agent.
6. Save the flow.

MCP input schema defines the values the agent should collect or pass into the flow
before invoking it.

Use an input schema when the flow needs specific information to run correctly.

Example:

A restaurant recommendation flow may need:

- cuisine
- location
- partySize

For each input field:

1. Use a short input name with no spaces or special characters.
2. Choose the appropriate property type.
3. Add a clear description.
4. Save the schema.

Example input schema descriptions:

|              |                                                                     |
| ------------ | ------------------------------------------------------------------- |
| **cuisine**  | The type of food the user wants, such as Italian, Thai, or Mexican. |
| **location** | The area where the user wants to find a restaurant.                 |

Inside the MCP-enabled flow, type { in supported fields to reference MCP input
variables in messages, Data request payloads, Split conditions, and other node
configurations.

Example message:

```
I'll look for {cuisine} restaurants near {location}.
```

## Attached slots

Slots must be attached to a flow before the flow can use them.

Attach slots when the flow needs to collect or reference structured values from the
user, such as a date, time, email, name, room type, or yes/no response.

###### To attach a slot

1. Open the flow.
2. Select **Settings** from the Canvas toolbar.
3. Open the **Attached slots** tab.
4. Select **Add slot**.
5. Choose a custom or built-in slot.
6. Enter the name that should be used for the slot in this flow.
7. Save the flow.

Only slots attached to the flow appear for selection in supported nodes, such as
User choice and Generative Journey.

Use _custom slots_ for business-specific values that you define.

Examples:

- Yes / No
- Small / Medium / Large
- Billing / Technical support / Account access

Use _built-in slots_ for common input types that agentic CX designer already
supports.

Examples:

- Date
- Time
- Email
- Name
- Number
- Phone number
- URL
- Freeform text

Custom slots are created from **Resources > Slots**. Built-in slots are selected when
attaching slots to a flow.

## Languages

The **Languages** tab lets you manage which languages are assigned to the flow.

Use flow-level languages when a flow needs specific localization support or when
you need to override workspace-level language settings.

###### To add a language to a flow

1. Open the flow.
2. Select **Settings** from the Canvas toolbar.
3. Open the **Languages** tab.
4. Select **Add language**.
5. Choose the language or locale.
6. Save the flow.

After adding languages, manage translations for flow messages and other
translatable content.

Create a new application build after updating translations that should be included in
testing or deployment.

## Variables in flows

Variables let your flow use dynamic information instead of hardcoded text.

A variable may come from user input, a slot, a Data request, a context variable, a
system variable, a generated output, a knowledge base response, or an MCP input.

To reference a variable, type { in a supported text field and choose from the
placeholder menu.

###### Topics

- [Nodes](acxd-nodes.md "acxd-nodes.md")
- [Generative Journey](acxd-generative-journey.md "acxd-generative-journey.md")
- [Live Sync](acxd-live-sync.md "acxd-live-sync.md")
- [Escalations](acxd-escalations.md "acxd-escalations.md")
