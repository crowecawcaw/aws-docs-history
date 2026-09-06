

# DirectoryDescription
<a name="API_DirectoryDescription"></a>

Contains information about an AWS Directory Service directory.

## Contents
<a name="API_DirectoryDescription_Contents"></a>

 ** AccessUrl **   <a name="DirectoryService-Type-DirectoryDescription-AccessUrl"></a>
The access URL for the directory, such as `http://<alias>.awsapps.com`. If no alias exists, `<alias>` is the directory identifier, such as `d-XXXXXXXXXX`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** Alias **   <a name="DirectoryService-Type-DirectoryDescription-Alias"></a>
The alias for the directory. If no alias exists, the alias is the directory identifier, such as `d-XXXXXXXXXX`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 62.  
Pattern: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`   
Required: No

 ** ConnectSettings **   <a name="DirectoryService-Type-DirectoryDescription-ConnectSettings"></a>
 [DirectoryConnectSettingsDescription](API_DirectoryConnectSettingsDescription.md) object that contains additional information about an AD Connector directory. Present only for AD Connector directories.  
Type: [DirectoryConnectSettingsDescription](API_DirectoryConnectSettingsDescription.md) object  
Required: No

 ** Description **   <a name="DirectoryService-Type-DirectoryDescription-Description"></a>
The description for the directory.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** DesiredNumberOfDomainControllers **   <a name="DirectoryService-Type-DirectoryDescription-DesiredNumberOfDomainControllers"></a>
The desired number of domain controllers in the directory if the directory is Microsoft AD.  
Type: Integer  
Valid Range: Minimum value of 2.  
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-DirectoryDescription-DirectoryId"></a>
The directory identifier.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** DnsIpAddrs **   <a name="DirectoryService-Type-DirectoryDescription-DnsIpAddrs"></a>
The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IP addresses of self-managed directory to which the AD Connector is connected.  
Type: Array of strings  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** DnsIpv6Addrs **   <a name="DirectoryService-Type-DirectoryDescription-DnsIpv6Addrs"></a>
The IPv6 addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IPv6 addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IPv6 addresses of the DNS servers or domain controllers in your self-managed directory to which the AD Connector is connected.  
Type: Array of strings  
Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`   
Required: No

 ** Edition **   <a name="DirectoryService-Type-DirectoryDescription-Edition"></a>
The edition associated with this directory.  
Type: String  
Valid Values: `Enterprise | Standard | Hybrid`   
Required: No

 ** HybridSettings **   <a name="DirectoryService-Type-DirectoryDescription-HybridSettings"></a>
Contains information about the hybrid directory configuration for the directory, including AWS System Manager managed node identifiers and DNS IPs.  
Type: [HybridSettingsDescription](API_HybridSettingsDescription.md) object  
Required: No

 ** LaunchTime **   <a name="DirectoryService-Type-DirectoryDescription-LaunchTime"></a>
The date and time when the directory was created.  
Type: Timestamp  
Required: No

 ** Name **   <a name="DirectoryService-Type-DirectoryDescription-Name"></a>
The fully qualified name of the directory.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: No

 ** NetworkType **   <a name="DirectoryService-Type-DirectoryDescription-NetworkType"></a>
The network type of the directory.  
Type: String  
Valid Values: `Dual-stack | IPv4 | IPv6`   
Required: No

 ** OsVersion **   <a name="DirectoryService-Type-DirectoryDescription-OsVersion"></a>
The operating system (OS) version of the directory.  
Type: String  
Valid Values: `SERVER_2012 | SERVER_2019`   
Required: No

 ** OwnerDirectoryDescription **   <a name="DirectoryService-Type-DirectoryDescription-OwnerDirectoryDescription"></a>
Describes the AWS Managed Microsoft AD directory in the directory owner account.  
Type: [OwnerDirectoryDescription](API_OwnerDirectoryDescription.md) object  
Required: No

 ** RadiusSettings **   <a name="DirectoryService-Type-DirectoryDescription-RadiusSettings"></a>
Information about the [RadiusSettings](API_RadiusSettings.md) object configured for this directory.  
Type: [RadiusSettings](API_RadiusSettings.md) object  
Required: No

 ** RadiusStatus **   <a name="DirectoryService-Type-DirectoryDescription-RadiusStatus"></a>
The status of the RADIUS MFA server connection.  
Type: String  
Valid Values: `Creating | Completed | Failed`   
Required: No

 ** RegionsInfo **   <a name="DirectoryService-Type-DirectoryDescription-RegionsInfo"></a>
Lists the Regions where the directory has replicated.  
Type: [RegionsInfo](API_RegionsInfo.md) object  
Required: No

 ** ShareMethod **   <a name="DirectoryService-Type-DirectoryDescription-ShareMethod"></a>
The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (`ORGANIZATIONS`) or with any AWS account by sending a shared directory request (`HANDSHAKE`).  
Type: String  
Valid Values: `ORGANIZATIONS | HANDSHAKE`   
Required: No

 ** ShareNotes **   <a name="DirectoryService-Type-DirectoryDescription-ShareNotes"></a>
A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** ShareStatus **   <a name="DirectoryService-Type-DirectoryDescription-ShareStatus"></a>
Current directory status of the shared AWS Managed Microsoft AD directory.  
Type: String  
Valid Values: `Shared | PendingAcceptance | Rejected | Rejecting | RejectFailed | Sharing | ShareFailed | Deleted | Deleting`   
Required: No

 ** ShortName **   <a name="DirectoryService-Type-DirectoryDescription-ShortName"></a>
The short name of the directory.  
Type: String  
Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`   
Required: No

 ** Size **   <a name="DirectoryService-Type-DirectoryDescription-Size"></a>
The directory size.  
Type: String  
Valid Values: `Small | Large`   
Required: No

 ** SsoEnabled **   <a name="DirectoryService-Type-DirectoryDescription-SsoEnabled"></a>
Indicates whether single sign-on is enabled for the directory. For more information, see [EnableSso](API_EnableSso.md) and [DisableSso](API_DisableSso.md).  
Type: Boolean  
Required: No

 ** Stage **   <a name="DirectoryService-Type-DirectoryDescription-Stage"></a>
The current stage of the directory.  
Type: String  
Valid Values: `Requested | Creating | Created | Active | Inoperable | Impaired | Restoring | RestoreFailed | Deleting | Deleted | Failed | Updating`   
Required: No

 ** StageLastUpdatedDateTime **   <a name="DirectoryService-Type-DirectoryDescription-StageLastUpdatedDateTime"></a>
The date and time when the stage was last updated.  
Type: Timestamp  
Required: No

 ** StageReason **   <a name="DirectoryService-Type-DirectoryDescription-StageReason"></a>
Additional information about the directory stage.  
Type: String  
Required: No

 ** Type **   <a name="DirectoryService-Type-DirectoryDescription-Type"></a>
The directory type.  
Type: String  
Valid Values: `SimpleAD | ADConnector | MicrosoftAD | SharedMicrosoftAD`   
Required: No

 ** VpcSettings **   <a name="DirectoryService-Type-DirectoryDescription-VpcSettings"></a>
A [DirectoryVpcSettingsDescription](API_DirectoryVpcSettingsDescription.md) object that contains additional information about a directory. Present only for Simple AD and AWS Managed Microsoft AD directories.  
Type: [DirectoryVpcSettingsDescription](API_DirectoryVpcSettingsDescription.md) object  
Required: No

## See Also
<a name="API_DirectoryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DirectoryDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DirectoryDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DirectoryDescription) 