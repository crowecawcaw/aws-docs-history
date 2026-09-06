# Configuring escalations

Escalations let an agentic CX designer conversation hand control back to a flow in
Amazon Connect Customer when the user needs human support or the application should
leave the conversational AI experience.

Use escalations when a task requires an agent, a business rule prevents
automation, the user asks for a person, or the flow needs to transfer the
conversation into a Connect Customer queue.

When an Escalate node is reached in an agentic CX designer flow, the conversation
exits through the Escalation path on the Agentic CX block in the Connect Customer
flow.

From there, the Connect Customer flow controls what happens next.

A common escalation pattern is:

1. The user reaches an Escalate node in agentic CX designer.
2. The conversation returns to the flow in Connect Customer through the Escalation path on the Agentic CX block.
3. A **Set contact attributes** block stores any context returned from agentic CX designer.
4. A **Set working queue** block selects the queue.
5. A **Transfer to queue** block transfers the customer to an agent.

## Adding an escalation to a flow

###### To add an escalation to a flow

1. Open the flow in the Canvas.
2. Add an Escalate node where the conversation should transfer out of agentic CX designer.
3. Add a message, if needed.
4. Optionally add a Node payload to pass context back to a flow in Connect Customer.
5. Connect any available failure, timeout, or continuation paths.
6. Save the flow.
7. Create a new application build and deploy it to the environment used by the Connect Customer flow.

Example escalation message:

```
Connecting you to an agent now.
```

## Passing escalation context

You can pass context back to a Connect Customer flow from the Escalate node
using Node payload.

Use this when you want the human agent or Connect Customer flow to receive
information collected or generated during the AI conversation.

Examples of escalation context:

- Transfer summary
- Customer intent
- Sentiment
- Authentication status
- Callback number
- Claim number
- Selected product or reservation
- Reason for escalation

The Node payload must use key-value syntax:

```
summary={transferSummary}
```

The key on the left becomes the value available to Connect Customer. The value on
the right references the agentic CX designer variable.

Do not enter only the variable by itself.

Avoid:

```
{transferSummary}
```

Use:

```
summary={transferSummary}
```

To pass multiple values, separate them with &:

```
summary={transferSummary}&customerIntent={customerIntent}
&callbackNumber={callbackNumber}
```

## Setting contact attributes in Connect Customer

After the Agentic CX block's Escalation path, add a **Set contact attributes** block in
a flow in Connect Customer.

Use this block to store the values returned from agentic CX designer so they can be
used later in the Connect Customer flow or surfaced to an agent.

###### To set returned context

1. In the Connect Customer flow, connect the Escalation path from the Agentic CX block to a **Set contact attributes** block.
2. Add a new contact attribute.
3. Enter the attribute key you want to create, such as `transferSummary`.
4. Choose **Use attribute**.
5. Select the **Agentic CX** namespace.
6. Select the returned context value, such as `summary`.
7. Confirm the block.

Example mapping:

| Contact attribute key | Returned context key |
| --------------------- | -------------------- |
| transferSummary       | summary              |
| customerIntent        | customerIntent       |
| callbackNumber        | callbackNumber       |

Use clear attribute names so the values are easy to reference later in the Connect Customer
flow or agent workspace.

After setting contact attributes, continue the Connect Customer flow by routing the
customer to the appropriate queue.

A typical queue transfer sequence is:

1. **Set contact attributes** — Stores context returned from agentic CX designer.
2. **Set working queue** — Selects the queue the contact should use.
3. **Transfer to queue** — Transfers the customer to the selected queue.

For example, if the AI determines that the user needs billing support, the escalation
path can pass `customerIntent=billingSupport`. The Connect Customer flow can
then use that value to route the customer to the correct queue.

## Escalation context for agents

Escalation context helps the human agent understand what happened before the
transfer.

Use returned context to provide:

- A short summary of the AI conversation
- The reason for escalation
- Values the customer already provided
- Relevant IDs or selections
- Authentication or eligibility status
- Failed automation details

This reduces repeat questions and helps the agent continue the conversation with
more context.

Example transfer summary:

```
The customer wants to update their billing address but the request
requires agent verification. The customer provided their account email
and confirmed they are the account holder.
```

## Escalation design pattern

Use this pattern when designing escalation from agentic CX designer to Connect Customer:

1. In agentic CX designer, collect or generate the context you want to preserve.
2. Store important values as context variables, slots, Define outputs, or Generative text outputs.
3. Add an Escalate node.
4. Add a user-facing escalation message.
5. Add a Node payload using key={variable} syntax.
6. Build and deploy the application.
7. In a flow of Connect Customer, connect the Agentic CX block's Escalation path to **Set contact attributes**.
8. Store returned values from the Agentic CX namespace.
9. Route the contact with **Set working queue** and **Transfer to queue**.

## Troubleshooting escalations

| Issue                                                | Cause                                                                                | Fix                                                                                                               |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Escalation does not leave agentic CX designer        | The flow did not reach an Escalate node or the deployed build is outdated.           | Confirm the Escalate node is connected, then create and deploy a new build.                                       |
| Returned context is missing in Connect Customer flow | Node payload was not configured or used the wrong format.                            | Use key={variable} format in the Escalate node's Node payload.                                                    |
| Returned value is empty                              | The referenced variable was not in scope at the Escalate node.                       | Store the value as a context variable, Define output, Generative text output, or captured slot before escalation. |
| Agent receives no summary                            | The Set contact attributes block was not added after the Agentic CX escalation path. | Add Set contact attributes before Set working queue or Transfer to queue.                                         |
| Wrong queue is selected                              | Queue routing logic does not use the returned context.                               | Use returned attributes to determine the correct queue before transfer.                                           |
| Recent escalation changes are not active             | The application was edited but not redeployed.                                       | Create a new build and deploy it to the environment used by the Connect Customer flow.                            |
