# Delete a host

You can use the Developer Tools console or the **delete-host** command in the AWS Command Line Interface
(AWS CLI) to delete a host.

###### Topics

- [Delete a host (console)](#connections-host-delete-console "#connections-host-delete-console")
- [Delete a host (CLI)](#connections-host-delete-cli "#connections-host-delete-cli")

## Delete a host (console)

###### To delete a host

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose the **Hosts** tab. In **Name**,
   choose the name of the host you want to delete.
3. Choose **Delete**.
4. Enter `delete` in the field to confirm, and then choose
   **Delete**.

###### Important

This action cannot be undone.

## Delete a host (CLI)

You can use the AWS Command Line Interface (AWS CLI) to delete a host.

To do this, use the **delete-host** command.

###### Important

Before you can delete a host, you must delete all connections associated with the
host.

After you run the command, the host is deleted. No confirmation dialog box is
displayed.

###### To delete a host

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **delete-host** command, specifying the Amazon Resource Name
  (ARN) of the host that you want to delete.

```
aws codeconnections delete-host --host-arn "arn:aws:codeconnections:us-west-2:`account_id`:host/My-Host-28aef605"
```

This command returns nothing.
