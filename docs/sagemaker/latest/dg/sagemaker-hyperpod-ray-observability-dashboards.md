# Ray Grafana dashboards

The SageMaker HyperPod Observability add-on provisions Grafana dashboards for your Ray workloads.
You get them without importing dashboard JSON yourself.

The add-on provisions the following dashboards:

- **Ray Core** — cluster resources, tasks,
  actors, and node state.
- **Ray Data** — dataset throughput and operator
  progress.
- **Ray Train** — training run progress and
  worker state.
- **Ray Serve** — request rate, latency, and
  replica state.

## Filtering a dashboard

Each dashboard exposes filters so you can scope a view to one workload:

- **Cluster name** — the
  HyperPod cluster, backed by the `cluster_name` label
- **Cluster ID** — the
  HyperPod cluster, backed by `cluster_id`
- **Namespace** — backed by
  `namespace`
- **Ray cluster** — the Ray
  cluster, backed by `ray_io_cluster`

Set the filters to a running cluster to see its metrics. For more information about
opening Grafana and access roles, see [Observability for Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS](sagemaker-hyperpod-eks-cluster-observability.md "sagemaker-hyperpod-eks-cluster-observability.md").
