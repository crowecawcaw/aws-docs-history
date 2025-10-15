# StorageLensGroupAndOperator

 A logical operator that allows multiple filter conditions to be joined for more complex
 comparisons of Storage Lens group data. 


## Contents





**MatchAnyPrefix** 


 Contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes
 are allowed. 


Type: Array of strings


Required: No




**MatchAnySuffix** 


 Contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes
 are allowed. 


Type: Array of strings


Required: No




**MatchAnyTag** 


 Contains the list of object tags. At least one object tag must be specified. Up to 10
 object tags are allowed. 


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: No




**MatchObjectAge** 


 Contains `DaysGreaterThan` and `DaysLessThan` to define the
 object age range (minimum and maximum number of days). 


Type: [MatchObjectAge](API_control_MatchObjectAge.md "API_control_MatchObjectAge.md") data type


Required: No




**MatchObjectSize** 


 Contains `BytesGreaterThan` and `BytesLessThan` to define the
 object size range (minimum and maximum number of Bytes). 


Type: [MatchObjectSize](API_control_MatchObjectSize.md "API_control_MatchObjectSize.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensGroupAndOperator "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensGroupAndOperator")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensGroupAndOperator "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensGroupAndOperator")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensGroupAndOperator "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensGroupAndOperator")
