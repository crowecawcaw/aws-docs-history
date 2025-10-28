# AWS Flow Framework Basic Concepts: Distributed Execution

A _workflow instance_ is essentially a virtual thread of execution that can span activities
and orchestration logic running on multiple remote computers. Amazon SWF and the AWS Flow Framework function as an operating system
that manages workflow instances on a virtual CPU by:

- Maintaining each instance's execution state.
- Switching between instances.
- Resuming execution of an instance at the point that it was switched out.

## Replaying Workflows

Because activities can be long-running, it's undesirable to have the workflow simply block until it
completes. Instead, the AWS Flow Framework manages workflow execution by using a _replay_ mechanism,
which relies on the workflow history maintained by Amazon SWF to execute the workflow in episodes.

Each episode replays the workflow logic in a way that _executes each activity only once_,
and ensures that activities and asynchronous methods don't execute until their [Promise](awsflow-basics-data-exchange-activities-workflows.md "awsflow-basics-data-exchange-activities-workflows.md") objects are ready.

The workflow starter initiates the first replay episode when it starts the workflow execution. The framework
calls the workflow's entry point method and:

1. Executes all workflow tasks that don't depend on activity completion, including calling all activity
   client methods.
2. Gives Amazon SWF a list of activities tasks to be scheduled for execution. For the first episode, this list
   consists of only those activities that don't depend on a Promise and can be executed
   immediately.
3. Notifies Amazon SWF that the episode is complete.

Amazon SWF stores the activity tasks in the workflow history and schedules them for execution by placing them on
the activity task list. The activity workers poll the task list and execute the tasks.

When an activity worker completes a task, it returns the result to Amazon SWF, which records it in the workflow
execution history and schedules a new _workflow task_ for the workflow worker by placing it on
the workflow task list. The workflow worker polls the task list and when it receives the task, it runs the next
replay episode, as follows:

1. The framework runs the workflow's entry point method again and:
   - Executes all workflow tasks that don't depend on activity completion, including calling all
     activity client methods. However, the framework checks the execution history and doesn't schedule
     duplicate activity tasks.
   - Checks the history to see which activity tasks have completed and executes any asynchronous
     workflow methods that depend on those activities.

2. When all workflow tasks that can be executed have completed, the framework reports
   back to Amazon SWF:
   - It gives Amazon SWF a list of any activities whose input `Promise<T>` objects have
     become ready since the last episode and can be scheduled for execution.
   - If the episode generated no additional activity tasks but there are still uncompleted
     activities, the framework notifies Amazon SWF that the episode is complete. It then waits for another
     activity to complete, initiating the next replay episode.
   - If the episode generated no additional activity tasks and all activities have completed, the
     framework notifies Amazon SWF that the workflow execution is complete.

For examples of replay behavior, see [AWS Flow Framework for Java Replay Behavior](programming-replay.md "programming-replay.md").

## Replay and Asynchronous Workflow Methods

Asynchronous workflow methods are often used much like activities, because the method defers execution until
all input `Promise<T>` objects are ready. However, the replay mechanism handles asynchronous methods
differently than activities.

- Replay doesn't guarantee that an asynchronous method will execute only once. It defers execution on
  an asynchronous method until its input Promise objects are ready, but it then executes that method for all
  subsequent episodes.
- When an asynchronous method completes, it doesn't start a new episode.

An example of replaying an asynchronous workflow is provided in [AWS Flow Framework for Java Replay Behavior](programming-replay.md "programming-replay.md").

## Replay and Workflow Implementation

For the most part, you don't need to be concerned with the details of the replay mechanism. It is basically
something that happens behind the scenes. However, replay has two important implications for your workflow
implementation.

- Do not use workflow methods to perform long-running tasks, because replay will repeat that task
  multiple times. Even asynchronous workflow methods typically run more than once. Instead, use activities for
  long running tasks; replay executes activities only once.
- Your workflow logic must be completely deterministic; every episode must take the same control flow
  path. For example, the control flow path should not depend on the current time. For a detailed description
  of replay and the determinism requirement, see [Nondeterminism](details.md#details.non "details.md#details.non").
