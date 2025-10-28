# Delete your VPC

When you are finished with a VPC, you can delete it.

###### Requirement

Before you can delete a VPC, you must first terminate or delete any resources that created a
[requester-managed network interface](../../../AWSEC2/latest/UserGuide/requester-managed-eni.md "../../../AWSEC2/latest/UserGuide/requester-managed-eni.md")
in the VPC. For example, you must terminate your EC2 instances and delete your load balancers,
NAT gateways, transit gateway VPC attachments, and interface VPC endpoints.

###### Note

If you have created a [flow log](flow-logs.md "flow-logs.md") for the VPC you are deleting, note that flow logs for deleted VPCs are eventually automatically removed.

###### Contents

- [Delete a VPC using the console](#delete-vpc-console "#delete-vpc-console")
- [Delete a VPC using the command line](#delete-vpc-cli "#delete-vpc-cli")

## Delete a VPC using the console

If you delete a VPC using the Amazon VPC console, we also delete the following VPC components
for you:

- DHCP options
- Egress-only internet gateways
- Gateway endpoints
- Internet gateways
- Network ACLs
- Route tables
- Security groups
- Subnets

###### To delete your VPC using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Terminate all instances in the VPC. For more information, see [Terminate Your
   Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_.
3. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
4. In the navigation pane, choose **Your VPCs**.
5. Select the VPC to delete and choose **Actions**,
   **Delete VPC**.
6. If there are resources that you must delete or terminate before we can
   delete the VPC, we display them. Delete or terminate these resources and
   then try again. Otherwise, we display the resources that we will delete
   in addition to the VPC. Review the list and then proceed to the next
   step.
7. (Optional) If you have a Site-to-Site VPN connection, you can select the option
   to delete it. If you plan to use the customer gateway with another VPC,
   we recommend that you keep the Site-to-Site VPN connection and the gateways. Otherwise,
   you must configure your customer gateway device again after you create a
   new Site-to-Site VPN connection.
8. When prompted for confirmation, enter `delete` and
   then choose **Delete**.

## Delete a VPC using the command line

Before you can delete a VPC using the command line, you must terminate or delete any
resources that created a requester-managed network interface in the VPC. You must also
delete or detach all VPC resources that you created, such as subnets, security groups,
network ACLs, route tables, internet gateways, and egress-only internet gateways. You do
not need to delete the default security group, default route table, or default network
ACL.

The following procedure demonstrates the commands that you use to delete common VPC
resources and then to delete your VPC. You must use these commands in this order. If you
created additional VPC resources, you'll also need to use their corresponding delete
command before you can delete the VPC.

###### To delete a VPC by using the AWS CLI

1. Delete your security group by using the [delete-security-group](../../../cli/latest/reference/ec2/delete-security-group.md "../../../cli/latest/reference/ec2/delete-security-group.md") command.

```
aws ec2 delete-security-group --group-id `sg-id`
```

2. Delete each network ACL by using the [delete-network-acl](../../../cli/latest/reference/ec2/delete-network-acl.md "../../../cli/latest/reference/ec2/delete-network-acl.md") command.

```
aws ec2 delete-network-acl --network-acl-id `acl-id`
```

3. Delete each subnet by using the [delete-subnet](../../../cli/latest/reference/ec2/delete-subnet.md "../../../cli/latest/reference/ec2/delete-subnet.md") command.

```
aws ec2 delete-subnet --subnet-id `subnet-id`
```

4. Delete each custom route table by using the [delete-route-table](../../../cli/latest/reference/ec2/delete-route-table.md "../../../cli/latest/reference/ec2/delete-route-table.md")
   command.

```
aws ec2 delete-route-table --route-table-id `rtb-id`
```

5. Detach your internet gateway from your VPC by using the [detach-internet-gateway](../../../cli/latest/reference/ec2/detach-internet-gateway.md "../../../cli/latest/reference/ec2/detach-internet-gateway.md") command.

```
aws ec2 detach-internet-gateway --internet-gateway-id `igw-id` --vpc-id `vpc-id`
```

6. Delete your internet gateway by using the [delete-internet-gateway](../../../cli/latest/reference/ec2/delete-internet-gateway.md "../../../cli/latest/reference/ec2/delete-internet-gateway.md") command.

```
aws ec2 delete-internet-gateway --internet-gateway-id `igw-id`
```

7. [Dual stack VPC] Delete your egress-only internet gateway by using the [delete-egress-only-internet-gateway](../../../cli/latest/reference/ec2/delete-egress-only-internet-gateway.md "../../../cli/latest/reference/ec2/delete-egress-only-internet-gateway.md") command.

```
aws ec2 delete-egress-only-internet-gateway --egress-only-internet-gateway-id `eigw-id`
```

8. Delete your VPC by using the [delete-vpc](../../../cli/latest/reference/ec2/delete-vpc.md "../../../cli/latest/reference/ec2/delete-vpc.md") command.

```
aws ec2 delete-vpc --vpc-id `vpc-id`
```
