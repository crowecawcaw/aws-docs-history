

# Allocate VPC peering data transfer

When you associate a Networking Flexible Cost Allocation (FCA) policy with a VPC peering connection, the data transfer charges for traffic over the connection are itemized at the granularity that you choose in the policy. Without a policy, the charges appear as a single charge.

The resource type for these policies is `pcx`.

The following rules apply to VPC peering policies:
+ You can allocate the `data-transfer` dimension. There is no data processing charge for a VPC peering connection.
+ The supported reporting granularities are `eni`, `ec2`, `subnet`, `vpc`, `account`, `peering-id`, and `cidr`. The `peering-id` granularity labels usage with the peering connection, and is available only for VPC peering connections.
+ Allocation applies to peering connections between VPCs in the same Region.
+ You can associate a VPC peering connection with a policy only from the requester account, which is the account that owns the VPC that requested the peering connection. If you own only the accepter VPC, the request fails with an `UnauthorizedOperation` error. Configure FCA for the connection from the requester account.
+ If the peer VPC is in a different account, the peer's resources might not be visible to you. In that case, usage that you specify at the `subnet`, `ec2`, or `eni` granularity is labeled with the peering connection.
+ To label usage by CIDR range, see [Label usage by CIDR range](networking-flex-cost-allocation-natgw.md#networking-flex-cost-allocation-natgw-cidr). For a peering connection, a `PrefixesType` of `source-prefixes` matches the IP address of the peer, and `destination-prefixes` matches the IP address of the local resource.

## Example – Allocate data transfer by peering connection
<a name="networking-flex-cost-allocation-pcx-example"></a>

In the following example, your VPC has peering connections with two other VPCs. You want to know how much data transfer each peering connection accounts for.

![VPC A, which has the policy associated, connects to VPC B through peering connection pcx-00abc and to VPC C through peering connection pcx-00def, within the same Region.](https://docs.aws.amazon.com/vpc/latest/userguide/images/fca-usecase-pcx.png)


You create the following policy and associate it with your VPC, using the Amazon VPC console, the AWS CLI, or AWS CloudFormation. The policy allocates data transfer by peering connection, and applies to every peering connection in the VPC.

------
#### [ AWS Management Console ]

**To create the policy in the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Networking flexible cost allocation policies**.

1. Choose **Create policy**.

1. For **Resource type**, choose **VPC peering connections**.

1. For **Dimensions**, choose **Data transfer**.

1. For **Reporting granularity**, choose **Peering connection**.

1. Choose **Next**, and for **VPC scopes**, select your VPC.

1. Choose **Next**, review the policy, and then choose **Create policy**.

------
#### [ AWS CLI ]

Create the policy, and then associate it with every peering connection in the VPC.

```
aws ec2 create-networking-flex-cost-allocation-policy \
    --network-resource-type pcx \
    --pcx-fca-policy-document '{"ReportingGranularity":["peering-id"],"Dimensions":["data-transfer"]}' \
    --show-back-enabled \
    --description "Allocate VPC peering costs by peering connection"
```

```
aws ec2 associate-networking-flex-cost-allocation-policy \
    --fca-policy-id fcap-0123456789abcdef0 \
    --network-resource-scope 'ResourceType=vpc,ResourceIds=[vpc-1a2b3c4d5e6f7a8b9]'
```

------
#### [ CloudFormation ]

The following template creates the policy and associates it with the VPC.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: FCA policy that allocates VPC peering data transfer by peering connection
Parameters:
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: The VPC whose peering connections to allocate costs for
Resources:
  PcxFcaPolicy:
    Type: AWS::EC2::FcaPolicy
    Properties:
      NetworkResourceType: pcx
      PcxFcaPolicyDocument:
        ReportingGranularity:
          - peering-id
        Dimensions:
          - data-transfer
      ShowBackEnabled: true
      Description: Allocate VPC peering costs by peering connection
  PcxFcaPolicyAssociation:
    Type: AWS::EC2::FcaPolicyAssociation
    Properties:
      FcaPolicyId: !GetAtt PcxFcaPolicy.FcaPolicyId
      NetworkResourceId: !Ref VpcId
      NetworkResourceScopeType: vpc
```

------

After the policy takes effect and you turn on the data in your Cost and Usage Reports, the data transfer from an instance in your VPC is itemized by peering connection, and each line item also shows the account that owns the peer VPC, as shown in the following table. The first line item is the summary line item for the instance. Without a policy, your report shows only this line item. To itemize by the peer's account instead, use the `account` granularity. The values in the table are examples.


| Shared resource | Allocated to | Owner account | Data transfer | 
| --- | --- | --- | --- | 
| i-0aaa | Not applicable | Not applicable | 50 GB | 
| i-0aaa | pcx-00abc | 222222222222 | 30 GB | 
| i-0aaa | pcx-00def | 333333333333 | 20 GB | 