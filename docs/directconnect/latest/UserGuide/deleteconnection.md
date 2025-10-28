# Delete an AWS Direct Connect connection

You can delete a connection as long as there are no virtual interfaces attached to it.
Deleting your connection stops all port hour charges for this connection, but you may
still incur cross-connect or network circuit charges (see below). AWS Direct Connectdata transfer
charges are associated with virtual interfaces. For more information about how to delete
a virtual interface, see [Delete a virtual interface](deletevif.md "deletevif.md").

Before deleting a connection, download the LOA for the connection containing the
cross-account information so you have the relevant information about the circuits being
disconnected. For the steps to download the connection LOA, see [Letter of Authorization and Connecting Facility
Assignment (LOA-CFA)](dedicated_connection.md#create-connection-loa-cfa "dedicated_connection.md#create-connection-loa-cfa").

When you delete a connection, AWS will instruct the colocation provider to
disconnect your network device from the Direct Connect router by removing the fiber-optic
cross-connect cable from the applicable AWS patch panel. However, your colocation or
circuit provider may still charge you cross-connect or network circuit charges because
the cross-connect cable may still be connected to your network device. These charges for
the cross-connect are independent of Direct Connect, and must be cancelled with the
colocation or circuit provider using information from the LOA.

If the connection is part of a link aggregation group (LAG), you cannot delete the
connection if doing so causes the LAG to fall below its setting for the minimum number
of operational connections.

You can delete a connection using either the AWS Direct Connect console or using the command line or API.

###### To delete a connection

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Connections**.
3. Select the connections and choose **Delete**.
4. In the **Delete confirmation** dialog box, choose
   **Delete**.

###### To delete a connection using the command line or API

- [delete-connection](../../../cli/latest/reference/directconnect/delete-connection.md "../../../cli/latest/reference/directconnect/delete-connection.md") (AWS CLI)
- [DeleteConnection](../APIReference/API_DeleteConnection.md "../APIReference/API_DeleteConnection.md") (AWS Direct Connect API)
