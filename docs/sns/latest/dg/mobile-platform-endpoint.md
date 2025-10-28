# Setting up an Amazon SNS platform endpoint for mobile

notifications

When an app and mobile device register with a push notification service (such as APNs or
Firebase Cloud Messaging), the push notification service returns a device token. Amazon SNS uses this device
token to create a platform endpoint, which acts as a target for sending direct push
notification messages to the app on the device. The platform endpoint serves as a bridge,
routing messages sent by Amazon SNS to the push notification service for delivery to the
corresponding mobile device. For more information, see [Prerequisites for Amazon SNS
user notifications](sns-prerequisites-for-mobile-push-notifications.md "sns-prerequisites-for-mobile-push-notifications.md") and [Setting up push notifications with
Amazon SNS](sns-mobile-application-as-subscriber.md#sns-user-notifications-process-overview "sns-mobile-application-as-subscriber.md#sns-user-notifications-process-overview").

## Understanding device tokens and

platform endpoints

A device token uniquely identifies a mobile device registered with a push notification
service (for example, APNs, Firebase Cloud Messaging). When an app registers with the push notification
service, it generates a device token specific to that app and device. Amazon SNS uses this
device token to create a platform endpoint within the corresponding platform
application.

The platform endpoint allows Amazon SNS to send push notification messages to the device
through the push notification service, maintaining the connection between your app and
the user's device.

## Create a platform endpoint

To push notifications to an app with Amazon SNS, that app's device token must first be
registered with Amazon SNS by calling the create platform endpoint action. This action takes
the Amazon Resource Name (ARN) of the platform application and the device token as
parameters and returns the ARN of the created platform endpoint.

The [`CreatePlatformEndpoint`](../api/API_CreatePlatformEndpoint.md "../api/API_CreatePlatformEndpoint.md") action does the following:

- If the platform endpoint already exists, do not create it again. Return to the
  caller the ARN of the existing platform endpoint.
- If the platform endpoint with the same device token but different settings
  already exists, do not create it again. Throw an exception to the caller.
- If the platform endpoint does not exist, create it. Return to the caller the
  ARN of the newly-created platform endpoint.

You should not call the create platform endpoint action immediately every time an app
starts, because this approach does not always provide a working endpoint. This can
happen, for example, when an app is uninstalled and reinstalled on the same device and
the endpoint for it already exists but is disabled. A successful registration process
should accomplish the following:

1. Ensure a platform endpoint exists for this app-device combination.
2. Ensure the device token in the platform endpoint is the latest valid device
   token.
3. Ensure the platform endpoint is enabled and ready to use.

## Pseudo code

The following pseudo code describes a recommended practice for creating a working,
current, enabled platform endpoint in a wide variety of starting conditions. This
approach works whether this is a first time the app is being registered or not, whether
the platform endpoint for this app already exists, and whether the platform endpoint is
enabled, has the correct device token, and so on. It is safe to call it multiple times
in a row, as it will not create duplicate platform endpoints or change an existing
platform endpoint if it is already up to date and enabled.

```
retrieve the latest device token from the mobile operating system
if (the platform endpoint ARN is not stored)
  # this is a first-time registration
  call create platform endpoint
  store the returned platform endpoint ARN
endif

call get endpoint attributes on the platform endpoint ARN

if (while getting the attributes a not-found exception is thrown)
  # the platform endpoint was deleted
  call create platform endpoint with the latest device token
  store the returned platform endpoint ARN
else
  if (the device token in the endpoint does not match the latest one) or
      (`GetEndpointAttributes` shows the endpoint as disabled)
    call set endpoint attributes to set the latest device token and then enable the platform endpoint
  endif
endif
```

This approach can be used any time the app wants to register or re-register itself. It
can also be used when notifying Amazon SNS of a device token change. In this case, you can
just call the action with the latest device token value. Some points to note about this
approach are:

- There are two cases where it may call the create platform endpoint action. It
  may be called at the very beginning, where the app does not know its own
  platform endpoint ARN, as happens during a first-time registration. It is also
  called if the initial `GetEndpointAttributes` action call fails with
  a not-found exception, as would happen if the application knows its endpoint ARN
  but it was deleted.
- The `GetEndpointAttributes` action is called to verify the platform
  endpoint's state even if the platform endpoint was just created. This happens
  when the platform endpoint already exists but is disabled. In this case, the
  create platform endpoint action succeeds but does not enable the platform
  endpoint, so you must double-check the state of the platform endpoint before
  returning success.

## AWS SDK example

The following code shows how to implement the previous pseudo code using the Amazon SNS
clients that are provided by the AWS SDKs.

To use an AWS SDK, you must configure it with your credentials. For more
information, see [The shared config and credentials
files](../../../sdkref/latest/guide/creds-config-files.md "../../../sdkref/latest/guide/creds-config-files.md") in the _AWS SDKs and Tools Reference Guide_.

CLI

**AWS CLI**

**To create a platform application endpoint**

The following `create-platform-endpoint` example creates an endpoint for the specified platform application using the specified token.

```
`aws sns create-platform-endpoint \
 --platform-application-arn `arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication` \
 --token `EXAMPLE12345...``

```

Output:

```
{
      "EndpointArn": "arn:aws:sns:us-west-2:1234567890:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234"
}
```

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.CreatePlatformEndpointRequest;
import software.amazon.awssdk.services.sns.model.CreatePlatformEndpointResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * In addition, create a platform application using the AWS Management Console.
 * See this doc topic:
 *
 * https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-register.html
 *
 * Without the values created by following the previous link, this code examples
 * does not work.
 */

public class RegistrationExample {
    public static void main(String[] args) {
        final String usage = """

            Usage:     <token> <platformApplicationArn>

            Where:
               token - The device token or registration ID of the mobile device. This is a unique
               identifier provided by the device platform (e.g., Apple Push Notification Service (APNS) for iOS devices, Firebase Cloud Messaging (FCM)
               for Android devices) when the mobile app is registered to receive push notifications.

               platformApplicationArn - The ARN value of platform application. You can get this value from the AWS Management Console.\s

            """;

        if (args.length != 2) {
            System.out.println(usage);
            return;
        }

        String token = args[0];
        String platformApplicationArn = args[1];
        SnsClient snsClient = SnsClient.builder()
            .region(Region.US_EAST_1)
            .build();

        createEndpoint(snsClient, token, platformApplicationArn);
    }
    public static void createEndpoint(SnsClient snsClient, String token, String platformApplicationArn) {
        System.out.println("Creating platform endpoint with token " + token);
        try {
            CreatePlatformEndpointRequest endpointRequest = CreatePlatformEndpointRequest.builder()
                .token(token)
                .platformApplicationArn(platformApplicationArn)
                .build();

            CreatePlatformEndpointResponse response = snsClient.createPlatformEndpoint(endpointRequest);
            System.out.println("The ARN of the endpoint is " + response.endpointArn());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
        }
    }
}


```

For more information, see [Mobile push API actions](mobile-push-api.md "mobile-push-api.md").

## Troubleshooting

### Repeatedly calling

create platform endpoint with an outdated device token

Especially for FCM endpoints, you may think it is best to store the first device
token the application is issued and then call the create platform endpoint with that
device token every time on application start-up. This may seem correct since it
frees the app from having to manage the state of the device token and Amazon SNS will
automatically update the device token to its latest value. However, this solution
has a number of serious issues:

- Amazon SNS relies on feedback from FCM to update expired device tokens to new
  device tokens. FCM retains information about old device tokens for some
  time, but not indefinitely. Once FCM forgets about the connection between
  the old device token and the new device token, Amazon SNS will no longer be able
  to update the device token stored in the platform endpoint to its correct
  value; it will just disable the platform endpoint instead.
- The platform application will contain multiple platform endpoints
  corresponding to the same device token.
- Amazon SNS imposes a quota on the number of platform endpoints that can be
  created starting with the same device token. Eventually, the creation of new
  endpoints will fail with an invalid parameter exception and the following
  error message: "This endpoint is already registered with a different
  token."

For more information on managing FCM endpoints, see [Amazon SNS management of Firebase Cloud Messaging
endpoints](sns-fcm-endpoint-management.md "sns-fcm-endpoint-management.md").

### Re-enabling a platform

endpoint associated with an invalid device token

When a mobile platform (such as APNs or FCM) informs Amazon SNS that the device
token used in the publish request was invalid, Amazon SNS disables the platform endpoint
associated with that device token. Amazon SNS will then reject subsequent publishes to
that device token. While you may think it is best to simply re-enable the platform
endpoint and keep publishing, in most situations doing this will not work: the
messages that are published do not get delivered and the platform endpoint becomes
disabled again soon afterward.

This is because the device token associated with the platform endpoint is
genuinely invalid. Deliveries to it cannot succeed because it no longer corresponds
to any installed app. The next time it is published to, the mobile platform will
again inform Amazon SNS that the device token is invalid, and Amazon SNS will again disable
the platform endpoint.

To re-enable a disabled platform endpoint, it needs to be associated with a valid
device token (with a set endpoint attributes action call) and then enabled. Only
then will deliveries to that platform endpoint become successful. The only time
re-enabling a platform endpoint without updating its device token will work is when
a device token associated with that endpoint used to be invalid but then became
valid again. This can happen, for example, when an app was uninstalled and then
re-installed on the same mobile device and receives the same device token. The
approach presented above does this, making sure to only re-enable a platform
endpoint after verifying that the device token associated with it is the most
current one available.
