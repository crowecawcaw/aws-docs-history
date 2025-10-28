# Update shared routes in AWS End User Messaging SMS

In some countries, AWS End User Messaging SMS maintains a pool of shared origination identities. When you
activate shared routes, AWS End User Messaging SMS makes an effort to deliver your message using one of the
shared identities. The origination identity could be a sender ID, long code or short code
and could vary within each country. When shared routes uses a sender ID as the origination identity, the sender ID
will be a generic sender ID, such as `NOTICE`. Shared identities are unavailable in some countries,
including the United States.

###### Note

Shared routes can be subject to increased downstream filtering and dedicated routes, where available, are preferred.

###### Turn on shared routes (AWS Management Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone pools**.
3. On the **Phone Pools** page, choose the pool that will have
   shared routes enabled.
4. On the **Shared routes** tab, choose the **Edit settings**
   button.
5. Choose **Enable shared routes** and then **Save
   changes**.
