

# Set up a mobile application to use CloudWatch RUM
<a name="CloudWatch-RUM-web-mobile"></a>

To monitor mobile applications, you create an app monitor, configure it for mobile platforms, and integrate the AWS Distro for OpenTelemetry (ADOT) SDK into your application. Mobile RUM uses the OpenTelemetry Protocol (OTLP) to send telemetry data to a dedicated OTLP endpoint. 

## To create an app monitor for a mobile platform
<a name="mobile-platform-app-monitor"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Application Signals**, **RUM**.

1. Choose **Add app monitor**.

1. For **App monitor name**, enter a name to be used to identify this app monitor within the CloudWatch RUM console.

1. Select **Android** or **iOS** as the platform.

1. Under **Data storage**, you can choose to store copies of RUM OTEL log events and spans in CloudWatch Logs and configure retention. By default, the CloudWatch Logs log group retains the data for 30 days. You can adjust the retention period in the CloudWatch Logs console.

1. (Optional) Under **Resource Based Policy**, choose to add a resource-based policy to control who can send requests to your app monitor. If you choose **Create public policy**, a resource policy will be attached that enables anyone to send requests to your app monitor. For more information, see [Using resource-based policies with CloudWatch RUM](CloudWatch-RUM-resource-policies.md).

1. To enable AWS X-Ray tracing of sampled user sessions, choose **Active tracing** and select **Trace my service with AWS X-Ray**.

   If selected, OTEL spans generated during sampled user sessions are traced. You can then see traces and spans from these sessions in the RUM dashboard, and the X-Ray trace map and trace details pages. These user sessions will also show up as client pages in Application Signals after you have enabled it for your application.

1. (Optional) To add tags to the app monitor:

   1. Choose **Tags**, **Add new tag**.

   1. For **Key**, enter a name for the tag. You can add an optional value in **Value**.

   1. To add another tag, choose **Add new tag** again.

   For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/tagging/latest/userguide/tagging-resources.html) in the *AWS Tagging and Tag Editor User Guide*.

1. Choose **Add app monitor**.

1. In the **Sample code** section, you can copy the code snippet to add to your application. Using the AWS Distro for OpenTelemetry (ADOT) SDK, you can choose between **Manual Instrumentation** to configure the monitoring in your application code, or **Zero-Code Instrumentation** which requires minimal configuration changes.

   For both Android and iOS applications, Zero-Code Instrumentation is the simplest option as it automatically initializes telemetry collection using a configuration file. Manual Instrumentation gives you more control over the initialization and configuration process.

1. Choose **Copy** or **Download**, and then choose **Done**.

### iOS Application Setup
<a name="CloudWatch-RUM-ios-setup"></a>

For iOS applications, integrate the [AWS Distro for OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift) to enable RUM monitoring. The SDK supports iOS 16 and later versions and provides automatic instrumentation for common performance scenarios.

### Android Application Setup
<a name="CloudWatch-RUM-android-setup"></a>

For Android applications, integrate the [AWS Distro for OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android) to enable RUM monitoring. The SDK provides automatic instrumentation and supports both signed and unsigned authentication models.

## Authentication and Security
<a name="CloudWatch-RUM-authentication"></a>

Mobile RUM supports flexible authentication models as defined in their SDKs.
+ iOS applications use the [AWS Distro for OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift). 
+ Android applications use the [AWS Distro for OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android).