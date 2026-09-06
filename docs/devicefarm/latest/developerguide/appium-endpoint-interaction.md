# Interacting with the device using Appium

After you [create a remote access session](how-to-create-session.md "how-to-create-session.md"), the device will be
available for Appium testing. For the duration of the remote access session, you can run as many Appium sessions
as you want on the device, with no limits on what clients you use. For example, you can start by running a test
using your local Appium code from your IDE, then switch to using Appium Inspector to troubleshoot any issues you
encounter. The session can last up to [150 minutes](limits.md#service-limits "limits.md#service-limits"). However, if there is no
activity for more than 5 minutes (through either the interactive console or the Appium endpoint), the session
times out.

## Using apps for testing with your Appium session

There are several ways to provide an app for use with your Appium session:

- Upload an app to Device Farm and install it in the session.
- Specify an HTTPS URL or an Amazon Simple Storage Service (Amazon S3) URI as the `appium:app`
  capability.
- Reference an already-installed app by its package name (using `appium:appPackage` on Android or `appium:bundleId` on iOS).
- Test a web app by specifying the `browserName` capability (`Chrome` on Android, `Safari` on iOS).

Standard [app size limits](limits.md#file-limits "limits.md#file-limits") (4 GB) apply to all app sources.

###### Note

Device Farm does not support passing a local filesystem path in `appium:app` during a remote access session.

### Uploading, installing, and using apps

To use an uploaded app with your Appium session, follow these steps:

1. ###### Upload and install your app

There are two ways to upload and install an app onto the device under test:

    * Include the app ARN in your [`CreateRemoteAccessSession`](../APIReference/API_CreateRemoteAccessSession.md "../APIReference/API_CreateRemoteAccessSession.md") request. The app is automatically installed onto the device when the session starts. You can also include auxiliary app ARNs, which will be installed alongside the primary app.
    * Install the app during an active session using the [`InstallToRemoteAccessSession`](../APIReference/API_InstallToRemoteAccessSession.md "../APIReference/API_InstallToRemoteAccessSession.md") API, or by uploading it through the Device Farm console. This allows you to change the app under test without creating a new session.

2. ###### Use the installed app

Once installed, the app is automatically injected as the default `appium:app` capability for any subsequent Appium sessions. If you included auxiliary apps, they are set as the `appium:otherApps` capability.

For example, if you create a remote access session using `com.aws.devicefarm.sample` as your app, and `com.aws.devicefarm.other.sample` as one of your auxiliary apps, then when you go to create an Appium session, it will have capabilities similar to the following:

```
{
    "value":
    {
        "sessionId": "abcdef123456-1234-5678-abcd-abcdef123456",
        "capabilities":
        {
            "app": "/tmp/com.aws.devicefarm.sample.apk",
            "otherApps": "[\"/tmp/com.aws.devicefarm.other.sample.apk\"]",
            ...
        }
    }
}
```

If you install a new app during the session, it replaces the current `appium:app` capability. If the previously installed app has a distinct package name, it remains on the device and moves to the `appium:otherApps` capability.

For example, if you initially use `com.aws.devicefarm.sample` when creating your
remote access session, but then install `com.aws.devicefarm.other.sample` during the
session, your Appium sessions will have capabilities similar to the following:

```
{
    "value":
    {
        "sessionId": "abcdef123456-1234-5678-abcd-abcdef123456",
        "capabilities":
        {
            "app": "/tmp/com.aws.devicefarm.other.sample.apk",
            "otherApps": "[\"/tmp/com.aws.devicefarm.sample.apk\"]",
            ...
        }
    }
}
```

###### Note

For more information about automatically uploading apps as part of your
remote access session, see [Automating Device Farm](api-ref.md "api-ref.md").

### Using an HTTPS URL

You can specify a publicly accessible HTTPS URL as the `appium:app` desired capability when creating an Appium session. The URL must point directly to a downloadable app file (for example, an `.apk` or `.ipa` file). Device Farm downloads the app from the specified URL and installs it onto the device under test.

###### Important

Only HTTPS URLs are supported. Plain HTTP URLs are rejected.

For example, the following Appium session creation request downloads an app from an HTTPS URL:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:app": "https://example.com/path/to/MyApp.apk"
            }
        ]
    }
}
```

### Using an Amazon S3 URI

You can specify an Amazon S3 URI (for example,
`s3://amzn-s3-demo-bucket/path/to/MyApp.ipa`) as the
`appium:app` desired capability when creating an Appium session.
Device Farm downloads the app from the specified Amazon S3 location and installs it onto the
device under test.

To use an Amazon S3 URI, the following requirements must be met:

- The remote access session must be started from a project that has an [IAM execution role](custom-test-environments-iam-roles.md "custom-test-environments-iam-roles.md") configured.
- The IAM execution role must have a maximum session duration of at least 150 minutes. This is
  the case because the role is assumed for the duration of the remote access session.
