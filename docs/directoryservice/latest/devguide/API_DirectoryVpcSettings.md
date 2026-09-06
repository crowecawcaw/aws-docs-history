

# DirectoryVpcSettings
<a name="API_DirectoryVpcSettings"></a>

Contains VPC information for the [CreateDirectory](API_CreateDirectory.md), [CreateMicrosoftAD](API_CreateMicrosoftAD.md), or [CreateHybridAD](API_CreateHybridAD.md) operation.

## Contents
<a name="API_DirectoryVpcSettings_Contents"></a>

 ** SubnetIds **   <a name="DirectoryService-Type-DirectoryVpcSettings-SubnetIds"></a>
The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.  
Type: Array of strings  
Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`   
Required: Yes

 ** VpcId **   <a name="DirectoryService-Type-DirectoryVpcSettings-VpcId"></a>
The identifier of the VPC in which to create the directory.  
Type: String  
Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`   
Required: Yes

## See Also
<a name="API_DirectoryVpcSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DirectoryVpcSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DirectoryVpcSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DirectoryVpcSettings) 