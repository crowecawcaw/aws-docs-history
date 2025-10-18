# VpcOptions

Describes the VPC options.


## Contents





**ApplianceModeSupport** 


Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is `false`.


Type: Boolean


Required: No




**DnsSupport** 


Indicates whether DNS is supported.


Type: Boolean


Required: No




**Ipv6Support** 


Indicates whether IPv6 is supported.


Type: Boolean


Required: No




**SecurityGroupReferencingSupport** 


Indicates whether security group referencing is enabled for this VPC attachment. The default is `true`. However, at the core network policy-level the default is set to `false`.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/VpcOptions "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/VpcOptions")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/VpcOptions "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/VpcOptions")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/VpcOptions "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/VpcOptions")
