# Autoscaling policies

for your HyperPod inference model deployment

This following information provides practical examples and configurations for
implementing autoscaling policies on Amazon SageMaker HyperPod inference model deployments.

You'll learn how to configure automatic scaling using the built-in
`autoScalingSpec` in your deployment YAML files, as well as how to create
standalone KEDA `ScaledObject` configurations for advanced scaling scenarios.
The examples cover scaling triggers based on CloudWatch metrics, Amazon SQS queue lengths,
Prometheus queries, and resource utilization metrics like CPU and memory.

## Using

autoScalingSpec in deployment YAML

Amazon SageMaker HyperPod inference operator provides built-in autoscaling capabilities for
model deployments using metrics from CloudWatch and Amazon Managed Prometheus (AMP). The
following deployment YAML example includes an `autoScalingSpec` section
that defines the configuration values for scaling your model deployment.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: JumpStartModel
metadata:
  name: deepseek-sample624
  namespace: ns-team-a
spec:
  sageMakerEndpoint:
    name: deepsek7bsme624
  model:
    modelHubName: SageMakerPublicHub
    modelId: deepseek-llm-r1-distill-qwen-1-5b
    modelVersion: 2.0.4
  server:
    instanceType: ml.g5.8xlarge
  metrics:
    enabled: true
  environmentVariables:
    - name: SAMPLE_ENV_VAR
      value: "sample_value"
  maxDeployTimeInSeconds: 1800
  tlsConfig:
    tlsCertificateOutputS3Uri: "s3://{USER}-tls-bucket-{REGION}/certificates"
  autoScalingSpec:
    minReplicaCount: 0
    maxReplicaCount: 5
    pollingInterval: 15
    initialCooldownPeriod: 60
    cooldownPeriod: 120
    scaleDownStabilizationTime: 60
    scaleUpStabilizationTime: 0
    cloudWatchTrigger:
        name: "SageMaker-Invocations"
        namespace: "AWS/SageMaker"
        useCachedMetrics: false
        metricName: "Invocations"
        targetValue: 10.5
        activationTargetValue: 5.0
        minValue: 0.0
        metricCollectionStartTime: 300
        metricCollectionPeriod: 30
        metricStat: "Sum"
        metricType: "Average"
        dimensions:
          - name: "EndpointName"
            value: "deepsek7bsme624"
          - name: "VariantName"
            value: "AllTraffic"
    prometheusTrigger:
        name: "Prometheus-Trigger"
        useCachedMetrics: false
        serverAddress: http://<prometheus-host>:9090
        query: sum(rate(http_requests_total{deployment="my-deployment"}[2m]))
        targetValue: 10.0
        activationTargetValue: 5.0
        namespace: "namespace"
        customHeaders: "X-Client-Id=cid"
        metricType: "Value"
