# RealtimeLogConfigs

A list of real-time log configurations.


## Contents





**IsTruncated** 


A flag that indicates whether there are more real-time log configurations than are
 contained in this list.


Type: Boolean


Required: Yes




**Marker** 


This parameter indicates where this list of real-time log configurations begins. This
 list includes real-time log configurations that occur after the marker.


Type: String


Required: Yes




**MaxItems** 


The maximum number of real-time log configurations requested.


Type: Integer


Required: Yes




**Items** 


Contains the list of real-time log configurations.


Type: Array of [RealtimeLogConfig](API_RealtimeLogConfig.md "API_RealtimeLogConfig.md") objects


Required: No




**NextMarker** 


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing real-time log configurations where you left off.
 


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/RealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/RealtimeLogConfigs")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/RealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/RealtimeLogConfigs")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/RealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/RealtimeLogConfigs")
