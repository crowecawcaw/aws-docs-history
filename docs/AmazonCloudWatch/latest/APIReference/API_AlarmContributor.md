# AlarmContributor

Represents an individual contributor to a multi-timeseries alarm, containing information about a specific time series and its contribution to the alarm's state.


## Contents





**ContributorAttributes** 


A map of attributes that describe the contributor, such as metric dimensions and other identifying characteristics.


Type: String to string map


Map Entries: Maximum number of 30 items.


Key Length Constraints: Minimum length of 1. Maximum length of 255.


Value Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**ContributorId** 


The unique identifier for this alarm contributor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**StateReason** 


An explanation for the contributor's current state, providing context about why it is in its current condition.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1023.


Required: Yes




**StateTransitionedTimestamp** 


The timestamp when the contributor last transitioned to its current state.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmContributor "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmContributor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmContributor "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmContributor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmContributor "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmContributor")
