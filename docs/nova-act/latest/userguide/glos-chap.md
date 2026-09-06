

# Nova Act glossary
<a name="glos-chap"></a>

 [A](#a) \| [B](#b) \| [C](#c) \| [H](#h) \| [I](#i) \| [M](#m) \| [O](#o) \| [S](#s) \| [T](#t) \| [U](#u) \| [W](#w) 

## A
<a name="_a"></a>

act  
  

An `act()` call that creates a new AI task within a session that can interact with tools and perform specific actions. Each act() executes the agentic loop within a session context. For example: `nova.act("search for 'rubber duck debugging'")`. For more information, see [CreateAct](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateAct.html) in the *Amazon Nova Act API Reference*.

agent trajectory data  
  

The data that Nova Act temporarily stores to maintain historical context while executing a workflow, including the input prompt, screenshots, and agent response. You can opt into persisting agent trajectory data indefinitely by configuring the service to write this data to an Amazon S3 bucket that you own and control. For more information, see [WorkflowExportConfig](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowExportConfig.html) in the *Amazon Nova Act API Reference*. To learn about the required S3 permissions, see [Configure access to an Amazon S3 bucket for data export](security-iam-s3-export-permissions.md).

agentic loop  
  

The iterative cycle where the Nova Act model observes the current state, reasons about the next action, executes that action, and evaluates progress toward task completion. This loop continues until the task is complete or requires escalation.

## B
<a name="_b"></a>

browser actuator  
  

The component that translates Nova Act model instructions into concrete browser actions using Playwright, enabling actual interaction with web pages including clicking, typing, scrolling, and navigation.

Builder Mode  
  

A development environment within the Nova Act IDE extension that brings the entire agent development experience directly into IDEs such as Visual Studio Code, Cursor, and Kiro. Builder Mode provides live browser preview, step-by-step execution control, and detailed visibility into the agent’s decision-making process during workflow development. For more information, see [Step 2: Develop locally](https://docs.aws.amazon.com/nova-act/latest/userguide/step-2-develop-locally.html).

## C
<a name="_c"></a>

call  
  

A request for the client to execute a specific tool with given parameters. Each call has a unique identifier used to match results back to requests. For more information, see [Call](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Call.html) in the *Amazon Nova Act API Reference*.

call result  
  

The result returned from executing a tool call, including the content returned by the tool execution which can include text or other media types. For more information, see [CallResult](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CallResult.html) in the *Amazon Nova Act API Reference*.

compatibility version  
  

The client compatibility version used to ensure API compatibility when Nova Act model updates are released, allowing workflows to filter models by compatibility and continue using previous model behavior until explicitly updated. For more information, see [CompatibilityInformation](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CompatibilityInformation.html) in the *Amazon Nova Act API Reference*.

## H
<a name="_h"></a>

human approval  
  

Human approval enables asynchronous human decision-making in automated processes. When Nova Act encounters a decision point requiring human judgment, it captures a screenshot of the current state and presents it to a human reviewer via a browser-based interface. Use this when you need binary or multi-choice decisions (Approve/Reject, Yes/No, or selecting from predefined options). For more information, see [Human-in-the-loop (HITL)](hitl.md).

## I
<a name="_i"></a>

invocation loop  
  

The execution cycle for calling external tools or APIs within a workflow, including parameter preparation, invocation, response handling, and error management. See also observation loop.

## M
<a name="_m"></a>

model lifecycle status  
  

The current support and availability state of a Nova Act model version. For more information, see [ModelLifecycle](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelLifecycle.html) in the *Amazon Nova Act API Reference*. The possible statuses are:
+ ACTIVE — The model version is currently recommended for production use and receives full support and updates.
+ DEPRECATED — The model version is no longer recommended for new workflows but remains available for existing workflows during a migration period.
+ LEGACY — The model version is maintained only for backward compatibility with existing workflows and will not receive new features or non-critical updates.

## O
<a name="_o"></a>

observation loop  
  

The cycle where Nova Act captures and processes the current state of the browser or environment, including screenshot analysis, and context extraction, before determining the next action. Works in conjunction with the invocation loop.

orchestrator  
  

The central component that manages workflow execution, coordinates between different Nova Act components (model, browser actuator, tools), handles state management, and ensures proper sequencing of operations.

## S
<a name="_s"></a>

session  
  

A session context within a workflow run that manages conversation state and acts. A session contains one or more act() calls that run sequentially. Multiple sessions can run in parallel within a workflow run. For more information, see [CreateSession](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateSession.html) in the *Amazon Nova Act API Reference*.

state guardrails  
  

Callback functions that inspect the browser state after each observation and decide whether to allow or block continued execution. State guardrails allow you to control which URLs the agent can visit during execution, preventing navigation to unauthorized domains or sensitive pages. If blocked, `act()` raises `ActStateGuardrailError`. For more information, see [SDK security](sdk-security.md).

step  
  

One cycle of the act processing tool call results and returning new tool calls if needed. Each act() call consists of multiple steps that run sequentially. For more information, see [InvokeActStep](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InvokeActStep.html) in the *Amazon Nova Act API Reference*.

## T
<a name="_t"></a>

tool spec  
  

A specification for a tool that acts can invoke, including the tool’s name, description, and input schema that defines the expected input format. For more information, see [ToolSpec](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ToolSpec.html) in the *Amazon Nova Act API Reference*.

trace location  
  

Information about where trace data is stored for debugging and monitoring, including the storage location type and the specific location of the trace data. For more information, see [TraceLocation](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_TraceLocation.html) in the *Amazon Nova Act API Reference*.

## U
<a name="_u"></a>

UI takeover  
  

UI takeover enables real-time human control of a remote browser session. When Nova Act encounters a task that requires human interaction, it hands control of the browser to a human operator via a live-streaming interface. The operator can interact with the browser using mouse and keyboard in real-time. For more information, see [Human-in-the-loop (HITL)](hitl.md).

## W
<a name="_w"></a>

workflow  
  

A workflow definition template that can be used to execute multiple workflow runs. Workflows define your agent’s end-to-end task by combining act() statements with Python code that orchestrate the automation logic. For more information, see [CreateWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowDefinition.html) in the *Amazon Nova Act API Reference*.

workflow run  
  

An execution instance of a workflow definition with specified parameters. A workflow can be run multiple times with different inputs, producing different results for each run. For more information, see [CreateWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowRun.html) in the *Amazon Nova Act API Reference*.