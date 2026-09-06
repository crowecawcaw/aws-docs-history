

# Security Hub CSPM controls for WorkSpaces
<a name="workspaces-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon WorkSpaces service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [WorkSpaces.1] WorkSpaces user volumes should be encrypted at rest
<a name="workspaces-1"></a>

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::WorkSpaces::Workspace`

**AWS Config rule:** [`workspaces-user-volume-encryption-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/workspaces-user-volume-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a user volume in an Amazon WorkSpaces WorkSpace is encrypted at rest. The control fails if the WorkSpace user volume isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation
<a name="workspaces-1-remediation"></a>

To encrypt a WorkSpaces user volume, see [ Encrypt a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html#encrypt_workspace) in the *Amazon WorkSpaces Administration Guide*.

## [WorkSpaces.2] WorkSpaces root volumes should be encrypted at rest
<a name="workspaces-2"></a>

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::WorkSpaces::Workspace`

**AWS Config rule:** [`workspaces-root-volume-encryption-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/workspaces-root-volume-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a root volume in an Amazon WorkSpaces WorkSpace is encrypted at rest. The control fails if the WorkSpace root volume isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation
<a name="workspaces-2-remediation"></a>

To encrypt a WorkSpaces root volume, see [ Encrypt a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html#encrypt_workspace) in the *Amazon WorkSpaces Administration Guide*.