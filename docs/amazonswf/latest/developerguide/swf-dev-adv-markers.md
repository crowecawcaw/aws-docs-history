# Markers in Amazon SWF

At times, you might want to record information in the workflow history of a workflow execution that is
specific to your use case. Markers enable you to record information in the workflow execution history that you can
use for any custom or scenario-specific purpose.

To use markers, a decider uses the RecordMarker decision, names the marker, attaches desired data to the
decision, and notifies Amazon SWF using the `RespondDecisionTaskCompleted` action. Amazon SWF receives the
request, records the marker in the workflow history, and enacts any other decisions in the request. From that
point on, deciders can see the marker in the workflow history and use it in any way that you program.

Recording a marker doesn't, by itself, initiate a decision task. To prevent the workflow execution from
becoming stuck, something must occur that continues the execution of the workflow. For example, this might include
the decider scheduling another activity task, the workflow execution receiving a signal, or a previously scheduled
activity task completing.

Examples of markers include the following:

- A counter that counts the number of loops in a recursive workflow.
- Progress of the workflow execution based on the results of activities.
- Information summarized from earlier workflow history events.
  In the e-commerce example, you might add an activity that checks the inventory every day and increments the
  count in a marker each time. Then, you could add decision logic that emails the customer or notifies a manager
  when the count exceeds five, without having to review the entire history.

In the following example, the decider completes a decision task and responds with a
`RespondDecisionTaskCompleted` action that contains a `RecordMarker` decision.

```
https://swf.us-east-1.amazonaws.com
RespondDecisionTaskCompleted
{
  "taskToken":"12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "decisions":[{
          "decisionType":"RecordMarker",
          "recordMarkerDecisionAttributes":{
              "markerName":"customer elected special shipping offer"
          }
      },
  ]
}
```

If Amazon SWF successfully records the marker, it returns a successful HTTP response similar to the following.

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 6c0373ce-074c-11e1-9083-8318c48dee96
```
