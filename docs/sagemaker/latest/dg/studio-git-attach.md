# Attach Suggested Git Repos to Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic offers a Git extension for you to enter the URL of a Git repository (repo),
clone it into your environment, push changes, and view commit history. In addition to this
Git extension, you can also attach suggested Git repository URLs at the Amazon SageMaker AI domain or
user profile level. Then, you can select the repo URL from the list of suggestions and clone
that into your environment using the Git extension in Studio Classic.

The following topics show how to attach Git repo URLs to a domain or user profile from
the AWS CLI and SageMaker AI console. You'll also learn how to detach these repository URLs.

###### Topics

- [Attach a Git Repository from the AWS CLI for Amazon SageMaker Studio Classic](studio-git-attach-cli.md "studio-git-attach-cli.md")
- [Attach a Git Repository from the SageMaker AI
  Console for Amazon SageMaker Studio Classic](studio-git-attach-console.md "studio-git-attach-console.md")
- [Detach Git Repos from Amazon SageMaker Studio Classic](studio-git-detach.md "studio-git-detach.md")
