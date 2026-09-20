

# Monitoring Beanstalk Cluster environments
<a name="monitoring-cluster-environments"></a>

A Beanstalk Cluster environment reports environment-level health through the same Elastic Beanstalk health model and APIs as a Beanstalk Standard environment. You view its health color and status in the Elastic Beanstalk console, and you can call `DescribeEnvironmentHealth` to read the current color, status, and the causes that explain it. Health colors and statuses have the same meanings in both modes.

When a Beanstalk Cluster environment uses an Application Load Balancer, Elastic Beanstalk determines application health from the environment's load balancer metrics: the request rate, the proportion of requests that return HTTP 4xx and 5xx responses, and response latency. An environment that serves requests successfully reports a healthy status. As the proportion of failing requests rises, the status becomes progressively more severe. An environment that receives too little traffic for Elastic Beanstalk to evaluate reports that the request rate is insufficient to determine health, which is expected for an idle environment. If you set the load balancer type to `None`, this load balancer evaluation doesn't apply.

Unlike a Beanstalk Standard environment, a Beanstalk Cluster environment doesn't report per-instance health. Beanstalk Cluster doesn't use the on-instance health agent, and the instance-level health reporting settings that apply to Standard environments don't apply.

Container probes control when application replicas receive traffic and when they restart: a readiness probe removes an unready copy from service, a liveness probe restarts a copy that stays unhealthy, and a startup probe gives a slow-starting copy time to initialize. Configure probes with the probe namespaces under `aws:elasticbeanstalk:eks:environment`. See [The container probe namespaces](command-options-general-eks.md#command-options-eks-probes).

## Metrics, logs, and traces
<a name="monitoring-cluster-environments-observability"></a>

Application observability is separate from environment health. You select the backends for your application's metrics, logs, and traces with the configuration options in the `aws:elasticbeanstalk:eks:observability` namespace. By default, Elastic Beanstalk sends your application's metrics and logs to Amazon CloudWatch (CloudWatch), and traces have no backend. You can send logs to Amazon S3 instead, send metrics to Amazon Managed Service for Prometheus, and send traces to AWS X-Ray. You can also send any of the three to a third-party backend that accepts OpenTelemetry data; see [Sending observability data to a third-party backend](#monitoring-cluster-environments-custom-backend). For the available options, see [aws:elasticbeanstalk:eks:observability](command-options-general-eks.md#command-options-eks-observability).

Elastic Beanstalk provisions and operates the collection components and publishes infrastructure metrics on your behalf. You are responsible for instrumenting your application so that it emits the metrics, logs, and traces that you want, and for providing and maintaining access to any destination that you select.

Your application has to emit OpenTelemetry data for a backend to receive anything. To get that without changing your application, set the `language` option in the `aws:elasticbeanstalk:eks:environment` namespace to your application's runtime. Elastic Beanstalk adds OpenTelemetry auto-instrumentation for that runtime to your container, which applies to every backend, AWS and third-party alike. Auto-instrumentation is available for Java, Node.js, Python, and .NET applications. For a Java application, the agent also bridges Log4j2, Logback, and `java.util.logging`, so that your application's logs reach the logs backend without any application changes.

Separately from the logs backend, Elastic Beanstalk collects a deployment log for each environment operation. It contains your pods' container logs and the Kubernetes events from the operation, which makes it the place to look when an operation fails. For more information, see [Deployment logs](environments-deployment-logs.md).

### Finding your logs and metrics in CloudWatch
<a name="monitoring-cluster-environments-destinations"></a>

With the default backends, Elastic Beanstalk writes to four CloudWatch log groups. The log group names are fixed and you can't change them.


**CloudWatch log groups for Beanstalk Cluster environments**  

| **Log group** | **Contents** | **Log stream name** | **When it exists** | 
| --- | --- | --- | --- | 
| `/aws/elasticbeanstalk/application/logs` | Output from your application's containers. | `eb-{{environment-name}}.{{pod-name}}` | When `logs-backend` is `cloudwatch`, the default. | 
| `/aws/elasticbeanstalk/application/metrics` | Metrics that your application emits. | `{{environment-name}}/{{pod-name}}` | When `metrics-backend` is `cloudwatch`, the default, and your application emits metrics. | 
| `/aws/elasticbeanstalk/infrastructure/logs` | Output from the components that Elastic Beanstalk runs on the cluster on your behalf. | `{{kubernetes-namespace}}.{{pod-name}}` | Always. | 
| `/aws/elasticbeanstalk/infrastructure/metrics` | The metrics that Elastic Beanstalk publishes for you, in embedded metric format. | `{{kubernetes-namespace}}.{{pod-name}}` | Always. | 

**Note**  
These log groups are shared. Every Beanstalk Cluster environment in an AWS account and Region writes to the same four groups, across every cluster. Your environment's data is separated by log stream name, not by log group. Elastic Beanstalk runs each environment in a Kubernetes namespace named `eb-` followed by the environment name, so your application's log streams begin with `eb-{{environment-name}}` and a period. Your application's metric streams begin with the environment name and a slash, with no `eb-` prefix.

Elastic Beanstalk creates these log groups without a retention policy, so their contents never expire. Log stream names contain the pod name, so every deployment creates new streams and the streams from earlier deployments remain. Set a retention policy on each log group to limit what you store.

The metrics that Elastic Beanstalk publishes for you arrive in three CloudWatch namespaces. All three are custom namespaces, which you pay for per metric. Beanstalk Standard environments instead publish to the `AWS/ElasticBeanstalk` namespace, which CloudWatch provides at no charge. A Beanstalk Cluster environment publishes the container metrics below for each of its replicas, so the number of custom metrics grows with the number of replicas that you run. For the current rates, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).


**CloudWatch metrics for Beanstalk Cluster environments**  

| **Namespace** | **Metrics** | **Dimensions** | 
| --- | --- | --- | 
| `ElasticBeanstalk/Infrastructure` | For your application's containers: `container_cpu_usage_seconds_total`, `container_memory_working_set_bytes`, and `EnvironmentReplicas`, the number of replicas that are ready. | The two container metrics are published with `namespace`, `pod`, `container` and again with `namespace` alone. `EnvironmentReplicas` is published with `namespace` only. | 
| `ElasticBeanstalk/System` | The same two container metrics, for the components that Elastic Beanstalk runs on the cluster on your behalf rather than for your application. | `namespace`, `pod`, `container`, and again with `namespace` alone. | 
| `ElasticBeanstalk/Application` | The metrics that your application emits, including the runtime metrics that auto-instrumentation produces. | `EnvironmentName`. Request duration is also published with `http.method`, `http.route`, and `http.status_code`. | 

The `namespace` dimension is the Kubernetes namespace, so its value is `eb-` followed by your environment name. The `ElasticBeanstalk/Application` namespace instead uses an `EnvironmentName` dimension whose value is the environment name on its own. Use the value that matches the namespace you are querying.

If you set `logs-backend` to `s3`, Elastic Beanstalk writes your application's logs to a bucket named `elasticbeanstalk-logs-{{account-id}}-{{region}}-an` instead, under a key built from the Kubernetes namespace, the pod name, and the date, and nothing goes to `/aws/elasticbeanstalk/application/logs`. Elastic Beanstalk batches these uploads, so an object can take up to a minute to appear. If you set `logs-backend` or `metrics-backend` to `custom`, that data goes to the backend you configure and doesn't appear in any of these log groups. See [Sending observability data to a third-party backend](#monitoring-cluster-environments-custom-backend).

## Sending observability data to a third-party backend
<a name="monitoring-cluster-environments-custom-backend"></a>

Beanstalk Cluster collects your application's telemetry with the OpenTelemetry collector, so you can send it to any backend that accepts OpenTelemetry data, such as Datadog or Splunk, instead of to an AWS destination. You supply the pipeline configuration and the credentials it needs, and Elastic Beanstalk runs your pipeline as a sidecar container in your application's pod.

Configuring a third-party backend takes four things:

1. Set each signal you want to redirect to `custom`. The signals are independent, so you can send metrics and logs to a third-party backend while traces continue to go to AWS X-Ray. Use `metrics-backend`, `logs-backend`, and `traces-backend` in the `aws:elasticbeanstalk:eks:observability` namespace.

1. Set `custom-config` to the collector's pipeline configuration, as JSON. Reference each credential as a `${{{NAME}}}` placeholder rather than putting the value in the configuration.

1. Store the credentials in AWS Secrets Manager and set `custom-credentials` to the secret's ARN. The secret value must be a JSON object whose keys match the placeholder names in your configuration.

1. Set the `application-role` option in the `aws:elasticbeanstalk:eks:environment` namespace, and grant that role permission to read the secret. The collector uses the application role at run time, not the observability role, and it reaches the secret through the pod's identity, which exists only when `application-role` is set. Without it, the mount fails and your replicas never start.

The following example sends metrics and logs to Datadog and keeps traces going to AWS X-Ray. First, create the secret that holds the credentials your configuration references:

```
$ aws secretsmanager create-secret \
    --name {{my-app/otel-credentials}} \
    --secret-string '{"DD_API_KEY":"{{your-api-key}}"}'
```

Grant the application role permission to read it, so that the collector can fetch it at run time:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "{{arn:aws:secretsmanager:us-east-1:111122223333:secret:my-app/otel-credentials-AbCdEf}}"
    }
  ]
}
```

Elastic Beanstalk refreshes the mounted credentials on a schedule, and the refresh checks the secret's current version, so grant `secretsmanager:DescribeSecret` in addition to `secretsmanager:GetSecretValue`. An environment starts with `GetSecretValue` alone, but each later refresh fails.

Next, put the option settings in a file. A collector configuration contains commas, which the shorthand syntax of `--option-settings` treats as separators, so pass the settings as JSON instead. Save the following as `options.json`, with the pipeline configuration as a JSON string in the `custom-config` value:

```
[
  {
    "Namespace": "aws:elasticbeanstalk:eks:observability",
    "OptionName": "metrics-backend",
    "Value": "custom"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:observability",
    "OptionName": "logs-backend",
    "Value": "custom"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:observability",
    "OptionName": "traces-backend",
    "Value": "xray"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:observability",
    "OptionName": "custom-config",
    "Value": "{\"receivers\":{\"otlp\":{\"protocols\":{\"grpc\":{\"endpoint\":\"0.0.0.0:4317\"},\"http\":{\"endpoint\":\"0.0.0.0:4318\"}}}},\"processors\":{\"batch\":{}},\"exporters\":{\"datadog\":{\"api\":{\"site\":\"{{datadoghq.com}}\",\"key\":\"${DD_API_KEY}\"}}},\"service\":{\"pipelines\":{\"metrics\":{\"receivers\":[\"otlp\"],\"processors\":[\"batch\"],\"exporters\":[\"datadog\"]},\"logs\":{\"receivers\":[\"otlp\"],\"processors\":[\"batch\"],\"exporters\":[\"datadog\"]}}}}"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:observability",
    "OptionName": "custom-credentials",
    "Value": "{{arn:aws:secretsmanager:us-east-1:111122223333:secret:my-app/otel-credentials-AbCdEf}}"
  }
]
```

Set `site` to the Datadog site that your organization uses. Then apply the file:

```
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings file://options.json
```

Define a pipeline for each signal that you set to `custom`. A signal that you leave on an AWS destination keeps using the collection that Elastic Beanstalk operates, and needs no pipeline of its own.

Components with no settings take an empty object, as `"batch": {}`. The `receivers` block is optional. If you omit it, Elastic Beanstalk adds the OTLP receiver that your application sends to, and records an environment event that reports the addition. The preceding example defines the receiver explicitly.

While you are setting this up, add a `debug` exporter to each pipeline and include it in the pipeline's `exporters` list. The collector then logs the telemetry it receives and exports, which tells you whether data is reaching the collector, and separately whether the collector can reach your backend.