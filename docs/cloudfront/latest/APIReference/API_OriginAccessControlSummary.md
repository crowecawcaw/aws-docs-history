# OriginAccessControlSummary

A CloudFront origin access control.


## Contents





**Description** 


A description of the origin access control.


Type: String


Required: Yes




**Id** 


The unique identifier of the origin access control.


Type: String


Required: Yes




**Name** 


A unique name that identifies the origin access control.


Type: String


Required: Yes




**OriginAccessControlOriginType** 


The type of origin that this origin access control is for.


Type: String


Valid Values: `s3 | mediastore | mediapackagev2 | lambda`



Required: Yes




**SigningBehavior** 


A value that specifies which requests CloudFront signs (adds authentication information to).
 This field can have one of the following values:



* `never` – CloudFront doesn't sign any origin requests.
* `always` – CloudFront signs all origin requests, overwriting the
 `Authorization` header from the viewer request if
 necessary.
* `no-override` – If the viewer request doesn't contain the
 `Authorization` header, CloudFront signs the origin request. If the
 viewer request contains the `Authorization` header, CloudFront doesn't sign
 the origin request, but instead passes along the `Authorization`
 header that it received in the viewer request.

Type: String


Valid Values: `never | always | no-override`



Required: Yes




**SigningProtocol** 


The signing protocol of the origin access control. The signing protocol determines how
 CloudFront signs (authenticates) requests. The only valid value is `sigv4`.


Type: String


Valid Values: `sigv4`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlSummary")
