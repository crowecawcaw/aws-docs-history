# Managing servers

In this section, you can find information on how to view a list of your servers, how to
view your server details, how to edit your server details, and how to change the host key
for your SFTP-enabled server.

###### Topics

- [View a list of servers](#configuring-servers-view-server-list "#configuring-servers-view-server-list")
- [Delete a server](#delete-server "#delete-server")
- [View SFTP, FTPS, and FTP server
  details](configuring-servers-view-info.md "configuring-servers-view-info.md")
- [View AS2 server details](view-as2-server-details.md "view-as2-server-details.md")
- [IPv6 support for Transfer Family servers](ipv6-support.md "ipv6-support.md")
- [Edit server details](edit-server-config.md "edit-server-config.md")
- [Edit identity provider
  configuration](configuring-servers-edit-custom-idp.md "configuring-servers-edit-custom-idp.md")
- [Manage host keys for your SFTP-enabled
  server](configuring-servers-change-host-key.md "configuring-servers-change-host-key.md")
- [Monitoring usage in the console](monitor-usage-transfer-console.md "monitor-usage-transfer-console.md")

## View a list of servers

On the AWS Transfer Family console, you can find a list of all your servers that are located in
the AWS Region that you chose.

###### To find a list of your servers that exist in an AWS Region

- Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").

If you have one or more servers in the current AWS Region, the console opens
to show a list of your servers. If you don't see a list of servers, make
sure that you are in the correct Region. You can also choose
**Servers** from the navigation pane.

For more information about viewing your server details, see [View SFTP, FTPS, and FTP server
details](configuring-servers-view-info.md "configuring-servers-view-info.md").

## Delete a server

This procedure explains how to delete a Transfer Family server by using the AWS Transfer Family console or
AWS CLI.

###### Important

You are billed, for each of the protocols enabled to access your endpoint, until
you delete the server.

###### Warning

Deleting a server results in all its users being deleted. Data in the bucket that
was accessed by using the server is not deleted, and remains accessible to AWS
users that have privileges to those Amazon S3 buckets.

Console

###### To delete a server by using the console

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose
   **Servers**.
3. Select the check box of the server that you want to delete.
4. For **Actions**, choose
   **Delete**.
5. In the confirmation dialog box that appears, enter the word
   `delete`, and then choose **Delete** to
   confirm that you want to delete the server.

The server is deleted from the **Servers** page and you
are no longer billed for it.

AWS CLI

###### To delete a server by using the CLI

1. (Optional) Run the following command to view the details for the
   server that you want to delete permanently.

```
aws transfer describe-server --server-id `your-server-id`
```

This `describe-server` command returns all of the
details for your server. 2. Run the following command to delete the server.

```
aws transfer delete-server --server-id `your-server-id`
```

If successful, the command deletes the server and does not return any
information.
