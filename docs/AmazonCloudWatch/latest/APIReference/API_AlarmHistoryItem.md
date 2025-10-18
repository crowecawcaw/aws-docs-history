# AlarmHistoryItem

Represents the history of a specific alarm.


## Contents





**AlarmContributorAttributes** 


A map of attributes that describe the alarm contributor associated with this history item, providing context about the contributor's characteristics at the time of the event.


Type: String to string map


Map Entries: Maximum number of 30 items.


Key Length Constraints: Minimum length of 1. Maximum length of 255.


Value Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmContributorId** 


The unique identifier of the alarm contributor associated with this history item, if applicable.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmName** 


The descriptive name for the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**AlarmType** 


The type of alarm, either metric alarm or composite alarm.


Type: String


Valid Values: `CompositeAlarm | MetricAlarm`



Required: No




**HistoryData** 


Data about the alarm, in JSON format.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 4095.


Required: No




**HistoryItemType** 


The type of alarm history item.


Type: String


Valid Values: `ConfigurationUpdate | StateUpdate | Action | AlarmContributorStateUpdate | AlarmContributorAction`



Required: No




**HistorySummary** 


A summary of the alarm history, in text format.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Timestamp** 


The time stamp for the alarm history item.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmHistoryItem "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmHistoryItem")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmHistoryItem "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmHistoryItem")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmHistoryItem "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmHistoryItem")