- The IAM execution role must have permission to call `s3:GetObject` on the S3
  object specified in the URI. This permission also authorizes the `HeadObject` API
  call on the same object, which allows Device Farm to validate the object's existence before attempting
  the download.

For example, the following Appium session creation request downloads an app from
an Amazon S3 URI:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:app": "s3://amzn-s3-demo-bucket/apps/MyApp.ipa"
            }
        ]
    }
}
```

The following is an example of an IAM permissions policy that grants the recommended access for
downloading an app from Amazon S3. The `s3:GetObject` permission also authorizes the
`HeadObject` API call, which is used to validate the object's existence. For more
information about configuring IAM execution roles, see [Access AWS resources using an IAM Execution Role](custom-test-environments-iam-roles.md "custom-test-environments-iam-roles.md").

###### Example

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/apps/*"
    }
  ]
}
```

### Using an already-installed app

If the app you want to test is already installed on the device, you can reference it directly by its package name instead of uploading it. Use the `appium:appPackage` and `appium:appActivity` capabilities on Android, or the `appium:bundleId` capability on iOS.

For example, the following Appium session creation request launches an Android app that's already
installed:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:appPackage": "com.example.myapp",
                "appium:appActivity": "com.example.myapp.MainActivity"
            }
        ]
    }
}
```

On iOS, use `appium:bundleId` instead:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "appium:bundleId": "com.example.myapp"
            }
        ]
    }
}
```

### Testing a web app

To test a web app, specify the `browserName` capability in your Appium session creation request. Use `Chrome` on Android devices or `Safari` on iOS devices.

For example, the following request opens Chrome on an Android device:

```
{
    "capabilities":
    {
        "alwaysMatch": {},
        "firstMatch":
        [
            {
                "browserName": "Chrome"
            }
        ]
    }
}
```

## How to use the Appium endpoint

Here are the steps to access the session's Appium endpoint from the console, the AWS CLI, and the AWS
SDKs. These steps include how to get started with running tests by using various Appium client testing
frameworks:

Console

1. Open your remote access session page in your web browser:

![The remote access session page](images/aws-device-farm-appium-endpoint.png) 2. For running a session by using Appium Inspector, do the following:

    1. Choose **Setup Appium session**.
    2. Follow the instructions on the page to start a session by using Appium
     Inspector.

3. For running an Appium test from your local IDE, do the following:

    1. Choose the copy icon next to **Appium endpoint URL**.
    2. Paste the copied URL into your local Appium code wherever you currently
     specify your remote address or command executor. For language-specific examples,
     refer to other tabs in this section.

