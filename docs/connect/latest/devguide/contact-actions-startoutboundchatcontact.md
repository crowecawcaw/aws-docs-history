# StartOutboundChatContact

Initiate an outbound chat contact to a customer. Only SMS chats are supported. For
more information, see the [StartOutboundChatContact](../APIReference/API_StartOutboundChatContact.md "../APIReference/API_StartOutboundChatContact.md") in the _Connect Customer API
Reference_.

## Parameter object

```
{
    "SourceEndpoint": {
        "Address": ConnectPhoneNumberArn of the SourceEndpoint,
        "Type": Type of the SourceEndpoint, currently only supports CONNECT_PHONENUMBER_ARN
    },
    "DestinationEndpoint": {
        "Address": E164 phone number of the DestinationEndpoint,
        "Type": Type of the DestinationEndpoint, currently only supports TELEPHONE_NUMBER
    },
    "ContactFlowArn": ContactFlowArn of the flow to be executed for the new outbound chat,
    "ContactSubtype": Subtype of the new chat contact, currently only supports connect:SMS,
    "InitialSystemMessage": [Optional] {
        "Content": content of the initial system message to be sent to the DestinationEndpoint
    },
    "RelatedContact": [Optional] Only supported value is CURRENT
}
```

## Results and conditions

None. No conditions are supported.

## Errors

- NoMatchingError - if no other Error matches.

## Restrictions

- This action only supports `connect:SMS` as the
  **ContactSubtype** currently.
- This action only supports `CONNECT_PHONENUMBER_ARN` as the Type
  of **SourceEndpoint** currently.
- This action only supports `TELEPHONE_NUMBER` as the Type of
  **DestinationEndpoint** currently.

## Corresponding block in the UI

[Send message](../adminguide/send-message.md "../adminguide/send-message.md")
