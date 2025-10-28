# Generative AI in SageMaker notebook environments

[Jupyter AI](https://github.com/jupyterlab/jupyter-ai "https://github.com/jupyterlab/jupyter-ai") is an open-source
extension of JupyterLab integrating generative AI capabilities into Jupyter notebooks. Through
the Jupyter AI chat interface and magic commands, users experiment with code generated from
natural language instructions, explain existing code, ask questions about their local files,
generate entire notebooks, and more. The extension connects Jupyter notebooks with large language
models (LLMs) that users can use to generate text, code, or images, and to ask questions about
their own data. Jupyter AI supports generative model providers such as AI21, Anthropic, AWS
(JumpStart and Amazon Bedrock), Cohere, and OpenAI.

You can also use Amazon Q Developer as an out of the box solution. Instead of having to
manually set up a connection to a model, you can start using Amazon Q Developer with minimal
configuration. When you enable Amazon Q Developer, it becomes the default solution provider
within Jupyter AI. For more information about using Amazon Q Developer, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").

The extension's package is included in [Amazon SageMaker Distribution](https://github.com/aws/sagemaker-distribution "https://github.com/aws/sagemaker-distribution")
[version
1.2 and onwards](https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1 "https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1"). Amazon SageMaker Distribution is a Docker environment for data science and
scientific computing used as the default image of JupyterLab notebook instances. Users of
different IPython environments can install Jupyter AI manually.

In this section, we provide an overview of Jupyter AI capabilities and demonstrate how to
configure models provided by JumpStart or Amazon Bedrock from [JupyterLab](studio-updated-jl.md "studio-updated-jl.md") or [Studio Classic](studio.md "studio.md") notebooks. For
more in-depth information on the Jupyter AI project, refer to its [documentation](https://jupyter-ai.readthedocs.io/en/latest/ "https://jupyter-ai.readthedocs.io/en/latest/"). Alternatively, you
can refer to the blog post _[Generative AI in
Jupyter](https://blog.jupyter.org/generative-ai-in-jupyter-3f7174824862 "https://blog.jupyter.org/generative-ai-in-jupyter-3f7174824862")_ for an overview and examples of key Jupyter AI capabilities.

Before using Jupyter AI and interacting with your LLMs, make sure that you satisfy the
following prerequisites:

- For models hosted by AWS, you should have the ARN of your SageMaker AI endpoint or have access
  to Amazon Bedrock. For other model providers, you should have the API key used to authenticate and
  authorize requests to your model. Jupyter AI supports a wide range of model providers and
  language models, refer to the list of its [supported models](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#model-providers "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#model-providers") to stay updated on the latest available models. For information
  on how to deploy a model in JumpStart, see [Deploy a Model](jumpstart-deploy.md "jumpstart-deploy.md") in the
  JumpStart documentation. You need to request access to [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") to use it as your model provider.
- Ensure that Jupyter AI libraries are present in your environment. If not, install the
  required package by following the instructions in [Jupyter AI installation](sagemaker-jupyterai-installation.md "sagemaker-jupyterai-installation.md").
- Familiarize yourself with the capabilities of Jupyter AI in [Access Jupyter AI Features](sagemaker-jupyterai-overview.md "sagemaker-jupyterai-overview.md").
- Configure the target models you wish to use by following the instructions in [Configure your model
  provider](sagemaker-jupyterai-model-configuration.md "sagemaker-jupyterai-model-configuration.md").
  After completing the prerequisite steps, you can proceed to [Use Jupyter AI in JupyterLab or Studio Classic](sagemaker-jupyterai-use.md "sagemaker-jupyterai-use.md").

###### Topics

- [Jupyter AI installation](sagemaker-jupyterai-installation.md "sagemaker-jupyterai-installation.md")
- [Access Jupyter AI Features](sagemaker-jupyterai-overview.md "sagemaker-jupyterai-overview.md")
- [Configure your model
  provider](sagemaker-jupyterai-model-configuration.md "sagemaker-jupyterai-model-configuration.md")
- [Use Jupyter AI in JupyterLab or Studio Classic](sagemaker-jupyterai-use.md "sagemaker-jupyterai-use.md")