AWS CLI
First, verify that your AWS CLI version is up-to-date by [downloading and installing the latest version](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Important

The Appium endpoint field isn't available in older versions of the AWS CLI.

Once your session is up and running, the Appium endpoint URL will be available via a field
named `remoteDriverEndpoint` in the response to a call to the
[`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
`$` `aws devicefarm get-remote-access-session \
 --arn "arn:aws:devicefarm:us-west-2:123456789876:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"`
```

This will show output such as the following:

```
`{
 "remoteAccessSession": {
 "arn": "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000",
 "name": "Google Pixel 8",
 "status": "RUNNING",
 "endpoints": {
 "remoteDriverEndpoint": "https://devicefarm-interactive-global.us-west-2.api.aws/remote-endpoint/ABCD1234...",
 ...
}`
```

You can use this URL in your local Appium code wherever you currently specify your remote
address or command executor. For language-specific examples, please click one of the tabs in
this example window for your language of choice.

For an example of how to interact with the endpoint directly from the command line, you can
use the [command-line tool curl](https://curl.se/ "https://curl.se/") to call a WebDriver
endpoint directly:

```
`$` `curl "https://devicefarm-interactive-global.us-west-2.api.aws/remote-endpoint/ABCD1234.../status"`
```

This will show output such as the following:

```
`{
 "value":
 {
 "ready": true,
 "message": "The server is ready to accept new connections",
 "build":
 {
 "version": "2.5.1"
 }
 }
}`
```

Python
Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
# To get the URL
import sys
import boto3
from botocore.exceptions import ClientError

def get_appium_endpoint() -> str:
    session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"
    device_farm_client = boto3.client("devicefarm", region_name="us-west-2")

    try:
        resp = device_farm_client.get_remote_access_session(arn=session_arn)
    except ClientError as exc:
        sys.exit(f"Failed to call Device Farm: {exc}")

    remote_access_session = resp.get("remoteAccessSession", {})
    endpoints = remote_access_session.get("endpoints", {})
    endpoint = endpoints.get("remoteDriverEndpoint")

    if not endpoint:
        sys.exit("Device Farm response did not include endpoints.remoteDriverEndpoint")

    return endpoint

# To use the URL
from appium import webdriver
from appium.options.android import UiAutomator2Options

opts = UiAutomator2Options()
driver = webdriver.Remote(get_appium_endpoint(), options=opts)
# ...
driver.quit()
```

Java
_Note: this example uses the AWS SDK for Java v2, and is compatible with JDK versions 11 and higher._

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
// To get the URL
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionResponse;

public class AppiumEndpointBuilder {
    public static String getAppiumEndpoint() throws Exception {
        String session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build()) {

            GetRemoteAccessSessionResponse resp = client.getRemoteAccessSession(
                    GetRemoteAccessSessionRequest.builder().arn(session_arn).build()
            );

            String endpoint = resp.remoteAccessSession().endpoints().remoteDriverEndpoint();
            if (endpoint == null || endpoint.isEmpty()) {
                throw new IllegalStateException("remoteDriverEndpoint missing from response");
            }
            return endpoint;
        }
    }
}

// To use the URL
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;

import java.net.URL;

public class ExampleTest {
    public static void main(String[] args) throws Exception {
        String endpoint = AppiumEndpointBuilder.getAppiumEndpoint();
        UiAutomator2Options options = new UiAutomator2Options();
        AndroidDriver driver = new AndroidDriver(new URL(endpoint), options);

        try {
            // ... your test ...
        } finally {
            driver.quit();
        }
    }
}
```

JavaScript
_Note: this example uses AWS SDK for JavaScript v3 and WebdriverIO v8+ using Node 18+._

Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
// To get the URL
import { DeviceFarmClient, GetRemoteAccessSessionCommand } from "@aws-sdk/client-device-farm";

export async function getAppiumEndpoint() {
  const sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

  const client = new DeviceFarmClient({ region: "us-west-2" });
  const resp = await client.send(new GetRemoteAccessSessionCommand({ arn: sessionArn }));

  const endpoint = resp?.remoteAccessSession?.endpoints?.remoteDriverEndpoint;
  if (!endpoint) throw new Error("remoteDriverEndpoint missing from response");
  return endpoint;
}

// To use the URL with WebdriverIO
import { remote } from "webdriverio";

(async () => {
  const endpoint = await getAppiumEndpoint();
  const u = new URL(endpoint);

  const driver = await remote({
    protocol: u.protocol.replace(":", ""),
    hostname: u.hostname,
    port: u.port ? Number(u.port) : (u.protocol === "https:" ? 443 : 80),
    path: u.pathname + u.search,
    capabilities: {
      platformName: "Android",
      "appium:automationName": "UiAutomator2",
      // ...other caps...
    },
  });

  try {
    // ... your test ...
  } finally {
    await driver.deleteSession();
  }
})();
```

C#
Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
// To get the URL
using System;
using System.Threading.Tasks;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

public static class AppiumEndpointBuilder
{
    public static async Task<string> GetAppiumEndpointAsync()
    {
        var sessionArn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000";

        var config = new AmazonDeviceFarmConfig
        {
            RegionEndpoint = RegionEndpoint.USWest2
        };
        using var client = new AmazonDeviceFarmClient(config);

        var resp = await client.GetRemoteAccessSessionAsync(new GetRemoteAccessSessionRequest { Arn = sessionArn });
        var endpoint = resp?.RemoteAccessSession?.Endpoints?.RemoteDriverEndpoint;

        if (string.IsNullOrWhiteSpace(endpoint))
            throw new InvalidOperationException("RemoteDriverEndpoint missing from response");

        return endpoint;
    }
}

// To use the URL
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Android;

class Example
{
    static async Task Main()
    {
        var endpoint = await AppiumEndpointBuilder.GetAppiumEndpointAsync();

        var options = new AppiumOptions();
        options.PlatformName = "Android";
        options.AutomationName = "UiAutomator2";

        using var driver = new AndroidDriver(new Uri(endpoint), options);
        try
        {
            // ... your test ...
        }
        finally
        {
            driver.Quit();
        }
    }
}
```

Ruby
Once your session is up and running, the Appium endpoint URL will be available via a field named `remoteDriverEndpoint` in the response to a call to the [`GetRemoteAccessSession`](../APIReference/API_GetRemoteAccessSession.md "../APIReference/API_GetRemoteAccessSession.md") API:

```
# To get the URL
require 'aws-sdk-devicefarm'

def get_appium_endpoint
  session_arn = "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000"

  client = Aws::DeviceFarm::Client.new(region: 'us-west-2')
  resp = client.get_remote_access_session(arn: session_arn)
  endpoint = resp.remote_access_session.endpoints.remote_driver_endpoint
  raise "remote_driver_endpoint missing from response" if endpoint.nil? || endpoint.empty?
  endpoint
end

# To use the URL
require 'appium_lib_core'

endpoint = get_appium_endpoint
opts = {
  server_url: endpoint,
  capabilities: {
    'platformName' => 'Android',
    'appium:automationName' => 'UiAutomator2'
  }
}

driver = Appium::Core.for(opts).start_driver
begin
  # ... your test ...
ensure
  driver.quit
end
```
