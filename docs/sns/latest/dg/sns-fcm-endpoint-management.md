

# Amazon SNS management of Firebase Cloud Messaging endpoints
<a name="sns-fcm-endpoint-management"></a>

## Managing and maintaining device tokens
<a name="sns-managing-device-tokens"></a>

You can ensure deliverability of your mobile application's push notifications by following these steps:

1. Store all device tokens, corresponding Amazon SNS endpoint ARNs, and timestamps on your application server.

1. Remove all stale tokens and delete the corresponding Amazon SNS endpoint ARNs.

Upon your app's initial start-up, you'll receive a device token (also referred to as registration token) for the device. This device token is minted by the device’s operating system, and is tied to your FCM application. Once you receive this device token, you can register it with Amazon SNS as a platform endpoint. We recommend that you store the device token, the Amazon SNS platform endpoint ARN, and the timestamp by saving the them to your application server, or another persistent store. To set-up your FCM application to retrieve and store device tokens, see [Retrieve and store registration tokens](https://firebase.google.com/docs/cloud-messaging/manage-tokens#retrieve-and-store-registration-tokens) in Google's *Firebase* documentation.

It's important that you maintain up-to-date tokens. Your user’s device tokens can change under the following conditions:

1. The mobile application is restored on a new device.

1. The user uninstalls or updates the application.

1. The user clears application data.

When your device token changes, we recommended that you update the corresponding Amazon SNS endpoint with the new token. This allows Amazon SNS to continue communication to the registered device. You can do this by implementing the following pseudo code within your mobile application. It describes a recommended practice for creating and maintaining enabled platform endpoints. This approach can be executed each time the mobile applications starts, or as a scheduled job in the background.

### Pseudo code
<a name="sns-device-token-pseudo-code"></a>

Use the following FCM pseudo code to manage and maintain device tokens.

```
retrieve the latest token from the mobile OS
if (endpoint arn not stored)
    # first time registration
    call CreatePlatformEndpoint
    store returned endpoint arn
endif

call GetEndpointAttributes on the endpoint arn 

if (getting attributes encountered NotFound exception)
    #endpoint was deleted 
    call CreatePlatformEndpoint
    store returned endpoint arn
else 
    if (token in endpoint does not match latest) or 
        (GetEndpointAttributes shows endpoint as disabled)
        call SetEndpointAttributes to set the 
                     latest token and enable the endpoint
    endif
endif
```

To learn more about token update requirements, see [Update Tokens on a Regular Basis](https://firebase.google.com/docs/cloud-messaging/manage-tokens#update-tokens-on-a-regular-basis) in Google's *Firebase* documentation.

## Detecting invalid tokens
<a name="sns-detecting-invalid-tokens"></a>

When a message is dispatched to an FCM v1 endpoint with an invalid device token, Amazon SNS will receive one of the following exceptions:
+ `UNREGISTERED` (HTTP 404) – When Amazon SNS receives this exception, you will receive a delivery failure event with a `FailureType` of `InvalidPlatformToken`, and a `FailureMessage` of *Platform token associated with the endpoint is not valid*. Amazon SNS will disable your platform endpoint when a delivery fails with this exception.
+ `INVALID_ARGUMENT` (HTTP 400) – When Amazon SNS receives this exception, it means that the device token or the message payload is invalid. For more information, see [ErrorCode](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode) in Google's *Firebase* documentation.

Since `INVALID_ARGUMENT` can be returned in either of these cases, Amazon SNS will return a `FailureType` of `InvalidNotification`, and a `FailureMessage` of *Notification body is invalid*. When you receive this error, verify that your payload is correct. If it is correct, verify that the device token is up-to-date. Amazon SNS will not disable your platform endpoint when a delivery fails with this exception.

Another case where you will experience an `InvalidPlatformToken` delivery failure event is when the registered device token doesn't belong to the application attempting to send that message. In this case, Google will return a *SENDER\_ID\_MISMATCH* error. Amazon SNS will disable your platform endpoint when a delivery fails with this exception.

All observed error codes received from the FCM v1 API are available to you in CloudWatch when you set up [delivery status logging](topics-attrib.md) for your application. 

To receive delivery events for your application, see [Available application events](application-event-notifications.md#application-event-notifications-events).

## Removing stale tokens
<a name="sns-removing-stale-tokens"></a>

Tokens are considered stale once message deliveries to the endpoint device start failing. Amazon SNS sets these stale tokens as disabled endpoints for your platform application. When you publish to a disabled endpoint, Amazon SNS will return a `EventDeliveryFailure` event with the `FailureType` of `EndpointDisabled`, and a `FailureMessage` of *Endpoint is disabled*. To receive delivery events for your application, see [Available application events](application-event-notifications.md#application-event-notifications-events).

When you receive this error from Amazon SNS, you need to remove or update the stale token in your platform application.