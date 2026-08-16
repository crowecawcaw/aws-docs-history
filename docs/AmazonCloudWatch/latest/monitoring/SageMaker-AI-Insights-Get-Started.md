# Get started with CloudWatch SageMaker AI Insights

Follow these steps to enable and access SageMaker AI Insights for your inference endpoints.

For the full setup guide on enabling detailed observability metrics on your endpoints, see
[SageMaker AI
detailed observability](../../../sagemaker/latest/dg/inference-detailed-observability.md "../../../sagemaker/latest/dg/inference-detailed-observability.md") in the _SageMaker AI Developer Guide_.

## Step 1: Enable OTel enrichment

SageMaker AI Insights requires [OTel metric
enrichment](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md") and resource tags to be enabled in your account.

###### To enable OTel enrichment (console)

1. Open the CloudWatch console and choose **Settings**.
2. Enable **OTel metric enrichment**.
3. Enable **Resource tags for telemetry**.

To enable OTel enrichment with the AWS CLI, use the following commands.

```
aws cloudwatch start-otel-enrichment
aws observabilityadmin start-telemetry-enrichment
```

## Step 2: Verify your endpoint configuration

Make sure that `EnableDetailedObservability` is set to `true` on your
endpoint configuration. This is the default for new endpoints.

```
aws sagemaker describe-endpoint-config --endpoint-config-name `name`
# Look for "EnableDetailedObservability": true
```

If it is not enabled, create a new endpoint configuration with the flag set to
`true` and update your endpoint.

## Step 3: Confirm your endpoint is InService

Confirm that your endpoint is in the `InService` state.

```
aws sagemaker describe-endpoint --endpoint-name `name` --query "EndpointStatus"
```

The expected output is `"InService"`.

## Step 4: Open SageMaker AI Insights

Navigate to the dashboard by using any of the following paths.

- CloudWatch console → **Infrastructure monitoring** → **SageMaker AI Insights**
- SageMaker AI console → **Endpoints** → choose **Open SageMaker AI Insights**
- SageMaker AI console → endpoint detail page → choose **View in SageMaker AI Insights**

## Step 5: Verify data is flowing

After 2–3 minutes, the dashboard should populate with the following data.

- Invocation counts in the summary bar
- Instance and inference component (IC) data in the **Performance** tab
- Utilization metrics in the **Capacity** tab

###### Tip

If you see **No data**, verify that OTel enrichment is enabled and your
endpoint has been `InService` for at least 2–3 minutes.

## Required permissions for SageMaker AI Insights

Certain IAM permissions are required to use SageMaker AI Insights. The following policy contains the
permissions required to use SageMaker AI Insights.

```
{
    "Effect": "Allow",
    "Action": [
        "cloudwatch:GetMetricData",
        "cloudwatch:ListMetrics",
        "cloudwatch:DescribeAlarms",
        "sagemaker:DescribeEndpoint",
        "sagemaker:DescribeEndpointConfig",
        "sagemaker:ListEndpoints",
        "sagemaker:ListInferenceComponents"
    ],
    "Resource": "*"
}
```
