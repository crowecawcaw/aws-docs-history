# List sync configurations

You can use the **list-sync-configurations** command in the AWS Command Line Interface
(AWS CLI) to list repository links for your account.

###### To list repository links

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **list-sync-configurations** command, specifying the sync type
   and repository link ID.

```
aws codeconnections list-sync-configurations --repository-link-id 6053346f-8a33-4edb-9397-10394b695173  --sync-type CFN_STACK_SYNC
```

2. This command returns the following output.

```
{
    "SyncConfigurations": [
        {
            "Branch": "main",
            "ConfigFile": "filename.yaml",
            "OwnerId": "`owner_id`",
            "ProviderType": "GitHub",
            "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
            "RepositoryName": "MyRepo",
            "ResourceName": "mystack",
            "RoleArn": "arn:aws:iam::`account_id`:role/myrole",
            "SyncType": "CFN_STACK_SYNC"
        }
    ]
}
```
