# DirectoryDescription

Contains information about an AWS Directory Service directory.

## Contents

**AccessUrl**

The access URL for the directory, such as
`http://<alias>.awsapps.com`. If no alias exists,
`<alias>` is the directory identifier, such as
`d-XXXXXXXXXX`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: No

**Alias**

The alias for the directory. If no alias exists, the alias is the directory identifier,
such as `d-XXXXXXXXXX`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 62.

Pattern: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`

Required: No

**ConnectSettings**

[DirectoryConnectSettingsDescription](API_DirectoryConnectSettingsDescription.md "API_DirectoryConnectSettingsDescription.md") object that contains additional
information about an AD Connector directory. Present only for AD Connector
directories.

Type: [DirectoryConnectSettingsDescription](API_DirectoryConnectSettingsDescription.md "API_DirectoryConnectSettingsDescription.md") object

Required: No

**Description**

The description for the directory.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**DesiredNumberOfDomainControllers**

The desired number of domain controllers in the directory if the directory is Microsoft
AD.

Type: Integer

Valid Range: Minimum value of 2.

Required: No

**DirectoryId**

The directory identifier.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**DnsIpAddrs**

The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers.
For an AD Connector directory, these are the IP addresses of self-managed directory to which
the AD Connector is connected.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**DnsIpv6Addrs**

The IPv6 addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
directory, these are the IPv6 addresses of the Simple AD or Microsoft AD directory servers.
For an AD Connector directory, these are the IPv6 addresses of the DNS servers or domain
controllers in your self-managed directory to which the AD Connector is connected.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**Edition**

The edition associated with this directory.

Type: String

Valid Values: `Enterprise | Standard | Hybrid`

Required: No

**HybridSettings**

Contains information about the hybrid directory configuration for the directory,
including AWS System Manager managed node identifiers and DNS IPs.

Type: [HybridSettingsDescription](API_HybridSettingsDescription.md "API_HybridSettingsDescription.md") object

Required: No

**LaunchTime**

The date and time when the directory was created.

Type: Timestamp

Required: No

**Name**

The fully qualified name of the directory.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: No

**NetworkType**

The network type of the directory.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

**OsVersion**

The operating system (OS) version of the directory.

Type: String

Valid Values: `SERVER_2012 | SERVER_2019`

Required: No

**OwnerDirectoryDescription**

Describes the AWS Managed Microsoft AD directory in the directory owner account.

Type: [OwnerDirectoryDescription](API_OwnerDirectoryDescription.md "API_OwnerDirectoryDescription.md") object

Required: No

**RadiusSettings**

Information about the [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object configured for this
directory.

Type: [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object

Required: No

**RadiusStatus**

The status of the RADIUS MFA server connection.

Type: String

Valid Values: `Creating | Completed | Failed`

Required: No

**RegionsInfo**

Lists the Regions where the directory has replicated.

Type: [RegionsInfo](API_RegionsInfo.md "API_RegionsInfo.md") object

Required: No

**ShareMethod**

The method used when sharing a directory to determine whether the directory should be
shared within your AWS organization (`ORGANIZATIONS`) or with any AWS account
by sending a shared directory request (`HANDSHAKE`).

Type: String

Valid Values: `ORGANIZATIONS | HANDSHAKE`

Required: No

**ShareNotes**

A directory share request that is sent by the directory owner to the directory consumer.
The request includes a typed message to help the directory consumer administrator determine
whether to approve or reject the share invitation.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**ShareStatus**

Current directory status of the shared AWS Managed Microsoft AD directory.

Type: String

Valid Values: `Shared | PendingAcceptance | Rejected | Rejecting | RejectFailed | Sharing | ShareFailed | Deleted | Deleting`

Required: No

**ShortName**

The short name of the directory.

Type: String

Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`

Required: No

**Size**

The directory size.

Type: String

Valid Values: `Small | Large`

Required: No

**SsoEnabled**

Indicates whether single sign-on is enabled for the directory. For more information, see
[EnableSso](API_EnableSso.md "API_EnableSso.md") and [DisableSso](API_DisableSso.md "API_DisableSso.md").

Type: Boolean

Required: No

**Stage**

The current stage of the directory.

Type: String

Valid Values: `Requested | Creating | Created | Active | Inoperable | Impaired | Restoring | RestoreFailed | Deleting | Deleted | Failed | Updating`

Required: No

**StageLastUpdatedDateTime**

The date and time when the stage was last updated.

Type: Timestamp

Required: No

**StageReason**

Additional information about the directory stage.

Type: String

Required: No

**Type**

The directory type.

Type: String

Valid Values: `SimpleAD | ADConnector | MicrosoftAD | SharedMicrosoftAD`

Required: No

**VpcSettings**

A [DirectoryVpcSettingsDescription](API_DirectoryVpcSettingsDescription.md "API_DirectoryVpcSettingsDescription.md") object that contains additional
information about a directory. Present only for Simple AD and AWS Managed Microsoft AD
directories.

Type: [DirectoryVpcSettingsDescription](API_DirectoryVpcSettingsDescription.md "API_DirectoryVpcSettingsDescription.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DirectoryDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/DirectoryDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryDescription.md")
