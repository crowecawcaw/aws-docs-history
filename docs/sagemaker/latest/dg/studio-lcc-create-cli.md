# Create a Lifecycle Configuration from the

AWS CLI for Amazon SageMaker Studio Classic

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following topic shows how to create a lifecycle configuration using the AWS CLI to
automate customization for your Studio Classic environment.

## Prerequisites

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to SageMaker AI domain by following the steps in [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

## Step 1: Create a lifecycle

configuration

The following procedure shows how to create a lifecycle configuration script that
prints `Hello World`.

###### Note

Each script can have up to **16,384
characters**.

1. From your local machine, create a file named `my-script.sh` with
   the following content.

```
#!/bin/bash
set -eux
echo 'Hello World!'
```

2. Convert your `my-script.sh` file into base64 format. This
   requirement prevents errors that occur from spacing and line break
   encoding.

```
LCC_CONTENT=`openssl base64 -A -in my-script.sh`
```

3. Create a lifecycle configuration for use with Studio Classic. The following command creates
   a lifecycle configuration that runs when you launch an associated
   `KernelGateway` application.

```
aws sagemaker create-studio-lifecycle-config \
--region `region` \
--studio-lifecycle-config-name `my-studio-lcc` \
--studio-lifecycle-config-content $LCC_CONTENT \
--studio-lifecycle-config-app-type KernelGateway
```

Note the ARN of the newly created lifecycle configuration that is returned.
This ARN is required to attach the lifecycle configuration to your
application.

## Step 2: Attach the lifecycle configuration

to your domain, user profile, or shared space

To attach the lifecycle configuration, you must update the `UserSettings`
for your domain or user profile, or the `SpaceSettings` for a shared space.
Lifecycle configuration scripts that are associated at the domain level are inherited by
all users. However, scripts that are associated at the user profile level are scoped to
a specific user, while scripts that are associated at the shared space level are scoped
to the shared space.

The following example shows how to create a new user profile with the lifecycle
configuration attached. You can also create a new domain or space with a lifecycle
configuration attached by using the [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html") and [create-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html") commands, respectively.

Add the lifecycle configuration ARN from the previous step to the settings for the
appropriate app type. For example, place it in the `JupyterServerAppSettings`
of the user. You can add multiple lifecycle configurations at the same time by passing a
list of lifecycle configurations. When a user launches a JupyterServer application with
the AWS CLI, they can pass a lifecycle configuration to use instead of the default. The
lifecycle configuration that the user passes must belong to the list of lifecycle
configurations in `JupyterServerAppSettings`.

```
# Create a new UserProfile
aws sagemaker create-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"JupyterServerAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

The following example shows how to update an existing shared space to attach the
lifecycle configuration. You can also update an existing domain or user profile with a
lifecycle configuration attached by using the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html") or [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html") command. When you update the list of lifecycle
configurations attached, you must pass all lifecycle configurations as part of the list.
If a lifecycle configuration is not part of this list, it will not be attached to the
application.

```
aws sagemaker update-space --domain-id `domain-id` \
--space-name `space-name` \
--region `region` \
--space-settings '{
"JupyterServerAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

For information about setting a default lifecycle configuration for a resource, see
[Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md").

## Step 3: Launch application with lifecycle

configuration

After you attach a lifecycle configuration to a domain, user profile, or space, the
user can select it when launching an application with the AWS CLI. This section describes
how to launch an application with an attached lifecycle configuration. For information
about changing the default lifecycle configuration after launching a JupyterServer
application, see [Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md").

Launch the desired application type using the `create-app` command and
specify the lifecycle configuration ARN in the `resource-spec` argument.

- The following example shows how to create a `JupyterServer`
  application with an associated lifecycle configuration. When creating the
  `JupyterServer`, the `app-name` must be
  `default`. The lifecycle configuration ARN passed as part of the
  `resource-spec` parameter must be part of the list of lifecycle
  configuration ARNs specified in `UserSettings` for your domain or
  user profile, or `SpaceSettings` for a shared space.

```
aws sagemaker create-app --domain-id `domain-id` \
--region `region` \
--user-profile-name `user-profile-name` \
--app-type JupyterServer \
--resource-spec LifecycleConfigArn=`lifecycle-configuration-arn` \
--app-name default
```

- The following example shows how to create a `KernelGateway`
  application with an associated lifecycle configuration.

```
aws sagemaker create-app --domain-id `domain-id` \
--region `region` \
--user-profile-name `user-profile-name` \
--app-type KernelGateway \
--resource-spec LifecycleConfigArn=`lifecycle-configuration-arn`,SageMakerImageArn=`sagemaker-image-arn`,InstanceType=`instance-type` \
--app-name `app-name`
```
