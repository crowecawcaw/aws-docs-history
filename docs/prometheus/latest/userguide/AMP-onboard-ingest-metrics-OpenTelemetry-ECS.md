# Set up metrics

ingestion from Amazon ECS using AWS Distro for Open Telemetry

This section explains how to collect metrics from Amazon Elastic Container Service (Amazon ECS) and ingest
them into Amazon Managed Service for Prometheus using AWS Distro for Open Telemetry (ADOT). It also describes
how to visualize your metrics in Amazon Managed Grafana.

## Prerequisites

###### Important

Before you begin, you must have an Amazon ECS environment on an AWS Fargate
cluster with default settings, an Amazon Managed Service for Prometheus workspace, and an Amazon Managed Grafana
workspace. We assume that you are familiar with container workloads,
Amazon Managed Service for Prometheus, and Amazon Managed Grafana.

For more information, see the following links:

- For information about how to create an Amazon ECS environment on a
  Fargate cluster with default settings, see [Creating a cluster](../../../AmazonECS/latest/developerguide/create_cluster.md "../../../AmazonECS/latest/developerguide/create_cluster.md") in the _Amazon ECS Developer
  Guide_.
- For information about how to create an Amazon Managed Service for Prometheus workspace, see [Create a workspace](AMP-onboard-create-workspace.md "AMP-onboard-create-workspace.md") in the _Amazon Managed Service for Prometheus User
  Guide_.
- For information about how to create an Amazon Managed Grafana workspace, see [Creating a workspace](../../../grafana/latest/userguide/AMG-create-workspace.md "../../../grafana/latest/userguide/AMG-create-workspace.md") in the _Amazon Managed Grafana User
  Guide_.

## Step 1:

Define a custom ADOT collector container image

Use the following config file as a template to define your own ADOT collector
container image. Replace `my-remote-URL` and
`my-region` with your `endpoint` and
`region` values. Save the config in a file called
_adot-config.yaml_.

###### Note

This configuration uses the `sigv4auth` extension to
authenticate calls to Amazon Managed Service for Prometheus. For more information about configuring
`sigv4auth`, see [Authenticator - Sigv4](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/sigv4authextension "https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/sigv4authextension") on GitHub.

```
receivers:
  prometheus:
    config:
      global:
        scrape_interval: 15s
        scrape_timeout: 10s
      scrape_configs:
      - job_name: "prometheus"
        static_configs:
        - targets: [ 0.0.0.0:9090 ]
  awsecscontainermetrics:
    collection_interval: 10s
processors:
  filter:
    metrics:
      include:
        match_type: strict
        metric_names:
          - ecs.task.memory.utilized
          - ecs.task.memory.reserved
          - ecs.task.cpu.utilized
          - ecs.task.cpu.reserved
          - ecs.task.network.rate.rx
          - ecs.task.network.rate.tx
          - ecs.task.storage.read_bytes
          - ecs.task.storage.write_bytes
exporters:
  prometheusremotewrite:
    endpoint: `my-remote-URL`
    auth:
      authenticator: sigv4auth
  logging:
    loglevel: info
extensions:
  health_check:
  pprof:
    endpoint: :1888
  zpages:
    endpoint: :55679
  sigv4auth:
    region: `my-region`
    service: aps
service:
  extensions: [pprof, zpages, health_check, sigv4auth]
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [logging, prometheusremotewrite]
    metrics/ecs:
      receivers: [awsecscontainermetrics]
      processors: [filter]
      exporters: [logging, prometheusremotewrite]
```

## Step 2: Push

your ADOT collector container image to an Amazon ECR repository

Use a Dockerfile to create and push your container image to an Amazon Elastic Container Registry (ECR)
repository.

1. Build the Dockerfile to copy and add your container image to the OTEL
   Docker image.

```
FROM public.ecr.aws/aws-observability/aws-otel-collector:latest
COPY adot-config.yaml /etc/ecs/otel-config.yaml
CMD ["--config=/etc/ecs/otel-config.yaml"]
```

2. Create an Amazon ECR repository.

```
# create repo:
COLLECTOR_REPOSITORY=$(aws ecr create-repository --repository aws-otel-collector \
                               --query repository.repositoryUri --output text)
```

3. Create your container image.

```
# build ADOT collector image:
docker build -t $COLLECTOR_REPOSITORY:ecs .
```

###### Note

This assumes you are building your container in the same
environment that it will run in. If not, you may need to use the
`--platform` parameter when building the
image. 4. Sign in to the Amazon ECR repository. Replace
`my-region` with your `region`
value.

```
# sign in to repo:
aws ecr get-login-password --region `my-region` | \
        docker login --username AWS --password-stdin $COLLECTOR_REPOSITORY
```

5. Push your container image.

```
# push ADOT collector image:
docker push $COLLECTOR_REPOSITORY:ecs
```

## Step 3:

Create an Amazon ECS task definition to scrape Amazon Managed Service for Prometheus

Create an Amazon ECS task definition to scrape Amazon Managed Service for Prometheus. Your task definition
should include a container named `adot-collector` and a container
named `prometheus`. `prometheus` generates metrics, and
`adot-collector` scrapes `prometheus`.

###### Note

Amazon Managed Service for Prometheus runs as a service, collecting metrics from containers. The
containers in this case run Prometheus locally, in Agent mode, which send
the local metrics to Amazon Managed Service for Prometheus.

**Example: Task definition**

The following is an example of how your task definition might look. You can
use this example as a template to create your own task definition. Replace the
`image` value of `adot-collector` with your repository
URL and image tag (`$COLLECTOR_REPOSITORY:ecs`). Replace the
`region` values of `adot-collector` and
`prometheus` with your `region` values.

```
{
  "family": "adot-prom",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "adot-collector",
      "image": "`account_id`.dkr.ecr.`region`.amazonaws.com/`image-tag`",
      "essential": true,
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/ecs-adot-collector",
          "awslogs-region": "`my-region`",
          "awslogs-stream-prefix": "ecs",
          "awslogs-create-group": "True"
        }
      }
    },
    {
      "name": "prometheus",
      "image": "prom/prometheus:main",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/ecs-prom",
          "awslogs-region": "`my-region`",
          "awslogs-stream-prefix": "ecs",
          "awslogs-create-group": "True"
        }
      }
    }
  ],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "cpu": "1024"
}
```

## Step 4:

Give your task permissions to access Amazon Managed Service for Prometheus

To send the scraped metrics to Amazon Managed Service for Prometheus, your Amazon ECS task must have the
correct permissions to call the AWS API operations for you. You must create an
IAM role for your tasks and attach the
`AmazonPrometheusRemoteWriteAccess` policy to it. For more
information about creating this role and attaching the policy, see [Creating an IAM role and policy for your tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role "../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role").

After you attach `AmazonPrometheusRemoteWriteAccess` to your IAM
role, and use that role for your tasks, Amazon ECS can send your scraped metrics to
Amazon Managed Service for Prometheus.

## Step 5:

Visualize your metrics in Amazon Managed Grafana

###### Important

Before you begin, you must run a Fargate task on your Amazon ECS task
definition. Otherwise, Amazon Managed Service for Prometheus can't consume your metrics.

1. From the navigation pane in your Amazon Managed Grafana workspace, choose
   **Data sources** under the AWS icon.
2. On the **Data sources** tab, for
   **Service**, select **Amazon Managed
   Service for Prometheus** and choose your **Default
   Region**.
3. Choose **Add data source**.
4. Use the `ecs` and `prometheus` prefixes to query
   and view your metrics.
