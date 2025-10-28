# Monitor AWS compute resource utilization in Amazon SageMaker Studio Classic

To track compute resource utilization of your training job, use the monitoring tools
offered by Amazon SageMaker Debugger.

For any training job you run in SageMaker AI using the SageMaker Python SDK, Debugger collects basic
resource utilization metrics, such as CPU utilization, GPU utilization, GPU memory
utilization, network, and I/O wait time every 500 milliseconds. To see the dashbard of the
resource utilization metrics of your training job, simply use the [SageMaker Debugger UI in
SageMaker Studio Experiments](debugger-on-studio.md "debugger-on-studio.md").

Deep learning operations and steps might operate in intervals of milliseconds. Compared to
Amazon CloudWatch metrics, which collect metrics at intervals of 1 second, Debugger provides finer
granularity into the resource utilization metrics down to 100-millisecond (0.1 second)
intervals so you can dive deep into the metrics at the level of an operation or a step.

If you want to change the metric collection time interval, you can add a paramter for
profiling configuration to your training job launcher. For example, if you're using the SageMaker AI
Python SDK, you need to pass the `profiler_config` parameter when you create an
estimator object. To learn how to adjust the resource utilization metric collection
interval, see [Code template for
configuring a SageMaker AI estimator object with the SageMaker Debugger Python modules in the SageMaker AI
Python SDK](debugger-configuration-for-profiling.md#debugger-configuration-structure-profiler "debugger-configuration-for-profiling.md#debugger-configuration-structure-profiler") and then [Configure settings for basic
profiling of system resource utilization](debugger-configure-system-monitoring.md "debugger-configure-system-monitoring.md").

Additionally, you can add issue detecting tools called _built-in
profiling rules_ provided by SageMaker Debugger. The built-in profiling rules run
analysis against the resource utilization metrics and detect computational performance
issues. For more information, see [Use built-in profiler rules managed
by Amazon SageMaker Debugger](use-debugger-built-in-profiler-rules.md "use-debugger-built-in-profiler-rules.md").
You can receive rule analysis results through the [SageMaker Debugger UI in SageMaker Studio
Experiments](debugger-on-studio.md "debugger-on-studio.md") or the [SageMaker Debugger Profiling Report](debugger-profiling-report.md "debugger-profiling-report.md"). You can also create custom profiling rules using
the SageMaker Python SDK.

To learn more about monitoring functionalities provided by SageMaker Debugger, see the following
topics.

###### Topics

- [Estimator configuration with
  parameters for basic profiling using the Amazon SageMaker Debugger Python modules](debugger-configuration-for-profiling.md "debugger-configuration-for-profiling.md")
- [Use built-in profiler rules managed
  by Amazon SageMaker Debugger](use-debugger-built-in-profiler-rules.md "use-debugger-built-in-profiler-rules.md")
- [List of Debugger built-in profiler
  rules](debugger-built-in-profiler-rules.md "debugger-built-in-profiler-rules.md")
- [Amazon SageMaker Debugger UI in Amazon SageMaker Studio Classic Experiments](debugger-on-studio.md "debugger-on-studio.md")
- [SageMaker Debugger interactive report](debugger-profiling-report.md "debugger-profiling-report.md")
- [Analyze data using the Debugger Python client
  library](debugger-analyze-data.md "debugger-analyze-data.md")
