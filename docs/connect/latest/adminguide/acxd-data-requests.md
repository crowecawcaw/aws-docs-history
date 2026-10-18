

# Data requests
<a name="acxd-data-requests"></a>

Data requests are custom integrations that let agentic CX designer send data to, or retrieve data from, external systems during a conversation.

Use data requests when your conversational AI application needs real-time information or needs to trigger an action in another system. For example, a data request can retrieve appointment availability, look up a customer profile, check order status, or send a confirmation message.

Data requests can be used in two main ways:


|  |  | 
| --- |--- |
| **Data request node** | Trigger the data request at a specific point in a deterministic flow, then use the returned data in later nodes. | 
| **Agentic tool** | Attach the data request as a tool to an agent node so the agent can call it when needed to complete a user task. | 

To access data requests, select **Resources** from your workspace menu, then choose **Data requests**.

Use data requests to connect conversations to systems such as scheduling tools, ticketing systems, order systems, account databases, and messaging services.

Common examples include:
+ Providing available appointment times
+ Authenticating a user
+ Retrieving customer profile or account details
+ Checking order, claim, or ticket status
+ Looking up products
+ Sending confirmation emails
+ Updating a reservation or appointment

## How data requests work
<a name="acxd-data-requests-how"></a>

A data request defines how agentic CX designer communicates with an external system.

When a data request is triggered, agentic CX designer can:

1. Send a request to an external endpoint.

1. Pass values from the conversation into the request.

1. Receive a structured response.

1. Make returned values available to the flow or agent.

1. Use those values in messages, conditions, user choices, prompts, or downstream logic.

For example, a scheduling flow may collect a user's preferred date, send it to an appointment API, receive available time slots, and present those options back to the user.

## Creating a data request
<a name="acxd-data-requests-create"></a>

**To create a data request**

1. Open **Resources** from the workspace menu.

1. Select **Data requests**.

1. Select **New data request**.

1. Enter a clear name.

1. Add a description.

1. For **Implementation**, select the implementation type (static, external, Model Context Protocol (MCP), or Connect flow module).

1. Define the request/response model, or MCP tools.

1. Save and test the data request.

Use a name and description that make the purpose easy for teammates to understand.

Examples:
+ GetAppointmentAvailability
+ AuthenticateCustomer
+ GetOrderStatus
+ UpdateReservation
+ SendConfirmationEmail

## Implementation types
<a name="acxd-data-requests-implementations"></a>

The **Implementation** tab defines what happens when the data request is called.

The following table describes the four implementation types.


|  |  | 
| --- |--- |
| **Static** | Returns a fixed response. Use this for prototyping, testing flow logic, or building before an endpoint is ready. | 
| **External** | Calls a configured external endpoint using an HTTP method, URL, headers, parameters, and request/response models. Use this for traditional API or webhook calls. | 
| **MCP** | Connects to an MCP server endpoint and syncs available tools so they can be reviewed, enabled, and used from the data request resource. Use this when the external service exposes tool-based capabilities through MCP. | 
| **Connect flow module** | Invokes a published flow module in your Connect Customer instance and returns its output to the conversation. Use this type to reuse conversation logic you already built and govern in Connect Customer, instead of building and maintaining an external endpoint. | 

Use a *Static* implementation when you want the data request to return sample data without calling an external system.

Static responses are useful when:
+ The real endpoint is not ready yet
+ You want to test flow logic first
+ You need predictable sample data
+ You are prototyping a new experience

For example, you might return a sample list of appointment times so you can build and test a scheduling flow before connecting to the real scheduling system.

Use an *External* implementation when the data request should call a real API or webhook.

When configuring an external implementation, define details such as:
+ HTTP method
+ Endpoint URL
+ URL parameters
+ Headers
+ Request payload
+ Response structure

External implementations can support separate Production and Development endpoint configurations. This lets you test safely against a development endpoint before using production systems.

If the endpoint requires authentication, use Secrets instead of hardcoding API keys, tokens, or credentials directly into headers or payloads.

Use an *MCP* implementation when the external service exposes one or more tools through an MCP server.

When configuring an MCP implementation, you provide the MCP endpoint details, such as:
+ HTTP method
+ Production endpoint URL
+ Headers, such as an authorization header
+ Dynamic header behavior, if needed

After the MCP implementation is configured, use **Sync** to retrieve the available tools from the MCP server. Synced tools appear in the **Tools** section of the data request.

