# Access the profiling data using the pandas data parsing tool

###### Note

End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources.
For more information, see [Profiler availability change](profiler-availability-change.md "profiler-availability-change.md").

The following `PandasFrame` class provides tools to convert the collected
profiling data to Pandas data frame.

```
from smdebug.profiler.analysis.utils.profiler_data_to_pandas import PandasFrame
```

The `PandasFrame` class takes the `tj` object's S3 bucket output
path, and its methods `get_all_system_metrics()`
`get_all_framework_metrics()` return system metrics and framework metrics in
the Pandas data format.

```
pf = PandasFrame(tj.profiler_s3_output_path)
system_metrics_df = pf.get_all_system_metrics()
framework_metrics_df = pf.get_all_framework_metrics(
    selected_framework_metrics=[
        'Step:ModeKeys.TRAIN',
        'Step:ModeKeys.GLOBAL'
    ]
)
```
