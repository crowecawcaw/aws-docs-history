

# View extension history
<a name="describe-extension-history-api-cli-sdk"></a>

Use the [`DescribeTrainingPlanExtensionHistory`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlanExtensionHistory.html) API to view the complete extension history for a training plan.

The following example uses an AWS CLI command to retrieve the extension history.

```
aws sagemaker describe-training-plan-extension-history \
--training-plan-arn "arn:aws:sagemaker:{{us-east-2}}:{{123456789012}}:training-plan/{{my-training-plan}}"
```

This JSON document is a sample response from the SageMaker training plans API. The response includes a paginated list of all extensions for the training plan.

```
{
    "TrainingPlanExtensions": [
        {
            "TrainingPlanExtensionOfferingId": "tpeo-{{SHA-256-hash-value}}",
            "ExtendedAt": "2025-09-17T10:00:00Z",
            "StartDate": "2025-09-23T12:00:00Z",
            "EndDate": "2025-09-25T12:00:00Z",
            "Status": "Active",
            "PaymentStatus": "Completed",
            "AvailabilityZone": "us-east-2a",
            "DurationHours": 48,
            "UpfrontFee": "xxxx.xx",
            "CurrencyCode": "USD"
        }
    ],
    "NextToken": null
}
```

The following sections define the mandatory and optional input request parameters for the `DescribeTrainingPlanExtensionHistory` API operation.

## Required parameters
<a name="describe-extension-history-required-params"></a>

When calling the [`DescribeTrainingPlanExtensionHistory`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlanExtensionHistory.html) API, you must provide the following value:
+ `TrainingPlanArn`: The of the training plan to retrieve extension history for.

## Optional parameters
<a name="describe-extension-history-optional-params"></a>

The following sections provide details on some optional parameters that you can pass to your `DescribeTrainingPlanExtensionHistory` API request.
+ `NextToken`: If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
+ `MaxResults`: The maximum number of extensions to return in the response.

## Extension status values
<a name="extension-status-values-api"></a>

Extensions can have the following status values:
+ `Pending`: The extension has been requested and is awaiting payment processing.
+ `Active`: The extension has been successfully purchased and is active.
+ `Scheduled`: The extension is scheduled to start at a future time.
+ `Failed`: The extension purchase failed (for example, due to payment issues).
+ `Expired`: The extension period has ended.