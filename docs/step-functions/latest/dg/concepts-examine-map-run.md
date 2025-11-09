# Viewing a Distributed Map Run execution in

Step Functions

The Step Functions console provides a _Map Run Details_ page which displays
all the information related to a _Distributed Map state_ execution. For example, you can view the status
of the _Distributed Map state_'s execution, the Map Run's ARN, and the statuses of the items processed
in the child workflow executions started by the _Distributed Map state_. You can also view a list of all
child workflow executions and access their details. If your Map Run was [redriven](redrive-map-run.md "redrive-map-run.md"), you will see redrive details in the Map Run execution summary too.

When you run a `Map` state in Distributed mode, Step Functions creates a Map Run resource. A Map Run refers to a set of child workflow executions that a _Distributed Map state_ starts, and the runtime settings that control these executions. Step Functions assigns an Amazon Resource Name (ARN) to your Map Run. You can examine a Map Run in the Step Functions console. You can also invoke the `DescribeMapRun` API action.

Child workflow executions of a Map Run emit metrics to CloudWatch;. These metrics will have a labelled State Machine ARN with the following format:

`arn:`partition`:states:`region`:`account`:stateMachine:`stateMachineName`/`MapRunLabel or UUID``

The _Map Run Details_ has three sections: _Map Run execution summary_, _Item processing status_, and _Listing executions_.

## Map Run execution summary

The _Map Run Execution summary_ provides an overview of the execution details of the _Distributed Map state_.

**Details**
Shows execution status of the _Distributed Map state_, the Map Run ARN, and type of the child workflow executions started by the _Distributed Map state_. You can view additional configurations, such as tolerated failure threshold for the Map Run and the maximum concurrency specified for child workflow executions.

**Input and output**
Shows the input received by the _Distributed Map state_ and the corresponding output that it generates.

You can view the input dataset and its location, and the input
filters applied to the individual data items in that dataset. If you export
the output of the _Distributed Map state_ execution, this tab shows the path to the Amazon S3
bucket that contains the execution results. Otherwise, it points you to the
parent workflow's _Execution Details_ page to view the
execution output.

## Error message

If your Map Run failed, the _Map Run Details_ page displays an
error message with the reason for failure.

From the **Recover** dropdown button on this error message, you can either redrive the unsuccessful child workflow executions started by this Map Run or start a new execution of the parent workflow.

See [Redriving Map Runs](redrive-map-run.md "redrive-map-run.md") to learn how to restart your workflow.

## Item processing status

The **Item processing status** section displays the status of the
items processed in a Map Run. For example, **Pending** indicates that
a child workflow execution hasn’t started processing the item yet.

Item statuses are dependent on the status of the child workflow executions processing
the items. If a child workflow execution failed, times out, or if a user cancels the
execution, Step Functions doesn't receive any information about the processing result of the
items inside that child workflow execution. All items processed by that execution share
the child workflow execution's status.

For example, say that you want to process 100 items in two child workflow executions,
where each execution processes a batch of 50 items. If one of the executions fails and
the other succeeds, you'll have 50 successful and 50 failed items.

The following table explains the types of processing statuses available for all
items:

| Status        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pending**   | Indicates an item that the child workflow execution hasn't started<br>processing. If a Map Run stops, fails, or a user cancels the<br>execution before processing of an item starts, the item remains in<br>**Pending\*<br>• status.<br>For example, if a Map Run fails with 10 unprocessed items, these 10 items remain in the **Pending\*<br>• status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Running**   | Indicates an item currently being processed by the child workflow<br>execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Succeeded** | Indicates that the child workflow execution successfully processed<br>the item.<br>A successful child workflow execution can't have any failed items.<br>If one item in the dataset fails during execution, the entire child<br>workflow execution fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Failed**    | Indicates that the child workflow execution either failed to<br>process the item, or the execution timed out. If any one item<br>processed by a child workflow execution fails, the entire child<br>workflow execution fails.<br>For example, consider a child workflow execution that processed<br>1000 items. If any one item in that dataset fails during execution,<br>then Step Functions considers the entire child workflow execution as<br>failed.<br>When you [redrive](redrive-map-run.md "redrive-map-run.md") a Map Run, the count of items<br>with this status is reset to 0.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Aborted**   | Indicates that the child workflow execution started processing the<br>item, but either the user cancelled the execution, or Step Functions stopped<br>the execution because the Map Run failed.<br>For example, consider a **Running\*<br>• child<br>workflow execution that's processing 50 items. If the Map Run<br>stops because of a failure or because a user cancelled the<br>execution, the child workflow execution and the status of all 50<br>items changes to **Aborted**.<br>If<br>you use a child workflow execution of the<br>**Express\*<br>• type, you can't stop the<br>execution.<br>When you [redrive](redrive-map-run.md "redrive-map-run.md") a Map Run that starts child workflow executions of type Express, the count of items with this status is reset to 0. This is because Express child workflows are restarted using the [StartExecution](../apireference/API_StartExecution.md "../apireference/API_StartExecution.md") API action instead of being redriven. |

## Listing executions

The **Executions** section lists all of the child workflow executions
for a specific Map Run. Use the **Search by exact execution name**
field to search for a specific child workflow execution. To see details about a specific execution, select a child
workflow execution from the list and choose the **View details** button
to open its [Execution details](concepts-view-execution-details.md "concepts-view-execution-details.md") page.

You can also use the API or AWS CLI to list child workflow executions started by the Map Run:

- Using the API, call [ListExecutions](../apireference/API_ListExecutions.md "../apireference/API_ListExecutions.md") with the `mapRunArn` parameter set to the ARN of the parent workflow.
- Using the AWS CLI, call [list-executions](../../../cli/latest/reference/stepfunctions/list-executions.md "../../../cli/latest/reference/stepfunctions/list-executions.md") with the `map-run-arn` parameter set to the ARN of the parent workflow.

###### Important

The retention policy for child workflow executions is 90 days.

Completed child
workflow executions that are older will not be displayed in
the **Executions** table, even if the _Distributed Map state_ or
parent workflow continues to run longer than the retention period. You can view
execution details, including results, of these child workflow executions if you
export the _Distributed Map state_ output to an Amazon S3 bucket using `ResultWriter (Map)`.

###### Tip

Choose the refresh button to view the most current list of all child workflow
executions.
