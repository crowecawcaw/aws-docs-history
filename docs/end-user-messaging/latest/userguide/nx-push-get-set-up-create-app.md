

# Step 2: Create an application and enable push channels
<a name="nx-push-get-set-up-create-app"></a>

An application is a storage container for your AWS End User Messaging Push settings and channels. Before you can send push notifications, you create an application and enable the push notification channels you want to use. To complete this procedure you are only required to enter an application name, and you can enable or disable any of the push channels at a later time. Before you enable a channel, make sure you have valid credentials for that push notification service, as described in the preceding section.

------
#### [ Console ]

**To create an application and enable push channels**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Choose **Create application**.

1. For **Application name**, enter the name for your application.

1. (Optional) To enable the **Apple Push Notification service (APNs)** channel, select **Enable**, and then for **Default authentication type** choose one of the following:

   1. If you choose **Key credentials**, provide the **Key ID** assigned to your signing key, the **Bundle identifier** assigned to your iOS app, the **Team identifier** assigned to your Apple developer account team, and the **Authentication key** .p8 file that you download from your Apple developer account.

   1. If you choose **Certificate credentials**, provide the **SSL certificate** .p12 file, the **Certificate password** if you assigned one, and the **Certificate type**.

1. (Optional) To enable the **Firebase Cloud Messaging (FCM)** channel, select **Enable**, and then for **Default authentication type** either choose **Token credentials (recommended)** and upload your service JSON file, or choose **Key credentials** and enter your key in **API key**.

1. (Optional) To enable the **Baidu Cloud Push** channel, select **Enable**, and then enter your **API key** and **Secret key**.

1. (Optional) To enable the **Amazon Device Messaging** channel, select **Enable**, and then enter your **Client ID** and **Client secret**.

1. Choose **Create application**.

------
#### [ AWS CLI ]

Create the application with the [create-app](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/create-app.html) command. The response includes the application `Id`, which you use when you enable channels and send.

```
$ aws pinpoint create-app \
> --create-application-request {{Name=ExampleApp}}
```

Enable a push channel on the application by providing that channel's credentials. For example, enable the APNs channel with [update-apns-channel](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/update-apns-channel.html), or the FCM channel with [update-gcm-channel](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/update-gcm-channel.html). Replace {{applicationId}} with the `Id` from the previous command.

```
$ aws pinpoint update-apns-channel \
> --application-id {{applicationId}} \
> --apns-channel-request Enabled=true
```

------