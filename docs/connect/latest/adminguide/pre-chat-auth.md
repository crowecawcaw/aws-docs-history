# Pre-chat authentication using the Amazon Connect StartChatContact

API

Customers who authenticate in your website or mobile application before starting a
chat can be recognized as authenticated when a chat is initiated. You can do this by
using the [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md")
API.

After an authenticated customer starts a chat, set their status using the parameters
in the [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md")
API, as shown in the following code snippet:

```
"SegmentAttributes": {
    "connect:CustomerAuthentication" : {
        "ValueMap": {
            "Status": {
                "ValueString": "AUTHENTICATED"
            }
        }
    },
    "CustomerId": "`12345`"
```

`CustomerId` is an optional field to identify the customer. This can be
either an Amazon Connect Customer Profiles ID or a custom identifier from an external system, such as a
CRM.
