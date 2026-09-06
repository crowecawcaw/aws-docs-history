# Data requests

Data requests are custom integrations that let agentic CX designer send data to, or
retrieve data from, external systems during a conversation.

Use data requests when your conversational AI application needs real-time
information or needs to trigger an action in another system. For example, a data
request can retrieve appointment availability, look up a customer profile, check
order status, or send a confirmation message.

Data requests can be used in two main ways:

|                       |                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Data request node** | Trigger the data request at a specific point in a deterministic flow, then use the<br>returned data in later nodes. |
| **Agent tool**        | Attach the data request as a tool to an agent node so the agent can call it when needed<br>to complete a user task. |

To access data requests, select **Resources** from your workspace menu, then
choose **Data requests**.

Use data requests to connect conversations to systems such as scheduling tools,
ticketing systems, order systems, account databases, and messaging services.

Common examples include:

- Providing available appointment times
- Authenticating a user
- Retrieving customer profile or account details
- Checking order, claim, or ticket status
- Looking up products
- Sending confirmation emails
- Updating a reservation or appointment

## How data requests work

A data request defines how agentic CX designer communicates with an external system.

When a data request is triggered, agentic CX designer can:

1. Send a request to an external endpoint.
2. Pass values from the conversation into the request.
3. Receive a structured response.
4. Make returned values available to the flow or agent.
5. Use those values in messages, conditions, user choices, prompts, or downstream logic.

For example, a scheduling flow may collect a user's preferred date, send it to an
appointment API, receive available time slots, and present those options back to the user.

## Creating a data request

###### To create a data request

1. Open **Resources** from the workspace menu.
2. Select **Data requests**.
3. Select **Create data request**.
4. Enter a clear name.
5. Add a description.
6. Select the implementation (static, external, or MCP).
7. Define the request/response model, or MCP tools.
8. Save and test the data request.

Use a name and description that make the purpose easy for teammates to understand.

## Implementation types

The **Implementation** tab defines what happens when the data request is called.

A data request can use one of three implementation types:

|              |                                                                                                                                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Static**   | Returns a fixed response. Use this for prototyping, testing flow logic, or building<br>before an endpoint is ready.                                                                                                           |
| **External** | Calls a configured external endpoint using an HTTP method, URL, headers,<br>parameters, and request/response models. Use this for traditional API or webhook calls.                                                           |
| **MCP**      | Connects to an MCP server endpoint and syncs available tools so they can be<br>reviewed, enabled, and used from the data request resource. Use this when the<br>external service exposes tool-based capabilities through MCP. |

Use a _Static_ implementation when you want the data request to return sample data
without calling an external system.

Static responses are useful when:

- The real endpoint is not ready yet
- You want to test flow logic first
- You need predictable sample data
- You are prototyping a new experience

For example, you might return a sample list of appointment times so you can build
and test a scheduling flow before connecting to the real scheduling system.

Use an _External_ implementation when the data request should call a real API or webhook.

When configuring an external implementation, define details such as:

- HTTP method
- Endpoint URL
- URL parameters
- Headers
- Request payload
- Response structure

External implementations can support separate Development and Production
endpoint configurations. This lets you test safely against a development endpoint
before using production systems.

If the endpoint requires authentication, use Secrets instead of hardcoding API keys,
tokens, or credentials directly into headers or payloads.

Use an _MCP_ implementation when the external service exposes one or more tools
through an MCP server.

When configuring an MCP implementation, you provide the MCP endpoint details, such as:

- HTTP method
- Production endpoint URL
- Headers, such as an authorization header
- Dynamic header behavior, if needed

After the MCP implementation is configured, use **Sync** to retrieve the available tools
from the MCP server. Synced tools appear in the **Tools** section of the data request.

From the **Tools** section, you can:

- Review available MCP tools
- Enable or disable individual tools
- Expand a tool to review its description
- Inspect expected arguments
- Review available input schema details
- See whether the tool declares an output schema

Each tool can include a description and an argument schema that explains what
information the tool expects.

MCP implementations can support separate Development and Production
endpoint configurations. This lets you test safely against a development endpoint
before using production systems.

If the endpoint requires authentication, use Secrets instead of hardcoding API keys,
tokens, or credentials directly into headers or payloads.

For external or MCP implementations, dynamic headers can let you adjust header
values when the data request is used.

Use dynamic headers when a header value may change based on the flow,
environment, or context.

For sensitive or reusable values, such as API keys, bearer tokens, or authorization
headers, use Secrets instead of entering the value directly.

## Request model

The request model defines the optional payload that agentic CX designer sends to
the external system.

Use a request model when the API needs values from the conversation.

You may select the Auto-generate option (star icon) to input sample JSON for
easily constructing a complex schema structure.

