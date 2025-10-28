# Create a repository link

You can use the **create-repository-link** command in the AWS Command Line Interface (AWS CLI)
to create a link between your connection and the external repository to sync to.

Before you can create a repository link, you must have already created your external
repository with your third-party provider, such as GitHub.

###### To create a repository link

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **create-repository-link** command. Specify the ARN of the
   associated connection, the owner ID, and the repository name.

```
aws codeconnections create-repository-link --connection-arn  arn:aws:codeconnections:us-east-1:`account_id`:connection/001f5be2-a661-46a4-b96b-4d277cac8b6e --owner-id `account_id` --repository-name MyRepo
```

2. This command returns the following output.

```
{
    "RepositoryLinkInfo": {
        "ConnectionArn": "arn:aws:codeconnections:us-east-1:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
        "OwnerId": "`account_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkArn": "arn:aws:codeconnections:us-east-1:`account_id`:repository-link/be8f2017-b016-4a77-87b4-608054f70e77",
        "RepositoryLinkId": "be8f2017-b016-4a77-87b4-608054f70e77",
        "RepositoryName": "MyRepo",
        "Tags": []
    }
}
```
