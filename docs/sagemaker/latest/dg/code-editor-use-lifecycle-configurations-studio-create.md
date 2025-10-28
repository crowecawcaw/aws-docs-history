# Create and attach

lifecycle configurations in Studio

The following section provides AWS CLI commands to create a lifecycle configuration,
attach a lifecycle configuration when creating a new user profile, and attach a lifecycle
configuration when updating a user profile. For prerequisites and general steps on
creating and attaching lifecycle configurations in Studio, see [Lifecycle configuration creation](jl-lcc-create.md "jl-lcc-create.md").

When creating your Studio lifecycle configuration with the
`create-studio-lifecycle-config` command, be sure to specify that the
`studio-lifecycle-config-app-type` is
`CodeEditor`. The following example shows how to
create a new Studio lifecycle configuration for your Code Editor application.

```
aws sagemaker create-studio-lifecycle-config \
--studio-lifecycle-config-name `my-code-editor-lcc` \
--studio-lifecycle-config-content $LCC_CONTENT \
--studio-lifecycle-config-app-type `CodeEditor`
```

Note the ARN of the newly created lifecycle configuration that is returned. When
attaching a lifecycle configuration, provide this ARN within the
`LifecycleConfigArns` list of `CodeEditorAppSettings`.

You can attach a lifecycle configuration when creating a user profile or domain. The
following example shows how to create a new user profile with the lifecycle configuration
attached. You can also create a new domain with a lifecycle configuration attached by
using the [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html") command.

```
# Create a new UserProfile
aws sagemaker create-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings '{
"CodeEditorAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

You can alternatively attach a lifecycle configuration when updating a user profile or
domain. The following example shows how to update a user profile with the lifecycle
configuration attached. You can also update a new domain with a lifecycle configuration
attached by using the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html") command.

```
# Update a UserProfile
aws sagemaker update-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings '{
"CodeEditorAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```
