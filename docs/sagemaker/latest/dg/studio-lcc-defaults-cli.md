# Set Defaults from the AWS CLI for Amazon SageMaker Studio Classic

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

You can set default lifecycle configuration scripts from the AWS CLI for the
following resources:

- Domains
- User profiles
- Shared spaces
  The following sections outline how to set default lifecycle configuration
  scripts from the AWS CLI.

###### Topics

- [Prerequisites](#studio-lcc-defaults-cli-prereq "#studio-lcc-defaults-cli-prereq")
- [Set a default lifecycle configuration when creating a new
  resource](#studio-lcc-defaults-cli-new "#studio-lcc-defaults-cli-new")
- [Set a default lifecycle configuration for an existing
  resource](#studio-lcc-defaults-cli-existing "#studio-lcc-defaults-cli-existing")

## Prerequisites

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS CLI version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to SageMaker AI domain by following the steps in [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Create a lifecycle
  configuration following the steps in [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](studio-lcc-create.md "studio-lcc-create.md").

## Set a default lifecycle configuration when creating a new

resource

To set a default lifecycle configuration when creating a new domain, user profile,
or space, pass the ARN of your previously created lifecycle configuration as part of
one of the following AWS CLI commands:

- [create-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html")
- [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-domain.html")
- [create-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html")

You must pass the lifecycle configuration ARN for the following values in the
KernelGateway or JupyterServer default settings:

- `DefaultResourceSpec`:`LifecycleConfigArn` - This specifies the default
  lifecycle configuration for the application type.

- `LifecycleConfigArns` - This is the list of all lifecycle configurations attached
  to the application type. The default lifecycle configuration must also be part
  of this list.

For example, the following API call creates a new user profile with a default
lifecycle configuration.

```
aws sagemaker create-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"KernelGatewayAppSettings": {
    "DefaultResourceSpec": {
            "InstanceType": "ml.t3.medium",
            "LifecycleConfigArn": "`lifecycle-configuration-arn`"
         },
    "LifecycleConfigArns": [`lifecycle-configuration-arn-list`]
  }
}'
```

## Set a default lifecycle configuration for an existing

resource

To set or update the default lifecycle configuration for an existing resource,
pass the ARN of your previously created lifecycle configuration as part of one of
the following AWS CLI commands:

- [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html")
- [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html")
- [update-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-space.html")

You must pass the lifecycle configuration ARN for the following values in the
KernelGateway or JupyterServer default settings:

- `DefaultResourceSpec`:`LifecycleConfigArn` - This
  specifies the default lifecycle configuration for the application
  type.

- `LifecycleConfigArns` - This is the list of all lifecycle
  configurations attached to the application type. The default lifecycle configuration must also be part
  of this list.

For example, the following API call updates a user profile with a default
lifecycle configuration.

```
aws sagemaker update-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"KernelGatewayAppSettings": {
    "DefaultResourceSpec": {
            "InstanceType": "ml.t3.medium",
            "LifecycleConfigArn": "`lifecycle-configuration-arn`"
         },
    "LifecycleConfigArns": [`lifecycle-configuration-arn-list`]
  }
}'
```

The following API call updates a domain to set a new default lifecycle
configuration.

```
aws sagemaker update-domain --domain-id `domain-id` \
--region `region` \
--default-user-settings '{
"JupyterServerAppSettings": {
    "DefaultResourceSpec": {
            "InstanceType": "system",
            "LifecycleConfigArn": "`lifecycle-configuration-arn`"
         },
    "LifecycleConfigArns": [`lifecycle-configuration-arn-list`]
  }
}'
```
