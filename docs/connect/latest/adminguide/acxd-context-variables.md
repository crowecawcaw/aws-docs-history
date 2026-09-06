

# Context variables
<a name="acxd-context-variables"></a>

Context variables store information that should remain available throughout a conversation session.

Use context variables when your application needs to remember information across flows, personalize responses, route users, avoid repeat questions, or pass context between the flow in Amazon Connect Customer and agentic CX designer.

For example, after a user is authenticated, you can set a context variable called `isAuthenticated` to `true`. Any flow in the same session can then check that value instead of asking the user to authenticate again.

To access context variables, select **Resources** from your workspace menu, then choose **Context variables**.

A context variable is a session-scoped value that can be referenced across flows.

Context variables are useful for information such as:
+ Customer name
+ Email address
+ Account ID
+ Claim number
+ Authentication status
+ Member or rewards tier
+ Issue type
+ Transfer summary
+ Callback number
+ Sentiment or intent
+ Retry counters
+ Selected product, reservation, appointment, or case

Context variables persist for the duration of the conversation session. They are different from local variables, which are intended for use within a single flow.

Use a Define node for temporary values that do not need to be shared across flows or passed during escalation.

## Creating a context variable
<a name="acxd-context-variables-create"></a>

**To create a context variable**

1. Open **Resources** from the workspace menu.

1. Select **Context variables**.

1. Select **Create context variable**.

1. Enter a variable name.

1. Choose the data type or define a schema.

1. Optionally add a description.

1. Confirm whether **Client-side updates** should remain enabled.

1. Save the context variable.

Use clear, predictable names.

Examples:
+ customerName
+ claimNumber
+ isAuthenticated
+ transferSummary
+ callbackNumber
+ customerIntent
+ selectedReservation

Context variable names should match exactly wherever they are referenced. Names are case-sensitive.

Each context variable has a schema that defines the type of value it can store.

Common types include:


|  |  | 
| --- |--- |
| **String** | Text values, such as name, email, claim number, or summary. | 
| **Number** | Numeric values, such as retry count or score. | 
| **Boolean** | True or false values, such as authentication status. | 
| **Object** | Structured data, such as a customer profile or reservation. | 
| **Array** | Multiple values, such as selected items or available options. | 

For complex structures, use auto-generate schema when available to create a schema from sample JSON.

## Client-side updates
<a name="acxd-context-variables-client-side"></a>

The **Client-side updates** setting controls whether values from outside agentic CX designer can update the context variable.

Keep this setting enabled when the value should be populated from:
+ Connect Customer
+ A frontend client
+ Touchpoint

Disable this setting when the value should only be set or modified inside agentic CX designer flows.

This setting is especially important when passing data from a flow in Connect Customer into agentic CX designer.

The exception is `nlx_userId`. When `nlx_userId` is passed on the Agentic CX block in a Connect Customer flow, it sets the built-in {System.userId} variable in agentic CX designer. You do not need to create a context variable named `nlx_userId`.

## Referencing context variables
<a name="acxd-context-variables-reference"></a>

After a context variable is created, you can reference it in supported fields across flows.

