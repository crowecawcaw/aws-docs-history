# Detach lifecycle

configurations in Studio

To detach lifecycle configurations for Code Editor, you can use either the console or the
AWS CLI. For steps on detaching lifecycle configurations from the Studio console, see
[Detach lifecycle configurations](jl-lcc-delete.md "jl-lcc-delete.md").

To detach a lifecycle configuration using the AWS CLI, remove the desired lifecycle
configuration from the list of lifecycle configurations attached to the resource. Then
pass the list as part of the respective command:

- [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html")
- [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html")
  For example, the following command removes all lifecycle configurations for the Code Editor
  application attached to the domain.

```
aws sagemaker update-domain --domain-id `domain-id` \
--default-user-settings '{
"CodeEditorAppSettings": {
  "LifecycleConfigArns":
    []
  }
}'
```
