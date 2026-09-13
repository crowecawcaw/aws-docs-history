

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

## Create a context variable
<a name="acxd-context-variables-create"></a>

**To create a context variable**

1. Open **Resources** from the workspace menu.

1. Select **Context variables**.

1. Select **Add context variable**.

1. Enter a variable name.

1. Choose the data type or define a schema.

1. Optionally add a description.

1. Confirm whether **Allow frontend updates** should remain enabled.

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
| **List** | Multiple values, such as selected items or available options. | 

For complex structures, use auto-generate schema when available to create a schema from sample JSON.

## Allow frontend updates
<a name="acxd-context-variables-client-side"></a>

The **Allow frontend updates** setting controls whether values from outside agentic CX designer can update the context variable.

Keep this setting enabled when the value should be populated from:
+ Connect Customer flow
+ A frontend client
+ Touchpoint

Disable this setting when the value should only be set or modified inside agentic CX designer flows.

This setting is especially important when passing data from a flow in Connect Customer into agentic CX designer.

The exception is `nlx_userId`. When `nlx_userId` is passed on the Agentic CX block in a Connect Customer flow, it sets the built-in {System.userId} variable in agentic CX designer. You do not need to create a context variable named `nlx_userId`.

## Use a context variable in a flow
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

## Passing context from Connect Customer flows
<a name="acxd-context-variables-from-connect"></a>

Connect Customer flows can send context into an agentic CX designer application session.

Use this when the contact flow already knows information that the conversational AI should use, such as a phone number, customer ID, claim number, language, account status, or previously collected intent.

In the Connect Customer flow, configure the Agentic CX block to send context variables into the agentic CX designer session.

In the block's **Context variables** section, add key-value pairs.

Each key should match a context variable created in agentic CX designer. The exception is `nlx_userId`. Passing `nlx_userId` on the Agentic CX block automatically sets {System.userId} in agentic CX designer. No matching context variable is required.

For context variables your team creates in agentic CX designer, you can set values in two ways in the Connect Customer flow:


| Option | Use | 
| --- | --- | 
| **Set manually** | Enter a fixed value directly in the Agentic CX block. | 
| **Set dynamically** | Pull a value from the contact flow, contact attributes, or another supported Connect Customer namespace. | 

Example:


| Agentic CX context key | Dynamic value from Connect Customer | 
| --- | --- | 
| claimNumber | Existing contact variable for the user's claim number | 
| customerName | Existing customer name value from Profiles | 
| customerIntent | Intent or reason collected earlier in the contact flow | 

When the conversation reaches the Agentic CX block, the configured key-value pairs are passed into agentic CX designer and populate matching context variables for the session.

When passing context from Connect Customer flow into agentic CX designer:
+ For standard context variables, the context variable must exist in agentic CX designer.
+ The key name must match exactly.
+ Names are case-sensitive.
+ **Allow frontend updates** must be enabled for the context variable.
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

To set {System.userId} from a Connect Customer flow, use:

```
nlx_userId
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

## Passing context to Connect Customer flows
<a name="acxd-context-variables-to-connect"></a>

Agentic CX designer can send context back to Connect Customer flows when Escalation or Exit Application nodes are reached in an agentic CX designer flow.

Use this when a conversation exits from the Agentic CX block in the Connect Customer flow, and the downstream process requires a summary, intent, callback number, customer selection, or other context collected.

To pass data back, add one or more State modifications to the Escalate node in your agentic CX designer flow that Sets one or more context variables.

For example, you may set a context variable {summary} to a variable generated upstream by a Generative text node that summarized the system transcript.

### Receive returned context in Connect Customer flow
<a name="acxd-context-variables-return"></a>

After the agentic CX designer escalation occurs, returned values can be used in the Connect Customer flow.

Use a **Set contact attributes** block after the Agentic CX block to store or remap the returned values.

For example:

1. Add a **Set contact attributes** block after the Agentic CX block.

1. Create an output attribute, such as Key: `summary`.

1. Set the value dynamically from the agentic CX designer returned context.

1. Select the Agentic CX namespace shown in the Connect Customer block.

1. Select the returned key, such as `summary`.

1. Confirm the block.

Example mapping:


| Contact attribute key | Dynamic value from Agentic CX | 
| --- | --- | 
| transferSummary | summary | 
| customerIntent | customerIntent | 
| callbackNumber | callbackNumber | 

## Troubleshooting
<a name="acxd-context-variables-troubleshooting"></a>


| Issue | Cause | Fix | 
| --- | --- | --- | 
| Context variable is not populated in agentic CX designer | Name mismatch or frontend updates disabled | Confirm exact name match and enable Allow frontend updates in the context variables Settings. | 
| {System.userId} is not populated for a chat interaction | nlx\_userId was not passed on the Agentic CX block, or the value was not available in the Connect Customer flow at the time the block was invoked. | In the Agentic CX block's context variables section, pass nlx\_userId and map it to the correct Connect Customer value, such as a contact attribute containing the customer ID. Do not create nlx\_userId as a context variable in agentic CX designer. Simply reference {System.userId} in agentic CX designer. | 
| Value from Connect Customer flow is missing | Value was not set on Agentic CX block or not mapped into context variables | Map the value in the Agentic CX block. | 
| Returned attribute is not available in Connect Customer flow | Context variable not set | Use a state modification to Set a context variable in the flow of agentic CX designer when Escalate or Exit application nodes are reached. | 
| Context variable value is empty or null | Variable is not in scope at the Escalate node | Use a context variable, Define output, Generative text output, or captured slot available downstream. | 
| Generative Journey value is not available later | Value was collected internally but not captured as a slot | Add the value as a required or optional slot in Data capture. | 
| Value is needed in multiple flows | Slot or local variable is flow-scoped | Copy the value into a context variable with state modifications. | 
| Returned value is hard to find in Connect Customer flow | Namespace or key is mismatched | Use the Agentic CX namespace and confirm the exact key spelling. | 