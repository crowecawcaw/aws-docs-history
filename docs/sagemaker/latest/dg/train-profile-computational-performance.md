# Profile and optimize computational performance

When training state-of-the-art deep learning models that rapidly grow in size, scaling the
training job of such models to a large GPU cluster and identifying computational performance
issues from billions and trillions of operations and communications in every iteration of
the gradient descent process become a challenge.

SageMaker AI provides profiling tools to visualize and diagnose such complex computation issues
arising from running training jobs on AWS cloud computing resources. There are two
profiling options that SageMaker AI offers: Amazon SageMaker Profiler and a resource utilzation monitor in
Amazon SageMaker Studio Classic. See the following introductions of the two functionalities to gain quick
insights and learn which one to use depending on your needs.

**Amazon SageMaker Profiler**

Amazon SageMaker Profiler is a profiling capability of SageMaker AI with which you can deep dive into compute
resources provisioned while training deep learning models, and gain visibility into
operation-level details. SageMaker Profiler provides Python modules for adding annotations throughout
PyTorch or TensorFlow training scripts and activating SageMaker Profiler. You can access the modules
through the SageMaker Python SDK and AWS Deep Learning Containers.

With SageMaker Profiler, you can track all activities on CPUs and GPUs, such as CPU and
GPU utilizations, kernel runs on GPUs, kernel launches on CPUs, sync operations, memory
operations across CPUs and GPUs, latencies between kernel launches and corresponding runs,
and data transfer between CPUs and GPUs.

SageMaker Profiler also offers a user interface (UI) that visualizes the
_profile_, a statistical summary of profiled events, and the timeline
of a training job for tracking and understanding the time relationship of the events between
GPUs and CPUs.

To learn more about SageMaker Profiler, see [Amazon SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md").

**Monitoring AWS compute resources in
Amazon SageMaker Studio Classic**

SageMaker AI also provides a user interface in Studio Classic for monitoring resource utilization at
high level, but with more granularity compared to the default utilization metrics collected
from SageMaker AI to CloudWatch.

For any training job you run in SageMaker AI using the SageMaker Python SDK, SageMaker AI starts profiling
basic resource utilization metrics, such as CPU utilization, GPU utilization, GPU memory
utilization, network, and I/O wait time. It collects these resource utilization metrics
every 500 milliseconds.

Compared to Amazon CloudWatch metrics, which collect metrics at intervals of 1 second, the
monitoring functionality of SageMaker AI provides finer granularity into the resource
utilization metrics down to 100-millisecond (0.1 second) intervals, so you can dive deep
into the metrics at the level of an operation or a step.

To access the dashboard for monitoring the resource utilization metrics of a training job,
see the [SageMaker AI
Debugger UI in SageMaker Studio Experiments](debugger-on-studio.md "debugger-on-studio.md").

###### Topics

- [Amazon SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md")
- [Monitor AWS compute resource utilization in Amazon SageMaker Studio Classic](debugger-profile-training-jobs.md "debugger-profile-training-jobs.md")
- [Release notes for profiling capabilities of
  Amazon SageMaker AI](profiler-release-notes.md "profiler-release-notes.md")
