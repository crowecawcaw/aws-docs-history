# Search training plan

offerings

To create a training plan, start by calling the [`SearchTrainingPlanOfferings`](../APIReference/API_SearchTrainingPlanOfferings.md "../APIReference/API_SearchTrainingPlanOfferings.md") API operation, passing your plan
requirements (such as instance type, count, and desired time window) as input parameters.
Training plans are specific to their target resource. Ensure that you specify which target
resource the plan will be used for (`training-job` or
`hyperpod-cluster`). The API returns a list of available offerings that match
your requirements. If no suitable offerings are found, you may need to adjust your
requirements and search again.

This API call retrieves the training plan offerings that best meet your capacity needs.
Each [`TrainingPlanOffering`](../APIReference/API_TrainingPlanOffering.md "../APIReference/API_TrainingPlanOffering.md") returned in the response is identified by a
unique offering ID. The first offering in the list represents the best match for your
requirements. If no suitable training plan is available within your specified dates, the
list is empty. Adjust your search criteria and look for a new set of offerings.

- Reservation durations are available in 1-day increments from 1 to 182 days.
- The reservation instance quantity options are 1, 2, 4, 8, 16, 32 or 64
  instances.
  To learn about the list of available instances supported by SageMaker training plans, see [Supported instance types,
  AWS Regions, and pricing](reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions "reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions").

The following example uses an AWS CLI command to request training plan offerings with a
specified instance type, count, and time information.

```
# List training plan offerings with instance type, instance count, duration in hours, start time after, and end time before.
aws sagemaker search-training-plan-offerings \
--target-resources "`training-job`" \
--instance-type "`ml.p4d.24xlarge`" \
--instance-count `1` \
--duration-hours `15` \
--start-time-after "`1737484800`"
--end-time-before "`1737657600`"
```

This JSON document is a sample response from the SageMaker training plans API. The response
provides information about multiple available training plan offerings that match the
specified capacity requirements. It includes three distinct offerings with varying
durations, upfront fees, and start/end times, all using the same instance type and targeting
training jobs.

```
{
    "TrainingPlanOfferings": [
        {
            "TrainingPlanOfferingId": "tpo-`SHA-256-hash-value`",
            "TargetResources": [
                "training-job"
            ],
            "RequestedStartTimeAfter": "2025-01-21T11:08:27.704000-08:00",
            "DurationHours": 15,
            "DurationMinutes": 51,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD",
            "ReservedCapacityOfferings": [
                {
                    "InstanceType": "ml.p4d.24xlarge",
                    "InstanceCount": 1,
                    "AvailabilityZone": "us-west-2a",
                    "DurationHours": 15,
                    "DurationMinutes": 51,
                    "StartTime": "2025-01-21T11:39:00-08:00",
                    "EndTime": "2025-01-22T03:30:00-08:00"
                }
            ]
        },
        {
            "TrainingPlanOfferingId": "tpo-`SHA-256-hash-value`",
            "TargetResources": [
                "training-job"
            ],
            "RequestedStartTimeAfter": "2025-01-21T11:08:27.704000-08:00",
            "DurationHours": 39,
            "DurationMinutes": 51,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD",
            "ReservedCapacityOfferings": [
                {
                    "InstanceType": "ml.p4d.24xlarge",
                    "InstanceCount": 1,
                    "AvailabilityZone": "us-west-2a",
                    "DurationHours": 39,
                    "DurationMinutes": 51,
                    "StartTime": "2025-01-21T11:39:00-08:00",
                    "EndTime": "2025-01-23T03:30:00-08:00"
                }
            ]
        },
        {
            "TrainingPlanOfferingId": "tpo-`SHA-256-hash-value`",
            "TargetResources": [
                "training-job"
            ],
            "RequestedStartTimeAfter": "2025-01-21T11:08:27.704000-08:00",
            "DurationHours": 24,
            "DurationMinutes": 0,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD",
            "ReservedCapacityOfferings": [
                {
                    "InstanceType": "ml.p4d.24xlarge",
                    "InstanceCount": 1,
                    "AvailabilityZone": "us-west-2a",
                    "DurationHours": 24,
                    "DurationMinutes": 0,
                    "StartTime": "2025-01-22T03:30:00-08:00",
                    "EndTime": "2025-01-23T03:30:00-08:00"
                }
            ]
        }
    ]
}
```

