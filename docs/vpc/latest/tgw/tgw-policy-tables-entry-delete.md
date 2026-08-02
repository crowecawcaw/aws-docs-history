# Delete a policy table entry in AWS Transit Gateway

Delete a customer-managed entry from a transit gateway policy table. System-managed entries cannot be
deleted.

###### Important

If you delete all customer-managed entries and there are no applicable system-managed
entries, the transit gateway drops all packets arriving on attachments associated with that table.
Add at least one rule or re-associate the attachment with a route table to restore
traffic forwarding.

###### To delete a policy table entry using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Transit Gateways**, choose
   **Transit Gateway Policy Tables**.
3. In **Transit Gateway Policy Tables**, select the policy
   table.
4. Choose the **Entries** tab.
5. Select the customer-managed entry you want to delete. System entries cannot be
   deleted.
6. Choose **Delete**.
7. In the confirmation dialog, review the entry details (rule number, target route
   table, source CIDR block, source port, destination CIDR block, destination port,
   protocol). Acknowledge the message _Once deleted, you'll need to create a
   new entry with the same attributes to restore it_ and choose
   **Delete**.
   A success banner appears: _Policy table entry with rule number {ruleNumber} was
   successfully deleted._

###### To delete a policy table entry using the AWS CLI

Use the [delete-transit-gateway-policy-table-entry](../../../cli/latest/reference/ec2/delete-transit-gateway-policy-table-entry.md "../../../cli/latest/reference/ec2/delete-transit-gateway-policy-table-entry.md") command. The deleted entry is
returned in the response with `"State": "deleted"`.

```
aws ec2 delete-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 100
```

```
{
    "TransitGatewayPolicyTableEntry": {
        "PolicyRuleNumber": "100",
        "PolicyRule": {
            "SourceCidrBlock": "10.100.0.0/16",
            "SourcePortRange": "*",
            "DestinationCidrBlock": "*",
            "DestinationPortRange": "443",
            "Protocol": "6"
        },
        "TargetRouteTableId": "tgw-rtb-0a823edbdeEXAMPLE",
        "State": "deleted"
    }
}
```

###### Note

You cannot delete a transit gateway route table that is referenced as a target by any policy
table entry. Use `GetTransitGatewayPolicyTableEntries` with a
`target-route-table-id` filter to identify referencing entries, then update
or delete them before retrying the route table deletion. Unlike route entries (which are
black-holed when a target attachment is deleted), policy table entries are not
automatically cleaned up. They must be explicitly removed.
