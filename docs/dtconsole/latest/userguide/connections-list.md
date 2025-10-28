# List connections

You can use the
Developer Tools console
or the **list-connections** command in the AWS Command Line Interface
(AWS CLI) to view a list of connections in your account.

## List connections (console)

###### To list connections

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose **Settings > Connections**.
3. View the name, status, and ARN for your connections.

## List connections (CLI)

You can use the AWS CLI to list your connections to third-party code repositories. For a
connection associated to a host resource, such as connections to GitHub Enteprise
Server, the output additionally returns the host ARN.

To do this, use the **list-connections** command.

###### To list connections

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows), and use the AWS CLI to
  run the **list-connections** command.

```
aws codeconnections list-connections --provider-type Bitbucket
--max-results 5 --next-token: `next-token`
```

This command returns the following output.

```
{
     "Connections": [
         {
             "ConnectionName": "my-connection",
             "ProviderType": "Bitbucket",
             "Status": "PENDING",
             "ARN": "arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
             "OwnerAccountId": "`account_id`"
         },
         {
             "ConnectionName": "my-other-connection",
             "ProviderType": "Bitbucket",
             "Status": "AVAILABLE",
             "ARN": "arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
             "OwnerAccountId": "`account_id`"
          },
      ],
     "NextToken": "`next-token`"
}
```
