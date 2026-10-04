

# Observe block
<a name="testing-simulation-observe-block"></a>

The Observe block is a fundamental component of the testing framework that defines what system events you want to monitor during test execution. Think of it as setting up checkpoints in your test where you wait for specific things to happen before taking action.

When you have an Observe block configured in your test, you're telling the system: "Watch for this particular event, and when it occurs, execute these specific actions." This event-driven approach mirrors how real-world interactions happen in contact centers: something occurs, and then you respond to it.

## Understanding active observations
<a name="testing-simulation-observe-active-observations"></a>

An Observe block becomes an active observation when it is actively watching for its specified event during simulation. Understanding how observations transition between active and inactive states is crucial for predicting test behavior.

**When observations become active:**
+ All starting interaction groups that are not connected from another interaction group or marked with a "start" banner are marked as active when test execution begins.
+ When an event is matched, any Check blocks and Actions blocks in the same interaction group will execute. On successful execution, any connected interaction group's observation is marked as active.
+ Multiple observations can be active simultaneously when you have multiple starting interaction groups in your test.

**When observations become inactive:**
+ An observation becomes inactive when its expected event is successfully matched.

**Impact on test results:**

If an active observation's expected event does not occur, the observation will continue watching for the event until the test times out after 5 minutes. This timeout indicates that the validation failed, causing your test to fail. When an observation fails due to timeout:
+ The observation remains active but unfulfilled.
+ Any Check blocks and Action blocks attached to that Observe block in the interaction group will not execute because the observed event was not fulfilled.
+ The test execution terminates with a failure status.

When an observation succeeds, which means the event is matched, the observation is marked as inactive, and any Check blocks or Action blocks in the same interaction group will execute before moving to the next connected interaction group.

![Observations transition between active and inactive states during test execution.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-active-observations.png)


## What events can you observe?
<a name="testing-simulation-observe-events"></a>

The Observe block can monitor several types of system events:

### Test started event
<a name="testing-simulation-observe-test-initiated"></a>

This event triggers at the very beginning of your test execution. It's particularly useful when you need to set up initial conditions before any customer interactions begin. For example, you might want to configure system behaviors or mock external dependencies right when the test starts.

Configuration options:
+ **Event Type** – Select "Test started" from the dropdown

Example Actions: Define what should happen when the test begins (such as overriding system behaviors).

![Observe block configuration showing Test started event type selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-test-initiated.png)


### Test completed event
<a name="testing-simulation-observe-test-completed"></a>

This event is observed when your test execution reaches its end. Use this to capture final state information actions after all test interactions are complete.

Configuration options:
+ **Event Type** – Select "Test Completed" from the dropdown

Example Actions: Specify any final validation or logging actions to perform.

![Observe block configuration showing Test Completed event type selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-test-completed.png)


### Message received event
<a name="testing-simulation-observe-message-received"></a>

This event detects when the system plays a prompt or sends any voice response to the simulated customer.

The Message Received event offers flexible matching options to identify the right message:

Configuration options:
+ **Event Type** – Select "Message Received" from the dropdown
+ **Message Content** – Specify what message to look for using one of these methods:
  + **Text** – Type the expected text content of the message
  + **SSML** – Provide SSML-formatted content to match
+ **Matching Criteria** – Choose how to match the message:
  + **Similar** – Uses intelligent semantic matching to find messages with similar meaning (recommended for most cases)
  + **Contains** – Checks if the observed message contains your specified text

**Important**  
(Voice) Test results might vary slightly between runs. The system breaks down audio into segments based on pauses and natural speech patterns, which can differ depending on how long someone pauses or how they structure their sentences. This means you might see variations in how prompts appear across test executions.

![Observe block configuration showing Message Received event type with matching criteria options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-message-received.png)


### Flow action started event
<a name="testing-simulation-observe-flow-action-started"></a>

This event observes when specific actions within your contact flow begin execution. With this event, you can detect and respond to operations happening in your flow, such as Lambda function calls, hours of operation checks, queue transfers, or bot initialization.

Configuration options:
+ **Event Type** – Select "Action Triggered" from the dropdown
+ **Resource Type** – Choose which flow action to observe:
  + **Lambda Function** – Detects when a Lambda function is called (select from the dropdown or specify the function ARN)
  + **Hours of Operation** – Monitors hours of operation checks (select from the dropdown or specify the hours of operation ARN)
  + **Queue** – Observes queue transfer actions (select from the dropdown or specify queue ARN)
  + **Lex Bot** – Detects Lex bot connections (select from the dropdown or specify the bot ARN and alias)

![Observe block configuration showing Action Triggered event type with resource type options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-flow-action-started.png)


### Flow Action Completed Event
<a name="testing-simulation-observe-flow-action-completed"></a>

This event observes when a specific action in your flow is completed successfully. Where the Flow Action Started event tells you when an action begins, the Flow Action Completed event tells you when it has completed successfully. More importantly, it makes the data that action produced available for you to validate and log in your test.

Think of it as the moment a Lambda function returns its response, a Lex bot resolves an intent, or an Agentic CX (customer experience) interaction completes successfully. At that point the action's results (such as an order status returned by a Lambda, the intent and slots resolved by a Lex bot, or the context variables produced by an Agentic CX interaction) become available to assert in Check blocks and Log data actions further along in your test.

When you would use this event:

