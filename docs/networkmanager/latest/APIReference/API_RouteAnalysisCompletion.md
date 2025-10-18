# RouteAnalysisCompletion

Describes the status of an analysis at completion.


## Contents





**ReasonCode** 


The reason code. Available only if a connection is not found.



* `BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND` - Found a black hole route with the destination CIDR block.
* `CYCLIC_PATH_DETECTED` - Found the same resource multiple times while traversing the path.
* `INACTIVE_ROUTE_FOR_DESTINATION_FOUND` - Found an inactive route with the destination CIDR block.
* `MAX_HOPS_EXCEEDED` - Analysis exceeded 64 hops without finding the destination.
* `ROUTE_NOT_FOUND` - Cannot find a route table with the destination CIDR block.
* `TGW_ATTACH_ARN_NO_MATCH` - Found an attachment, but not with the correct destination ARN.
* `TGW_ATTACH_NOT_FOUND` - Cannot find an attachment.
* `TGW_ATTACH_NOT_IN_TGW` - Found an attachment, but not to the correct transit gateway.
* `TGW_ATTACH_STABLE_ROUTE_TABLE_NOT_FOUND` - The state of the route table association is not associated.

Type: String


Valid Values: `TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND | TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY | CYCLIC_PATH_DETECTED | TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND | ROUTE_NOT_FOUND | BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND | INACTIVE_ROUTE_FOR_DESTINATION_FOUND | TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH | MAX_HOPS_EXCEEDED | POSSIBLE_MIDDLEBOX | NO_DESTINATION_ARN_PROVIDED`



Required: No




**ReasonContext** 


Additional information about the path. Available only if a connection is not found.


Type: String to string map


Key Length Constraints: Minimum length of 0. Maximum length of 10000000.


Key Pattern: `[\s\S]*`



Value Length Constraints: Minimum length of 0. Maximum length of 10000000.


Value Pattern: `[\s\S]*`



Required: No




**ResultCode** 


The result of the analysis. If the status is `NOT_CONNECTED`, check the 
 reason code.


Type: String


Valid Values: `CONNECTED | NOT_CONNECTED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysisCompletion "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysisCompletion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysisCompletion "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysisCompletion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysisCompletion "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysisCompletion")
