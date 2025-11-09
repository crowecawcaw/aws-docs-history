# Learn about state machines in Step Functions

Step Functions is based on _state machines_, which are also called
_workflows_. Workflows are comprised of a series of event-driven steps.

You define a workflow using Amazon States Language, also known as ASL. You can optionally use Workflow Studio, a
visual workflow designer, to build and edit your workflows.

Each step in a workflow is called a _state_. There are two types of
states: Flow states and Task states:

**Flow states**

Flow states control the flow of execution of the steps. For example,
**Choice states** provide conditional logic;
**Wait states** pause workflow execution; **Map states** run child workflows for each item in a
dataset; and **Parallel states** create separate
branches in your workflows.

**Task states**

Task states represent a unit of work that another AWS service performs, such
as calling another AWS service or API. Tasks states are also known as
**Actions**. You can choose hundreds of actions to
perform work in AWS and external services. (Note: You can also use workers
that run outside of Step Functions to perform tasks. For more info, see [Activities](concepts-activities.md "concepts-activities.md").)

![Illustrative example of the components of a Step Functions workflow.](images/state-machine-conceptual-jsonata.png)
**Executions and handling errors**

When you run your workflows, Step Functions creates a workflow instance called an _execution_. You can monitor the status of your workflow executions.
If an execution experiences an error, the workflow might catch the error. Depending on your
use case, you might redrive the execution later to resume the workflow.

**Passing data**

You can optionally provide **input data** in the form of JSON
text to your workflows. Each **step** can pass data to
subsequent steps using variables and state output. Data stored in variables can be used by
later steps. State output becomes the input for the very next step. To learn more about
passing data, see [Passing data between states with variables](workflow-variables.md "workflow-variables.md").

At the end of workflows, your state machine can optionally produce output, also in the
form of JSON.

**Transforming data**

States and state machines can transform data using a **query
language**. The recommended query language is **JSONata**; however, state machines created prior to re:Invent 2024 use **JSONPath**. For backward compatibility, your state machines or
individual states must opt-in to using JSONata for their query language.

You can recognize JSONata state machines and individual states by the
`QueryLanguage` field set to "JSONata". State machines and states that use
JSONPath, lack the `QueryLanguage` field.

States that use JSONPath will have state fields such as InputPath, Parameters,
ResultSelector, ResultPath, and OutputPath. In JSONPath state machine definitions, you will
also see field names that end
in `.$` and values prefixed with `$.` and `$$.`, both of which
represent paths. In the paths, you might see various intrinsic functions, such as
`States.MathAdd`. Intrinsic functions are **only**
used in JSONPath.

JSONata states use **Arguments** and **Output** fields. In these optional fields, you might see JSONata expressions that
look like the following: `"{% $type = 'local' %}"`. With JSONata, you can use
expressions, operators, and functions. To learn more, see [Transforming data with JSONata in Step Functions](transforming-data.md "transforming-data.md").

###### Note

You can use only one query language per state. You cannot mix JSONPath and JSONata
within a single step.

## Key concepts

The following provides an overview of the key Step Functions terms for context.

