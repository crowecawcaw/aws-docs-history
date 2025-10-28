# Update and Detach Lifecycle Configurations in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

A lifecycle configuration script can't be changed after it's created. To update your
script, you must create a new lifecycle configuration script and attach it to the respective
domain, user profile, or shared space. For more information about creating and attaching the
lifecycle configuration, see [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](studio-lcc-create.md "studio-lcc-create.md").

The following topic shows how to detach a lifecycle configuration using the AWS CLI and SageMaker AI
console.

###### Topics

- [Prerequisites](#studio-lcc-delete-pre "#studio-lcc-delete-pre")
- [Detach using the AWS CLI](#studio-lcc-delete-cli "#studio-lcc-delete-cli")

## Prerequisites

Before detaching a lifecycle configuration, you must complete the following prerequisite.

- To successfully detach a lifecycle configuration, no running application can be
  using the lifecycle configuration. You must first shut down the running applications as
  shown in [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md "studio-tasks-update.md").

## Detach using the AWS CLI

To detach a lifecycle configuration using the AWS CLI, remove the desired lifecycle
configuration from the list of lifecycle configurations attached to the resource and
pass the list as part of the respective command:

- [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html")
- [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html")
- [update-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html")

For example, the following command removes all lifecycle configurations for
KernelGateways attached to the domain.

```
aws sagemaker update-domain --domain-id `domain-id` \
--region `region` \
--default-user-settings '{
"KernelGatewayAppSettings": {
  "LifecycleConfigArns":
    []
  }
}'
```
