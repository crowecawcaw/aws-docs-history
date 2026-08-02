# Associate a transit gateway policy table in AWS Transit Gateway

Associate a policy table with one or more transit gateway attachments. An attachment can be
associated with either a policy table or a route table, but not both. If the attachment
currently has a route table associated, you must disassociate it first.

Customer-managed policy based routing is compatible with all transit gateway attachment types: VPC,
Direct Connect, VPN (Site-to-Site), Client VPN, VPN Concentrator, Network Functions, transit gateway
Connect, and Peering. The exception is transit gateway-to-Cloud WAN (CWAN) peering attachments. For
details, see [Limitations](tgw-policy-tables-limitations.md "tgw-policy-tables-limitations.md").

You can associate the same policy table with multiple attachments. All traffic arriving on
those attachments is evaluated against the same rule set.

## Disassociate an existing route table

If the attachment is currently associated with a route table, disassociate it
first.

###### To disassociate a route table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway Route
   Tables** and select the route table.
3. Choose the **Associations** tab.
4. Select the attachment row and choose **Delete
   association**.
5. In the confirmation dialog, choose **Delete association**.

###### To disassociate a route table using the AWS CLI

Use the [disassociate-transit-gateway-route-table](../../../cli/latest/reference/ec2/disassociate-transit-gateway-route-table.md "../../../cli/latest/reference/ec2/disassociate-transit-gateway-route-table.md") command.

```
# Disassociate existing route table (if applicable)
aws ec2 disassociate-transit-gateway-route-table \
    --transit-gateway-attachment-id tgw-attach-0def6EXAMPLE \
    --transit-gateway-route-table-id tgw-rtb-CURRENTEXAMPLE
```

Example response. The association transitions to the `disassociating`
state:

```
{
    "Association": {
        "TransitGatewayRouteTableId": "tgw-rtb-CURRENTEXAMPLE",
        "TransitGatewayAttachmentId": "tgw-attach-0def6EXAMPLE",
        "ResourceId": "vpc-0abcd1234EXAMPLE",
        "ResourceType": "vpc",
        "State": "disassociating"
    }
}
```

## Associate the policy table

###### To associate a policy table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Transit Gateways**, choose
   **Transit Gateway Policy Tables** and select your policy
   table.
3. Choose the **Associations** tab.
4. Choose **Create association**.
5. On the **Create association** modal, the **Transit
   gateway policy table** and **Transit gateway ID**
   fields are pre-filled.
6. For **Transit gateway attachment**, select the attachment from
   the dropdown. The dropdown lists all eligible attachments on the same transit gateway (VPC,
   Direct Connect, VPN, transit gateway Connect, Peering).
7. Choose **Create**.

The association **State** transitions from
**Associating** to **Associated**. You can repeat these
steps to associate additional attachments with the same policy table.

###### To associate a policy table using the AWS CLI

Use the [associate-transit-gateway-policy-table](../../../cli/latest/reference/ec2/associate-transit-gateway-policy-table.md "../../../cli/latest/reference/ec2/associate-transit-gateway-policy-table.md") command.

```
# Associate the policy table
aws ec2 associate-transit-gateway-policy-table \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --transit-gateway-attachment-id tgw-attach-0def6EXAMPLE
```

Example response. The association starts in the `associating` state and
transitions to `associated`:

```
{
    "Association": {
        "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
        "TransitGatewayAttachmentId": "tgw-attach-0def6EXAMPLE",
        "ResourceType": "vpc",
        "State": "associating"
    }
}
```

## IAM condition example

You can use resource-level conditions to restrict which attachments or policy tables a
principal can act on. For example, the following policy allows a user to associate policy
tables only with attachments tagged `network: Prod Network`:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": ["ec2:AssociateTransitGatewayPolicyTable"],
        "Resource": "arn:aws:ec2:*:*:transit-gateway-attachment/*",
        "Condition": {
            "StringEquals": {
                "ec2:ResourceTag/network": "Prod Network"
            }
        }
    }]
}
```
