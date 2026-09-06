

# Deploy to multiple instance types with instance pools
<a name="realtime-endpoints-heterogeneous"></a>

When you deploy a model to a SageMaker AI endpoint, you typically specify a single instance type for the production variant. If that instance type is unavailable in the target Availability Zone, the deployment fails with an insufficient capacity error (ICE), and you must manually retry with a different instance type.

With instance pools, you can specify an ordered list of up to five instance types for a production variant. SageMaker AI attempts to provision instances starting with the highest-priority type (priority 1) and automatically falls back to lower-priority types when capacity is unavailable. This eliminates the need for manual retry and improves endpoint availability.

Instance pools support both real-time and asynchronous inference endpoints. You can use them with single-model endpoints and with inference components.

The following steps describe how instance pool provisioning works:

1. SageMaker AI tries to provision instances from the highest-priority pool (priority 1).

1. If SageMaker AI encounters an insufficient capacity error (ICE) for the current instance type, it automatically falls back to the next pool in priority order.

1. This continues until the required number of instances is provisioned, all pools are exhausted, or the total provisioning timeout (`VariantInstanceProvisionTimeoutInSeconds`) is reached.

**Topics**
+ [Set up an endpoint with instance pools](#heterogeneous-endpoint-setup)
+ [Monitor instance pools](#heterogeneous-endpoint-observability)
+ [Auto-scaling with instance pools](#heterogeneous-endpoint-autoscaling)

## Set up an endpoint with instance pools
<a name="heterogeneous-endpoint-setup"></a>

To use instance pools, you replace the `InstanceType` parameter in your production variant with an `InstancePools` list. Each entry specifies an instance type and a priority (1 to 5, where 1 is the highest). You can optionally set `VariantInstanceProvisionTimeoutInSeconds` (300 to 3600 seconds) to control the total time SageMaker AI spends attempting to provision instances across all pools before the operation fails.

### Real-time endpoint with a single model
<a name="heterogeneous-endpoint-setup-realtime"></a>

The following example creates an endpoint configuration with two instance pools. If `ml.g6.2xlarge` instances are unavailable, SageMaker AI falls back to `ml.g6e.2xlarge`.

```
import boto3

sagemaker_client = boto3.client("sagemaker")

endpoint_config_name = "my-heterog-endpoint-config"

sagemaker_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[
        {
            "VariantName": "AllTraffic",
            "ModelName": "my-model",
            "InitialInstanceCount": 2,
            "InstancePools": [
                {
                    "InstanceType": "ml.g6.2xlarge",
                    "Priority": 1,
                },
                {
                    "InstanceType": "ml.g6e.2xlarge",
                    "Priority": 2,
                },
            ],
            "VariantInstanceProvisionTimeoutInSeconds": 600,
        }
    ],
)

sagemaker_client.create_endpoint(
    EndpointName="my-heterog-endpoint",
    EndpointConfigName=endpoint_config_name,
)
```

You can also use the `ModelNameOverride` parameter in each pool to specify a different model optimized for that instance type. For example, you might deploy a model compiled for GPU on one instance type and an uncompiled version on another.

### Real-time endpoint with inference components
<a name="heterogeneous-endpoint-setup-ic"></a>

When you use inference components with instance pools, you have two options for defining specifications:
+ **Single `Specification`** — Use the same model and resource configuration across all instance types in the endpoint's instance pools. This works when the model can run on any of the provisioned instance types with the same resource requirements.
+ **Multiple `Specifications`** — Use the `Specifications` parameter (plural) to define different model or resource configurations for each instance type. Each specification includes an `InstanceType` field that maps it to an instance type in the endpoint's instance pools.

The following example creates an inference component with per-instance-type specifications:

```
sagemaker_client.create_inference_component(
    InferenceComponentName="my-ic",
    EndpointName="my-heterog-endpoint",
    VariantName="AllTraffic",
    Specifications=[
        {
            "InstanceType": "ml.g6.2xlarge",
            "ModelName": "my-model-g6",
            "Container": {
                "Image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-image:latest",
            },
            "ComputeResourceRequirements": {
                "NumberOfAcceleratorDevicesRequired": {{1}},
                "MinMemoryRequiredInMb": {{4096}},
            },
        },
        {
            "InstanceType": "ml.g6e.2xlarge",
            "ModelName": "my-model-g6e",
            "Container": {
                "Image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-image:latest",
            },
            "ComputeResourceRequirements": {
                "NumberOfAcceleratorDevicesRequired": {{1}},
                "MinMemoryRequiredInMb": {{8192}},
            },
        },
    ],
    RuntimeConfig={
        "CopyCount": 2,
    },
)
```

## Monitor instance pools
<a name="heterogeneous-endpoint-observability"></a>

Existing CloudWatch metrics that are aggregated across all instances in a variant — such as `Invocations`, `ModelLatency`, and `CPUUtilization` — continue to work the same way when you use instance pools. In addition, CloudWatch publishes these metrics with an `InstanceType` dimension so you can monitor performance for each instance type separately.

### Per-instance-type metrics
<a name="heterogeneous-observability-per-type"></a>

When a production variant uses instance pools, the following dimension combinations become available in CloudWatch for per-instance-type monitoring:


| Dimension combination | Use case | 
| --- | --- | 
| EndpointName, VariantName, InstanceType | Filter endpoint-level and invocation metrics (such as CPUUtilization, Invocations, ModelLatency) for a specific instance type within the variant. | 
| InferenceComponentName, InstanceType | Filter inference component metrics for a specific instance type. Use this to compare how the same inference component performs across different instance types. | 

These dimensions are available for both standard CloudWatch metrics and enhanced metrics. For the full list of available metrics, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md) and [Amazon SageMaker AI enhanced metrics for inference endpoints](monitoring-cloudwatch-enhanced-metrics.md).

### Check fleet distribution
<a name="heterogeneous-observability-distribution"></a>

To see the current instance count for each pool, call the [`DescribeEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API. The `ProductionVariants` in the response include an `InstancePools` list with the current count for each instance type. This shows your fleet composition after provisioning, including any fallback instances from lower-priority pools.

If you use inference components, the [`DescribeInferenceComponent`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceComponent.html) response includes a `PlacementStatus` field in the runtime configuration summary that shows the copy count per instance type. Use this to understand how inference component copies are distributed across the instance types in your fleet.

## Auto-scaling with instance pools
<a name="heterogeneous-endpoint-autoscaling"></a>

Auto-scaling with instance pools follows the same process as standard endpoint auto-scaling. You register scalable targets, define scaling policies, and apply them to your endpoint. For general auto-scaling setup, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md).

The key difference is how SageMaker AI provisions and releases instances when a scaling event triggers:

Scale out (adding instances)  
SageMaker AI provisions instances starting with the highest-priority pool (lowest priority value). If SageMaker AI encounters an insufficient capacity error for the current instance type, it automatically falls back to the next pool in priority order. SageMaker AI continues retrying across pools until instances are provisioned or the total `VariantInstanceProvisionTimeoutInSeconds` is reached.

Scale in (removing instances)  
SageMaker AI releases instances starting with the lowest-priority pool (highest priority value). Your preferred, higher-priority instance types are kept running as long as possible, and fallback instances are released first.

### Use predefined scaling metrics
<a name="heterogeneous-autoscaling-predefined"></a>

Predefined scaling metrics such as `SageMakerVariantInvocationsPerInstance` continue to work with instance pools. These metrics aggregate across all instance types in the variant, so the scaling behavior is the same as a standard endpoint. This is the simplest approach when all instance types in your pools have similar capacity.

For target tracking and step scaling policy setup, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md).

### Use weighted custom metrics for mixed fleets
<a name="heterogeneous-autoscaling-weighted"></a>

When your instance pools contain instance types with different compute capacities, you can use CloudWatch metric math to create a weighted scaling signal. This lets you control how much each instance type's load contributes to the overall scaling decision.

The following example creates a target tracking policy that uses a weighted average of `ConcurrentRequestsPerModel` across two instance types. The weights determine how sensitive the scaling policy is to each type's load:

```
import boto3

aas_client = boto3.client("application-autoscaling")

# Register the scalable target
aas_client.register_scalable_target(
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/my-heterog-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    MinCapacity=1,
    MaxCapacity=10,
)

# Define target tracking policy with weighted metric math
aas_client.put_scaling_policy(
    PolicyName="weighted-concurrent-requests",
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/my-heterog-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    PolicyType="TargetTrackingScaling",
    TargetTrackingScalingPolicyConfiguration={
        "TargetValue": {{10.0}},
        "CustomizedMetricSpecification": {
            "Metrics": [
                {
                    "Id": "cr_g6",
                    "Label": "ConcurrentRequests-g6-2xlarge",
                    "MetricStat": {
                        "Metric": {
                            "Namespace": "AWS/SageMaker",
                            "MetricName": "ConcurrentRequestsPerModel",
                            "Dimensions": [
                                {"Name": "EndpointName", "Value": "my-heterog-endpoint"},
                                {"Name": "VariantName", "Value": "AllTraffic"},
                                {"Name": "InstanceType", "Value": "ml.g6.2xlarge"},
                            ],
                        },
                        "Stat": "Average",
                    },
                    "ReturnData": False,
                },
                {
                    "Id": "cr_g6e",
                    "Label": "ConcurrentRequests-g6e-2xlarge",
                    "MetricStat": {
                        "Metric": {
                            "Namespace": "AWS/SageMaker",
                            "MetricName": "ConcurrentRequestsPerModel",
                            "Dimensions": [
                                {"Name": "EndpointName", "Value": "my-heterog-endpoint"},
                                {"Name": "VariantName", "Value": "AllTraffic"},
                                {"Name": "InstanceType", "Value": "ml.g6e.2xlarge"},
                            ],
                        },
                        "Stat": "Average",
                    },
                    "ReturnData": False,
                },
                {
                    "Id": "weighted_avg",
                    "Label": "WeightedConcurrentRequests",
                    "Expression": "{{0.5}} * cr_g6 + {{0.5}} * cr_g6e",
                    "ReturnData": True,
                },
            ],
        },
    },
)
```

In this example, `cr_g6` and `cr_g6e` fetch the per-instance-type `ConcurrentRequestsPerModel` metric. The `weighted_avg` expression combines them with equal weights (0.5 / 0.5). Adjust the weights to change how the policy responds to load on each instance type.

**How weights affect scaling behavior:** A higher weight on an instance type means the scaling policy is *more sensitive* to that type's load — not less. The lower-weighted type's signal is dampened, so it can run at higher utilization before triggering a scaling event.


| Weight strategy | High-priority type tolerance | Low-priority type tolerance | Best for | 
| --- | --- | --- | --- | 
| Higher weight on high-priority (0.7 / 0.3) | Lower (protected) | Higher (runs hotter) | Protecting expensive or high-capacity instances from overload | 
| Equal (0.5 / 0.5) | Balanced | Balanced | Default recommendation for most workloads | 
| Higher weight on low-priority (0.3 / 0.7) | Higher (runs hotter) | Lower (protected) | Preventing smaller fallback instances from becoming saturated | 

For more information about custom metrics with auto-scaling, see [Define a custom metric (CloudWatch metric: CPUUtilization)](endpoint-auto-scaling-add-code-define.md#endpoint-auto-scaling-add-code-custom).