

# NetworkConnectorVpcEgressConfiguration
<a name="API_NetworkConnectorVpcEgressConfiguration"></a>

Configuration for a VPC egress network connector. Specifies the VPC subnets, security groups, network protocol, and associated Lambda compute resource types.

## Contents
<a name="API_NetworkConnectorVpcEgressConfiguration_Contents"></a>

 ** AssociatedComputeResourceTypes **   <a name="lambdacore-Type-NetworkConnectorVpcEgressConfiguration-AssociatedComputeResourceTypes"></a>
The types of Lambda compute resources that can use this connector. Currently, only `MicroVm` is supported.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `MicroVm`   
Required: No

 ** NetworkProtocol **   <a name="lambdacore-Type-NetworkConnectorVpcEgressConfiguration-NetworkProtocol"></a>
The network protocol for the connector. Specify `IPv4` for IPv4-only networking, or `DualStack` for both IPv4 and IPv6.  
Type: String  
Valid Values: `IPv4 | DualStack`   
Required: No

 ** SecurityGroupIds **   <a name="lambdacore-Type-NetworkConnectorVpcEgressConfiguration-SecurityGroupIds"></a>
The IDs of the VPC security groups to attach to the ENIs. Specify 0 to 5 security groups. All security groups must be in the same VPC as the subnets.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `sg-[0-9a-zA-Z]*`   
Required: No

 ** SubnetIds **   <a name="lambdacore-Type-NetworkConnectorVpcEgressConfiguration-SubnetIds"></a>
The IDs of the VPC subnets where Lambda provisions elastic network interfaces (ENIs). Specify 1 to 16 subnets. All subnets must be in the same VPC.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `subnet-[0-9a-z]*`   
Required: No

## See Also
<a name="API_NetworkConnectorVpcEgressConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorVpcEgressConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorVpcEgressConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorVpcEgressConfiguration) 