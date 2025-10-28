# View repository link details

You can use the **get-repository-link** command in the AWS Command Line Interface (AWS CLI) to
view details about a repository link.

###### To view repository link details

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **get-repository-link** command, specifying the repository link
   ID.

```
aws codestar-connections get-repository-link --repository-link-id 6053346f-8a33-4edb-9397-10394b695173
```

2. This command returns the following output.

```
{
    "RepositoryLinkInfo": {
        "ConnectionArn": "arn:aws:codestar-connections:us-east-1:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
        "OwnerId": "`owner_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkArn": "arn:aws:codestar-connections:us-east-1:`account_id`:repository-link/be8f2017-b016-4a77-87b4-608054f70e77",
        "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
        "RepositoryName": "MyRepo",
        "Tags": []
    }
}
```
