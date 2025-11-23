# Create a connection to GitHub

Enterprise Server (CLI)

You can use the AWS Command Line Interface (AWS CLI) to create a connection.

To do this, use the **create-host** and the
**create-connection** commands.

###### Important

A connection created through the AWS CLI or AWS CloudFormation is in `PENDING`
status by default. After you create a connection with the CLI or CloudFormation, use the
console to edit the connection to make its status `AVAILABLE`.

###### Step 1: To create a host for GitHub Enterprise Server (CLI)

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
   the **create-host** command, specifying the `--name`,
   `--provider-type`, and `--provider-endpoint` for your
   connection. In this example, the third-party provider name is
   `GitHubEnterpriseServer` and the endpoint is
   `my-instance.dev`.

```
aws codeconnections create-host --name MyHost --provider-type GitHubEnterpriseServer --provider-endpoint "https://my-instance.dev"
```

If successful, this command returns the host Amazon Resource Name (ARN)
information similar to the following.

```
{
    "HostArn": "arn:aws:codeconnections:us-west-2:`account_id`:host/My-Host-28aef605"
}
```

After this step, the host is in `PENDING` status. 2. Use the console to complete the host setup and move the host to an
`Available` status. For more information, see [Set up a pending host](connections-host-setup.md "connections-host-setup.md").

###### Step 2: To set up a pending host in the console

1. Sign in to the AWS Management Console and open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Use the console to complete the host setup and move the host to an
   `Available` status. See [Set up a pending host](connections-host-setup.md "connections-host-setup.md").

###### Step 3: To create a connection for GitHub Enterprise Server (CLI)

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
   the **create-connection** command, specifying the
   `--host-arn` and `--connection-name` for your
   connection.

```
aws codeconnections create-connection --host-arn arn:aws:codeconnections:us-west-2:`account_id`:host/MyHost-234EXAMPLE --connection-name MyConnection
```

If successful, this command returns the connection ARN information similar to
the following.

```
{
    "ConnectionArn": "arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad"
}
```

2. Use the console to set up the pending connection. For more information, see
   [Update a pending connection](connections-update.md "connections-update.md").

###### Step 4: To complete a connection for GitHub Enterprise Server in the

console

1. Sign in to the AWS Management Console and open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Use the console to set up the pending connection and move the connection to an
   `Available` status. For more information, see [Update a pending connection](connections-update.md "connections-update.md").
