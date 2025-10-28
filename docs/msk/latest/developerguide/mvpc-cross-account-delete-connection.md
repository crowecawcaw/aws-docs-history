# Delete a managed VPC connection to an Amazon MSK cluster

The cross-account user can delete a managed VPC connection for an MSK cluster
from the client account console. Because the cluster owner user doesn’t own the
managed VPC connection, the connection can’t be deleted from the cluster admin
account. Once a VPC connection is deleted, it no longer incurs cost.

###### To delete a managed VPC connection using the MSK console

1. From the client account, open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk "https://console.aws.amazon.com/msk").
2. In the navigation pane, select **Managed VPC connections**.
3. From the connection list, select the connection that you want to delete.
4. Confirm that you want to delete the VPC connection.
   To delete a managed VPC connection using the API, use the `DeleteVpcConnection` API.
