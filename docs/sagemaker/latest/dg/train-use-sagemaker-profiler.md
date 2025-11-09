# Amazon SageMaker Profiler

|                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Amazon SageMaker Profiler is currently in preview release and available at no cost<br>in supported AWS Regions. The generally available version of<br>Amazon SageMaker Profiler (if any) may include features and pricing that are<br>different than those offered in preview. |

Amazon SageMaker Profiler is a capability of Amazon SageMaker AI that provides a detailed view into the AWS
compute resources provisioned during training deep learning models on SageMaker AI. It focuses on
profiling the CPU and GPU usage, kernel runs on GPUs, kernel launches on CPUs, sync
operations, memory operations across CPUs and GPUs, latencies between kernel launches and
corresponding runs, and data transfer between CPUs and GPUs. SageMaker Profiler also offers a user
interface (UI) that visualizes the _profile_, a statistical summary of
profiled events, and the timeline of a training job for tracking and understanding the time
relationship of the events between GPUs and CPUs.

###### Note

SageMaker Profiler supports PyTorch and TensorFlow and is available in [AWS Deep Learning Containers for SageMaker AI](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only"). To learn more, see [Supported framework images, AWS Regions, and
instance types](profiler-support.md "profiler-support.md").

**For data scientists**

Training deep learning models on a large compute cluster often has computational
optimization problems, such as bottlenecks, kernel launch latencies, memory limit, and low
resource utilization.

To identify such computational performance issues, you need to profile deeper into the
compute resources to understand which kernels introduce latencies and which operations cause
bottlenecks. Data scientists can take the benefit from using the SageMaker Profiler UI for visualizing
the detailed profile of training jobs. The UI provides a dashboard furnished with summary
charts and a timeline interface to track every event on the compute resources. Data
scientists can also add custom annotations to track certain parts of the training job using
the SageMaker Profiler Python modules.

**For administrators**

Through the Profiler landing page in the SageMaker AI console or [SageMaker AI domain](sm-domain.md "sm-domain.md"), you can manage the
Profiler application users if you are an administrator of an AWS account or SageMaker AI
domain. Each domain user can access their own Profiler application given the
granted permissions. As a SageMaker AI domain administrator and domain user, you can create
and delete the Profiler application given the permission level you have.

###### Topics

- [Supported framework images, AWS Regions, and
  instance types](profiler-support.md "profiler-support.md")
- [Prerequisites for SageMaker Profiler](profiler-prereq.md "profiler-prereq.md")
- [Prepare and run a training job with SageMaker Profiler](profiler-prepare.md "profiler-prepare.md")
- [Open the SageMaker Profiler UI application](profiler-access-smprofiler-ui.md "profiler-access-smprofiler-ui.md")
- [Explore the profile output data visualized in the
  SageMaker Profiler UI](profiler-explore-viz.md "profiler-explore-viz.md")
- [Troubleshooting for SageMaker Profiler](profiler-faq.md "profiler-faq.md")
