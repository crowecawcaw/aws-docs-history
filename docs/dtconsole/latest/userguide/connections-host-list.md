# List hosts

You can use the
Developer Tools console
or the **list-connections** command in the AWS Command Line Interface
(AWS CLI) to view a list of connections in your account.

## List hosts (console)

###### To list hosts

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose the **Hosts** tab. View the name, status, and ARN for
   your hosts.

## List hosts (CLI)

You can use the AWS CLI to list your hosts for installed third-party provider
connections.

To do this, use the **list-hosts** command.

###### To list hosts

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows), and use the AWS CLI to
  run the **list-hosts** command.

```
aws codeconnections list-hosts
```

This command returns the following output.

```
{
    "Hosts": [
        {
            "Name": "My-Host",
            "HostArn": "arn:aws:codeconnections:us-west-2:`account_id`:host/My-Host-28aef605",
            "ProviderType": "GitHubEnterpriseServer",
            "ProviderEndpoint": "https://my-instance.test.dev",
            "Status": "AVAILABLE"
        }
    ]
}

```
