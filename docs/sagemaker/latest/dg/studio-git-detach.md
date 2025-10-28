# Detach Git Repos from Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

This guide shows how to detach Git repository URLs from an Amazon SageMaker AI domain or user profile
using the AWS CLI or Amazon SageMaker AI console.

###### Topics

- [Detach a Git repo using the AWS CLI](#studio-git-detach-cli "#studio-git-detach-cli")
- [Detach the Git repo using the SageMaker AI
  console](#studio-git-detach-console "#studio-git-detach-console")

## Detach a Git repo using the AWS CLI

To detach all Git repo URLs from a domain or user profile, you must pass an empty
list of code repositories. This list is passed as part of the
`JupyterServerAppSettings` parameter in an `update-domain` or
`update-user-profile` command. To detach only one Git repo URL, pass the
code repositories list without the desired Git repo URL. This section shows how to
detach all Git repo URLs from your domain or user profile using the AWS Command Line Interface
(AWS CLI).

### Detach from a domain

The following command detaches all Git repo URLs from a domain.

```
aws sagemaker update-domain --region `region` --domain-name `domain-name` \
    --domain-settings JupyterServerAppSettings={CodeRepositories=[]}
```

### Detach from a user

profile

The following command detaches all Git repo URLs from a user profile.

```
aws sagemaker update-user-profile --domain-name `domain-name` --user-profile-name `user-name`\
    --user-settings JupyterServerAppSettings={CodeRepositories=[]}
```

## Detach the Git repo using the SageMaker AI

console

The following sections show how to detach a Git repo URL from a domain or user
profile using the SageMaker AI console.

### Detach from a domain

Use the following steps to detach a Git repo URL from an existing
domain.

###### To detach a Git repo URL from an existing domain

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select the domain with the Git repo URL that you want to
   detach.
5. On the **domain details** page, choose the
   **Environment** tab.
6. On the **Suggested code repositories for the domain**
   tab, select the Git repository URL to detach.
7. Choose
   **Detach**.
8. From the new window, choose **Detach**.

### Detach from a user

profile

Use the following steps to detach a Git repo URL from a user profile.

###### To detach a Git repo URL from a user profile

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select the domain that includes the user profile with the Git repo URL
   that you want to detach.
5. On the **domain details** page, choose the
   **User profiles** tab.
6. Select the user profile with the Git repo URL that you want to
   detach.
7. On the **User details** page, choose
   **Edit**.
8. On the **Studio settings** page, select the Git repo URL
   to detach from the **Suggested code repositories for the
   user** tab.
9. Choose
   **Detach**.
10. From the new window, choose **Detach**.
