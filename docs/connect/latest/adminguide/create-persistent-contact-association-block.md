

# Flow block in Connect Customer: Create persistent contact association
<a name="create-persistent-contact-association-block"></a>

This topic defines the flow block for creating a persistent contact association, enabling conversations with contacts to continue where they left off.

## Description
<a name="create-persistent-contact-association-description"></a>
+ Enables persistent chat experience on the current chat.
+ With persistent chat, you can select the required rehydration mode. For more information about chat rehydration, see [Enable customers to resume chat conversations in Connect Customer](chat-persistence.md). 

## Supported channels
<a name="create-persistent-contact-association-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | No - Error branch | 
| Chat | Yes | 
| Task | No - Error branch | 

## Flow types
<a name="create-persistent-contact-association-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer Queue flow
+ Customer hold flow
+ Customer whisper flow
+ Outbound whisper flow
+ Agent hold flow
+ Agent whisper flow
+ Transfer to agent flow
+ Transfer to queue flow

## Properties
<a name="create-persistent-contact-association-properties"></a>

The following image shows the **Properties** page of the **Create persistent contact association** block.

![The properties page of the Create persistent contact associations block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/create-persistent-contact-association-properties.png)


## Configuration tips
<a name="create-persistent-contact-association-tips"></a>
+ To enable persistent chat you can add the **Create persistent contact association** block to your flow, or provide the previous `contactId` in the `SourceContactId` parameter of the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API, but not both. You can enable persistence of a `SourceContactID` on a new chat only once.

  We recommend that you enable persistent chat by using the **Create persistent contact association** block when using the following features:
  + [Connect Customer chat widget](add-chat-to-website.md)
  + [Apple Messages for Business](apple-messages-for-business.md)
+ You can configure persistent chats to rehydrate the entire past chat conversation or rehydrate from a specific segment of a past chat conversation. For information about rehydration types, see [Enable customers to resume chat conversations in Connect Customer](chat-persistence.md).

## Configured block
<a name="create-persistent-contact-association-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has two branches: **Success** and **Error**. 

![A configured Create persistent contact associations block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/create-persistent-contact-association-configured.png)
