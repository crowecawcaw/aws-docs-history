# VpcOriginEndpointConfig

An Amazon CloudFront VPC origin endpoint configuration.


## Contents





**Arn** 


The ARN of the CloudFront VPC origin endpoint configuration.


Type: String


Required: Yes




**HTTPPort** 


The HTTP port for the CloudFront VPC origin endpoint configuration. The default value is `80`.


Type: Integer


Required: Yes




**HTTPSPort** 


The HTTPS port of the CloudFront VPC origin endpoint configuration. The default value is `443`.


Type: Integer


Required: Yes




**Name** 


The name of the CloudFront VPC origin endpoint configuration.


Type: String


Required: Yes




**OriginProtocolPolicy** 


The origin protocol policy for the CloudFront VPC origin endpoint configuration.


Type: String


Valid Values: `http-only | match-viewer | https-only`



Required: Yes




**OriginSslProtocols** 


A complex type that contains information about the SSL/TLS protocols that CloudFront can use
 when establishing an HTTPS connection with your origin.


Type: [OriginSslProtocols](API_OriginSslProtocols.md "API_OriginSslProtocols.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginEndpointConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginEndpointConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginEndpointConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginEndpointConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginEndpointConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginEndpointConfig")
