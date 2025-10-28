# View connection details

You can use the Developer Tools console or the **get-connection** command in the
AWS Command Line Interface (AWS CLI) to view details for a connection. To use the AWS CLI, you must have already
installed a recent version of the AWS CLI or updated to the current version. For more
information, see [Installing the AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in
the _AWS Command Line Interface User Guide_.

###### To view a connection (console)

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose **Settings > Connections**.
3. Choose the button next to the connection you want to view, and then choose
   **View details**.
4. The following information appears for your connection:
   - The connection name.
   - The provider type for your connection.
   - The connection status.
   - The connection ARN.
   - If the connection was created for an installed provider, such as GitHub
     Enterprise Server, the host information associated with the
     connection.
   - If the connection was created for an installed provider, such as GitHub
     Enterprise Server, the endpoint information associated with the host for the
     connection.

5. If the connection is in **Pending** status, to complete the
   connection, choose **Update pending connection**. For more
   information , see [Update a pending
   connection](connections-update.md "connections-update.md").

###### To view a connection (CLI)

- At the terminal or command line, run the **get-connection**
  command. For example, use the following command to view details for a connection
  with the
  `arn:aws:codestar-connections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`
  ARN value.

```
aws codeconnections get-connection --connection-arn arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f
```

If successful, this command returns the connections details.

Example output for a Bitbucket connection:

```
{
    "Connection": {
        "ConnectionName": "MyConnection",
        "ConnectionArn": "arn:aws:codeconnections:us-west-2:`account_id`:connection/cdacd948-EXAMPLE",
        "ProviderType": "Bitbucket",
        "OwnerAccountId": "`account_id`",
        "ConnectionStatus": "AVAILABLE"
    }
}
```

Example output for a GitHub connection:

```
{
    "Connection": {
        "ConnectionName": "MyGitHubConnection",
        "ConnectionArn": "arn:aws:codeconnections:us-west-2:`account_id`:connection/ebcd4a13-EXAMPLE",
        "ProviderType": "GitHub",
        "OwnerAccountId": "`account_id`",
        "ConnectionStatus": "AVAILABLE"
    }
}
```

Example output for a GitHub Enterprise Server connection:

```
{
    "Connection": {
        "ConnectionName": "MyConnection",
        "ConnectionArn": "arn:aws:codeconnections:us-west-2:`account_id`:connection/2d178fb9-EXAMPLE",
        "ProviderType": "GitHubEnterpriseServer",
        "OwnerAccountId": "`account_id`",
        "ConnectionStatus": "PENDING",
        "HostArn": "arn:aws:ccodeconnections:us-west-2:`account_id`:host/sdfsdf-EXAMPLE"
    }
}
```
