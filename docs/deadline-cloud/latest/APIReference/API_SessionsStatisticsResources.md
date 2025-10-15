# SessionsStatisticsResources

Specifies the fleet IDs or queue IDs to return statistics. You can specify only fleet
 IDs or queue IDS, not both.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**fleetIds** 


One to 10 fleet IDs that specify the fleets to return statistics for. If you specify the
 `fleetIds` field, you can't specify the `queueIds` field.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `fleet-[0-9a-f]{32}`



Required: No




**queueIds** 


One to 10 queue IDs that specify the queues to return statistics for. If you specify the
 `queueIds` field, you can't specify the `fleetIds` field.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `queue-[0-9a-f]{32}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionsStatisticsResources "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionsStatisticsResources")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionsStatisticsResources "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionsStatisticsResources")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionsStatisticsResources "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionsStatisticsResources")