| Term                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workflow                       | A sequence of steps that often reflect a business process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| States                         | Individual steps in your state machine that can make decisions based on their input, perform actions from those inputs, and pass output to other states.<br>For more information, see [Discovering workflow states to use in Step Functions](workflow-states.md "workflow-states.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Workflow Studio                | A visual workflow designer that helps you to prototype and build workflows faster.<br>For more information, see [Developing workflows in Step Functions Workflow Studio](workflow-studio.md "workflow-studio.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| State machine                  | A workflow defined using JSON text representing the individual states or steps in the workflow along with fields, such as `StartAt`, `TimeoutSeconds`, and `Version`.<br>For more information, see [State machine structure in Amazon States Language for Step Functions workflows](statemachine-structure.md "statemachine-structure.md").                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Amazon States Language         | A JSON-based, structured language used to define your state machines. With ASL, you define a collection of [states](workflow-states.md "workflow-states.md") that can do work ([Task state](state-task.md "state-task.md")), determine<br>which states to transition to next ([Choice state](state-choice.md "state-choice.md")), and stop an execution with an error ([Fail state](state-fail.md "state-fail.md")).<br>For more information, see [Using Amazon States Language to define Step Functions workflows](concepts-amazon-states-language.md "concepts-amazon-states-language.md").                                                                                                                                                               |
| Input and output configuration | States in a workflow receive JSON data as input and usually pass JSON data as output to the next state. Step Functions provides filters to control the data flow between states.<br>For more information, see [Processing input and output in Step Functions](concepts-input-output-filtering.md "concepts-input-output-filtering.md").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Service integration            | You can call AWS service API actions from your workflow.<br>For more information, see [Integrating services with Step Functions](integrate-services.md "integrate-services.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Service integration type       | • [AWS SDK integrations](supported-services-awssdk.md "supported-services-awssdk.md") – Standard way to call any of over two hundred AWS services and over nine thousand API actions directly from your state machine.<br>• [Optimized integrations](integrate-optimized.md "integrate-optimized.md") – Custom integrations that streamline calling and exchanging data with certain services. For example, **Lambda Invoke** will automatically convert the `Payload` field of the response from an escaped JSON string into a JSON object.                                                                                                                                                                                                                |
| Service integration pattern    | When calling an AWS service, you use one of the following service integration patterns:<br>• [Request a response (default)](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") – Call a service and move to the next state immediately after receiving an HTTP<br>response.<br>• [Run a job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") – Call a service and have Step Functions wait for a job to complete.<br>• [Wait for a callback with a task token<br>(.waitForTaskToken)](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token") – Call a service with a task token and have Step Functions wait until the task token returns with a callback. |
| Execution                      | State machine executions are instances where you run your workflow to perform tasks.<br>For more information, see [Starting state machine executions in Step Functions](statemachine-starting.md "statemachine-starting.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## State Machine Data

State machine data takes the following forms:

- The initial input into a state machine
- Data passed between states
- The output from a state machine

This section describes how state machine data is formatted and used in AWS Step Functions.

###### Topics

- [Data Format](#concepts-state-machine-data-format "#concepts-state-machine-data-format")
- [State Machine
  Input/Output](#concepts-state-machine-data-state-machine-input-output "#concepts-state-machine-data-state-machine-input-output")
- [State
  Input/Output](#concepts-state-machine-data-state-input-output "#concepts-state-machine-data-state-input-output")

### Data Format

State machine data is represented by JSON text.
You
can provide values
to a state machine
using any data type supported by JSON.

###### Note

- Numbers in JSON text format conform to JavaScript semantics. These numbers
  typically correspond to double-precision [IEEE-854](https://standards.ieee.org/findstds/standard/854-1987.html "https://standards.ieee.org/findstds/standard/854-1987.html") values.
- The following is valid JSON text:
  - Standalone, quote-delimited strings
  - Objects
  - Arrays
  - Numbers
  - Boolean values
  - `null`

- The output of a state becomes the input
  for
  the next state. However, you can restrict states to
  work
  on a subset of the input data by using [Input and Output
  Processing](concepts-input-output-filtering.md "concepts-input-output-filtering.md").

### State Machine

Input/Output

You
can give your initial input data to an AWS Step Functions state machine in one of two ways. You
can pass the data to a
`StartExecution` action when you start an execution. You can also
pass the data to the state machine from the [Step Functions
console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/"). Initial data is passed to the state machine's
`StartAt` state. If no input is provided, the default is an empty object
(`{}`).

The output of the execution is returned by the last state (`terminal`).
This output appears as JSON text in the execution's result.

For Standard Workflows, you can retrieve execution results from the execution history
using external callers,
such
as the `DescribeExecution`
action. You
can view execution results on the [Step Functions
console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/").

For Express Workflows, if you
enabled
logging, you can retrieve results from
CloudWatch Logs,
or view and debug the executions in the Step Functions console. For more information, see [Using CloudWatch Logs to log execution history in Step Functions](cw-logs.md "cw-logs.md") and [Viewing execution details in the Step Functions console](concepts-view-execution-details.md "concepts-view-execution-details.md").

You should also consider quotas related to your state machine. For more information, see
[Step Functions service quotas](service-quotas.md "service-quotas.md")

### State

Input/Output

Each state's input consists of JSON text from the preceding state or, for the
`StartAt` state, the input into the execution. Certain flow-control
states echo their input to their output.

In the following example, the state machine adds two numbers together.

1. Define the AWS Lambda function.

```
function Add(input) {
  var numbers = JSON.parse(input).numbers;
  var total = numbers.reduce(
    function(previousValue, currentValue, index, array) {
      return previousValue + currentValue; });
  return JSON.stringify({ result: total });
}
```

2. Define the state machine.

```
{
  "Comment": "An example that adds two numbers together.",
  "StartAt": "Add",
  "Version": "1.0",
  "TimeoutSeconds": 10,
  "States":
    {
        "Add": {
          "Type": "Task",
          "Resource": "arn:aws:lambda:`region`:123456789012:function:Add",
          "End": true
        }
    }
}
```

3. Start an execution with the following JSON text.

```
{ "numbers": [3, 4] }
```

The `Add` state receives the JSON text and passes it to the Lambda
function.

The Lambda function returns the result of the calculation to the state.

The state returns the following value in its output.

```
{ "result": 7 }
```

Because `Add` is also the final state in the state machine, this
value is returned as the state machine's output.

If the final state returns no output, then the state machine returns an empty
object (`{}`).

For more information, see [Processing input and output in Step Functions](concepts-input-output-filtering.md "concepts-input-output-filtering.md").

## Invoke AWS Step Functions from other services

You can configure several other services to invoke state machines. Based on the state machine's [workflow type](choosing-workflow-type.md "choosing-workflow-type.md"),
you can invoke state machines asynchronously or synchronously. To invoke state machines synchronously, use the
`StartSyncExecution` API call or Amazon API Gateway
integration with Express Workflows. With asynchronous invocation, Step Functions pauses the workflow execution until a task token is returned. However, waiting for a task token does make the workflow synchronous.

Services that you can configure to invoke Step Functions include:

- AWS Lambda, using the [`StartExecution`](../apireference/API_StartExecution.md "../apireference/API_StartExecution.md") call.
- [Amazon API Gateway](tutorial-api-gateway.md "tutorial-api-gateway.md")
- [Amazon EventBridge](../../../eventbridge/latest/userguide/create-eventbridge-rule.md "../../../eventbridge/latest/userguide/create-eventbridge-rule.md")
- [AWS CodePipeline](../../../codepipeline/latest/userguide/action-reference-StepFunctions.md "../../../codepipeline/latest/userguide/action-reference-StepFunctions.md")
- [AWS IoT Rules Engine](../../../iot/latest/developerguide/iot-rule-actions.md "../../../iot/latest/developerguide/iot-rule-actions.md")
- [AWS Step Functions](connect-stepfunctions.md "connect-stepfunctions.md")

Step Functions invocations are governed by the `StartExecution` quota. For more information, see:

- [Step Functions service quotas](service-quotas.md "service-quotas.md")

## Transitions in state machines

When you start a new execution of your state machine, the system begins with the state
referenced in the top-level `StartAt` field. This field, given as a string, must
exactly match, including case, the name of a state in the workflow.

After a state runs, AWS Step Functions uses the value of the `Next` field to determine
the next state to advance to.

`Next` fields also specify state names as strings. This string is case-sensitive
and must match the name of a state specified in the state machine description exactly

For example, the following state includes a transition to `NextState`.

```
"SomeState" : {
  ...,
  "Next" : "NextState"
}
```

Most states permit only a single transition rule with the `Next` field. However,
certain flow-control states, such as a `Choice` state, allow you to specify
multiple transition rules, each with its own `Next` field. The [Amazon States Language](concepts-amazon-states-language.md "concepts-amazon-states-language.md") provides details
about each of the state types you can specify, including information about how to specify
transitions.

States can have multiple incoming transitions from other states.

The process repeats until it either reaches a terminal state (a state with `"Type":
 Succeed`, `"Type": Fail`, or `"End": true`), or a runtime
error occurs.

When you [redrive](redrive-executions.md "redrive-executions.md") an execution, it's considered as a state transition. In addition, all states that are rerun in a redrive are also considered as state transitions.

The following rules apply to states within a state machine:

- States can occur in any order within the enclosing block. However, the order
  in which they're listed doesn't affect the order in which they're run. That order is
  determined by the contents of the states.
- Within a state machine, there can be only one state designated as the
  `start` state. The `start` state is defined by the value
  of the `StartAt` field in the top-level structure.
- Depending on your state machine logic — for example, if your state
  machine has multiple logic branches — you may have more than one
  `end` state.
- If your state machine consists of only one state, it can be both the
  start and end state.

### Transitions in Distributed Map state

When you use the `Map` state in Distributed mode, you'll be charged one state transition for each child workflow execution that the _Distributed Map state_ starts. When you use the `Map` state in Inline mode, you aren't charged a state transition for each iteration of the _Inline Map state_.

You can optimize cost by using the `Map` state in Distributed mode and
include a nested workflow in the `Map` state definition. The _Distributed Map state_ also
adds more value when you start child workflow executions of type **Express**.
Step Functions stores the response and status of the Express child workflow executions, which
reduces the need to store execution data in CloudWatch Logs. You can also get access to flow
controls available with a _Distributed Map state_, such as defining error thresholds or batching a
group of items. For information about Step Functions pricing, see [AWS Step Functions pricing](https://aws.amazon.com/step-functions/pricing/ "https://aws.amazon.com/step-functions/pricing/").

## Read Consistency in Step Functions

State machine updates in AWS Step Functions are eventually consistent. All
`StartExecution` calls within a few seconds will use the updated definition
and `roleArn` (the Amazon Resource Name for the IAM role). Executions started immediately after calling
`UpdateStateMachine` might use the previous state machine definition and
`roleArn`.

For more information, see the following:

- [`UpdateStateMachine`](../apireference/API_UpdateStateMachine.md "../apireference/API_UpdateStateMachine.md") in the
  _AWS Step Functions API Reference_
