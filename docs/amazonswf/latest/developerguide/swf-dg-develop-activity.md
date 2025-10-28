# Developing an Activity Worker in Amazon SWF

An activity worker provides the implementation of one or more activity types. An activity worker communicates
with Amazon SWF to receive activity tasks and perform them. You can have a fleet of multiple activity workers performing
activity tasks of the same activity type.

Amazon SWF makes an activity task available to activity workers when the decider schedules the activity task. When a
decider schedules an activity task, it provides the data (which you determine) that the activity worker needs to
perform the activity task. Amazon SWF inserts this data into the activity task before sending it to the activity worker.

Activity workers are managed by you. They can be written in any language. A worker can be run anywhere, as long
as it can communicate with Amazon SWF through the API. Because Amazon SWF provides all the information needed to perform an
activity task, all activity workers can be stateless. Statelessness enables your workflows to be highly scalable; to
handle increased capacity requirements, simply add more activity workers.

This section explains how to implement an activity worker. The activity workers should repeatedly do the
following.

1. Poll Amazon SWF for an activity task.
2. Begin performing the task.
3. Periodically report a heartbeat to Amazon SWF if the task is long-lived.
4. Report that the task completed or failed and return the results to Amazon SWF.

###### Topics

- [Polling for Activity Tasks](#swf-dg-polling-activity-tasks "#swf-dg-polling-activity-tasks")
- [Performing the Activity Task](#swf-dg-performing-activity-tasks "#swf-dg-performing-activity-tasks")
- [Reporting Activity Task Heartbeats](#swf-dg-managing-activity-tasks "#swf-dg-managing-activity-tasks")
- [Completing or Failing an Activity Task](#swf-dg-complete-or-fail "#swf-dg-complete-or-fail")
- [Launching Activity Workers](#swf-dg-launch-activity-workers "#swf-dg-launch-activity-workers")

## Polling for Activity Tasks

To perform activity tasks, each activity worker must poll Amazon SWF by periodically calling the `PollForActivityTask` action.

In the following example, the activity worker `ChargeCreditCardWorker01` polls for a
task on the task list, `ChargeCreditCard-v0.1`. If no activity tasks are available, after 60
seconds, Amazon SWF sends back an empty response. An empty response is a `Task` structure in which the
value of the `taskToken` is an empty string.

```
https://swf.us-east-1.amazonaws.com
PollForActivityTask
{
  "domain" : "867530901",
  "taskList" : { "name": "ChargeCreditCard-v0.1" },
  "identity" : "ChargeCreditCardWorker01"
}
```

If an activity task becomes available, Amazon SWF returns it to the activity worker. The task contains the data
that the decider specifies when it schedules the activity.

After an activity worker receives an activity task, it is ready to perform the work. The next section
provides information about performing an activity task.

## Performing the Activity Task

After receiving an activity task, the activity worker is ready to perform it.

###### To perform an activity task

1. Program your activity worker to interpret the content in the input field of the task. This field
   contains the data specified by the decider when the task was scheduled.
2. Program the activity worker to begin processing the data and executing your logic.

The next section describes how to program your activity workers to provide status updates to Amazon SWF for long
running activities.

## Reporting Activity Task Heartbeats

If a heartbeat timeout was registered with the activity type, then the activity worker must record a
heartbeat before the heartbeat timeout is exceeded. If an activity task doesn't provide a heartbeat within the
timeout, the task times out, Amazon SWF closes it and schedules a new decision task to inform a decider of the timeout.
The decider can then reschedule the activity task or take another action.

If, after timing out, the activity worker attempts to contact Amazon SWF, such as by calling `RespondActivityTaskCompleted`, Amazon SWF will return an `UnknownResource` fault.

This section describes how to provide an activity heartbeat.

To record an activity task heartbeat, program your activity worker to call the `RecordActivityTaskHeartbeat` action. This action also provides a
string field that you can use to store free-form data to quantify progress in whatever way
works for your application.

In this example, the activity worker reports heartbeat to Amazon SWF and uses the details field to report that
the activity task is 40 percent complete. To report heartbeat, the activity worker must specify the task token of
the activity task.

```
https://swf.us-east-1.amazonaws.com
RecordActivityTaskHeartbeat
{
  "taskToken" : "12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "details" : "40"
}
```

This action doesn't in itself create an event in the workflow execution history; however, if the task times
out, the workflow execution history will contain a `ActivityTaskTimedOut` event that contains the
information from the last heartbeat generated by the activity worker.

## Completing or Failing an Activity Task

After executing a task, the activity worker should report whether the activity task completed or
failed.

### Completing an Activity Task

To complete an activity task, program the activity worker to call the `RespondActivityTaskCompleted` action after it successfully completes an activity
task, specifying the task token.

In this example, the activity worker indicates that the task completed successfully.

```
https://swf.us-east-1.amazonaws.com
RespondActivityTaskCompleted
{
  "taskToken": "12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "results": "40"
}
```

When the activity completes, Amazon SWF schedules a new decision task for the workflow execution with which
the activity is associated.

Program the activity worker to poll for another activity task after it has completed the task at hand.
This creates a loop where the activity worker continuously polls for and completes tasks.

If the activity doesn't respond within the _StartToCloseTimeout_ period, or if
_ScheduleToCloseTimeout_ has been exceeded, Amazon SWF times out the activity task and schedules
a decision task. This enables a decider to take an appropriate action, such as rescheduling the task.

For example, if an Amazon EC2 instance is executing an activity task and the instance fails before the
task is complete, the decider receives a timeout event in the workflow execution history. If the activity task
is using a heartbeat, the decider receives the event when the task fails to deliver the next heartbeat after
the Amazon EC2 instance fails. If not, the decider eventually receives the event when the activity task fails to
complete before it hits one of its overall timeout values. It is then up to the decider to re-assign the task
or take some other action.

### Failing an Activity Task

If an activity worker can't perform an activity task for some reason, but it can still communicate with
Amazon SWF, you can program it to fail the task.

To program an activity worker to fail an activity task, program the activity worker to call the `RespondActivityTaskFailed` action that specifies the task token of the task.

```
https://swf.us-east-1.amazonaws.com
RespondActivityTaskFailed
{
  "taskToken" : "12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "reason" : "CC-Invalid",
  "details" : "Credit Card Number Checksum Failed"
}
```

As the developer, you define the values that are stored in the reason and details fields. These are
free-form strings; you can use any error code conventions that serve your application. Amazon SWF doesn't process
these values. However, Amazon SWF may display these values in the console.

When an activity task is failed, Amazon SWF schedules a decision task for the workflow execution with which
the activity task is associated to inform the decider of the failure. Program your decider to handle failed
activities, such as by rescheduling the activity or failing the workflow execution, depending on the nature of
the failure.

## Launching Activity Workers

To launch activity workers, package your logic into an executable that you can use on your activity worker
platform. For example, you might package your activity code as a Java executable that you can run on both Linux and
Windows servers.

Once launched, your workers start polling for tasks. Until the decider schedules activity tasks, though, these
polls time out with no tasks and your workers just continue polling.

Because polls are outbound requests, activity worker can run on any network that has access to the Amazon SWF
endpoint.

You can launch as many activity workers as you like. As the decider schedules activity tasks, Amazon SWF
automatically distributes the activity tasks to the polling activity workers.
