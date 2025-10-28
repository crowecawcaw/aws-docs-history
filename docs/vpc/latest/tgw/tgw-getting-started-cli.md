# Tutorial: Create an AWS Transit Gateway using the AWS

command line

In this tutorial, you'll learn how to use the AWS CLI to create a transit gateway and
connect two VPCs to it. You'll create the transit gateway, attach both VPCs, and then
configure the necessary routes to enable communication between the transit gateway and your
VPCs.

## Prerequisites

Before you begin, make sure you have:

- AWS CLI installed and configured with appropriate permissions. If you don't have the AWS CLI
  installed, see the _AWS Command Line Interface
  Documentation_.
- The VPCs can neither have identical nor overlapping CIDRs. For more information, see [Create a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md") in the
  _Amazon VPC User Guide_.
- One EC2 instance in each VPC. For the steps to launch an EC2 instance into a VPC, see [Launch an
  instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_.
- Security groups configured to allow ICMP traffic between the instances. For the steps to
  control traffic using security groups, see [Control traffic to your
  AWS resources using security groups](../userguide/vpc-security-groups.md "../userguide/vpc-security-groups.md") in the
  _Amazon VPC User Guide_.
- Appropriate IAM permissions to work with transit gateways. To check transit gateway IAM
  permissions, see [Identity and access management in AWS Transit Gateways](transit-gateway-authentication-access-control.md "transit-gateway-authentication-access-control.md") in the
  _AWS Transit Gateway Guide_.

###### Steps

- [Step 1: Create the transit gateway](#create-transit-gateway "#create-transit-gateway")
- [Step 2: Verify the transit gateway availability state](#verify-state "#verify-state")
- [Step 3: Attach your VPCs to your transit gateway](#attach-vpcs "#attach-vpcs")
- [Step 4: Verify that the transit gateway attachments are available](#configure-routes "#configure-routes")
- [Step 5: Add routes between your transit gateway and VPCs](#create-routes "#create-routes")
- [Step 6: Test the transit gateway](#test-connectivity "#test-connectivity")
- [Step 7: Delete the transit gateway attachments and transit
  gateway](#cleanup "#cleanup")
- [Conclusion](#conclusion "#conclusion")

## Step 1: Create the transit gateway

When you create a transit gateway, AWS creates a default transit gateway route table
and uses it as the default association route table and the default propagation route
table. The following shows an example `create-transit-gateway` request in the
`us-west-2` Region. Additional `options` were passed in the
request. For more information about the `create-transit-gateway` command,
including a list of the options you can pass in the request, see [create-transit-gateway](../../../cli/latest/reference/ec2/create-transit-gateway.md "../../../cli/latest/reference/ec2/create-transit-gateway.md").

```
aws ec2 create-transit-gateway \
  --description "My Transit Gateway" \
  --region us-west-2
```

The response then shows that the transit gateway was created. In the response, the
`Options` that are returned are all default values.

```
{
    "TransitGateway": {
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-1234567890abcdef0",
        "State": "pending",
        "OwnerId": "123456789012",
        "Description": "My Transit Gateway",
        "CreationTime": "2025-06-23T17:39:33+00:00",
        "Options": {
            "AmazonSideAsn": 64512,
            "AutoAcceptSharedAttachments": "disable",
            "DefaultRouteTableAssociation": "enable",
            "AssociationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
            "DefaultRouteTablePropagation": "enable",
            "PropagationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
            "VpnEcmpSupport": "enable",
            "DnsSupport": "enable",
            "SecurityGroupReferencingSupport": "disable",
            "MulticastSupport": "disable"
        }
    }
}
```

###### Note

This command returns information about your new transit gateway, including its ID. Make note of the transit gateway ID (`tgw-1234567890abcdef0`) as you'll need it in subsequent steps.

## Step 2: Verify the transit gateway availability state

When you create a transit gateway, it's placed in a `pending` state. The
state will change from pending to available automatically, but until it does you can't
attach any VPCs until the state changes. To verify the state, run the
`describe-transit-gatweways` command using the newly created transit
gateway ID along with the filters option. The `filters` option uses
`Name=state` and `Values=available` pairs. The command then
searches to verify if the state of your transit gateway is in an available state. If it
is, the response shows `"State": "available"`. If it's in any other state
then it is not yet available for use. Wait several minutes before running the
command.

For more information about the `describe-transit-gateways` command, see
[describe-transit-gateways](../../../cli/latest/reference/ec2/describe-transit-gateways.md "../../../cli/latest/reference/ec2/describe-transit-gateways.md").

```
aws ec2 describe-transit-gateways \
  --transit-gateway-ids tgw-1234567890abcdef0 \
  --filters Name=state,Values=available

```

Wait until the transit gateway state changes from `pending` to
`available` before proceeding. In the following response, the
`State` has changed to `available`.

```
{
    "TransitGateways": [
        {
            "TransitGatewayId": "tgw-1234567890abcdef0",
            "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-1234567890abcdef0",
            "State": "available",
            "OwnerId": "123456789012",
            "Description": "My Transit Gateway",
            "CreationTime": "2022-04-20T19:58:25+00:00",
            "Options": {
                "AmazonSideAsn": 64512,
                "AutoAcceptSharedAttachments": "disable",
                "DefaultRouteTableAssociation": "enable",
                "AssociationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
                "DefaultRouteTablePropagation": "enable",
                "PropagationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
                "VpnEcmpSupport": "enable",
                "DnsSupport": "enable",
                "SecurityGroupReferencingSupport": "disable",
                "MulticastSupport": "disable"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "example-transit-gateway"
                }
            ]
        }
    ]
}
```

## Step 3: Attach your VPCs to your transit gateway

Once your transit gateway is available, create an attachment for each VPC using the
`create-transit-gateway-vpc-attachment`. You'll need to include the
`transit-gateway-id`, the `vpc-id`, and the
`subnet-ids`.

For more information about the `create-transit-vpc attachment` command,
see [create-transit-gateway-vpc-attachment](../../../cli/latest/reference/ec2/create-transit-gateway-vpc-attachment.md "../../../cli/latest/reference/ec2/create-transit-gateway-vpc-attachment.md").

In the following example, the command is run twice, once for each VPC.

For the first VPC run the following using the first `vpc_id` and
`subnet-ids`:

```
aws ec2 create-transit-gateway-vpc-attachment \
  --transit-gateway-id tgw-1234567890abcdef0 \
  --vpc-id vpc-1234567890abcdef0 \
  --subnet-ids subnet-1234567890abcdef0
```

The response shows the successful attachment. The attachment is created in a
`pending` state. There's no need to change this state as it changes to an
`available` state automatically. This might take several minutes.

```
{
    "TransitGatewayVpcAttachment": {
        "TransitGatewayAttachmentId": "tgw-attach-1234567890abcdef0",
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "VpcId": "vpc-1234567890abcdef0",
        "VpcOwnerId": "123456789012",
        "State": "pending",
        "SubnetIds": [
            "subnet-1234567890abcdef0",
            "subnet-abcdef1234567890"
        ],
        "CreationTime": "2025-06-23T18:35:11+00:00",
        "Options": {
            "DnsSupport": "enable",
            "SecurityGroupReferencingSupport": "enable",
            "Ipv6Support": "disable",
            "ApplianceModeSupport": "disable"
        }
    }
}
```

For the second VPC, run the same command as above using the second `vpc_id`
and `subnet-ids`:

```
aws ec2 create-transit-gateway-vpc-attachment \
  --transit-gateway-id tgw-1234567890abcdef0 \
  --vpc-id vpc-abcdef1234567890 \
  --subnet-ids subnet-abcdef01234567890
```

The response for this command also shows a successful attachment, with the attachment
currently in a `pending` state.

```
{
    {
    "TransitGatewayVpcAttachment": {
        "TransitGatewayAttachmentId": "tgw-attach-abcdef1234567890",
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "VpcId": "vpc-abcdef1234567890",
        "VpcOwnerId": "123456789012",
        "State": "pending",
        "SubnetIds": [
            "subnet-fedcba0987654321",
            "subnet-0987654321fedcba"
        ],
        "CreationTime": "2025-06-23T18:42:56+00:00",
        "Options": {
            "DnsSupport": "enable",
            "SecurityGroupReferencingSupport": "enable",
            "Ipv6Support": "disable",
            "ApplianceModeSupport": "disable"
        }
    }
}
```

## Step 4: Verify that the transit gateway attachments are available

Transit gateway attachments are created in a initial `pending` state. You
won't be able to use these the attachments in your routes until the state changes to
`available`. This happens automatically. Use the
`describe-transit-gateways` command, along with the
`transit-gateway-id`, to check the `State`. For more
information about the `describe-transit-gateways` command, see [describe-transit-gateways](../../../cli/latest/reference/ec2/create-route.md "../../../cli/latest/reference/ec2/create-route.md").

Run the following command to check the status. In this example, optional
`Name` and `Values` filters fields are passed in the
request:

```
aws ec2 describe-transit-gateway-vpc-attachments \
  --filters Name=transit-gateway-id,Values=tgw-1234567890abcdef0
```

The following response shows that both attachments in an `available`
state:

```
{
    "TransitGatewayVpcAttachments": [
        {
            "TransitGatewayAttachmentId": "tgw-attach-1234567890abcdef0",
            "TransitGatewayId": "tgw-1234567890abcdef0",
            "VpcId": "vpc-1234567890abcdef0",
            "VpcOwnerId": "123456789012",
            "State": "available",
            "SubnetIds": [
                "subnet-1234567890abcdef0",
                "subnet-abcdef1234567890"
            ],
            "CreationTime": "2025-06-23T18:35:11+00:00",
            "Options": {
                "DnsSupport": "enable",
                "SecurityGroupReferencingSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": []
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-abcdef1234567890",
            "TransitGatewayId": "tgw-1234567890abcdef0",
            "VpcId": "vpc-abcdef1234567890",
            "VpcOwnerId": "123456789012",
            "State": "available",
            "SubnetIds": [
                "subnet-fedcba0987654321",
                "subnet-0987654321fedcba"
            ],
            "CreationTime": "2025-06-23T18:42:56+00:00",
            "Options": {
                "DnsSupport": "enable",
                "SecurityGroupReferencingSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": []
        }
    ]
}
```

## Step 5: Add routes between your transit gateway and VPCs

Configure routes in each VPC's route table to direct traffic to the other VPC through
the transit gateway using the `create-route` command along with the
`transit-gateway-id` for each VPC route table. In the following example,
the command is run twice, once for each route table. The request includes the
`route-table-id`, the `destination-cidr-block`, and
`transit-gateway-id` for each VPC route you're creating.

For more information about `create-route` command, see [create-route](../../../cli/latest/reference/ec2/create-route.md "../../../cli/latest/reference/ec2/create-route.md").

For the first VPC's route table run the following command:

```
aws ec2 create-route \
  --route-table-id rtb-1234567890abcdef0 \
  --destination-cidr-block 10.2.0.0/16 \
  --transit-gateway-id tgw-1234567890abcdef0
```

For the second VPC's route table run the following command. This route uses a
`route-table-id` and `destination-cidr-block` different from
the first VPC. However, since you're only using a single transit gateway, the same
`transit-gateway-id` is used.

```

aws ec2 create-route \
  --route-table-id rtb-abcdef1234567890 \
  --destination-cidr-block 10.1.0.0/16 \
  --transit-gateway-id tgw-1234567890abcdef0
```

The response returns `true` for each route, indicating the routes were
created.

```
{
    "Return": true
}
```

###### Note

Replace the destination CIDR blocks with the actual CIDR blocks of your VPCs.

## Step 6: Test the transit gateway

You can confirm that the transit gateway was successfully created by connecting to an
EC2 instance in one VPC and pinging an instance in the other VPC, and then running the
`ping` command.

1. Connect to your EC2 instance in the first VPC using SSH or EC2 Instance Connect
2. Ping the private IP address of the EC2 instance in the second VPC:

```
ping 10.2.0.50
```

###### Note

Replace `10.2.0.50` with the actual private IP address of your EC2 instance in the second VPC.

If the ping is successful, your transit gateway is correctly configured and routing traffic between your VPCs.

## Step 7: Delete the transit gateway attachments and transit

gateway

When you no longer need the transit gateway, you can delete it. First, you must delete
all attachments. Run the `delete-transit-gateway-vpc-attachment` command,
using the `transit-gateway-attachment-id` for each attachment. After running
the command, use `delete-transit-gateway` to delete the transit gateway. For
the following, delete the two VPC attachments and the single transit gateway that were
created in the previous steps.

###### Important

You'll stop incurring charges once you delete all of the transit gateway
attachments.

1. Delete the VPC attachments using the
   `delete-transit-gateway-vpc-attachment` command. For more
   information about `delete-transit-gateway-vpc-attachment` command, see [delete-transit-gateway-vpc-attachment](../../../cli/latest/reference/ec2/delete-transit-gateway-vpc-attachment.md "../../../cli/latest/reference/ec2/delete-transit-gateway-vpc-attachment.md").

For the first attachment, run the following command:

```
aws ec2 delete-transit-gateway-vpc-attachment \
  --transit-gateway-attachment-id tgw-attach-1234567890abcdef0
```

The delete response for the first VPC attachment returns the following:

```
{
    "TransitGatewayVpcAttachment": {
        "TransitGatewayAttachmentId": "tgw-attach-1234567890abcdef0",
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "VpcId": "vpc-abcdef1234567890",
        "VpcOwnerId": "123456789012",
        "State": "deleting",
        "CreationTime": "2025-06-23T18:42:56+00:00"
    }
}
```

Run the `delete-transit-gateway-vpc-attachment` command for the
second attachment:

```
aws ec2 delete-transit-gateway-vpc-attachment \
  --transit-gateway-attachment-id tgw-attach-abcdef1234567890
```

The delete response for the second VPC attachment returns the
following:

```
The response returns:
{
    "TransitGatewayVpcAttachment": {
        "TransitGatewayAttachmentId": "tgw-attach-abcdef1234567890",
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "VpcId": "vpc-abcdef1234567890",
        "VpcOwnerId": "123456789012",
        "State": "deleting",
        "CreationTime": "2025-06-23T18:42:56+00:00"
    }
}
```

2. Attachments are in a `deleting` state until they're deleted. Once
   deleted, you can then delete the transit gateway. Use the
   `delete-transit-gateway` command along with the
   `transit-gateway-id`. For more information about
   `delete-transit-gateway` command, see [delete-transit-gateway](../../../cli/latest/reference/ec2/delete-transit-gateway.md "../../../cli/latest/reference/ec2/delete-transit-gateway.md").

The following example deletes `My Transit Gateway` which you
created in the first step above:

```
aws ec2 delete-transit-gateway \
  --transit-gateway-id tgw-1234567890abcdef0
```

The following shows the response to the request, which includes the deleted transit
gateway ID and name, along with the original options set for the transit
gateway when it was created.

```
{
    "TransitGateway": {
        "TransitGatewayId": "tgw-1234567890abcdef0",
        "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-1234567890abcdef0",
        "State": "deleting",
        "OwnerId": "123456789012",
        "Description": "My Transit Gateway",
        "CreationTime": "2025-06-23T17:39:33+00:00",
        "Options": {
            "AmazonSideAsn": 64512,
            "AutoAcceptSharedAttachments": "disable",
            "DefaultRouteTableAssociation": "enable",
            "AssociationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
            "DefaultRouteTablePropagation": "enable",
            "PropagationDefaultRouteTableId": "tgw-rtb-abcdef1234567890a",
            "VpnEcmpSupport": "enable",
            "DnsSupport": "enable",
            "SecurityGroupReferencingSupport": "disable",
            "MulticastSupport": "disable"
        },
        "Tags": [
            {
                "Key": "Name",
                "Value": "example-transit-gateway"
            }
        ]
    }
}
```

## Conclusion

You've successfully created a transit gateway, attached two VPCs to it, configured routing
between them, and verified connectivity. This simple example demonstrates the basic
functionality of AWS Transit Gateways. For more complex scenarios, such as connecting
to on-premises networks or implementing more advanced routing configurations, see the
[_AWS Transit Gateways Guide_](what-is-transit-gateway.md "what-is-transit-gateway.md").