From the **Tools** section, you can:
+ Review available MCP tools
+ Enable or disable individual tools
+ Expand a tool to review its description
+ Inspect expected arguments
+ Review available input schema details
+ See whether the tool declares an output schema

Each tool can include a description and an argument schema that explains what information the tool expects.

MCP implementations can support separate Production and Development endpoint configurations. This lets you test safely against a development endpoint before using production systems.

If the endpoint requires authentication, use Secrets instead of hardcoding API keys, tokens, or credentials directly into headers or payloads.

For external or MCP implementations, dynamic headers can let you adjust header values when the data request is used.

Use dynamic headers when a header value may change based on the flow, environment, or context.

For sensitive or reusable values, such as API keys, bearer tokens, or authorization headers, use Secrets instead of entering the value directly.

Use a *Connect flow module* implementation when a data request should call a published flow module in your Connect Customer instance. A flow module packages conversation logic that you author, version, and govern in Connect Customer. With this implementation type, agentic CX designer invokes that logic during a conversation and returns its output to your application. You reuse governed logic instead of standing up and maintaining an external endpoint.

When you configure a *Connect flow module* implementation, you select and review the following items:
+ The published flow module to invoke
+ The module version
+ The read-only request and response models
+ An optional mock response used for testing

**Important**  
Before a flow module appears in agentic CX designer, an administrator must publish the module and enable external invocation for it in Connect Customer. You can select only modules that an administrator has published and enabled for external invocation. For instructions on preparing a module, see [Create module as tools](contact-flow-modules.md#create-module-as-tools).

When you configure the implementation, you choose a module version. Choose **Latest** to always use the current published version of the module. When you republish the module, the data request uses the new current version. Choose a specific version number to pin the data request to that exact version. The data request keeps using that version even after you republish the module.

For a *Connect flow module* data request, the request and response models are read-only. These models derive from the module's input and output parameters, which you edit in Connect Customer. You cannot change the fields of these models in agentic CX designer. The only setting you can edit here is each field's sensitivity.

**To configure a Connect flow module data request**

1. For the implementation method, choose **Connect flow module**.

1. For the module, choose **Select Connect flow module**, then choose a module from the list.

   Only modules that are published and externally invocable appear in the list. A module that is not published, or that is not externally invocable, does not appear in the list. If you expect a module and cannot find it, prepare it as described in the prerequisites, then reopen the list.

1. For the version, choose **Select version**, then choose **Latest** or a specific version number.

1. Review the read-only request and response models.

1. (Optional) For **Mock response**, enter valid JSON. The data request uses the mock response only when you test it.

   When you test the data request in the resource editor, on the canvas, or on the application page, agentic CX designer returns this mock response and never invokes the live module. A flow module runs only in a real conversation. Author a mock response that matches the shape of the module's response model so that your tests exercise realistic data.

After you configure the implementation, add the data request to a flow so your conversation can call the module and use its results. This procedure adds a data request node that calls the module and makes the returned data available to later nodes.

Before you start, configure the *Connect flow module* implementation for the data request, including the module, version, and models. For instructions on preparing a module in Connect Customer, see [Create module as tools](contact-flow-modules.md#create-module-as-tools).

The **Payload** editor is bound to the module's declared input schema. It marks required fields.

**To use the data request in a data request node**

1. Add a data request node and select the *Connect flow module* data request you configured.

1. In the **Payload** editor, map the values to send to the module. Provide a value for each required field, either a literal value or a reference to conversation data.

1. For **Output variable**, enter a name for the variable that receives the module's result.

1. Reference the fields of the output variable in later nodes to use the returned data downstream in the conversation.

**Important**  
Saving a *Connect flow module* data request validates only the shape of the request. For example, it checks that the mock response is valid JSON and that field values are within their limits. Saving does not verify that the referenced module exists, is published, or is externally invocable.  
Saving accepts a reference to a module that is missing or ineligible. The reference fails during a live conversation, when the module cannot be invoked. Confirm that the module is published and externally invocable before you rely on the data request in production.

The following limits apply to a *Connect flow module* data request.


| Field | Constraint | 
| --- | --- | 
| **Connect flow module** | Required. The module identifier is 1 to 256 characters. | 
| **Version** | Optional. Defaults to **Latest**. A specific version is an integer of 1 or greater. | 
| **Mock response** | Optional. Up to 200,000 characters. Must be valid JSON. Used only when you test the data request. | 
| **Payload** | Optional. Bound to the module's input schema. The serialized request payload is 1 to 60,000 characters. | 
| **Output variable** | Required. A local variable name that receives the module's result. | 

The module's response is limited to 1 MiB (1,048,576 bytes). If a response is larger than this limit, agentic CX designer rejects it instead of truncating it, and the data request takes the failure path. Because the limit is measured in bytes, a response that contains multi-byte characters reaches the limit with fewer characters.

Use a mock response that matches the shape of the module's response model so that your tests behave like a real invocation. The following JSON mock response returns an order status:

```
{
  "orderStatus": "SHIPPED",
  "estimatedDelivery": "2026-10-02",
  "carrier": "ExampleCarrier"
}
```

When you test the data request, agentic CX designer returns this response instead of invoking the module. To reference a field of this result downstream, use the output variable name. For example, if the output variable is named `orderLookup`, reference `orderLookup.orderStatus`.

In the **Payload** editor, map each required input field to a literal value or to conversation data. In the following example, replace `A12345` and `C67890` with your own order and customer identifiers.

The following JSON payload maps two values to the module's declared input fields:

```
{
  "orderId": "A12345",
  "customerId": "C67890"
}
```

## Request model
<a name="acxd-data-requests-request-model"></a>

The request model defines the optional payload that agentic CX designer sends to the external system.

Use a request model when the API needs values from the conversation.

You may select the Auto-generate option (star icon) to input sample JSON for easily constructing a complex schema structure.

Examples:


| Request field | Example use | 
| --- | --- | 
| `email` | Send the user's email to retrieve a profile. | 
| `appointmentDate` | Send a selected date to retrieve available times. | 
| `orderId` | Send an order number to retrieve order status. | 
| `reservationId` | Send a reservation ID to update a booking. | 
| `message` | Send a confirmation message to an external notification service. | 

Fields in the request model can be populated dynamically from values captured in the conversation, such as slots, context variables, system variables, or prior data request results.

## Response model
<a name="acxd-data-requests-response-model"></a>

The response model defines the structure of the data returned from the external system.

Use the response model to shape returned data so it can be referenced in the conversation.

You may select the Auto-generate option (star icon) to input sample JSON for easily constructing a complex schema structure.

Examples:


| Response data | How it might be used | 
| --- | --- | 
| `firstName` | Personalize a greeting or confirmation. | 
| `availableTimes` | Present appointment options to the user. | 
| `orderStatus` | Tell the user where their order stands. | 
| `confirmationNumber` | Confirm a completed action. | 
| `eligibleItems` | Show selectable return or exchange options. | 

A clear response model makes it easier to use returned values in later nodes, prompts, user choices, conditions, and messages.

When defining request and response models, choose the property type that matches the value.


|  |  | 
| --- |--- |
| **String** | A text value, such as a name, email, status, or confirmation message. | 
| **Number** | A numeric value, such as age, quantity, price, or count. | 
| **Boolean** | A true or false value, such as whether a customer is authenticated or eligible. | 
| **List** | A list of values, such as available times, products, orders, or options. | 
| **Object** | A structured group of related values, such as a customer profile or reservation record. | 

Use Array when the response returns multiple values that may need to be presented as options. Use Object when the response returns a structured item with multiple properties.

List responses are useful when a user needs to choose from returned options.

Examples:
+ Available appointment times
+ Open reservations
+ Eligible return items
+ Nearby store locations
+ Support ticket results

A list can be used with a User choice node when the user should select from returned options.

If the response contains a list of objects, use a Loop node to iterate over the nested values, or a Transform node or Generative text node to change the schema to a desired output and reference the correct nested properties depending on how you want to display or process the returned values.

## Sensitive fields
<a name="acxd-data-requests-sensitive"></a>

You can mark fields as **Sensitive** to help prevent values from appearing in conversation logs where supported.

Use sensitive fields for values such as:
+ Personally identifiable information
+ Account identifiers
+ Tokens or credentials
+ Payment-related data
+ Authentication responses
+ Protected customer details

To mark a field as sensitive, open the field settings and enable the **Sensitive** toggle.

You may also use the data request-level sensitive setting if the entire data request should be treated as sensitive.

## Data request settings
<a name="acxd-data-requests-settings"></a>


|  |  | 
| --- |--- |
| **Description** | Explains the purpose of the data request. Helpful for builders and for agent tool use. | 
| **Sensitive** | Prevents values for the data request from appearing in logs where supported. Useful for concealing sensitive or personally identifiable information. | 
| **Send context** | Sends available conversation context variables when the webhook is called. This is enabled by default when supported. | 

## Testing a data request
<a name="acxd-data-requests-test"></a>

Use the test feature to confirm that a data request is configured correctly before using it in a flow or agent node.

**To test a data request**

1. Open **Resources**.

1. Select **Data requests**.

1. Choose the data request you want to test.

1. Select **Test**.

1. Enter any required test values.

1. Choose the environment to test, if applicable.

1. Run the test.

1. Review the response.

A successful test should return the expected response structure based on your response model.

If the test fails, review:
+ Endpoint URL
+ HTTP method
+ Headers
+ Secrets or authentication values
+ URL parameters
+ Request payload
+ Request model
+ Response model
+ Environment selection

## Using a data request in a flow
<a name="acxd-data-requests-in-flow"></a>

**To use a data request in a deterministic flow**

1. Open the flow in the Canvas.

1. Add a Data request node.

1. Select the data request.

1. Map required request fields to values collected upstream from the conversation.

1. Connect the success path to the next node.

1. Configure failure, timeout, or in-progress paths.

1. Save and test the flow.

After the data request returns successfully, use the returned values in downstream messages, conditions, user choices, or other nodes.

Example:

"I found three available times: {AvailableTimes}. Which one works best for you?"

## Using a data request as an agent tool
<a name="acxd-data-requests-as-tool"></a>

**To use a data request as an agentic tool**

1. Open the flow that contains the agent node.

1. Select the agent node.

1. Add a custom data request tool.

1. Choose the data request.

1. Provide a clear tool prompt or description.

1. Define when the agent should call the tool.

1. Map any required inputs to values collected upstream or allow the agent to collect them.

1. Save and test the agent behavior.

Use this pattern when the agent should decide when to call the integration as part of completing a task.

Example:

A rescheduling agent may collect the user's preferred date, call a data request to retrieve availability, ask the user to choose a time, then call another data request to update the appointment.

## Synchronous and asynchronous data requests
<a name="acxd-data-requests-async"></a>

On the data request node, the **Mode** control sets whether the conversation waits for the data request to finish. **Mode** has two options: **Synchronous** and **Asynchronous**. This setting is available on voice and chat.

In **Synchronous** mode, the conversation turn waits for the data request to resolve before it continues. The node routes the conversation on its result. For example, it can route along a success, failure, or timeout path.

In **Asynchronous** mode, the data request runs on a background path and the conversation turn continues without waiting. The result becomes available on a later turn.

Asynchronous mode removes the success and failure edges from the node. Because there is no failure edge in asynchronous mode, you must design failure handling differently. Plan how a later turn reads the result, and how the conversation responds when the result is missing or indicates a failure.

You can add an **In progress** edge to deliver a message while the request is still resolving. When you use the **In progress** edge, set a **Wait time** from 0 to 30,000 milliseconds. The conversation follows the **In progress** edge to deliver your message, then returns to the data request.

## Resolve flow module data request errors
<a name="acxd-data-requests-troubleshooting"></a>

Use the following table to resolve the messages you might see when you configure a *Connect flow module* data request in agentic CX designer, or when a data request fails during a conversation. Some messages appear in the designer while you build. Others reach you as the failure reason on a data request that failed during a live conversation. The symptom column shows the message text where a message exists. The cause and remediation help you correct the underlying configuration.


| Symptom | Cause | What to do | 
| --- | --- | --- | 
| Save error: **You must select a compatible flow module** | The selected module is not published, or it is not enabled for external invocation. | In Connect Customer, publish the module and enable it as a tool. Then return to the data request and select the module again. | 
| Notice: **Connect flow module not published** | The referenced module has no published version. | Publish a version of the module in Connect Customer. | 
| Notice: **External invocation disabled**, with the link **How to enable external invocation** | The module is not saved and published as a tool, so it cannot be invoked from outside a flow. | Enable external invocation on the module in Connect Customer. For instructions, see [Create module as tools](contact-flow-modules.md#create-module-as-tools). | 
| Drift banner: **Out of date**, with text about parameters that have changed since the models were last synced, and a **Re-sync** button | The module's input or output parameters changed in Connect Customer after the request and response models were last synced. | Choose **Re-sync**. Then review your mapped inputs and outputs, because a parameter might have been added, removed, or renamed. | 
| Mock editor error: **Invalid response** | The mock response does not match the response model. | Edit the mock response so that it matches the fields and types in the response model. | 
| Save or test error: **Invalid JSON mock response.** or **The mock response of this flow module data request is not valid JSON.** | The mock response is not valid JSON. | Enter valid JSON for the mock response. | 
| Empty state: **No Connect flow modules available** or **There are no Connect flow modules in your Connect Customer instance yet…** | Your instance has no modules that qualify, or no modules at all. | In Connect Customer, create a module, publish it, and enable it as a tool. | 
| A module you expect is missing from the module list | The module is not published, or it is not enabled for external invocation. Modules that do not qualify do not appear in the list. | In Connect Customer, publish the module and enable it as a tool. After the module qualifies, it appears in the list. | 
| Canvas warning: **Data request not found.** | The data request that the node references was deleted or is missing. | Recreate the data request, or select a different data request on the node. | 
| A data request saves without error but fails only during a live conversation | Saving validates the shape of your configuration. It does not check that the module exists, that your instance owns it, that it is published, or that it is enabled for external invocation. | Confirm that the module exists in your instance, is published, and is enabled as a tool. | 
| Failure reason: **Flow module request could not be built** | The request payload is outside the allowed size, or an input mapping is missing required context. | Reduce or correct the request payload, and check your input mapping against the module's required inputs. | 
| Failure reason: **flow module response exceeds the 1,048,576-byte limit** | The module returned a response larger than 1 MiB. The response is rejected, not truncated. | Reduce the size of the data that the module returns. | 
| Failure reason: **flow module response did not match its declared schema** | The module's output does not match the declared response model. | Change the module so that its output matches the declared response model. | 
| Failure reason: **flow module orchestration** followed by a status (for example, `TIMED_OUT` or `FAILED`), or the module's own error details | The module did not finish successfully. | Handle the failure edge on the data request node, and review the module's own error handling. | 
| Failure reason: **Flow module invocation throttled: request rate exceeded** | The synchronous request rate for the instance was exceeded. | Reduce the request rate, then retry. | 
| Failure reason: **Flow module invocation throttled: too many concurrent requests** | Too many asynchronous requests ran at the same time. | Reduce the number of concurrent requests, then retry. | 
| Failure reason: **Flow module endpoint could not be resolved** | The module's endpoint could not be resolved. This can happen after your Connect Customer account is migrated. | Contact AWS Support. This condition can persist, so retrying does not resolve it. | 
| Failure reason: **Flow module invocation failed** or **Failed to trigger async flow module invocation** | The invocation, or the asynchronous dispatch, failed. | Handle the failure edge on the data request node, then retry. | 

**Note**  
A data request can report success while its output variable holds unexpected or empty content. This can happen when a module signals a failure in a way that the data request node does not recognize as a failure. If a downstream step behaves as though the data succeeded when it did not, check the module's own error handling and confirm how the module reports failures in its output.

## Best practices
<a name="acxd-data-requests-best-practices"></a>
+ Use clear data request names and descriptions.
+ Use static implementations for prototyping before the real endpoint is ready.
+ Use external implementations for real API calls.
+ Use Secrets for API keys, tokens, and credentials.
+ Define request and response models clearly.
+ Mark sensitive fields appropriately.
+ Send only the data the external system needs.
+ Test the data request before using it in a flow or agent node.
+ Use a data request node for controlled deterministic calls.
+ Keep chained data request nodes shallow. Each data request node that runs in sequence across conversation turns adds to the time a customer waits. When you need several results, prefer adding several data requests to one node over chaining separate nodes across turns.

**Important**  
Make modules with side effects idempotent. A module that changes state, such as one that takes a payment, can run more than once for a single customer intent. A retried conversation turn can invoke the module again, and a deliberate repeat invocation of the same module on the same node might return the earlier result instead of running again. Design modules that have side effects to be idempotent, or add a guard that prevents a repeated action from taking effect twice.

**Important**  
Author failure-edge handling. When a data request fails, the customer hears nothing from this node unless you handle the failure. Authoring failure-edge handling is required, not optional. On the data request node, connect the failure edge to a step that responds to the customer or recovers the conversation.

**Note**  
Treat module output as untrusted. A flow module's output can be bound to a variable that a generative node later references. Validate or sanitize the module's output before you reference it from a generative node.