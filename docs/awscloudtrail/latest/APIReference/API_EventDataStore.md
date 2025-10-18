# EventDataStore

A storage lake of event data against which you can run complex SQL-based queries. An
 event data store can include events that you have logged on your account. To select events for an event data
 store, use [advanced event selectors](../userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../userguide/cloudtrail-lake-concepts.md#adv-event-selectors").


## Contents





**AdvancedEventSelectors** 



*This member has been deprecated.*



The advanced event selectors that were used to select
 events for the data store.


Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md "API_AdvancedEventSelector.md") objects


Required: No




**CreatedTimestamp** 



*This member has been deprecated.*



The timestamp of the event data store's creation.


Type: Timestamp


Required: No




**EventDataStoreArn** 


The ARN of the event data store.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**MultiRegionEnabled** 



*This member has been deprecated.*



Indicates whether the event data store includes events
 from all Regions, or only from the Region in which it was created.


Type: Boolean


Required: No




**Name** 


The name of the event data store.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9._\-]+$`



Required: No




**OrganizationEnabled** 



*This member has been deprecated.*



Indicates that an event data store is collecting logged
 events for an organization.


Type: Boolean


Required: No




**RetentionPeriod** 



*This member has been deprecated.*



The retention period, in days.


Type: Integer


Valid Range: Minimum value of 7. Maximum value of 3653.


Required: No




**Status** 



*This member has been deprecated.*



The status of an event data store.


Type: String


Valid Values: `CREATED | ENABLED | PENDING_DELETION | STARTING_INGESTION | STOPPING_INGESTION | STOPPED_INGESTION`



Required: No




**TerminationProtectionEnabled** 



*This member has been deprecated.*



Indicates whether the event data store is protected from
 termination.


Type: Boolean


Required: No




**UpdatedTimestamp** 



*This member has been deprecated.*



The timestamp showing when an event data store was
 updated, if applicable. `UpdatedTimestamp` is always either the same or newer
 than the time shown in `CreatedTimestamp`.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/EventDataStore "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/EventDataStore")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/EventDataStore "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/EventDataStore")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/EventDataStore "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/EventDataStore")
