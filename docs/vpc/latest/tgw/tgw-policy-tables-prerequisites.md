# Prerequisites for transit gateway policy tables in AWS Transit Gateway

Before configuring Policy-Based Routing (PBR) on a transit gateway attachment, confirm the
following:

- You have an existing transit gateway. PBR is enabled on all transit gateways by default. No additional
  configuration is required to activate the feature.
- You have the IAM permissions required to call the PBR APIs. At minimum, the
  following actions must be allowed on the relevant resources:

  - `ec2:CreateTransitGatewayPolicyTable`
  - `ec2:DescribeTransitGatewayPolicyTables`
  - `ec2:DeleteTransitGatewayPolicyTable`
  - `ec2:AssociateTransitGatewayPolicyTable`
  - `ec2:DisassociateTransitGatewayPolicyTable`
  - `ec2:GetTransitGatewayPolicyTableAssociations`
  - `ec2:GetTransitGatewayPolicyTableEntries`
  - `ec2:CreateTransitGatewayPolicyTableEntry`
  - `ec2:ModifyTransitGatewayPolicyTableEntry`
  - `ec2:DeleteTransitGatewayPolicyTableEntry`

- The transit gateway route tables you intend to reference as targets already exist.
- If an attachment is currently associated with a route table, you must disassociate
  it before associating a policy table.
  For information about resource-level IAM conditions for PBR, see the example policy in
  [Associate a transit gateway policy table](tgw-policy-tables-associate.md "tgw-policy-tables-associate.md").
