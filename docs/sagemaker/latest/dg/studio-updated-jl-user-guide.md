# JupyterLab user guide

This guide shows JupyterLab users how to run analytics and machine learning workflows
within SageMaker Studio. You can get fast storage and scale your compute up or down,
depending on your needs.

JupyterLab supports both private and shared spaces. Private spaces are scoped to a single user in a domain.
Shared spaces let other users in your domain collaborate with you in real time.
For information about Studio spaces, see [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").

To get started using JupyterLab, create a space and launch your JupyterLab
application. The space running your JupyterLab application is a JupyterLab space.
The JupyterLab space uses a single Amazon EC2 instance for your compute and a single Amazon EBS
volume for your storage. Everything in your space such as your code, git profile, and
environment variables are stored on the same Amazon EBS volume. The volume has 3000 IOPS and a
throughput of 125 megabytes per second (MBps). You can use the fast storage to open and run
multiple Jupyter notebooks on the same instance. You can also switch kernels in a notebook
very quickly.

Your administrator has configured the default Amazon EBS storage settings for your space. The
default storage size is 5 GB, but you can increase the amount of space that you get. You can
talk to your administrator to provide you with guidelines.

You can switch the Amazon EC2 instance type that you’re using to run JupyterLab, scaling your
compute up or down depending on your needs. The **Fast launch** instances
start up much faster than the other instances.

Your administrator might provide you with a lifecycle configuration that customizes your
environment. You can specify the lifecycle configuration when you create the space.

If your administrator gives you access to an Amazon EFS, you can configure your JupyterLab
space to access it.

By default, the JupyterLab application uses the SageMaker distribution image. This includes
support for many machine learning, analytics, and deep learning packages. However, if you
need a custom image, your administrator can help provide access to the custom
images.

The Amazon EBS volume persists independently from the life of an instance. You won’t lose your
data when you change instances. Use the conda and pip package management libraries to create
reproducible custom environments that persist even when you switch instance types.

After you open JupyterLab, you can configure your environment using the terminal. To open
the terminal, navigate to the **Launcher** and choose
**Terminal**.

The following are examples of different ways that you can configure an environment in
JupyterLab.

###### Note

Within Studio, you can use lifecycle configurations to customize your
environment, but we recommend using a package manager instead. Using lifecycle
configurations is a more error-prone method. It’s easier to add or remove dependencies
than it is to debug a lifecycle configuration script. It can also increase the
JupyterLab startup time.

For information about lifecycle configurations, see [Lifecycle configurations with JupyterLab](jl-lcc.md "jl-lcc.md").

###### Topics

- [Create a space](studio-updated-jl-user-guide-create-space.md "studio-updated-jl-user-guide-create-space.md")
- [Configure a space](studio-updated-jl-user-guide-configure-space.md "studio-updated-jl-user-guide-configure-space.md")
- [Customize your
  environment using a package manager](studio-updated-jl-user-guide-customize-package-manager.md "studio-updated-jl-user-guide-customize-package-manager.md")
- [Clean up a conda
  environment](studio-updated-jl-clean-up-conda.md "studio-updated-jl-clean-up-conda.md")
- [Share conda
  environments between instance types](studio-updated-jl-create-conda-share-environment.md "studio-updated-jl-create-conda-share-environment.md")
- [Use Amazon Q to Expedite Your Machine
  Learning Workflows](studio-updated-jl-user-guide-use-amazon-q.md "studio-updated-jl-user-guide-use-amazon-q.md")
