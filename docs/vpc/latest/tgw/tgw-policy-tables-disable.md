# Delete a transit gateway policy table in AWS Transit Gateway

Delete a transit gateway policy table. When a table is deleted, all policy rules within that
table are deleted.

###### Important

Before deleting a policy table, disassociate all attachments from it. Any attachment
that loses its policy table association without being reassociated with a route table
will drop all ingressing traffic.

###### To delete a transit gateway policy table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Transit gateways**, choose
   **Transit Gateway Policy Tables**.
3. Select the transit gateway policy table to delete.
4. Choose **Actions**, and then choose **Delete
   policy table**.
5. In the confirmation dialog, confirm that you want to delete the table.

###### To delete a transit gateway policy table using the AWS CLI

Use the [delete-transit-gateway-policy-table](../../../cli/latest/reference/ec2/delete-transit-gateway-policy-table.md "../../../cli/latest/reference/ec2/delete-transit-gateway-policy-table.md") command.

```
aws ec2 delete-transit-gateway-policy-table \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE
```

Example response. The table transitions to the `deleting` state:

```
{
    "TransitGatewayPolicyTable": {
        "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
        "TransitGatewayId": "tgw-0bc994abffEXAMPLE",
        "State": "deleting",
        "CreationTime": "2026-01-01T00:00:00.000Z"
    }
}
```
