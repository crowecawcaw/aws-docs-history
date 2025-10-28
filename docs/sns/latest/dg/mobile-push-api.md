# Mobile push API actions

To use the Amazon SNS mobile push APIs, you must first meet the prerequisites for the push
notification service, such as Apple Push Notification Service (APNs) and Firebase Cloud Messaging (FCM). For more
information about the prerequisites, see [Prerequisites for Amazon SNS
user notifications](sns-prerequisites-for-mobile-push-notifications.md "sns-prerequisites-for-mobile-push-notifications.md").

To send a push notification message to a mobile app and device using the APIs, you must
first use the `CreatePlatformApplication` action, which returns a
`PlatformApplicationArn` attribute. The `PlatformApplicationArn`
attribute is then used by `CreatePlatformEndpoint`, which returns an
`EndpointArn` attribute. You can then use the `EndpointArn`
attribute with the `Publish` action to send a notification message to a mobile
app and device, or you could use the `EndpointArn` attribute with the
`Subscribe` action for subscription to a topic. For more information, see
[Setting up push notifications with
Amazon SNS](sns-mobile-application-as-subscriber.md#sns-user-notifications-process-overview "sns-mobile-application-as-subscriber.md#sns-user-notifications-process-overview").

The Amazon SNS mobile push APIs are as follows:

`CreatePlatformApplication`

Creates a platform application object for one of the supported push
notification services, such as APNs and FCM, to which devices and mobile
apps may register. Returns a `PlatformApplicationArn` attribute,
which is used by the `CreatePlatformEndpoint` action.

`CreatePlatformEndpoint`

Creates an endpoint for a device and mobile app on one of the supported push
notification services. `CreatePlatformEndpoint` uses the
`PlatformApplicationArn` attribute returned from the
`CreatePlatformApplication` action. The `EndpointArn`
attribute, which is returned when using `CreatePlatformEndpoint`, is
then used with the `Publish` action to send a notification message to
a mobile app and device.

`CreateTopic`

Creates a topic to which messages can be published.

`DeleteEndpoint`

Deletes the endpoint for a device and mobile app on one of the supported push
notification services.

`DeletePlatformApplication`

Deletes a platform application object.

`DeleteTopic`

Deletes a topic and all its subscriptions.

`GetEndpointAttributes`

Retrieves the endpoint attributes for a device and mobile app.

`GetPlatformApplicationAttributes`

Retrieves the attributes of the platform application object.

`ListEndpointsByPlatformApplication`

Lists the endpoints and endpoint attributes for devices and mobile apps in a
supported push notification service.

`ListPlatformApplications`

Lists the platform application objects for the supported push notification
services.

`Publish`

Sends a notification message to all of a topic's subscribed endpoints.

`SetEndpointAttributes`

Sets the attributes for an endpoint for a device and mobile app.

`SetPlatformApplicationAttributes`

Sets the attributes of the platform application object.

`Subscribe`

Prepares to subscribe an endpoint by sending the endpoint a confirmation
message. To actually create a subscription, the endpoint owner must call the
ConfirmSubscription action with the token from the confirmation message.

`Unsubscribe`

Deletes a subscription.
