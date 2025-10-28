# Detach Git repo URLs

This section shows how to detach Git repository URLs from an Amazon SageMaker AI domain (domain) or a
user profile. You can detach repo URLs by using the AWS Command Line Interface (AWS CLI) or the Amazon SageMaker AI
console.

## Detach a Git repo using the

AWS CLI

To detach all Git repo URLs from a domain or user profile, you must pass an empty list
of code repositories. This list is passed as part of the
`JupyterLabAppSettings` parameter in an `update-domain` or
`update-user-profile` command. To detach only one Git repo URL, pass the
code repositories list without the desired Git repo URL.

### Detach from an Amazon SageMaker AI domain

The following command detaches all Git repo URLs from a domain:

```
aws sagemaker update-domain --region `region` --domain-name `domain-name` \
    --domain-settings JupyterLabAppSettings={CodeRepositories=[]}
```

### Detach from a user

profile

The following command detaches all Git repo URLs from a user profile:

```
aws sagemaker update-user-profile --domain-name `domain-name` --user-profile-name `user-name`\
    --user-settings JupyterLabAppSettings={CodeRepositories=[]}
```
