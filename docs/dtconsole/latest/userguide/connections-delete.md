# Delete a connection

You can use the Developer Tools console or the **delete-connection** command in the
AWS Command Line Interface (AWS CLI) to delete a connection.

###### Topics

- [Delete a connection (console)](#connections-delete-console "#connections-delete-console")
- [Delete a connection (CLI)](#connections-delete-cli "#connections-delete-cli")

## Delete a connection (console)

###### To delete a connection

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose **Settings > Connections**.
3. In **Connection name**, choose the name of the connection you
   want to delete.
4. Choose **Delete**.
5. Enter `delete` in the field to confirm, and then choose
   **Delete**.

###### Important

This action cannot be undone.

## Delete a connection (CLI)

You can use the AWS Command Line Interface (AWS CLI) to delete a connection.

To do this, use the **delete-connection** command.

###### Important

After you run the command, the connection is deleted. No confirmation dialog box
is displayed. You can create a new connection, but the Amazon Resource Name (ARN) is
never reused.

###### To delete a connection

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **delete-connection** command, specifying the ARN of the
  connection that you want to delete.

```
aws codeconnections delete-connection --connection-arn arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f
```

This command returns nothing.
