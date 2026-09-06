

# Working with sync configurations for linked repositories
<a name="configurations"></a>

In AWS CodeConnections, you use a connection to associate AWS resources to a third-party repository, such as GitHub, Bitbucket Cloud, GitHub Enterprise Server, and GitLab. Using the `CFN_STACK_SYNC` sync type, you can create a sync configuration, which allows AWS to sync content from a Git repository to update a specified AWS resource. CloudFormation integrates with connections so that you can use Git sync to manage your template and parameter files in a linked repository that you sync with.

After creating a connection, you can use the connections CLI or the CloudFormation console to create your repository link and sync configuration. 
+ Repository link: A repository link creates an association between your connection and an external Git repository. The repository link allows Git sync to monitor and sync changes to files in a specified Git repository.
+ Sync configuration: Use the sync configuration to sync content from a Git repository to update a specified AWS resource. 

For more information, see the [*AWS CodeConnections API Reference*](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html). 

For a tutorial that walks you through creating a sync configuration for an CloudFormation stack using the CloudFormation console, see [Working with CloudFormation Git sync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync.html) in the *CloudFormation User Guide*.

**Topics**
+ [Working with repository links](repositorylinks.md)
+ [Working with sync configurations](syncconfigurations.md)