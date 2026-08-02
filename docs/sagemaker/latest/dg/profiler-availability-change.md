# Profiler availability change

###### Note

End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources.

## Replacing Amazon SageMaker Profiler

If you are currently using SageMaker Profiler, follow this guidance to transition to
alternative services.

## Overview

Amazon SageMaker Profiler provided deep visibility into GPU and CPU activity during
training, including kernel runs, kernel launches, sync operations, memory operations, and
latencies between CPU-initiated launches and GPU kernel execution. This guide walks you
through removing your existing Profiler configuration and adopting framework-native profilers,
TensorBoard, and Amazon CloudWatch for training performance diagnostics.

For PyTorch and TensorFlow workloads, the combination of framework-native profilers and
TensorBoard provides equivalent kernel-level visibility with direct integration into the
open-source ecosystem. Amazon CloudWatch provides system-level resource monitoring with
configurable alarms. Together, these tools offer alternatives to SageMaker Profiler's training
performance diagnostics.

## Capability mapping

| Profiler capability                                                                       | Replaced by                                          |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| GPU kernel traces, CPU/GPU utilization, sync analysis, kernel launch-to-execution latency | PyTorch Profiler / TensorFlow Profiler + TensorBoard |
| Data loader and input pipeline profiling                                                  | Framework Profilers + TensorBoard                    |
| System resource monitoring (CPU, GPU, memory, disk)                                       | Amazon CloudWatch                                    |
| Custom operation annotations                                                              | Framework Profiler annotations                       |
| Profiler UI timeline visualization                                                        | TensorBoard Profiler Plugin                          |

## Step 1: Remove Profiler configuration

### Remove smprof annotations from your training script

If your training script uses the SageMaker Profiler Python modules (`smprof`
or the older `smppy`), remove:

- `import smprof` (or `import smppy as smprof`)
- `SMProfiler.instance()`, `SMProf.configure()`,
  `SMProf.start_profiling()`, `SMProf.stop_profiling()`
- All `smprof.annotate()` context managers and
  `smprof.annotation_begin()` / `smprof.annotation_end()`
  calls

### Remove ProfilerConfig from your training configuration

Remove the `profiler_config` parameter from your SageMaker training
configuration:

```
# Remove this configuration
# V2
from sagemaker import ProfilerConfig, Profiler

profiler_config = ProfilerConfig(
    profile_params = Profiler(cpu_profiling_duration=3600)
)

# V3
from sagemaker.core.debugger.profiler_config import ProfilerConfig
from sagemaker.core.debugger.profiler import Profiler
```

### Delete Profiler output in Amazon S3

SageMaker Profiler stored profile data under the `rule-output` path of your
training job:

```
s3://<output-path>/<training-job-name>/rule-output/
```

Delete this prefix if you no longer need the historical profiling data. Your training
job logs and model artifacts remain unaffected.

### Remove SageMaker Profiler Python package (if manually installed)

If you added the `smprof` package to a `requirements.txt` or
custom Docker container, remove any lines referencing
`smppy.s3.amazonaws.com`.

### Delete CloudWatch Log Groups (optional)

Check for CloudWatch log groups created by Profiler rule processing under
`/aws/sagemaker/ProcessingJobs`. Delete these if no longer needed to reduce
storage costs.

### Review IAM policies

Remove IAM policies that granted permissions specifically for Profiler usage:

- `s3:GetObject` / `s3:PutObject` scoped to Profiler
  rule-output paths
- Roles attached to training jobs solely for Profiler support

Retain any policies still needed for your training jobs or CloudWatch
monitoring.

### Disable dependent automation

Update or delete any automation that consumed Profiler output:

- Step Functions workflows that processed Profiler data
- Amazon EventBridge rules triggered by Profiler output
- Post-training processors that read from Profiler S3 paths

## Step 2: Configure replacements

### Enable framework-level profiling

Update your training script to use your framework's built-in profiler. Both PyTorch and
TensorFlow profilers integrate directly with TensorBoard for visualization, including
timeline views, kernel statistics, and performance recommendations.

**PyTorch:**

```
import torch
from torch.profiler import profile, schedule, tensorboard_trace_handler

with profile(
    activities=[torch.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA],
    schedule=schedule(wait=1, warmup=1, active=3, repeat=1),
    on_trace_ready=tensorboard_trace_handler("./tensorboard/logs"),
    record_shapes=True,
    profile_memory=True,
    with_stack=True
) as prof:
    for step, batch in enumerate(train_loader):
        inputs, labels = batch
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        prof.step()
```

To annotate specific operations (replacing `smprof.annotate()`):

```
with torch.profiler.record_function("forward_pass"):
    outputs = model(inputs)

with torch.profiler.record_function("backward_pass"):
    loss.backward()
```

**TensorFlow:**

```
import tensorflow as tf

tf.profiler.experimental.start("./tensorboard/logs")
model.fit(train_dataset, epochs=5)
tf.profiler.experimental.stop()
```

###### Note

As with SageMaker Profiler, profiling an entire training job is not recommended.
Profile a representative subset of steps (up to a few hundred) to minimize
overhead.

### Visualize with TensorBoard

Launch TensorBoard to view profiling results, execution timelines, and performance
recommendations:

```
tensorboard --logdir=./tensorboard/logs
```

The TensorBoard Profiler Plugin provides GPU kernel timelines equivalent to the
SageMaker Profiler UI, along with kernel statistics, execution summaries, input pipeline
analysis, and performance recommendations. For managed TensorBoard in SageMaker AI, refer
to [TensorBoard in Amazon SageMaker
AI](tensorboard-on-sagemaker.md "tensorboard-on-sagemaker.md"). Managed TensorBoard requires a SageMaker Domain and is available in select
regions.

### Use Amazon CloudWatch for system monitoring and alerts

Amazon CloudWatch captures resource utilization metrics for your training jobs,
including CPU, GPU, memory, and disk, in real time, with support for configurable alarms to
detect resource bottlenecks, underutilization, or unexpected spikes, and dashboards
combining system metrics across training runs. For detailed steps, refer to [Amazon CloudWatch
Metrics for Monitoring and Analyzing Training Jobs](training-metrics.md "training-metrics.md"). Alternatively, you can log
system performance metrics from your training script directly to MLflow for unified tracking
alongside your experiment metrics.

## What happens to your existing data

- **Training logs and artifacts in S3** – Your
  training job output and model artifacts remain accessible. These are independent of
  Profiler.
- **Profiler trace data** – Historical profiling
  data remains in S3 under `rule-output/` until you delete it.
- **CloudWatch metrics** – Historical system
  metrics already in CloudWatch are retained per your account's [retention settings](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention").
