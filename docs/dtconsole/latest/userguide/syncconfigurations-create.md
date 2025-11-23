# Create a sync configuration

You can use the **create-repository-link** command in the AWS Command Line Interface (AWS CLI)
to create a link between your connection and the external repository to sync to.

Before you can create a sync configuration, you must have already created a repository
link between your connection and your third-party repository.

###### To create a sync configuration

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **create-repository-link** command. Specify the ARN of the
   associated connection, the owner ID, and the repository name. The following command
   creates a sync configuration with a sync type for a resource in CloudFormation. It also
   specifies the repository branch and configuration file in the repository. In this
   example, the resource is a stack named **`mystack`**.

```
aws codeconnections create-sync-configuration --branch main --config-file filename --repository-link-id be8f2017-b016-4a77-87b4-608054f70e77 --resource-name mystack --role-arn arn:aws:iam::`account_id`:role/myrole --sync-type CFN_STACK_SYNC
```

2. This command returns the following output.

```
{
    "SyncConfiguration": {
        "Branch": "main",
        "ConfigFile": "filename",
        "OwnerId": "`account_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkId": "be8f2017-b016-4a77-87b4-608054f70e77",
        "RepositoryName": "MyRepo",
        "ResourceName": "mystack",
        "RoleArn": "arn:aws:iam::`account_id`:role/myrole",
        "SyncType": "CFN_STACK_SYNC"
    }
```
