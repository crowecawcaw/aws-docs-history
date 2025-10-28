# Using Autoscaler for Flink applications

The operator autoscaler can help ease backpressure by collecting metrics from Flink jobs and automatically adjusting parallelism on a job vertex level. The following is an example
of what your configuration might look like:

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  ...
spec:
  ...
  flinkVersion: v1_18
  flinkConfiguration:
    job.autoscaler.enabled: "true"
    job.autoscaler.stabilization.interval: 1m
    job.autoscaler.metrics.window: 5m
    job.autoscaler.target.utilization: "0.6"
    job.autoscaler.target.utilization.boundary: "0.2"
    job.autoscaler.restart.time: 2m
    job.autoscaler.catch-up.duration: 5m
    pipeline.max-parallelism: "720"
  ...
```

This configuration uses default values for the latest release of Amazon EMR. If you use other versions,
you might have different values.

###### Note

As of Amazon EMR 7.2.0, you don't need to include the prefix `kubernetes.operator`
in your configuration. If you use 7.1.0 or lower, you must use the prefix before each configuration.
For example, you must specify `kubernetes.operator.job.autoscaler.scaling.enabled`.

The following are configuration options for the autoscaler.

- `job.autoscaler.scaling.enabled` – specifies whether to enable vertex scaling execution by the autoscaler. The default is `true`. If you disable this configuration,
  the autoscaler only collects metrics and evaluates the suggested parallelism for each vertex but doesn't upgrade the jobs.
- `job.autoscaler.stabilization.interval` – the stabilization period in which no new scaling will be executed.
  Default is 5 minutes.
- `job.autoscaler.metrics.window` – the scaling metrics aggregation window size. The larger the window, the more smooth and stability,
  but the autoscaler might be slower to react to sudden load changes. Default is 15 minutes. We recommend you experiment
  by using a value between 3 to 60 minutes.
- `job.autoscaler.target.utilization` – the target vertex utilization to provide stable job performance and some buffer for load fluctuations.
  The default is `0.7` targeting 70% utilization/load for the job vertexes.
- `job.autoscaler.target.utilization.boundary` – the target vertex utilization boundary that serves as extra buffer to avoid
  immediate scaling on load fluctuations. Default is `0.3`, which means 30% deviation from the target utilization is allowed before triggering a scaling action.
- `ob.autoscaler.restart.time` – the expected time to restart the application. Default is 5 minutes.
- `job.autoscaler.catch-up.duration` – the expected time to catch up, meaning fully processing any backlog after a scaling operation completes.
  Default is 5 minutes. By lowering the catch-up duration, the autoscaler haves to reserve more extra capacity for the scaling actions.
- `pipeline.max-parallelism` – the maximum parallelism the autoscaler can use. The autoscaler ignores this limit
  if it is higher than the max parallelism configured in the Flink config or directly on each operator. Default is -1. Note that the autoscaler computes
  the parallelism as a divisor of the max parallelism number therefore it is recommended to choose max parallelism settings that have a lot
  of divisors instead of relying on the Flink provided defaults. We recommend using multiples of 60
  for this configuration, such as 120, 180, 240, 360, 720 etc.
  For a more detailed configuration reference page, see [Autoscaler configuration](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/operations/configuration/#autoscaler-configuration "https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/operations/configuration/#autoscaler-configuration").
