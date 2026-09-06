

# Search for extension offerings
<a name="search-extension-offerings-api-cli-sdk"></a>

Use the [`SearchTrainingPlanOfferings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html) API with the `TrainingPlanArn` parameter to find available extension offerings for your training plan.

The following example uses an AWS CLI command to search for extension offerings for an existing training plan.

```
aws sagemaker search-training-plan-offerings \
--training-plan-arn "arn:aws:sagemaker:{{us-east-2}}:{{123456789012}}:training-plan/{{my-training-plan}}" \
--duration-hours {{48}}
```

This JSON document is a sample response from the SageMaker training plans API. The response includes `TrainingPlanExtensionOfferings` containing available extension offerings for the specified training plan.

```
{
    "TrainingPlanOfferings": [],
    "TrainingPlanExtensionOfferings": [
        {
            "TrainingPlanExtensionOfferingId": "tpeo-{{SHA-256-hash-value}}",
            "AvailabilityZone": "us-east-2a",
            "StartDate": "2025-09-23T12:00:00Z",
            "EndDate": "2025-09-25T12:00:00Z",
            "DurationHours": 48,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD"
        }
    ]
}
```

The following sections define the mandatory and optional input request parameters for the `SearchTrainingPlanOfferings` API operation when searching for extension offerings.

## Required parameters
<a name="search-extension-offerings-required-params"></a>

When calling the [`SearchTrainingPlanOfferings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html) API to search for extension offerings, you must provide the following value:
+ `TrainingPlanArn`: The of the training plan you want to extend. The `TrainingPlanArn` must reference an existing training plan with a status of `Active` or `Scheduled`.

## Optional parameters
<a name="search-extension-offerings-optional-params"></a>

The following sections provide details on some optional parameters that you can pass to your `SearchTrainingPlanOfferings` API request when searching for extension offerings.
+ `DurationHours`: The desired duration in hours for the extension. The `DurationHours` is rounded up to the nearest multiple of 24.