The following is a sample command of how to use the AWS CLI to search for training plan offerings that include UltraServers.

```
aws sagemaker search-training-plan-offerings \
--ultra-server-type ml.c6i-32xlargesc \
--ultra-server-count 1 \
--duration-hours 24 \
--target-resources hyperpod-cluster
--start-time-after "1737484800" \
--end-time-before "1737657600"
```

```
{
    "TrainingPlanOfferings": [
        {
            "TrainingPlanOfferingId": "tpo-`SHA-256-hash-value`",
            "TargetResources": [
                "training-job"
            ],
            "RequestedStartTimeAfter": "2025-07-21T16:59:25.760000+00:00",
            "DurationHours": 24,
            "DurationMinutes": 0,
            "UpfrontFee": "0.24",
            "CurrencyCode": "USD",
            "ReservedCapacityOfferings": [
                {
                    "ReservedCapacityType": "UltraServer",
                    "UltraServerType": "ml.u-p6e-gb200x72",
                    "UltraServerCount": 1,
                    "InstanceType": "ml.p6e-gb200.36xlarge",
                    "InstanceCount": 18,
                    "AvailabilityZone": "us-east-2a",
                    "DurationHours": 24,
                    "DurationMinutes": 0,
                    "StartTime": "2025-07-22T11:30:00+00:00",
                    "EndTime": "2025-07-23T11:30:00+00:00"
                }
            ]
        }
    ]
}
```

The following sections define the mandatory and optional input request parameters for
the `SearchTrainingPlanOfferings` API operation.

## Required parameters

When calling the [`SearchTrainingPlanOfferings`](../APIReference/API_SearchTrainingPlanOfferings.md "../APIReference/API_SearchTrainingPlanOfferings.md") API to list training plan offerings
that meet your requirements, you must provide the following values:

- `TargetResources`: The target resources (`training-job` or
  `hyperpod-cluster`) for which the plan will be used. The default value is
  `training-job`. Training plans are specific to their target
  resource.
  - A training plan designed for SageMaker training jobs can only be used to schedule
    and run training jobs.
  - A training plan for HyperPod clusters can be used exclusively to
    provide compute resources to a cluster's instance group.

- `InstanceType`: The type of instance to provision. The
  `InstanceType` must be of a supported type.

To learn about the list of available instances supported by SageMaker training plans, see
[Supported instance types,
AWS Regions, and pricing](reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions "reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions").

- `InstanceCount`: The number of instances to provision. If the number of
  instances is greater than 1, it should be a power of 2.
- `DurationHour`: The total duration of your requested plan in hours. The
  `DurationHour` is rounded up to the nearest multiple of 24.

## Optional parameters

The following sections provide details on some optional parameters that you can pass
to your `SearchTrainingPlanOfferings` API request.

- `StartTimeAfter`: Specify the requested start time of the plan. The
  `StartTimeAfter` should be a `timestamp` or an `ISO 8601
date/time` value in the future.
- `EndTimeBefore`: Specify the requested end time of the plan in a
  `timestamp` or an `ISO 8601 date/time` format. The
  `EndTimeBefore` should be at least 24 hours after the start time .
- `UltraServerType` : Specify the type of UltraServer to search for. For more information about UltraServers, see
  [UltraServers in SageMaker AI](reserve-capacity-with-training-plans.md#training-plans-ultraservers "reserve-capacity-with-training-plans.md#training-plans-ultraservers").
- `UltraServerCount`: Specify the number of UltraServers to search for.