```

### Explanation of fields used in deployment YAML

`minReplicaCount` (Optional, Integer)

Specifies the minimum number of model deployment replicas to
maintain in the cluster. During scale-down events, the deployment
scales down to this minimum number of pods. Must be greater than or
equal to 0. Default: 1.

`maxReplicaCount` (Optional, Integer)

Specifies the maximum number of model deployment replicas to
maintain in the cluster. Must be greater than or equal to
`minReplicaCount`. During scale-up events, the
deployment scales up to this maximum number of pods. Default: 5.

`pollingInterval` (Optional, Integer)

The time interval in seconds for querying metrics. Minimum: 0.
Default: 30 seconds.

`cooldownPeriod` (Optional, Integer)

The time interval in seconds to wait before scaling down from 1 to
0 pods during a scale-down event. Only applies when
`minReplicaCount` is set to 0. Minimum: 0. Default:
300 seconds.

`initialCooldownPeriod` (Optional, Integer)

The time interval in seconds to wait before scaling down from 1 to
0 pods during initial deployment. Only applies when
`minReplicaCount` is set to 0. Minimum: 0. Default:
300 seconds.

`scaleDownStabilizationTime` (Optional, Integer)

The stabilization time window in seconds after a scale-down
trigger activates before scaling down occurs. Minimum: 0. Default:
300 seconds.

`scaleUpStabilizationTime` (Optional, Integer)

The stabilization time window in seconds after a scale-up trigger
activates before scaling up occurs. Minimum: 0. Default: 0
seconds.

`cloudWatchTrigger`

The trigger configuration for CloudWatch metrics used in autoscaling
decisions. The following fields are available in
`cloudWatchTrigger`:

- `name` (Optional, String) - Name for the
  CloudWatch trigger. If not provided, uses the default
  format:
  <model-deployment-name>-scaled-object-cloudwatch-trigger.
- `useCachedMetrics` (Optional, Boolean) -
  Determines whether to cache metrics queried by KEDA. KEDA
  queries metrics using the pollingInterval, while the
  Horizontal Pod Autoscaler (HPA) requests metrics from KEDA
  every 15 seconds. When set to true, queried metrics are
  cached and used to serve HPA requests. Default: true.
- `namespace` (Required, String) - The CloudWatch
  namespace for the metric to query.
- `metricName` (Required, String) - The name of
  the CloudWatch metric.
- `dimensions` (Optional, List) - The list of
  dimensions for the metric. Each dimension includes a name
  (dimension name - String) and value (dimension value -
  String).
- `targetValue` (Required, Float) - The target
  value for the CloudWatch metric used in autoscaling
  decisions.
- `activationTargetValue` (Optional, Float) - The
  target value for the CloudWatch metric used when scaling
  from 0 to 1 pod. Only applies when
  `minReplicaCount` is set to 0. Default:

0.

- `minValue` (Optional, Float) - The value to use
  when the CloudWatch query returns no data. Default:

0.

- `metricCollectionStartTime` (Optional, Integer)

* The start time for the metric query, calculated as
  T-metricCollectionStartTime. Must be greater than or equal
  to metricCollectionPeriod. Default: 300 seconds.

- `metricCollectionPeriod` (Optional, Integer) -
  The duration for the metric query in seconds. Must be a
  CloudWatch-supported value (1, 5, 10, 30, or a multiple of
  60). Default: 300 seconds.
- `metricStat` (Optional, String) - The statistic
  type for the CloudWatch query. Default:
  `Average`.
- `metricType` (Optional, String) - Defines how
  the metric is used for scaling calculations. Default:
  `Average`. Allowed values:
  `Average`, `Value`.
  - **Average**: Desired
    replicas = ceil (Metric Value) /
    (targetValue)
  - **Value**: Desired
    replicas = (current replicas) × ceil (Metric Value)
    / (targetValue)

`prometheusTrigger`

The trigger configuration for Amazon Managed Prometheus (AMP)
metrics used in autoscaling decisions. The following fields are
available in `prometheusTrigger`:

- `name` (Optional, String) - Name for the
  CloudWatch trigger. If not provided, uses the default
  format:
  <model-deployment-name>-scaled-object-cloudwatch-trigger.
- `useCachedMetrics` (Optional, Boolean) -
  Determines whether to cache metrics queried by KEDA. KEDA
  queries metrics using the pollingInterval, while the
  Horizontal Pod Autoscaler (HPA) requests metrics from KEDA
  every 15 seconds. When set to true, queried metrics are
  cached and used to serve HPA requests. Default: true.
- `serverAddress` (Required, String) - The
  address of the AMP server. Must use the format:
  <https://aps-workspaces.<region>.amazonaws.com/workspaces/<workspace_id>
- `query` (Required, String) - The PromQL query
  used for the metric. Must return a scalar value.
- `targetValue` (Required, Float) - The target
  value for the CloudWatch metric used in autoscaling
  decisions.
- `activationTargetValue` (Optional, Float) - The
  target value for the CloudWatch metric used when scaling
  from 0 to 1 pod. Only applies when
  `minReplicaCount` is set to 0. Default:

0.

- `namespace` (Optional, String) - The namespace
  to use for namespaced queries. Default: empty string
  (`""`).
- `customHeaders` (Optional, String) - Custom
  headers to include when querying the Prometheus endpoint.
  Default: empty string ("").
- `metricType` (Optional, String) - Defines how
  the metric is used for scaling calculations. Default:
  `Average`. Allowed values:
  `Average`, `Value`.
  - **Average**: Desired
    replicas = ceil (Metric Value) /
    (targetValue)
  - **Value**: Desired
    replicas = (current replicas) × ceil (Metric Value)
    / (targetValue)

## Using KEDA

ScaledObject yaml definitions through kubectl

In addition to configuring autoscaling through the autoScalingSpec section in your
deployment YAML, you can create and apply standalone KEDA `ScaledObject`
YAML definitions using kubectl.

This approach provides greater flexibility for complex scaling scenarios and
allows you to manage autoscaling policies independently from your model deployments.
KEDA `ScaledObject` configurations support a [wide range of scaling triggers](https://keda.sh/docs/2.17/scalers/ "https://keda.sh/docs/2.17/scalers/")
including CloudWatch metrics, Amazon SQS queue lengths, Prometheus queries, and resource-based
metrics like CPU and memory utilization. You can apply these configurations to
existing model deployments by referencing the deployment name in the scaleTargetRef
section of the ScaledObject specification.

###### Note

Ensure the keda operator role provided during the HyperPod Inference
operator installation has adequate permissions to query the metrics defined in
the scaled object triggers.

### CloudWatch metrics

The following KEDA yaml policy uses CloudWatch metrics as a trigger to perform
autoscaling on a kubernetes deployment. The policy queries the number of
invocations for a Sagemaker endpoint and scales the number of deployment pods.
The complete list of parameters supported by KEDA for
`aws-cloudwatch` trigger can be found at [https://keda.sh/docs/2.17/scalers/aws-cloudwatch/](https://keda.sh/docs/2.17/scalers/aws-cloudwatch/ "https://keda.sh/docs/2.17/scalers/aws-cloudwatch/").

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 1 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  triggers:
  - type: aws-cloudwatch
    metadata:
      namespace: AWS/SageMaker
      metricName: Invocations
      targetMetricValue: "1"
      minMetricValue: "1"
      awsRegion: "us-west-2"
      dimensionName: EndpointName;VariantName
      dimensionValue: $ENDPOINT_NAME;$VARIANT_NAME
      metricStatPeriod: "30" # seconds
      metricStat: "Sum"
      identityOwner: operator
```

