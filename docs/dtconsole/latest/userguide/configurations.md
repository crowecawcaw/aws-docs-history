# Working with sync configurations for linked

repositories

In AWS CodeConnections, you use a connection to associate AWS resources to a third-party repository,
such as GitHub, Bitbucket Cloud, GitHub Enterprise Server, and GitLab. Using the
`CFN_STACK_SYNC` sync type, you can create a sync configuration, which allows AWS
to sync content from a Git repository to update a specified AWS resource. AWS CloudFormation integrates
with connections so that you can use Git sync to manage your template and parameter files in a
linked repository that you sync with.

After creating a connection, you can use the connections CLI or the AWS CloudFormation console to create
your repository link and sync configuration.

- Repository link: A repository link creates an association between your connection and an
  external Git repository. The repository link allows Git sync to monitor and sync changes to
  files in a specified Git repository.
- Sync configuration: Use the sync configuration to sync content from a Git repository to
  update a specified AWS resource.
  For more information, see the [_AWS CodeConnections API
  Reference_](../../../codeconnections/latest/APIReference/Welcome.md "../../../codeconnections/latest/APIReference/Welcome.md").

For a tutorial that walks you through creating a sync configuration for an AWS CloudFormation stack using
the AWS CloudFormation console, see [Working with AWS CloudFormation Git
sync](../../../AWSCloudFormation/latest/UserGuide/git-sync.md "../../../AWSCloudFormation/latest/UserGuide/git-sync.md") in the _CloudFormation User Guide_.

###### Topics

- [Working with repository links](repositorylinks.md "repositorylinks.md")
- [Working with sync configurations](syncconfigurations.md "syncconfigurations.md")
