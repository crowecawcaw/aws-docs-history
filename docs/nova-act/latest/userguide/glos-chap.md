# Nova Act glossary

[A](#a "#a") | [B](#b "#b") | [C](#c "#c") | [H](#h "#h") | [I](#i "#i") | [M](#m "#m") | [O](#o "#o") | [S](#s "#s") | [T](#t "#t") | [U](#u "#u") | [W](#w "#w")

## A

act

An `act()` call that creates a new AI task within a session that can interact with tools and perform specific actions. Each act() executes the agentic loop within a session context. For example: `nova.act("search for 'rubber duck debugging'")`. For more information, see [CreateAct](../APIReference/API_CreateAct.md "../APIReference/API_CreateAct.md") in the _Amazon Nova Act API Reference_.

agent trajectory data

The data that Nova Act temporarily stores to maintain historical context while executing a workflow, including the input prompt, screenshots, and agent response. You can opt into persisting agent trajectory data indefinitely by configuring the service to write this data to an Amazon S3 bucket that you own and control. For more information, see [WorkflowExportConfig](../APIReference/API_WorkflowExportConfig.md "../APIReference/API_WorkflowExportConfig.md") in the _Amazon Nova Act API Reference_. To learn about the required S3 permissions, see [Configure access to an Amazon S3 bucket for data export](security-iam-s3-export-permissions.md "security-iam-s3-export-permissions.md").

agentic loop

The iterative cycle where the Nova Act model observes the current state, reasons about the next action, executes that action, and evaluates progress toward task completion. This loop continues until the task is complete or requires escalation.

## B

browser actuator

The component that translates Nova Act model instructions into concrete browser actions using Playwright, enabling actual interaction with web pages including clicking, typing, scrolling, and navigation.

Builder Mode

A development environment within the Nova Act IDE extension that brings the entire agent development experience directly into IDEs such as Visual Studio Code, Cursor, and Kiro. Builder Mode provides live browser preview, step-by-step execution control, and detailed visibility into the agent’s decision-making process during workflow development. For more information, see [Step 2: Develop locally](step-2-develop-locally.md "step-2-develop-locally.md").

## C

call

A request for the client to execute a specific tool with given parameters. Each call has a unique identifier used to match results back to requests. For more information, see [Call](../APIReference/API_Call.md "../APIReference/API_Call.md") in the _Amazon Nova Act API Reference_.

call result

The result returned from executing a tool call, including the content returned by the tool execution which can include text or other media types. For more information, see [CallResult](../APIReference/API_CallResult.md "../APIReference/API_CallResult.md") in the _Amazon Nova Act API Reference_.

compatibility version

The client compatibility version used to ensure API compatibility when Nova Act model updates are released, allowing workflows to filter models by compatibility and continue using previous model behavior until explicitly updated. For more information, see [CompatibilityInformation](../APIReference/API_CompatibilityInformation.md "../APIReference/API_CompatibilityInformation.md") in the _Amazon Nova Act API Reference_.

## H

human approval

Human approval enables asynchronous human decision-making in automated processes. When Nova Act encounters a decision point requiring human judgment, it captures a screenshot of the current state and presents it to a human reviewer via a browser-based interface. Use this when you need binary or multi-choice decisions (Approve/Reject, Yes/No, or selecting from predefined options). For more information, see [Human-in-the-loop (HITL)](hitl.md "hitl.md").

## I

invocation loop

The execution cycle for calling external tools or APIs within a workflow, including parameter preparation, invocation, response handling, and error management. See also observation loop.

## M

model lifecycle status

The current support and availability state of a Nova Act model
version. For more information, see [ModelLifecycle](../APIReference/API_ModelLifecycle.md "../APIReference/API_ModelLifecycle.md") in the _Amazon Nova Act API Reference_. The possible statuses are:

- ACTIVE — The model version is currently recommended for production use and receives full support and updates.
- DEPRECATED — The model version is no longer recommended for new workflows but remains available for existing workflows during a migration period.
- LEGACY — The model version is maintained only for backward compatibility with existing workflows and will not receive new features or non-critical updates.

## O

observation loop

The cycle where Nova Act captures and processes the current state of the browser or environment, including screenshot analysis, and context extraction, before determining the next action. Works in conjunction with the invocation loop.

orchestrator

The central component that manages workflow execution, coordinates between different Nova Act components (model, browser actuator, tools), handles state management, and ensures proper sequencing of operations.

## S

session

A session context within a workflow run that manages conversation state and acts. A session contains one or more act() calls that run sequentially. Multiple sessions can run in parallel within a workflow run. For more information, see [CreateSession](../APIReference/API_CreateSession.md "../APIReference/API_CreateSession.md") in the _Amazon Nova Act API Reference_.

state guardrails

Callback functions that inspect the browser state after each observation and decide whether to allow or block continued execution. State guardrails allow you to control which URLs the agent can visit during execution, preventing navigation to unauthorized domains or sensitive pages. If blocked, `act()` raises `ActStateGuardrailError`. For more information, see [SDK security](sdk-security.md "sdk-security.md").

step

One cycle of the act processing tool call results and returning new tool calls if needed. Each act() call consists of multiple steps that run sequentially. For more information, see [InvokeActStep](../APIReference/API_InvokeActStep.md "../APIReference/API_InvokeActStep.md") in the _Amazon Nova Act API Reference_.

## T

tool spec

A specification for a tool that acts can invoke, including the tool’s name, description, and input schema that defines the expected input format. For more information, see [ToolSpec](../APIReference/API_ToolSpec.md "../APIReference/API_ToolSpec.md") in the _Amazon Nova Act API Reference_.

trace location

Information about where trace data is stored for debugging and monitoring, including the storage location type and the specific location of the trace data. For more information, see [TraceLocation](../APIReference/API_TraceLocation.md "../APIReference/API_TraceLocation.md") in the _Amazon Nova Act API Reference_.

## U

UI takeover

UI takeover enables real-time human control of a remote browser session. When Nova Act encounters a task that requires human interaction, it hands control of the browser to a human operator via a live-streaming interface. The operator can interact with the browser using mouse and keyboard in real-time. For more information, see [Human-in-the-loop (HITL)](hitl.md "hitl.md").

## W

workflow

A workflow definition template that can be used to execute multiple workflow runs. Workflows define your agent’s end-to-end task by combining act() statements with Python code that orchestrate the automation logic. For more information, see [CreateWorkflowDefinition](../APIReference/API_CreateWorkflowDefinition.md "../APIReference/API_CreateWorkflowDefinition.md") in the _Amazon Nova Act API Reference_.

workflow run

An execution instance of a workflow definition with specified parameters. A workflow can be run multiple times with different inputs, producing different results for each run. For more information, see [CreateWorkflowRun](../APIReference/API_CreateWorkflowRun.md "../APIReference/API_CreateWorkflowRun.md") in the _Amazon Nova Act API Reference_.
