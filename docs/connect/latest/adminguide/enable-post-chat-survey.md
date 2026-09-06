

# Enable post-chat survey
<a name="enable-post-chat-survey"></a>

With post-chat survey, you can collect end customer feedback immediately after a chat conversation ends. With the **`DisconnectOnCustomerExit`** parameter in the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API, you can configure automatic agent disconnection when end customer disconnects, making sure that disconnect flow is triggered consistently regardless of which participant disconnects first.

## Implementation options
<a name="post-chat-survey-implementation"></a>

There are two ways to enable post-chat survey:

### For Custom Chat Widget
<a name="post-chat-survey-custom-builder"></a>

If you're using a custom chat implementation:

1. Upgrade to the latest version of [amazon-connect-chatjs](https://github.com/amazon-connect/amazon-connect-chatjs).

1. Add the `DisconnectOnCustomerExit` parameter to your [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API request:

   ```
   {
       "DisconnectOnCustomerExit": ["AGENT"],
       // ... other StartChatContact parameters
   }
   ```

### For Connect Customer Communication Widget
<a name="post-chat-survey-communication-widget"></a>

If you're using the Connect Customer Communication Widget:

1. Open the Connect Customer console and navigate to **Communication widgets**.

1. Enable the post-chat survey setting through the Communication Widgets page.  
![The Communication Widget settings page showing the post-chat survey option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/post-chat-survey-communication-widget.png)

## Update contact flow to add post-chat survey as a disconnect flow
<a name="post-chat-survey-disconnect-flow"></a>

To enable post-chat survey, you'll need to update the disconnect flow that's connected to your chat solution. Once configured, the survey will automatically trigger when customers end their chat sessions.

For information about creating a disconnect flow, see [Example chat scenario](web-and-mobile-chat.md#example-chat-scenario).

There are two ways to implement a survey in your disconnect flow:
+ **Option \#1: Using ShowView block** - Use the [Flow block in Connect Customer: Show view](show-view-block.md) to display a custom survey interface.
+ **Option \#2: Using Lex** - Integrate with Amazon Lex for text-based survey collection. For more information, see [Add an Amazon Lex bot to Connect Customer](amazon-lex.md).

**Note**  
For supervisor barge-in scenarios, make sure you add a [Flow block in Connect Customer: Set working queue](set-working-queue.md) block before **Transfer to Queue**. Omitting it will cause chat contacts to terminate rather than transfer for this feature.  

![A flow diagram showing the Set Working Queue block before Transfer to Queue for supervisor barge-in scenarios.](http://docs.aws.amazon.com/connect/latest/adminguide/images/post-chat-survey-set-working-queue-block.png)


**Contact Trace Records**  
When a customer ends a chat session, Connect Customer sets `disconnectReason` to `CUSTOMER_DISCONNECT` in the [ContactTraceRecord](ctr-data-model.md#ctr-ContactTraceRecord). When `DisconnectOnCustomerExit` is configured, the system generates a new contact ID (`nextContactId`) and initiates the configured disconnect flow.  
Example:  

```
{
    "contactId": "104c05e3-abscdfre",
    "nextContactId": "4cbae06d-ca5b-1234567",
    "channel": "CHAT",
    "initiationMethod": "DISCONNECT",
    "disconnectReason": "CUSTOMER_DISCONNECT"
}
```
[How contact attributes work in Connect Customer](what-is-a-contact-attribute.md) will update in Contact Search and Contact Details.  

![Contact details showing the contact attributes for a post-chat survey.](http://docs.aws.amazon.com/connect/latest/adminguide/images/post-chat-survey-contact-attributes.png)


## Additional resources
<a name="post-chat-survey-additional-resources"></a>
+ [StartChatContact API](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html)
+ [Sample inbound flow in Connect Customer for the first contact experience](sample-inbound-flow.md)
+ [Example chat scenario](web-and-mobile-chat.md#example-chat-scenario)
+ [Flow block in Connect Customer: Set working queue](set-working-queue.md)
+ [Flow block in Connect Customer: Transfer to queue](transfer-to-queue.md)
+ [Connect Customer ShowView](https://docs.aws.amazon.com/connect/latest/adminguide/show-view-block.html)
+ [Connect Customer with Lex](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-lex.html)
+ [How contact attributes work in Connect Customer](what-is-a-contact-attribute.md)