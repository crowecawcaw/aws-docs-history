# Considerations for controls and OUs

When working with controls and OUs, consider the following properties:

###### Controls, landing zones, and OUs

- After you create your landing zone, all resources in your landing zone are subject to controls. For example, certain controls apply to Amazon S3 buckets.
- OUs created through AWS Control Tower have mandatory controls applied to them
  automatically. Optional controls are applied at the discretion of
  administrators.
- OUs created outside of an AWS Control Tower landing zone (such as,_unregistered OUs created in AWS Organizations_) are displayed in the AWS Control Tower console, but
  AWS Control Tower controls do not apply to those OUs, unless they become registered
  OUs.
- Regarding nested OUs, preventive controls enabled on any OUs higher in the tree will apply to unregistered OUs in that tree.
- When you enable controls on an organizational unit (OU) that is registered
  with AWS Control Tower, preventive controls apply to all member accounts under the OU,
  enrolled and unenrolled. Detective controls apply to enrolled accounts
  only.
  For more information about how controls are applied to nested OUs, in AWS Control Tower, see
  [Nested Ous and controls](../userguide/nested-ous.md#nested-ous-and-controls "../userguide/nested-ous.md#nested-ous-and-controls").
