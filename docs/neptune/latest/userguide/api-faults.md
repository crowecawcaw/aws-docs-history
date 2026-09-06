

# Neptune Exceptions Specific to Individual APIs
<a name="api-faults"></a>

**Exceptions:**
+ [AuthorizationAlreadyExistsFault (structure)](#AuthorizationAlreadyExistsFault)
+ [AuthorizationNotFoundFault (structure)](#AuthorizationNotFoundFault)
+ [AuthorizationQuotaExceededFault (structure)](#AuthorizationQuotaExceededFault)
+ [CertificateNotFoundFault (structure)](#CertificateNotFoundFault)
+ [DBClusterAlreadyExistsFault (structure)](#DBClusterAlreadyExistsFault)
+ [DBClusterNotFoundFault (structure)](#DBClusterNotFoundFault)
+ [DBClusterParameterGroupNotFoundFault (structure)](#DBClusterParameterGroupNotFoundFault)
+ [DBClusterQuotaExceededFault (structure)](#DBClusterQuotaExceededFault)
+ [DBClusterRoleAlreadyExistsFault (structure)](#DBClusterRoleAlreadyExistsFault)
+ [DBClusterRoleNotFoundFault (structure)](#DBClusterRoleNotFoundFault)
+ [DBClusterRoleQuotaExceededFault (structure)](#DBClusterRoleQuotaExceededFault)
+ [DBClusterSnapshotAlreadyExistsFault (structure)](#DBClusterSnapshotAlreadyExistsFault)
+ [DBClusterSnapshotNotFoundFault (structure)](#DBClusterSnapshotNotFoundFault)
+ [DBInstanceAlreadyExistsFault (structure)](#DBInstanceAlreadyExistsFault)
+ [DBInstanceNotFoundFault (structure)](#DBInstanceNotFoundFault)
+ [DBLogFileNotFoundFault (structure)](#DBLogFileNotFoundFault)
+ [DBParameterGroupAlreadyExistsFault (structure)](#DBParameterGroupAlreadyExistsFault)
+ [DBParameterGroupNotFoundFault (structure)](#DBParameterGroupNotFoundFault)
+ [DBParameterGroupQuotaExceededFault (structure)](#DBParameterGroupQuotaExceededFault)
+ [DBSecurityGroupAlreadyExistsFault (structure)](#DBSecurityGroupAlreadyExistsFault)
+ [DBSecurityGroupNotFoundFault (structure)](#DBSecurityGroupNotFoundFault)
+ [DBSecurityGroupNotSupportedFault (structure)](#DBSecurityGroupNotSupportedFault)
+ [DBSecurityGroupQuotaExceededFault (structure)](#DBSecurityGroupQuotaExceededFault)
+ [DBSnapshotAlreadyExistsFault (structure)](#DBSnapshotAlreadyExistsFault)
+ [DBSnapshotNotFoundFault (structure)](#DBSnapshotNotFoundFault)
+ [DBSubnetGroupAlreadyExistsFault (structure)](#DBSubnetGroupAlreadyExistsFault)
+ [DBSubnetGroupDoesNotCoverEnoughAZs (structure)](#DBSubnetGroupDoesNotCoverEnoughAZs)
+ [DBSubnetGroupNotAllowedFault (structure)](#DBSubnetGroupNotAllowedFault)
+ [DBSubnetGroupNotFoundFault (structure)](#DBSubnetGroupNotFoundFault)
+ [DBSubnetGroupQuotaExceededFault (structure)](#DBSubnetGroupQuotaExceededFault)
+ [DBSubnetQuotaExceededFault (structure)](#DBSubnetQuotaExceededFault)
+ [DBUpgradeDependencyFailureFault (structure)](#DBUpgradeDependencyFailureFault)
+ [DomainNotFoundFault (structure)](#DomainNotFoundFault)
+ [EventSubscriptionQuotaExceededFault (structure)](#EventSubscriptionQuotaExceededFault)
+ [GlobalClusterAlreadyExistsFault (structure)](#GlobalClusterAlreadyExistsFault)
+ [GlobalClusterNotFoundFault (structure)](#GlobalClusterNotFoundFault)
+ [GlobalClusterQuotaExceededFault (structure)](#GlobalClusterQuotaExceededFault)
+ [InstanceQuotaExceededFault (structure)](#InstanceQuotaExceededFault)
+ [InsufficientDBClusterCapacityFault (structure)](#InsufficientDBClusterCapacityFault)
+ [InsufficientDBInstanceCapacityFault (structure)](#InsufficientDBInstanceCapacityFault)
+ [InsufficientStorageClusterCapacityFault (structure)](#InsufficientStorageClusterCapacityFault)
+ [InvalidDBClusterEndpointStateFault (structure)](#InvalidDBClusterEndpointStateFault)
+ [InvalidDBClusterSnapshotStateFault (structure)](#InvalidDBClusterSnapshotStateFault)
+ [InvalidDBClusterStateFault (structure)](#InvalidDBClusterStateFault)
+ [InvalidDBInstanceStateFault (structure)](#InvalidDBInstanceStateFault)
+ [InvalidDBParameterGroupStateFault (structure)](#InvalidDBParameterGroupStateFault)
+ [InvalidDBSecurityGroupStateFault (structure)](#InvalidDBSecurityGroupStateFault)
+ [InvalidDBSnapshotStateFault (structure)](#InvalidDBSnapshotStateFault)
+ [InvalidDBSubnetGroupFault (structure)](#InvalidDBSubnetGroupFault)
+ [InvalidDBSubnetGroupStateFault (structure)](#InvalidDBSubnetGroupStateFault)
+ [InvalidDBSubnetStateFault (structure)](#InvalidDBSubnetStateFault)
+ [InvalidEventSubscriptionStateFault (structure)](#InvalidEventSubscriptionStateFault)
+ [InvalidGlobalClusterStateFault (structure)](#InvalidGlobalClusterStateFault)
+ [InvalidOptionGroupStateFault (structure)](#InvalidOptionGroupStateFault)
+ [InvalidRestoreFault (structure)](#InvalidRestoreFault)
+ [InvalidSubnet (structure)](#InvalidSubnet)
+ [InvalidVPCNetworkStateFault (structure)](#InvalidVPCNetworkStateFault)
+ [KMSKeyNotAccessibleFault (structure)](#KMSKeyNotAccessibleFault)
+ [OptionGroupNotFoundFault (structure)](#OptionGroupNotFoundFault)
+ [PointInTimeRestoreNotEnabledFault (structure)](#PointInTimeRestoreNotEnabledFault)
+ [ProvisionedIopsNotAvailableInAZFault (structure)](#ProvisionedIopsNotAvailableInAZFault)
+ [ResourceNotFoundFault (structure)](#ResourceNotFoundFault)
+ [SNSInvalidTopicFault (structure)](#SNSInvalidTopicFault)
+ [SNSNoAuthorizationFault (structure)](#SNSNoAuthorizationFault)
+ [SNSTopicArnNotFoundFault (structure)](#SNSTopicArnNotFoundFault)
+ [SharedSnapshotQuotaExceededFault (structure)](#SharedSnapshotQuotaExceededFault)
+ [SnapshotQuotaExceededFault (structure)](#SnapshotQuotaExceededFault)
+ [SourceNotFoundFault (structure)](#SourceNotFoundFault)
+ [StorageQuotaExceededFault (structure)](#StorageQuotaExceededFault)
+ [StorageTypeNotSupportedFault (structure)](#StorageTypeNotSupportedFault)
+ [SubnetAlreadyInUse (structure)](#SubnetAlreadyInUse)
+ [SubscriptionAlreadyExistFault (structure)](#SubscriptionAlreadyExistFault)
+ [SubscriptionCategoryNotFoundFault (structure)](#SubscriptionCategoryNotFoundFault)
+ [SubscriptionNotFoundFault (structure)](#SubscriptionNotFoundFault)

## AuthorizationAlreadyExistsFault (structure)
<a name="AuthorizationAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

The specified CIDRIP or EC2 security group is already authorized for the specified DB security group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## AuthorizationNotFoundFault (structure)
<a name="AuthorizationNotFoundFault"></a>

**HTTP status code returned:  ** 404.

Specified CIDRIP or EC2 security group is not authorized for the specified DB security group.

Neptune may not also be authorized via IAM to perform necessary actions on your behalf.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## AuthorizationQuotaExceededFault (structure)
<a name="AuthorizationQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

DB security group authorization quota has been reached.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## CertificateNotFoundFault (structure)
<a name="CertificateNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*CertificateIdentifier* does not refer to an existing certificate.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterAlreadyExistsFault (structure)
<a name="DBClusterAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

User already has a DB cluster with the given identifier.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterNotFoundFault (structure)
<a name="DBClusterNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBClusterIdentifier* does not refer to an existing DB cluster.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterParameterGroupNotFoundFault (structure)
<a name="DBClusterParameterGroupNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBClusterParameterGroupName* does not refer to an existing DB Cluster parameter group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterQuotaExceededFault (structure)
<a name="DBClusterQuotaExceededFault"></a>

**HTTP status code returned:  ** 403.

User attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterRoleAlreadyExistsFault (structure)
<a name="DBClusterRoleAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

The specified IAM role Amazon Resource Name (ARN) is already associated with the specified DB cluster.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterRoleNotFoundFault (structure)
<a name="DBClusterRoleNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The specified IAM role Amazon Resource Name (ARN) is not associated with the specified DB cluster.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterRoleQuotaExceededFault (structure)
<a name="DBClusterRoleQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

You have exceeded the maximum number of IAM roles that can be associated with the specified DB cluster.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterSnapshotAlreadyExistsFault (structure)
<a name="DBClusterSnapshotAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

User already has a DB cluster snapshot with the given identifier.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBClusterSnapshotNotFoundFault (structure)
<a name="DBClusterSnapshotNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBInstanceAlreadyExistsFault (structure)
<a name="DBInstanceAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

User already has a DB instance with the given identifier.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBInstanceNotFoundFault (structure)
<a name="DBInstanceNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBInstanceIdentifier* does not refer to an existing DB instance.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBLogFileNotFoundFault (structure)
<a name="DBLogFileNotFoundFault"></a>

**HTTP status code returned:  ** 404.

 *LogFileName* does not refer to an existing DB log file.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBParameterGroupAlreadyExistsFault (structure)
<a name="DBParameterGroupAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

A DB parameter group with the same name exists.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBParameterGroupNotFoundFault (structure)
<a name="DBParameterGroupNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBParameterGroupName* does not refer to an existing DB parameter group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBParameterGroupQuotaExceededFault (structure)
<a name="DBParameterGroupQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of DB parameter groups.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSecurityGroupAlreadyExistsFault (structure)
<a name="DBSecurityGroupAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

A DB security group with the name specified in *DBSecurityGroupName* already exists.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSecurityGroupNotFoundFault (structure)
<a name="DBSecurityGroupNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBSecurityGroupName* does not refer to an existing DB security group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSecurityGroupNotSupportedFault (structure)
<a name="DBSecurityGroupNotSupportedFault"></a>

**HTTP status code returned:  ** 400.

A DB security group is not allowed for this action.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSecurityGroupQuotaExceededFault (structure)
<a name="DBSecurityGroupQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of DB security groups.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSnapshotAlreadyExistsFault (structure)
<a name="DBSnapshotAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

*DBSnapshotIdentifier* is already used by an existing snapshot.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSnapshotNotFoundFault (structure)
<a name="DBSnapshotNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBSnapshotIdentifier* does not refer to an existing DB snapshot.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetGroupAlreadyExistsFault (structure)
<a name="DBSubnetGroupAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

*DBSubnetGroupName* is already used by an existing DB subnet group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetGroupDoesNotCoverEnoughAZs (structure)
<a name="DBSubnetGroupDoesNotCoverEnoughAZs"></a>

**HTTP status code returned:  ** 400.

Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetGroupNotAllowedFault (structure)
<a name="DBSubnetGroupNotAllowedFault"></a>

**HTTP status code returned:  ** 400.

Indicates that the DBSubnetGroup should not be specified while creating read replicas that lie in the same region as the source instance.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetGroupNotFoundFault (structure)
<a name="DBSubnetGroupNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*DBSubnetGroupName* does not refer to an existing DB subnet group.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetGroupQuotaExceededFault (structure)
<a name="DBSubnetGroupQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of DB subnet groups.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBSubnetQuotaExceededFault (structure)
<a name="DBSubnetQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of subnets in a DB subnet groups.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DBUpgradeDependencyFailureFault (structure)
<a name="DBUpgradeDependencyFailureFault"></a>

**HTTP status code returned:  ** 400.

The DB upgrade failed because a resource the DB depends on could not be modified.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## DomainNotFoundFault (structure)
<a name="DomainNotFoundFault"></a>

**HTTP status code returned:  ** 404.

*Domain* does not refer to an existing Active Directory Domain.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## EventSubscriptionQuotaExceededFault (structure)
<a name="EventSubscriptionQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

You have exceeded the number of events you can subscribe to.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## GlobalClusterAlreadyExistsFault (structure)
<a name="GlobalClusterAlreadyExistsFault"></a>

**HTTP status code returned:  ** 400.

The `GlobalClusterIdentifier` already exists. Choose a new global database identifier (unique name) to create a new global database cluster.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## GlobalClusterNotFoundFault (structure)
<a name="GlobalClusterNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster. 

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## GlobalClusterQuotaExceededFault (structure)
<a name="GlobalClusterQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

The number of global database clusters for this account is already at the maximum allowed.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InstanceQuotaExceededFault (structure)
<a name="InstanceQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of DB instances.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InsufficientDBClusterCapacityFault (structure)
<a name="InsufficientDBClusterCapacityFault"></a>

**HTTP status code returned:  ** 403.

The DB cluster does not have enough capacity for the current operation.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InsufficientDBInstanceCapacityFault (structure)
<a name="InsufficientDBInstanceCapacityFault"></a>

**HTTP status code returned:  ** 400.

Specified DB instance class is not available in the specified Availability Zone.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InsufficientStorageClusterCapacityFault (structure)
<a name="InsufficientStorageClusterCapacityFault"></a>

**HTTP status code returned:  ** 400.

There is insufficient storage available for the current action. You may be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBClusterEndpointStateFault (structure)
<a name="InvalidDBClusterEndpointStateFault"></a>

**HTTP status code returned:  ** 400.

The requested operation cannot be performed on the endpoint while the endpoint is in this state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBClusterSnapshotStateFault (structure)
<a name="InvalidDBClusterSnapshotStateFault"></a>

**HTTP status code returned:  ** 400.

The supplied value is not a valid DB cluster snapshot state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBClusterStateFault (structure)
<a name="InvalidDBClusterStateFault"></a>

**HTTP status code returned:  ** 400.

The DB cluster is not in a valid state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBInstanceStateFault (structure)
<a name="InvalidDBInstanceStateFault"></a>

**HTTP status code returned:  ** 400.

The specified DB instance is not in the *available* state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBParameterGroupStateFault (structure)
<a name="InvalidDBParameterGroupStateFault"></a>

**HTTP status code returned:  ** 400.

The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBSecurityGroupStateFault (structure)
<a name="InvalidDBSecurityGroupStateFault"></a>

**HTTP status code returned:  ** 400.

The state of the DB security group does not allow deletion.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBSnapshotStateFault (structure)
<a name="InvalidDBSnapshotStateFault"></a>

**HTTP status code returned:  ** 400.

The state of the DB snapshot does not allow deletion.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBSubnetGroupFault (structure)
<a name="InvalidDBSubnetGroupFault"></a>

**HTTP status code returned:  ** 400.

Indicates the DBSubnetGroup does not belong to the same VPC as that of an existing cross region read replica of the same source instance.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBSubnetGroupStateFault (structure)
<a name="InvalidDBSubnetGroupStateFault"></a>

**HTTP status code returned:  ** 400.

The DB subnet group cannot be deleted because it is in use.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidDBSubnetStateFault (structure)
<a name="InvalidDBSubnetStateFault"></a>

**HTTP status code returned:  ** 400.

The DB subnet is not in the *available* state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidEventSubscriptionStateFault (structure)
<a name="InvalidEventSubscriptionStateFault"></a>

**HTTP status code returned:  ** 400.

The event subscription is in an invalid state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidGlobalClusterStateFault (structure)
<a name="InvalidGlobalClusterStateFault"></a>

**HTTP status code returned:  ** 400.

The global cluster is in an invalid state and can't perform the requested operation. 

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidOptionGroupStateFault (structure)
<a name="InvalidOptionGroupStateFault"></a>

**HTTP status code returned:  ** 400.

The option group is not in the *available* state.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidRestoreFault (structure)
<a name="InvalidRestoreFault"></a>

**HTTP status code returned:  ** 400.

Cannot restore from vpc backup to non-vpc DB instance.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidSubnet (structure)
<a name="InvalidSubnet"></a>

**HTTP status code returned:  ** 400.

The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## InvalidVPCNetworkStateFault (structure)
<a name="InvalidVPCNetworkStateFault"></a>

**HTTP status code returned:  ** 400.

DB subnet group does not cover all Availability Zones after it is created because users' change.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## KMSKeyNotAccessibleFault (structure)
<a name="KMSKeyNotAccessibleFault"></a>

**HTTP status code returned:  ** 400.

Error accessing KMS key.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## OptionGroupNotFoundFault (structure)
<a name="OptionGroupNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The designated option group could not be found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## PointInTimeRestoreNotEnabledFault (structure)
<a name="PointInTimeRestoreNotEnabledFault"></a>

**HTTP status code returned:  ** 400.

*SourceDBInstanceIdentifier* refers to a DB instance with *BackupRetentionPeriod* equal to 0.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## ProvisionedIopsNotAvailableInAZFault (structure)
<a name="ProvisionedIopsNotAvailableInAZFault"></a>

**HTTP status code returned:  ** 400.

Provisioned IOPS not available in the specified Availability Zone.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## ResourceNotFoundFault (structure)
<a name="ResourceNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The specified resource ID was not found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SNSInvalidTopicFault (structure)
<a name="SNSInvalidTopicFault"></a>

**HTTP status code returned:  ** 400.

The SNS topic is invalid.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SNSNoAuthorizationFault (structure)
<a name="SNSNoAuthorizationFault"></a>

**HTTP status code returned:  ** 400.

There is no SNS authorization.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SNSTopicArnNotFoundFault (structure)
<a name="SNSTopicArnNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The ARN of the SNS topic could not be found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SharedSnapshotQuotaExceededFault (structure)
<a name="SharedSnapshotQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

You have exceeded the maximum number of accounts that you can share a manual DB snapshot with.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SnapshotQuotaExceededFault (structure)
<a name="SnapshotQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed number of DB snapshots.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SourceNotFoundFault (structure)
<a name="SourceNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The source could not be found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## StorageQuotaExceededFault (structure)
<a name="StorageQuotaExceededFault"></a>

**HTTP status code returned:  ** 400.

Request would result in user exceeding the allowed amount of storage available across all DB instances.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## StorageTypeNotSupportedFault (structure)
<a name="StorageTypeNotSupportedFault"></a>

**HTTP status code returned:  ** 400.

*StorageType* specified cannot be associated with the DB Instance.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SubnetAlreadyInUse (structure)
<a name="SubnetAlreadyInUse"></a>

**HTTP status code returned:  ** 400.

The DB subnet is already in use in the Availability Zone.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SubscriptionAlreadyExistFault (structure)
<a name="SubscriptionAlreadyExistFault"></a>

**HTTP status code returned:  ** 400.

This subscription already exists.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SubscriptionCategoryNotFoundFault (structure)
<a name="SubscriptionCategoryNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The designated subscription category could not be found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.

## SubscriptionNotFoundFault (structure)
<a name="SubscriptionNotFoundFault"></a>

**HTTP status code returned:  ** 404.

The designated subscription could not be found.

**Fields**
+ **message** – This is an ExceptionMessage, of type: `string` (a UTF-8 encoded string).

  A message describing the details of the problem.