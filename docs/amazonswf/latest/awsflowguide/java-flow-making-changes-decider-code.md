# Making Changes to Decider Code: Versioning and Feature Flags

This section shows how to avoid backwards-incompatible changes to a decider using two
methods:

- [Versioning](java-flow-making-changes-solutions.md#use-versioning "java-flow-making-changes-solutions.md#use-versioning") provides a basic solution.
- [Versioning with Feature Flags](java-flow-making-changes-solutions.md#use-feature-flags "java-flow-making-changes-solutions.md#use-feature-flags") builds on the Versioning solution:
  No new version of the workflow is introduced, and there is no need to push new code to update the version.
  Before you try these solutions, familiarize yourself with the [Example Scenario](java-flow-making-changes-example-scenario.md "java-flow-making-changes-example-scenario.md") section which
  explains the causes and effects of backwards-incompatible decider changes.

## The Replay Process and Code Changes

When an AWS Flow Framework for Java decider worker executes a decision task, it first must rebuild
the current state of the execution before it can add steps to it. The decider does
this using a process called _replay_.

The replay process re-executes the decider code from the beginning, while
simultaneously going through the history of events that have already occurred. Going
through the event history allows the framework to react to signals or task
completion and unblock `Promise` objects in the code.

When the framework executes the decider code, it assigns an ID to each scheduled task
(an activity, Lambda function, timer, child workflow, or outgoing signal) by
incrementing a counter. The framework communicates this ID to Amazon SWF, and adds the ID
to history events, such as `ActivityTaskCompleted`.

For the replay process to succeed, it is important for the decider code to be
deterministic, and to schedule the same tasks in the same order for every decision
in every workflow execution. If you don't adhere to this requirement, the framework
might, for example, fail to match the ID in an `ActivityTaskCompleted`
event to an existing `Promise` object.
