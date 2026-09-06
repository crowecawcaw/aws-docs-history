

# Amazon SageMaker AI enhanced metrics for inference endpoints
<a name="monitoring-cloudwatch-enhanced-metrics"></a>

Enhanced metrics provide instance-level and container-level monitoring data for Amazon SageMaker AI real-time endpoints. When you enable enhanced metrics, Amazon CloudWatch metrics can include `InstanceId`, `ContainerId`, and `AcceleratorId` dimensions (availability varies by namespace) for granular per-instance, per-container, and per-GPU visibility. Enhanced metrics are available for single-model endpoints and inference components. Multi-Container Endpoints (MCE) support instance-level enhanced metrics but not container-level metrics.

Key characteristics of enhanced metrics:
+ **Instance-level granularity**. Utilization and invocation metrics include an `InstanceId` dimension that identifies the specific instance hosting the endpoint. This is available for all real-time endpoints.
+ **Container-level granularity**. For endpoints that use inference components, metrics include a `ContainerId` dimension that identifies the specific container running the model. Container-level dimensions appear in both the `AWS/SageMaker` namespace (invocation metrics) and the `/aws/sagemaker/InferenceComponents` namespace (utilization metrics).
+ **Per-GPU granularity**. GPU utilization metrics include an `AcceleratorId` dimension that identifies the specific GPU on an instance.
+ **Configurable publishing frequency**. You can configure the metric publishing interval to 10, 30, 60, 120, 180, 240, or 300 seconds. The default is 60 seconds. This interval applies to utilization metrics regardless of whether enhanced metrics is enabled. With enhanced metrics enabled, it also applies to invocation metrics.

## Enabling enhanced metrics
<a name="enhanced-metrics-enabling"></a>

You enable enhanced metrics by setting `EnableEnhancedMetrics` to `True` in the [MetricsConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricsConfig.html) parameter when you call the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API.

The `MetricsConfig` parameter has the following fields:


**MetricsConfig parameters**  

| Parameter | Type | Required | Default | Description | 
| --- | --- | --- | --- | --- | 
| EnableEnhancedMetrics | Boolean | No | False | Enables instance-level and container-level metric dimensions. | 
| MetricPublishFrequencyInSeconds | Integer | No | 60 | The interval, in seconds, at which metrics are published to Amazon CloudWatch. Defaults to `60`. Valid values: `10`, `30`, `60`, `120`, `180`, `240`, `300`. When `EnableEnhancedMetrics` is set to `False`, this interval applies to utilization metrics only; invocation metrics continue to be published at the default 60-second interval. When set to `True`, this interval applies to both utilization and invocation metrics. | 

**Note**  
`MetricsConfig` is set at the endpoint configuration level. You cannot configure different settings for individual inference components on the same endpoint.

To enable enhanced metrics on an existing endpoint, create a new endpoint configuration with the desired `MetricsConfig` settings, and then call [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) with the new endpoint configuration name. This triggers a blue/green or rolling deployment. Enhanced metrics do not appear until the deployment completes. The same process applies when changing `MetricsConfig` settings on an already-configured endpoint.

When you configure `MetricsConfig`, both [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) and [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html) return `MetricsConfig` in the response.

When you enable enhanced metrics, SageMaker AI adds additional dimensions to metrics across three CloudWatch namespaces: `/aws/sagemaker/Endpoints` for utilization metrics, `AWS/SageMaker` for invocation metrics, and `/aws/sagemaker/InferenceComponents` for inference component utilization metrics.

## Instance-level utilization metrics
<a name="enhanced-metrics-instance-utilization"></a>

