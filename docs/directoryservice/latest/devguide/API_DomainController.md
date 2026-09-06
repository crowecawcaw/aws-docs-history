

# DomainController
<a name="API_DomainController"></a>

Contains information about the domain controllers for a specified directory.

## Contents
<a name="API_DomainController_Contents"></a>

 ** AvailabilityZone **   <a name="DirectoryService-Type-DomainController-AvailabilityZone"></a>
The Availability Zone where the domain controller is located.  
Type: String  
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-DomainController-DirectoryId"></a>
Identifier of the directory where the domain controller resides.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** DnsIpAddr **   <a name="DirectoryService-Type-DomainController-DnsIpAddr"></a>
The IP address of the domain controller.  
Type: String  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** DnsIpv6Addr **   <a name="DirectoryService-Type-DomainController-DnsIpv6Addr"></a>
The IPv6 address of the domain controller.  
Type: String  
Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`   
Required: No

 ** DomainControllerId **   <a name="DirectoryService-Type-DomainController-DomainControllerId"></a>
Identifies a specific domain controller in the directory.  
Type: String  
Pattern: `^dc-[0-9a-f]{10}$`   
Required: No

 ** LaunchTime **   <a name="DirectoryService-Type-DomainController-LaunchTime"></a>
Specifies when the domain controller was created.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-DomainController-Status"></a>
The status of the domain controller.  
Type: String  
Valid Values: `Creating | Active | Impaired | Restoring | Deleting | Deleted | Failed | Updating`   
Required: No

 ** StatusLastUpdatedDateTime **   <a name="DirectoryService-Type-DomainController-StatusLastUpdatedDateTime"></a>
The date and time that the status was last updated.  
Type: Timestamp  
Required: No

 ** StatusReason **   <a name="DirectoryService-Type-DomainController-StatusReason"></a>
A description of the domain controller state.  
Type: String  
Required: No

 ** SubnetId **   <a name="DirectoryService-Type-DomainController-SubnetId"></a>
Identifier of the subnet in the VPC that contains the domain controller.  
Type: String  
Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`   
Required: No

 ** VpcId **   <a name="DirectoryService-Type-DomainController-VpcId"></a>
The identifier of the VPC that contains the domain controller.  
Type: String  
Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`   
Required: No

## See Also
<a name="API_DomainController_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DomainController) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DomainController) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DomainController) 