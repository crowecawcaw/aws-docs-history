# ObjectLambdaAccessPointAlias

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

The alias of an Object Lambda Access Point. For more information, see [How to use a
 bucket-style alias for your S3 bucket Object Lambda Access Point](../userguide/olap-use.md#ol-access-points-alias "../userguide/olap-use.md#ol-access-points-alias").


## Contents





**Status** 


The status of the Object Lambda Access Point alias. If the status is `PROVISIONING`, the Object Lambda Access Point
 is provisioning the alias and the alias is not ready for use yet. If the status is
 `READY`, the Object Lambda Access Point alias is successfully provisioned and ready for
 use.


Type: String


Length Constraints: Minimum length of 2. Maximum length of 16.


Valid Values: `PROVISIONING | READY`



Required: No




**Value** 


The alias value of the Object Lambda Access Point.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Pattern: `^[0-9a-z\\-]{3,63}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaAccessPointAlias "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaAccessPointAlias")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaAccessPointAlias "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaAccessPointAlias")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaAccessPointAlias "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaAccessPointAlias")
