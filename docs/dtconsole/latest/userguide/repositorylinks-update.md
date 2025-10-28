# Update a repository link

You can use the **update-repository-link** command in the AWS Command Line Interface (AWS CLI)
to update a specified repository link.

You can update the following information for your repository link:

- `--connection-arn`
- `--owner-id`
- `--repository-name`
  You might update a repository link when you want to change the connection that is
  associated with your repository. To use a different connection, you need to specify the
  connection ARN. For the steps to view your connection ARN, see [View connection details](connections-view-details.md "connections-view-details.md").

###### To update a repository link

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
   **update-repository-link** command, specifying the value to
   update for the repository link. For example, the following command updates the
   connection associated to the repository link ID. It specifies the new connection ARN
   with the `--connection` parameter.

```
aws codestar-connections update-repository-link --repository-link-id 6053346f-8a33-4edb-9397-10394b695173 --connection-arn arn:aws:codestar-connections:us-east-1:`account_id`:connection/aEXAMPLE-f055-4843-adef-4ceaefcb2167
```

2. This command returns the following output.

```
{
    "RepositoryLinkInfo": {
        "ConnectionArn": "arn:aws:codestar-connections:us-east-1:`account_id`:connection/aEXAMPLE-f055-4843-adef-4ceaefcb2167",
        "OwnerId": "`owner_id`",
        "ProviderType": "GitHub",
        "RepositoryLinkArn": "arn:aws:codestar-connections:us-east-1:`account_id`:repository-link/6053346f-8a33-4edb-9397-10394b695173",
        "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
        "RepositoryName": "MyRepo",
        "Tags": []
    }
}
```
