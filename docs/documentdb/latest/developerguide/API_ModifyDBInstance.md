# ModifyDBInstance

Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBInstanceIdentifier**

The instance identifier. This value is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing `DBInstance`.

Type: String

Required: Yes

**ApplyImmediately**

Specifies whether the modifications in this request and any pending modifications are
asynchronously applied as soon as possible, regardless of the
`PreferredMaintenanceWindow` setting for the instance.

If this parameter is set to `false`, changes to the instance are
applied during the next maintenance window. Some parameter changes can cause an outage
and are applied on the next reboot.

Default: `false`

Type: Boolean

Required: No

**AutoMinorVersionUpgrade**

This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.

Type: Boolean

Required: No

**CACertificateIdentifier**

Indicates the certificate that needs to be associated with the instance.

Type: String

Required: No

**CertificateRotationRestart**

Specifies whether the DB instance is restarted when you rotate your
SSL/TLS certificate.

By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate
is not updated until the DB instance is restarted.

###### Important

Set this parameter only if you are _not_ using SSL/TLS to connect to the DB instance.

If you are using SSL/TLS to connect to the DB instance, see [Updating Your Amazon DocumentDB TLS
Certificates](ca_cert_rotation.md "ca_cert_rotation.md") and
[Encrypting Data in Transit](security.encryption.md "security.encryption.md") in the _Amazon DocumentDB Developer
Guide_.

Type: Boolean

Required: No

**CopyTagsToSnapshot**

A value that indicates whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.

Type: Boolean

Required: No

**DBInstanceClass**

The new compute and memory capacity of the instance; for example, `db.r5.large`. Not all instance classes are available in all AWS Regions.

If you modify the instance class, an outage occurs during the change. The change is
applied during the next maintenance window, unless `ApplyImmediately` is
specified as `true` for this request.

Default: Uses existing setting.

Type: String

Required: No

**EnablePerformanceInsights**

A value that indicates whether to enable Performance Insights for the DB Instance. For
more information, see [Using Amazon
Performance Insights](performance-insights.md "performance-insights.md").

Type: Boolean

Required: No

**NewDBInstanceIdentifier**

The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set `Apply Immediately` to `true`. It occurs during the next maintenance window if you set `Apply Immediately` to `false`. This value is stored as a lowercase string.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

Type: String

Required: No

**PerformanceInsightsKMSKeyId**

The AWS KMS key identifier for encryption of Performance Insights
data.

The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name
for the KMS key.

If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your
default KMS key. There is a default KMS key for your
Amazon Web Services account. Your Amazon Web Services account has a different
default KMS key for each Amazon Web Services region.

Type: String

Required: No

**PreferredMaintenanceWindow**

The weekly time range (in UTC) during which system maintenance can occur, which might
result in an outage. Changing this parameter doesn't result in an outage except in the
following situation, and the change is asynchronously applied as soon as possible. If
there are pending actions that cause a reboot, and the maintenance window is changed to
include the current time, changing this parameter causes a reboot of the instance. If
you are moving this window to the current time, there must be at least 30 minutes
between the current time and end of the window to ensure that pending changes are
applied.

Default: Uses existing setting.

Format: `ddd:hh24:mi-ddd:hh24:mi`

Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

Constraints: Must be at least 30 minutes.

Type: String

Required: No

**PromotionTier**

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

Default: 1

Valid values: 0-15

Type: Integer

Required: No

## Response Elements

The following element is returned by the service.

**DBInstance**

Detailed information about an instance.

Type: [DBInstance](API_DBInstance.md "API_DBInstance.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AuthorizationNotFound**

The specified CIDR IP or Amazon EC2 security group isn't authorized for the specified security group.

Amazon DocumentDB also might not be authorized to perform necessary actions on your behalf using IAM.

HTTP Status Code: 404

**CertificateNotFound**

`CertificateIdentifier` doesn't refer to an existing certificate.

HTTP Status Code: 404

**DBInstanceAlreadyExists**

You already have a instance with the given identifier.

HTTP Status Code: 400

**DBInstanceNotFound**

`DBInstanceIdentifier` doesn't refer to an existing instance.

HTTP Status Code: 404

**DBParameterGroupNotFound**

`DBParameterGroupName` doesn't refer to an existing parameter group.

HTTP Status Code: 404

**DBSecurityGroupNotFound**

`DBSecurityGroupName` doesn't refer to an existing security group.

HTTP Status Code: 404

**DBUpgradeDependencyFailure**

The upgrade failed because a resource that the depends on can't be
modified.

HTTP Status Code: 400

**InsufficientDBInstanceCapacity**

The specified instance class isn't available in the specified Availability Zone.

HTTP Status Code: 400

**InvalidDBInstanceState**

The specified instance isn't in the _available_ state.

HTTP Status Code: 400

**InvalidDBSecurityGroupState**

The state of the security group doesn't allow deletion.

HTTP Status Code: 400

**InvalidVPCNetworkStateFault**

The subnet group doesn't cover all Availability Zones after it is created
because of changes that were made.

HTTP Status Code: 400

**StorageQuotaExceeded**

The request would cause you to exceed the allowed amount of storage available across
all instances.

HTTP Status Code: 400

**StorageTypeNotSupported**

Storage of the specified `StorageType` can't be associated with the DB
instance.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/cli2/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForCpp/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/boto3/docdb-2014-10-31/ModifyDBInstance.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBInstance.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBInstance.md")
