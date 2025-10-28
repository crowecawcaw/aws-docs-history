# Signals

Signals enable you to inject information into a running workflow execution. In some scenarios, you might
want to add information to a running workflow execution to let it know that something has changed or to inform it
of an external event. Any process can send a signal to an open workflow execution. For example, one workflow
execution might signal another.

###### Note

An attempt to send a signal to a workflow execution that isn't open results in
`SignalWorkflowExecution` failing with `UnknownResourceFault`.

To use signals, define the signal name and data to be passed to the signal—if any. Then, program the
decider to recognize the signal event ([WorkflowExecutionSignaled](../apireference/API_WorkflowExecutionSignaledEventAttributes.md "../apireference/API_WorkflowExecutionSignaledEventAttributes.md")) in the history and process it
appropriately. When a process wants to signal a workflow execution, it makes a call to Amazon SWF (using the [SignalWorkflowExecution](../apireference/API_SignalWorkflowExecution.md "../apireference/API_SignalWorkflowExecution.md") action or, in the case of a
decider, using the [SignalExternalWorkflowExecution](../apireference/API_SignalExternalWorkflowExecutionInitiatedEventAttributes.md "../apireference/API_SignalExternalWorkflowExecutionInitiatedEventAttributes.md") decision) that specifies
the identifier for the target workflow execution, the signal name, and the signal data. Amazon SWF then receives the
signal, records it in the history of the target workflow execution, and schedules a decision task for it. When
the decider receives the decision task, it also receives the signal inside the workflow execution history. The
decider can then take appropriate actions based on the signal and its data.

Sometimes you might want to wait for a signal. For example, a user could cancel an order by sending a signal,
but only within one hour of placing the order. Amazon SWF doesn't have a primitive to enable a decider to wait for a
signal from the service. Pause functionality needs to be implemented in the decider itself. In order to pause, the
decider should start a timer, using the `StartTimer` decision, which specifies the duration for which the
decider will wait for the signal while continuing to poll for decision tasks. When the decider receives a decision
task, it should check the history to see if either the signal has been received or the timer has fired. If the
signal has been received, then the decider should cancel the timer. However, if instead, the timer has fired, then
it means that the signal did not arrive within the specified time. To summarize, in order to wait for a specific
signal, do the following.

1. Create a timer for the amount of time the decider should wait.
2. When a decision task is received, check the history to see if the signal has arrived or if the timer has
   fired.
3. If a signal has arrived, cancel the timer using a `CancelTimer` decision and process the signal.
   Depending on the timing, the history may contain both `TimerFired` and
   `WorkflowExecutionSignaled` events. In such cases, you can rely on the relative order of the events
   in the history to determine which occurred first.
4. If the timer has fired, before a signal is received, then the decider has timed out waiting for the signal.
   You can fail the execution or do whatever other logic is appropriate to your use case.
   For cases in which a workflow should be canceled—for example, the order itself was canceled by the
   customer—the `RequestCancelWorkflowExecution` action should be used rather than sending a signal
   to the workflow.

Some applications for signals include the following:

- Pausing workflow executions from progressing until a signal is received (e.g., waiting for an
  inventory shipment).
- Providing information to a workflow execution that might affect the logic of how deciders make
  decisions. This is useful for workflows affected by external events (e.g., trying to finish the sale of a
  stock after the market closes).
- Updating a workflow execution when you anticipate that changes might occur (e.g., changing order
  quantities after an order is placed and before it ships).
  In the following example, the workflow execution is sent a signal to cancel an order.

```
https://swf.us-east-1.amazonaws.com
SignalWorkflowExecution
{"domain": "867530901",
 "workflowId": "20110927-T-1",
 "runId": "f5ebbac6-941c-4342-ad69-dfd2f8be6689",
 "signalName": "CancelOrder",
 "input": "order 3553"}
```

If the workflow execution receives the signal, Amazon SWF returns a successful HTTP response similar to the
following. Amazon SWF will generate a decision task to inform the decider to process the signal.

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: bf78ae15-3f0c-11e1-9914-a356b6ea8bdf
```
