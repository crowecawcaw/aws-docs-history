# Jupyter AI installation

To use Jupyter AI, you must first install the Jupyter AI package. For [Amazon SageMaker AI
Distribution](https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1 "https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1") users, we recommend selecting the SageMaker Distribution image version 1.2
or later. No further installation is necessary. Users of JupyterLab in Studio can choose
the version of their Amazon SageMaker Distribution when creating a space.

For users of other IPython environments, the version of the recommended Jupyter AI package
depends on the version of JupyterLab they are using.

The Jupyter AI distribution consists of two packages.

- `jupyter_ai`: This package provides a JupyterLab extension and a native
  chat user interface (UI). It acts as a conversational assistant using the large language
  model of your choice.
- `jupyter_ai_magics`: This package provides the IPython `%%ai`
  and `%ai` magic commands with which you can invoke a large language model (LLM)
  from your notebook cells.

###### Note

Installing `jupyter_ai` also installs `jupyter_ai_magics`.
However, you can install `jupyter_ai_magics` independently without JupyterLab or
`jupyter_ai`. The magic commands `%%ai` and `%ai` work in
any IPython kernel environment. If you only install `jupyter_ai_magics`, you
can't use the chat UI.

For users of JupyterLab 3, in particular Studio Classic users, we recommend installing
`jupyter-ai`
[version 1.5.x](https://pypi.org/project/jupyter-ai/#history "https://pypi.org/project/jupyter-ai/#history") or any later
1.x version. However, we highly recommend using Jupyter AI with JupyterLab 4. The
`jupyter-ai` version compatible with JupyterLab 3 may not allow users to set
additional model parameters such as temperature, top-k and top-p sampling, max tokens or max
length, or user acceptance license agreements.

For users of JupyterLab 4 environments that do not use SageMaker Distribution, we recommend
installing `jupyter-ai`
[version 2.5.x](https://pypi.org/project/jupyter-ai/#history "https://pypi.org/project/jupyter-ai/#history") or any later
2.x version.

See the installation instructions in the _Installation_
section of [Jupyter AI documentation](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#installation-via-pip "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#installation-via-pip").
