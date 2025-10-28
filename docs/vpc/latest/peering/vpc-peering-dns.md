# Enable DNS resolution for a VPC peering connection

The DNS settings for a VPC peering connection determine how public DNS hostnames are
resolved for requests that traverse the VPC peering connection. If an EC2 instance
on one side of a VPC peering connection sends a request to an EC2 instance on the other
side using the public IPv4 DNS hostname of the instance, the DNS hostname is resolved
as follows.

**DNS resolution disabled (default)**

The public IPv4 DNS hostname resolves to the public IPv4 address of the instance.

**DNS resolution enabled**

The public IPv4 DNS hostname resolves to the private IPv4 address of the instance.

###### Requirements

- Both VPCs must be enabled for DNS hostnames and DNS resolution. For more information,
  see [DNS attributes
  for your VPC](../userguide/AmazonDNS-concepts.md#vpc-dns-support "../userguide/AmazonDNS-concepts.md#vpc-dns-support") in the _Amazon VPC User Guide_.
- The peering connection must be in the `active` state. You can't enable
  DNS resolution when you create a peering connection.
- The owner of the requester VPC must modify the requester VPC peering options, and the
  owner of the accepter VPC must modify the accepter VPC peering options. If the
  VPCs are in the same account, you can enable DNS resolution for the requester
  and accepter VPCs at the same time. This works for both same-region and
  cross-region VPC peering connections.

###### To enable DNS resolution for a peering connection using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Peering connections**.
3. Select the VPC peering connection.
4. Choose **Actions**, **Edit DNS settings**.
5. To enable DNS resolution for requests from the requester VPC, select
   **Requester DNS resolution**,
   **Allow accepter VPC to resolve the DNS of requester VPC**.
6. To ensure DNS resolution for requests from the accepter VPC, select
   **Accepter DNS resolution**,
   **Allow requester VPC to resolve the DNS of accepter VPC**.
7. Choose **Save changes**.

###### To enable DNS resolution using the command line

- [modify-vpc-peering-connection-options](../../../cli/latest/reference/ec2/modify-vpc-peering-connection-options.md "../../../cli/latest/reference/ec2/modify-vpc-peering-connection-options.md") (AWS CLI)
- [Edit-EC2VpcPeeringConnectionOption](../../../powershell/latest/reference/items/Edit-EC2VpcPeeringConnectionOption.md "../../../powershell/latest/reference/items/Edit-EC2VpcPeeringConnectionOption.md") (AWS Tools for Windows PowerShell)

###### To describe VPC peering connection options using the command line

- [describe-vpc-peering-connections](../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md "../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md") (AWS CLI)
- [Get-EC2VpcPeeringConnection](../../../powershell/latest/reference/items/Get-EC2VpcPeeringConnection.md "../../../powershell/latest/reference/items/Get-EC2VpcPeeringConnection.md") (AWS Tools for Windows PowerShell)
