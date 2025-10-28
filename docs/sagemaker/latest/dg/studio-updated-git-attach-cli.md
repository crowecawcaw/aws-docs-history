# Attach a Git repository (AWS CLI)

This section shows how to attach a Git repository (repo) URL using the AWS CLI. After you
attach the Git repo URL, you can clone it by following the steps in [Clone a Git repo in Amazon SageMaker Studio](#studio-updated-tasks-git "#studio-updated-tasks-git").

## Prerequisites

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS Command Line Interface Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to Amazon SageMaker AI domain. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

## Attach the Git repo to a Amazon SageMaker AI domain (domain) or user profile

Git repo URLs that are associated at the domain level are inherited by all users.
However, Git repo URLs that are associated at the user profile level are scoped to a
specific user. You can attach multiple Git repo URLs to a Amazon SageMaker AI domain or
to a user profile by passing a list of repository URLs.

The following sections show how to attach a Git repo URL to your domain and your user
profile.

### Attach to a Amazon SageMaker AI domain

The following command attaches a Git repo URL to an existing domain:

```
aws sagemaker update-domain --region `region` --domain-id `domain-id` \
    --default-user-settings JupyterLabAppSettings={CodeRepositories=[{RepositoryUrl="`repository`"}]}
```

### Attach to a user

profile

The following command attaches a Git repo URL to an existing user profile:

```
aws sagemaker update-user-profile --domain-id `domain-id` --user-profile-name `user-name`\
    --user-settings JupyterLabAppSettings={CodeRepositories=[{RepositoryUrl="`repository`"}]}
```

## Clone a Git repo in Amazon SageMaker Studio

Amazon SageMaker Studio connects to a local Git repo only. To access the files in the repo,
clone the Git repo from within Studio. To do so, Studio offers a Git extension
for you to enter the URL of a Git repo, clone it into your environment, push changes,
and view commit history.

If the repo is private and requires credentials to access, you receive a prompt to
enter your user credentials. Your credentials include your username and personal access
token. For more information about personal access tokens, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens").

Admins can also attach suggested Git repository URLs at the Amazon SageMaker AI domain or user
profile level. Users can then select the repo URL from the list of suggestions and clone
that into Studio. For more information about attaching suggested repos, see [Attach Suggested Git Repos to Amazon SageMaker Studio Classic](studio-git-attach.md "studio-git-attach.md").
