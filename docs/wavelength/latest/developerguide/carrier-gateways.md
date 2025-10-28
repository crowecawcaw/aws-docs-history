# Carrier gateway for AWS Wavelength

A carrier gateway serves two purposes. It allows inbound traffic from a carrier network in a
specific location, and it allows outbound traffic to the carrier network and the internet. There
is generally no inbound connection configuration from the internet to a Wavelength Zone through
the carrier gateway with the exception of select partners. For more information,
see [Multi-access AWS Wavelength](multi-access.md "multi-access.md").

A carrier gateway supports IPv4 traffic.

Carrier gateways are only available for VPCs that contain subnets in a Wavelength Zone. The
carrier gateway provides connectivity between your Wavelength Zone and the carrier, and devices on
the carrier network. The carrier gateway performs NAT of the Wavelength instances' IP addresses to
the Carrier IP addresses from a pool that is assigned to the network border group. The carrier
gateway NAT function is similar to how an internet gateway functions in a Region.

## Enable access to the carrier network

To enable access to or from the carrier network for instances in a Wavelength subnet, you must
do the following:

- Create a VPC.
- Create a carrier gateway and attach the carrier gateway to your VPC. When you create
  the carrier gateway, you can optionally choose which subnets route to the carrier gateway.
  When you select this option, we automatically create the resources related to carrier
  gateways, such as route tables and network ACLs. If you do not choose this option, then
  you must perform the following tasks:
  - Select the subnets that route traffic to the carrier gateway.
  - Ensure that your subnet route tables have a route that directs traffic to the
    carrier gateway.
  - Ensure that instances in your subnet have a globally unique Carrier IP
    address.
  - Ensure that your network access control lists and security group rules allow the
    relevant traffic to flow to and from your instance.

## Work with carrier gateways

The following sections describe how to manually create a carrier gateway for your VPC to
support inbound traffic from the carrier network (for example, mobile phones), and to support
outbound traffic to the carrier network and the internet.

###### Tasks

