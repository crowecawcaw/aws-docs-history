# Create a transit gateway policy table in AWS Transit Gateway

Create a policy table and associate it with your transit gateway.

###### To create a transit gateway policy table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Transit gateways**, choose
   **Transit Gateway Policy Tables**.
3. Choose **Create transit gateway policy table**.
4. For **Transit gateway ID**, select your transit gateway from the dropdown
   list.
5. (Optional) Under **Tags**, add tags to help identify the policy
   table.
6. Choose **Create transit gateway policy table**.
   The policy table enters a **Pending** state. Wait for the state to change
   to **Available** before proceeding.

###### To create a transit gateway policy table using the AWS CLI

Use the [create-transit-gateway-policy-table](../../../cli/latest/reference/ec2/create-transit-gateway-policy-table.md "../../../cli/latest/reference/ec2/create-transit-gateway-policy-table.md") command. Replace
`tgw-0bc994abffEXAMPLE` with your transit gateway ID.

```
aws ec2 create-transit-gateway-policy-table \
    --transit-gateway-id tgw-0bc994abffEXAMPLE
```

Example response:

```
{
    "TransitGatewayPolicyTable": {
        "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
        "TransitGatewayId": "tgw-0bc994abffEXAMPLE",
        "State": "pending"
    }
}
```
