# Default system

monitoring and customized framework profiling with different profiling
options

This section gives information about the supported profiling configuration
classes, as well as an example configuration. You can use the following profiling
configuration classes to manage the framework profiling options:

- [DetailedProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DetailedProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DetailedProfilingConfig") – Specify a target step or time
  range to profile framework operations using the native framework profilers
  (TensorFlow profiler and PyTorch profiler). For example, if using
  TensorFlow, the Debugger hooks enable the TensorFlow profiler to collect
  TensorFlow-specific framework metrics. Detailed profiling enables you to
  profile all framework operators at a pre-step (before the first step),
  within steps, and between steps of a training job.

###### Note

Detailed profiling might significantly increase GPU memory
consumption. We do not recommend enabling detailed profiling for more
than a couple of steps.

- [DataloaderProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DataloaderProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DataloaderProfilingConfig") – Specify a target step or
  time range to profile deep learning framework data loader processes. Debugger
  collects every data loader event of the frameworks.

###### Note

Data loader profiling might lower the training performance while
collecting information from data loaders. We don't recommend enabling
data loader profiling for more than a couple of steps.

Debugger is preconfigured to annotate data loader processes only for the
AWS deep learning containers. Debugger cannot profile data loader
processes from any other custom or external training containers.

- [PythonProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.PythonProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.PythonProfilingConfig") – Specify a target step or time
  range to profile Python functions. You can also choose between two Python
  profilers: cProfile and Pyinstrument.
  - _cProfile_ – The standard Python
    profiler. cProfile collects information for every Python operator
    called during training. With cProfile, Debugger saves cumulative time
    and annotation for each function call, providing complete detail
    about Python functions. In deep learning, for example, the most
    frequently called functions might be the convolutional filters and
    backward pass operators, and cProfile profiles every single of them.
    For the cProfile option, you can further select a timer option:
    total time, CPU time, and off-CPU time. While you can profile every
    function call executing on processors (both CPU and GPU) in CPU
    time, you can also identify I/O or network bottlenecks with the
    off-CPU time option. The default is total time, and Debugger profiles
    both CPU and off-CPU time. With cProfile, you are able to drill down
    to every single functions when analyzing the profile data.
  - _Pyinstrument_ – Pyinstrument is
    a low-overhead Python profiler that works based on sampling. With
    the Pyinstrument option, Debugger samples profiling events every
    millisecond. Because Pyinstrument measures elapsed wall-clock time
    instead of CPU time, the Pyinstrument option can be a better choice
    over the cProfile option for reducing profiling noise (filtering out
    irrelevant function calls that are cumulatively fast) and capturing
    operators that are actually compute intensive (cumulatively slow)
    for training your model. With Pyinstrument, you are able to see a
    tree of function calls and better understand the structure and root
    cause of the slowness.

###### Note

Enabling Python profiling might slow down the overall training time.
cProfile profiles the most frequently called Python operators at every
call, so the processing time on profiling increases with respect to the
number of calls. For Pyinstrument, the cumulative profiling time
increases with respect to time because of its sampling mechanism.
The following example configuration shows the full structure when you use the
different profiling options with specified values.

```
import time
from sagemaker.debugger import (ProfilerConfig,
                                FrameworkProfile,
                                DetailedProfilingConfig,
                                DataloaderProfilingConfig,
                                PythonProfilingConfig,
                                PythonProfiler, cProfileTimer)

profiler_config=ProfilerConfig(
    system_monitor_interval_millis=`500`,
    framework_profile_params=FrameworkProfile(
        detailed_profiling_config=DetailedProfilingConfig(
            start_step=`5`,
            num_steps=`1`
        ),
        dataloader_profiling_config=DataloaderProfilingConfig(
            start_step=`7`,
            num_steps=`1`
        ),
        python_profiling_config=PythonProfilingConfig(
            start_step=`9`,
            num_steps=`1`,
            python_profiler=PythonProfiler.`CPROFILE`,
            cprofile_timer=`cProfileTimer.TOTAL_TIME`
        )
    )
)
```

For more information about available profiling options, see [DetailedProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DetailedProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DetailedProfilingConfig"), [DataloaderProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DataloaderProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DataloaderProfilingConfig"), and [PythonProfilingConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.PythonProfilingConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.PythonProfilingConfig") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
