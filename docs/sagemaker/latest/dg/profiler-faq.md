# Troubleshooting for SageMaker Profiler

Use the following question-and-answer pairs to troubleshoot problems while using
SageMaker Profiler.

**Q. I’m getting an error message, `ModuleNotFoundError: No
 module named 'smppy'`**

Since December 2023, the name of the SageMaker Profiler Python package has changed from
`smppy` to `smprof` to resolve a duplicate package name issue;
`smppy` is already used by an open source package.

Therefore, if you have been using `smppy` since before December 2023 and
experiencing this `ModuleNotFoundError` issue, it might be due to the
outdated package name in your training script while having the latested
`smprof` package installed or using one of the latest [SageMaker AI framework images pre-installed
with SageMaker Profiler](profiler-support.md#profiler-support-frameworks "profiler-support.md#profiler-support-frameworks"). In this case, make sure that you replace
all mentions of `smppy` with `smprof` throughout your training
script.

While updating the SageMaker Profiler Python package name in your training scripts, to avoid
confusion around which version of the package name you should use, consider using a
conditional import statement as shown in the following code snippet.

```
try:
    import smprof
except ImportError:
    # backward-compatability for TF 2.11 and PT 1.13.1 images
    import smppy as smprof
```

Also note that if you have been using `smppy` while upgrading to the latest
PyTorch or TensorFlow versions, make sure that you install the latest
`smprof` package by following instructions at [(Optional) Install the SageMaker Profiler
Python package](profiler-prepare.md#profiler-install-python-package "profiler-prepare.md#profiler-install-python-package").

**Q. I’m getting an error message, `ModuleNotFoundError: No
 module named 'smprof'`**

First, make sure that you use one of the officially supported SageMaker AI Framework
Containers. If you don’t use one of those, you can install the `smprof`
package by following instructions at [(Optional) Install the SageMaker Profiler
Python package](profiler-prepare.md#profiler-install-python-package "profiler-prepare.md#profiler-install-python-package").

**Q. I’m not able to import
`ProfilerConfig`**

If you are unable to import `ProfilerConfig` in your job launcher
script using the SageMaker Python SDK, your local environment or the Jupyter kernel
might have a significantly outdated version of the SageMaker Python SDK. Make sure
that you upgrade the SDK to the latest version.

```
$ pip install --upgrade sagemaker
```

**Q. I’m getting an error message, `aborted: core dumped when
 importing smprof into my training script`**

In an earlier version of `smprof`, this issue occurs with PyTorch 2.0+
and PyTorch Lightning. To resolve this issue, also install the latest
`smprof` package by following instructions at [(Optional) Install the SageMaker Profiler
Python package](profiler-prepare.md#profiler-install-python-package "profiler-prepare.md#profiler-install-python-package").

**Q. I cannot find the SageMaker Profiler UI from SageMaker Studio. How can
I find it?**

If you have access to the SageMaker AI console, choose one of the following options.

- [Option 1: Launch
  the SageMaker Profiler UI from the domain details page](profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-console-smdomain "profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-console-smdomain")
- [Option
  2: Launch the SageMaker Profiler UI application from the SageMaker Profiler landing page in the SageMaker AI
  console](profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-console-profiler-landing-page "profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-console-profiler-landing-page")
  If you are a domain user and don't have access to the SageMaker AI console, you can access
  the application through SageMaker Studio Classic. If this is your case, choose the following
  option.

- [Option 3: Use the application launcher function in the SageMaker AI Python
  SDK](profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-app-launcher-function "profiler-access-smprofiler-ui.md#profiler-access-smprofiler-ui-app-launcher-function")
