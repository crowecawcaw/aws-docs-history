# CreateStreamingDistributionWithTags

This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP)
 distributions on December 31, 2020. For more information, [read the announcement](http://forums.aws.amazon.com/ann.jspa?annID=7356 "http://forums.aws.amazon.com/ann.jspa?annID=7356") on the Amazon CloudFront discussion
 forum.


## Request Syntax



```
POST /2020-05-31/streaming-distribution?WithTags HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<StreamingDistributionConfigWithTags xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <StreamingDistributionConfig>
      <Aliases>
         <Items>
            <CNAME>`string`</CNAME>
         </Items>
         <Quantity>`integer`</Quantity>
      </Aliases>
      <CallerReference>`string`</CallerReference>
      <Comment>`string`</Comment>
      <Enabled>`boolean`</Enabled>
      <Logging>
         <Bucket>`string`</Bucket>
         <Enabled>`boolean`</Enabled>
         <Prefix>`string`</Prefix>
      </Logging>
      <PriceClass>`string`</PriceClass>
      <S3Origin>
         <DomainName>`string`</DomainName>
         <OriginAccessIdentity>`string`</OriginAccessIdentity>
      </S3Origin>
      <TrustedSigners>
         <Enabled>`boolean`</Enabled>
         <Items>
            <AwsAccountNumber>`string`</AwsAccountNumber>
         </Items>
         <Quantity>`integer`</Quantity>
      </TrustedSigners>
   </StreamingDistributionConfig>
   <Tags>
      <Items>
         <Tag>
            <Key>`string`</Key>
            <Value>`string`</Value>
         </Tag>
      </Items>
   </Tags>
</StreamingDistributionConfigWithTags>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[StreamingDistributionConfigWithTags](#API_CreateStreamingDistributionWithTags_RequestSyntax "#API_CreateStreamingDistributionWithTags_RequestSyntax")**


Root level tag for the StreamingDistributionConfigWithTags parameters.


Required: Yes




**[StreamingDistributionConfig](#API_CreateStreamingDistributionWithTags_RequestSyntax "#API_CreateStreamingDistributionWithTags_RequestSyntax")**


A streaming distribution Configuration.


Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md "API_StreamingDistributionConfig.md") object


Required: Yes




**[Tags](#API_CreateStreamingDistributionWithTags_RequestSyntax "#API_CreateStreamingDistributionWithTags_RequestSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[StreamingDistribution](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


Root level tag for the StreamingDistribution parameters.


Required: Yes




**[ActiveTrustedSigners](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


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




**[ARN](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The ARN (Amazon Resource Name) for the distribution. For example:
 `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where
 `123456789012` is your AWS account ID.


Type: String




**[DomainName](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The domain name that corresponds to the streaming distribution, for example,
 `s5c39gqb8ow64r.cloudfront.net`.


Type: String




**[Id](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The identifier for the RTMP distribution. For example:
 `EGTXBD79EXAMPLE`.


Type: String




**[LastModifiedTime](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The date and time that the distribution was last modified.


Type: Timestamp




**[Status](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The current status of the RTMP distribution. When the status is `Deployed`,
 the distribution's information is propagated to all CloudFront edge locations.


Type: String




**[StreamingDistributionConfig](#API_CreateStreamingDistributionWithTags_ResponseSyntax "#API_CreateStreamingDistributionWithTags_ResponseSyntax")**


The current configuration information for the RTMP distribution.


Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md "API_StreamingDistributionConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**CNAMEAlreadyExists** 


The CNAME specified is already defined for CloudFront.


HTTP Status Code: 409




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidOrigin** 


The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.


HTTP Status Code: 400




**InvalidOriginAccessControl** 


The origin access control is not valid.


HTTP Status Code: 400




**InvalidOriginAccessIdentity** 


The origin access identity is not valid or doesn't exist.


HTTP Status Code: 400




**InvalidTagging** 


The tagging specified is not valid.


HTTP Status Code: 400




**MissingBody** 


This operation requires a body. Ensure that the body is present and the
 `Content-Type` header is set.


HTTP Status Code: 400




**StreamingDistributionAlreadyExists** 


The caller reference you attempted to create the streaming distribution with is
 associated with another distribution


HTTP Status Code: 409




**TooManyStreamingDistributionCNAMEs** 


Your request contains more CNAMEs than are allowed per distribution.


HTTP Status Code: 400




**TooManyStreamingDistributions** 


Processing your request would cause you to exceed the maximum number of streaming
 distributions allowed.


HTTP Status Code: 400




**TooManyTrustedSigners** 


Your request contains more trusted signers than are allowed per distribution.


HTTP Status Code: 400




**TrustedSignerDoesNotExist** 


One or more of your trusted signers don't exist.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateStreamingDistributionWithTags")
