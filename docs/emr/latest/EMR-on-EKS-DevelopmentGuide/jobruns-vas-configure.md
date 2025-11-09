# Configuring vertical autoscaling for

Amazon EMR on EKS

You can configure vertical autoscaling when you submit Amazon EMR Spark jobs through the
[StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") API. Set the autoscaling-related configuration parameters on the
Spark driver pod as shown in the example in [Submitting a Spark job with vertical
autoscaling](jobruns-vas-gs.md#jobruns-vas-spark-submit "jobruns-vas-gs.md#jobruns-vas-spark-submit").

The Amazon EMR on EKS vertical autoscaling operator listens to driver pods that have
autoscaling, then sets up integration with the Kubernetes Vertical Pod Autoscaler (VPA) with
the settings on the driver pod. This facilitates resource tracking and autoscaling of Spark
executor pods.

The following sections describe the parameters that you can use when you configure
vertical autoscaling for your Amazon EKS cluster.

###### Note

Configure the feature toggle parameter as a label, and configure the remaining
parameters as annotations on the Spark driver pod. The autoscaling parameters belong to
the `emr-containers.amazonaws.com/` domain and have the
`dynamic.sizing` prefix.

## Required parameters

You must include the following two parameters on the Spark job driver when you submit
your job:

| Key                        | Description    | Accepted values | Default value | Type       | Spark parameter1                                                                           |
| -------------------------- | -------------- | --------------- | ------------- | ---------- | ------------------------------------------------------------------------------------------ |
| `dynamic.sizing`           | Feature toggle | `true`, `false` | not set       | label      | `spark.kubernetes.driver.label.emr-containers.amazonaws.com/dynamic.sizing`                |
| `dynamic.sizing.signature` | Job signature  | _string_        | not set       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.signature` |

1 Use this parameter as a `SparkSubmitParameter`
or `ConfigurationOverride` in the `StartJobRun` API.

- `dynamic.sizing` – You can turn
  vertical autoscaling on and off with the `dynamic.sizing` label. To turn on
  vertical autoscaling, set `dynamic.sizing` to `true` on the
  Spark driver pod. If you omit this label or set it to any value other than
  `true`, vertical autoscaling is off.
- `dynamic.sizing.signature` – Set
  the job signature with the `dynamic.sizing.signature` annotation on the
  driver pod. Vertical autoscaling aggregates your resource usage data across different
  runs of Amazon EMR Spark jobs to derive resource recommendations. You provide the unique
  identifier to tie the jobs together.

###### Note

If your job recurs at a fixed interval such as daily or weekly, then your job
signature should remain the same for each new instance of the job. This ensures that
vertical autoscaling can compute and aggregate recommendations across different runs
of the job.

1 Use this parameter as a `SparkSubmitParameter`
or `ConfigurationOverride` in the `StartJobRun` API.

## Optional parameters

Vertical autoscaling also supports the following optional parameters. Set them as
annotations on the driver pod.

| Key                               | Description                      | Accepted values                                                                                                                                                                       | Default value | Type       | Spark parameter1                                                                                  |
| --------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| `dynamic.sizing.mode`             | Vertical autoscaling mode        | `Off`, `Initial`, `Auto`                                                                                                                                                              | `Off`         | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.mode`             |
| `dynamic.sizing.scale.memory`     | Enables memory scaling           | _`true`, `false`_                                                                                                                                                                     | `true`        | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.memory`     |
| `dynamic.sizing.scale.cpu`        | Turn CPU scaling on or off       | _`true`, `false`_                                                                                                                                                                     | `false`       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.cpu`        |
| `dynamic.sizing.scale.memory.min` | Minumum limit for memory scaling | _string, [K8s<br>resource quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity "https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity") ex:_<br>`1G` | not set       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.memory.min` |
| `dynamic.sizing.scale.memory.max` | Maximum limit for memory scaling | _string, [K8s<br>resource quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity "https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity") ex:_<br>`4G` | not set       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.memory.max` |
| `dynamic.sizing.scale.cpu.min`    | Minimum limit for CPU scaling    | _string, [K8s<br>resource quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity "https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity") ex:_<br>`1`  | not set       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.cpu.min`    |
| `dynamic.sizing.scale.cpu.max`    | Maximum limit for CPU scaling    | _string, [K8s<br>resource quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity "https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity") ex:_<br>`2`  | not set       | annotation | `spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.scale.cpu.max`    |

### Vertical autoscaling modes

The `mode` parameter maps to the different autoscaling modes that the VPA
supports. Use the `dynamic.sizing.mode` annotation on the driver pod to set
the mode. The following values are supported for this parameter:

- Off – A dry-run mode where you can monitor
  recommendations, but autoscaling is not performed. This is the default mode for
  vertical autoscaling. In this mode, the associated vertical pod autoscaler resource
  computes recommendations, and you can monitor the recommendations through tools like
  kubectl, Prometheus, and Grafana.
- Initial – In this mode, VPA autoscales
  resources when the job starts if recommendations are available based on historic
  runs of the job, such as in the case of a recurring job.
- Auto – In this mode, VPA evicts Spark
  executor pods, and autoscales them with the recommended resource settings when the
  Spark driver pod restarts them. Sometimes, the VPA evicts running Spark executor
  pods, so it might result in additional latency when it retries the interrupted
  executor.

### Resource scaling

When you set up vertical autoscaling, you can choose whether to scale CPU and memory
resources. Set the `dynamic.sizing.scale.cpu` and
`dynamic.sizing.scale.memory` annotations to `true` or
`false`. By default, CPU scaling is set to `false`, and memory
scaling is set to `true`.

### Resource minimums and maximums

(Bounds)

Optionally, you can also set boundaries on the CPU and memory resources. Choose a
minimum and maximum value for these resources with the
`dynamic.sizing.[memory/cpu].[min/max]` annotations when you enable
autoscaling. By default, the resources have no limitations. Set the annotations as
string values that represent a Kubernetes resource quantity. For example, set
`dynamic.sizing.memory.max` to `4G` to represent
4 GB.
