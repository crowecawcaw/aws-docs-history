# Subscription Workflow Tutorial Part 2: Implementing the Workflow

Up until now, our code has been pretty generic. This is the part where we begin to really define what our
workflow does, and what activities we'll need to implement it.

###### Topics

- [Designing the Workflow](#designing-the-workflow "#designing-the-workflow")
- [Setting up our Workflow Code](#setting-up-our-workflow-code "#setting-up-our-workflow-code")
- [Registering the Workflow](#registering-the-workflow "#registering-the-workflow")
- [Polling for Decisions](#polling-for-decisions "#polling-for-decisions")
- [Starting the Workflow Execution](#starting-the-workflow-execution "#starting-the-workflow-execution")
- [Next Steps](#implementing-workflow-next-steps "#implementing-workflow-next-steps")

## Designing the Workflow

If you recall, the initial idea for this workflow consisted of the following steps:

1. Get a subscription address (email or SMS) from the user.
2. Create an SNS topic and subscribe the provided endpoints to the topic.
3. Wait for the user to confirm the subscription.
4. If the user confirms, publish a congratulatory message to the topic.

We can think of each step in our workflow as an _activity_ that it must perform. Our
_workflow_ is responsible for scheduling each activity at the appropriate time, and
coordinating data transfer between activities.

For this workflow, we'll create a separate activity for each of these steps, naming them
descriptively:

1. get_contact_activity
2. subscribe_topic_activity
3. wait_for_confirmation_activity
4. send_result_activity

These activities will be executed in order, and data from each step will be used in the subsequent
step.

We could design our application so that all of the code exists in one source file, but this runs contrary to
the way that Amazon SWF was designed. It is designed for workflows that can span the entire Internet in scope, so let's
at least break the application up into two separate executables:

- `swf_sns_workflow.rb` - Contains the workflow and workflow starter.
- `swf_sns_activities.rb` - Contains the activities and activities starter.

The workflow and activity implementations can be run in separate windows, separate computers, or even
different parts of the world. Because Amazon SWF is keeping track of the details of your workflows and activities,
your workflow can coordinate scheduling and data transfer of your activities no matter where they are
running.

## Setting up our Workflow Code

We'll begin by creating a file called `swf_sns_workflow.rb`. In this file, declare a class
called **SampleWorkflow**. Here is the class declaration and its constructor, the
`initialize` method.

```
require_relative 'utils.rb'

# SampleWorkflow - the main workflow for the SWF/SNS Sample
#
# See the file called `README.md` for a description of what this file does.
class SampleWorkflow

  attr_accessor :name

  def initialize(workflowId)

    # the domain to look for decision tasks in.
    @domain = init_domain

    # the task list is used to poll for decision tasks.
    @workflowId = workflowId

    # The list of activities to run, in order. These name/version hashes can be
    # passed directly to AWS::SimpleWorkflow::DecisionTask#schedule_activity_task.
    @activity_list = [
      { :name => 'get_contact_activity', :version => 'v1' },
      { :name => 'subscribe_topic_activity', :version => 'v1' },
      { :name => 'wait_for_confirmation_activity', :version => 'v1' },
      { :name => 'send_result_activity', :version => 'v1' },
    ].reverse! # reverse the order... we're treating this like a stack.

    register_workflow
  end
```

As you can see, we are keeping the following class instance data:

- `domain` - The domain name retrieved from `init_domain` in
  `utils.rb`.
- `workflowId` - The task list passed in to `initialize`.
- `activity_list` - The activity list, which has the names and versions of the activities we'll
  run.

The domain name, activity name, and activity version are enough for Amazon SWF to positively identify an activity
type, so that is all of the data we need to keep about our activities in order to schedule them.

The task list will be used by the workflow's _decider_ code to poll for decision tasks
and schedule activities.

At the end of this function, we call a method we haven't yet defined: `register_workflow`.
We'll define this method next.

## Registering the Workflow

To use a workflow type, we must first register it. Like an activity type, a workflow type is identified by
its domain, name, and version. Also, like both domains and activity types, you can't re-register an existing
workflow type. If you need to change anything about a workflow type, you must provide it with a new version,
which essentially creates a new type.

Here is the code for `register_workflow`, which is used to either retrieve the existing workflow
type we registered on a previous run or to register the workflow if it has not yet been registered.

```
  # Registers the workflow
  def register_workflow
    workflow_name = 'swf-sns-workflow'
    @workflow_type = nil

    # a default value...
    workflow_version = '1'

    # Check to see if this workflow type already exists. If so, use it.
    @domain.workflow_types.each do | a |
      if (a.name == workflow_name) && (a.version == workflow_version)
        @workflow_type = a
      end
    end

    if @workflow_type.nil?
      options =  {
        :default_child_policy => :terminate,
        :default_task_start_to_close_timeout => 3600,
        :default_execution_start_to_close_timeout => 24 * 3600 }

      puts "registering workflow: #{workflow_name}, #{workflow_version}, #{options.inspect}"
      @workflow_type = @domain.workflow_types.register(workflow_name, workflow_version, options)
    end

    puts "** registered workflow: #{workflow_name}"
  end
```

First, we check to see if the workflow name and version is already registered by iterating through the
domain's [workflow_types](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#workflow_types-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#workflow_types-instance_method")
collection. If we find a match, we'll use the workflow type that was already registered.

If we don't find a match, then a new workflow type is registered (by calling [register](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowTypeCollection.md#register-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowTypeCollection.md#register-instance_method")
on the same `workflow_types` collection that we were searching for the workflow in) with the name
'swf-sns-workflow', version '1', and the following options.

```
      options =  {
        :default_child_policy => :terminate,
        :default_task_start_to_close_timeout => 3600,
        :default_execution_start_to_close_timeout => 24 * 3600 }
```

Options passed in during registration are used to set _default behavior_ for our
workflow type, so we don't need to set these values every time we start a new workflow execution.

Here, we just set some timeout values: the maximum time it can take from the time a task starts to when it
closes (one hour), and the maximum time it can take for the workflow execution to complete (24 hours). If either
of these times are exceeded, the task or workflow will timeout.

For more information about timeout values, see [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md") .

## Polling for Decisions

At the heart of every workflow execution there is a _decider_. The decider's
responsibility is for managing the execution of the workflow itself. The decider receives _decision
tasks_ and responds to them, either by scheduling new activities, cancelling and restarting activities,
or by setting the state of the workflow execution as complete, cancelled, or failed.

The decider uses the workflow execution's _task list_ name to receive decision tasks to
respond to. To poll for decision tasks, call [poll](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTaskCollection.md#poll-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTaskCollection.md#poll-instance_method")
on the domain's [decision_tasks](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#decision_tasks-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#decision_tasks-instance_method")
collection to loop over available decision tasks. You can then check for new events in the decision task by
iterating over its [new_events](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#new_events-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#new_events-instance_method")
collection.

The returned events are [AWS::SimpleWorkflow::HistoryEvent](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/HistoryEvent.md "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/HistoryEvent.md")
objects, and you can get the type of the event by using the returned event's [event_type](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/HistoryEvent.md#event_type-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/HistoryEvent.md#event_type-instance_method")
member. For a list and description of history event types, see [HistoryEvent](../apireference/API_HistoryEvent.md "../apireference/API_HistoryEvent.md") in the
_Amazon Simple Workflow Service API Reference_.

Here is the beginning of the decision task poller's logic. A new method in our workflow class called
`poll_for_decisions`.

```
  def poll_for_decisions
    # first, poll for decision tasks...
    @domain.decision_tasks.poll(@workflowId) do | task |
      task.new_events.each do | event |
        case event.event_type
```

We'll now branch the execution of our decider based on the `event_type` that is received.
The first one we are likely to receive is **WorkflowExecutionStarted**. When this
event is received, it means that Amazon SWF is signaling to your decider that it should begin the workflow execution.
We'll begin by scheduling the first activity by calling [schedule_activity_task](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#schedule_activity_task-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#schedule_activity_task-instance_method")
on the task we received while polling.

We'll pass it the first activity we declared in our activity list, which, because we reversed the list so
we can use it like a stack, occupies the `last` position on the list. The "activities"
we defined are just maps consisting of a name and version number, but this is all that Amazon SWF needs to identify
the activity for scheduling, assuming that the activity has already been registered.

```
          when 'WorkflowExecutionStarted'
            # schedule the last activity on the (reversed, remember?) list to
            # begin the workflow.
            puts "** scheduling activity task: #{@activity_list.last[:name]}"

            task.schedule_activity_task( @activity_list.last,
              { :workflowId => "#{@workflowId}-activities" } )
```

When we schedule an activity, Amazon SWF sends an _activity task_ to the activity task list
that we pass in while scheduling it, signaling the task to begin. We'll deal with activity tasks in
[Subscription Workflow Tutorial Part 3: Implementing the Activities](swf-sns-tutorial-implementing-activities.md "swf-sns-tutorial-implementing-activities.md"), but it is worth noting that we don't execute the task
here. We only tell Amazon SWF that it should be _scheduled_.

The next activity that we'll need to address is the **ActivityTaskCompleted** event, which occurs when Amazon SWF has received an activity completed
response from an activity task.

```
          when 'ActivityTaskCompleted'
            # we are running the activities in strict sequential order, and
            # using the results of the previous activity as input for the next
            # activity.
            last_activity = @activity_list.pop

            if(@activity_list.empty?)
              puts "!! All activities complete! Sending complete_workflow_execution..."
              task.complete_workflow_execution
              return true;
            else
              # schedule the next activity, passing any results from the
              # previous activity. Results will be received in the activity
              # task.
              puts "** scheduling activity task: #{@activity_list.last[:name]}"
              if event.attributes.has_key?('result')
                task.schedule_activity_task(
                  @activity_list.last,
                  { :input => event.attributes[:result],
                    :workflowId => "#{@workflowId}-activities" } )
              else
                task.schedule_activity_task(
                  @activity_list.last, { :workflowId => "#{@workflowId}-activities" } )
              end
            end
```

Because we are executing our tasks in a linear fashion, and only one activity is executing at once, we'll
take this opportunity to pop the completed task from the `activity_list` stack. If this results in an empty list,
then we know that our workflow is complete. In this case, we signal to Amazon SWF that our workflow is complete by
calling [complete_workflow_execution](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#complete_workflow_execution-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DecisionTask.md#complete_workflow_execution-instance_method")
on the task.

In the event that the list still has entries, we'll schedule the next activity on the list (again, in the
last position). This time, however, we'll look to see if the previous activity returned any result data to Amazon SWF
upon completion, which is provided to the workflow in the event's attributes, in the optional
`result` key. If the activity generated a result, we'll pass it as the `input`
option to the next scheduled activity, along with the activity task list.

By retrieving the `result` values of completed activities, and by setting the
`input` values of scheduled activities, we can pass data from one activity to the next, or we can
use data from an activity to change behavior in our decider based on the results from an activity.

For the purposes of this tutorial, these two event types are the most important in defining the behavior of
our workflow. However, an activity can generate events other than **ActivityTaskCompleted**. We'll wrap up our decider code by providing demonstration handler
code for the **ActivityTaskTimedOut** and **ActivityTaskFailed** events, and for the **WorkflowExecutionCompleted** event, which will be generated when Amazon SWF processes the
`complete_workflow_execution` call that we make when we run out of activities to run.

```
          when 'ActivityTaskTimedOut'
            puts "!! Failing workflow execution! (timed out activity)"
            task.fail_workflow_execution
            return false

          when 'ActivityTaskFailed'
            puts "!! Failing workflow execution! (failed activity)"
            task.fail_workflow_execution
            return false

          when 'WorkflowExecutionCompleted'
            puts "## Yesss, workflow execution completed!"
            task.workflow_execution.terminate
            return false
        end
      end
    end
  end
```

## Starting the Workflow Execution

Before any decision tasks will be generated for the workflow to poll for, we need to start the workflow
execution.

To start the workflow execution, call [start_execution](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md#start_execution-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md#start_execution-instance_method")
on your registered workflow type ([AWS::SimpleWorkflow::WorkflowType](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md")).
We'll define a small wrapper around this to make use of the `workflow_type` instance member that
we retrieved in the class constructor.

```
  def start_execution
    workflow_execution = @workflow_type.start_execution( {
      :workflowId => @workflowId } )
    poll_for_decisions
  end
end
```

Once the workflow is executing, decision events will begin to appear on the workflow's task list, which is
passed as a workflow execution option in [start_execution](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md#start_execution-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/WorkflowType.md#start_execution-instance_method").

Unlike options that are provided when the workflow type is registered, options that are passed to
`start_execution` are not considered to be part of the workflow type. You are free to change these per workflow
execution without changing the workflow's version.

Because we'd like the workflow to begin executing when we run the file, add some code that instantiates the
class and then calls the `start_execution` method that we just defined.

```
if __FILE__ == $0
  require 'securerandom'

  # Use a different task list name every time we start a new workflow execution.
  #
  # This avoids issues if our pollers re-start before SWF considers them closed,
  # causing the pollers to get events from previously-run executions.
  workflowId = SecureRandom.uuid

  # Let the user start the activity worker first...

  puts ""
  puts "Amazon SWF Example"
  puts "------------------"
  puts ""
  puts "Start the activity worker, preferably in a separate command-line window, with"
  puts "the following command:"
  puts ""
  puts "> ruby swf_sns_activities.rb #{workflowId}-activities"
  puts ""
  puts "You can copy & paste it if you like, just don't copy the '>' character."
  puts ""
  puts "Press return when you're ready..."

  i = gets

  # Now, start the workflow.

  puts "Starting workflow execution."
  sample_workflow = SampleWorkflow.new(workflowId)
  sample_workflow.start_execution
end
```

To avoid any task list naming conflicts, we'll use `SecureRandom.uuid` to generate a
random UUID that we can use as the task list name, guaranteeing that a different task list name is used for each
workflow execution.

###### Note

Task lists are used to record events about a workflow execution, so if you use the same task list for
multiple executions of the same workflow type, you might get events that were generated during a previous
execution, especially if you are running them in near succession to each other, which is often the case when
trying out new code or running tests.

To avoid the issue of having to deal with artifacts from previous executions, we can use a new task list for
each execution, specifying it when we begin the workflow execution.

There is also a bit of code here to provide instructions for the person running it (probably you), and to
provide the "activity" version of the task list. The decider uses this task list name to schedule
activities for the workflow, and the activities implementation will listen for activity events on this task list
name to know when to begin the scheduled activities and to provide updates about the activity execution.

The code also waits for the user to start running the activities starter _before_ it
starts the workflow execution, so the activities starter will be ready to respond when activity tasks begin
appearing on the provided task list.

## Next Steps

You have implemented the work flow. Next, you will define the activities and an activities starter, in
[Subscription Workflow Tutorial Part 3: Implementing the Activities](swf-sns-tutorial-implementing-activities.md "swf-sns-tutorial-implementing-activities.md").
