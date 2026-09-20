

# Configure calling for a phone number
<a name="whatsapp-calling-settings"></a>

You configure calling for each phone number using its call settings. Call settings include whether calling is enabled, the hours during which your business accepts calls, the visibility of the call button in WhatsApp, and the callback permission behavior.

**Call settings**
+ **Calling enabled** – Turns calling on or off for the phone number.
+ **Call hours** – The hours during which your business accepts calls, defined as a weekly schedule in a time zone that you choose. Each day can have up to two time ranges, and you can add date-specific overrides for holidays. When call hours are not enabled, your business accepts calls at any time.
+ **Call icon visibility** – Controls whether the call button appears to users in WhatsApp.
+ **Callback permission** – Controls whether inbound callers are prompted to grant your business permission to call them back.

The available values for call icon visibility and callback permission are determined by Meta. For more information, see the [WhatsApp calling documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/calling) from Meta.

## Configure calling for a phone number
<a name="whatsapp-calling-settings_steps"></a>

To turn on and configure calling for a phone number, update the phone number's call settings.

1. Open the AWS End User Messaging Social console at [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/).

1. In **Business accounts**, choose the WhatsApp Business Account (WABA) that contains the phone number.

1. On the **Phone numbers** tab, choose the phone number that you want to configure.

1. In **Call settings**, turn on calling, and then set the call hours, call icon visibility, and callback permission for the phone number.

1. Choose **Save**.

To configure calling with the API, use the `UpdateLinkedWhatsAppBusinessAccountPhoneNumber` operation and provide the call settings for the phone number. To view the current call settings, use the `GetLinkedWhatsAppBusinessAccountPhoneNumber` operation.