

# Requester-managed network interfaces
<a name="requester-managed-eni"></a>

A requester-managed network interface is a network interface that an AWS service creates in your VPC on your behalf. The network interface is associated with a resource for another service, such as a DB instance from Amazon RDS, a NAT gateway, or an interface VPC endpoint from AWS PrivateLink.

**Considerations**
+ You can view the requester-managed network interfaces in your account and you can add or remove tags. However, you can't perform the following actions on a requester-managed network interface:
  + Modify network interface attributes
  + Attach or detach the network interface
  + Associate or disassociate Elastic IP addresses
  + Assign or unassign private IP addresses
  + Specify the network interface when launching an instance

  You can still reset network interface attributes, even though you can't modify them.
+ When you delete the resource associated with a requester-managed network interface, the AWS service detaches the network interface and deletes it. If the service detached a network interface but didn't delete it, you can delete the detached network interface.

------
#### [ Console ]

**To view requester-managed network interfaces**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Network & Security**, **Network Interfaces**.

1. Select the ID of the network interface to open its details page.

1. The following are the key fields that you can use to determine the purpose of the network interface:
   + **Description**: A description provided by the AWS service that created the interface. For example, "VPC Endpoint Interface vpce 089f2123488812123".
   + **Requester-managed**: Indicates whether the network interface is managed by AWS.
   + **Requester ID**: The alias or AWS account ID of the principal or service that created the network interface. If you created the network interface, this is your AWS account ID. Otherwise, another principal or service created it.

------
#### [ AWS CLI ]

**To view requester-managed network interfaces**  
Use the [describe-network-interfaces](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-interfaces.html) command as follows.

```
aws ec2 describe-network-interfaces \
    --filters "Name=requester-managed,Values=true" \
    --query "NetworkInterfaces[*].[Description, InterfaceType]" \ 
    --output table
```

The following is example output that shows the key fields that you can use to determine the purpose of the network interface: `Description` and `InterfaceType`.

```
-------------------------------------------------------------------------------
|                          DescribeNetworkInterfaces                          |
+---------------------------------------------------+-------------------------+
|  VPC Endpoint Interface: vpce-0f00567fa8477a1e6   |  interface              |
|  VPC Endpoint Interface vpce-0d8ddce4be80e4474    |  interface              |
|  VPC Endpoint Interface vpce-078221a1e27d1ea5b    |  vpc_endpoint           |
|  Resource Gateway Interface rgw-0bba03f3d56060135 |  interface              |
|  VPC Endpoint Interface: vpce-0cc199f605eaeace7   |  interface              |
|  VPC Endpoint Interface vpce-019b90d6f16d4f958    |  interface              |
+---------------------------------------------------+-------------------------+
```

------
#### [ PowerShell ]

**To view requester-managed network interfaces**  
Use the [Get-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2NetworkInterface.html) cmdlet as follows.

```
Get-EC2NetworkInterface -Filter @{Name="requester-managed"; Values="true"} | Select Description, InterfaceType
```

The following is example output that shows the key fields that you can use to determine the purpose of a network interface: `Description` and `InterfaceType`.

```
Description                                      InterfaceType
-----------                                      -------------
VPC Endpoint Interface: vpce-0f00567fa8477a1e6   interface
VPC Endpoint Interface vpce-0d8ddce4be80e4474    interface
VPC Endpoint Interface vpce-078221a1e27d1ea5b    vpc_endpoint
Resource Gateway Interface rgw-0bba03f3d56060135 interface
VPC Endpoint Interface: vpce-0cc199f605eaeace7   interface
VPC Endpoint Interface vpce-019b90d6f16d4f958    interface
```

------