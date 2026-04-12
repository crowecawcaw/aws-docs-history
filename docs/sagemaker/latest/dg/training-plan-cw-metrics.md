# Monitor capacity reservation usage with Amazon CloudWatch metrics

You can use [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") metrics to
monitor the utilization of capacity reservations associated with your SageMaker training plans. This
feature provides access to both historical and real-time metrics on instance usage—at the
individual plan level and across all plans in your account—so you can make informed decisions
about capacity and cost. These metrics will be published directly in your account, and the
SageMaker training plans service will not have access to them.

## Onboarding considerations

The `AWSServiceRoleForSageMakerCapacityReservation` service-linked role (SLR)
must exist in your account for metrics to be published. You need to add the
`iam:CreateServiceLinkedRole` permission to your account role. SageMaker AI will
automatically set up the required SLR the next time you call
`CreateTrainingPlan`. Once the SLR is set up, CloudWatch metrics will be available
for new plan purchases.

The following statement needs to be added to your IAM policy:

```
{
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "iam:AWSServiceName": "capacityreservation.sagemaker.amazonaws.com"
        }
    }
}
```

###### Note

While the `Resource` field is set to `"*"` (required for
`CreateServiceLinkedRole`), the `Condition` block restricts this
permission to only create the SageMaker AI capacity reservation SLR. Furthermore, if the role is
deleted for some reason, it is recreated on the next `CreateTrainingPlan` call
through the API or the console.

### Manually creating service-linked role

You can also create the SLR through the AWS CLI instead of relying on SageMaker AI to set it up
by running the following command:

```
aws iam create-service-linked-role --aws-service-name capacityreservation.sagemaker.amazonaws.com
```

This command creates the `AWSServiceRoleForSageMakerCapacityReservation`
role in your account. For more information about service-linked roles, see [Using
service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md").

###### Important

The service starts publishing the metrics only after SLR is created. The plans purchased
before SLR creation will not show any older utilization data on CloudWatch.

## Capacity reservation usage metrics

SageMaker AI publishes the following metrics in the
`aws/sagemaker/CapacityReservations` namespace.

| Metric                   | Description                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| `UsedInstanceCount`      | The number of instances that are currently in use. Unit: Count                            |
| `AvailableInstanceCount` | The number of instances that are available. Unit: Count                                   |
| `TotalInstanceCount`     | The total number of instances in your training plan. Unit: Count                          |
| `InstanceUtilization`    | The percentage of reserved capacity instances that are currently in use. Unit:<br>Percent |

## Capacity reservation metric dimensions

You can use the following dimensions to filter the metrics.

| Dimension          | Description                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `ReservationName`  | Filters metrics by the name.                                                                                                         |
| `ComponentType`    | Filters metrics by SageMaker AI component, such as a SageMaker HyperPod Cluster, Training Job,<br>Inference endpoint, or Studio App. |
| `AvailabilityZone` | Filters metrics by Availability Zone.                                                                                                |
| `InstanceType`     | Filters metrics by instance type.                                                                                                    |
| `ReservationType`  | Filters metrics by reservation type (`TrainingPlan`).                                                                                |

## View Amazon CloudWatch metrics for capacity reservations

You can view capacity reservation metrics by using the Amazon CloudWatch console or the
AWS CLI.

###### To view capacity reservation metrics using the Amazon CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, then
   **All metrics**.
3. Choose the `aws/sagemaker/CapacityReservations` namespace.
4. Choose a metric dimension to filter by.
5. Select the check box next to a metric to graph it.

To list available metrics by using the AWS CLI, run the following command:

```
aws cloudwatch list-metrics --namespace "aws/sagemaker/CapacityReservations"
```
