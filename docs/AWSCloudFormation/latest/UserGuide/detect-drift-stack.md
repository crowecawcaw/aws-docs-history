# Detect drift on an entire CloudFormation stack

Performing a drift detection operation on a stack determines whether the stack has
drifted from its expected template configuration, and returns detailed information about
the drift status of each resource in the stack that supports drift detection.

###### To detect drift on an entire

stack using the AWS Management Console

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the list of stacks, select the stack on which you want to perform drift
   detection. In the stack details pane, choose **Stack actions**,
   and then choose **Detect drift**.

![The Detect drift for current stack command selected on the Stack actions menu for the selected stack.](images/console-stacks-actions-detect-drift-1.png)

CloudFormation displays an information bar stating that drift detection has been
initiated for the selected stack. 3. Wait until CloudFormation completes the drift detection operation. When the drift
detection operation completes, CloudFormation updates **Drift
status** and **Last drift check time** for your
stack. These fields are listed in the **Overview** section of
the **Stack info** pane of the stack details page.

The drift detection operation may take several minutes, depending on the
number of resources included in the stack. You can only run a single drift
detection operation on a given stack at the same time. CloudFormation continues the
drift detection operation even after you dismiss the information bar. 4. Review the drift detection results for the stack and its resources. With your
stack selected, from the **Stack actions** menu select
**View drift results**.

CloudFormation lists the overall drift status of the stack, in addition to the
last time drift detection was initiated on the stack or any of its individual
resources. A stack is considered to have drifted if one or more of its resources
have drifted.

![The Drifts page for the selected stack, showing overall stack drift status, drift detection status, and the last time drift detection was initiated on the stack or any of its individual resources.](images/console-stacks-drifts-overview-1.png)

In the **Resource drift status** section, CloudFormation lists
each stack resource, its drift status, and the last time drift detection was
initiated on the resource. The logical ID and physical ID of each resource is
displayed to help you identify them. In addition, for resources with a status of
**MODIFIED**, CloudFormation displays resource drift
details.

You can sort the resources based on their drift status using the
**Drift status** column.

    1. To view the details on a modified resource.


    	1. With the modified resource selected, select **View
    	 drift details**.


    	CloudFormation displays the drift detail page for that resource.
    	 This page lists the resource's expected and current property
    	 values, and any differences between the two.


    	To highlight a difference, in the
    	 **Differences** section select the property
    	 name.




    		* Added properties are highlighted in green in the
    		 **Current** column of the
    		 **Details** section.
    		* Deleted properties are highlighted in red in the
    		 **Expected** column of the
    		 **Details** section.
    		* Properties whose value have been changed are
    		 highlighted in yellow in the both
    		 **Expected** and
    		 **Current** columns.

![The Resource drift status section of the Drift Details page, which contains drift information for each resource in the stack that supports drift detection. Details include drift status and expected and current property values.](images/console-stacks-drifts-drift-details-differences-1.png)

###### To detect drift on an entire stack

using the AWS CLI

###### Important

Review the **Last drift check time** for the stack and confirm that it's earlier than the timestamp shown in the resource drift results to prevent the use of stale data.

To detect drift on an entire stack using the AWS CLI, use the following AWS CLI commands:

- **detect-stack-drift** to initiate a drift detection operation on
  a stack.
- **describe-stack-drift-detection-status** to monitor the status
  of the stack drift detection operation.
- **describe-stack-resource-drifts** to review the details of the
  stack drift detection operation.

1. Use the **detect-stack-drift** to detect drift on an entire stack.
   Specify the stack name or ARN. You can also specify the logical IDs of any
   specific resources that you want to use as filters for this drift detection
   operation.

```
aws cloudformation detect-stack-drift --stack-name `my-stack-with-resource-drift`
```

Output:

```
{
    "StackDriftDetectionId": "624af370-311a-11e8-b6b7-500cexample"
}
```

2. Because stack drift detection operations can be long-running, use
   **describe-stack-drift-detection-status** to monitor the status of
   drift operation. This command takes the stack drift detection ID returned by the
   **detect-stack-drift** command.

In the example below, we've taken the stack drift detection ID returned by the
**detect-stack-drift** example above and passed it as a parameter
to **describe-stack-drift-detection-status**. The parameter returns
operation details that show that the drift detection operation has completed, a
single stack resource has drifted, and that the entire stack is considered to
have drifted as a result.

```
aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id `624af370-311a-11e8-b6b7-500cexample`
```

Output:

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:099908667365:stack/my-stack-with-resource-drift/489e5570-df85-11e7-a7d9-50example",
    "StackDriftDetectionId": "624af370-311a-11e8-b6b7-500cexample",
    "StackDriftStatus": "DRIFTED",
    "Timestamp": "2018-03-26T17:23:22.279Z",
    "DetectionStatus": "DETECTION_COMPLETE",
    "DriftedStackResourceCount": 1
}
```

3. When the stack drift detection operation is complete, use the
   **describe-stack-resource-drifts** command to review the results,
   including actual and expected property values for resources that have
   drifted.

The example below uses the `--stack-resource-drift-status-filters`
option to request stack drift information for those resources that have been
modified or deleted. The request returns information on the one resource that
has been modified, including details about two of its properties whose values
have been changed. No resources have been deleted.

```
aws cloudformation describe-stack-resource-drifts --stack-name `my-stack-with-resource-drift` --stack-resource-drift-status-filters MODIFIED DELETED
```

Output:

```
{
    "StackResourceDrifts": [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:099908667365:stack/my-stack-with-resource-drift/489e5570-df85-11e7-a7d9-50example",
            "ActualProperties": "{\"ReceiveMessageWaitTimeSeconds\":0,\"DelaySeconds\":120,\"RedrivePolicy\":{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:099908667365:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3\",\"maxReceiveCount\":12},\"MessageRetentionPeriod\":345600,\"MaximumMessageSize\":262144,\"VisibilityTimeout\":60,\"QueueName\":\"my-stack-with-resource-drift-Queue-494PBHCO76H4\"}",
            "ResourceType": "AWS::SQS::Queue",
            "Timestamp": "2018-03-26T17:23:34.489Z",
            "PhysicalResourceId": "https://sqs.us-east-1.amazonaws.com/099908667365/my-stack-with-resource-drift-Queue-494PBHCO76H4",
            "StackResourceDriftStatus": "MODIFIED",
            "ExpectedProperties": "{\"ReceiveMessageWaitTimeSeconds\":0,\"DelaySeconds\":20,\"RedrivePolicy\":{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:099908667365:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3\",\"maxReceiveCount\":10},\"MessageRetentionPeriod\":345600,\"MaximumMessageSize\":262144,\"VisibilityTimeout\":60,\"QueueName\":\"my-stack-with-resource-drift-Queue-494PBHCO76H4\"}",
            "PropertyDifferences": [
                {
                    "PropertyPath": "/DelaySeconds",
                    "ActualValue": "120",
                    "ExpectedValue": "20",
                    "DifferenceType": "NOT_EQUAL"
                },
                {
                    "PropertyPath": "/RedrivePolicy/maxReceiveCount",
                    "ActualValue": "12",
                    "ExpectedValue": "10",
                    "DifferenceType": "NOT_EQUAL"
                }
            ],
            "LogicalResourceId": "Queue"
        }
    ]
}
```
