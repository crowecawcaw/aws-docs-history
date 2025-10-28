# Developing workflow components with Amazon SWF

Developing distributed applications requires coordinating many components and dealing with
latency and unreliability inherent in remote communication.

With Amazon Simple Workflow Service (Amazon SWF), you can develop asynchronous and distributed applications by providing a
programming model and infrastructure for coordinating distributed components and maintaining their execution state in
a reliable way. By relying on Amazon SWF, you are freed to focus on building the aspects of your application that
differentiate it.

## Components of a workflow

Components of a workflow
The fundamental concept in Amazon SWF is the _workflow_. A workflow is a set of
_activities_ that carry out some objective, together with logic that coordinates the activities.
For example, a workflow could receive a customer order and take whatever actions are necessary to fulfill the order.

Each workflow runs in a resource called a _domain_, which controls the workflow's scope. An AWS
account can have multiple domains, each of which can contain multiple workflows, but workflows in different domains
can't interact.

When designing an Amazon SWF workflow, you define each of the required activities. You then
register each activity with Amazon SWF as an activity type. You will provide a name, version,
and timeout values. For example, a customer may have an expectation that an order will
ship within 24 hours.

In the process of carrying out the workflow, some activities may need to be performed more than once, perhaps
with varying inputs. For example, in a customer-order workflow, you might have an activity that handles purchased
items. If the customer purchases multiple items, then this activity would have to run multiple times. Amazon SWF has the
concept of an _activity task_ that represents one invocation of an activity. In our example, the
processing of each item would be represented by a single activity task.

An _activity worker_ is a program that receives activity tasks,
performs them, and provides results. The task might actually be performed by a person.
For example, a statistical analyst might receive sets of data, analyze the data, and
then send back their analysis.

Activity tasks, and the activity workers that perform them, can run synchronously or
asynchronously. Workers can run in one location or be distributed across multiple
computers, potentially in different geographic regions. Different activity workers can
be written in different programming languages and run on different operating systems.
For example, one activity worker might be running on a server in Asia, while another
might be running on a mobile device in North America.

The coordination logic in a workflow is contained in a software program called a
_decider_. A decider schedules activity tasks, provides input to
activity workers, processes events that arrive while the workflow is in progress, and
ends (or closes) the workflow after the objective has been met.

The role of the Amazon SWF service is to function as a reliable central hub through which data is exchanged between
the decider, the activity workers, and other relevant entities such as the person administering the workflow. Amazon SWF
also maintains the state of each workflow execution, which saves your application from having to store the state in
a durable way.

The decider directs the workflow by receiving decision tasks from Amazon SWF and responding
back to Amazon SWF with decisions. A decision represents an action or set of actions, which
are the next steps in the workflow. A typical decision would be to schedule an activity
task. Decisions can also be used to delay tasks with timers, request cancellation of
in-progress tasks, and to complete workflows.

The mechanism by which both the activity workers and the decider receive their tasks (activity tasks and
decision tasks respectively) is by polling the Amazon SWF service.

Amazon SWF informs the decider of the state of the workflow by including, with each decision
task, a copy of the current workflow execution history. The workflow execution history
is composed of events, where an event represents a significant change in the state of
the workflow execution. Examples of events include task completion, task time outs, or
the expiration of a timer. The history is a complete, consistent, and authoritative
record of the workflow's progress.

Amazon SWF access control uses AWS Identity and Access Management (IAM), so you can control access to AWS resources.
For example, you can allow a user to access your account, but only to run certain
workflows in a particular domain.

## Running your workflow

The following provide an overview of the steps necessary to develop and run a workflow in Amazon SWF:

1. Write **activity workers** to perform the processing steps in your workflow.
2. Write a **decider** to handle the coordination logic of your workflow.
3. Register your activities and workflow with Amazon SWF.

You can do this step programmatically or by using the AWS Management Console. 4. Start your activity workers and decider.

These actors can run on any computing device that can access an Amazon SWF endpoint. For example, you could use
compute instances in the cloud, such as Amazon Elastic Compute Cloud (Amazon EC2); servers in your data center; or even a mobile device,
to host a decider or activity worker. Once started, the decider and activity workers should start polling Amazon SWF
for tasks. 5. Start one or more executions of your workflow.

You can start workflows programmatically or via the AWS Management Console.

Each execution runs independently and you can provide each with its own set of input
data. When an execution is started, Amazon SWF schedules the initial decision task.
In response, your decider begins generating decisions that initiate activity
tasks. Execution continues until your decider makes a decision to close the
execution. 6. View workflow executions using the AWS Management Console.

You can filter and view complete details of running and completed executions. For
example, you can select an open execution to see which tasks have been completed
and what their results were.

## Setting up your development environment

You have the option of developing for Amazon SWF in any of the
programming languages supported by AWS. For Java developers, the AWS Flow Framework is also available. For more information, see the [AWS Flow Framework](https://aws.amazon.com/swf/flow/ "https://aws.amazon.com/swf/flow/") website, and see [AWS Flow Framework for Java Developer Guide](../awsflowguide.md "../awsflowguide.md").

To reduce latency and to store data in a location that meets your requirements, Amazon SWF
provides **endpoints** in different Regions.

Each endpoint in Amazon SWF is completely independent. Any domains,
workflows, and activities you have registered in one Region will not share data or
attributes with those in another Region.

When you register an Amazon SWF domain, workflow, or activity, it exists _only
within the Region you registered it in_. For example, you could register a
domain named `SWF-Flows-1` in two different Regions, but they will share no
data or attributes with each other — each acting as a completely independent
domain.

For a list of Amazon SWF endpoints, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

## Develop with AWS SDKs

Amazon SWF is supported by the AWS SDKs for Java, .NET, Node.js, PHP, Python, and Ruby,
providing a convenient way to use the Amazon SWF HTTP API in the programming language of your
choice.

You can develop _deciders_, _activity workers_, or _workflow starters_ using the API exposed by these libraries. And, you can use visibility operations through these libraries so you can develop your own Amazon SWF monitoring and reporting tools.

To download tools for developing and managing applications on AWS, including SDKs, go to the [Developer Center](https://aws.amazon.com/developer/tools "https://aws.amazon.com/developer/tools").

For detailed information about the Amazon SWF operations in each SDK, refer to the
language-specific reference documentation for the SDK.

## Consider the AWS Flow Framework

The AWS Flow Framework is an enhanced SDK for writing distributed, asynchronous programs that run as workflows
on Amazon SWF. The framework is available for the Java programming language and provides classes for
writing complex distributed programs.

With the AWS Flow Framework, you use preconfigured types to map the definition of your workflow
directly to methods in your program. The AWS Flow Framework supports standard object-oriented
concepts, such as exception-based error handling. Programs written with the AWS Flow Framework can
be created, run, and debugged entirely within your preferred editor or IDE. For more
information, see the [AWS Flow Framework](https://aws.amazon.com/swf/flow/ "https://aws.amazon.com/swf/flow/") website,
and see [AWS Flow Framework for Java Developer Guide](../awsflowguide.md "../awsflowguide.md").
