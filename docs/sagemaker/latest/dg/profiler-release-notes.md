# Release notes for profiling capabilities of

Amazon SageMaker AI

See the following release notes to track the latest updates for profiling capabilities of
Amazon SageMaker AI.

## March 21, 2024

**Currency updates**

[SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md") has added support for
PyTorch v2.2.0, v2.1.0, and v2.0.1.

**AWS Deep Learning Containers pre-installed with
SageMaker Profiler**

[SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md") is packaged in the
following [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

- SageMaker AI Framework Container for PyTorch v2.2.0
- SageMaker AI Framework Container for PyTorch v2.1.0
- SageMaker AI Framework Container for PyTorch v2.0.1

## December 14, 2023

**Currency updates**

[SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md") has added support for
TensorFlow v2.13.0.

**Breaking changes**

This release involves a breaking change. The SageMaker Profiler Python package name is changed
from `smppy` to `smprof`. If you have been using the previous
version of the package while you have started using the latest [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") for TensorFlow listed in the following section,
make sure that you update the package name from `smppy` to
`smprof` in the import statement in your training script.

**AWS Deep Learning Containers pre-installed with
SageMaker Profiler**

[SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md") is packaged in the
following [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

- SageMaker AI Framework Container for TensorFlow v2.13.0
- SageMaker AI Framework Container for TensorFlow v2.12.0

If you use the previous versions of the [framework containers](profiler-support.md#profiler-support-frameworks "profiler-support.md#profiler-support-frameworks") such TensorFlow v2.11.0, the SageMaker Profiler Python package is
still available as `smppy`. If you are uncertain which version or the package
name you should use, replace the import statement of the SageMaker Profiler package with the
following code snippet.

```
try:
    import smprof
except ImportError:
    # backward-compatability for TF 2.11 and PT 1.13.1 images
    import smppy as smprof
```

## August 24, 2023

**New features**

Released Amazon SageMaker Profiler, a profiling and visualization capability of SageMaker AI to deep dive
into compute resources provisioned while training deep learning models and gain
visibility into operation-level details. SageMaker Profiler provides Python modules
(`smppy`) for adding annotations throughout PyTorch or TensorFlow
training scripts and activating SageMaker Profiler. You can access the modules through the SageMaker AI
Python SDK and AWS Deep Learning Containers. For any jobs run with the SageMaker Profiler Python
modules, you can load the profile data in the SageMaker Profiler UI application that provides a
summary dashboard and a detailed timeline. To learn more, see [Amazon SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md").

This release of the SageMaker Profiler Python package is integrated into the following [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") for PyTorch and TensorFlow.

- PyTorch v2.0.0
- PyTorch v1.13.1
- TensorFlow v2.12.0
- TensorFlow v2.11.0
