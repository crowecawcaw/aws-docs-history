# AWS Flow Framework Basic Concepts: Reliable Execution

Asynchronous distributed applications must deal with reliability issues that are not encountered by
conventional applications, including:

- How to _provide reliable communication_ between asynchronous distributed components,
  such as long-running components on remote systems.
- How to _ensure that results are not lost_ if a component fails or is disconnected,
  especially for long-running applications.
- How to _handle failed distributed components_.
  Applications can rely on the AWS Flow Framework and Amazon SWF to manage these issues. We'll explore how Amazon SWF provides
  mechanisms to ensure that your workflows operate reliably and in a predictable way, even when they are long-running
  and depend on asynchronous tasks carried out computationally and with human interaction.

## Providing Reliable Communication

AWS Flow Framework provides reliable communication between a workflow worker and its activities workers by using
Amazon SWF to dispatch tasks to distributed activities workers and return the results to the workflow worker. Amazon SWF
uses the following methods to ensure reliable communication between a worker and its activities:

- Amazon SWF durably stores scheduled activity and workflow tasks and guarantees that they will be performed at
  most once.
- Amazon SWF guarantees that an activity task will either complete successfully and return a valid result or it
  will notify the workflow worker that the task failed.
- Amazon SWF durably stores each completed activity's result or, for failed activities, it stores relevant
  error information.

The AWS Flow Framework then uses the activity results from Amazon SWF to determine how to proceed with the
workflow's execution.

## Ensuring that Results are Not Lost

### Maintaining Workflow History

An activity that performs a data-mining operation on a petabyte of data might take
_hours_ to complete, and an activity that directs a human worker to perform a complex task
might take _days_, or even _weeks_ to complete!

To accommodate scenarios such as these, AWS Flow Framework workflows and activities can take arbitrarily long to
complete: _up to a limit of one year_ for a workflow execution. Reliably executing long
running processes requires a mechanism to durably store the workflow's execution history on an ongoing
basis.

The AWS Flow Framework handles this by depending on Amazon SWF, which maintains a running history of each workflow
instance. The workflow's history provides a complete and authoritative record of the workflow's progress,
including all the workflow and activity tasks that have been scheduled and completed, and the information returned
by completed or failed activities.

AWS Flow Framework applications usually don't need to interact with the workflow history directly, although they
can access it if necessary. For most purposes, applications can simply let the framework interact with the
workflow history behind the scenes. For a full discussion of workflow history, see [Workflow History](../developerguide/swf-dg-basic.md#swf-dev-about-workflow-history "../developerguide/swf-dg-basic.md#swf-dev-about-workflow-history") in the _Amazon Simple Workflow Service Developer Guide_.

### Stateless Execution

The execution history allows workflow workers to be _stateless_. If you have multiple
instances of a workflow or activity worker, any worker can perform any task. The worker receives all the state
information that it needs to perform the task from Amazon SWF.

This approach makes workflows more reliable. For example, if an activity worker fails, you don't have to
restart the workflow. Just restart the worker and it will start polling the task list and processing whatever
tasks are on the list, regardless of when the failure occurred. You can make your overall workflow fault-tolerant
by using two or more workflow and activity workers, perhaps on separate systems. Then, if one of the workers
fails, the others will continue to handle scheduled tasks without any interruption in workflow progress.

## Handling Failed Distributed Components

Activities often fail for ephemeral reasons, such as a brief disconnection, so a common strategy for
handling failed activities is to retry the activity. Instead of handling the retry process by implementing complex
message passing strategies, applications can depend on the AWS Flow Framework. It provides several mechanisms for retrying
failed activities, and provides a built-in exception-handling mechanism that works with asynchronous, distributed
execution of tasks in a workflow.