To reference a context variable, type { in a supported text field, then select the context variable from the placeholder menu.

Examples:

```
Thanks, {customerName}. I found your claim: {claimNumber}.
The customer's authentication status is {isAuthenticated}.
Here is the summary I'll pass to the agent: {transferSummary}.
```

Context variables can be used in:
+ Messages
+ Split conditions
+ Data request payloads
+ Agent prompts
+ Knowledge base questions
+ Node payloads
+ Modality payloads
+ State modifications

## Receiving context from Connect Customer
<a name="acxd-context-variables-from-connect"></a>

Connect Customer can send context into an agentic CX designer session.

Use this when the contact flow already knows information that the conversational AI should use, such as a phone number, customer ID, claim number, language, account status, or previously collected intent.

In the Connect Customer flow, configure the Agentic CX block to send context variables into the agentic CX designer session.

In the block's **Context variables** section, add key-value pairs.

Each key should match a context variable created in agentic CX designer. The exception is `nlx_userId`. Passing `nlx_userId` on the Agentic CX block automatically sets {System.userId} in agentic CX designer. No matching context variable is required.

For context variables your team creates in agentic CX designer, you can set values in two ways:


|  |  | 
| --- |--- |
| **Static value** | Enter a fixed value directly in the Agentic CX block. | 
| **Dynamic value** | Pull a value from the contact flow, contact attributes, or another supported Connect Customer namespace. | 

Example:


| Key | Value source | 
| --- | --- | 
| claimNumber | Existing contact attribute for the user's claim number | 
| customerName | Existing customer name value from Profiles | 
| customerIntent | Intent or reason collected earlier in the contact flow | 

When the conversation reaches the Agentic CX block, the configured key-value pairs are passed into agentic CX designer and populate matching context variables for the session.

When passing context from Connect Customer into agentic CX designer:
+ For standard context variables, the context variable must exist in agentic CX designer.
+ The key name must match exactly.
+ Names are case-sensitive.
+ **Client-side updates** must be enabled for the context variable.
+ The value must be available before or when the Agentic CX block invokes the application.
+ You do not need to add a system-internal prefix to the context variable name.
+ The special key `nlx_userId` does not need to be created as a context variable. When passed on the Agentic CX block, it sets {System.userId}.

For example, use:

```
claimNumber
```

Not:

```
acxd_claimNumber
```

## Setting context variables with state modifications
<a name="acxd-context-variables-state-modifications"></a>

Context variables can also be set or updated inside agentic CX designer flows.

Use **State modifications** when you want to copy a value into a context variable so it can be used later in the same session.

Examples:
+ Set `isAuthenticated` after a successful authentication Data request.
+ Set `selectedReservation` after the user chooses a reservation.
+ Set `customerIntent` after a User input or Split node identifies the issue.
+ Set `transferSummary` after a Generative text node creates a summary.

Common pattern:

1. Capture or retrieve a value.

1. Add a node with State modifications (be sure to do that downstream from a successful capture/retrieval).

1. Set the context variable to the captured or generated value.

1. Reference the context variable in later flows.

Use this pattern when values need to persist across multiple flows.

## Sending context back to Connect Customer
<a name="acxd-context-variables-to-connect"></a>

Agentic CX designer can send context back to Connect Customer during escalation events.

Use this when a conversation transfers to an agent and the Connect Customer flow needs a summary, intent, callback number, customer selection, or other context collected by the AI.

To pass data back to Connect Customer, add a Node payload to the Escalate node in your agentic CX designer flow.

The Node payload must use key-value syntax:

```
summary={transferSummary}
```

Do not enter only the variable by itself.

Avoid:

```
{transferSummary}
```

Use:

```
summary={transferSummary}
```

If the payload does not use key={variable} format, the value may not be created as an attribute for the contact flow.

To pass multiple values, separate each key-value pair with &.

Example:

```
summary={transferSummary}&customerIntent={customerIntent}
&callbackNumber={callbackNumber}
```

Each key becomes a separate value that Connect Customer can reference after escalation.

Examples:
+ summary
+ customerIntent
+ callbackNumber

After the agentic CX designer escalation occurs, returned values can be used in the Connect Customer flow.

Use a **Set contact attributes** block after the Agentic CX block to store or remap the returned values.

**To store returned values**

1. Add a **Set contact attributes** block after the Agentic CX block.

1. Create an output attribute, such as Key: transferSummary.

1. Set the value dynamically from the Agentic CX returned context.

1. Select the Agentic CX namespace shown in the Connect Customer block.

1. Select the returned key, such as `summary`.

1. Confirm the block.

Example mapping:


| Contact attribute key | Returned context key | 
| --- | --- | 
| transferSummary | summary | 
| customerIntent | customerIntent | 
| callbackNumber | callbackNumber | 

## Troubleshooting
<a name="acxd-context-variables-troubleshooting"></a>


| Issue | Cause | Fix | 
| --- | --- | --- | 
| Context variable is not populated in agentic CX designer | Name mismatch or client-side updates disabled | Confirm exact name match and enable Client-side updates in the context variable's Settings. | 
| {System.userId} is not populated for a chat interaction | nlx\_userId was not passed on the Agentic CX block, or the value was not available in the Connect Customer flow at the time the block was invoked. | In the Agentic CX block's context variables section, pass nlx\_userId and map it to the correct Connect Customer value, such as a contact attribute containing the customer ID. Do not create nlx\_userId as a context variable in agentic CX designer. Simply reference {System.userId} in agentic CX designer. | 
| Value from Connect Customer is missing | Value was not set before the Agentic CX block or not mapped into context variables | Set the value earlier in the contact flow and map it in the Agentic CX block. | 
| Returned attribute is not available in Connect Customer | Node payload used {variable} without a key | Use key={variable} format. | 
| Payload value is empty or null | Variable is not in scope at the Escalate node | Use a context variable, Define output, Generative text output, or captured slot available downstream. | 
| Generative Journey value is not available later | Value was collected internally but not captured as a slot | Add the value as a required or optional slot in Data capture. | 
| Value is needed in multiple flows | Slot or local variable is flow-scoped | Copy the value into a context variable with state modifications. | 
| Returned value is hard to find in Connect Customer | Namespace or key is mismatched | Use the Agentic CX namespace shown in the Connect Customer block and confirm the exact key spelling. | 