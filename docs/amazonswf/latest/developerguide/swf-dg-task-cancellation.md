# Cancelling activity tasks in Amazon SWF

Activity task cancellation informs the decider to end activities that no longer need to be performed. Amazon SWF uses
a cooperative cancellation mechanism and doesn't forcibly interrupt running activity tasks. You must program your
activity workers to handle cancellation requests.

The decider can decide to cancel an activity task while it is processing a decision task. To cancel an activity
task, the decider uses the `RespondDecisionTaskCompleted` action with the
`RequestCancelActivityTask` decision.

If the activity task has not yet been acquired by an activity worker, the service will cancel the task. Note
that there is a potential race condition in that an activity worker could acquire the task at any time. If the task
has already been assigned to an activity worker, then the activity worker will be requested to cancel the
task.

In this example, the workflow execution is sent a signal to cancel the order.

```
https://swf.us-east-1.amazonaws.com
SignalWorkflowExecution
{"domain": "867530901",
 "workflowId": "20110927-T-1",
 "runId": "9ba33198-4b18-4792-9c15-7181fb3a8852",
 "signalName": "CancelOrder",
 "input": "order 3553"}
```

If the workflow execution receives the signal, Amazon SWF returns a successful HTTP response similar to the
following. Amazon SWF will generate a decision task to inform the decider to process the signal.

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 6c0373ce-074c-11e1-9083-8318c48dee96
```

When the decider processes the decision task and sees the signal in the history, the decider attempts to cancel
the outstanding activity that has the `ShipOrderActivity0001` activity ID. The activity ID is provided in
the workflow history from the schedule activity task event.

```
https://swf.us-east-1.amazonaws.com
RespondDecisionTaskCompleted
{
  "taskToken":"12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "decisions":[{
          "decisionType":"RequestCancelActivityTask",
          "RequestCancelActivityTaskDecisionAttributes":{
              "ActivityID":"ShipOrderActivity0001"
          }
      }
  ]
}
```

If Amazon SWF successfully receives the cancellation request, it returns a successful HTTP response similar to the
following:

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 6c0373ce-074c-11e1-9083-8318c48dee96
```

The cancellation attempt is recorded in the history as the `ActivityTaskCancelRequested`
event.

If the task is successfully canceled—as indicated by an `ActivityTaskCanceled`
event—program your decider to take the appropriate steps that should follow task cancellation such as closing
the workflow execution.

If the activity task could not be canceled—for example, if the task completes, fails, or times out instead
of canceling—your decider should accept the results of the activity or perform any cleanup or mitigation
necessitated by your use case.

If the activity task has already been acquired by an activity worker, then the request to cancel is transmitted
through the task-heartbeat mechanism. Activity workers can periodically use `RecordActivityTaskHeartbeat`
to report to Amazon SWF that the task is still in progress.

Note that activity workers are not required to heartbeat, although it is recommended for long-running tasks.
Task cancellation requires periodic heartbeat to be recorded; if the worker doesn't heartbeat, the task can't be
canceled.

If the decider requests a cancellation of the task, Amazon SWF sets the value of the `cancelRequest`
object to true. The `cancelRequest` object is part of the `ActivityTaskStatus` object which is
returned by the service in response to `RecordActivityTaskHeartbeat`.

Amazon SWF doesn't prevent the successful completion of an activity task whose cancellation has been requested; it
is up to the activity to determine how to handle the cancellation request. Depending on your requirements, program
the activity worker to either cancel the activity task or ignore the cancellation request.

If you want the activity worker to indicate that the work for the activity task was canceled, program it to
respond with a `RespondActivityTaskCanceled`. If you want the activity worker to complete the task,
program it to respond with a standard `RespondActivityTaskCompleted`.

When Amazon SWF receives the `RespondActivityTaskCompleted` or `RespondActivityTaskCanceled`
request, it updates the workflow execution history and schedules a decision task to inform the decider.

Program the decider to process the decision task and return any additional decisions. If the activity task is
successfully canceled, program the decider to perform the tasks needed to continue or close the workflow execution.
If the activity task isn't successfully canceled, program the decider to accept the results, ignore the results, or
schedule any required cleanup.
