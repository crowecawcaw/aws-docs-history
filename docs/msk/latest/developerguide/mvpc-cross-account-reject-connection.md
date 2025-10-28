# Reject a managed VPC connection to an Amazon MSK cluster

From the Amazon MSK console on the cluster admin account, you can reject a client
VPC connection. The client VPC connection must be in the AVAILABLE state to be
rejected. You might want to reject a managed VPC connection from a client that
is no longer authorized to connect to your cluster. To prevent new managed VPC
connections from a connecting to a client, deny access to the client in the
cluster policy. A rejected connection still incurs cost until its deleted by the
connection owner. See [Delete a managed VPC connection to an Amazon MSK cluster](mvpc-cross-account-delete-connection.md "mvpc-cross-account-delete-connection.md") .

###### To reject a client VPC connection using the MSK console

1. Open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk "https://console.aws.amazon.com/msk").
2. In the navigation pane, select **Clusters** and scroll to the **Network settings > Client VPC connections** list.
3. Select the connection that you want to reject and select **Reject client VPC
   connection**.
4. Confirm that you want to reject the selected client VPC connection.
   To reject a managed VPC connection using the API, use the `RejectClientVpcConnection` API.
