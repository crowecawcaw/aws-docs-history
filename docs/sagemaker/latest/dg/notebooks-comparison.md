# How Are Amazon SageMaker Studio Classic Notebooks Different from

Notebook Instances?

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

When you're starting a new notebook, we recommend that you create the notebook in
Amazon SageMaker Studio Classic instead of launching a notebook instance from the Amazon SageMaker AI console. There are
many benefits to using a Studio Classic notebook, including the following:

- **Faster:** Starting a Studio Classic notebook is faster than
  launching an instance-based notebook. Typically, it is 5-10 times faster than
  instance-based notebooks.
- **Easy notebook sharing:** Notebook sharing is an
  integrated feature in Studio Classic. Users can generate a shareable link that reproduces the
  notebook code and also the SageMaker image required to execute it, in just a few clicks.
- **Latest Python SDK:** Studio Classic notebooks come
  pre-installed with the latest [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
- **Access all Studio Classic features:** Studio Classic notebooks
  are accessed from within Studio Classic. This enables you to build, train, debug, track, and
  monitor your models without leaving Studio Classic.
- **Persistent user directories:** Each member of a Studio
  team gets their own home directory to store their notebooks and other files. The directory
  is automatically mounted onto all instances and kernels as they're started, so their
  notebooks and other files are always available. The home directories are stored in
  Amazon Elastic File System (Amazon EFS) so that you can access them from other services.
- **Direct access:** When using IAM Identity Center, you use your IAM Identity Center
  credentials through a unique URL to directly access Studio Classic. You don't have to interact
  with the AWS Management Console to run your notebooks.
- **Optimized images:** Studio Classic notebooks are equipped
  with a set of predefined SageMaker image settings to get you started faster.

###### Note

Studio Classic notebooks don't support _local mode_. However, you can use
a notebook instance to train a sample of your dataset locally, and then use the same code in
a Studio Classic notebook to train on the full dataset.

When you open a notebook in SageMaker Studio Classic, the view is an extension of the JupyterLab
interface. The primary features are the same, so you'll find the typical features of a Jupyter
notebook and JupyterLab. For more information about the Studio Classic interface, see [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
