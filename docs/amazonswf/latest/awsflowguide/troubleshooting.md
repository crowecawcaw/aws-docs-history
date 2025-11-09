# Troubleshooting and debugging tips for AWS Flow Framework for Java

###### Topics

- [Compilation errors](#troubleshooting.compilation "#troubleshooting.compilation")
- [Unknown resource fault](#troubleshooting.UnknownResourceFault "#troubleshooting.UnknownResourceFault")
- [Exceptions when calling get() on a Promise](#troubleshooting.ExceptionsCallingGet "#troubleshooting.ExceptionsCallingGet")
- [Nondeterministic workflows](#troubleshooting.NonDeterministicWorkflows "#troubleshooting.NonDeterministicWorkflows")
- [Problems due to versioning](#troubleshooting.Versioning "#troubleshooting.Versioning")
- [Troubleshooting and debugging a workflow execution](#troubleshooting.DebuggingWorkflowExecution "#troubleshooting.DebuggingWorkflowExecution")
- [Lost tasks](#troubleshooting.LostTasks "#troubleshooting.LostTasks")
- [Validation failure due to API parameter length constraints](#troubleshooting.validation-fail "#troubleshooting.validation-fail")
  This section describes some common pitfalls that you might run into while developing
  workflows using AWS Flow Framework for Java. It also provides some tips to help you diagnose and debug
  problems.

## Compilation errors

If you are using the AspectJ compile time weaving option, you may run into compile time
errors in which the compiler isn't able to find the generated client classes for your
workflow and activities. The likely cause of such compilation errors is that the AspectJ
builder ignored the generated clients during compilation. You can fix this issue by removing
AspectJ capability from the project and re-enabling it. Note that you will need to do this
every time your workflow or activities interfaces change. Because of this issue, we recommend
that you use the load time weaving option instead. See the section [Setting up the AWS Flow Framework for Java](setup.md "setup.md") for more details.

## Unknown resource fault

Amazon SWF returns unknown resource fault when you try to perform an operation on a resource
that isn't available. The common causes for this fault are:

- You configure a worker with a domain that doesn't exist. To fix this, first register
  the domain using the [Amazon SWF
  console](../developerguide/swf-dg-register-domain-console.md "../developerguide/swf-dg-register-domain-console.md") or the [Amazon SWF
  service API](../apireference/API_RegisterDomain.md "../apireference/API_RegisterDomain.md").
- You try to create workflow execution or activity tasks of types that have not been
  registered. This can happen if you try to create the workflow execution before the workers
  have been run. Because workers register their types when they are run for the first time,
  you must run them at least once before attempting to start executions (or manually
  register the types using the Console or the service API). Note that once types have been
  registered, you can create executions even if no worker is running.
- A worker attempts to complete a task that has already timed out. For example, if a
  worker takes too long to process a task and exceeds a timeout, it will get an
  UnknownResource fault when it attempts to complete or fail the task. The AWS Flow Framework workers
  will continue to poll Amazon SWF and process additional tasks. However, you should consider
  adjusting the timeout. Adjusting the timeout requires that you register a new version of
  the activity type.

## Exceptions when calling get() on a Promise

Unlike Java Future, `Promise` is a non-blocking construct and calling
`get()` on a `Promise` that isn't ready yet will throw an exception
instead of blocking. The correct way to use a `Promise` is to pass it to an
asynchronous method (or a task) and access its value in the asynchronous method.
AWS Flow Framework for Java ensures that an asynchronous method is called only when all
`Promise` arguments passed to it have become ready. If you believe your code is
correct or if you run into this while running one of the AWS Flow Framework samples, then it is most
likely due to AspectJ not being properly configured. For details, see the section [Setting up the AWS Flow Framework for Java](setup.md "setup.md").

## Nondeterministic workflows

As described in the section [Nondeterminism](details.md#details.non "details.md#details.non"), the
implementation of your workflow must be deterministic. Some common mistakes that can lead to
nondeterminism are use of system clock, use of random numbers, and generation of GUIDs. Because
these constructs may return different values at different times, the control flow of your
workflow may take different paths each time it is executed (see the sections [AWS Flow Framework Basic Concepts: Distributed Execution](awsflow-basics-distributed-execution.md "awsflow-basics-distributed-execution.md") and [Understanding a Task in AWS Flow Framework for Java](details.md "details.md") for details). If the framework detects nondeterminism while
executing the workflow, an exception will be thrown.

## Problems due to versioning

When you implement a new version of your workflow or activity—for instance, when you
add a new feature—you should increase the version of the type by using the appropriate
annotation: `@Workflow`, `@Activites`, or `@Activity`. When
new versions of a workflow are deployed, often times you will have executions of the existing
version that are already running. Therefore, you need to make sure that workers with the
appropriate version of your workflow and activities get the tasks. You can accomplish this by
using a different set of task lists for each version. For example, you can append the version
number to the name of the task list. This ensures that tasks belonging to different versions
of the workflow and activities are assigned to the appropriate workers.

## Troubleshooting and debugging a workflow execution

The first step in troubleshooting a workflow execution is to use the Amazon SWF console to look
at the workflow history. The workflow history is a complete and authoritative record of all
the events that changed the execution state of the workflow execution. This history is
maintained by Amazon SWF and is invaluable for diagnosing problems. The Amazon SWF console enables you
to search for workflow executions and drill down into individual history events.

AWS Flow Framework provides a `WorkflowReplayer` class that you can use to replay a
workflow execution locally and debug it. Using this class, you can debug closed and running
workflow executions. `WorkflowReplayer` relies on the history stored in Amazon SWF to
perform the replay. You can point it to a workflow execution in your Amazon SWF account or provide
it with the history events (for example, you can retrieve the history from Amazon SWF and serialize
it locally for later use). When you replay a workflow execution using the
`WorkflowReplayer`, it doesn't impact the workflow execution running in your
account. The replay is done completely on the client. You can debug the workflow, create
breakpoints, and step into code using your debugging tools as usual. If you are using Eclipse,
consider adding step filters to filter AWS Flow Framework packages.

For example, the following code snippet can be used to replay a workflow execution:

```
String workflowId = "testWorkflow";
String runId = "<run id>";
Class<HelloWorldImpl> workflowImplementationType = HelloWorldImpl.class;
WorkflowExecution workflowExecution = new WorkflowExecution();
workflowExecution.setWorkflowId(workflowId);
workflowExecution.setRunId(runId);

WorkflowReplayer<HelloWorldImpl> replayer = new WorkflowReplayer<HelloWorldImpl>(
    swfService, domain, workflowExecution, workflowImplementationType);

System.out.println("Beginning workflow replay for " + workflowExecution);
Object workflow = replayer.loadWorkflow();
System.out.println("Workflow implementation object:");
System.out.println(workflow);
System.out.println("Done workflow replay for " + workflowExecution);

```

AWS Flow Framework also allows you to get an asynchronous thread dump of your workflow execution.
This thread dump gives you the call stacks of all open asynchronous tasks. This information
can be useful to determine which tasks in the execution are pending and possibly stuck. For
example:

```
String workflowId = "testWorkflow";
String runId = "<run id>";
Class<HelloWorldImpl> workflowImplementationType = HelloWorldImpl.class;
WorkflowExecution workflowExecution = new WorkflowExecution();
workflowExecution.setWorkflowId(workflowId);
workflowExecution.setRunId(runId);

WorkflowReplayer<HelloWorldImpl> replayer = new WorkflowReplayer<HelloWorldImpl>(
    swfService, domain, workflowExecution, workflowImplementationType);

try {
    String flowThreadDump = replayer.getAsynchronousThreadDumpAsString();
    System.out.println("Workflow asynchronous thread dump:");
    System.out.println(flowThreadDump);
}
catch (WorkflowException e) {
    System.out.println("No asynchronous thread dump available as workflow has failed: " + e);
}

```

## Lost tasks

Sometimes you may shut down workers and start new ones in quick succession only to
discover that tasks get delivered to the old workers. This can happen due to race conditions
in the system, which is distributed across several processes. The problem can also appear when
you are running unit tests in a tight loop. Stopping a test in Eclipse can also sometimes
cause this because shutdown handlers may not get called.

In order to make sure that the problem is in fact due to old workers getting tasks, you
should look at the workflow history to determine which process received the task that you
expected the new worker to receive. For example, the `DecisionTaskStarted` event in
history contains the identity of the workflow worker that received the task. The id used by
the Flow Framework is of the form: {`processId`}`@`{`host name`}. For instance, following are the
details of the `DecisionTaskStarted` event in the Amazon SWF console for a sample
execution:

|                    |                                  |
| ------------------ | -------------------------------- |
| Event Timestamp    | Mon Feb 20 11:52:40 GMT-800 2012 |
| Identity           | 2276@ip-0A6C1DF5                 |
| Scheduled Event Id | 33                               |

In order to avoid this situation, use different task lists for each test. Also, consider
adding a delay between shutting down old workers and starting new ones.

## Validation failure due to API parameter length constraints

Amazon SWF enforces length constraints on API parameters. You will receive an `HTTP 400` error if your workflow or activity implementation exceeds the constraints. For example, when calling `recordActivityHeartbeat` on `ActivityExecutionContext` to send a heartbeat for a running activity, the string must not be longer than 2048 characters.

Another common scenario is when an activity fails due to an exception. The framework reports an activity failure to Amazon SWF by calling [RespondActivityTaskFailed](../apireference/API_RespondActivityTaskFailed.md "../apireference/API_RespondActivityTaskFailed.md") with the serialized exception as details. The API call will report a 400 error if the serialized exception has a length greater than 32,768 bytes. To mitigate this situation, you can truncate the exception message or the causes to conform to the length constraint.
