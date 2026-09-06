

# Customer Profiles standard communication record object fields
<a name="customer-profiles-standard-communication-record-object-fields"></a>

 The following table lists all the fields in the Customer Profiles standard communication record object. 


|  Standard communicationRecord field  |  Data type  |  Description  | 
| --- | --- | --- | 
|  CommunicationRecordId  |  String  |  The unique identifier of a standard communication record.  | 
|  Channel  |  String  |  The method used to contact your contact center. For example: VOICE, CHAT, EMAIL  | 
|  ConnectInstanceArn  |  String  |  The ARN of the AWS Connect instance.  | 
|  CreatedDate  |  String  |  The timestamp indicating when the communication record was created.  | 
|  UpdatedDate  |  String  |  The timestamp indicating when the communication record was last updated.  | 
|  LastEventType  |  String  |  The event type of the last event ingested for this communication.  | 
|  Campaign  |  Campaign  |  Details about the campaign associated with this communication.  | 
|  Endpoint  |  Endpoint  |  Information about the endpoint used for this communication.  | 
|  Events  |  Map<String, Event>  |  A map of events where the key is the event type such as email delivered, opened or clicked. This tracks the last event of each unique event type that occurred during this communication.  | 
|  Attributes  |  Map<String, String>  |  Key-value pair of attributes of a standard communication record.  | 

 The standard communication record objects are indexed by the keys in the following table. 


|  Standard index name  |  Standard communication record field  | 
| --- | --- | 
|  \_communicationRecordId  |  CommunicationRecordId  | 

 For example, you can use `_communicationRecordId` as a key name with the [SearchProfiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_SearchProfiles.html) API to find a profile that has a communication record whose `CommunicationRecordId` matches with the search value. You can find the standard `communicationRecord` objects associated with a specific profile by using the [ListProfileObjects](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListProfileObjects.html) API with the `ProfileId` and `ObjectTypeName` set to `_communicationRecord`. 

## Campaign data type
<a name="campaign-data-type"></a>


|  Field  |  Data type  |  Description  | 
| --- | --- | --- | 
|  CampaignId  |  String  |  The unique ID for the outbound campaign.  | 
|  CampaignName  |  String  |  The name of the outbound campaign.  | 
|  CampaignRunId  |  String  |  The unique ID for a specific run of the campaign.  | 
|  CampaignActivityId  |  String  |  The unique ID of the activity within the campaign.  | 
|  SegmentArn  |  String  |  The ARN of a segment of users.  | 

## Endpoint data type
<a name="endpoint-data-type"></a>


|  Field  |  Data type  |  Description  | 
| --- | --- | --- | 
|  EndpointAddress  |  String  |  The address of the endpoint (for example, email address, phone number).  | 
|  EndpointType  |  String  |  The type of the endpoint such as default email or business email.  | 

## Event data type
<a name="event-data-type"></a>


|  Field  |  Data type  |  Description  | 
| --- | --- | --- | 
|  UpdatedDate  |  String  |  The timestamp indicating when the communication event occurred.  | 
|  EventId  |  String  |  The unique identifier for each communication event.  | 
|  EventType  |  String  |  The specific communication event type.  | 
|  Attributes  |  Map<String, String>  |  Key-value pair of attributes specific to the event type.  | 