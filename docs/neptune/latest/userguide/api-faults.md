# Neptune Exceptions Specific to Individual APIs

**Exceptions:**

- [AuthorizationAlreadyExistsFault (structure)](#AuthorizationAlreadyExistsFault "#AuthorizationAlreadyExistsFault")
- [AuthorizationNotFoundFault (structure)](#AuthorizationNotFoundFault "#AuthorizationNotFoundFault")
- [AuthorizationQuotaExceededFault (structure)](#AuthorizationQuotaExceededFault "#AuthorizationQuotaExceededFault")
- [CertificateNotFoundFault (structure)](#CertificateNotFoundFault "#CertificateNotFoundFault")
- [DBClusterAlreadyExistsFault (structure)](#DBClusterAlreadyExistsFault "#DBClusterAlreadyExistsFault")
- [DBClusterNotFoundFault (structure)](#DBClusterNotFoundFault "#DBClusterNotFoundFault")
- [DBClusterParameterGroupNotFoundFault (structure)](#DBClusterParameterGroupNotFoundFault "#DBClusterParameterGroupNotFoundFault")
- [DBClusterQuotaExceededFault (structure)](#DBClusterQuotaExceededFault "#DBClusterQuotaExceededFault")
- [DBClusterRoleAlreadyExistsFault (structure)](#DBClusterRoleAlreadyExistsFault "#DBClusterRoleAlreadyExistsFault")
- [DBClusterRoleNotFoundFault (structure)](#DBClusterRoleNotFoundFault "#DBClusterRoleNotFoundFault")
- [DBClusterRoleQuotaExceededFault (structure)](#DBClusterRoleQuotaExceededFault "#DBClusterRoleQuotaExceededFault")
- [DBClusterSnapshotAlreadyExistsFault (structure)](#DBClusterSnapshotAlreadyExistsFault "#DBClusterSnapshotAlreadyExistsFault")
- [DBClusterSnapshotNotFoundFault (structure)](#DBClusterSnapshotNotFoundFault "#DBClusterSnapshotNotFoundFault")
- [DBInstanceAlreadyExistsFault (structure)](#DBInstanceAlreadyExistsFault "#DBInstanceAlreadyExistsFault")
- [DBInstanceNotFoundFault (structure)](#DBInstanceNotFoundFault "#DBInstanceNotFoundFault")
- [DBLogFileNotFoundFault (structure)](#DBLogFileNotFoundFault "#DBLogFileNotFoundFault")
- [DBParameterGroupAlreadyExistsFault (structure)](#DBParameterGroupAlreadyExistsFault "#DBParameterGroupAlreadyExistsFault")
- [DBParameterGroupNotFoundFault (structure)](#DBParameterGroupNotFoundFault "#DBParameterGroupNotFoundFault")
- [DBParameterGroupQuotaExceededFault (structure)](#DBParameterGroupQuotaExceededFault "#DBParameterGroupQuotaExceededFault")
- [DBSecurityGroupAlreadyExistsFault (structure)](#DBSecurityGroupAlreadyExistsFault "#DBSecurityGroupAlreadyExistsFault")
- [DBSecurityGroupNotFoundFault (structure)](#DBSecurityGroupNotFoundFault "#DBSecurityGroupNotFoundFault")
- [DBSecurityGroupNotSupportedFault (structure)](#DBSecurityGroupNotSupportedFault "#DBSecurityGroupNotSupportedFault")
- [DBSecurityGroupQuotaExceededFault (structure)](#DBSecurityGroupQuotaExceededFault "#DBSecurityGroupQuotaExceededFault")
- [DBSnapshotAlreadyExistsFault (structure)](#DBSnapshotAlreadyExistsFault "#DBSnapshotAlreadyExistsFault")
- [DBSnapshotNotFoundFault (structure)](#DBSnapshotNotFoundFault "#DBSnapshotNotFoundFault")
- [DBSubnetGroupAlreadyExistsFault (structure)](#DBSubnetGroupAlreadyExistsFault "#DBSubnetGroupAlreadyExistsFault")
- [DBSubnetGroupDoesNotCoverEnoughAZs (structure)](#DBSubnetGroupDoesNotCoverEnoughAZs "#DBSubnetGroupDoesNotCoverEnoughAZs")
- [DBSubnetGroupNotAllowedFault (structure)](#DBSubnetGroupNotAllowedFault "#DBSubnetGroupNotAllowedFault")
- [DBSubnetGroupNotFoundFault (structure)](#DBSubnetGroupNotFoundFault "#DBSubnetGroupNotFoundFault")
- [DBSubnetGroupQuotaExceededFault (structure)](#DBSubnetGroupQuotaExceededFault "#DBSubnetGroupQuotaExceededFault")
- [DBSubnetQuotaExceededFault (structure)](#DBSubnetQuotaExceededFault "#DBSubnetQuotaExceededFault")
- [DBUpgradeDependencyFailureFault (structure)](#DBUpgradeDependencyFailureFault "#DBUpgradeDependencyFailureFault")
- [DomainNotFoundFault (structure)](#DomainNotFoundFault "#DomainNotFoundFault")
- [EventSubscriptionQuotaExceededFault (structure)](#EventSubscriptionQuotaExceededFault "#EventSubscriptionQuotaExceededFault")
- [GlobalClusterAlreadyExistsFault (structure)](#GlobalClusterAlreadyExistsFault "#GlobalClusterAlreadyExistsFault")
- [GlobalClusterNotFoundFault (structure)](#GlobalClusterNotFoundFault "#GlobalClusterNotFoundFault")
- [GlobalClusterQuotaExceededFault (structure)](#GlobalClusterQuotaExceededFault "#GlobalClusterQuotaExceededFault")
- [InstanceQuotaExceededFault (structure)](#InstanceQuotaExceededFault "#InstanceQuotaExceededFault")
- [InsufficientDBClusterCapacityFault (structure)](#InsufficientDBClusterCapacityFault "#InsufficientDBClusterCapacityFault")
- [InsufficientDBInstanceCapacityFault (structure)](#InsufficientDBInstanceCapacityFault "#InsufficientDBInstanceCapacityFault")
- [InsufficientStorageClusterCapacityFault (structure)](#InsufficientStorageClusterCapacityFault "#InsufficientStorageClusterCapacityFault")
- [InvalidDBClusterEndpointStateFault (structure)](#InvalidDBClusterEndpointStateFault "#InvalidDBClusterEndpointStateFault")
- [InvalidDBClusterSnapshotStateFault (structure)](#InvalidDBClusterSnapshotStateFault "#InvalidDBClusterSnapshotStateFault")
- [InvalidDBClusterStateFault (structure)](#InvalidDBClusterStateFault "#InvalidDBClusterStateFault")
- [InvalidDBInstanceStateFault (structure)](#InvalidDBInstanceStateFault "#InvalidDBInstanceStateFault")
- [InvalidDBParameterGroupStateFault (structure)](#InvalidDBParameterGroupStateFault "#InvalidDBParameterGroupStateFault")
- [InvalidDBSecurityGroupStateFault (structure)](#InvalidDBSecurityGroupStateFault "#InvalidDBSecurityGroupStateFault")
- [InvalidDBSnapshotStateFault (structure)](#InvalidDBSnapshotStateFault "#InvalidDBSnapshotStateFault")
- [InvalidDBSubnetGroupFault (structure)](#InvalidDBSubnetGroupFault "#InvalidDBSubnetGroupFault")
- [InvalidDBSubnetGroupStateFault (structure)](#InvalidDBSubnetGroupStateFault "#InvalidDBSubnetGroupStateFault")
- [InvalidDBSubnetStateFault (structure)](#InvalidDBSubnetStateFault "#InvalidDBSubnetStateFault")
- [InvalidEventSubscriptionStateFault (structure)](#InvalidEventSubscriptionStateFault "#InvalidEventSubscriptionStateFault")
- [InvalidGlobalClusterStateFault (structure)](#InvalidGlobalClusterStateFault "#InvalidGlobalClusterStateFault")
- [InvalidOptionGroupStateFault (structure)](#InvalidOptionGroupStateFault "#InvalidOptionGroupStateFault")
- [InvalidRestoreFault (structure)](#InvalidRestoreFault "#InvalidRestoreFault")
- [InvalidSubnet (structure)](#InvalidSubnet "#InvalidSubnet")
- [InvalidVPCNetworkStateFault (structure)](#InvalidVPCNetworkStateFault "#InvalidVPCNetworkStateFault")
- [KMSKeyNotAccessibleFault (structure)](#KMSKeyNotAccessibleFault "#KMSKeyNotAccessibleFault")
- [OptionGroupNotFoundFault (structure)](#OptionGroupNotFoundFault "#OptionGroupNotFoundFault")
- [PointInTimeRestoreNotEnabledFault (structure)](#PointInTimeRestoreNotEnabledFault "#PointInTimeRestoreNotEnabledFault")
- [ProvisionedIopsNotAvailableInAZFault (structure)](#ProvisionedIopsNotAvailableInAZFault "#ProvisionedIopsNotAvailableInAZFault")
- [ResourceNotFoundFault (structure)](#ResourceNotFoundFault "#ResourceNotFoundFault")
- [SNSInvalidTopicFault (structure)](#SNSInvalidTopicFault "#SNSInvalidTopicFault")
- [SNSNoAuthorizationFault (structure)](#SNSNoAuthorizationFault "#SNSNoAuthorizationFault")
- [SNSTopicArnNotFoundFault (structure)](#SNSTopicArnNotFoundFault "#SNSTopicArnNotFoundFault")
- [SharedSnapshotQuotaExceededFault (structure)](#SharedSnapshotQuotaExceededFault "#SharedSnapshotQuotaExceededFault")
- [SnapshotQuotaExceededFault (structure)](#SnapshotQuotaExceededFault "#SnapshotQuotaExceededFault")
- [SourceNotFoundFault (structure)](#SourceNotFoundFault "#SourceNotFoundFault")
- [StorageQuotaExceededFault (structure)](#StorageQuotaExceededFault "#StorageQuotaExceededFault")
- [StorageTypeNotSupportedFault (structure)](#StorageTypeNotSupportedFault "#StorageTypeNotSupportedFault")
- [SubnetAlreadyInUse (structure)](#SubnetAlreadyInUse "#SubnetAlreadyInUse")
- [SubscriptionAlreadyExistFault (structure)](#SubscriptionAlreadyExistFault "#SubscriptionAlreadyExistFault")
- [SubscriptionCategoryNotFoundFault (structure)](#SubscriptionCategoryNotFoundFault "#SubscriptionCategoryNotFoundFault")
- [SubscriptionNotFoundFault (structure)](#SubscriptionNotFoundFault "#SubscriptionNotFoundFault")

## AuthorizationAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

The specified CIDRIP or EC2 security group is already authorized for the
specified DB security group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## AuthorizationNotFoundFault (structure)

**HTTP status code returned:** 404.

Specified CIDRIP or EC2 security group is not authorized for the specified
DB security group.

Neptune may not also be authorized via IAM to perform necessary actions
on your behalf.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## AuthorizationQuotaExceededFault (structure)

**HTTP status code returned:** 400.

DB security group authorization quota has been reached.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## CertificateNotFoundFault (structure)

**HTTP status code returned:** 404.

_CertificateIdentifier_ does not refer to an existing
certificate.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

User already has a DB cluster with the given identifier.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBClusterIdentifier_ does not refer to an existing
DB cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterParameterGroupNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBClusterParameterGroupName_ does not refer
to an existing DB Cluster parameter group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterQuotaExceededFault (structure)

**HTTP status code returned:** 403.

User attempted to create a new DB cluster and the user has already reached
the maximum allowed DB cluster quota.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterRoleAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

The specified IAM role Amazon Resource Name (ARN) is already associated
with the specified DB cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterRoleNotFoundFault (structure)

**HTTP status code returned:** 404.

The specified IAM role Amazon Resource Name (ARN) is not associated with
the specified DB cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterRoleQuotaExceededFault (structure)

**HTTP status code returned:** 400.

You have exceeded the maximum number of IAM roles that can be associated
with the specified DB cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterSnapshotAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

User already has a DB cluster snapshot with the given identifier.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBClusterSnapshotNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBClusterSnapshotIdentifier_ does not refer
to an existing DB cluster snapshot.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBInstanceAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

User already has a DB instance with the given identifier.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBInstanceNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBInstanceIdentifier_ does not refer to an existing
DB instance.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBLogFileNotFoundFault (structure)

**HTTP status code returned:** 404.

_LogFileName_ does not refer to an existing DB log
file.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBParameterGroupAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

A DB parameter group with the same name exists.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBParameterGroupNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBParameterGroupName_ does not refer to an existing
DB parameter group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBParameterGroupQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of DB parameter
groups.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSecurityGroupAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

A DB security group with the name specified in _DBSecurityGroupName_
already exists.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSecurityGroupNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBSecurityGroupName_ does not refer to an existing
DB security group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSecurityGroupNotSupportedFault (structure)

**HTTP status code returned:** 400.

A DB security group is not allowed for this action.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSecurityGroupQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of DB security
groups.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSnapshotAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

_DBSnapshotIdentifier_ is already used by an existing
snapshot.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSnapshotNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBSnapshotIdentifier_ does not refer to an existing
DB snapshot.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetGroupAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

_DBSubnetGroupName_ is already used by an existing
DB subnet group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetGroupDoesNotCoverEnoughAZs (structure)

**HTTP status code returned:** 400.

Subnets in the DB subnet group should cover at least two Availability Zones
unless there is only one Availability Zone.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetGroupNotAllowedFault (structure)

**HTTP status code returned:** 400.

Indicates that the DBSubnetGroup should not be specified while creating
read replicas that lie in the same region as the source instance.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetGroupNotFoundFault (structure)

**HTTP status code returned:** 404.

_DBSubnetGroupName_ does not refer to an existing
DB subnet group.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetGroupQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of DB subnet
groups.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBSubnetQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of subnets in
a DB subnet groups.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DBUpgradeDependencyFailureFault (structure)

**HTTP status code returned:** 400.

The DB upgrade failed because a resource the DB depends on could not be modified.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## DomainNotFoundFault (structure)

**HTTP status code returned:** 404.

_Domain_ does not refer to an existing Active Directory
Domain.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## EventSubscriptionQuotaExceededFault (structure)

**HTTP status code returned:** 400.

You have exceeded the number of events you can subscribe to.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## GlobalClusterAlreadyExistsFault (structure)

**HTTP status code returned:** 400.

The `GlobalClusterIdentifier` already exists. Choose a new global database identifier (unique name) to create a new global database cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## GlobalClusterNotFoundFault (structure)

**HTTP status code returned:** 404.

The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## GlobalClusterQuotaExceededFault (structure)

**HTTP status code returned:** 400.

The number of global database clusters for this account is already at the
maximum allowed.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InstanceQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of DB instances.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InsufficientDBClusterCapacityFault (structure)

**HTTP status code returned:** 403.

The DB cluster does not have enough capacity for the current operation.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InsufficientDBInstanceCapacityFault (structure)

**HTTP status code returned:** 400.

Specified DB instance class is not available in the specified Availability
Zone.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InsufficientStorageClusterCapacityFault (structure)

**HTTP status code returned:** 400.

There is insufficient storage available for the current action. You may
be able to resolve this error by updating your subnet group to use different Availability
Zones that have more storage available.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBClusterEndpointStateFault (structure)

**HTTP status code returned:** 400.

The requested operation cannot be performed on the endpoint while the
endpoint is in this state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBClusterSnapshotStateFault (structure)

**HTTP status code returned:** 400.

The supplied value is not a valid DB cluster snapshot state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBClusterStateFault (structure)

**HTTP status code returned:** 400.

The DB cluster is not in a valid state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBInstanceStateFault (structure)

**HTTP status code returned:** 400.

The specified DB instance is not in the _available_
state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBParameterGroupStateFault (structure)

**HTTP status code returned:** 400.

The DB parameter group is in use or is in an invalid state. If you are attempting
to delete the parameter group, you cannot delete it when the parameter group is
in this state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBSecurityGroupStateFault (structure)

**HTTP status code returned:** 400.

The state of the DB security group does not allow deletion.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBSnapshotStateFault (structure)

**HTTP status code returned:** 400.

The state of the DB snapshot does not allow deletion.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBSubnetGroupFault (structure)

**HTTP status code returned:** 400.

Indicates the DBSubnetGroup does not belong to the same VPC as that of an
existing cross region read replica of the same source instance.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBSubnetGroupStateFault (structure)

**HTTP status code returned:** 400.

The DB subnet group cannot be deleted because it is in use.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidDBSubnetStateFault (structure)

**HTTP status code returned:** 400.

The DB subnet is not in the _available_ state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidEventSubscriptionStateFault (structure)

**HTTP status code returned:** 400.

The event subscription is in an invalid state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidGlobalClusterStateFault (structure)

**HTTP status code returned:** 400.

The global cluster is in an invalid state and can't perform the requested
operation.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidOptionGroupStateFault (structure)

**HTTP status code returned:** 400.

The option group is not in the _available_ state.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidRestoreFault (structure)

**HTTP status code returned:** 400.

Cannot restore from vpc backup to non-vpc DB instance.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidSubnet (structure)

**HTTP status code returned:** 400.

The requested subnet is invalid, or multiple subnets were requested that
are not all in a common VPC.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## InvalidVPCNetworkStateFault (structure)

**HTTP status code returned:** 400.

DB subnet group does not cover all Availability Zones after it is created
because users' change.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## KMSKeyNotAccessibleFault (structure)

**HTTP status code returned:** 400.

Error accessing KMS key.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## OptionGroupNotFoundFault (structure)

**HTTP status code returned:** 404.

The designated option group could not be found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## PointInTimeRestoreNotEnabledFault (structure)

**HTTP status code returned:** 400.

_SourceDBInstanceIdentifier_ refers to a DB instance
with _BackupRetentionPeriod_ equal to 0.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## ProvisionedIopsNotAvailableInAZFault (structure)

**HTTP status code returned:** 400.

Provisioned IOPS not available in the specified Availability Zone.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## ResourceNotFoundFault (structure)

**HTTP status code returned:** 404.

The specified resource ID was not found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SNSInvalidTopicFault (structure)

**HTTP status code returned:** 400.

The SNS topic is invalid.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SNSNoAuthorizationFault (structure)

**HTTP status code returned:** 400.

There is no SNS authorization.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SNSTopicArnNotFoundFault (structure)

**HTTP status code returned:** 404.

The ARN of the SNS topic could not be found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SharedSnapshotQuotaExceededFault (structure)

**HTTP status code returned:** 400.

You have exceeded the maximum number of accounts that you can share a manual
DB snapshot with.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SnapshotQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed number of DB snapshots.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SourceNotFoundFault (structure)

**HTTP status code returned:** 404.

The source could not be found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## StorageQuotaExceededFault (structure)

**HTTP status code returned:** 400.

Request would result in user exceeding the allowed amount of storage available
across all DB instances.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## StorageTypeNotSupportedFault (structure)

**HTTP status code returned:** 400.

_StorageType_ specified cannot be associated
with the DB Instance.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SubnetAlreadyInUse (structure)

**HTTP status code returned:** 400.

The DB subnet is already in use in the Availability Zone.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SubscriptionAlreadyExistFault (structure)

**HTTP status code returned:** 400.

This subscription already exists.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SubscriptionCategoryNotFoundFault (structure)

**HTTP status code returned:** 404.

The designated subscription category could not be found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.

## SubscriptionNotFoundFault (structure)

**HTTP status code returned:** 404.

The designated subscription could not be found.

###### Fields

- **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

A message describing the details of the problem.
