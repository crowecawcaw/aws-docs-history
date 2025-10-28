# Update a sync configuration

You can use the **update-sync-configuration** command in the AWS Command Line Interface
(AWS CLI) to update a specified sync configuration.

You can update the following information for your sync configuration:

- `--branch`
- `--config-file`
- `--repository-link-id`
- `--resource-name`
- `--role-arn`

###### To update a sync configuration

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **update-sync-configuration** command, specifying the value you
   want to update, along with the resource name and sync type. For example, the
   following command updates the branch name associated to the sync configuration with
   the `--branch` parameter.

```
aws codeconnections update-sync-configuration --sync-type CFN_STACK_SYNC --resource-name mystack --branch feature-branch
```

2. This command returns the following output.

```
{
    "SyncConfiguration": {
        "Branch": "feature-branch",
        "ConfigFile": "filename.yaml",
        "OwnerId": "`owner_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
        "RepositoryName": "MyRepo",
        "ResourceName": "mystack",
        "RoleArn": "arn:aws:iam::`account_id`:role/myrole",
        "SyncType": "CFN_STACK_SYNC"
    }
```
