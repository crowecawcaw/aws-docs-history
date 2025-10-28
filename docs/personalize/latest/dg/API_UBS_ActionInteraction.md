# ActionInteraction

Represents an action interaction event sent using the
`PutActionInteractions` API.

## Contents

**actionId**

The ID of the action the user interacted with. This corresponds to the `ACTION_ID`
field of the Action interaction schema.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**eventType**

The type of action interaction event. You can specify `Viewed`, `Taken`, and `Not Taken` event types. For more
information about action interaction event type data, see [Event type data](action-interaction-event-type-data.md "action-interaction-event-type-data.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**sessionId**

The ID associated with the user's visit.
Your application generates a unique `sessionId` when a user first visits your website or uses your application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**timestamp**

The timestamp for when the action interaction event occurred. Timestamps must be in Unix epoch time format, in seconds.

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

**impression**

A list of action IDs that represents the sequence of actions you have shown the user. For example, `["actionId1", "actionId2", "actionId3"]`.
Amazon Personalize doesn't use impressions data from action interaction events. Instead, record multiple events for each action and use the `Viewed` event type.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 25 items.

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**properties**

A string map of event-specific data that you might choose to record. For example, if a
user takes an action, other than the action ID, you might also send the number of actions taken by the user.

Each item in the map consists of a key-value pair. For example,

`{"numberOfActions": "12"}`

The keys use camel case names that match the fields in the Action interactions
schema. In the above example, the `numberOfActions` would match the
'NUMBER_OF_ACTIONS' field defined in the Action interactions schema.

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

The ID of the list of recommendations that contains the action the user interacted with.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 40.

Required: No

**userId**

The ID of the user who interacted with the action. This corresponds to the `USER_ID`
field of the Action interaction schema.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/ActionInteraction.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/ActionInteraction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/ActionInteraction.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/ActionInteraction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/ActionInteraction.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/ActionInteraction.md")
