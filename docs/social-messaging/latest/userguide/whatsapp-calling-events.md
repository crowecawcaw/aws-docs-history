

# Send call events
<a name="whatsapp-calling-events"></a>

You send WhatsApp call events, such as connecting or ending a call, using the `SendWhatsAppCallEvent` operation. AWS End User Messaging Social passes the call event through to Meta's calling API. The operation returns the call identifier that Meta assigns to the call.

The request includes the origination phone number, the version of the Meta Graph API to use, and the call event. The call event is a JSON payload in the format defined by Meta's calling API, and AWS End User Messaging Social passes it through without modification. The Meta Graph API version and the call event format are defined by Meta. For the call event schema and supported API versions, see the [WhatsApp calling documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/calling) from Meta.