# Metrics collected by Application Signals

Application Signals collects both [standard application metrics](#AppSignals-StandardMetrics "#AppSignals-StandardMetrics")
and [runtime metrics](#AppSignals-StandardMetrics "#AppSignals-StandardMetrics") from the applications that you enable it for.

Standard application metrics relate to the most critical parts of service performance, latency and availability.

Runtime metrics track application metrics over time, including memory usage, CPU usage, and garbage collection. Application Signals
displays the runtime metrics in the context of the services that you have enabled for Application Signals. When you
have an operational issue, observing the runtime metrics can be useful to help you find the root cause of the issue. For example, you can
see if spikes in latency in your service relate to spikes in a runtime metric.

###### Topics

- [Standard application metrics collected](#AppSignals-StandardMetrics "#AppSignals-StandardMetrics")
- [Runtime metrics](#AppSignals-RuntimeMetrics "#AppSignals-RuntimeMetrics")
- [Disabling the collection of runtime metrics](#AppSignals-RuntimeMetrics-Disable "#AppSignals-RuntimeMetrics-Disable")

## Standard application metrics collected

Application Signals collects _standard application metrics_ from the
services that it discovers. These metrics relate to the most critical aspects of a service's
performance: latency, faults, and errors. They can help you identify issues, monitor performance
trends, and optimize resources to improve the overall user experience.

The following table lists the metrics collected by Application Signals. These metrics are
sent to CloudWatch in the `ApplicationSignals` namespace.

| Metric    | Description                                                                                                                                                                                                                                                                         |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Latency` | The delay before data transfer begins after the request is made.<br>Units: Milliseconds                                                                                                                                                                                             |
| `Fault`   | A count of both HTTP 5XX server-side faults and OpenTelemetry span status errors.<br>Units: None                                                                                                                                                                                    |
| `Error`   | A count of HTTP 4XX client-side errors. These are considered to be request errors<br>that are not caused by service problems. Therefore, the `Availability`<br>metric displayed on Application Signals dashboards does not regard these errors as<br>service faults.<br>Units: None |

The `Availability` metric displayed on Application Signals dashboards
is computed as **(1 - `Faults`/Total)\*100**. Total responses includes all responses and is derived from `SampleCount(Latency)`.
Successful responses are
all responses without a `5XX` error.
`4XX` responses are treated as successful when Application Signals calculates `Availability`.

### Dimensions collected and dimension combinations

The following dimensions are defined for each of the standard application metrics. For
more information about dimensions, see [Dimensions](cloudwatch_concepts.md#Dimension "cloudwatch_concepts.md#Dimension").

Different dimensions are collected for _service metrics_ and
_dependency metrics_. Within the services discovered by Application
Signals, when microservice A calls microservice B, microservice B is serving the request. In
this case, microservice A emits dependency metrics and microservice B emits service metrics.
When a client calls microservice A, microservice A is serving the request and emits service
metrics.

**Dimensions for service metrics**

The following dimensions are collected for service metrics.

| Dimension     | Description                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`     | The name of the service.<br>The maximum value is 255 characters.                                                                                                                                                                                                       |
| `Operation`   | The name of the API operation or other activity.<br>The maxiumum value is 1024 characters. You can set service level objectives on<br>operations only if the operation name is 194 characters or fewer.                                                                |
| `Environment` | The name of the environment where services are running. If services are not<br>running on Amazon EKS, you can specify an optional custom value for<br>`deployment.environment` in the<br>`OTEL_ATTRIBUTE_RESOURCES` parameter.<br>The maximum value is 259 characters. |

When you view these metrics in the CloudWatch console, you can view them using the following
dimension combinations:

- `[Environment, Service, Operation, [Latency, Error, Fault]]`
- `[Environment, Service, [Latency, Error, Fault]]`

**Dimensions for dependency metrics**

The following dimensions are collected for dependency metrics:

| Dimension                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`                  | The name of the service.<br>The maximum value is 255 characters.                                                                                                                                                                                                                                                                                                                                                                        |
| `Operation`                | The name of the API operation or other operation.<br>The maximum value is 1024 characters.                                                                                                                                                                                                                                                                                                                                              |
| `RemoteService`            | The name of the remote service being invoked.<br>The maximum value is 255 characters.                                                                                                                                                                                                                                                                                                                                                   |
| `RemoteOperation`          | The name of the API operation being invoked.<br>The maximum value is 1024 characters.                                                                                                                                                                                                                                                                                                                                                   |
| `Environment`              | The name of the environment where services are running. If services are not<br>running on Amazon EKS, you can specify an optional custom value for<br>`deployment.environment` in the<br>`OTEL_ATTRIBUTE_RESOURCES` parameter.<br>The maxiumum value is 259 characters.                                                                                                                                                                 |
| `RemoteEnvironment`        | The name of the environment where dependency services are running. The<br>`RemoteEnvironment` parameter is automatically generated when a service<br>calls a dependency and they are both running in the same cluster. Otherwise,<br>`RemoteEnvironment` is neither generated nor reported in the service<br>dependency's metrics. Currently only available on Amazon EKS and K8S<br>platforms.<br>The maximum value is 259 characters. |
| `RemoteResourceIdentifier` | The name of the resource invoked by a remote call. The<br>`RemoteResourceIdentifier` parameter is automatically generated if<br>service calls a remote AWS service. Otherwise,<br>`RemoteResourceIdentifier` is neither generated nor reported in the<br>service dependency's metrics.<br>The maximum value is 1024 characters.                                                                                                         |
| `RemoteResourceType`       | The type of the resource that is invoked by a remote call. Required only if<br>`RemoteResourceIdentifier` is defined.<br>The maximum value is 1024 characters.                                                                                                                                                                                                                                                                          |

When you view these metrics in the CloudWatch console, you can view them using the following
dimension combinations:

**Running on Amazon EKS clusters**

- `[Environment, Service, Operation, RemoteService, RemoteOperation,
RemoteEnvironment, RemoteResourceIdentifier, RemoteResourceType, [Latency, Error,
Fault]]`
- `[Environment, Service, Operation, RemoteService, RemoteOperation,
RemoteEnvironment, [Latency, Error, Fault]]`
- `[Environment, Service, Operation, RemoteService, RemoteOperation,
RemoteResourceIdentifier, RemoteResourceType, [Latency, Error, Fault]]`
- `[Environment, Service, Operation, RemoteService, RemoteOperation, [Latency,
Error, Fault]]`
- `[Environment, Service, RemoteService, RemoteEnvironment, [Latency, Error,
Fault]]`
- `[Environment, Service, RemoteService, [Latency, Error, Fault]]`
- `[Environment, Service, RemoteService, RemoteOperation, RemoteEnvironment,
RemoteResourceIdentifier, RemoteResourceType, [Latency, Error, Fault]]`
- `[Environment, Service, RemoteService, RemoteOperation, RemoteEnvironment,
[Latency, Error, Fault]]`
- `[Environment, Service, RemoteService, RemoteOperation, RemoteResourceIdentifier,
RemoteResourceType, [Latency, Error, Fault]]`
- `[Environment, Service, RemoteService, RemoteOperation, [Latency, Error,
Fault]]`
- `[RemoteService [Latency, Error,
Fault]]`
- `[RemoteService, RemoteResourceIdentifier, RemoteResourceType [Latency, Error,
Fault]]`

## Runtime metrics

Application Signals uses the AWS Distro for OpenTelemetry SDK to automatically collect OpenTelemetry-compatible metrics from your Java and Python applications.
To have runtime metrics collected, you must meet the following pre-requisites:

- Your CloudWatch agent must be version `1.300049.1` or later.
- If you use the Amazon CloudWatch Observability EKS add-on, it must be version `2.30-eksbuild.1` or later. If you update the add-on, you must restart
  your applications.
- For Java applications, you must be running `1.32.5` or later of the AWS Distro for OpenTelemetry SDK for Java.
- For Python applications, you must be running `0.7.0` or later of the AWS Distro for OpenTelemetry SDK for Python.
- For .Net applications, you must be running `1.6.0` or later of the AWS Distro for OpenTelemetry SDK for .Net.

Runtime metrics are not collected for Node.js applications.

Runtime metric are charged as part of Application Signals costs. For more information about CloudWatch pricing, see
[Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Note

**Known issues**

The runtime metrics collection in the Java SDK release v1.32.5 is known to not work with applications using JBoss Wildfly. This issue extends to the
Amazon CloudWatch Observability EKS add-on, affecting versions `2.3.0-eksbuild.1` through `2.6.0-eksbuild.1`. The issue is fixed in Java SDK release `v1.32.6` and the Amazon CloudWatch Observability EKS add-on version `v3.0.0-eksbuild.1`.

If you are impacted, either upgrade the Java SDK version or disable your runtime metrics collection by adding the
environment variable `OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED=false` to your application.

### Java runtime metrics

Application Signals collects the following JVM metrics from Java applications that you enable for Application Signals. All runtime metrics are
sent to CloudWatch in the `ApplicationSignals` namespace, and are collected with the `Service` and `Environment` dimension set.

| Metric name                  | Description                                                                                                                               | Meaningful statistics          |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `JVMGCDuration`              | Aggregated metric for the duration of JVM garbage collection actions.<br>Unit: Milliseconds                                               | Sum, Average, Minimum, Maximum |
| `JVMGCOldGenDuration`        | Aggregated metric for the duration of JVM garbage collection actions of the old generation. Available only in G1.<br>Unit: Milliseconds   | Sum, Average, Minimum, Maximum |
| `JVMGCYoungGenDuration`      | Aggregated metric for the duration of JVM garbage collection actions of the young generation. Available only in G1.<br>Unit: Milliseconds | Sum, Average, Minimum, Maximum |
| `JVMGCCount`                 | Aggregated metric for the number of JVM garbage collection actions.<br>Unit: None                                                         | Sum, Average, Minimum, Maximum |
| `JVMGCOldGenCount`           | Aggregated metric for the number of JVM garbage collection actions of the old generation. Available only in G1.<br>Unit: None             | Sum, Average, Minimum, Maximum |
| `JVMGCYoungGenCount`         | Aggregated metric for the number of JVM garbage collection actions of the young generation. Available only in G1.<br>Unit: None           | Sum, Average, Minimum, Maximum |
| `JVMMemoryHeapUsed`          | The amount of memory heap used.<br>Unit: Bytes                                                                                            | Average, Minimum, Maximum      |
| `JVMMemoryUsedAfterLastGC`   | Amount of memory used, as measured after the most recent garbage collection event on this pool.<br>Unit: Bytes                            | Average, Minimum, Maximum      |
| `JVMMemoryOldGenUsed`        | The amount of memory used by the old generation.<br>Unit: Bytes                                                                           | Average, Minimum, Maximum      |
| `JVMMemorySurvivorSpaceUsed` | The amount of memory heap used by the survivor space.<br>Unit: Bytes                                                                      | Average, Minimum, Maximum      |
| `JVMMemoryEdenSpaceUsed`     | The amount of memory used by the eden space.<br>Unit: Bytes                                                                               | Average, Minimum, Maximum      |
| `JVMMemoryNonHeapUsed`       | The amount of non-heap memory used.<br>Unit: Bytes                                                                                        | Average, Minimum, Maximum      |
| `JVMThreadCount`             | The number of executing threads, including both daemon and non-daemon threads.<br>Unit: None                                              | Sum, Average, Minimum, Maximum |
| `JVMClassLoaded`             | The number of classes loaded.<br>Unit: None                                                                                               | Sum, Average, Minimum, Maximum |
| `JVMCpuTime`                 | The CPU time used by the process, as reported by the JVM.<br>Unit: None (Nanoseconds)                                                     | Sum, Average, Minimum, Maximum |
| `JVMCpuRecentUtilization`    | The recent CPU utilized by the process, as reported by the JVM.<br>Unit: None                                                             | Average, Minimum, Maximum      |

### Python runtime metrics

Application Signals collects the following metrics from Python applications that you enable for Application Signals. All runtime metrics are
sent to CloudWatch in the `ApplicationSignals` namespace, and are collected with the `Service` and `Environment` dimension set.

| Metric name                   | Description                                                                         | Meaningful statistics          |
| ----------------------------- | ----------------------------------------------------------------------------------- | ------------------------------ |
| `PythonProcessGCCount`        | The total number of objects currently being tracked.<br>Unit: None                  | Sum, Average, Minimum, Maximum |
| `PythonProcessGCGen0Count`    | The number of objects currently being tracked in Generation 0.<br>Unit: None        | Sum, Average, Minimum, Maximum |
| `PythonProcessGCGen1Count`    | The number of objects currently being tracked in Generation 1.<br>Unit: None        | Sum, Average, Minimum, Maximum |
| `PythonProcessGCGen2Count`    | The number of objects currently being tracked in Generation 2.<br>Unit: None        | Sum, Average, Minimum, Maximum |
| `PythonProcessVMSMemoryUsed`  | The total amount of virtual memory used by the process.<br>Unit: Bytes              | Average, Minimum, Maximum      |
| `PythonProcessRSSMemoryUsed`  | The total amount of non-swapped physical memory used by the process.<br>Unit: Bytes | Average, Minimum, Maximum      |
| `PythonProcessThreadCount`    | The number of threads currently used by the process.<br>Unit: None                  | Sum, Average, Minimum, Maximum |
| `PythonProcessCpuTime`        | The CPU time used by the process.<br>Unit: Seconds                                  | Sum, Average, Minimum, Maximum |
| `PythonProcessCpuUtilization` | The CPU utilization of the process.<br>Unit: None                                   | Average, Minimum, Maximum      |

### .Net runtime metrics

Application Signals collects the following metrics from .Net applications that you enable for Application Signals. All runtime metrics are
sent to CloudWatch in the `ApplicationSignals` namespace, and are collected with the `Service` and `Environment` dimension set.

| Metric name               | Description                                                                                                                                                                                                | Meaningful statistics          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `DotNetGCGen0Count`       | The total number of garbage collection metrics tracked in Generation 0 since the process started.<br>Unit: None                                                                                            | Sum, Average, Minimum, Maximum |
| `DotNetGCGen1Count`       | The total number of garbage collection metrics tracked in Generation 1 since the process started.<br>Unit: None                                                                                            | Sum, Average, Minimum, Maximum |
| `DotNetGCGen2Count`       | The total number of garbage collection metrics tracked in Generation 2 since the process started.<br>Unit: None                                                                                            | Sum, Average, Minimum, Maximum |
| `DotNetGCDuration`        | The total amount of time paused in garbage collection since the process started.<br>Unit: None                                                                                                             | Sum, Average, Minimum, Maximum |
| `DotNetGCGen0HeapSize`    | The heap size (including fragmentation) of Generation 0 observed during the latest garbage collection.<br>NoteThis metric is only available after the first Garbage Collection is complete.<br>Unit: Bytes | Average, Minimum, Maximum      |
| `DotNetGCGen1HeapSize`    | The heap size (including fragmentation) of Generation 1 observed during the latest garbage collection.<br>NoteThis metric is only available after the first Garbage Collection is complete.<br>Unit: Bytes | Average, Minimum, Maximum      |
| `DotNetGCGen2HeapSize`    | The heap size (including fragmentation) of Generation 2 observed during the latest garbage collection.<br>NoteThis metric is only available after the first Garbage Collection is complete.<br>Unit: Bytes | Average, Minimum, Maximum      |
| `DotNetGCLOHHeapSize`     | The large object heap size (including fragmentation) observed during the latest garbage collection.<br>NoteThis metric is only available after the first Garbage Collection is complete.<br>Unit: Bytes    | Average, Minimum, Maximum      |
| `DotNetGCPOHHeapSize`     | The pinned object heap size (including fragmentation) observed during the latest garbage collection.<br>NoteThis metric is only available after the first Garbage Collection is complete.<br>Unit: Bytes   | Average, Minimum, Maximum      |
| `DotNetThreadCount`       | The number of thread pool threads that currently exist.<br>Unit: None                                                                                                                                      | Average, Minimum, Maximum      |
| `DotNetThreadQueueLength` | The number of work items that are currently queued to be processed by the thread pool.<br>Unit: None                                                                                                       | Average, Minimum, Maximum      |

## Disabling the collection of runtime metrics

Runtime metrics are collected by default for Java and Python applications that are enabled for Application Signals. If you want to disable the
collection of these metrics, follow the instructions in this section for your environment.

### Amazon EKS

To disable runtime metrics in Amazon EKS applications at the application level, add the following environment variable to your workload specification.

```
env:
    - name: OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED
      value: "false"
```

To disable runtime metrics in Amazon EKS applications at the cluster level, apply the configuration to the advanced configuration of your Amazon CloudWatch Observability EKS add-on.

```
{
  "agent": {
    "config": {
      "traces": {
        "traces_collected": {
          "application_signals": {

          }
        }
      },
      "logs": {
        "metrics_collected": {
          "application_signals": {

          }
        }
      }
    },
    "manager": {
      "autoInstrumentationConfiguration": {
        "java": {
          "runtime_metrics": {
            "enabled": false
          }
        },
        "python": {
          "runtime_metrics": {
            "enabled": false
          }
        },
        "dotnet": {
          "runtime_metrics": {
            "enabled": false
          }
        }
      }
    }
  }
}
```

### Amazon ECS

To disable runtime metrics in Amazon ECS applications, add the environment variable `OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED=false`
in the new task definition revision and redeploy the application.

### EC2

To disable runtime metrics in Amazon EC2 applications, add the environment variable `OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED=false` before the application starts.

### Kubernetes

To disable runtime metrics in Kubernetes applications at the application level, add the following environment variable to your workload specification.

```
env:
    - name: OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED
      value: "false"
```

To disable runtime metrics in Kubernetes applications at the cluster level, use the following:

```
helm upgrade ... \
--set-string manager.autoInstrumentationConfiguration.java.runtime_metrics.enabled=false \
--set-string manager.autoInstrumentationConfiguration.python.runtime_metrics.enabled=false \
-\-set-string manager.autoInstrumentationConfiguration.dotnet.runtime_metrics.enabled=false
```
