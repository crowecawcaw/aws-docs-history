# View public IP insights

You can use **Public IP insights** to see the following:

- If your IPAM is [integrated with accounts in an
  AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md"), you can view all public IPv4 addresses used by
  services across all AWS Regions for your entire AWS Organization.
- If your IPAM is [integrated with a single
  account](enable-single-user-ipam.md "enable-single-user-ipam.md"), you can view all public IPv4 addresses used by services across
  all AWS Regions in your account.
  A public IPv4 address is an IPv4 address that is routable from the internet. A public IPv4
  address is necessary for a resource to be directly reachable from the internet over
  IPv4.

###### Note

AWS charges for all public IPv4 addresses, including public IPv4 addresses
associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

You can view insights into the following public IPv4 address types:

- **Elastic IP addresses (EIPs)**: Static, public IPv4 addresses
  provided by Amazon that you can associate with an EC2 instance, elastic network
  interface, or AWS resource.
- **EC2 public IPv4 addresses**: Public IPv4 addresses assigned to
  an EC2 instance by Amazon (if the EC2 instance is launched into a default subnet or
  if the instance is launched into a subnet that’s been configured to automatically
  assign a public IPv4 address).
- **BYOIPv4 addresses**: Public IPv4 addresses in the IPv4 address
  range that you’ve brought to AWS using [Bring your own IP addresses (BYOIP)](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md").
- **Service-managed IPv4 addresses**: Public IPv4 addresses
  automatically provisioned on AWS resources and managed by an AWS service. For
  example, public IPv4 addresses on Amazon ECS, Amazon RDS, or Amazon WorkSpaces.
  Public IP insights shows you all public IPv4 addresses used by services across Regions. You can use these insights to identify public IPv4 address usage and view recommendations to release unused Elastic IP addresses.

- **Public IP types**: The number of public IPv4 addresses organized by type.
  - **Amazon-owned EIPs**: Elastic IP addresses that you have provisioned or assigned to resources in your AWS account.
  - **EC2 public IPs**: Public IPv4 addresses assigned to EC2 instances when the instances were launched into a default subnet or into a subnet that’s been configured to automatically assign a public IPv4 address.
  - **BYOIP**: Public IPv4 addresses that you have brought to AWS using Bring your own IP addresses (BYOIP).
  - **Service managed IPs**: Public IPv4 addresses provisioned and managed by an AWS service.
  - **Service managed BYOIP**: Public IPv4 addresses brought to AWS and managed by an AWS service.
  - **Amazon-owned contiguous EIPs**: Elastic IP addresses allocated from an Amazon-provided contiguous public IPv4 IPAM pool.

- **EIP usage**: The number of Elastic IP addresses organized by how they are used.
  - **Associated Amazon-owned EIPs**: Elastic IP addresses that you have provisioned in your AWS account and that you have associated with an EC2 instance, network interface, or AWS resource.
  - **Associated BYOIP**: Public IPv4 addresses you have brought to AWS using BYOIP that you have associated with a network interface.
  - **Unassociated Amazon-owned EIPs**: Elastic IP addresses that you have provisioned in your AWS account but you have not associated with a network interface.
  - **Unassociated BYOIP**: Public IPv4 addresses you have brought to AWS using BYOIP but you have not associated with a network interface.
  - **Associated Amazon-owned contiguous EIPs**: Elastic IP addresses allocated from an Amazon-provided contiguous public IPv4 IPAM pool and associated with a resource.
  - **Unassociated Amazon-owned contiguous EIPs**: Elastic IP addresses allocated from an Amazon-provided contiguous public IPv4 IPAM pool and unassociated with a resource.

- **Amazon-owned IPv4 contiguous IPs usage**: A table that shows contiguous public IPv4 address usage over time and related Amazon-owned IPv4 IPAM pools.
- **Public IP addresses**: A table of public IPv4 addresses and their attributes.

      + **IP address**: The public IPv4 address.
      + **Associated**: Whether or not the address is associated with an EC2 instance, network interface, or AWS resource.




      	- **Associated**: The public IPv4 address is associated with an EC2 instance, network interface, or AWS resource.
      	- **Unassociated**: The public IPv4 address is not associated to any resource and is idle in your AWS account.
      + **Address type**: The IP address type.




      	- **Amazon-owned EIP**: The public IPv4 address is an Elastic IP address.
      	- **BYOIP**: The public IPv4 address was brought to AWS using BYOIP.
      	- **EC2 public IP**: The public IPv4 address was assigned automatically to an EC2 instance.
      	- **Service managed BYOIP**: The public IPv4 address was brought to AWS using Bring your own IP (BYOIP).
      	- **Service managed IP**: The public IPv4 address was provisioned and is managed by an AWS service.
      + **Service**: The service that the IP address is associated with.




      	- **AGA**: An AWS Global Accelerator. If a [custom routing accelerator](../../../global-accelerator/latest/dg/work-with-custom-routing-accelerators.md "../../../global-accelerator/latest/dg/work-with-custom-routing-accelerators.md") is used, its public IPs are not listed. To view these public IPs, see [Viewing your custom routing accelerators](../../../global-accelerator/latest/dg/about-custom-routing-accelerators.md#about-custom-routing-accelerators.viewing "../../../global-accelerator/latest/dg/about-custom-routing-accelerators.md#about-custom-routing-accelerators.viewing").
      	- **Database Migration Service**: An AWS Database Migration Service (DMS) replication instance.
      	- **Redshift**: An Amazon Redshift cluster.
      	- **RDS**: An Amazon Relational Database Service (RDS) instance.
      	- **Load balancer (EC2)**: An Application Load Balancer or a Network Load Balancer.
      	- **NAT gateway (VPC)**: An Amazon VPC public NAT gateway.
      	- **Site-to-Site VPN**: An AWS Site-to-Site VPN virtual private gateway.
      	- **Other**: Other service that is not currently identifiable.
      + **Name (EIP ID)**: If this public IPv4 address is an Elastic IP address allocation, this is the name and ID of the EIP allocation.
      + **Network interface ID**: If this public IPv4 address is associated with a network interface, this is the ID of the network interface.
      + **Instance ID**: If this public IPv4 address is associated with an EC2 instance, this is the instance ID.
      + **Security groups**: If this public IPv4 address is associated with an EC2 instance, this is the name and ID of the security group assigned to the instance.
      + **Public IPv4 pool**: If this is an Elastic IP address from an IP address pool owned and managed by Amazon, the value is "-". If this is an Elastic IP address from an IP address range which you own and have brought to Amazon (using BYOIP), the value is the public IPv4 pool ID.
      + **Network border group**: If the IP address is advertised, this is the AWS Region from which the IP address is advertised.
      + **Owner ID**:The AWS account number of resource owner.
      + **Sample time**: The last successful resource discovery time.
      + **Resource discovery ID**: ID of the resource discovery that has discovered this public IPv4 address.
      + **Service resource**: Resource ARN or ID.

  If an Elastic IP address is allocated to your account but is not associated with a network interface, a banner appears informing you that you have unassociated EIPs in your account and you should release them.

###### Important

Public IP insights was recently updated. If you see an error related to not having permissions to call GetIpamDiscoveredPublicAddresses, the managed permission attached to a resource discovery that was shared with you needs to be updated. Contact the person who created the resource discovery and ask them to update the managed permission `AWSRAMPermissionIpamResourceDiscovery` to the default version. For more information, see [Update a resource share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM User Guide_ .

AWS Management Console

###### To view public IP address insights

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Public IP insights**.
3. To view details for a public IP address, select an IP address by clicking on it.
4. View the following information about the IP address:
   - **Details**: The same information visible in the columns of the main Public IP insights pane, such as the **Address type** and **Service**.
   - **Inbound security group rules**: If this IP address is associated with an EC2 instance, these are the security group rules that control the inbound traffic to the instance.
   - **Outbound security group rules**: If this IP address is associated with an EC2 instance, these are the security group rules that control the outbound traffic from the instance.
   - **Tags**: Key and value pairs that act as metadata for organizing your AWS resources.

Command line
Use the following command to get the public IP addresses that have been
discovered by IPAM: [get-ipam-discovered-public-addresses](../../../cli/latest/reference/ec2/get-ipam-discovered-public-addresses.md "../../../cli/latest/reference/ec2/get-ipam-discovered-public-addresses.md")
