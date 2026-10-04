

# Setup Push Notifications
<a name="nx-push"></a>

AWS End User Messaging Push lets you engage the users of your mobile and web applications by sending push notifications to their devices. It supports four push notification services: Apple Push Notification service (APNs) for iOS devices and the Safari browser on macOS, Firebase Cloud Messaging (FCM) for Android and web, Amazon Device Messaging (ADM) for Amazon devices, and Baidu Cloud Push. Common use cases include transactional alerts such as order and delivery updates, re-engagement and promotional campaigns, breaking-news and time-sensitive notifications, and in-app event prompts.

You send push notifications with the Amazon Pinpoint API (the `mobiletargeting` namespace, which you call as `aws pinpoint` on the AWS CLI). The main send operation is `SendMessages`, which delivers a message to one or more endpoints and forwards it to the push notification service that matches each recipient device. Unlike the other AWS End User Messaging channels, which use the SMS and Voice v2 or Social Messaging APIs, Push uses the Amazon Pinpoint API.

**Key concepts**

The following concepts are central to sending push notifications with AWS End User Messaging.


| Concept | Description | 
| --- | --- | 
| Application | The top-level AWS End User Messaging Push resource that represents your mobile or web app. You create an application, then enable the push channels it uses. | 
| Push notification channel | A connection to a push notification service: APNs, FCM, ADM, or Baidu Cloud Push. You enable a channel and provide the provider credentials that authorize AWS End User Messaging Push to deliver through it. | 
| Provider credentials | The certificates or keys from Apple, Google, Amazon, or Baidu that authorize AWS End User Messaging Push to send through each service. You supply these when you enable a channel. | 
| Endpoint and device token | A specific destination for a push notification. Each device registers a token with its push notification service, and you address messages to that endpoint or token. | 
| Message payload | The notification content and presentation settings, in the format defined by the target push notification service. You construct the payload according to the requirements of APNs, FCM, ADM, or Baidu Cloud Push. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-push-get-set-up.md) | Create an application, enable the push channels you need with their provider credentials, and send a test notification. | You are new to Push and want a working test send. | 
| [Send a message](nx-push-send.md) | Send push notifications from your application to registered devices across your enabled channels. | You have an application with channels enabled and want to send from your own code. | 
| [Scale](nx-push-scale.md) | Monitor delivery, manage quotas, and apply best practices for production push. | You are sending in production and want to keep it healthy and grow. | 