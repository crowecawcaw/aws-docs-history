# Resource identifiers for APIs and controls

Each control in AWS Control Tower has unique identifiers for use with the control APIs. You can
call a control API using a global identifier or a Region-based identifier.

- The AWS Control Tower identifer is Region-based and has been available longer.
- We recommend that you use the global identifiers for most use cases in
  AWS Control Tower.

## Regional and global identifiers

A _global identifier_ (ARN) is available for all controls that are
part of AWS Control Catalog. This identifier is independent of any AWS Region. All
AWS Control Tower controls are included in AWS Control Catalog, and each AWS Control Tower control has a global
identifier.

Also, each AWS Control Tower control has a Regional identifier (ARN), which is a unique identifier for each Region in
which AWS Control Tower operates. The identifier for each control is shown in the [Tables of control
metadata](../userguide/control-metadata-tables.md "../userguide/control-metadata-tables.md").

- _The Regional identifier is not shown in the AWS Control Tower console, only in documentation._
- The global identifier is shown in the **API controlIdentifier**
  field, on the **Control details** page in the AWS Control Tower console. For a
  full list of global identifiers, see [All global identifiers for AWS Control Tower controls](all-global-identifiers.md "all-global-identifiers.md").

###### Note

The **API controlIdentifier** is distinct from the **ControlID** field, which
is a classification system for controls.

### View the Regional control identifiers for all controls

To view the Regional
`controlIdentifier` ARN for each control and Region, and other metadata, see [Tables of
control metadata](../userguide/control-metadata-tables.md "../userguide/control-metadata-tables.md"). The tables also include the identifiers for Security Hub
controls that are part of the [**AWS Security Hub Service-Managed Standard:
AWS Control Tower**](../userguide/security-hub-controls.md "../userguide/security-hub-controls.md").

###### How to change from AWS Control Tower control ARNs (Regional) to Control Catalog

control ARNs (global)

1. Deactivate the enabled control that has the ARN you wish to change.
2. Re-enable the control and specify the Control Catalog ARN, which will
   create a new AWS resource that has the Control Catalog ARN.

###### Important

When you disable the control, your environment may experience a gap in
governance until the new control resource is enabled.

### View global control identifiers in the

console

To view the global control identifiers and other details about AWS Control Tower controls in the
console, navigate to the **Control details** page in the AWS Control Tower
console. You can find the identifier in the **API
controlIdentifier** field.

###### Example forms of identifiers

Here are examples of identifiers you
may see.

- Security Hub example **API controlIdentifier**
  (regional):
  `arn:aws:controltower:us-east-1::control/OOTDCUSIKIZZ`
- Legacy control example **API controlIdentifier**
  (regional):
  `arn:aws:controltower:us-east-1::control/AWS-GR_LOG_GROUP_POLICY`
- Proactive control example **API controlIdentifier**
  (regional):
  `arn:aws:controltower:us-east-1::control/EHSOKSSMVFWF`
- Control catalog example **API controlIdentifier**
  (global):
  `arn:aws:controlcatalog:::control/5mhjhod4ky44haldvja2v4x3a`
  Older controls (legacy controls) include the name of the control in the ARN,
  but newer controls have a different identifier, and that is expected.

Legacy control example:
`arn:aws:controltower:us-east-1::control/AWS-GR_CLOUDTRAIL_CHANGE_PROHIBITED`

Newer control example:
`arn:aws:controltower:us-east-1::control/WTDSMKDKDNLE`

### Find identifiers for OUs

For more information about how to find the resource identifier for an OU and its
resources, see [Resource types defined by AWS Organizations](../../../service-authorization/latest/reference/list_awsorganizations.md#awsorganizations-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsorganizations.md#awsorganizations-resources-for-iam-policies").

To learn more about how to get information from an OU, see [the
AWS Organizations API Reference](../../../organizations/latest/APIReference/API_DescribeOrganizationalUnit.md "../../../organizations/latest/APIReference/API_DescribeOrganizationalUnit.md").
