# AWS Flow Framework Basic Concepts: Application Structure

Conceptually, an AWS Flow Framework application consists of three basic components: _workflow
starters_, _workflow workers_, and _activity workers_. One or more host
applications are responsible for registering the workers (workflow and activity) with Amazon SWF, starting the workers,
and handling cleanup. The workers handle the mechanics of executing the workflow and may be implemented on several
hosts.

This diagram represents a basic AWS Flow Framework application:

![Schematic AWS Flow Framework application](images/swf-application-model.png)

###### Note

Implementing these components in three separate applications is convenient conceptually, but you can create
applications to implement this functionality in a variety of ways. For example, you can use a single host application
for the activity and workflow workers, or use separate activity and workflow hosts. You can also have multiple activity
workers, each handling a different set of activities on separate hosts, and so on.

The three AWS Flow Framework components interact indirectly by sending HTTP requests to Amazon SWF, which manages
the requests. Amazon SWF does the following:

- Maintains one or more decision task lists, which determine the next step to be performed by a workflow
  worker.
- Maintains one or more activities task lists, which determine which tasks will be performed by an activity
  worker.
- Maintains a detailed step-by-step history of the workflow's execution.
  With the AWS Flow Framework, your application code doesn't need to deal directly with many of the details shown in the
  figure, such as sending HTTP requests to Amazon SWF. You simply call AWS Flow Framework methods and the framework handles the
  details behind the scenes.

## Role of the Activity Worker

The activity worker performs the various tasks that the workflow must accomplish. It consists of:

- The activities implementation, which includes a set of activity methods that perform particular tasks
  for the workflow.
- An
  [ActivityWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md")
  object, which uses HTTP long poll requests to poll Amazon SWF for activity tasks to be performed.
  When a task is needed, Amazon SWF responds to the request by sending the information required to perform the task. The
  [ActivityWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md")
  object then calls the appropriate activity method, and returns the results to Amazon SWF.

## Role of the Workflow Worker

The workflow worker orchestrates the execution of the various activities, manages data flow, and handles
failed activities. It consists of:

- The workflow implementation, which includes the activity orchestration logic, handles failed
  activities, and so on.
- An activities client, which serves as a proxy for the activity worker and enables the workflow
  worker to schedule activities to be executed asynchronously.
- A [WorkflowWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md")
  object, which uses HTTP long poll requests to poll Amazon SWF for decision tasks. If
  there are tasks on the workflow task list, Amazon SWF responds to the request by returning the information that
  is required to perform the task. The framework then executes the workflow to perform the task and returns
  the results to Amazon SWF.

## Role of the Workflow Starter

The workflow starter starts a workflow instance, also referred to as a _workflow
execution_, and can interact with an instance during execution in order to pass additional
data to the workflow worker or obtain the current workflow state.

The workflow starter uses a workflow client to start the workflow execution, interacts with the workflow as
needed during execution, and handles cleanup. The workflow starter could be a locally-run application, a web
application, the AWS CLI or even the AWS Management Console.

## How Amazon SWF Interacts with Your Application

Amazon SWF mediates the interaction between the workflow components and maintains a detailed workflow history.
Amazon SWF doesn't initiate communication with the components; it waits for HTTP requests from the components and
manages the requests as required. For example:

- If the request is from a worker, polling for available tasks, Amazon SWF responds directly to the worker if
  a task is available. For more information about how polling works, see [Polling for Tasks](../developerguide/swf-dg-basic.md#swf-dev-comm-proto "../developerguide/swf-dg-basic.md#swf-dev-comm-proto") in the _Amazon
  Simple Workflow Service Developer Guide_.
- If the request is a notification from an activity worker that a task is complete, Amazon SWF records the
  information in the execution history and adds a task to the decision task list to inform the workflow worker
  that the task is complete, allowing it to proceed to the next step.
- If the request is from the workflow worker to execute an activity, Amazon SWF records the information in
  the execution history and adds a task to the activities task list to direct an activity worker to execute
  the appropriate activity method.

This approach allows workers to run on any system with an Internet connection, including Amazon EC2 instances,
corporate data centers, client computers, and so on. They don't even have to be running the same operating system.
Because the HTTP requests originate with the workers, there is no need for externally visible ports; workers can run
behind a firewall.

## For More Information

For a more thorough discussion of how Amazon SWF works, see [Amazon Simple Workflow Service Developer Guide](../developerguide.md "../developerguide.md").
