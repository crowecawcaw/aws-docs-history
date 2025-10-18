# ListStreamingDistributions

List streaming distributions.


## Request Syntax



```
GET /2020-05-31/streaming-distribution?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListStreamingDistributions_RequestSyntax "#API_ListStreamingDistributions_RequestSyntax")**


The value that you provided for the `Marker` request parameter.




**[MaxItems](#API_ListStreamingDistributions_RequestSyntax "#API_ListStreamingDistributions_RequestSyntax")**


The value that you provided for the `MaxItems` request parameter.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StreamingDistributionList>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
      <StreamingDistributionSummary>
         <Aliases>
            <Items>
               <CNAME>***string***</CNAME>
            </Items>
            <Quantity>***integer***</Quantity>
         </Aliases>
         <ARN>***string***</ARN>
         <Comment>***string***</Comment>
         <DomainName>***string***</DomainName>
         <Enabled>***boolean***</Enabled>
         <Id>***string***</Id>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
         <PriceClass>***string***</PriceClass>
         <S3Origin>
            <DomainName>***string***</DomainName>
            <OriginAccessIdentity>***string***</OriginAccessIdentity>
         </S3Origin>
         <Status>***string***</Status>
         <TrustedSigners>
            <Enabled>***boolean***</Enabled>
            <Items>
               <AwsAccountNumber>***string***</AwsAccountNumber>
            </Items>
            <Quantity>***integer***</Quantity>
         </TrustedSigners>
      </StreamingDistributionSummary>
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</StreamingDistributionList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[StreamingDistributionList](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


Root level tag for the StreamingDistributionList parameters.


Required: Yes




**[IsTruncated](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


A flag that indicates whether more streaming distributions remain to be listed. If
 your results were truncated, you can make a follow-up pagination request using the
 `Marker` request parameter to retrieve more distributions in the list.
 


Type: Boolean




**[Items](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


A complex type that contains one `StreamingDistributionSummary` element for
 each distribution that was created by the current AWS account.


Type: Array of [StreamingDistributionSummary](API_StreamingDistributionSummary.md "API_StreamingDistributionSummary.md") objects




**[Marker](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


The value you provided for the `Marker` request parameter.


Type: String




**[MaxItems](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


The value you provided for the `MaxItems` request parameter.


Type: Integer




**[NextMarker](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


If `IsTruncated` is `true`, this element is present and contains
 the value you can use for the `Marker` request parameter to continue listing
 your RTMP distributions where they left off.


Type: String




**[Quantity](#API_ListStreamingDistributions_ResponseSyntax "#API_ListStreamingDistributions_ResponseSyntax")**


The number of streaming distributions that were created by the current AWS account.
 


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListStreamingDistributions")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListStreamingDistributions "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListStreamingDistributions")
