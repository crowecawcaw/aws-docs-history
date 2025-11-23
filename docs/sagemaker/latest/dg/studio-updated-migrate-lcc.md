# (Optional) Migrate custom images and lifecycle

configurations

You must update your custom images and lifecycle configuration (LCC) scripts to work with
the simplified local run model in Amazon SageMaker Studio. If you have not created custom images or
lifecycle configurations in your domain, skip this phase.

Amazon SageMaker Studio Classic operates in a split environment with:

- A `JupyterServer` application running the Jupyter
  Server.
- Studio Classic notebooks running on one or more `KernelGateway`
  applications.
  Studio has shifted away from a split environment. Studio runs the
  JupyterLab and Code Editor, based on Code-OSS, Visual Studio Code - Open Source applications in a local runtime model. For more information
  about the change in architecture, see [Boost productivity on Amazon SageMaker Studio](https://aws.amazon.com/blogs//machine-learning/boost-productivity-on-amazon-sagemaker-studio-introducing-jupyterlab-spaces-and-generative-ai-tools/ "https://aws.amazon.com/blogs//machine-learning/boost-productivity-on-amazon-sagemaker-studio-introducing-jupyterlab-spaces-and-generative-ai-tools/").

## Migrate custom images

Your existing Studio Classic custom images may not work in Studio. We recommend
creating a new custom image that satisfies the requirements for use in Studio. The
release of Studio simplifies the process to build custom images by providing [SageMaker Studio image support policy](sagemaker-distribution.md "sagemaker-distribution.md"). SageMaker AI
Distribution images include popular libraries and packages for machine learning, data
science, and data analytics visualization. For a list of base SageMaker Distribution images
and Amazon Elastic Container Registry account information, see [Amazon SageMaker Images Available for Use With
Studio Classic Notebooks](notebooks-available-images.md "notebooks-available-images.md").

To build a custom image, complete one of the following.

- Extend a SageMaker Distribution image with custom packages and modules. These
  images are pre-configured with JupyterLab and Code Editor, based on Code-OSS, Visual Studio Code - Open Source.
- Build a custom Dockerfile file by following the instructions in [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md"). You must install
  JupyterLab and the open source CodeServer on the image to make it
  compatible with Studio.

## Migrate lifecycle

configurations

Because of the simplified local runtime model in Studio, we recommend migrating
the structure of your existing Studio Classic LCCs. In Studio Classic, you often have to create
separate lifecycle configurations for both KernelGateway and
JupyterServer applications. Because the JupyterServer
and KernelGateway applications run on separate compute resources within
Studio Classic, Studio Classic LCCs can be one of either type:

- JupyterServer LCC: These LCCs mostly govern a user’s home
  actions, including setting proxy, creating environment variables, and
  auto-shutdown of resources.
- KernelGateway LCC: These LCCs govern Studio Classic notebook
  environment optimizations. This includes updating numpy package versions in the
  `Data Science 3.0` kernel and installing the snowflake package in
  `Pytorch 2.0 GPU` kernel.

In the simplified Studio architecture, you only need one LCC script that runs at
application start up. While migration of your LCC scripts varies based on development
environment, we recommend combining JupyterServer and
KernelGateway LCCs to build a combined LCC.

LCCs in Studio can be associated with one of the following applications:

- JupyterLab
- Code Editor

Users can select the LCC for the respective application type when creating a space or
use the default LCC set by the admin.

###### Note

Existing Studio Classic auto-shutdown scripts do not work with Studio. For an
example Studio auto-shutdown script, see [SageMaker Studio Lifecycle Configuration examples](https://github.com/aws-samples/sagemaker-studio-apps-lifecycle-config-examples "https://github.com/aws-samples/sagemaker-studio-apps-lifecycle-config-examples").

### Considerations when refactoring LCCs

Consider the following differences between Studio Classic and Studio when
refactoring your LCCs.

- JupyterLab and Code Editor applications, when created, are run as
  `sagemaker-user` with `UID:1001` and
  `GID:101`. By default, `sagemaker-user` has
  permissions to assume sudo/root permissions. KernelGateway
  applications are run as `root` by default.
- SageMaker Distribution images that run inside JupyterLab and Code Editor apps use
  the Debian-based package manager, `apt-get`.
- Studio JupyterLab and Code Editor applications use the
  Conda package manager. SageMaker AI creates a single base
  Python3
  Conda environment when a Studio application is launched.
  For information about updating packages in the base Conda
  environment and creating new Conda environments, see [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md"). In contrast, not all
  KernelGateway applications use Conda as a
  package manager.
- The Studio JupyterLab application uses `JupyterLab
4.0`, while Studio Classic uses `JupyterLab 3.0`. Validate
  that all JupyterLab extensions you use are compatible with
  `JupyterLab 4.0`. For more information about extensions, see
  [Extension
  Compatibility
  with JupyterLab 4.0](https://github.com/jupyterlab/jupyterlab/issues/14590 "https://github.com/jupyterlab/jupyterlab/issues/14590").
