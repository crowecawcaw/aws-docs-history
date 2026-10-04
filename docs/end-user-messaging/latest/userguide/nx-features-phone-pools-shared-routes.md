

# Update shared routes in AWS End User Messaging
<a name="nx-features-phone-pools-shared-routes"></a>

In some countries, AWS End User Messaging maintains a pool of shared origination identities. When you activate shared routes, AWS End User Messaging makes an effort to deliver your message using one of the shared identities. The origination identity could be a sender ID, long code or short code and could vary within each country. When shared routes uses a sender ID as the origination identity, the sender ID will be a generic sender ID, such as `NOTICE`. Shared identities are unavailable in some countries, including the United States.

**Note**  
Shared routes can be subject to increased downstream filtering and dedicated routes, where available, are preferred.

**Important**  
Shared routes are not supported for RCS sending. If your pool or account contains an AWS RCS Agent and a message is routed to the RCS path, messages that cannot be delivered as RCS do not fall back to shared routes. To provide SMS fallback for RCS messages, ensure the pool or account contains a dedicated originator (phone number or sender ID) that is valid for the destination country.

**Turn on shared routes (Console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**.

1. On the **Phone Pools** page, choose the pool that will have shared routes enabled.

1. On the **Shared routes** tab, choose the **Edit settings** button.

1. Choose **Enable shared routes** and then **Save changes**.