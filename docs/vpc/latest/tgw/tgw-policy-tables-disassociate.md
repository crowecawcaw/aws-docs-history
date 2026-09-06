

# Disassociate a transit gateway policy table in AWS Transit Gateway
<a name="tgw-policy-tables-disassociate"></a>

Disassociate a policy table from a transit gateway attachment.

**Important**  
After the association is removed, the attachment has no route table or policy table associated with it. All ingressing traffic is dropped until you associate the attachment with a route table or a new policy table.

**To disassociate a policy table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Transit Gateways**, choose **Transit Gateway Policy Tables**, and select the policy table.

1. Choose the **Associations** tab.

1. Select the association you want to remove.

1. Choose **Delete association**.

1. In the confirmation dialog, review the policy table ID and attachment ID. Acknowledge the warning: *Removing this association will disable policy-based routing for traffic from this attachment. All ingress traffic from this attachment will be dropped until you associate it with a route table or a new policy table.* Choose **Delete**.

A success banner appears: *Successfully deleted association from {tgw-attach-id}.*

**To disassociate a policy table using the AWS CLI**  
Use the [disassociate-transit-gateway-policy-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-transit-gateway-policy-table.html) command.

```
aws ec2 disassociate-transit-gateway-policy-table \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --transit-gateway-attachment-id tgw-attach-0def6EXAMPLE
```

Example response. The association transitions to the `disassociating` state:

```
{
    "Association": {
        "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
        "TransitGatewayAttachmentId": "tgw-attach-0def6EXAMPLE",
        "State": "disassociating"
    }
}
```