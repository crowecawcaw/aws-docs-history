# Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Although you can attach multiple lifecycle configuration scripts to a single resource, you
can only set one default lifecycle configuration for each JupyterServer or KernelGateway
application. The behavior of the default lifecycle configuration depends on whether it is
set for JupyterServer or KernelGateway apps.

- JupyterServer apps: When set as the default
  lifecycle configuration script for JupyterServer apps, the lifecycle configuration
  script runs automatically when the user signs in to Studio Classic for the first time or
  restarts Studio Classic. Use this default lifecycle configuration to automate one-time
  setup actions for the Studio Classic developer environment, such as installing notebook
  extensions or setting up a GitHub repo. For an example of this, see [Customize Amazon SageMaker Studio using Lifecycle
  Configurations](https://aws.amazon.com/blogs/machine-learning/customize-amazon-sagemaker-studio-using-lifecycle-configurations/ "https://aws.amazon.com/blogs/machine-learning/customize-amazon-sagemaker-studio-using-lifecycle-configurations/").
- KernelGateway apps: When set as the default
  lifecycle configuration script for KernelGateway apps, the lifecycle configuration
  is selected by default in the Studio Classic launcher. Users can launch a notebook or
  terminal with the default script selected, or they can select a different one from
  the list of lifecycle configurations.
  SageMaker AI supports setting a default lifecycle configuration for the following
  resources:

- Domains
- User profiles
- Shared spaces
  While domains and user profiles support setting a default lifecycle configuration from
  both the Amazon SageMaker AI console and AWS Command Line Interface, shared spaces only support setting a default
  lifecycle configuration from the AWS CLI.

You can set a lifecycle configuration as the default when creating a new resource or
updating an existing resource. The following topics demonstrate how to set a default
lifecycle configuration using the SageMaker AI console and AWS CLI.

## Default lifecycle configuration inheritance

Default lifecycle configurations set at the _domain_ level are
inherited by all users and shared spaces. Default lifecycle configurations set at the
_user_ and _shared space_ level are scoped to
only that user or shared space. User and space defaults override defaults set at the
domain level.

A default KernelGateway lifecycle configuration set for a domain applies to all
KernelGateway applications launched in the domain. Unless the user selects a different
lifecycle configuration from the list presented in the Studio Classic launcher, the default
lifecycle configuration is used. The default script also runs if `No Script`
is selected by the user. For more information about selecting a script, see [Step 3: Launch an application with the
lifecycle configuration](studio-lcc-create-console.md#studio-lcc-create-console-step3 "studio-lcc-create-console.md#studio-lcc-create-console-step3").

###### Topics

- [Set Defaults from the AWS CLI for Amazon SageMaker Studio Classic](studio-lcc-defaults-cli.md "studio-lcc-defaults-cli.md")
- [Set Defaults from the SageMaker AI Console for Amazon SageMaker Studio Classic](studio-lcc-defaults-console.md "studio-lcc-defaults-console.md")
