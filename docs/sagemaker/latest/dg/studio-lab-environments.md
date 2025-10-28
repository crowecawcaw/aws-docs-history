# Studio Lab pre-installed environments

Amazon SageMaker Studio Lab uses conda environments to manage packages (or libraries) for your projects.
This guide explains what conda environments are, how to interact with them, and the different
pre-installed environments available in Studio Lab.

A conda environment is a directory that contains a collection of packages you have
installed. It allows you to create isolated environments with specific package versions,
preventing conflicts between projects with different dependencies.

You can interact with conda environments in Studio Lab in two ways:

- Terminal: Use the terminal to create, activate, and manage environments.
- JupyterLab Notebook: When opening a JupyterLab notebook, select the kernel with the
  environment name you wish to use, to use the packages installed in that environment.
  For a walkthrough on managing environments, see [Manage your environment](studio-lab-use-manage.md "studio-lab-use-manage.md")

Studio Lab comes with several pre-installed environments that are either persistent or
non-persistent memory environments. Any changes made to persistent memory environments will
remain for your next session. Any changes to non-persistent memory environments will not remain
for your next sessions, but the packages within will be updated and tested for compatability by
Amazon SageMaker AI. Here's an overview of each environment and its use case:

- `sagemaker-distribution`: A non-persistent environment managed by Amazon SageMaker AI.
  It contains popular packages for machine learning, data science, and visualization. This
  environment is regularly updated and tested for compatibility. Use this environment if you
  want a fully-managed setup with common packages pre-installed.

The `sagemaker-distribution` environment is closely related to the
environment used in Amazon SageMaker Studio Classic, so after graduating from Studio Lab to Studio Classic the
notebooks should run similarly. For information on exporting your environment from Studio Lab
to Studio Classic, see [Export an Amazon SageMaker Studio Lab environment to
Amazon SageMaker Studio Classic](studio-lab-use-migrate.md "studio-lab-use-migrate.md").

- `default`: A persistent environment with minimal packages pre-installed. Use
  this environment if you want to customize it significantly by installing additional
  packages.
- `studiolab`: A persistent environment where JupyterLab and related packages
  installed. Use this environment for configuring the JupyterLab user interface and installing
  Jupyter server extensions.
- `studiolab-safemode`: A non-persistent environment activated automatically
  when there's an issue with your project runtime. Use this environment for troubleshooting
  purposes. For information on troubleshooting, see [Troubleshooting](studio-lab-troubleshooting.md "studio-lab-troubleshooting.md").
- `base`: A non-persistent environment used for system tooling. This
  environment is not intended for customer use.
  To view the packages in an environment, run the command `conda list`.

For more information on installing packages within your environment, see [Customize your
environment](studio-lab-use-manage.md#studio-lab-use-manage-conda-default-customize "studio-lab-use-manage.md#studio-lab-use-manage-conda-default-customize").

If you plan to graduate from Studio Lab to Amazon SageMaker Studio Classic, see [Export an Amazon SageMaker Studio Lab environment to
Amazon SageMaker Studio Classic](studio-lab-use-migrate.md "studio-lab-use-migrate.md").

For information on SageMaker images and their versions, see [Amazon SageMaker Images Available for Use With
Studio Classic Notebooks](notebooks-available-images.md "notebooks-available-images.md").
