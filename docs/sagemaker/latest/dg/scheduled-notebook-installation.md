# Installation guide

The following provides information about what you need to install
to use Notebook Jobs in your JupyterLab environment.

**For Amazon SageMaker Studio and Amazon SageMaker Studio Lab**

If your notebook is in Amazon SageMaker Studio or Amazon SageMaker Studio Lab, you don’t need to perform
additional installation—SageMaker Notebook Jobs is built into the platform. To set up
required permissions for Studio, see [Set up policies and permissions for
Studio](scheduled-notebook-policies-studio.md "scheduled-notebook-policies-studio.md").

**For local Jupyter notebooks**

If you want to use SageMaker Notebook Jobs for your local JupyterLab environment, you need to
perform additional installation.

To install SageMaker Notebook Jobs, complete the following steps:

1. Install Python 3. For details, see [Installing Python 3 and Python
   Packages](https://www.codecademy.com/article/install-python3 "https://www.codecademy.com/article/install-python3").
2. Install JupyterLab version 4 or higher. For details, see [JupyterLab SDK documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html "https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html").
3. Install the AWS CLI. For details, see [Installing or updating the
   latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
4. Install two sets of permissions. The IAM user needs permissions to submit jobs to
   SageMaker AI, and once submitted, the notebook job itself assumes an IAM role that needs
   permissions to access resources depending on the job tasks.
   1. If you haven’t yet created an IAM user, see [Creating an IAM user in your AWS
      account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md").
   2. If you haven’t yet created your notebook job role, see [Creating a role to delegate
      permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").
   3. Attach the necessary permissions and trust policy to attach to your user and role.
      For step-by-step instructions and permission details, see [Install policies and permissions for
      local Jupyter environments](scheduled-notebook-policies-other.md "scheduled-notebook-policies-other.md").

5. Generate AWS credentials for your newly-created IAM user and save them in the
   credentials file (~/.aws/credentials) of your JupyterLab environment. You can do this with
   the CLI command `aws configure`. For instructions, see section _Set and view configuration settings using commands_ in [Configuration
   and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").
6. (optional) By default, the scheduler extension uses a pre-built SageMaker AI Docker image with
   Python 2.0. Any non-default kernel used in the notebook should be installed in the
   container. If you want to run your notebook in a container or Docker image, you need to
   create an Amazon Elastic Container Registry (Amazon ECR) image. For information about how to push a Docker image to an Amazon ECR,
   see [Pushing a Docker
   Image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md").
7. Add the JupyterLab extension for SageMaker Notebook Jobs. You can add it to your JupyterLab
   environment with the command: `pip install amazon_sagemaker_jupyter_scheduler`.
   You may need to restart your Jupyter server with the command:`sudo systemctl restart
jupyter-server`.
8. Start JupyterLab with the command: `jupyter lab`.
9. Verify that the Notebook Jobs widget (
   ![Blue icon of a calendar with a checkmark, representing a scheduled task or event.](images/icons/notebook-schedule.png)
   ) appears in your Jupyter notebook taskbar.
