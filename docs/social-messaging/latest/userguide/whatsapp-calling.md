

# WhatsApp calling in AWS End User Messaging Social
<a name="whatsapp-calling"></a>

WhatsApp calling lets your business place and receive voice calls with WhatsApp users directly in the WhatsApp conversation, using the same business phone number that you use for messaging. A customer can move from a chat to a live voice call without leaving WhatsApp.

You control calling for each phone number in your WhatsApp Business Account (WABA). You can turn calling on or off, set the hours during which your business accepts calls, and control whether the call button appears to users in WhatsApp. You can also check whether you have permission to call a user before you place a call. Calling uses the WhatsApp calling APIs that Meta provides, and AWS End User Messaging Social passes your call events through to Meta.

**Note**  
WhatsApp calling is subject to Meta's requirements. A user must grant your business permission before you can call them, and the specific permission and eligibility rules are determined by Meta. For more information, see the [WhatsApp calling documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/calling) from Meta.

Business-initiated calling is subject to country restrictions that are set by Meta. The country code of the business phone number that you call from must be in a supported country. According to Meta, business-initiated calling is available in every location where the WhatsApp Cloud API is available, except the following countries, where it is not supported:
+ United States
+ Canada
+ Egypt
+ Vietnam
+ Nigeria

The country of the WhatsApp user that you call is not restricted. For the current list of supported countries, see the [WhatsApp calling documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling#business-initiated-calling) from Meta.

For information about pricing for WhatsApp calling, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Topics**
+ [Prerequisites for WhatsApp calling](whatsapp-calling-prerequisites.md)
+ [Configure calling for a phone number](whatsapp-calling-settings.md)
+ [Check calling permission for a user](whatsapp-calling-permission.md)
+ [Send call events](whatsapp-calling-events.md)