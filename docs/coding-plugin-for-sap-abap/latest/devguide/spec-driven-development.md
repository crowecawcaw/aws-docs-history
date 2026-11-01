

# Spec-driven development with AWS Coding Plugin for SAP ABAP
<a name="spec-driven-development"></a>

Spec-driven development (SDD) makes a written specification, not the code, the primary artifact. A *spec* is a set of documents that state what to build. The plug-in generates the SAP ABAP from the spec, so the code is an output rather than the source of truth. SDD is a discipline, not a feature of any one tool, and AWS Coding Plugin for SAP ABAP ("Coding Plugin") brings it to Eclipse and SAP ABAP Development Tools (ADT).

## Why spec-driven development matters for SAP ABAP
<a name="spec-driven-development-why"></a>

SAP ABAP code is not disposable. It lives for decades, passing through many hands as teams, owners, and organizations change. A spec keeps a durable record of intent that outlives any one developer.
+ The spec-writing process mirrors how ABAP development is conducted, with an analysis of business requirements before designing and coding a solution.
+ The spec is a living document, readable by a future developer, human or agent.
+ Later changes start from stated intent, not from reverse-engineering the code.
+ The requirements defined in the spec are testable by Coding Plugin and become part of the self-correcting loop that ensures it produces accurate business logic.
+ The spec-writing process is the primary collaboration between human and agent. While writing the spec, both the human and agent learn and explore the business requirements, discover edge cases, and plan for an optimal result.

## The three spec documents
<a name="spec-driven-development-documents"></a>

Kiro records a spec as three documents. Each builds on the one before it.
+  `requirements.md` states what to build: the object type, inputs and outputs, business rules, error cases, which patterns to use or avoid, and the security requirements.
+  `design.md` states how to build it: the technical design and the tables, CDS views, APIs, and other objects it depends on. Coding Plugin queries the ABAP system to understand the available objects in the system during this stage.
+  `tasks.md` breaks the design into an ordered list of implementation tasks that the agent executes. The task list can branch into parallel tasks where ABAP objects can be modified by multiple subagents without conflict.

Specs are stored in the `.kiro/specs/<feature>/` directory of your project, so they can be committed to a durable Git repository for sharing with the team.

## Working with specs in Eclipse
<a name="spec-driven-development-eclipse"></a>

Coding Plugin supports the spec workflow in the UI. Certain keywords such as "spec" will automatically activate spec mode, or you can manually set a chat tab to spec mode in the mode drop-down. In spec mode, you will see spec action buttons at the top of the chat tab at certain points in the spec workflow.

These buttons appear according to which spec documents exist on disk.
+  **Generate Design** appears while the spec has requirements but no design.
+  **Generate Tasks** appears once a design exists.
+  **Run All Tasks** appears when the task list exists. It opens a new tab and reports one line for each task as the status changes (queued, in progress, completed, failed, or stopped).

When the agent needs a decision during the workflow, it pauses and renders the choices as clickable option cards. When a prompt looks like it should be a spec, the plug-in nudges you to start one.

As it executes tasks, the agent verifies its own work through the self-correcting loop (see [the self-correcting loop](abap-development.md#abap-development-self-correcting-loop)).

Coding Plugin estimates credit usage in developing each spec, which is useful to customers and service providers to evaluate a project’s credit consumption (see [Monitoring credit usage](using-chat.md#using-chat-credit-usage)). For what a credit is, see [Pricing](pricing.md).

## How specs are written
<a name="spec-driven-development-authoring"></a>

The spec-writing process is collaborative. You and Kiro define the requirements, design the solution, and develop a task list. During the design phase, Coding Plugin benefits from a live SAP connection so that it can discover the tables, APIs, and objects your system actually offers.