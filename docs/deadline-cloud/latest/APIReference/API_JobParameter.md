# JobParameter

The details of job parameters.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**float** 


A double precision IEEE-754 floating point number represented as a string.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 26.


Pattern: `[-]?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?`



Required: No




**int** 


A signed integer represented as a string.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 20.


Pattern: `[-]?(0|[1-9][0-9]*)`



Required: No




**path** 


A file system path represented as a string.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**string** 


A UTF-8 string.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobParameter "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobParameter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobParameter "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobParameter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobParameter "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobParameter")
