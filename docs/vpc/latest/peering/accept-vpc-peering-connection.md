# Accept or reject a VPC peering connection

A VPC peering connection that's in the `pending-acceptance` state must be
accepted by the owner of the accepter VPC to be activated. For more information about
the `Deleted` peering connection status, see [VPC peering connection lifecycle](vpc-peering-basics.md#vpc-peering-lifecycle "vpc-peering-basics.md#vpc-peering-lifecycle"). You can't
accept a VPC peering connection request that you sent to another AWS account. To
create a VPC peering connection between VPCs in the same AWS account, you can both
create and accept the request yourself.

You can reject any VPC peering connection request that you've received that's
in the `pending-acceptance` state. You should only accept VPC peering
connections from AWS accounts that you know and trust; you can reject any unwanted
requests. For more information about the `Rejected` peering connection status,
see [VPC peering connection lifecycle](vpc-peering-basics.md#vpc-peering-lifecycle "vpc-peering-basics.md#vpc-peering-lifecycle").

###### Important

Do not accept VPC peering connections from unknown AWS accounts. A malicious user may have
sent you a VPC peering connection request to gain unauthorized network access to
your VPC. This is known as peer phishing. You can safely reject unwanted VPC
peering connection requests without any risk of the requester gaining access to
any information about your AWS account or your VPC. For more information, see
Accept or reject a VPC peering connection. You can also ignore the
request and let it expire; by default, requests expire after 7 days.

###### To accept or reject a peering connection using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Use the Region selector to choose the Region of the accepter VPC.
3. In the navigation pane, choose **Peering connections**.
4. To reject a peering connection, select the VPC peering connection, and choose **Actions**,
   **Reject request**. When prompted for confirmation, choose **Reject request**.
5. To accept a peering connection, select the pending VPC peering connection (the status is
   `pending-acceptance`), and choose
   **Actions**, **Accept request**.
   For more information about peering connection lifecycle statuses, see [VPC peering connection lifecycle](vpc-peering-basics.md#vpc-peering-lifecycle "vpc-peering-basics.md#vpc-peering-lifecycle").

If there is no pending VPC peering connection, verify that you selected the
Region of the accepter VPC. 6. When prompted for confirmation, choose **Accept request**. 7. Choose **Modify my route tables now** to add a route to the
VPC route table so that you can send and receive traffic across the peering
connection. For more information, see [Update your route tables for a VPC peering connection](vpc-peering-routing.md "vpc-peering-routing.md").

###### To accept a peering connection using the command line

- [accept-vpc-peering-connection](../../../cli/latest/reference/ec2/accept-vpc-peering-connection.md "../../../cli/latest/reference/ec2/accept-vpc-peering-connection.md") (AWS CLI)
- [Approve-EC2VpcPeeringConnection](../../../powershell/latest/reference/items/Approve-EC2VpcPeeringConnection.md "../../../powershell/latest/reference/items/Approve-EC2VpcPeeringConnection.md") (AWS Tools for Windows PowerShell)

###### To reject a peering connection using the command line

- [reject-vpc-peering-connection](../../../cli/latest/reference/ec2/reject-vpc-peering-connection.md "../../../cli/latest/reference/ec2/reject-vpc-peering-connection.md") (AWS CLI)
- [Deny-EC2VpcPeeringConnection](../../../powershell/latest/reference/items/Deny-EC2VpcPeeringConnection.md "../../../powershell/latest/reference/items/Deny-EC2VpcPeeringConnection.md") (AWS Tools for Windows PowerShell)
