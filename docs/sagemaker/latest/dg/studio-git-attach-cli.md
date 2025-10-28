# Attach a Git Repository from the AWS CLI for Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following topic shows how to attach a Git repository URL using the AWS CLI, so that
Amazon SageMaker Studio Classic automatically suggests it for cloning. After you attach the Git repository
URL, you can clone it by following the steps in [Clone a Git Repository in Amazon SageMaker Studio Classic](studio-tasks-git.md "studio-tasks-git.md").

## Prerequisites

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to Amazon SageMaker AI domain. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

## Attach the Git repo to a domain or

user profile

Git repo URLs associated at the domain level are inherited by all users. However,
Git repo URLs that are associated at the user profile level are scoped to a specific
user. You can attach multiple Git repo URLs to a domain or user profile by passing a
list of repository URLs.

The following sections show how to attach a Git repo URL to your domain and user
profile.

### Attach to a domain

The following command attaches a Git repo URL to an existing domain.

```
aws sagemaker update-domain --region `region` --domain-id `domain-id` \
    --default-user-settings JupyterServerAppSettings={CodeRepositories=[{RepositoryUrl="`repository`"}]}
```

### Attach to a user

profile

The following shows how to attach a Git repo URL to an existing user
profile.

```
aws sagemaker update-user-profile --domain-id `domain-id` --user-profile-name `user-name`\
    --user-settings JupyterServerAppSettings={CodeRepositories=[{RepositoryUrl="`repository`"}]}
```
