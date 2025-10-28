# View sync configuration details

You can use the **get-sync-configuration** command in the AWS Command Line Interface (AWS CLI)
to view details for a sync configuration.

###### To view details for a sync configuration

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **get-sync-configuration** command, specifying the repository
   link ID.

```
aws codeconnections get-sync-configuration --sync-type CFN_STACK_SYNC --resource-name mystack
```

2. This command returns the following output.

```
{
    "SyncConfiguration": {
        "Branch": "main",
        "ConfigFile": "filename",
        "OwnerId": "`owner_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkId": "be8f2017-b016-4a77-87b4-608054f70e77",
        "RepositoryName": "MyRepo",
        "ResourceName": "mystack",
        "RoleArn": "arn:aws:iam::`account_id`:role/myrole",
        "SyncType": "CFN_STACK_SYNC"
    }
}
```
