# Performing drift detection on CloudFormation StackSets

Even as you manage your stacks and the resources they contain through CloudFormation, users
can change those resources outside of CloudFormation. Users can edit resources directly by using
the underlying service that created the resource. By performing drift detection on a StackSet, you can determine if any of the stack instances belonging to that StackSet differ, or
have _drifted_, from their expected configuration.

###### Topics

- [How CloudFormation performs drift detection on a
  StackSet](#stacksets-drift-how "#stacksets-drift-how")
- [Detect drift on a StackSet (console)](#stacksets-drift-console-procedure "#stacksets-drift-console-procedure")
- [Detect drift on a StackSet (AWS CLI)](#stacksets-drift-cli-procedure "#stacksets-drift-cli-procedure")
- [Stopping drift detection on a StackSet](#stacksets-drift-stop "#stacksets-drift-stop")

## How CloudFormation performs drift detection on a

StackSet

When CloudFormation performs drift detection on a StackSet, it performs drift detection
on the stack associated with each stack instance in the StackSet. To do this,
CloudFormation compares the current state of each resource in the stack with the
expected state of that resource, as defined in the stack's template and any specified
input parameters. If the current state of a resource varies from its expected state,
that resource is considered to have drifted. If one or more resources in a stack have
drifted, then the stack itself is considered to have drifted, and the stack instances
that the stack is associated with is considered to have drifted as well. If one or more
stack instances in a StackSet have drifted, the StackSet itself is considered to have
drifted.

Drift detection identifies unmanaged changes; that is, changes made to stacks outside
of CloudFormation. Changes made through CloudFormation to a stack directly, rather than
at the StackSet level, aren't considered drift. For example, suppose you have a stack
that is associated with a stack instance of a StackSet. If you use CloudFormation to
update that stack to use a different template, that is not considered drift, even though
that stack now has a different template than any other stacks belonging to the StackSet. This is because the stack still matches its expected template and parameter
configuration in CloudFormation.

For detailed information on how CloudFormation performs drift detection on a stack, see
[Detect unmanaged configuration changes to stacks and
resources with drift detection](using-cfn-stack-drift.md "using-cfn-stack-drift.md").

Because CloudFormation performs drift detection on each stack individually, it takes
any overridden parameter values into account when determining whether a stack has
drifted. For more information on overriding template parameters in stack instances, see
[Override parameter values on stacks within
your CloudFormation StackSet](stackinstances-override.md "stackinstances-override.md").

If you perform drift detection [directly on a
stack](using-cfn-stack-drift.md "using-cfn-stack-drift.md") that is associated with a stack instance, those drift results aren't
available from the **StackSets** console page.

## Detect drift on a StackSet (console)

###### To detect drift on a StackSet

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **StackSets** page, select the StackSet on which you
   want to perform drift detection.
3. From the **Actions** menu, select **Detect
   drifts**.

CloudFormation displays an information bar stating that drift detection has
been initiated for the selected StackSet. 4. Optional: To monitor the progress of the drift detection operation:

    1. Select the StackSet name to display the **Stackset
     details** page.
    2. Select the **Operations** tab, select the drift
     detection operation, and then select **View drift
     details**.CloudFormation displays the **Operation details** dialog

box. 5. Wait until CloudFormation completes the drift detection operation. When the
drift detection operation completes, CloudFormation updates **Drift
status** and **Last drift check time** for your
StackSet. These fields are listed on the **Overview** tab of
the **StackSet details** page for the selected StackSet.

The drift detection operation may take some time, depending on the number of
stack instances included in the StackSet, and the number of resources included
in the StackSet. You can only run a single drift detection operation on a given
StackSet at one time. CloudFormation continues the drift detection operation
even after you dismiss the information bar. 6. To review the drift detection results for the stack instances in a StackSet,
select the **Stack instances** tab.

The **Stack name** column lists the name of the stack
associated with each stack instance, and the **Drift status**
column lists the drift status of that stack. A stack is considered to have
drifted if one or more of its resources have drifted. 7. To review the drift detection results for the stack associated with a specific
stack instance:

    1. Choose the **Operations** tab.
    2. Select the drift operation you want to view drift detection results
     for. A split panel will display the stack instance status and reason for
     the selected operation. For a drift operation, the status reason column
     shows the drift status of a stack instance.
    3. Choose the stack instance you want to view drift details for, and
     choose **View resource drifts**. In the
     **Resource drift status** table on the
     **Resource Drifts** page, each stack resource is
     listed with its drift status and the last time drift detection was
     initiated on the resource. The logical ID and physical ID of each
     resource is displayed to help you identify them.

8. You can sort the resources based on their drift status using the
   **Drift status** column.

To view the details on a modified resource:

    1. With the resource selected, choose **View drift
     details**.


    CloudFormation displays the drift detail page for that particular
     resource. This page lists the resource's differences. It also lists the
     resource's expected and current property values.


    ###### Note

    If the stack belongs to a different Region and account than the
     one you're currently signed into, the **Detect
     drift** button will be disabled and you will be unable
     to view the details.

## Detect drift on a StackSet (AWS CLI)

To detect drift on an entire stack using the AWS CLI, use the following procedure:

###### To detect drift on a StackSet

1. Use the [detect-stack-set-drift](../../../cli/latest/reference/cloudformation/detect-stack-set-drift.md "../../../cli/latest/reference/cloudformation/detect-stack-set-drift.md") command to detect drift on an entire StackSet
   and its associated stack instances.

The following example initiates drift detection on the StackSet
`stack-set-drift-example`.

```
aws cloudformation detect-stack-set-drift \
    --stack-set-name `stack-set-drift-example`
```

Output:

```
{
    "OperationId": "c36e44aa-3a83-411a-b503-cb611example"
}
```

2. Because StackSet drift detection operations can be a long-running operation,
   use the [describe-stack-set-operation](../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md "../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md") command to monitor the status of drift
   operation. This command takes the StackSet operation ID returned by the
   **detect-stack-set-drift** command.

The following examples uses the operation ID from the previous example to
return information on the StackSet drift detection operation. In this example,
the operation is still running. Of the seven stack instances associated with
this StackSet, one stack instance has already been found to have drifted, two
instances are in sync , and drift detection for the remaining four stack
instances is still in progress. Because one instance has drifted, the drift
status of the StackSet itself is now `DRIFTED`.

```
aws cloudformation describe-stack-set-operation \
    --stack-set-name `stack-set-drift-example` \
    --operation-id `c36e44aa-3a83-411a-b503-cb611example`
```

Output:

```
{
    "StackSetOperation": {
        "Status": "RUNNING",
        "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole",
        "OperationPreferences": {
            "RegionOrder": []
        },
        "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole",
        "StackSetDriftDetectionDetails": {
            "DriftedStackInstancesCount": 1,
            "TotalStackInstancesCount": 7,
            "LastDriftCheckTimestamp": "2019-12-04T20:34:28.543Z",
            "InSyncStackInstancesCount": 2,
            "InProgressStackInstancesCount": 4,
            "DriftStatus": "DRIFTED",
            "FailedStackInstancesCount": 0
        },
        "Action": "DETECT_DRIFT",
        "CreationTimestamp": "2019-12-04T20:33:13.673Z",
        "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22example",
        "OperationId": "c36e44aa-3a83-411a-b503-cb611example"
    }
}
```

Performing the same command later, this example shows the information returned
once the drift detection operation has completed. Two of the seven total stack
instances associated with this StackSet have drifted, rendering the drift
status of the StackSet itself as `DRIFTED`.

```
aws cloudformation describe-stack-set-operation \
    --stack-set-name `stack-set-drift-example` \
    --operation-id `c36e44aa-3a83-411a-b503-cb611example`
```

Output:

```
{
    "StackSetOperation": {
        "Status": "SUCCEEDED",
        "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole",
        "OperationPreferences": {
            "RegionOrder": []
        }
        "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole",
        "EndTimestamp": "2019-12-04T20:37:32.829Z",
        "StackSetDriftDetectionDetails": {
            "DriftedStackInstancesCount": 2,
            "TotalStackInstancesCount": 7,
            "LastDriftCheckTimestamp": "2019-12-04T20:36:55.612Z",
            "InSyncStackInstancesCount": 5,
            "InProgressStackInstancesCount": 0,
            "DriftStatus": "DRIFTED",
            "FailedStackInstancesCount": 0
        },
        "Action": "DETECT_DRIFT",
        "CreationTimestamp": "2019-12-04T20:33:13.673Z",
        "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22example",
        "OperationId": "c36e44aa-3a83-411a-b503-cb611example"
    }
}
```

3. When the StackSet drift detection operation is complete, use the
   **describe-stack-set**, **list-stack-instances**,
   **describe-stack-instance**, and
   **list-stack-instance-resource-drifts** commands to review the
   results.

The [describe-stack-set](../../../cli/latest/reference/cloudformation/describe-stack-set.md "../../../cli/latest/reference/cloudformation/describe-stack-set.md") command includes the same detailed drift
information returned by the **describe-stack-set-operation**
command.

```
aws cloudformation describe-stack-set \
    --stack-set-name `stack-set-drift-example`
```

Output:

```
{
    "StackSet": {
        "Status": "ACTIVE",
        "Description": "Demonstration of drift detection on stack sets.",
        "Parameters": [],
        "Tags": [
            {
                "Value": "Drift detection",
                "Key": "Feature"
            }
        ],
        "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole",
        "Capabilities": [],
        "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole",
        "StackSetDriftDetectionDetails": {
            "DriftedStackInstancesCount": 2,
            "TotalStackInstancesCount": 7,
            "LastDriftCheckTimestamp": "2019-12-04T20:36:55.612Z",
            "InProgressStackInstancesCount": 0,
            "DriftStatus": "DRIFTED",
            "DriftDetectionStatus": "COMPLETED",
            "InSyncStackInstancesCount": 5,
            "FailedStackInstancesCount": 0
        },
        "StackSetARN": "arn:aws:cloudformation:us-east-1:123456789012:stackset/stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22example",
        "TemplateBody": [details omitted],
        "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22ebexample",
        "StackSetName": "stack-set-drift-example"
    }
}
```

You can use the [list-stack-instances](../../../cli/latest/reference/cloudformation/list-stack-instances.md "../../../cli/latest/reference/cloudformation/list-stack-instances.md") command to return summary
information about the stack instances associated with a StackSet, including the
drift status of each stack instance.

In this example, executing **list-stack-instances** on the example
StackSet with the drift status filter set to `DRIFTED` enables you
to identify which two stack instances have a drift status of
`DRIFTED`.

```
aws cloudformation list-stack-instances \
    --stack-set-name `stack-set-drift-example` \
    --filters `Name=DRIFT_STATUS,Values=DRIFTED`
```

Output:

```
{
"Summaries": [
        {
"StackId": "arn:aws:cloudformation:eu-west-1:123456789012:stack/StackSet-stack-set-drift-example-b0fb6083-60c0-4e39-af15-2f071e0db90c/0e4f0940-16d4-11ea-93d8-0641cexample",
            "Status": "CURRENT",
            "Account": "012345678910",
            "Region": "eu-west-1",
            "LastDriftCheckTimestamp": "2019-12-04T20:37:32.687Z",
            "DriftStatus": "DRIFTED",
            "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22eexample",
            "LastOperationId": "c36e44aa-3a83-411a-b503-cb611example"
        },
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/StackSet-stack-set-drift-example-b7fde68e-e541-44c2-b33d-ef2e2988071a/008e6030-16d4-11ea-8090-12f89example",
            "Status": "CURRENT",
            "Account": "123456789012",
            "Region": "us-east-1",
            "LastDriftCheckTimestamp": "2019-12-04T20:34:28.275Z",
            "DriftStatus": "DRIFTED",
            "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22eexample",
            "LastOperationId": "c36e44aa-3a83-411a-b503-cb611example"
        },

        `[additional stack instances omitted]`

    ]
}
```

The [describe-stack-instance](../../../cli/latest/reference/cloudformation/describe-stack-instance.md "../../../cli/latest/reference/cloudformation/describe-stack-instance.md") command also returns this
information, but for a single stack instance, as in the example below.

```
aws cloudformation describe-stack-instance \
    --stack-set-name `stack-set-drift-example` \
    --stack-instance-account `012345678910` --stack-instance-region `us-east-1`
```

Output:

```
{
    "StackInstance": {
        "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/StackSet-stack-set-drift-example-b7fde68e-e541-44c2-b33d-ef2e2988071a/008e6030-16d4-11ea-8090-12f89example",
        "Status": "CURRENT",
        "Account": "123456789012",
        "Region": "us-east-1",
        "ParameterOverrides": [],
        "DriftStatus": "DRIFTED",
        "LastDriftCheckTimestamp": "2019-12-04T20:34:28.275Z",
        "StackSetId": "stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22eexample",
        "LastOperationId": "c36e44aa-3a83-411a-b503-cb611example"
    }
}
```

4. Once you've identified which stack instances have drifted, you can use the
   information about the stack instances that is returned by the
   **list-stack-instances** or **describe-stack-instance**
   commands to run the [list-stack-instance-resource-drifts](../../../cli/latest/reference/cloudformation/list-stack-instance-resource-drifts.md "../../../cli/latest/reference/cloudformation/list-stack-instance-resource-drifts.md") command. This
   command returns detailed information about which resources in the stack have
   drifted for a particular drift operation.

The following example uses the
`--stack-instance-resource-drift-statuses` parameter to request
stack drift information for the resources that have been modified or deleted in
the previous drift operation example. The request returns information on the one
resource that has been modified, including details about two of its properties
and their changed values. No resources have been deleted.

```
aws cloudformation list-stack-instance-resource-drifts \
    --stack-set-name `my-stack-set-with-resource-drift` \
    --stack-instance-account `123456789012` \
    --stack-instance-region `us-east-1` \
    --operation-id `c36e44aa-3a83-411a-b503-cb611example` \
    --stack-instance-resource-drift-statuses `MODIFIED DELETED`
```

Output:

```
{
    "Summaries": [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/my-stack-set-with-resource-drift/489e5570-df85-11e7-a7d9-50example",
            "ResourceType": "AWS::SQS::Queue",
            "Timestamp": "2018-03-26T17:23:34.489Z",
            "PhysicalResourceId": "https://sqs.us-east-1.amazonaws.com/123456789012/my-stack-with-resource-drift-Queue-494PBHCO76H4",
            "StackResourceDriftStatus": "MODIFIED",
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

## Stopping drift detection on a StackSet

Because drift detection on a StackSet can be a long-running operation, there may be
instances when you want to stop a drift detection operation that is currently running on
a StackSet.

###### To stop drift detection on a

StackSet (console)

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **StackSets** page, select the name of the StackSet.

CloudFormation displays the **StackSets details** page for the
selected StackSet. 3. On the **StackSets details** page, select the
**Operations** tab, and then select the drift detection
operation. 4. Select **Stop operation**.

###### To stop drift detection on a StackSet (AWS CLI)

- Use the [stop-stack-set-operation](../../../cli/latest/reference/cloudformation/stop-stack-set-operation.md "../../../cli/latest/reference/cloudformation/stop-stack-set-operation.md") command. You must
  supply both the StackSet name and the operation ID of the drift detection StackSet operation.

```
aws cloudformation stop-stack-set-operation \
    --stack-set-name `stack-set-drift-example` \
    --operation-id `624af370-311a-11e8-b6b7-500cexample`
```
