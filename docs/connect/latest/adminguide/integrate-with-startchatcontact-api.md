

# Start chats in your applications by using Connect Customer APIs
<a name="integrate-with-startchatcontact-api"></a>

Use the StartChatContact API in Connect Customer APIs to start chats in your own applications.

To start a chat, use the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API.

When you explore the chat experience for the first time, you'll notice that chats aren't counted in the **Contacts Incoming** metric in your historical metrics report. This is because the initiation method for the chat in the contact record is **API**. 

The following image of a contact record shows the *Initiation Method* set to *API*. 

![A contact record, the initiation method set to API.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-api.png)


After a chat is transferred to an agent, the **Contacts Incoming** metric is incremented. The contact record for the transfer no longer increments the API, but it does increment **Contacts Incoming**. 