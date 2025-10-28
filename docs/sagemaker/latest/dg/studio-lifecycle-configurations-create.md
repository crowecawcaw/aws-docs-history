# Create and attach lifecycle

configurations

You can create and attach lifecycle configurations using either the AWS Management Console or the
AWS Command Line Interface.

###### Topics

- [Create and attach
  lifecycle configurations (AWS CLI)](#studio-lifecycle-configurations-create-cli "#studio-lifecycle-configurations-create-cli")
- [Create and attach
  lifecycle configurations (console)](#studio-lifecycle-configurations-create-console "#studio-lifecycle-configurations-create-console")

## Create and attach

lifecycle configurations (AWS CLI)

###### Important

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide
  your AWS credentials. For information about AWS credentials, see
  [Understanding and
  getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to Amazon SageMaker AI domain. For conceptual information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). For
  a quickstart guide, see [Use quick setup for Amazon SageMaker AI](onboard-quick-start.md "onboard-quick-start.md").

The following procedure shows how to create a lifecycle configuration script that
prints `Hello World` within Code Editor or JupyterLab.

###### Note

Each script can have up to **16,384
characters**.

1. From your local machine, create a file named `my-script.sh`
   with the following content:

```
#!/bin/bash
set -eux
echo 'Hello World!'
```

2. Use the following to convert your `my-script.sh` file into
   base64 format. This requirement prevents errors that occur from spacing and
   line break encoding.

```
LCC_CONTENT=`openssl base64 -A -in my-script.sh`
```

3. Create a lifecycle configuration for use with Studio. The following
   command creates a lifecycle configuration that runs when you launch an
   associated `JupyterLab` application:

```
aws sagemaker create-studio-lifecycle-config \
--region `region` \
--studio-lifecycle-config-name `my-lcc` \
--studio-lifecycle-config-content $LCC_CONTENT \
--studio-lifecycle-config-app-type `application-type`
```

For `studio-lifecycle-config-app-type`, specify either
`CodeEditor` or
`JupyterLab`.

###### Note

The ARN of the newly created lifecycle configuration that is returned.
This ARN is required to attach the lifecycle configuration to your
application.

To ensure that the environments are customized properly, users and administrators
use different commands to attach lifecycle configurations.

To attach the lifecycle configuration, you must update the
`UserSettings` for your domain or user profile. Lifecycle
configuration scripts that are associated at the domain level are
inherited by all users. However, scripts that are associated at the user
profile level are scoped to a specific user.

You can create a new user profile, domain, or space with a lifecycle
configuration attached by using the following commands:

- [create-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html")
- [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html")
- [create-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html")
  The following command creates a user profile with a lifecycle
  configuration for a JupyterLab application. Add the lifecycle configuration
  ARN from the preceding step to the `JupyterLabAppSettings` of the
  user. You can add multiple lifecycle configurations at the same time by
  passing a list of them. When a user launches a JupyterLab application with
  the AWS CLI, they can specify a lifecycle configuration instead of using the
  default one. The lifecycle configuration that the user passes must belong to
  the list of lifecycle configurations in
  `JupyterLabAppSettings`.

```
# Create a new UserProfile
aws sagemaker create-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"JupyterLabAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

The following command creates a user profile with a lifecycle
configuration for a Code Editor application. Add the lifecycle configuration ARN
from the preceding step to the `CodeEditorAppSettings` of the
user. You can add multiple lifecycle configurations at the same time by
passing a list of them. When a user launches a Code Editor application with the
AWS CLI, they can specify a lifecycle configuration instead of using the
default one. The lifecycle configuration that the user passes must belong to
the list of lifecycle configurations in
`CodeEditorAppSettings`.

```
# Create a new UserProfile
aws sagemaker create-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"CodeEditorAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

To attach the lifecycle configuration, you must update the
`UserSettings` for your user profile.

The following command creates a user profile with a lifecycle
configuration for a JupyterLab application. Add the lifecycle configuration
ARN from the preceding step to the `JupyterLabAppSettings` of
your user profile.

```
# Update a UserProfile
aws sagemaker update-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"JupyterLabAppSettings": {
  "BuiltInLifecycleConfigArn":"`lifecycle-configuration-arn`"
  }
}'
```

The following command creates a user profile with a lifecycle
configuration for a Code Editor application. Add the lifecycle configuration ARN
from the preceding step to the `CodeEditorAppSettings` of your
user profile. The lifecycle configuration that the user passes must belong
to the list of lifecycle configurations in
`CodeEditorAppSettings`.

```
# Update a UserProfile
aws sagemaker update-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"CodeEditorAppSettings": {
  "BuiltInLifecycleConfigArn":"`lifecycle-configuration-arn`"
  }
}'
```

## Create and attach

lifecycle configurations (console)

To create and attach lifecycle configurations in the AWS Management Console, navigate to the
[Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") and choose
**Lifecycle configurations** in the left-hand navigation. The
console will guide you through the process of creating the lifecycle
configuration.
