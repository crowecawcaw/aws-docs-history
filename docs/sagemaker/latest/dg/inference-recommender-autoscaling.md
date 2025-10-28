# Get autoscaling policy

recommendations

With Amazon SageMaker Inference Recommender, you can get recommendations for autoscaling policies for your
SageMaker AI endpoint based on your anticipated traffic pattern. If you’ve already completed
an inference recommendation job, you can provide the details of the job to get a
recommendation for an autoscaling policy that you can apply to your endpoint.

Inference Recommender benchmarks different values for each metric to determine the ideal
autoscaling configuration for your endpoint. The autoscaling recommendation returns
a recommended autoscaling policy for each metric that was defined in your inference
recommendation job. You can save the policies and apply them to your endpoint with
the [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md") API.

To get started, review the following prerequisites.

## Prerequisites

Before you begin, you must have completed a successful inference
recommendation job. In the following section, you can provide either an
inference recommendation ID or the name of a SageMaker AI endpoint that was benchmarked
during an inference recommendation job.

To retrieve your recommendation job ID or endpoint name, you can either view
the details of your inference recommendation job in the SageMaker AI console, or you can
use the `RecommendationId` or `EndpointName` fields
returned by the [DescribeInferenceRecommendationsJob](../APIReference/API_DescribeInferenceRecommendationsJob.md "../APIReference/API_DescribeInferenceRecommendationsJob.md") API.

## Create an autoscaling

configuration recommendation

To create an autoscaling recommendation policy, you can use the
AWS SDK for Python (Boto3).

The following example shows the fields for the [GetScalingConfigurationRecommendation](../APIReference/API_GetScalingConfigurationRecommendation.md "../APIReference/API_GetScalingConfigurationRecommendation.md") API. Use the following
fields when you call the API:

- `InferenceRecommendationsJobName` – Enter the name
  of your inference recommendation job.
- `RecommendationId` – Enter the ID of an inference
  recommendation from a recommendation job. This is optional if you’ve
  specified the `EndpointName` field.
- `EndpointName` – Enter the name of an endpoint that
  was benchmarked during an inference recommendation job. This is optional
  if you’ve specified the `RecommendationId` field.
- `TargetCpuUtilizationPerCore` – (Optional) Enter a
  percentage value of how much utilization you want an instance on your
  endpoint to use before autoscaling. The default value if you don’t
  specify this field is 50%.
- `ScalingPolicyObjective` – (Optional) An object
  where you specify your anticipated traffic pattern.
  - `MinInvocationsPerMinute` – (Optional) The
    minimum number of expected requests to your endpoint per
    minute.
  - `MaxInvocationsPerMinute` – (Optional) The
    maximum number of expected requests to your endpoint per
    minute.

```
{
    "InferenceRecommendationsJobName": "`string`", // Required
    "RecommendationId": "`string`", // Optional, provide one of RecommendationId or EndpointName
    "EndpointName": "`string`", // Optional, provide one of RecommendationId or EndpointName
    "TargetCpuUtilizationPerCore": `number`, // Optional
    "ScalingPolicyObjective": { // Optional
        "MinInvocationsPerMinute": `number`,
        "MaxInvocationsPerMinute": `number`
    }
}
```

After submitting your request, you’ll receive a response with autoscaling
policies defined for each metric. See the following section for information
about interpreting the response.

## Review your

autoscaling configuration recommendation results

The following example shows the response from the [GetScalingConfigurationRecommendation](../APIReference/API_GetScalingConfigurationRecommendation.md "../APIReference/API_GetScalingConfigurationRecommendation.md") API:

```
{
    "InferenceRecommendationsJobName": "string",
    "RecommendationId": "string", // One of RecommendationId or EndpointName is shown
    "EndpointName": "string",
    "TargetUtilizationPercentage": Integer,
    "ScalingPolicyObjective": {
        "MinInvocationsPerMinute": Integer,
        "MaxInvocationsPerMinute": Integer
    },
    "Metric": {
        "ModelLatency": Integer,
        "InvocationsPerInstance": Integer
    },
    "DynamicScalingConfiguration": {
        "MinCapacity": number,
        "MaxCapacity": number,
        "ScaleInCooldown": number,
        "ScaleOutCooldown": number,
        "ScalingPolicies": [
            {
                "TargetTracking": {
                    "MetricSpecification": {
                        "Predefined" {
                            "PredefinedMetricType": "string"
                         },
                        "Customized": {
                            "MetricName": "string",
                            "Namespace": "string",
                            "Statistic": "string"
                         }
                    },
                    "TargetValue": Double
                }
            }
        ]
    }
}
```

The `InferenceRecommendationsJobName`,
`RecommendationID` or `EndpointName`,
`TargetCpuUtilizationPerCore`, and the
`ScalingPolicyObjective` object fields are copied from your
initial request.

The `Metric` object lists the metrics that were benchmarked in your
inference recommendation job, along with a calculation of the values for each
metric when the instance utilization would be the same as the
`TargetCpuUtilizationPerCore` value. This is useful for
anticipating the performance metrics on your endpoint when it scales in and out
with the recommended autoscaling policy. For example, consider if your instance
utilization was 50% in your inference recommendation job and your
`InvocationsPerInstance` value was originally `4`. If
you specify the `TargetCpuUtilizationPerCore` value to be 100% in
your autoscaling recommendation request, then the
`InvocationsPerInstance` metric value returned in the response is
`2` because you anticipated allocating twice as much instance
utilization.

The `DynamicScalingConfiguration` object returns the values that
you should specify for the [TargetTrackingScalingPolicyConfiguration](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md#autoscaling-PutScalingPolicy-request-TargetTrackingScalingPolicyConfiguration "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md#autoscaling-PutScalingPolicy-request-TargetTrackingScalingPolicyConfiguration") when you call the [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md") API. This includes the recommended minimum and
maximum capacity values, the recommended scale in and scale out cooldown times,
and the `ScalingPolicies` object, which contains the recommended
`TargetValue` you should specify for each metric.
