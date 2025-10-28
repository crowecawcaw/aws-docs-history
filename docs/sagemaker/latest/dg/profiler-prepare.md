# Prepare and run a training job with SageMaker Profiler

Setting up to running a training job with the SageMaker Profiler consists of two steps: adapting
the training script and configuring the SageMaker training job launcher.

###### Topics

- [Step 1: Adapt your training
  script using the SageMaker Profiler Python modules](#profiler-prepare-training-script "#profiler-prepare-training-script")
- [Step 2: Create a SageMaker AI framework estimator
  and activate SageMaker Profiler](#profiler-profilerconfig "#profiler-profilerconfig")
- [(Optional) Install the SageMaker Profiler
  Python package](#profiler-install-python-package "#profiler-install-python-package")

## Step 1: Adapt your training

script using the SageMaker Profiler Python modules

To start capturing kernel runs on GPUs while the training job is running, modify
your training script using the SageMaker Profiler Python modules. Import the library and add
the `start_profiling()` and `stop_profiling()` methods to
define the beginning and the end of profiling. You can also use optional custom
annotations to add markers in the training script to visualize hardware activities
during particular operations in each step.

Note that the annotators extract operations from GPUs. For profiling operations in
CPUs, you don’t need to add any additional annotations. CPU profiling is also
activated when you specify the profiling configuration, which you’ll practice in
[Step 2: Create a SageMaker AI framework estimator
and activate SageMaker Profiler](#profiler-profilerconfig "#profiler-profilerconfig").

###### Note

Profiling an entire training job is not the most efficient use of resources. We
recommend profiling at most 300 steps of a training job.

###### Important

The release on [December 14, 2023](profiler-release-notes.md#profiler-release-notes-20231214 "profiler-release-notes.md#profiler-release-notes-20231214") involves a
breaking change. The SageMaker Profiler Python package name is changed from
`smppy` to `smprof`. This is effective in the [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") for TensorFlow v2.12 and later.

If you use one of the previous versions of the [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") such TensorFlow v2.11.0, the SageMaker Profiler
Python package is still available as `smppy`. If you are uncertain
about which version or the package name you should use, replace the import
statement of the SageMaker Profiler package with the following code snippet.

```
try:
    import smprof
except ImportError:
    # backward-compatability for TF 2.11 and PT 1.13.1 images
    import smppy as smprof
```

**Approach 1.** Use the context manager
`smprof.annotate` to annotate full functions

You can wrap full functions with the `smprof.annotate()` context
manager. This wrapper is recommended if you want to profile by functions instead of
code lines. The following example script shows how to implement the context manager
to wrap the training loop and full functions in each iteration.

```
import smprof

SMProf = smprof.SMProfiler.instance()
config = smprof.Config()
config.profiler = {
    "EnableCuda": "1",
}
SMProf.configure(config)
SMProf.start_profiling()

for epoch in range(args.epochs):
    if world_size > 1:
        sampler.set_epoch(epoch)
    tstart = time.perf_counter()
    for i, data in enumerate(trainloader, 0):
        with smprof.annotate(`"step_"+str(i)`):
            inputs, labels = data
            inputs = inputs.to("cuda", non_blocking=True)
            labels = labels.to("cuda", non_blocking=True)

            optimizer.zero_grad()

            with smprof.annotate(`"Forward"`):
                outputs = net(inputs)
            with smprof.annotate(`"Loss"`):
                loss = criterion(outputs, labels)
            with smprof.annotate(`"Backward"`):
                loss.backward()
            with smprof.annotate(`"Optimizer"`):
                optimizer.step()

SMProf.stop_profiling()
```

**Approach 2.** Use
`smprof.annotation_begin()` and `smprof.annotation_end()`
to annotate specific code line in functions

You can also define annotations to profile specific code lines. You can set the
exact starting point and end point of profiling at the level of individual code
lines, not by the functions. For example, in the following script, the
`step_annotator` is defined at the beginning of each iteration and
ends at the end of the iteration. Meanwhile, other detailed annotators for each
operations are defined and wrap around the target operations throughout each
iteration.

```
import smprof

SMProf = smprof.SMProfiler.instance()
config = smprof.Config()
config.profiler = {
    "EnableCuda": "1",
}
SMProf.configure(config)
SMProf.start_profiling()

for epoch in range(args.epochs):
    if world_size > 1:
        sampler.set_epoch(epoch)
    tstart = time.perf_counter()
    for i, data in enumerate(trainloader, 0):
        step_annotator = smprof.annotation_begin(`"step_" + str(i)`)

        inputs, labels = data
        inputs = inputs.to("cuda", non_blocking=True)
        labels = labels.to("cuda", non_blocking=True)
        optimizer.zero_grad()

        forward_annotator = smprof.annotation_begin(`"Forward"`)
        outputs = net(inputs)
        smprof.annotation_end(forward_annotator)

        loss_annotator = smprof.annotation_begin(`"Loss"`)
        loss = criterion(outputs, labels)
        smprof.annotation_end(loss_annotator)

        backward_annotator = smprof.annotation_begin(`"Backward"`)
        loss.backward()
        smprof.annotation_end(backward_annotator)

        optimizer_annotator = smprof.annotation_begin(`"Optimizer"`)
        optimizer.step()
        smprof.annotation_end(optimizer_annotator)

        smprof.annotation_end(step_annotator)

SMProf.stop_profiling()
```

After annotating and setting up the profiler initiation modules, save the script
to submit using a SageMaker training job launcher in the following Step 2. The
sample launcher assumes that the training script is named
`train_with_profiler_demo.py`.

## Step 2: Create a SageMaker AI framework estimator

and activate SageMaker Profiler

The following procedure shows how to prepare a SageMaker AI framework estimator for
training using the SageMaker Python SDK.

1. Set up a `profiler_config` object using the
   `ProfilerConfig` and `Profiler` modules as
   follows.

```
from sagemaker import ProfilerConfig, Profiler
profiler_config = ProfilerConfig(
    profile_params = Profiler(cpu_profiling_duration=3600)
)
```

The following is the description of the `Profiler` module and
its argument.

    * `Profiler`: The module for activating SageMaker Profiler with the
     training job.




    	+ `cpu_profiling_duration` (int): Specify the time
    	 duration in seconds for profiling on CPUs. Default is 3600
    	 seconds.

2. Create a SageMaker AI framework estimator with the `profiler_config`
   object created in the previous step. The following code shows an example of
   creating a PyTorch estimator. If you want to create a TensorFlow estimator,
   import `sagemaker.tensorflow.TensorFlow` instead, and specify one
   of the [TensorFlow
   versions](profiler-support.md#profiler-support-frameworks-tensorflow "profiler-support.md#profiler-support-frameworks-tensorflow") supported by SageMaker Profiler. For more information about
   supported frameworks and instance types, see [SageMaker AI framework images pre-installed
   with SageMaker Profiler](profiler-support.md#profiler-support-frameworks "profiler-support.md#profiler-support-frameworks").

```
import sagemaker
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    framework_version="`2.0.0`",
    role=sagemaker.get_execution_role(),
    entry_point="`train_with_profiler_demo.py`", # your training job entry point
    source_dir=`source_dir`, # source directory for your training script
    output_path=`output_path`,
    base_job_name="`sagemaker-profiler-demo`",
    hyperparameters=`hyperparameters`, # if any
    instance_count=`1`, # Recommended to test with < 8
    instance_type=`ml.p4d.24xlarge`,
    profiler_config=`profiler_config`
)
```

3. Start the training job by running the `fit` method. With
   `wait=False`, you can silence the training job logs and let
   it run in the background.

```
estimator.fit(wait=False)
```

While running the training job or after the job has completed, you can go to the
next topic at [Open the SageMaker Profiler UI application](profiler-access-smprofiler-ui.md "profiler-access-smprofiler-ui.md") and start exploring
and visualizing the saved profiles.

If you want to directly access the profile data saved in the Amazon S3
bucket, use the following script to retrieve the S3 URI.

```
import os
# This is an ad-hoc function to get the S3 URI
# to where the profile output data is saved
def get_detailed_profiler_output_uri(estimator):
    config_name = None
    for processing in estimator.profiler_rule_configs:
        params = processing.get("RuleParameters", dict())
        rule = config_name = params.get("rule_to_invoke", "")
        if rule == "DetailedProfilerProcessing":
            config_name = processing.get("RuleConfigurationName")
            break
    return os.path.join(
        estimator.output_path,
        estimator.latest_training_job.name,
        "rule-output",
        config_name,
    )

print(
    f"Profiler output S3 bucket: ",
    get_detailed_profiler_output_uri(estimator)
)
```

## (Optional) Install the SageMaker Profiler

Python package

To use SageMaker Profiler on PyTorch or TensorFlow framework images not listed in [SageMaker AI framework images pre-installed
with SageMaker Profiler](profiler-support.md#profiler-support-frameworks "profiler-support.md#profiler-support-frameworks"), or on your own custom Docker container
for training, you can install SageMaker Profiler by using one of the [SageMaker Profiler Python package binary
files](profiler-support.md#profiler-python-package "profiler-support.md#profiler-python-package").

**Option 1: Install the SageMaker Profiler package while launching a
training job**

If you want to use SageMaker Profiler for training jobs using PyTorch or TensorFlow images
not listed in [SageMaker AI framework images pre-installed
with SageMaker Profiler](profiler-support.md#profiler-support-frameworks "profiler-support.md#profiler-support-frameworks"), create a
`requirements.txt` file and locate it under the path you specify to
the `source_dir` parameter of the SageMaker AI framework estimator in [Step 2](#profiler-profilerconfig "#profiler-profilerconfig"). For more information about
setting up a `requirements.txt` file in general, see [Using third-party libraries](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#using-third-party-libraries "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#using-third-party-libraries") in the _SageMaker Python SDK
documentation_. In the `requirements.txt` file, add one of
the S3 bucket paths for the [SageMaker Profiler Python package binary
files](profiler-support.md#profiler-python-package "profiler-support.md#profiler-python-package").

```
# requirements.txt
https://smppy.s3.amazonaws.com/`tensorflow/cu112/smprof-0.3.332-cp39-cp39-linux_x86_64.whl`
```

**Option 2: Install the SageMaker Profiler package in your custom Docker
containers**

If you use a custom Docker container for training, add one of the [SageMaker Profiler Python package binary
files](profiler-support.md#profiler-python-package "profiler-support.md#profiler-python-package") to your Dockerfile.

```
# Install the smprof package version compatible with your CUDA version
RUN pip install https://smppy.s3.amazonaws.com/`tensorflow/cu112/smprof-0.3.332-cp39-cp39-linux_x86_64.whl`
```

For guidance on running a custom Docker container for training on SageMaker AI in general,
see [Adapting your own training container](adapt-training-container.md "adapt-training-container.md").
