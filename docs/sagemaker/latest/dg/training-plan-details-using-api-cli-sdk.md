# View training plan details

To monitor the status or retrieve details of a training plan, you can use the [`DescribeTrainingPlan`](../APIReference/API_DescribeTrainingPlan.md "../APIReference/API_DescribeTrainingPlan.md") API. The API response includes a
`Status` field, which reflects the current state of the training plan:

- If the plan purchase fails, the status is set to `Failed`.
- Upon successful payment, the status transitions from `Pending` to
  `Scheduled`, based on the plan's start date.
- When the plan reaches its start date, the status changes to
  `Active`.
- For plans with multiple discontinuous reserved capacities, the status reverts to
  `Scheduled` between active periods, until the start date of the next
  reserved capacity.
- After the plan's end date, the status becomes `Expired`.
  Once the status is `Scheduled`, you can utilize the capacity reserved in the
  plan for your SageMaker training jobs or HyperPod cluster workloads.

###### Note

- Training jobs associated with the plan remain in `Pending` status until
  the plan becomes `Active`.
- For HyperPod clusters using a training plan for compute capacity, the
  instance group status appears as `InService` once created.
  The following example uses an AWS CLI command to retrieve the details of a training plan
  by its name.

```
aws sagemaker describe-training-plan \
--training-plan-name "`name`"
```

This JSON document is a sample response from the SageMaker training plans API. This response
provides details about a training plan that has been successfully created.

```
      {
         "AvailableInstanceCount": 2,
         "CurrencyCode": "USD",
         "DurationHours": 48,
         "DurationMinutes": 0,
         "EndTime": "2024-09-28T04:30:00-07:00",
         "InUseInstanceCount": 2,
         "ReservedCapacitySummaries": [
            {
               "AvailabilityZone": "string",
               "DurationHours": 48,
               "DurationMinutes": 0,
               "EndTime": "2024-09-28T04:30:00-07:00",
               "InstanceType": "ml.p5.48xlarge",
               "ReservedCapacityArn": "arn:aws:sagemaker:us-east-1:123456789123:reserved-capacity/large-models-fine-tuning-rc1",
               "StartTime": "2024-09-26T04:30:00-07:00",
               "Status": "Scheduled",
               "TotalInstanceCount": 4,
               "UltraServerCount": 4,
               "UltraServerType": "ml.p6e-gb200.36xlarge"
            }
         ],
         "StartTime": "2024-09-26T04:30:00-07:00",
         "Status": "Scheduled",
         "StatusMessage": "Payment confirmed, training plan scheduled."
         "TargetResources": [ "training-job" ],
         "TotalInstanceCount": 4,
         "TotalUltraServerCount": 4,
         "TrainingPlanArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/large-models-fine-tuning",
         "TrainingPlanName": "large-models-fine-tuning",
         "UpfrontFee": "xxxx.xx"
      }
```

The following sections define the mandatory input request parameter for the
`DescribeTrainingPlan` API operation.

## Required parameters

- `TrainingPlanName`: The name of the training plan you want to
  describe.
