# List training plans

You can list all the training plans that have been created in your AWS account and
Region by calling the [`ListTrainingPlans`](../APIReference/API_ListTrainingPlans.md "../APIReference/API_ListTrainingPlans.md") API.

The following example uses an AWS CLI command to retrieve the list of your training
plans.

```
aws sagemaker list-training-plans \
--start-time-after "2024-09-26T00:00:01.000Z"
```

This JSON document is a sample response from the SageMaker training plans API. The response
provides details about one training plan that has been successfully created and
reserved.

```
{
   "TrainingPlanSummaries": [
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
   ]
}
```

The following sections provide details of some optional parameters that you can pass to
your `ListTrainingPlans` API request.

## Optional parameters

The following sections provide details on some optional parameters that you can pass
to your `ListTrainingPlans` API request.

- `StartTimeAfter`: The start time of the actual time range of the listed
  plans, specified as a `timestamp` or an `ISO 8601 date/time`.
- `StartTimeBefore`: The end time of the actual time range of the listed
  plans, specified as a `timestamp` or an `ISO 8601 date/time`.
- `Filters`: Criteria used to filter the results, with up to 5 Name-Value
  pairs where "Name" is the name of a field of a [TrainingPlanSummary](../APIReference/API_TrainingPlanSummary.md "../APIReference/API_TrainingPlanSummary.md") and "Value" is the value to consider for the filter.
  For example `Name=Status,Value=Active`.

The following example uses an AWS CLI command to retrieve your list of training plans,
using some of the optional parameters described above.

```
aws sagemaker list-training-plans --max-results 10 --sort-by StartTime --sort-order Descending --start-time-after 13000000 --filters Name=Status,Value=Active
```
