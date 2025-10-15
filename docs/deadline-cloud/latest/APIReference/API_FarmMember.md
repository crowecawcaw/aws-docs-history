# FarmMember

The member of a farm.


## Contents





**farmId** 


The farm ID of the farm member.


Type: String


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**identityStoreId** 


The identity store ID of the farm member.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 36.


Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`



Required: Yes




**membershipLevel** 


The farm member's membership level.


Type: String


Valid Values: `VIEWER | CONTRIBUTOR | OWNER | MANAGER`



Required: Yes




**principalId** 


The principal ID of the farm member.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 47.


Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`



Required: Yes




**principalType** 


The principal type of the farm member.


Type: String


Valid Values: `USER | GROUP`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FarmMember "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FarmMember")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FarmMember "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FarmMember")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FarmMember "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FarmMember")
