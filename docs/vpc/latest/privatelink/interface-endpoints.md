

# Configure an interface endpoint
<a name="interface-endpoints"></a>

After you create an interface VPC endpoint, you can update its configuration.

**Topics**
+ [Add or remove subnets](#add-remove-subnets)
+ [Associate security groups](#associate-security-groups)
+ [Edit the VPC endpoint policy](#edit-vpc-endpoint-policy)
+ [Enable private DNS names](#enable-private-dns-names)
+ [Manage tags](#add-remove-interface-endpoint-tags)

## Add or remove subnets
<a name="add-remove-subnets"></a>

You can choose one subnet per Availability Zone for your interface endpoint. If you add a subnet, we create an endpoint network interface in the subnet and assign it a private IP address from the IP address range of the subnet. If you remove a subnet, we delete its endpoint network interface. For more information, see [Subnets and Availability Zones](privatelink-access-aws-services.md#aws-service-subnets-zones).

**To change the subnets using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Manage subnets**.

1. Select or deselect Availability Zones as needed. For each Availability Zone, select one subnet. By default, we select IP addresses from the subnet IP address ranges and assign them to the endpoint network interfaces. To choose the IP addresses for an endpoint network interface, select **Designate IP addresses** and enter an IPv4 address from the subnet address range. If the endpoint service supports IPv6, you can also enter an IPv6 address from the subnet address range.

   If you specify an IP address for a subnet that already has an endpoint network interface for this VPC endpoint, we replace the endpoint network interface with a new one. This processes temporarily disconnects the subnet and the VPC endpoint.

1. Choose **Modify subnets**.

**To change the subnets using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Associate security groups
<a name="associate-security-groups"></a>

You can change the security groups that are associated with the network interfaces for your interface endpoint. The security group rules control the traffic that is allowed to the endpoint network interface from the resources in your VPC.

**To change the security groups using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Manage security groups**.

1. Select or deselect security groups as needed.

1. Choose **Modify security groups**.

**To change the security groups using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Edit the VPC endpoint policy
<a name="edit-vpc-endpoint-policy"></a>

If the AWS service supports endpoint policies you can edit the endpoint policy for the endpoint. After you update an endpoint policy, it can take a few minutes for the changes to take effect. For more information, see [Endpoint policies](vpc-endpoints-access.md).

**To change the endpoint policy using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Manage policy**.

1. Choose **Full Access** to allow full access to the service, or choose **Custom** and attach a custom policy.

1. Choose **Save**.

**To change the endpoint policy using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Enable private DNS names
<a name="enable-private-dns-names"></a>

We recommend that you enable private DNS names for your VPC endpoints for AWS services. This ensures that requests that use the public service endpoints, such as requests made through an AWS SDK, resolve to your VPC endpoint.

To use private DNS names, you must enable both [DNS hostnames and DNS resolution](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) for your VPC. After you enable private DNS names, it might take a few minutes for the private IP addresses to become available. The DNS records that we create when you enable private DNS names are private. Therefore, the private DNS name is not publicly resolvable.

**To change the private DNS names option using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Modify private DNS name**.

1. Select or clear **Enable for this endpoint** as required.

1. If the service is Amazon S3, selecting **Enable for this endpoint** in the previous step also selects **Enable private DNS only for inbound endpoint**. If you prefer the standard private DNS functionality, clear **Enable private DNS only for inbound endpoint**. If you do not have a gateway endpoint for Amazon S3 in addition to an interface endpoint for Amazon S3, and you select **Enable private DNS only for inbound endpoint**, you'll receive an error when you save changes in the next step. For more information, see [Private DNS](vpc-endpoints-s3.md#private-dns-s3).

1. Choose **Save changes**.

**To change the private DNS names option using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Manage tags
<a name="add-remove-interface-endpoint-tags"></a>

You can tag your interface endpoint to help you identify it or categorize it according to your organization's needs.

**To manage tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Manage tags**.

1. For each tag to add choose **Add new tag** and enter the tag key and tag value.

1. To remove a tag, choose **Remove** to the right of the tag key and value.

1. Choose **Save**.

**To manage tags using the command line**
+ [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) (AWS CLI)
+ [New-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Tag.html) and [Remove-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Tag.html) (Tools for Windows PowerShell)