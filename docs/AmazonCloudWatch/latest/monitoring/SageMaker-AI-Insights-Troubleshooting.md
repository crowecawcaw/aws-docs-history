

# Troubleshooting SageMaker AI Insights
<a name="SageMaker-AI-Insights-Troubleshooting"></a>

The following sections describe common issues and resolutions for the CloudWatch SageMaker AI Insights dashboard. If your issue is not listed here, verify that your endpoint is `InService` and that OTel enrichment is enabled in your account.

## Dashboard shows "No data" for all panels
<a name="SageMaker-AI-Insights-tshoot-no-data"></a>

**Cause:** OTel enrichment is not enabled in your account.

**Resolution:**

1. Open the CloudWatch console and choose **Settings**.

1. Enable **OTel metric enrichment**.

1. Enable **Resource tags for telemetry**.

1. Wait 2–3 minutes for metrics to begin flowing.

Alternatively, enable OTel enrichment with the following AWS CLI commands.

```
aws cloudwatch start-otel-enrichment
aws observabilityadmin start-telemetry-enrichment
```

## TTFT, TPS, and KV cache columns show a dash
<a name="SageMaker-AI-Insights-tshoot-framework-metrics"></a>

**Cause:** These metrics are only available for endpoints using the vLLM or SGLang frameworks. Endpoints using other frameworks (TensorRT‐LLM, custom containers) do not emit these metrics.

**Resolution:** No action needed—this is expected behavior.

## SageMaker AI Insights redirects to Database Insights
<a name="SageMaker-AI-Insights-tshoot-redirect"></a>

**Cause:** Known issue in some accounts.

**Workaround:** In the redirected URL, replace `instances` with `endpoints`. The dashboard then loads correctly.

## Dashboard loads but shows 0 invocations
<a name="SageMaker-AI-Insights-tshoot-zero-invocations"></a>

**Cause:** The endpoint is `InService` but not receiving traffic, or the selected time range has no invocations.

**Resolution:**
+ Send test invocations to the endpoint.
+ Adjust the time range to a period when traffic was active.

## Metrics appear in CloudWatch but not in SageMaker AI Insights
<a name="SageMaker-AI-Insights-tshoot-metrics-not-shown"></a>

**Cause:** `EnableDetailedObservability` might not be set to `true` on the endpoint configuration.

**Resolution:** Verify the endpoint configuration with the following command.

```
aws sagemaker describe-endpoint-config --endpoint-config-name {{name}}
# Look for "EnableDetailedObservability": true
```

## Scaling events table is empty
<a name="SageMaker-AI-Insights-tshoot-scaling-empty"></a>

**Cause:** Application Auto Scaling is not configured, or no scaling events occurred in the selected time range.

**Resolution:**
+ Configure an autoscaling policy for your endpoint.
+ Adjust the time range to include periods when scaling events occurred.