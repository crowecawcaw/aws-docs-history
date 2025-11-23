# JupyterLab versioning

###### Important

JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to JupyterLab 4 notebook instances for continued support. For more information, see [JupyterLab version maintenance](#nbi-jl-version-maintenance "#nbi-jl-version-maintenance").

The Amazon SageMaker notebook instance interface is based on JupyterLab, which is a web-based
interactive development environment for notebooks, code, and data. Notebooks now support using
either JupyterLab 1, JupyterLab 3, or JupyterLab 4. A single notebook instance can run a
single instance of JupyterLab (at most). You can have multiple notebook instances with
different JupyterLab versions.

You can configure your notebook to run your preferred JupyterLab version by selecting the
appropriate platform identifier. Use either the AWS CLI or the SageMaker AI console when creating your
notebook instance. For more information about platform identifiers, see [AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md")
and [Amazon Linux 2 notebook instances](nbi-al2.md "nbi-al2.md"). If you don’t explicitly configure a platform identifier, your notebook
instance defaults to running JupyterLab 1.

###### Topics

- [JupyterLab version maintenance](#nbi-jl-version-maintenance "#nbi-jl-version-maintenance")
- [JupyterLab 4](#nbi-jl-4 "#nbi-jl-4")
- [JupyterLab 3](#nbi-jl-3 "#nbi-jl-3")
- [Create a notebook with your JupyterLab version](nbi-jl-create.md "nbi-jl-create.md")
- [View the JupyterLab version of a notebook from the
  console](nbi-jl-view.md "nbi-jl-view.md")

## JupyterLab version maintenance

JupyterLab 1 and JupyterLab 3 platforms reached end of standard support on June 30, 2025. As of this date:

- You can no longer create new or restart stopped JupyterLab 1 and JupyterLab 3 notebook instances.
- Existing in-service JupyterLab 1 and JupyterLab 3 notebook instances may continue to function, but no longer receive SageMaker AI security updates or critical bug fixes.
- You are responsible for managing the security of these deprecated instances.
- If issues arise with existing JupyterLab 1 or JupyterLab 3 notebook instances, SageMaker AI cannot guarantee their continued availability. You must migrate your workload to a JupyterLab 4 notebook instance.

Migrate your work to JupyterLab 4 notebook instances (the latest version's platform identifier is
[notebook-al2023-v1](nbi-al2023.md "nbi-al2023.md")) to ensure you have a secure and supported environment. This allows you to leverage the
latest versions of Jupyter notebooks, JupyterLab, and other ML libraries. For instructions, see [migrate your work to an SageMaker AI notebook instance with Amazon Linux 2](https://aws.amazon.com/blogs//machine-learning/migrate-your-work-to-amazon-sagemaker-notebook-instance-with-amazon-linux-2/ "https://aws.amazon.com/blogs//machine-learning/migrate-your-work-to-amazon-sagemaker-notebook-instance-with-amazon-linux-2/").

## JupyterLab 4

JupyterLab 4 support is available only on the Amazon Linux 2 operating system platform.
JupyterLab 4 includes the following features that are not available in JupyterLab 3:

- Optimized rendering for a faster experience
- Opt-in settings for faster tab switching and better performance with long notebooks.
  For more information, see the blog post [JupyterLab 4.0 is
  Here](https://blog.jupyter.org/jupyterlab-4-0-is-here-388d05e03442 "https://blog.jupyter.org/jupyterlab-4-0-is-here-388d05e03442").
- Upgraded text editor
- New extension manager installing from pypi
- Added improvements to the UI, including document search and accessibility
  improvements

You can run JupyterLab 4 by specifying [notebook-al2023-v1](nbi-al2023.md "nbi-al2023.md")
(the latest and recommended version) or [notebook-al2-v3](nbi-al2.md "nbi-al2.md") as the
platform identifier when creating your notebook instance.

###### Note

If you attempt to migrate to a JupyterLab 4 Notebook Instance from another JupyterLab
version, the package version changes between JupyterLab 3 and JupyterLab 4 might break any
existing lifecycle configurations or Jupyter/JupyterLab extensions.

**Package version changes**

JupyterLab 4 has the following package version changes from JupyterLab 3:

- JupyterLab has been upgraded from 3.x to 4.x.
- Jupyter notebook has been upgraded from 6.x to 7.x.
- jupyterlab-git has been updated to version 0.50.0.

## JupyterLab 3

###### Important

JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to JupyterLab 4 notebook instances for continued support. For more information, see [JupyterLab version maintenance](#nbi-jl-version-maintenance "#nbi-jl-version-maintenance").

JupyterLab 3 support is available only on the Amazon Linux 2 operating system platform.
JupyterLab 3 includes the following features that are not available in JupyterLab 1. For
more information about these features, see [JupyterLab 3.0 is
released!](https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb "https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb").

- Visual debugger when using the following kernels:
  - conda_pytorch_p38
  - conda_tensorflow2_p38
  - conda_amazonei_pytorch_latest_p37

- File browser filter
- Table of Contents (TOC)
- Multi-language support
- Simple mode
- Single interface mode
- Live editing SVG files with updated rendering
- User interface for notebook cell tags

### Important changes to JupyterLab 3

For information about important changes when using JupyterLab 3, see the following
JupyterLab change logs:

- [v2.0.0](https://github.com/jupyterlab/jupyterlab/releases "https://github.com/jupyterlab/jupyterlab/releases")
- [v3.0.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#for-developers "https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#for-developers")

**Package version changes**

JupyterLab 3 has the following package version changes from JupyterLab 1:

- JupyterLab has been upgraded from 1.x to 3.x.
- Jupyter notebook has been upgraded from 5.x to 6.x.
- jupyterlab-git has been updated to version 0.37.1.
- nbserverproxy 0.x (0.3.2) has been replaced with jupyter-server-proxy 3.x
  (3.2.1).
