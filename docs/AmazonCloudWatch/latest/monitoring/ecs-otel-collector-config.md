

# Step 2: Create the collector configuration
<a name="ecs-otel-collector-config"></a>

Save the following configuration. You pass it to the collector in step 3.

```
extensions:
  sigv4auth/cloudwatch:
    region: ${env:AWS_REGION}
    service: monitoring

receivers:
  awsecscontainermetrics:
    collection_interval: 60s

processors:
  memory_limiter:
    check_interval: 1s
    limit_percentage: 80
    spike_limit_percentage: 20
  metric_start_time:
    strategy: true_reset_point
  resource/trim:
    attributes:
      - {key: cloud.account.id,              action: delete}
      - {key: cloud.region,                  action: delete}
      - {key: aws.ecs.task.arn,              action: delete}
      - {key: aws.ecs.task.version,          action: delete}
      - {key: aws.ecs.task.pull_started_at,  action: delete}
      - {key: aws.ecs.task.pull_stopped_at,  action: delete}
      - {key: aws.ecs.task.known_status,     action: delete}
      - {key: aws.ecs.docker.name,           action: delete}
      - {key: aws.ecs.container.created_at,  action: delete}
      - {key: aws.ecs.container.started_at,  action: delete}
      - {key: aws.ecs.container.finished_at, action: delete}
      - {key: aws.ecs.container.known_status, action: delete}
      - {key: aws.ecs.container.image.id,    action: delete}
      - {key: container.id,                  action: delete}
  batch:
    send_batch_size: 512
    timeout: 10s

exporters:
  otlp_http/cloudwatch:
    metrics_endpoint: https://monitoring.${env:AWS_REGION}.amazonaws.com/v1/metrics
    auth:
      authenticator: sigv4auth/cloudwatch

service:
  extensions: [sigv4auth/cloudwatch]
  telemetry:
    logs:
      level: warn
    metrics:
      level: none
  pipelines:
    metrics:
      receivers: [awsecscontainermetrics]
      processors: [memory_limiter, metric_start_time, resource/trim, batch]
      exporters: [otlp_http/cloudwatch]
```

This configuration does the following:
+ **Collects every 60 seconds** The receiver's default is 20 seconds, which triples the ingested volume.
+ **Sets a start time on cumulative metrics** with the `metric_start_time` processor. The receiver reports cumulative counters, such as storage bytes, without a start time, and CloudWatch rejects those data points. This processor is required.
+ **Removes attributes that are rarely queried** Each resource attribute is sent with every data point and counts toward ingested bytes. CloudWatch adds `@aws.account` and `@aws.region` labels to every series, so the configuration removes the account and Region attributes. To keep any of the removed attributes, delete its line.
+ **Opens no listening ports,** because the collector's own telemetry endpoint is turned off.

**Note**  
Collector versions earlier than 0.165.0 use the component names `metricstarttime` and `otlphttp`. Version 0.165.0 accepts the old names but logs a deprecation warning.