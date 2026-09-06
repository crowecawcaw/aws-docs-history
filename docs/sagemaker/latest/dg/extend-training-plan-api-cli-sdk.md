

# Purchase an extension
<a name="extend-training-plan-api-cli-sdk"></a>

After selecting an extension offering, use the [`ExtendTrainingPlan`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html) API to purchase the extension.

The following example uses an AWS CLI command to extend a training plan.

```
aws sagemaker extend-training-plan \
--training-plan-extension-offering-id "{{tpeo-SHA-256-hash-value}}"
```

This JSON document is a sample response from the SageMaker training plans API. The response includes the list of extensions for the training plan.

```
{
    "TrainingPlanExtensions": [
        {
            "TrainingPlanExtensionOfferingId": "tpeo-{{SHA-256-hash-value}}",
            "ExtendedAt": "2025-09-17T10:00:00Z",
            "StartDate": "2025-09-23T12:00:00Z",
            "EndDate": "2025-09-25T12:00:00Z",
            "Status": "Pending",
            "PaymentStatus": "Pending",
            "AvailabilityZone": "us-east-2a",
            "DurationHours": 48,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD"
        }
    ]
}
```

The following section defines the mandatory input request parameter for the `ExtendTrainingPlan` API operation.

## Required parameters
<a name="extend-training-plan-required-params"></a>

When calling the [`ExtendTrainingPlan`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html) API to extend a training plan, you must provide the following value:
+ `TrainingPlanExtensionOfferingId`: The ID of the extension offering you are purchasing. You can retrieve this ID from the `TrainingPlanExtensionOfferings` in the response of your `SearchTrainingPlanOfferings` API call. Its format should start with `tpeo-*`.