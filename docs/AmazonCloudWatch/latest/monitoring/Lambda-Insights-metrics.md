# Metrics collected by Lambda Insights

Lambda Insights collects several metrics from the Lambda functions where it is installed.
Some of these metrics are available as time series aggregated data in CloudWatch Metrics.
Other metrics are not aggregated into time series data but can be found in the
embedded metric format log entries by using CloudWatch Logs Insights.

The following metrics are available as time series aggregated data in CloudWatch Metrics
in the `LambdaInsights` namespace.

| Metric name          | Dimensions                              | Description                                                                                                                                                                                          |
| -------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cpu_total_time`     | function_name<br>function_name, version | Sum of `cpu_system_time` and `cpu_user_time`.<br>Unit: Milliseconds                                                                                                                                  |
| `init_duration`      | function_name<br>function_name, version | The amount of time spent in the `init` phase of the Lambda<br>execution environment lifecycle.<br>Unit: Milliseconds                                                                                 |
| `memory_utilization` | function_name<br>function_name, version | The maximum memory measured as a percentage of the memory allocated<br>to the function.<br>Unit: Percent                                                                                             |
| `rx_bytes`           | function_name<br>function_name, version | The number of bytes received by the function.<br>Unit: Bytes                                                                                                                                         |
| `tmp_used`           |                                         | The amount of space used in the `/tmp` directory.<br>Unit: Bytes                                                                                                                                     |
| `tx_bytes`           | function_name<br>function_name, version | The number of bytes sent by the function.<br>Unit: Bytes                                                                                                                                             |
| `total_memory`       | function_name<br>function_name, version | The amount of memory allocated to your Lambda function. This is the same as your<br>function’s memory size.<br>Unit: Megabytes                                                                       |
| `total_network`      | function_name<br>function_name, version | Sum of `rx_bytes` and `tx_bytes`. Even for functions that<br>don't perform I/O tasks, this value is usually greater than zero because of network<br>calls made by the Lambda runtime.<br>Unit: Bytes |
| `used_memory_max`    | function_name<br>function_name, version | The measured memory of the function sandbox.<br>Unit: Megabytes                                                                                                                                      |

The following metrics can be found in the
embedded metric format log entries by using CloudWatch Logs Insights. For more information
about CloudWatch Logs Insights, see [Analyzing Log Data with CloudWatch Logs
Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md").

For more information about embedded metric format,
see [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md "CloudWatch_Embedded_Metric_Format.md").

| Metric name          | Description                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cpu_system_time`    | The amount of time the CPU spent executing kernel code.<br>Unit: Milliseconds                                                                                                                        |
| `cpu_total_time`     | Sum of `cpu_system_time` and `cpu_user_time`.<br>Unit: Milliseconds                                                                                                                                  |
| `cpu_user_time`      | The amount of time the CPU spent executing user code.<br>Unit: Milliseconds                                                                                                                          |
| `fd_max`             | The maximum number of file descriptors available.<br>Unit: Count                                                                                                                                     |
| `fd_use`             | The maximum number of file descriptors in use.<br>Unit: Count                                                                                                                                        |
| `memory_utilization` | The maximum memory measured as a percentage of the memory allocated<br>to the function.<br>Unit: Percent                                                                                             |
| `rx_bytes`           | The number of bytes received by the function.<br>Unit: Bytes                                                                                                                                         |
| `tx_bytes`           | The number of bytes sent by the function.<br>Unit: Bytes                                                                                                                                             |
| `threads_max`        | The number of threads in use by the function process. As a function author, you<br>don't control the initial number of threads created by the runtime.<br>Unit: Count                                |
| `tmp_max`            | The amount of space available in the `/tmp` directory.<br>Unit: Bytes                                                                                                                                |
| `total_memory`       | The amount of memory allocated to your Lambda function. This is the same as your<br>function’s memory size.<br>Unit: Megabytes                                                                       |
| `total_network`      | Sum of `rx_bytes` and `tx_bytes`. Even for functions that<br>don't perform I/O tasks, this value is usually greater than zero because of network<br>calls made by the Lambda runtime.<br>Unit: Bytes |
| `used_memory_max`    | The measured memory of the function sandbox.<br>Unit: Bytes                                                                                                                                          |
