# Disassociate a transit gateway policy table in AWS Transit Gateway

Disassociate a policy table from a transit gateway attachment.

###### Important

After the association is removed, the attachment has no route table or policy table
associated with it. All ingressing traffic is dropped until you associate the attachment
with a route table or a new policy table.

###### To disassociate a policy table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Transit Gateways**, choose
   **Transit Gateway Policy Tables**, and select the policy
   table.
3. Choose the **Associations** tab.
4. Select the association you want to remove.
5. Choose **Delete association**.
6. In the confirmation dialog, review the policy table ID and attachment ID.
   Acknowledge the warning: _Removing this association will disable
   policy-based routing for traffic from this attachment. All ingress traffic from this
   attachment will be dropped until you associate it with a route table or a new policy
   table._ Choose **Delete**.
   A success banner appears: _Successfully deleted association from
   {tgw-attach-id}._

###### To disassociate a policy table using the AWS CLI

Use the [disassociate-transit-gateway-policy-table](../../../cli/latest/reference/ec2/disassociate-transit-gateway-policy-table.md "../../../cli/latest/reference/ec2/disassociate-transit-gateway-policy-table.md") command.

```
aws ec2 disassociate-transit-gateway-policy-table \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --transit-gateway-attachment-id tgw-attach-0def6EXAMPLE
```

Example response. The association transitions to the `disassociating`
state:

```
{
    "Association": {
        "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
        "TransitGatewayAttachmentId": "tgw-attach-0def6EXAMPLE",
        "State": "disassociating"
    }
}
```