The `/aws/sagemaker/Endpoints` namespace includes utilization metrics for all real-time endpoints, including those that use inference components. When you enable enhanced metrics, the `InstanceId` and `AcceleratorId` (GPU metrics only) dimensions become available alongside the existing namespace dimensions. For a complete list of metrics and dimensions, see [SageMaker AI endpoint metrics](monitoring-cloudwatch.md#cloudwatch-metrics-endpoints).

When you enable enhanced metrics, the following additional dimensions are available:


**Additional dimensions for instance-level utilization metrics**  

| Dimension | Description | 
| --- | --- | 
| InstanceId | Filters utilization metrics for a specific instance. | 
| AcceleratorId | (GPU metrics only) Filters utilization metrics for a specific GPU. | 

## Instance and container-level invocation metrics
<a name="enhanced-metrics-invocation"></a>

The `AWS/SageMaker` namespace includes invocation metrics. When you enable enhanced metrics, the `InstanceId` and `ContainerId` (inference components only) dimensions become available alongside the existing namespace dimensions. For a complete list of metrics and dimensions, see [SageMaker AI endpoint invocation metrics](monitoring-cloudwatch.md#cloudwatch-metrics-endpoint-invocation).

When you enable enhanced metrics, the following additional dimensions are available:


**Additional dimensions for invocation metrics**  

| Dimension | Description | 
| --- | --- | 
| InstanceId | Filters invocation metrics for a specific instance. | 
| ContainerId | (Inference components only) Filters invocation metrics for a specific container. | 

## Container-level utilization metrics
<a name="enhanced-metrics-container"></a>

The `/aws/sagemaker/InferenceComponents` namespace includes utilization metrics for endpoints that use inference components. When you enable enhanced metrics, the `InstanceId`, `ContainerId`, and `AcceleratorId` (GPU metrics only) dimensions become available alongside the existing namespace dimensions. For a complete list of metrics and dimensions, see [SageMaker AI inference component metrics](monitoring-cloudwatch.md#cloudwatch-metrics-inference-component).

When you enable enhanced metrics, the following additional dimensions are available:


**Additional dimensions for container-level utilization metrics**  

| Dimension | Description | 
| --- | --- | 
| InstanceId | Filters utilization metrics for a specific instance. | 
| ContainerId | Filters utilization metrics for a specific container. | 
| AcceleratorId | (GPU metrics only) Filters utilization metrics for a specific GPU. | 

## Configurable metric frequency
<a name="enhanced-metrics-frequency"></a>

You can configure the interval at which metrics are published to CloudWatch. The default frequency is 60 seconds.

**Valid values:** 10, 30, 60, 120, 180, 240, or 300 seconds.

When `EnableEnhancedMetrics` is set to `False`, this frequency applies to utilization metrics only; invocation metrics continue to be published at the default 60-second interval. When set to `True`, this frequency applies to both utilization and invocation metrics.

**Note**  
Metrics published at intervals less than 60 seconds (high-resolution) are retained for 3 hours.

Standard CloudWatch pricing applies per metric per unique dimension combination. Enhanced metrics increase the number of metric streams because each instance, container, and GPU creates additional dimension combinations. For pricing details, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Code examples: configure enhanced metrics
<a name="enhanced-metrics-code-examples"></a>

The following examples show how to create an endpoint configuration with enhanced metrics enabled and how to verify the configuration.

### Create an endpoint configuration with enhanced metrics
<a name="enhanced-metrics-create-example"></a>

------
#### [ AWS SDK for Python (Boto3) ]

**Example Create an endpoint configuration with enhanced metrics**  

```
import boto3

sagemaker_client = boto3.client('sagemaker')

response = sagemaker_client.create_endpoint_config(
    EndpointConfigName='{{my-enhanced-metrics-config}}',
    ProductionVariants=[
        {
            'VariantName': '{{AllTraffic}}',
            'ModelName': '{{my-model}}',
            'InstanceType': '{{ml.m5.xlarge}}',
            'InitialInstanceCount': {{2}},
        }
    ],
    MetricsConfig={
        'EnableEnhancedMetrics': True,
        'MetricPublishFrequencyInSeconds': {{60}}
    }
)
```

------
#### [ AWS CLI ]

**Example Create an endpoint configuration with enhanced metrics**  

```
aws sagemaker create-endpoint-config \
    --endpoint-config-name {{my-enhanced-metrics-config}} \
    --production-variants file://production-variants.json \
    --metrics-config file://metrics-config.json
```
Where `metrics-config.json` contains:  

```
{
    "EnableEnhancedMetrics": true,
    "MetricPublishFrequencyInSeconds": {{60}}
}
```

------

### Verify enhanced metrics configuration
<a name="enhanced-metrics-verify-example"></a>

------
#### [ AWS SDK for Python (Boto3) ]

**Example Verify enhanced metrics configuration**  

```
response = sagemaker_client.describe_endpoint_config(
    EndpointConfigName='{{my-enhanced-metrics-config}}'
)
print(response['MetricsConfig'])
# {'EnableEnhancedMetrics': True, 'MetricPublishFrequencyInSeconds': 60}

response = sagemaker_client.describe_endpoint(
    EndpointName='{{my-endpoint}}'
)
print(response['MetricsConfig'])
```

------
#### [ AWS CLI ]

**Example Verify enhanced metrics configuration**  

```
aws sagemaker describe-endpoint-config \
    --endpoint-config-name {{my-enhanced-metrics-config}} \
    --query 'MetricsConfig'
```

```
aws sagemaker describe-endpoint \
    --endpoint-name {{my-endpoint}} \
    --query 'MetricsConfig'
```

------