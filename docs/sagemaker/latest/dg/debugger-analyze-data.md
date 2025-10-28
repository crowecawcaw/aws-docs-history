# Analyze data using the Debugger Python client

library

While your training job is running or after it has completed, you can access the training
data collected by Debugger using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") and the [SMDebug client library](https://github.com/awslabs/sagemaker-debugger/ "https://github.com/awslabs/sagemaker-debugger/"). The
Debugger Python client library provides analysis and visualization tools that enable you to
drill down into your training job data.

**To install the library and use its analysis tools (in a JupyterLab
notebook or an iPython kernel)**

```
! pip install -U smdebug
```

The following topics walk you through how to use the Debugger Python tools to visualize and
analyze the training data collected by Debugger.

**Analyze system and framework metrics**

- [Access the profile data](debugger-analyze-data-profiling.md "debugger-analyze-data-profiling.md")
- [Plot the system metrics
  and framework metrics data](debugger-access-data-profiling-default-plot.md "debugger-access-data-profiling-default-plot.md")
- [Access the profiling data
  using the pandas data parsing tool](debugger-access-data-profiling-pandas-frame.md "debugger-access-data-profiling-pandas-frame.md")
- [Access the Python profiling
  stats data](debugger-access-data-python-profiling.md "debugger-access-data-python-profiling.md")
- [Merge timelines of multiple profile trace
  files](debugger-merge-timeline.md "debugger-merge-timeline.md")
- [Profiling data loaders](debugger-data-loading-time.md "debugger-data-loading-time.md")
