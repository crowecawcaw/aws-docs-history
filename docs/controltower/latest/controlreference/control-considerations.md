# Considerations for controls and OUs

When working with controls and OUs, consider the following properties:

###### Controls, landing zones, and OUs

- Mandatory controls are no longer enabled by default. Optional controls are applied at the discretion of administrators.
- Controls can now be enabled on any OU within a customer's AWS Organization once they enable AWS Control Tower.
- Regarding nested OUs, preventive controls enabled on any OUs higher in the tree will apply all OUs in the tree.
- Detective controls can be applied to an OU that has either the ConfigBaseline enabled or the AWSControlTowerBaseline.
- Hook controls can now be deployed into any OU. The hook will deploy the AWSServiceRoleForControlTower Service Linked Role (SLR), into the account and activate the opt-in regions.
  For more information about how controls are applied to nested OUs, in AWS Control Tower, see
  [Nested Ous and controls](../userguide/nested-ous.md#nested-ous-and-controls "../userguide/nested-ous.md#nested-ous-and-controls").
