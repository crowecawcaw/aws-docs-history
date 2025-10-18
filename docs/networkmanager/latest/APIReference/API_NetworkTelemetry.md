# NetworkTelemetry

Describes the telemetry information for a resource.


## Contents





**AccountId** 


The AWS account ID.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`



Required: No




**Address** 


The address.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**AwsRegion** 


The AWS Region.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**Health** 


The connection health.


Type: [ConnectionHealth](API_ConnectionHealth.md "API_ConnectionHealth.md") object


Required: No




**RegisteredGatewayArn** 


The ARN of the gateway.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceId** 


The ID of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**ResourceType** 


The resource type.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkTelemetry")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkTelemetry")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkTelemetry")