### Amazon SQS metrics

The following KEDA yaml policy uses Amazon SQS metrics as a trigger to perform
autoscaling on a kubernetes deployment. The policy queries the number of
invocations for a Sagemaker endpoint and scales the number of deployment pods.
The complete list of parameters supported by KEDA for
`aws-cloudwatch` trigger can be found at [https://keda.sh/docs/2.17/scalers/aws-sqs/](https://keda.sh/docs/2.17/scalers/aws-sqs/ "https://keda.sh/docs/2.17/scalers/aws-sqs/").

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 1 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  triggers:
  - type: aws-sqs-queue
    metadata:
      queueURL: https://sqs.eu-west-1.amazonaws.com/account_id/QueueName
      queueLength: "5"  # Default: "5"
      awsRegion: "us-west-1"
      scaleOnInFlight: true
      identityOwner: operator
```

### Prometheus metrics

The following KEDA yaml policy uses Prometheus metrics as a trigger to perform
autoscaling on a kubernetes deployment. The policy queries the number of
invocations for a Sagemaker endpoint and scales the number of deployment pods.
The complete list of parameters supported by KEDA for
`aws-cloudwatch` trigger can be found at [https://keda.sh/docs/2.17/scalers/prometheus/](https://keda.sh/docs/2.17/scalers/prometheus/ "https://keda.sh/docs/2.17/scalers/prometheus/").

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 1 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://<prometheus-host>:9090
      query: avg(rate(http_requests_total{deployment="$DEPLOYMENT_NAME"}[2m])) # Note: query must return a vector/scalar single element response
      threshold: '100.50'
      namespace: example-namespace  # for namespaced queries, eg. Thanos
      customHeaders: X-Client-Id=cid,X-Tenant-Id=tid,X-Organization-Id=oid # Optional. Custom headers to include in query. In case of auth header, use the custom authentication or relevant authModes.
      unsafeSsl: "false" #  Default is `false`, Used for skipping certificate check when having self-signed certs for Prometheus endpoint
      timeout: 1000 # Custom timeout for the HTTP client used in this scaler
      identityOwner: operator
```

### CPU metrics

The following KEDA yaml policy uses cpu metric as a trigger to perform
autoscaling on a kubernetes deployment. The policy queries the number of
invocations for a Sagemaker endpoint and scales the number of deployment pods.
The complete list of parameters supported by KEDA for
`aws-cloudwatch` trigger can be found at [https://keda.sh/docs/2.17/scalers/prometheus/](https://keda.sh/docs/2.17/scalers/prometheus/ "https://keda.sh/docs/2.17/scalers/prometheus/").

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 1 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  triggers:
  - type: cpu
    metricType: Utilization # Allowed types are 'Utilization' or 'AverageValue'
    metadata:
        value: "60"
        containerName: "" # Optional. You can use this to target a specific container
```

### Memory metrics

The following KEDA yaml policy uses Prometheus metrics query as a trigger to
perform autoscaling on a kubernetes deployment. The policy queries the number of
invocations for a Sagemaker endpoint and scales the number of deployment pods.
The complete list of parameters supported by KEDA for
`aws-cloudwatch` trigger can be found at [https://keda.sh/docs/2.17/scalers/prometheus/](https://keda.sh/docs/2.17/scalers/prometheus/ "https://keda.sh/docs/2.17/scalers/prometheus/").

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 1 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  triggers:
  - type: memory
    metricType: Utilization # Allowed types are 'Utilization' or 'AverageValue'
    metadata:
        value: "60"
        containerName: "" # Optional. You can use this to target a specific container in a pod
```

## Sample Prometheus policy for scaling down to 0 pods

The following KEDA yaml policy uses prometheus metrics query as a trigger to
perform autoscaling on a kubernetes deployment. This policy uses a
`minReplicaCount` of 0 which enables KEDA to scale the deployment
down to 0 pods. When `minReplicaCount` is set to 0, you need to provide
an activation criteria in order to bring up the first pod, after the pods scale down
to 0. For the Prometheus trigger, this value is provided by
`activationThreshold`. For the SQS queue, it comes from
`activationQueueLength`.

###### Note

While using `minReplicaCount` of 0, make sure the activation does
not depend on a metric that is being generated by the pods. When the pods scale
down to 0, that metric will never be generated and the pods will not scale up
again.

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: invocations-scaledobject # name of the scaled object that will be created by this
  namespace: ns-team-a # namespace that this scaled object targets
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME # name of the model deployment
  minReplicaCount: 0 # minimum number of pods to be maintained
  maxReplicaCount: 4 # maximum number of pods to scale to
  pollingInterval: 10
  cooldownPeriod:  30
  initialCooldownPeriod:  180 # time before scaling down the pods after initial deployment
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://<prometheus-host>:9090
      query: sum(rate(http_requests_total{deployment="my-deployment"}[2m])) # Note: query must return a vector/scalar single element response
      threshold: '100.50'
      activationThreshold: '5.5' # Required if minReplicaCount is 0 for initial scaling
      namespace: example-namespace
      timeout: 1000
      identityOwner: operator
```

###### Note

The CPU and Memory triggers can scale to 0 only when you define at least one
additional scaler which is not CPU or Memory (eg. SQS + CPU, or Prometheus +
CPU).
