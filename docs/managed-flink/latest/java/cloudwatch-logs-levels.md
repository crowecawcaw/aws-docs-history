Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Set CloudWatch metrics reporting levels

You can control the level of application metrics that your application creates.
Managed Service for Apache Flink supports the following metrics levels:

- **Application:** The application only reports
  the highest level of metrics for
  each application. Managed Service for Apache Flink metrics are published at the Application level by default.
- **Task:** The application reports
  task-specific metric dimensions for metrics defined with the Task
  metric reporting level, such as number of records in and out of
  the application per second.
- **Operator:** The application reports
  operator-specific metric dimensions for metrics defined with the Operator
  metric reporting level, such as metrics for each filter or map
  operation.
- **Parallelism:** The application reports
  `Task` and `Operator` level metrics for each
  execution thread. This reporting level is not recommended for applications with
  a Parallelism setting above 64 due to excessive costs.

###### Note

You should only use this metric level for troubleshooting because of the amount
of metric data that the service generates. You can only set this metric level
using the CLI. This metric level is not available in the console.
The default level is **Application**. The application
reports metrics at the current level and all higher levels. For example, if the
reporting level is set to **Operator**, the application
reports **Application**, **Task**, and **Operator** metrics.

You set the CloudWatch metrics reporting level using the
`MonitoringConfiguration` parameter of the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action, or the
`MonitoringConfigurationUpdate` parameter of the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action. The following example request
for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action sets the CloudWatch metrics
reporting level to **Task**:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": {
         "MonitoringConfigurationUpdate": {
            "ConfigurationTypeUpdate": "CUSTOM",
            "MetricsLevelUpdate": "TASK"
         }
      }
   }
}
```

You can also configure the logging level using the `LogLevel` parameter
of the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action or the
`LogLevelUpdate` parameter of the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action. You can use the following log
levels:

- `ERROR`: Logs potentially recoverable error events.
- `WARN`: Logs warning events that might lead to an error.
- `INFO`: Logs informational events.
- `DEBUG`: Logs general debugging events.
  For more information about Log4j logging levels, see [Custom Log Levels](https://logging.apache.org/log4j/2.x/manual/customloglevels.html "https://logging.apache.org/log4j/2.x/manual/customloglevels.html") in the [Apache
  Log4j](https://logging.apache.org/log4j/2.x/ "https://logging.apache.org/log4j/2.x/") documentation.
