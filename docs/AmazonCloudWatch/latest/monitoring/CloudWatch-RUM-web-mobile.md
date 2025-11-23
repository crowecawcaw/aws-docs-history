# Set up a mobile application to use

CloudWatch RUM

To monitor mobile applications, you create an app monitor, configure it for mobile
platforms, and integrate the AWS Distro for OpenTelemetry (ADOT) SDK into your
application. Mobile RUM uses the OpenTelemetry Protocol (OTLP) to send telemetry data to
a dedicated OTLP endpoint.

## To create an app monitor for a mobile platform

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**,
   **RUM**.
3. Choose **Add app monitor**.
4. For **App monitor name**, enter a name to be used to
   identify this app monitor within the CloudWatch RUM console.
5. Select **Android** or **iOS** as the
   platform.
6. Under **Data storage**, you can choose to store copies of
   RUM OTEL log events and spans in CloudWatch Logs and configure retention. By
   default, the CloudWatch Logs log group retains the data for 30 days. You can
   adjust the retention period in the CloudWatch Logs console.
7. (Optional) Under **Resource Based Policy**, choose to add
   a resource-based policy to control who can send requests to your app
   monitor. If you choose **Create public policy**, a resource
   policy will be attached that enables anyone to send requests to your app
   monitor. For more information, see [Using resource-based policies with
   CloudWatch RUM](CloudWatch-RUM-resource-policies.md "CloudWatch-RUM-resource-policies.md").
8. To enable AWS X-Ray tracing of sampled user sessions, choose
   **Active tracing** and select **Trace my
   service with AWS X-Ray**.

If selected, OTEL spans generated during sampled user sessions are traced.
You can then see traces and spans from these sessions in the RUM dashboard,
and the X-Ray trace map and trace details pages. These user sessions will
also show up as client pages in Application Signals after you have enabled
it for your application. 9. (Optional) To add tags to the app monitor:

    1. Choose **Tags**, **Add new
     tag**.
    2. For **Key**, enter a name for the tag. You can
     add an optional value in **Value**.
    3. To add another tag, choose **Add new tag**
     again.For more information, see [Tagging AWS

Resources](../../../tagging/latest/userguide/tagging-resources.md "../../../tagging/latest/userguide/tagging-resources.md") in the _AWS Tagging and Tag Editor User
Guide_. 10. Choose **Add app monitor**. 11. In the **Sample code** section, you can copy the code
snippet to add to your application. Using the AWS Distro for OpenTelemetry
(ADOT) SDK, you can choose between **Manual
Instrumentation** to configure the monitoring in your
application code, or **Zero-Code Instrumentation** which
requires minimal configuration changes.

For both Android and iOS applications, Zero-Code Instrumentation is the
simplest option as it automatically initializes telemetry collection using a
configuration file. Manual Instrumentation gives you more control over the
initialization and configuration process. 12. Choose **Copy** or **Download**, and
then choose **Done**.

### iOS Application Setup

For iOS applications, integrate the [AWS Distro for
OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift "https://github.com/aws-observability/aws-otel-swift") to enable RUM monitoring. The SDK
supports iOS 16 and later versions and provides automatic instrumentation for
common performance scenarios.

### Android Application Setup

For Android applications, integrate the [AWS Distro for
OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android "https://github.com/aws-observability/aws-otel-android") to enable RUM monitoring. The SDK
provides automatic instrumentation and supports both signed and unsigned
authentication models.

## Authentication and Security

Mobile RUM supports flexible authentication models as defined in their
SDKs.

- iOS applications use the [AWS Distro
  for OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift "https://github.com/aws-observability/aws-otel-swift").
- Android applications use the [AWS Distro
  for OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android "https://github.com/aws-observability/aws-otel-android").
