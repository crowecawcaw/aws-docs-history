# Default system

monitoring and customized framework profiling for target steps or a target time
range

If you want to specify target steps or target time intervals to profile your
training job, you need to specify parameters for the `FrameworkProfile`
class. The following code examples show how to specify the target ranges for
profiling along with system monitoring.

- **For a target step range**

With the following example configuration, Debugger monitors the entire
training job every 500 milliseconds (the default monitoring) and profiles a
target step range from step 5 to step 15 (for 10 steps).

```
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    framework_profile_params=FrameworkProfile(start_step=`5`, num_steps=`10`)
)
```

With the following example configuration, Debugger monitors the entire
training job every 1000 milliseconds and profiles a target step range from
step 5 to step 15 (for 10 steps).

```
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    system_monitor_interval_millis=`1000`,
    framework_profile_params=FrameworkProfile(start_step=`5`, num_steps=`10`)
)
```

- **For a target time range**

With the following example configuration, Debugger monitors the entire
training job every 500 milliseconds (the default monitoring) and profiles a
target time range from the current Unix time for 600 seconds.

```
import time
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    framework_profile_params=FrameworkProfile(start_unix_time=int(`time.time()`), duration=`600`)
)
```

With the following example configuration, Debugger monitors the entire
training job every 1000 milliseconds and profiles a target time range from
the current Unix time for 600 seconds.

```
import time
from sagemaker.debugger import ProfilerConfig, FrameworkProfile

profiler_config=ProfilerConfig(
    system_monitor_interval_millis=`1000`,
    framework_profile_params=FrameworkProfile(start_unix_time=int(`time.time()`), duration=`600`)
)
```

The framework profiling is performed for all of the profiling options at
the target step or time range.

To find more information about available profiling options, see [SageMaker Debugger APIs – FrameworkProfile](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.FrameworkProfile") in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

The next section shows you how to script the available profiling
options.
