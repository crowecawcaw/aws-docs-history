# StartRouteAnalysis

Starts analyzing the routing path between the specified source and destination. For more information, 
 see [Route Analyzer](https://docs.aws.amazon.com/vpc/latest/tgw/route-analyzer.html "https://docs.aws.amazon.com/vpc/latest/tgw/route-analyzer.html").


## Request Syntax



```
POST /global-networks/`globalNetworkId`/route-analyses HTTP/1.1
Content-type: application/json

{
   "Destination": { 
      "IpAddress": "`string`",
      "TransitGatewayAttachmentArn": "`string`"
   },
   "IncludeReturnPath": `boolean`,
   "Source": { 
      "IpAddress": "`string`",
      "TransitGatewayAttachmentArn": "`string`"
   },
   "UseMiddleboxes": `boolean`
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_StartRouteAnalysis_RequestSyntax "#API_StartRouteAnalysis_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Destination](#API_StartRouteAnalysis_RequestSyntax "#API_StartRouteAnalysis_RequestSyntax")**


The destination.


Type: [RouteAnalysisEndpointOptionsSpecification](API_RouteAnalysisEndpointOptionsSpecification.md "API_RouteAnalysisEndpointOptionsSpecification.md") object


Required: Yes




**[IncludeReturnPath](#API_StartRouteAnalysis_RequestSyntax "#API_StartRouteAnalysis_RequestSyntax")**


Indicates whether to analyze the return path. The default is `false`.


Type: Boolean


Required: No




**[Source](#API_StartRouteAnalysis_RequestSyntax "#API_StartRouteAnalysis_RequestSyntax")**


The source from which traffic originates.


Type: [RouteAnalysisEndpointOptionsSpecification](API_RouteAnalysisEndpointOptionsSpecification.md "API_RouteAnalysisEndpointOptionsSpecification.md") object


Required: Yes




**[UseMiddleboxes](#API_StartRouteAnalysis_RequestSyntax "#API_StartRouteAnalysis_RequestSyntax")**


Indicates whether to include the location of middlebox appliances in the route analysis.
 The default is `false`.


Type: Boolean


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "RouteAnalysis": { 
      "Destination": { 
         "IpAddress": "***string***",
         "TransitGatewayArn": "***string***",
         "TransitGatewayAttachmentArn": "***string***"
      },
      "ForwardPath": { 
         "CompletionStatus": { 
            "ReasonCode": "***string***",
            "ReasonContext": { 
               "***string***" : "***string***" 
            },
            "ResultCode": "***string***"
         },
         "Path": [ 
            { 
               "DestinationCidrBlock": "***string***",
               "Resource": { 
                  "Definition": "***string***",
                  "IsMiddlebox": ***boolean***,
                  "NameTag": "***string***",
                  "RegisteredGatewayArn": "***string***",
                  "ResourceArn": "***string***",
                  "ResourceType": "***string***"
               },
               "Sequence": ***number***
            }
         ]
      },
      "GlobalNetworkId": "***string***",
      "IncludeReturnPath": ***boolean***,
      "OwnerAccountId": "***string***",
      "ReturnPath": { 
         "CompletionStatus": { 
            "ReasonCode": "***string***",
            "ReasonContext": { 
               "***string***" : "***string***" 
            },
            "ResultCode": "***string***"
         },
         "Path": [ 
            { 
               "DestinationCidrBlock": "***string***",
               "Resource": { 
                  "Definition": "***string***",
                  "IsMiddlebox": ***boolean***,
                  "NameTag": "***string***",
                  "RegisteredGatewayArn": "***string***",
                  "ResourceArn": "***string***",
                  "ResourceType": "***string***"
               },
               "Sequence": ***number***
            }
         ]
      },
      "RouteAnalysisId": "***string***",
      "Source": { 
         "IpAddress": "***string***",
         "TransitGatewayArn": "***string***",
         "TransitGatewayAttachmentArn": "***string***"
      },
      "StartTimestamp": ***number***,
      "Status": "***string***",
      "UseMiddleboxes": ***boolean***
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[RouteAnalysis](#API_StartRouteAnalysis_ResponseSyntax "#API_StartRouteAnalysis_ResponseSyntax")**


The route analysis.


Type: [RouteAnalysis](API_RouteAnalysis.md "API_RouteAnalysis.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**ConflictException** 


There was a conflict processing the request. Updating or deleting the resource can
 cause an inconsistent state.





**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




HTTP Status Code: 409




**InternalServerException** 


The request has failed due to an internal error.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 500




**ResourceNotFoundException** 


The specified resource could not be found.





**Context** 


The specified resource could not be found.




**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




HTTP Status Code: 404




**ThrottlingException** 


The request was denied due to request throttling.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 429




**ValidationException** 


The input fails to satisfy the constraints.





**Fields** 


The fields that caused the error, if applicable.




**Reason** 


The reason for the error.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/StartRouteAnalysis")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/StartRouteAnalysis "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/StartRouteAnalysis")