- [Create a VPC](#Add_CGW_Create_VPC "#Add_CGW_Create_VPC")
- [Create a carrier gateway](#Add_CGW_create_Gateway "#Add_CGW_create_Gateway")
- [Create a security group to access the carrier
  network](#Add_CGW_Security_Groups "#Add_CGW_Security_Groups")
- [Allocate and associate a Carrier IP address
  with the instance in the Wavelength Zone subnet](#wavelength-allocate-carrier-ip "#wavelength-allocate-carrier-ip")
- [Routing to a Wavelength Zone carrier gateway](#route-tables-cgw "#route-tables-cgw")
- [View the carrier gateway details](#view-cgw "#view-cgw")
- [Manage carrier gateway tags](#manage-cgw-tags "#manage-cgw-tags")
- [Delete a carrier gateway](#delete-cgw "#delete-cgw")

### Create a VPC

You can create an empty Wavelength VPC as follows.

###### Limitation

You can specify a range of publicly routable IPv4 addresses. However, we do not
support direct access to the internet from publicly routable CIDR blocks in a VPC. Windows
instances cannot boot correctly if launched into a VPC with ranges from
`224.0.0.0` to `255.255.255.255` (Class D and Class E IP address
ranges).

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**, **Create
   VPC**.
3. Do the following and then choose **Create**.
   - **Name tag**: Optionally provide a name for your VPC. Doing so
     creates a tag with a key of `Name` and the value that you specify.
   - **IPv4 CIDR block**: Specify an IPv4 CIDR block for the VPC. We
     recommend that you specify a CIDR block from the private (non-publicly routable) IP
     address ranges as specified in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html "http://www.faqs.org/rfcs/rfc1918.html"); for example, `10.0.0.0/16`, or
     `192.168.0.0/16`.

###### To create a VPC using the AWS CLI

Use the [create-vpc](../../../cli/latest/reference/ec2/create-vpc.md "../../../cli/latest/reference/ec2/create-vpc.md")
command.

### Create a carrier gateway

After you create a VPC, create a carrier gateway and then select the subnets that route
traffic to the carrier gateway.

If you have not opted in to a Wavelength Zone, the Amazon Virtual Private Cloud Console prompts you to
opt in. For more information, see [Manage Zones](#manage-zones "#manage-zones").

When you choose to automatically route traffic from subnets to the carrier gateway, we
create the following resources:

- A carrier gateway
- A subnet. You can optionally assign all carrier gateway tags that do not have a
  **Key** value of `Name` to the subnet.
- A network ACL with the following resources:
  - A subnet associated with the subnet in the Wavelength Zone
  - Default inbound and outbound rules for all of your traffic.

- A route table with the following resources:
  - A route for all local traffic
  - A route that routes all non-local traffic to the carrier gateway
  - An association with the subnet

###### To create a carrier gateway

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Carrier Gateways**, and then
   choose **Create carrier gateway**.
3. Optional: For **Name**, enter a name for the carrier
   gateway.
4. For **VPC**, choose the VPC.
5. Choose **Route subnet traffic to carrier gateway**, and under
   **Subnets to route** do the following.
   1. Under **Existing subnets in Wavelength Zone**, select the box for
      each subnet to route to the carrier gateway.
   2. To create a subnet in the Wavelength Zone, choose **Add new
      subnet**, specify the following information, and then choose
      **Add new subnet**:
      - **Name tag**: Optionally provide a name for
        your subnet. Doing so creates a tag with a key of `Name` and the
        value that you specify.
      - **VPC**: Choose the VPC.
      - **Availability Zone**: Choose the Wavelength Zone.
      - **IPv4 CIDR block**: Specify an IPv4 CIDR block
        for your subnet, for example, `10.0.1.0/24`.
      - To apply the carrier gateway tags to the subnet, select **Apply same
        tags from this carrier gateway**.

6. (Optional) To add a tag to the carrier gateway, choose **Add tag**,
   and then do the following:
   - For **Key**, enter the key name.
   - For **Value**, enter the key value.

7. Choose **Create carrier gateway**.

###### To create a carrier gateway using the AWS CLI

1.  Use the [create-carrier-gateway](../../../cli/latest/reference/ec2/create-carrier-gateway.md "../../../cli/latest/reference/ec2/create-carrier-gateway.md") command.
2.  Add a VPC route table with the following resources:

        * A route for all VPC local traffic
        * A route that routes all non-local traffic to the carrier gateway
        * An association with the subnets in the Wavelength Zone

    For more information, see [Routing to a Wavelength Zone carrier gateway](#route-tables-cgw "#route-tables-cgw").

### Create a security group to access the carrier

network

By default, a VPC security group allows all outbound traffic. You can create a new
security group and add rules that allow inbound traffic from the carrier. Then, you
associate the security group with instances in the subnet.

###### To create a new security group and associate it with your instances

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security Groups**, and then choose
   **Create Security Group**.
3. To create a security group, choose **Create security group**,
   specify the following information, and then choose **create**:
   - **Security group name**: Enter a name for the
     subnet.
   - **Description**: Enter the security group description.
   - **VPC**: Choose the VPC.

4. Select the security group. The details pane displays the details for the security
   group, plus tabs for working with its inbound rules and outbound rules.
5. On the **Inbound Rules** tab, choose **Edit**.
   Choose **Add Rule**, and complete the required information. For
   example, select **HTTP** or **HTTPS** from the
   **Type** list, and enter the **Source** as
   `0.0.0.0/0` for IPv4 traffic, or `::/0` for IPv6 traffic. Choose
   **Save**.
6. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
7. In the navigation pane, choose **Instances**.
8. Select the instance, choose **Actions**,
   **Networking**, and then select **Change Security
   Groups**.
9. Clear the check box for the currently selected security group, and then select the
   new one. Choose **Assign Security Groups**.

###### To create a security group using the AWS CLI

Use the [create-security-group](../../../cli/latest/reference/ec2/create-security-group.md "../../../cli/latest/reference/ec2/create-security-group.md") command.

### Allocate and associate a Carrier IP address

with the instance in the Wavelength Zone subnet

If you used the Amazon EC2 console to launch the instance, or you did not use the
`associate-carrier-ip-address` option in the AWS CLI, then you must allocate a
Carrier IP address and assign it to the instance:

###### To allocate and associate a Carrier IP address using the AWS CLI

1. Use the [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md") command as follows.

```
aws ec2 allocate-address --region us-east-1 --domain vpc --network-border-group us-east-1-wl1-bos-wlz-1
```

The following is example output:

```
{
    "AllocationId": "eipalloc-05807b62acEXAMPLE",
    "PublicIpv4Pool": "amazon",
    "NetworkBorderGroup": "us-east-1-wl1-bos-wlz-1",
    "Domain": "vpc",
    "CarrierIp": "155.146.10.111"

}
```

2. Use the [associate-address](../../../cli/latest/reference/ec2/associate-address.md "../../../cli/latest/reference/ec2/associate-address.md") command to associate the Carrier IP address with the EC2
   instance as follows.

```
aws ec2 associate-address --allocation-id eipalloc-05807b62acEXAMPLE --network-interface-id eni-1a2b3c4d
```

The following is example output:

```
{
    "AssociationId": "eipassoc-02463d08ceEXAMPLE",
}
```

### Routing to a Wavelength Zone carrier gateway

Subnets that are in Wavelength Zones can have an additional target type of a carrier
gateway. Consider the case where you want to have the carrier gateway route traffic to route
all non-VPC traffic to the carrier network. To do this, create and attach a carrier gateway
to your VPC, and then add the following routes:

| Destination | Target    |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0.0.0.0/0   | `cagw-id` |
| ::/0        | `cagw-id` | ### View the carrier gateway details You can view information about your carrier gateway, including the state and the tags. ###### To view the carrier gateway details 1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 2. In the navigation pane, choose **Carrier Gateways**. 3. Select the carrier gateway and choose **Actions**, **View details**. ###### To view the carrier gateway details using the AWS CLI Use the [describe-carrier-gateways](../../../cli/latest/reference/ec2/describe-carrier-gateways.md "../../../cli/latest/reference/ec2/describe-carrier-gateways.md") command. ### Manage carrier gateway tags Tags help you to identify your carrier gateways. You can add or remove tags. ###### To manage the carrier gateway tags 1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 2. In the navigation pane, choose **Carrier Gateways**. 3. Select the carrier gateway and choose **Actions**, **Manage tags**. 4. To add a tag, choose **Add tag**, and then do the following: <br>• For **Key**, enter the key name. <br>• For **Value**, enter the key value. 5. To remove a tag, choose **Remove** to the right of the tag’s Key and Value. 6. Choose **Save**. ###### To manage the carrier gateway tags using the AWS CLI <br>• To add tags, use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command. <br>• To delete tags, use the [delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md") command. ### Delete a carrier gateway If you no longer need a carrier gateway, you can delete it. ###### Important If you do not delete the route that has the carrier gateway as the **Target**, the route is a blackhole route. ###### To delete a carrier gateway 1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). 2. In the navigation pane, choose **Carrier Gateways**. 3. Select the carrier gateway and choose **Actions**, **Delete carrier gateway**. 4. In the **Delete carrier gateway** dialog box, enter **Delete**, and then choose **Delete**. ###### To delete a carrier gateway using the AWS CLI Use the [delete-carrier-gateway](../../../cli/latest/reference/ec2/delete-carrier-gateway.md "../../../cli/latest/reference/ec2/delete-carrier-gateway.md") command. ## Manage Zones Before you specify a Wavelength Zone for a resource or service, you must opt in to the AWS Zone. |
