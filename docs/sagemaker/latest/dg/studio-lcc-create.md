# Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker AI provides interactive applications that enable Studio Classic's visual interface, code
authoring, and run experience. This series shows how to create a lifecycle configuration and
associate it with a SageMaker AI domain.

Application types can be either `JupyterServer` or `KernelGateway`.

- `JupyterServer` applications: This
  application type enables access to the visual interface for Studio Classic. Every user
  and shared space in Studio Classic gets its own JupyterServer application.
- `KernelGateway` applications: This
  application type enables access to the code run environment and kernels for your
  Studio Classic notebooks and terminals. For more information, see [Jupyter Kernel
  Gateway](https://jupyter-kernel-gateway.readthedocs.io/en/latest/ "https://jupyter-kernel-gateway.readthedocs.io/en/latest/").
  For more information about Studio Classic's architecture and Studio Classic applications, see
  [Use Amazon SageMaker Studio Classic
  Notebooks](notebooks.md "notebooks.md").

###### Topics

- [Create a Lifecycle Configuration from the
  AWS CLI for Amazon SageMaker Studio Classic](studio-lcc-create-cli.md "studio-lcc-create-cli.md")
- [Create a Lifecycle Configuration from the SageMaker AI
  Console for Amazon SageMaker Studio Classic](studio-lcc-create-console.md "studio-lcc-create-console.md")
