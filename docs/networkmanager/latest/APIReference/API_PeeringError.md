# PeeringError

Describes an error associated with a peering request.


## Contents





**Code** 


The error code for the peering request.


Type: String


Valid Values: `TRANSIT_GATEWAY_NOT_FOUND | TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED | MISSING_PERMISSIONS | INTERNAL_ERROR | EDGE_LOCATION_PEER_DUPLICATE | INVALID_TRANSIT_GATEWAY_STATE`



Required: No




**Message** 


The message associated with the error `code`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**MissingPermissionsContext** 


Provides additional information about missing permissions for the peering
 error.


Type: [PermissionsErrorContext](API_PermissionsErrorContext.md "API_PermissionsErrorContext.md") object


Required: No




**RequestId** 


The ID of the Peering request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the requested peering resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PeeringError "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PeeringError")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PeeringError "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PeeringError")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PeeringError "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PeeringError")
