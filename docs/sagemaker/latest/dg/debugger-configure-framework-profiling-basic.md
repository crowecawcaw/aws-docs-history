# Default framework

profiling

Debugger framework default profiling includes the following options: detailed
profiling, data loader profiling, and Python profiling. The following example code
is the simplest `profiler_config` parameter setting to start the default
system monitoring and the default framework profiling. The
`FrameworkProfile` class in the following example code initiates the
default framework profiling when a training job starts.

```
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    framework_profile_params=FrameworkProfile()
)
```

With this `profiler_config` parameter configuration, Debugger calls the
default settings of monitoring and profiling. Debugger monitors system metrics every
500 milliseconds; profiles the fifth step with the detailed profiling option; the
seventh step with the data loader profiling option; and the ninth, tenth, and
eleventh steps with the Python profiling option.

To find available profiling configuration options, the default parameter settings,
and examples of how to configure them, see [Default system
monitoring and customized framework profiling with different profiling
options](debugger-configure-framework-profiling-options.md "debugger-configure-framework-profiling-options.md") and [SageMaker Debugger APIs – FrameworkProfile](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile") in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

If you want to change the system monitoring interval and enable the default
framework profiling, you can specify the `system_monitor_interval_millis`
parameter explicitly with the `framework_profile_params` parameter. For
example, to monitor every 1000 milliseconds and enable the default framework
profiling, use the following example code.

```
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    system_monitor_interval_millis=`1000`,
    framework_profile_params=FrameworkProfile()
)
```

For more information about the `FrameworkProfile` class, see [SageMaker Debugger APIs – FrameworkProfile](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile") in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
