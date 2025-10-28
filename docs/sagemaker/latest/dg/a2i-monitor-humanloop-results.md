# Monitor and Manage Your Human Loop

Once you've started a human review loop, you can check the results of tasks sent to the
loop and manage it using the [Amazon Augmented AI Runtime API](../../../augmented-ai/2019-11-07/APIReference/Welcome.md "../../../augmented-ai/2019-11-07/APIReference/Welcome.md").
Additionally, Amazon A2I integrates with Amazon EventBridge (also known as Amazon CloudWatch Events) to alert you
when a human review loop status changes to `Completed`, `Failed`, or
`Stopped`. This event delivery is guaranteed at least once, which means all
events created when human loops finish are successfully delivered to EventBridge.

Use the procedures below to learn how to use the Amazon A2I Runtime API to monitor and
manage your human loops. See [Use Amazon CloudWatch Events in
Amazon Augmented AI](a2i-cloudwatch-events.md "a2i-cloudwatch-events.md") to learn how Amazon A2I integrates with
Amazon EventBridge.

###### To check your output data:

1. Check the results of your human loop by calling the [`DescribeHumanLoop`](../../../augmented-ai/2019-11-07/APIReference/API_DescribeHumanLoop.md "../../../augmented-ai/2019-11-07/APIReference/API_DescribeHumanLoop.md") operation. The result of this API
   operation contains information about the reason for and outcome of the loop
   activation.
2. Check the output data from your human loop in Amazon Simple Storage Service (Amazon S3). In the path to
   the data,
   ``YYYY`/`MM`/`DD`/`hh`/`mm`/`ss``
   represents the human loop creation date with year (`YYYY`), month
   (`MM`), and day (`DD`), and the creation time with hour
   (`hh`), minute (`mm`), and second (`ss`).

```
s3://`customer-output-bucket-specified-in-flow-definition`/`flow-definition-name`/`YYYY`/`MM`/`DD`/`hh`/`mm`/`ss`/`human-loop-name`/output.json

```

You can integrate this structure with AWS Glue or Amazon Athena to partition and analyze your
output data. For more information, see [Managing Partitions for
ETL Output in AWS Glue](../../../glue/latest/dg/aws-glue-programming-etl-partitions.md "../../../glue/latest/dg/aws-glue-programming-etl-partitions.md").

To learn more about Amazon A2I output data format, see [Amazon A2I Output Data](a2i-output-data.md "a2i-output-data.md").

###### To stop and delete your human loop:

1. Once a human loop has been started, you can stop your human loop by calling the
   [`StopHumanLoop`](../../../augmented-ai/2019-11-07/APIReference/API_StopHumanLoop.md "../../../augmented-ai/2019-11-07/APIReference/API_StopHumanLoop.md") operation using the
   `HumanLoopName`. If a human loop was successfully stopped, the server
   sends back an HTTP 200 response.
2. To delete a human loop for which the status equals `Failed`,
   `Completed`, or `Stopped`, use the [`DeleteHumanLoop`](../../../augmented-ai/2019-11-07/APIReference/API_DeleteHumanLoop.md "../../../augmented-ai/2019-11-07/APIReference/API_DeleteHumanLoop.md") operation.

###### To list human loops:

1. You can list all active human loops by calling the
   [`ListHumanLoops`](../../../augmented-ai/2019-11-07/APIReference/API_ListHumanLoops.md "../../../augmented-ai/2019-11-07/APIReference/API_ListHumanLoops.md") operation. You can filter human
   loops by the creation date of the loop using the `CreationTimeAfter` and
   `CreateTimeBefore` parameters.
2. If successful, `ListHumanLoops` returns [`HumanLoopSummaries`](../../../augmented-ai/2019-11-07/APIReference/API_HumanLoopSummary.md "../../../augmented-ai/2019-11-07/APIReference/API_HumanLoopSummary.md") and `NextToken` objects
   in the response element. `HumanLoopSummaries` contains information about
   a single human loop. For example, it
   lists
   a loop's status
   and,
   if applicable,
   its
   failure reason.

Use the string returned in `NextToken` as an input in a subsequent call
to `ListHumanLoops` to see the next page of human loops.
