Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Implement application scaling in Managed Service for Apache Flink

You can configure the parallel execution of tasks and the allocation of resources for
Amazon Managed Service for Apache Flink to implement scaling. For information about how Apache Flink schedules
parallel instances of tasks, see [Parallel Execution](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/") in the Apache Flink Documentation.

###### Topics

- [Configure application parallelism and
  ParallelismPerKPU](#how-parallelism "#how-parallelism")
- [Allocate Kinesis Processing Units](#how-scaling-kpus "#how-scaling-kpus")
- [Update your application's parallelism](#how-scaling-howto "#how-scaling-howto")
- [Use automatic scaling in Managed Service for Apache Flink](how-scaling-auto.md "how-scaling-auto.md")
- [maxParallelism considerations](#how-scaling-auto-max-parallelism "#how-scaling-auto-max-parallelism")

## Configure application parallelism and

ParallelismPerKPU

You configure the parallel execution for your Managed Service for Apache Flink application tasks (such as reading
from a source or executing an operator) using the following [`ParallelismConfiguration`](../apiv2/API_ApplicationConfiguration.md "../apiv2/API_ApplicationConfiguration.md")
properties:

- `Parallelism` — Use this property to set the default Apache
  Flink application parallelism. All operators, sources, and sinks execute with
  this parallelism unless they are overridden in the application code. The default
  is `1`, and the default maximum is `256`.
- `ParallelismPerKPU` — Use this property to set the number of
  parallel tasks that can be scheduled per Kinesis Processing Unit (KPU) of your
  application. The default is `1`, and the maximum is `8`.
  For applications that have blocking operations (for example, I/O), a higher
  value of `ParallelismPerKPU` leads to full utilization of KPU
  resources.

###### Note

The limit for `Parallelism` is equal to `ParallelismPerKPU` times the limit for KPUs (which has a default of 64). The KPUs limit can be increased by requesting a limit increase. For instructions on how to
request a limit increase, see "To request a limit increase" in [Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

For information about setting task parallelism for a specific operator, see [Setting the Parallelism: Operator](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/#operator-level "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/#operator-level") in the Apache Flink Documentation.

## Allocate Kinesis Processing Units

Managed Service for Apache Flink provisions capacity as KPUs. A single KPU provides you with 1 vCPU and 4 GB of
memory. For every KPU allocated, 50 GB of running application storage is also provided.

Managed Service for Apache Flink calculates the KPUs that are needed to run your application using the
`Parallelism` and `ParallelismPerKPU` properties, as
follows:

```
Allocated KPUs for the application = Parallelism/ParallelismPerKPU
```

Managed Service for Apache Flink quickly gives your applications resources in response to spikes in throughput or
processing activity. It removes resources from your application gradually after the
activity spike has passed. To disable the automatic allocation of resources, set the
`AutoScalingEnabled` value to `false`, as described
later in [Update your application's parallelism](#how-scaling-howto "#how-scaling-howto").

The default limit for KPUs for your application is 64. For instructions on how to
request an increase to this limit, see "To request a limit increase" in [Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

###### Note

An additional KPU is charged for orchestrations purposes. For more information, see [Managed Service for Apache Flink pricing](https://aws.amazon.com/kinesis/data-analytics/pricing/ "https://aws.amazon.com/kinesis/data-analytics/pricing/").

## Update your application's parallelism

This section contains sample requests for API actions that set an application's
parallelism. For more examples and instructions for how to use request blocks with API
actions, see [Managed Service for Apache Flink API example code](api-examples.md "api-examples.md").

The following example request for the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action sets parallelism when you are
creating an application:

```
{
   "ApplicationName": "string",
   "RuntimeEnvironment":"FLINK-1_18",
   "ServiceExecutionRole":"arn:aws:iam::123456789123:role/myrole",
   "ApplicationConfiguration": {
      "ApplicationCodeConfiguration":{
      "CodeContent":{
         "S3ContentLocation":{
            "BucketARN":"arn:aws:s3:::amzn-s3-demo-bucket",
            "FileKey":"myflink.jar",
            "ObjectVersion":"AbCdEfGhIjKlMnOpQrStUvWxYz12345"
            }
         },
      "CodeContentType":"ZIPFILE"
   },
      "FlinkApplicationConfiguration": {
         "ParallelismConfiguration": {
            "AutoScalingEnabled": "true",
            "ConfigurationType": "CUSTOM",
            "Parallelism": 4,
            "ParallelismPerKPU": 4
         }
      }
   }
}
```

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action sets parallelism for an existing
application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": {
         "ParallelismConfigurationUpdate": {
            "AutoScalingEnabledUpdate": "true",
            "ConfigurationTypeUpdate": "CUSTOM",
            "ParallelismPerKPUUpdate": 4,
            "ParallelismUpdate": 4
         }
      }
   }
}
```

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action disables parallelism for an existing
application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": {
         "ParallelismConfigurationUpdate": {
            "AutoScalingEnabledUpdate": "false"
         }
      }
   }
}
```

## maxParallelism considerations

The maximum parallelism a Flink job can scale is limited by the
_minimum_
`maxParallelism` across all operators of the job. For example, if you have a
simple job with only a source and a sink, and the source has a
`maxParallelism` of 16 and the sink has 8, the application can't scale
beyond parallelism of 8.

To learn how the default `maxParallelism` of an operator is calculated and
how to override the default, refer to [Setting the Maximum Parallelism](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/#setting-the-maximum-parallelism "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/execution/parallel/#setting-the-maximum-parallelism") in the Apache Flink docummentation.

As a basic rule, be aware that that if you don't define `maxParallelism`
for any operator and you start your application with parallelism less than or equal to
128, all operators will have a `maxParallelism` of 128.

###### Note

The job's maximum parallelism is the upper limit of parallelism for scaling your
application retaining the state.

If you modify `maxParallelism` of an existing application, the
application won't be able to restart from a previous snapshot taken with the old
`maxParallelism`. You can only restart the application without
snapshot.

If you plan to scale your application to a parallelism greater that 128, you must
explicitly set the `maxParallelism` in your application.

- Autoscaling logic will prevent scaling a Flink job to a parallelism that will exceed maximum
  parallelism of the job.
- If you use a custom autoscaling or scheduled scaling, configure them so that they don't exceed
  the maximum parallelism of the job.
- If you manually scale your application beyond maximum parallelism, the application fails to
  start.
