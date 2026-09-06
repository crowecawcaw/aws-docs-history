

# StartOutboundChatContact
<a name="contact-actions-startoutboundchatcontact"></a>

Initiate an outbound chat contact to a customer. Only SMS chats are supported. For more information, see the [StartOutboundChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html) in the *Connect Customer API Reference*. 

## Parameter object
<a name="startoutboundchatcontact-parameter"></a>

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
<a name="startoutboundchatcontact-results"></a>

None. No conditions are supported.

## Errors
<a name="startoutboundchatcontact-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="startoutboundchatcontact-restrictions"></a>
+ This action only supports `connect:SMS` as the **ContactSubtype** currently.
+ This action only supports `CONNECT_PHONENUMBER_ARN` as the Type of **SourceEndpoint** currently.
+ This action only supports `TELEPHONE_NUMBER` as the Type of **DestinationEndpoint** currently.

## Corresponding block in the UI
<a name="startoutboundchatcontact-ui"></a>

[Send message](https://docs.aws.amazon.com/connect/latest/adminguide/send-message.html) 