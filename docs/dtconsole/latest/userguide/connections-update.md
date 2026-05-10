# Update a pending connection

A connection created through the AWS Command Line Interface (AWS CLI) or AWS CloudFormation is in `PENDING`
status by default. After you create a connection with the AWS CLI or CloudFormation, use the console to
update the connection to make its status `AVAILABLE`.

###### Note

You must use the console to update a pending connection. You cannot update a pending
connection using the AWS CLI.

The first time you use the console to add a new connection to a third-party provider, you
must complete the OAuth handshake with the third-party provider using the installation
associated with your connection.

You can use the Developer Tools console to complete a pending connection.

###### To complete a connection

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").
2. Choose **Settings > Connections**.

The names of all connections associated with your AWS account are
displayed. 3. In **Name**, choose the name of the pending connection you want
to update.

**Update a pending connection** is enabled when you choose a
connection with a **Pending** status. 4. Choose **Update a pending connection**. 5. On the **Connect to Bitbucket** page, in **Connection
name**, verify the name of your connection.

Under **Bitbucket apps**, choose an app installation, or choose
**Install a new app** to create one.

![Console screenshot showing the Connect to Bitbucket dialog box, with the install new app button.](images/newreview-source-wizard-bitbucket.png) 6. On the app installation page, a message shows that the AWS CodeStar app is trying to
connect to your Bitbucket account. Choose **Grant access**.

![Console screenshot showing AWS CodeStar requests access.](/images/dtconsole/latest/userguide/images/bitbucket-access-popup.png) 7. The connection ID for your new installation is displayed. Choose
**Complete connection**.
