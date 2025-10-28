# Detach lifecycle configurations

To update your script, you must create a new lifecycle configuration script and attach it
to the respective Amazon SageMaker AI domain (domain), user profile, or shared space. A lifecycle configuration script
can't be changed after it's created. For more information about creating and attaching the
lifecycle configuration, see [Lifecycle configuration creation](jl-lcc-create.md "jl-lcc-create.md").

The following section shows how to detach a lifecycle configuration using the AWS Command Line Interface
(AWS CLI).

## Detach using the AWS CLI

To detach a lifecycle configuration using the (AWS CLI), remove the desired lifecycle
configuration from the list of lifecycle configurations attached to the resource. You
then pass the list as part of the respective command:

- [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html")
- [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html")
- [update-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html")

For example, the following command removes all lifecycle configurations for the
JupyterLab application that's attached to the domain.

```
aws sagemaker update-domain --domain-id `domain-id` \
--region `region` \
--default-user-settings '{
"JupyterLabAppSettings": {
  "LifecycleConfigArns":
    []
  }
}'
```
