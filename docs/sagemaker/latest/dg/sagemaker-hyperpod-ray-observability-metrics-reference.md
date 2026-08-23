# Ray metrics reference

The SageMaker HyperPod Observability add-on collects the metrics that Ray exports. We do not
add, rename, or remove Ray metrics, so metric names and labels match open source Ray.

The following sections list the metric groups each provisioned dashboard covers. For the
individual metric names, definitions, and types, see [Ray
system metrics](https://docs.ray.io/en/latest/ray-observability/reference/system-metrics.html "https://docs.ray.io/en/latest/ray-observability/reference/system-metrics.html") in the Ray documentation.

## Ray Core metrics

The **Ray Core** dashboard covers system-level Ray state
and the hardware the cluster runs on, across these groups:

- Tasks, actors, and placement groups
- Cluster resources and object store
- Node hardware and OS
- Per-component usage
- Autoscaler state

## Ray Data metrics

The **Ray Data** dashboard covers dataset throughput,
task lifecycle, iteration, and memory pressure, across these groups:

- Rows, bytes, and blocks
- Task counts and lifecycle
- Other operator counters
- Iteration
- Object store and memory budget
- Cluster utilization and budgets

## Ray Train metrics

The **Ray Train** dashboard covers training run and
worker state, checkpointing, and node hardware, across these groups:

- Run and worker state
- Checkpointing and reporting
- Node hardware and OS

## Ray Serve metrics

The **Ray Serve** dashboard covers request rate, latency,
errors, and replica health, across these groups:

- Requests and latency
- Errors and queueing
- Replica and controller health
- Node hardware and cluster state

## Labels for querying

Metrics land in Amazon Managed Service for Prometheus, so you can query them outside
Grafana. The collector adds `cluster_name`, `cluster_id`, and
`namespace`. Ray adds `ray_io_cluster`, which identifies the Ray
cluster and is the label the dashboards pivot on.

For more information about visualizing these metrics, see [Ray Grafana dashboards](sagemaker-hyperpod-ray-observability-dashboards.md "sagemaker-hyperpod-ray-observability-dashboards.md").
