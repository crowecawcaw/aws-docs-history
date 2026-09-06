

# NetworkConnectorConfiguration
<a name="API_NetworkConnectorConfiguration"></a>

The network configuration for a network connector. Different connector types use different configuration shapes; specify the configuration that matches your connector type.

## Contents
<a name="API_NetworkConnectorConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** VpcEgressConfiguration **   <a name="lambdacore-Type-NetworkConnectorConfiguration-VpcEgressConfiguration"></a>
Configuration for a VPC egress network connector. Specifies the subnets, security groups, and network protocol for routing outbound traffic through your VPC.  
Type: [NetworkConnectorVpcEgressConfiguration](API_NetworkConnectorVpcEgressConfiguration.md) object  
Required: No

## See Also
<a name="API_NetworkConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorConfiguration) 