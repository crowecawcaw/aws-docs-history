# GetStreamingDistribution

Gets information about a specified RTMP distribution, including the distribution
 configuration.


## Request Syntax



```
GET /2020-05-31/streaming-distribution/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetStreamingDistribution_RequestSyntax "#API_GetStreamingDistribution_RequestSyntax")**


The streaming distribution's ID.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StreamingDistribution>
   <ActiveTrustedSigners>
      <Enabled>***boolean***</Enabled>
      <Items>
         <Signer>
            <AwsAccountNumber>***string***</AwsAccountNumber>
            <KeyPairIds>
               <Items>
                  <KeyPairId>***string***</KeyPairId>
               </Items>
               <Quantity>***integer***</Quantity>
            </KeyPairIds>
         </Signer>
      </Items>
      <Quantity>***integer***</Quantity>
   </ActiveTrustedSigners>
   <ARN>***string***</ARN>
   <DomainName>***string***</DomainName>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <Status>***string***</Status>
   <StreamingDistributionConfig>
      <Aliases>
         <Items>
            <CNAME>***string***</CNAME>
         </Items>
         <Quantity>***integer***</Quantity>
      </Aliases>
      <CallerReference>***string***</CallerReference>
      <Comment>***string***</Comment>
      <Enabled>***boolean***</Enabled>
      <Logging>
         <Bucket>***string***</Bucket>
         <Enabled>***boolean***</Enabled>
         <Prefix>***string***</Prefix>
      </Logging>
      <PriceClass>***string***</PriceClass>
      <S3Origin>
         <DomainName>***string***</DomainName>
         <OriginAccessIdentity>***string***</OriginAccessIdentity>
      </S3Origin>
      <TrustedSigners>
         <Enabled>***boolean***</Enabled>
         <Items>
            <AwsAccountNumber>***string***</AwsAccountNumber>
         </Items>
         <Quantity>***integer***</Quantity>
      </TrustedSigners>
   </StreamingDistributionConfig>
</StreamingDistribution>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[StreamingDistribution](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


Root level tag for the StreamingDistribution parameters.


Required: Yes




**[ActiveTrustedSigners](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


A complex type that lists the AWS accounts, if any, that you included in the
 `TrustedSigners` complex type for this distribution. These are the
 accounts that you want to allow to create signed URLs for private content.


The `Signer` complex type lists the AWS account number of the trusted
 signer or `self` if the signer is the AWS account that created the
 distribution. The `Signer` element also includes the IDs of any active CloudFront
 key pairs that are associated with the trusted signer's AWS account. If no
 `KeyPairId` element appears for a `Signer`, that signer can't
 create signed URLs.


For more information, see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md "API_ActiveTrustedSigners.md") object




**[ARN](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The ARN (Amazon Resource Name) for the distribution. For example:
 `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where
 `123456789012` is your AWS account ID.


Type: String




**[DomainName](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The domain name that corresponds to the streaming distribution, for example,
 `s5c39gqb8ow64r.cloudfront.net`.


Type: String




**[Id](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The identifier for the RTMP distribution. For example:
 `EGTXBD79EXAMPLE`.


Type: String




**[LastModifiedTime](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The date and time that the distribution was last modified.


Type: Timestamp




**[Status](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The current status of the RTMP distribution. When the status is `Deployed`,
 the distribution's information is propagated to all CloudFront edge locations.


Type: String




**[StreamingDistributionConfig](#API_GetStreamingDistribution_ResponseSyntax "#API_GetStreamingDistribution_ResponseSyntax")**


The current configuration information for the RTMP distribution.


Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md "API_StreamingDistributionConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchStreamingDistribution** 


The specified streaming distribution does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetStreamingDistribution")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetStreamingDistribution")
