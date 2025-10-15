# TypeFilters

Filter criteria to use in determining which extensions to return.


## Contents





**Category** 


The category of extensions to return.



* `REGISTERED`: Private extensions that have been registered for this account and
 Region.
* `ACTIVATED`: Public extensions that have been activated for this account and
 Region.
* `THIRD_PARTY`: Extensions available for use from publishers other than Amazon.
 This includes:




	+ Private extensions registered in the account.
	+ Public extensions from publishers other than Amazon, whether activated or not.
* `AWS_TYPES`: Extensions available for use from Amazon.

Type: String


Valid Values: `REGISTERED | ACTIVATED | THIRD_PARTY | AWS_TYPES`



Required: No




**PublisherId** 


The id of the publisher of the extension.


Extensions published by Amazon aren't assigned a publisher ID. Use the
 `AWS_TYPES` category to specify a list of types published by Amazon.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




**TypeNamePrefix** 


A prefix to use as a filter for results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 204.


Pattern: `([A-Za-z0-9]{2,64}::){0,2}([A-Za-z0-9]{2,64}:?){0,1}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeFilters "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeFilters")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeFilters "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeFilters")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeFilters "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeFilters")
