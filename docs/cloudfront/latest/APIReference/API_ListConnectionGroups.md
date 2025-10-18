# ListConnectionGroups

Lists the connection groups in your AWS account.


## Request Syntax



```
POST /2020-05-31/connection-groups HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListConnectionGroupsRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <AssociationFilter>
      <AnycastIpListId>`string`</AnycastIpListId>
   </AssociationFilter>
   <Marker>`string`</Marker>
   <MaxItems>`integer`</MaxItems>
</ListConnectionGroupsRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[ListConnectionGroupsRequest](#API_ListConnectionGroups_RequestSyntax "#API_ListConnectionGroups_RequestSyntax")**


Root level tag for the ListConnectionGroupsRequest parameters.


Required: Yes




**[AssociationFilter](#API_ListConnectionGroups_RequestSyntax "#API_ListConnectionGroups_RequestSyntax")**


Filter by associated Anycast IP list ID.


Type: [ConnectionGroupAssociationFilter](API_ConnectionGroupAssociationFilter.md "API_ConnectionGroupAssociationFilter.md") object


Required: No




**[Marker](#API_ListConnectionGroups_RequestSyntax "#API_ListConnectionGroups_RequestSyntax")**


The marker for the next set of connection groups to retrieve.


Type: String


Required: No




**[MaxItems](#API_ListConnectionGroups_RequestSyntax "#API_ListConnectionGroups_RequestSyntax")**


The maximum number of connection groups to return.


Type: Integer


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListConnectionGroupsResult>
   <ConnectionGroups>
      <ConnectionGroupSummary>
         <AnycastIpListId>***string***</AnycastIpListId>
         <Arn>***string***</Arn>
         <CreatedTime>***timestamp***</CreatedTime>
         <Enabled>***boolean***</Enabled>
         <ETag>***string***</ETag>
         <Id>***string***</Id>
         <IsDefault>***boolean***</IsDefault>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
         <Name>***string***</Name>
         <RoutingEndpoint>***string***</RoutingEndpoint>
         <Status>***string***</Status>
      </ConnectionGroupSummary>
   </ConnectionGroups>
   <NextMarker>***string***</NextMarker>
</ListConnectionGroupsResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListConnectionGroupsResult](#API_ListConnectionGroups_ResponseSyntax "#API_ListConnectionGroups_ResponseSyntax")**


Root level tag for the ListConnectionGroupsResult parameters.


Required: Yes




**[ConnectionGroups](#API_ListConnectionGroups_ResponseSyntax "#API_ListConnectionGroups_ResponseSyntax")**


The list of connection groups that you retrieved.


Type: Array of [ConnectionGroupSummary](API_ConnectionGroupSummary.md "API_ConnectionGroupSummary.md") objects




**[NextMarker](#API_ListConnectionGroups_ResponseSyntax "#API_ListConnectionGroups_ResponseSyntax")**


A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListConnectionGroups")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListConnectionGroups "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListConnectionGroups")
