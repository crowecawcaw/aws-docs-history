

# Prerequisites

Before you begin, make sure that you have the following:
+ **Task metadata endpoint version 4** Tasks on Fargate must use platform version 1.4.0 or later. Tasks on Amazon EC2 must use Amazon ECS container agent version 1.39.0 or later.
+ **A collector image** Use the OpenTelemetry Collector Contrib distribution, `otel/opentelemetry-collector-contrib`, version 0.165.0 or later. Pin a specific version rather than `latest`. If you build your own distribution, include these components:
  + `awsecscontainermetrics` receiver
  + `memory_limiter`, `metric_start_time`, `resource`, and `batch` processors
  + `otlp_http` exporter
  + `sigv4auth` extension
+ **No duplicate collection** If Container Insights is turned on for the cluster, Amazon ECS already collects task and container metrics for it. To check, run the following AWS CLI command.

  ```
  aws ecs describe-clusters --clusters {{cluster-name}} --include SETTINGS --query 'clusters[0].settings'
  ```