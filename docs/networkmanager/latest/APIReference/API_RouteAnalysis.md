# RouteAnalysis

Describes a route analysis.


## Contents





**Destination** 


The destination.


Type: [RouteAnalysisEndpointOptions](API_RouteAnalysisEndpointOptions.md "API_RouteAnalysisEndpointOptions.md") object


Required: No




**ForwardPath** 


The forward path.


Type: [RouteAnalysisPath](API_RouteAnalysisPath.md "API_RouteAnalysisPath.md") object


Required: No




**GlobalNetworkId** 


The ID of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**IncludeReturnPath** 


Indicates whether to analyze the return path. The return path is not analyzed if the forward path
 analysis does not succeed.


Type: Boolean


Required: No




**OwnerAccountId** 


The ID of the AWS account that created the route analysis.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`



Required: No




**ReturnPath** 


The return path.


Type: [RouteAnalysisPath](API_RouteAnalysisPath.md "API_RouteAnalysisPath.md") object


Required: No




**RouteAnalysisId** 


The ID of the route analysis.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Source** 


The source.


Type: [RouteAnalysisEndpointOptions](API_RouteAnalysisEndpointOptions.md "API_RouteAnalysisEndpointOptions.md") object


Required: No




**StartTimestamp** 


The time that the analysis started.


Type: Timestamp


Required: No




**Status** 


The status of the route analysis.


Type: String


Valid Values: `RUNNING | COMPLETED | FAILED`



Required: No




**UseMiddleboxes** 


Indicates whether to include the location of middlebox appliances in the route analysis.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysis "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysis")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysis "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysis")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysis "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysis")
