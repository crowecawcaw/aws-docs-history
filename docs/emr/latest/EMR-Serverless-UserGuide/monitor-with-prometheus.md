# Monitor Spark metrics with

Amazon Managed Service for Prometheus

With Amazon EMR releases 7.1.0 and higher, you can integrate EMR Serverless with Amazon Managed Service for Prometheus to collect Apache Spark metrics for EMR Serverless jobs and applications. This integration is available
when you submit a job or create an application using either the AWS console, the EMR Serverless API, or the AWS CLI.

## Prerequisites

Before you can deliver your Spark metrics to Amazon Managed Service for Prometheus, complete the following prerequisites.

- [Create an Amazon Managed Service for Prometheus workspace.](../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md "../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md") This workspace serves as an ingestion endpoint.
  Make a note of the URL displayed for **Endpoint - remote write URL**. You'll need
  to specify the URL when you create your EMR Serverless application.
- To grant access of your jobs to Amazon Managed Service for Prometheus for monitoring purposes, add the following policy to your job execution role.

```
{
    "Sid": "AccessToPrometheus",
    "Effect": "Allow",
    "Action": ["aps:RemoteWrite"],
    "Resource": "arn:aws:aps:`<AWS_REGION>`:`<AWS_ACCOUNT_ID>`:workspace/`<WORKSPACE_ID>`"
}
```

## Setup

###### To use the AWS console to create an application that's integrated with Amazon Managed Service for Prometheus

1. See [Getting started with Amazon EMR Serverless](getting-started.md "getting-started.md") to create an application.
2. While you're creating an application, choose **Use custom settings**, and then configure your application by specifying the information into the fields you want to configure.
3. Under **Application logs and metrics**, choose **Deliver engine metrics to Amazon Managed Service for Prometheus**, and then specify your remote write URL.
4. Specify any other configuration settings you want, and then choose **Create and start application**.

**Use the AWS CLI or EMR Serverless API**

You can also use the AWS CLI or EMR Serverless API to integrate your EMR Serverless application with Amazon Managed Service for Prometheus when you're running the `create-application` or the
`start-job-run` commands.

create-application

```
aws emr-serverless create-application \
--release-label emr-7.1.0 \
--type "SPARK" \
--monitoring-configuration '{
    "prometheusMonitoringConfiguration": {
        "remoteWriteUrl": "https://aps-workspaces.`<AWS_REGION>`.amazonaws.com/workspaces/`<WORKSPACE_ID>`/api/v1/remote_write"
    }
}'
```

start-job-run

```
aws emr-serverless start-job-run \
--application-id `<APPPLICATION_ID>` \
--execution-role-arn `<JOB_EXECUTION_ROLE>` \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "local:///usr/lib/spark/examples/src/main/python/pi.py",
        "entryPointArguments": ["10000"],
        "sparkSubmitParameters": "--conf spark.dynamicAllocation.maxExecutors=10"
    }
}' \
--configuration-overrides '{
     "monitoringConfiguration": {
        "prometheusMonitoringConfiguration": {
            "remoteWriteUrl": "https://aps-workspaces.`<AWS_REGION>`.amazonaws.com/workspaces/`<WORKSPACE_ID>`/api/v1/remote_write"
        }
    }
}'
```

Including `prometheusMonitoringConfiguration` in your command indicates that EMR Serverless must run the Spark job with an agent that collects the Spark metrics
and writes them to your `remoteWriteUrl` endpoint for Amazon Managed Service for Prometheus. You can then use the Spark metrics in Amazon Managed Service for Prometheus for visualization, alerts, and analysis.

## Advanced configuration properties

EMR Serverless uses a component within Spark named `PrometheusServlet` to collect Spark metrics and translates performance data into data that's
compatible with Amazon Managed Service for Prometheus. By default, EMR Serverless sets default values in Spark and parses driver and executor metrics when you submit a job using `PrometheusMonitoringConfiguration`.

The following table describes all of the properties configure when submitting a Spark job that sends metrics to Amazon Managed Service for Prometheus.

| Spark property                                            | Default value                                   | Description                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spark.metrics.conf.*.sink.prometheusServlet.class`       | org.apache.spark.metrics.sink.PrometheusServlet | The class that Spark uses to send metrics to Amazon Managed Service for Prometheus. To override the default behavior, specify your own custom class.                                                                                                                          |
| `spark.metrics.conf.*.source.jvm.class`                   | org.apache.spark.metrics.source.JvmSource       | The class Spark uses to collect and send crucial metrics from the underlying Java virtual machine.<br>To stop collecting JVM metrics, disable this property by setting it to an empty string, such as `""`. To override the default behavior, specify your own custom class.  |
| `spark.metrics.conf.driver.sink.prometheusServlet.path`   | /metrics/prometheus                             | The distinct URL that Amazon Managed Service for Prometheus uses to collect metrics from the driver. To override the default behavior,<br>specify your own path. To stop collecting driver metrics, disable this property by setting it to an empty string, such as `""`.     |
| `spark.metrics.conf.executor.sink.prometheusServlet.path` | /metrics/executor/prometheus                    | The distinct URL that Amazon Managed Service for Prometheus uses to collect metrics from the executor. To override the default behavior,<br>specify your own path. To stop collecting executor metrics, disable this property by setting it to an empty string, such as `""`. |

For more information about the Spark metrics, refer to [Apache Spark metrics](https://spark.apache.org/docs/3.5.0/monitoring.html#metrics "https://spark.apache.org/docs/3.5.0/monitoring.html#metrics").

## Considerations and limitations

When using Amazon Managed Service for Prometheus to collect metrics from EMR Serverless, consider the following considerations and limitations.

- Support for using Amazon Managed Service for Prometheus with EMR Serverless is available only in the [AWS Regions where Amazon Managed Service for Prometheus is generally available.](../../../general/latest/gr/prometheus-service.md "../../../general/latest/gr/prometheus-service.md")
- Running the agent to collect Spark metrics on Amazon Managed Service for Prometheus requires more resources from workers. If you choose
  a smaller worker size, such as one vCPU worker, your job run time might increase.
- Support for using Amazon Managed Service for Prometheus with EMR Serverless is available only for Amazon EMR releases 7.1.0 and higher.
- Amazon Managed Service for Prometheus must be deployed in the same account where you run EMR Serverless to collect metrics.