Observe a completed action whenever you want to validate the output of that action, not just that it ran. For example, confirm or log that a Lambda returned `orderStatus = "Shipped"`, that a Lex bot resolved the `CheckOrderStatus` intent with the expected slot values, or that an Agentic CX interaction set the expected context variable.

Configuration options:
+ **Event Type** – Choose "Action completed" from the dropdown.
+ **Resource Type** – Choose the completed flow action to observe:
  + **Lambda Function** – Detects when a Lambda function invocation completes successfully (select from the dropdown or specify the function ARN).
  + **Lex Bot** – Detects when a Lex bot interaction completes successfully (select from the dropdown or specify the bot ARN and alias).
  + **Agentic CX** – Detects when an Agentic CX interaction completes successfully (select the Agentic CX workspace, application, and alias from the dropdown).

**Important**  
The results of an action only become available for reference after a Flow Action Completed observation for that action matches during test execution. If you reference `$.LambdaInvocation.ResultData.*`, `$.Lex.*`, or `$.AgenticCX.*` values without first observing the corresponding action's completion, those references resolve to an empty value and your assertion will fail. Always place a Flow Action Completed observation for an action before any Check or Log data step that references that action's results.

![Observe block configured for the Action completed event and Agentic CX resource type.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-flow-action-completed-agentic-cx.png)


#### What Data Becomes Available After an Action Completes?
<a name="testing-simulation-observe-flow-action-completed-data"></a>

When a Flow Action Completed observation matches, the results of that action are captured and made available under a dedicated namespace that you can reference by JSONPath, the same way you reference attributes in your flows:
+ **Lambda results** – reference under `$.External.<key>` (for example, `$.External.orderStatus`). You can also use the flow-language path `$.LambdaInvocation.ResultData.<key>`, which resolves to the same data.
+ **Lex results** – reference under `$.Lex.<path>` (for example, `$.Lex.IntentName`, `$.Lex.Slots.OrderNumber`, or `$.Lex.IntentConfidence.Score`).
+ **Agentic CX results** – reference under `$.AgenticCX.ContextVariables.<key>` for context variables the interaction produced, and `$.AgenticCX.metadata.<key>` for interaction metadata.

Once your observations of these actions match successfully, these references resolve to exactly the same values they would during a real contact. This ensures that the assertions you write in a test match the behavior your customers experience.

**Note**  
Only single values can be referenced. A reference that points to an entire object or list, rather than a specific value inside it, resolves to an empty value. For example, reference `$.Lex.Slots.OrderNumber` (a value), not `$.Lex.Slots` (an object). When the same action type completes successfully more than once, references resolve to the most recently captured results.

#### How Do You Reference an Action's Results?
<a name="testing-simulation-observe-flow-action-completed-reference-results"></a>

Example configuration to validate the order status returned by a Lambda function.

1. Add an **Observe** block and select the **Flow Action Completed** event, with **Resource Type** set as **Lambda function** and **Target resource** set to your Lambda function.

1. Add a **Check** block to the same interaction group: **Namespace** = **External**, **Key** = `orderStatus`, **Condition** = **Equals**, **Value** = `Shipped`.

1. Add a **Log data** action: **Log identifier** = `"Order status"`, **Log value** = `$.External.orderStatus`.

What happens: When the Lambda completes successfully during the simulated contact, the observation matches and captures the Lambda's results. The Check block then confirms `orderStatus` equals `Shipped`, and the Log data action records the value in your test results for later review. Lex and Agentic CX interactions follow the same pattern using their respective namespaces.

![Interaction group showing a Flow action completed Observe block connected to a Check block and a Log data action.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-flow-action-completed-lambda-workflow.png)


![Observe block configured for the Action completed event, Lambda function resource type, and getCustomerInfo target resource.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-flow-action-completed-lambda.png)


![Check block configured to validate that the External orderStatus attribute equals Shipped.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-check-flow-action-completed-lambda.png)


![Log data action configured to record Order status using the $.External.orderStatus JSONPath expression.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-log-data-flow-action-completed-lambda.png)


#### What Happens When an Action Takes the Error Branch?
<a name="testing-simulation-observe-flow-action-completed-error-branch"></a>

A Flow Action Completed observation matches only when the action completes successfully, meaning it takes the success or another default branch in your flow (not the error branch). "Completed" here means the action finished and succeeded.

If the action takes the error branch, it is not treated as completed. The observation does not match, so it keeps waiting for a successful completion that does not arrive. It times out after 5 minutes, causing the test to fail. Any Check or Log data steps attached to that observation do not run, because the completion event was never matched.

**Note**  
This applies equally to Lambda, Lex, and Agentic CX actions.

## How often should the event occur?
<a name="testing-simulation-observe-event-frequency"></a>

Each Observe block inherits a default usage setting from the interaction group that controls how many times the event should be matched during test execution. The default is that the event must occur exactly once. Changing this setting is not supported.

## Connecting interaction groups
<a name="testing-simulation-observe-connecting-groups"></a>

After defining what to observe, add a connector to the interaction group. In the interaction group menu (⋮), choose **Add connector**, then drag the connector to the start of the interaction group that contains the next observation. This creates a logical flow through your test, moving from one checkpoint to another as events occur.

![Interaction groups connected with connectors showing the logical flow between observe checkpoints.](https://docs.aws.amazon.com/connect/latest/adminguide/images/test-observe-connecting-groups.png)
