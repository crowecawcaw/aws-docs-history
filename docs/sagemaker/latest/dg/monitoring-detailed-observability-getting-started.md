

# Getting started with detailed observability
<a name="monitoring-detailed-observability-getting-started"></a>

Detailed observability is controlled by the `EnableDetailedObservability` flag in your endpoint configuration. The behavior of this flag depends on when the endpoint configuration was created. The following sections describe the different cases and how to enable the feature for each.

## New endpoint configurations
<a name="detailed-observability-getting-started-new"></a>

For endpoint configurations created after June 17, 2026, `EnableDetailedObservability` defaults to `true`. No action required.

![Endpoint detail page showing Observability: Enabled.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Observability_Enabled_page.png)


### Verify via API
<a name="detailed-observability-getting-started-verify-api"></a>

```
aws sagemaker describe-endpoint-config \
    --endpoint-config-name {{your-config-name}} \
    --query 'MetricsConfig.EnableDetailedObservability'
```

Expected output: `true`

### Disable via API
<a name="detailed-observability-getting-started-disable-api"></a>

To disable detailed observability, create a new endpoint configuration with the flag set to `false`, then update your endpoint to use it:

```
# Create endpoint config with detailed observability disabled
aws sagemaker create-endpoint-config \
    --endpoint-config-name {{name}}-no-observability \
    --execution-role-arn {{role-arn}} \
    --production-variants '[{"VariantName":"primary","ModelName":"{{model}}","InitialInstanceCount":1,"InstanceType":"ml.g5.xlarge"}]' \
    --metrics-config '{"EnableDetailedObservability": false}'

# Update endpoint to use the new config
aws sagemaker update-endpoint \
    --endpoint-name {{your-endpoint}} \
    --endpoint-config-name {{name}}-no-observability
```

## Existing endpoints (opt-in)
<a name="detailed-observability-getting-started-existing"></a>

### Via API
<a name="detailed-observability-getting-started-existing-api"></a>

```
# Create a new endpoint config with detailed observability enabled
aws sagemaker create-endpoint-config \
    --endpoint-config-name {{name}}-v2 \
    --execution-role-arn {{role-arn}} \
    --production-variants '[{"VariantName":"primary","ModelName":"{{model}}","InitialInstanceCount":2,"InstanceType":"ml.g5.12xlarge"}]' \
    --metrics-config '{"EnableDetailedObservability": true}'

# Update endpoint to use new config
aws sagemaker update-endpoint \
    --endpoint-name {{your-endpoint}} \
    --endpoint-config-name {{name}}-v2
```

### Via console (3-step wizard)
<a name="detailed-observability-getting-started-existing-console"></a>

1. Navigate to **SageMaker AI Console** → **Deployments and inference** → **Endpoints**.

1. Click **Enable detailed observability** in the banner.  
![Enablement banner on the endpoints list page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Observability_banner.png)

1. **Step 1:** Review the metrics that detailed observability provides. This includes inference framework metrics (TTFT, KV cache, queue depth), GPU health, node health, and lifecycle events. For the complete list, see [OpenTelemetry metrics reference](inference-monitoring.md). Enabling this feature also activates the SageMaker AI Insights dashboard — an auto-generated dashboard in Amazon CloudWatch that displays these metrics along with a health overview across all your endpoints.  
![Enablement wizard Step 1: Review metrics included.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Enablement_Step1.png)

1. **Step 2:** Enable OTel enrichment in your Amazon CloudWatch account settings. This step is required so that your metrics are queryable via PromQL in CloudWatch Query Studio and Amazon Managed Grafana. The wizard provides instructions and a direct link to the CloudWatch Settings page.  
![Enablement wizard Step 2: OTel enrichment guidance.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Enablement_Step2.png)

1. **Step 3:** Select the endpoints you want to enable detailed observability on and confirm. The console creates new endpoint configurations with `EnableDetailedObservability` set to `true` and applies them to your selected endpoints.  
![Enablement wizard Step 3: Confirm enablement.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Enablement_Step3.png)

## MetricsConfig API parameters
<a name="detailed-observability-getting-started-params"></a>

Set on the endpoint configuration via `CreateEndpointConfig`:


**MetricsConfig parameters**  

| Parameter | Type | Required | Default | Description | 
| --- | --- | --- | --- | --- | 
| EnableDetailedObservability | Boolean | No | false (existing), true (new) | Enables OTel-based metric collection | 
| EnableEnhancedMetrics | Boolean | No | false | Enables instance-level dimensions for legacy CloudWatch metrics | 
| MetricPublishFrequencyInSeconds | Integer | No | 60 | Scrape interval. Valid: 10, 30, 60, 120, 180, 240, 300 | 

