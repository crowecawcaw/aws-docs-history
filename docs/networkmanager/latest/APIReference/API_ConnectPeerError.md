# ConnectPeerError

Describes an error associated with a Connect peer request


## Contents





**Code** 


The error code for the Connect peer request.


Type: String


Valid Values: `EDGE_LOCATION_NO_FREE_IPS | EDGE_LOCATION_PEER_DUPLICATE | SUBNET_NOT_FOUND | IP_OUTSIDE_SUBNET_CIDR_RANGE | INVALID_INSIDE_CIDR_BLOCK | NO_ASSOCIATED_CIDR_BLOCK`



Required: No




**Message** 


The message associated with the error `code`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**RequestId** 


The ID of the Connect peer request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the requested Connect peer resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerError "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerError")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerError "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerError")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerError "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerError")
