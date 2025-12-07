# Manage your environment

Amazon SageMaker Studio Lab provides pre-installed environments for your Studio Lab notebook instances.
Environments allow you to start up a Studio Lab notebook instance with the packages you want to
use. This is done by installing packages in the environment and then selecting the environment
as a Kernel.

Studio Lab has various environments pre-installed for you. You will typically want to use the
`sagemaker-distribution` environment if you want to use a fully managed environment
that already contains many popular packages used for machine learning (ML) engineers and data
scientists. Otherwise you can use the `default` environment if you want persistent
customization for your environment. For more information on the available pre-installed Studio Lab
environments, see [Studio Lab pre-installed environments](studio-lab-environments.md "studio-lab-environments.md").

You can customize your environment by adding new packages (or libraries) to it. You can also
create new environments from Studio Lab, import compatible environments, reset your environment to
create space, and more.

The following commands are for running in a Studio Lab terminal. However, while installing
packages it is highly recommended to install them within your Studio Lab Jupyter notebook. This
ensures that the packages are installed in the intended environment. To run the commands in a
Jupyter notebook, prefix the command with a `%` before running the cell. For example,
the code snippet `pip list` in a terminal is the same as `%pip list` in a
Jupyter notebook.

The following sections give information about your `default` conda environment,
how to customize it, and how to add and remove conda environments. For a list of sample
environments that you can install into Studio Lab, see [Creating Custom
conda Environments](https://github.com/aws/studio-lab-examples/tree/main/custom-environments "https://github.com/aws/studio-lab-examples/tree/main/custom-environments"). To use these sample environment YAML files with Studio Lab, see [Step 4: Install your Studio Lab conda environments
in Studio Classic](studio-lab-use-migrate.md#studio-lab-use-migrate-step4 "studio-lab-use-migrate.md#studio-lab-use-migrate-step4").

###### Topics

- [Your default environment](#studio-lab-use-manage-conda-default "#studio-lab-use-manage-conda-default")
- [View environments](#studio-lab-use-view-conda-envs "#studio-lab-use-view-conda-envs")
- [Create, activate, and use new conda
  environments](#studio-lab-use-manage-conda-new-conda "#studio-lab-use-manage-conda-new-conda")
- [Using sample Studio Lab environments](#studio-lab-use-manage-conda-sample "#studio-lab-use-manage-conda-sample")
- [Customize your
  environment](#studio-lab-use-manage-conda-default-customize "#studio-lab-use-manage-conda-default-customize")
- [Refresh Studio Lab](#studio-lab-use-manage-conda-reset "#studio-lab-use-manage-conda-reset")

## Your default environment

Studio Lab uses conda environments to encapsulate the software packages that are needed to
run notebooks. Your project contains a default conda environment, named `default`,
with the [IPython kernel](https://ipython.readthedocs.io/en/stable/ "https://ipython.readthedocs.io/en/stable/"). This
environment serves as the default kernel for your Jupyter notebooks.

## View environments

To view the environments in Studio Lab you can use a terminal or Jupyter notebook. The
following command will be for a Studio Lab terminal. If you wish to run the corresponding
commands in a Jupyter notebook, see [Manage your environment](studio-lab-use-manage.md "studio-lab-use-manage.md").

Open the Studio Lab terminal by opening the **File Browser** panel (
![Black square icon representing a placeholder or empty image.](images/studio/icons/folder.png)
), choose the plus (**+**) sign on the menu at the top of
the file browser to open the **Launcher**, then choose
**Terminal**. From the Studio Lab terminal, list the conda environments by
running the following.

```
conda env list
```

This command outputs a list of the conda environments and their locations in the file
system. When you onboard to Studio Lab, you automatically activate the `studiolab` 
conda environment. The following is an example of listed environments after you
onboard.

```
# conda environments:
#
default                  /home/studio-lab-user/.conda/envs/default
studiolab             *  /home/studio-lab-user/.conda/envs/studiolab
studiolab-safemode       /opt/amazon/sagemaker/safemode-home/.conda/envs/studiolab-safemode
base                     /opt/conda
sagemaker-distribution     /opt/conda/envs/sagemaker-distribution
```

The `*` marks the activated environment.

## Create, activate, and use new conda

environments

If you would like to maintain multiple environments for different use cases, you can
create new conda environments in your project. The following sections show how to create and
activate new conda environments. For a Jupyter notebook that shows how to create a custom
environment, see [Setting up a Custom Environment in SageMaker Studio Lab](https://github.com/aws/studio-lab-examples/blob/main/custom-environments/custom_environment.ipynb "https://github.com/aws/studio-lab-examples/blob/main/custom-environments/custom_environment.ipynb").

###### Note

Maintaining multiple environments counts against your available Studio Lab memory.

**Create conda environment**

To create a conda environment, run the following conda command from your terminal. This
example creates a new environment with Python 3.9.

```
conda create --name `<ENVIRONMENT_NAME>` python=3.9
```

Once the conda environment is created, you can view the environment in your environment
list. For more information on how to view your environment list, see [View environments](#studio-lab-use-view-conda-envs "#studio-lab-use-view-conda-envs").

**Activate a conda environment**

To activate any conda environment, run the following command in the terminal.

```
conda activate `<ENVIRONMENT_NAME>`
```

When you run this command, any packages installed using conda or pip are installed in the
environment. For more information on installing packages, see [Customize your
environment](#studio-lab-use-manage-conda-default-customize "#studio-lab-use-manage-conda-default-customize").

**Use a conda environment**

1. To use your new conda environments with notebooks, make sure the
   `ipykernel` package is installed in the environment.

```
conda install ipykernel
```

2. Once the `ipykernel` package is installed in the environment, you can
   select the environment as the kernel for your notebook.

You may need to restart JupyterLab to see the environment available as a kernel. This
can be done by choosing **Amazon SageMaker Studio Lab** in the top menu of your Studio Lab
open project, and choosing **Restart JupyterLab...**. 3. You can choose the kernel for an existing notebook or when you create a new
one.

    * For an existing notebook: open the notebook and choose the current kernel
     from the right side of the top menu. You can choose the kernel you wish to use from
     the drop-down menu.
    * For a new notebook: open the Studio Lab launcher and choose the kernel under
     **Notebook**. This will open the notebook with the kernel you
     choose.


    For an overview of the Studio Lab UI, see [Amazon SageMaker Studio Lab UI overview](studio-lab-use-ui.md "studio-lab-use-ui.md").

## Using sample Studio Lab environments

Studio Lab provides sample custom environments through the [SageMaker Studio Lab Examples](https://github.com/aws/studio-lab-examples "https://github.com/aws/studio-lab-examples") repository.
The following shows how to clone and build these environments.

1. Clone the SageMaker Studio Lab Examples GitHub repository by following the instructions in
   [Use GitHub resources](studio-lab-use-external.md#studio-lab-use-external-clone-github "studio-lab-use-external.md#studio-lab-use-external-clone-github").
2. In Studio Lab choose the **File Browser** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/folder.png)
   ) on the left menu, so that the **File Browser**
   panel shows on the left.
3. Navigate to the `studio-lab-examples/custom-environments` directory in the
   File Browser.
4. Open the directory for the environment that you want to build.
5. Right click the `.yml` file in the folder, then select **Build
   conda Environment**.
6. You can now use the environment as a kernel after your conda environment has finished
   building. For instructions on how to use an existing environment as a kernel, see [Create, activate, and use new conda
   environments](#studio-lab-use-manage-conda-new-conda "#studio-lab-use-manage-conda-new-conda")

## Customize your

environment

You can customize your environment by installing and removing extensions and packages as
needed. Studio Lab comes with environments with packages pre-installed and using an existing
environment may save you time and memory, as pre-installed packages do not count against your
available Studio Lab memory. For more information on the available pre-installed Studio Lab
environments, see [Studio Lab pre-installed environments](studio-lab-environments.md "studio-lab-environments.md").

Any installed extensions and packages installed on your `default` environment
will persist in your project. That is, you do not need to install your packages for every
project runtime session. However, extensions and packages installed on your
`sagemaker-distribution` environment will not persist, so you will need to
install new packages during your next session. Thus, it is highly recommended to install
packages within your notebook to ensure that the packages are installed in the intended
environment.

To view your environments, run the command `conda env list`.

To activate your environment, run the command `conda
 activate `<ENVIRONMENT_NAME>``.

To view the packages in an environment, run the command `conda list`.

**Install packages**

It is highly recommended to install your packages within your Jupyter notebook to ensure
that your packages are installed in the intended environment. To install additional packages
to your environment from a Jupyter notebook, run one of the following commands in a cell within
your Jupyter notebook. These commands install packages in the currently activated environment.

- `%conda install `<PACKAGE>``
- `%pip install `<PACKAGE>``

We don't recommend using the `!pip` or `!conda` commands because
they can behave in unexpected ways when you have multiple environments.

After you install new packages to your environment, you may need to restart the kernel to
ensure that the packages work in your notebook. This can be done by choosing
**Amazon SageMaker Studio Lab** in the top menu of your Studio Lab open project and choosing
**Restart JupyterLab...**.

**Remove packages**

To remove a package, run the command

```
%conda remove `<PACKAGE_NAME>`
```

This command will also remove any package that depends on
`<PACKAGE_NAME>`, unless a replacement can be
found without that dependency.

To remove all of the packages in an environment, run the command

```
conda deactivate
&& conda env remove --name
`<ENVIRONMENT_NAME>`
```

## Refresh Studio Lab

To refresh Studio Lab, remove all of your environments and files.

1. List all conda environments.

```
conda env list
```

2. Activate the base environment.

```
conda activate base
```

3. Remove each environment in the list of conda environments, besides base.

```
conda remove --name `<ENVIRONMENT_NAME>` --all
```

4. Delete all of the files on your Studio Lab.

```
rm -rf *.*
```