## Relationship to enhanced metrics
<a name="detailed-observability-getting-started-vs-enhanced"></a>

`EnableDetailedObservability` and `EnableEnhancedMetrics` are separate features that can coexist on the same endpoint:


**Enhanced metrics vs. detailed observability**  

| Feature | `EnableEnhancedMetrics` | `EnableDetailedObservability` | 
| --- | --- | --- | 
| Purpose | Instance-level and container-level dimensions for legacy CloudWatch metrics | Full OTel-based metric collection with PromQL support | 
| Metrics store | CloudWatch classic metrics (namespace/dimension model) | OpenTelemetry metrics (label-based, PromQL-queryable) | 
| Query language | CloudWatch Metrics API | PromQL | 
| GPU metrics | GPUUtilization (with InstanceId, ContainerId, AcceleratorId dimensions) | DCGM\_FI\_DEV\_GPU\_UTIL (GPU utilization %), DCGM\_FI\_DEV\_MEM\_COPY\_UTIL (memory copy utilization %), DCGM\_FI\_DEV\_GPU\_TEMP (GPU temperature), DCGM\_FI\_DEV\_MEMORY\_TEMP (memory temperature), DCGM\_FI\_DEV\_FB\_FREE (framebuffer memory free), DCGM\_FI\_DEV\_FB\_USED (framebuffer memory used), DCGM\_FI\_DEV\_SM\_ACTIVE (streaming multiprocessor active %) — all per-GPU | 
| Token metrics | Not available | TTFT, ITL, KV cache, queue depth, TPS | 

Both flags can be enabled simultaneously. They publish to different metric stores and do not conflict.

For more information about GPU metrics available through the DCGM exporter, refer to the Data Center GPU Manager exporter documentation.

## Configure for custom containers (BYOC)
<a name="detailed-observability-getting-started-byoc"></a>

If you are using a custom container (bring your own container), the platform cannot automatically detect where your container exposes Prometheus metrics. You must specify the metrics endpoint path using `ContainerMetricsConfig` so that the OTel Collector knows where to scrape.

**Note**  
Your container must expose metrics in Prometheus format on port 8080. The default metrics path is `/metrics`. If your container uses a different path, configure `ContainerMetricsConfig` with the custom path.

You still need to set `EnableDetailedObservability` and `MetricPublishFrequencyInSeconds` in the endpoint configuration. Then, set `ContainerMetricsConfig` on the inference component or production variant with your custom metrics path:

```
{
    "ContainerMetricsConfig": {
        "MetricsEndpoints": [
            {
                "MetricsEndpointPath": "{{/metrics}}"
            }
        ]
    }
}
```

## Enabling OTel enrichment in Amazon CloudWatch
<a name="detailed-observability-getting-started-enrichment"></a>

To query metrics via PromQL (required for SageMaker AI Insights dashboard and Grafana), enable OTel enrichment at the account level.

**Important**  
OTel metric enrichment converts CloudWatch metrics into OpenTelemetry format and enriches each data point with AWS resource tags and account metadata. Enriched metrics are ingested at $0.50 per GB. Actual bytes per data point depend on the number and size of resource tags applied to your AWS resources. For details, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

### Via CloudWatch console
<a name="detailed-observability-getting-started-enrichment-console"></a>

1. Open Amazon CloudWatch console.

1. Choose **Settings** in the left navigation.

1. Enable **OTel metric enrichment**.

1. Enable **Resource tags for telemetry**.

![CloudWatch Settings page with OTel metric enrichment and Resource tags for telemetry enabled.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/CW_Setting_page.png)


### Via AWS CLI
<a name="detailed-observability-getting-started-enrichment-cli"></a>

```
# Enable OTel enrichment
aws cloudwatch start-otel-enrichment

# Enable resource tags for telemetry
aws observabilityadmin start-telemetry-enrichment

# Verify
aws cloudwatch get-otel-enrichment-status
```

### What enrichment adds
<a name="detailed-observability-getting-started-enrichment-adds"></a>

Every metric is automatically tagged with AWS resource context:


**Enrichment attributes**  

| Attribute | Description | Example | 
| --- | --- | --- | 
| @aws.account | AWS account ID | 123456789012 | 
| @aws.region | AWS Region | us-west-2 | 
| cloud.resource\_id | Full resource ARN | arn:aws:sagemaker:us-west-2:123456789012:endpoint/my-ep | 
| Resource tags | Tags from AWS Resource Explorer | env=production, team=ml | 