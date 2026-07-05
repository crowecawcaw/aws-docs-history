# NetworkConnectorConfiguration

The network configuration for a network connector. Different connector types use different configuration
shapes; specify the configuration that matches your connector type.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**VpcEgressConfiguration**

Configuration for a VPC egress network connector. Specifies the subnets, security groups, and network protocol
for routing outbound traffic through your VPC.

Type: [NetworkConnectorVpcEgressConfiguration](API_NetworkConnectorVpcEgressConfiguration.md "API_NetworkConnectorVpcEgressConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorConfiguration.md "../../../goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorConfiguration.md "../../../goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorConfiguration.md "../../../goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorConfiguration.md")
