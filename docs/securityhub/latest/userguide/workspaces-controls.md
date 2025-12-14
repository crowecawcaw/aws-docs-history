# Security Hub CSPM controls for WorkSpaces

These AWS Security Hub CSPM controls evaluate the Amazon WorkSpaces service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [WorkSpaces.1] WorkSpaces user volumes should be encrypted at rest

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::WorkSpaces::Workspace`

**AWS Config rule:**
[`workspaces-user-volume-encryption-enabled`](../../../config/latest/developerguide/workspaces-user-volume-encryption-enabled.md "../../../config/latest/developerguide/workspaces-user-volume-encryption-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a user volume in an Amazon WorkSpaces WorkSpace is encrypted at rest. The control fails if the
WorkSpace user volume isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To encrypt a WorkSpaces user volume, see [Encrypt a WorkSpace](../../../workspaces/latest/adminguide/encrypt-workspaces.md#encrypt_workspace "../../../workspaces/latest/adminguide/encrypt-workspaces.md#encrypt_workspace") in the _Amazon WorkSpaces Administration Guide_.

## [WorkSpaces.2] WorkSpaces root volumes should be encrypted at rest

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::WorkSpaces::Workspace`

**AWS Config rule:**
[`workspaces-root-volume-encryption-enabled`](../../../config/latest/developerguide/workspaces-root-volume-encryption-enabled.md "../../../config/latest/developerguide/workspaces-root-volume-encryption-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a root volume in an Amazon WorkSpaces WorkSpace is encrypted at rest. The control fails if the
WorkSpace root volume isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To encrypt a WorkSpaces root volume, see [Encrypt a WorkSpace](../../../workspaces/latest/adminguide/encrypt-workspaces.md#encrypt_workspace "../../../workspaces/latest/adminguide/encrypt-workspaces.md#encrypt_workspace") in the _Amazon WorkSpaces Administration Guide_.
