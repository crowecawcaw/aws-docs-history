# Event

Represents item interaction event information sent using the
`PutEvents` API.

## Contents

**eventType**

The type of event, such as click or download. This property corresponds to the `EVENT_TYPE`
field of your Item interactions dataset's schema and depends on the types of events you are tracking.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**sentAt**

The timestamp (in Unix time) on the client side when the event occurred.

Type: Timestamp

Required: Yes

**eventId**

An ID associated with the event. If an event ID is not provided, Amazon Personalize generates
a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses
the event ID to distinguish unique events. Any subsequent events after the first with the
same event ID are not used in model training.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**eventValue**

The event value that corresponds to the `EVENT_VALUE` field of the Item interactions schema.

Type: Float

Required: No

**impression**

A list of item IDs that represents the sequence of items you have shown the user. For example, `["itemId1", "itemId2", "itemId3"]`. Provide a list of
items to manually record impressions data for an event. For more information on recording impressions data,
see [Recording impressions data](recording-events.md#putevents-including-impressions-data "recording-events.md#putevents-including-impressions-data").

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 25 items.

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**itemId**

The item ID key that corresponds to the `ITEM_ID` field of the Item interactions dataset's schema.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**metricAttribution**

Contains information about the metric attribution associated with an event. For more information about metric attributions, see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

Type: [MetricAttribution](API_UBS_MetricAttribution.md "API_UBS_MetricAttribution.md") object

Required: No

**properties**

A string map of event-specific data that you might choose to record. For example, if a
user rates a movie on your site, other than movie ID (`itemId`) and rating (`eventValue`)
, you might also send the number of movie ratings made by the user.

Each item in the map consists of a key-value pair. For example,

`{"numberOfRatings": "12"}`

The keys use camel case names that match the fields in the Item interactions dataset's
schema. In the above example, the `numberOfRatings` would match the
'NUMBER_OF_RATINGS' field defined in the Item interactions dataset's schema.

The following can't be included as a keyword for properties (case insensitive).

- userId
- sessionId
- eventType
- timestamp
- recommendationId
- impression

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

**recommendationId**

The ID of the list of recommendations that contains the item the user interacted with. Provide a `recommendationId` to have Amazon Personalize implicitly record the
recommendations you show your user as impressions data. Or provide a `recommendationId` if you use a metric attribution to measure the impact of recommendations.

For more information on recording impressions data, see [Recording impressions data](recording-events.md#putevents-including-impressions-data "recording-events.md#putevents-including-impressions-data").
For more information on creating a metric attribution see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 40.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/Event.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/Event.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Event.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Event.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Event.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Event.md")