Examples:

- Send the user's email to retrieve a profile.
- Send a selected date to retrieve available times.
- Send an order number to retrieve order status.
- Send a reservation ID to update a booking.
- Send a confirmation message to an external notification service.

Fields in the request model can be populated dynamically from values captured in
the conversation, such as slots, context variables, system variables, or prior data
request results.

## Response model

The response model defines the structure of the data returned from the external system.

Use the response model to shape returned data so it can be referenced in the conversation.

You may select the Auto-generate option (star icon) to input sample JSON for
easily constructing a complex schema structure.

Examples:

- Personalize a greeting or confirmation.
- Present appointment options to the user.
- Tell the user where their order stands.
- Confirm a completed action.
- Show selectable return or exchange options.

A clear response model makes it easier to use returned values in later nodes,
prompts, user choices, conditions, and messages.

When defining request and response models, choose the property type that matches the value.

|             |                                                                                         |
| ----------- | --------------------------------------------------------------------------------------- |
| **String**  | A text value, such as a name, email, status, or confirmation message.                   |
| **Number**  | A numeric value, such as age, quantity, price, or count.                                |
| **Boolean** | A true or false value, such as whether a customer is authenticated or eligible.         |
| **Array**   | A list of values, such as available times, products, orders, or options.                |
| **Object**  | A structured group of related values, such as a customer profile or reservation record. |

Use Array when the response returns multiple values that may need to be presented
as options. Use Object when the response returns a structured item with multiple properties.

List responses are useful when a user needs to choose from returned options.

Examples:

- Available appointment times
- Open reservations
- Eligible return items
- Nearby store locations
- Support ticket results

A list can be used with a User choice node when the user should select from returned options.

If the response contains a list of objects, use a Loop node to iterate over the nested
values, or a Transform node or Define node to change the schema to a
desired output and reference the correct nested properties depending on how you
want to display or process the returned values.

## Sensitive fields

You can mark fields as **Sensitive** to help prevent values from appearing in
conversation logs where supported.

Use sensitive fields for values such as:

- Personally identifiable information
- Account identifiers
- Tokens or credentials
- Payment-related data
- Authentication responses
- Protected customer details

To mark a field as sensitive, open the field settings and enable the **Sensitive** toggle.

You may also use the data request-level sensitive setting if the entire data request
should be treated as sensitive.

## Data request settings

|                  |                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**  | Explains the purpose of the data request. Helpful for builders and for agent tool use.                                                                  |
| **Sensitive**    | Prevents values for the data request from appearing in logs where supported. Useful<br>for concealing sensitive or personally identifiable information. |
| **Send context** | Sends available conversation context variables when the webhook is called. This<br>is enabled by default when supported.                                |

## Testing a data request

Use the test feature to confirm that a data request is configured correctly before
using it in a flow or agent node.

###### To test a data request

1. Open **Resources**.
2. Select **Data requests**.
3. Choose the data request you want to test.
4. Select **Test**.
5. Enter any required test values.
6. Choose the environment to test, if applicable.
7. Run the test.
8. Review the response.

A successful test should return the expected response structure based on your response model.

If the test fails, review:

- Endpoint URL
- HTTP method
- Headers
- Secrets or authentication values
- URL parameters
- Request payload
- Request model
- Response model
- Environment selection

## Using a data request in a flow

###### To use a data request in a deterministic flow

1. Open the flow in the Canvas.
2. Add a Data request node.
3. Select the data request.
4. Map required request fields to values collected upstream from the conversation.
5. Connect the success path to the next node.
6. Configure failure, timeout, or in-progress paths.
7. Save and test the flow.

After the data request returns successfully, use the returned values in downstream
messages, conditions, user choices, or other nodes.

## Using a data request as an agent tool

###### To use a data request as an agentic tool

1. Open the flow that contains the agent node.
2. Select the agent node.
3. Add a custom data request tool.
4. Choose the data request.
5. Provide a clear tool prompt or description.
6. Define when the agent should call the tool.
7. Map any required inputs to values collected upstream or allow the agent to collect them.
8. Save and test the agent behavior.

Use this pattern when the agent should decide when to call the integration as part
of completing a task.

Example:

A rescheduling agent may collect the user's preferred date, call a data request to
retrieve availability, ask the user to choose a time, then call another data request to
update the appointment.

## Best practices

- Use clear data request names and descriptions.
- Use static implementations for prototyping before the real endpoint is ready.
- Use external implementations for real API calls.
- Use Secrets for API keys, tokens, and credentials.
- Define request and response models clearly.
- Mark sensitive fields appropriately.
- Send only the data the external system needs.
- Test the data request before using it in a flow or agent node.
- Use a data request node for controlled deterministic calls.
