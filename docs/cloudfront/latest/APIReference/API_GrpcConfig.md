# GrpcConfig

Amazon CloudFront supports gRPC, an open-source remote procedure call (RPC) framework built on
 HTTP/2. gRPC offers bi-directional streaming and binary protocol that buffers payloads,
 making it suitable for applications that require low latency communications.

To enable your distribution to handle gRPC requests, you must include HTTP/2 as one of the supported `HTTP` versions and allow `HTTP` methods, including `POST`.

For more information, see [Using gRPC with CloudFront distributions](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-using-grpc.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-using-grpc.md") in the
 *Amazon CloudFront Developer Guide*.


## Contents





**Enabled** 


Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your
 origins.


Type: Boolean


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GrpcConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GrpcConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GrpcConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GrpcConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GrpcConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GrpcConfig")
