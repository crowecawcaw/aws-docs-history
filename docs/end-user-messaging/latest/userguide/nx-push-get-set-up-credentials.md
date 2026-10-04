

# Step 1: Obtain provider credentials
<a name="nx-push-get-set-up-credentials"></a>

To set up AWS End User Messaging Push so that it can send push notifications to your apps, you first provide the credentials that authorize AWS End User Messaging Push to send messages to your app. The credentials that you provide depend on which push notification service you use.
+ For Apple Push Notification service (APNs), obtain either an encryption key and key ID, or a provider certificate, from your Apple developer account. For more information, see the guidance on establishing a token-based connection and a certificate-based connection to APNs in the Apple Developer documentation.
+ For Firebase Cloud Messaging (FCM), obtain your credentials through the Firebase console. For more information, see the Firebase Cloud Messaging documentation.
+ For Baidu Cloud Push, obtain your API key and secret key. For more information, see the Baidu Push documentation.
+ For Amazon Device Messaging (ADM), obtain your client ID and client secret. For more information, see the guidance on obtaining credentials in the Amazon Device Messaging documentation.

For APNs, you can authenticate with either a signing key or a TLS certificate. A signing key is a private key that AWS End User Messaging Push uses to cryptographically sign APNs authentication tokens. When you provide a signing key, AWS End User Messaging Push uses a token to authenticate with APNs for every push notification that you send, and you can send to both the APNs production and sandbox environments. Unlike a certificate, a signing key does not expire, you provide it only once, and you can use the same signing key for multiple apps. A TLS certificate authenticates with APNs when you send push notifications, can support both production and sandbox environments or the sandbox environment only, and expires after one year. When a certificate expires, you create a new one and provide it to AWS End User Messaging Push to renew push notification delivery.