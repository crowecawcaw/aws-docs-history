

# Supported features and versions
<a name="appium-endpoint-support"></a>

During a remote access session, you can select the major version of the Appium server that runs on your device. Choose the version that supports the Appium features that your tests require.

The Device Farm Appium endpoint also supports most of the same commands and desired capabilities that you use on local devices, with a few exceptions. The following sections list the capabilities and commands that aren't supported.

**Topics**
+ [Supported Appium server versions](#appium-endpoint-supported-versions)
+ [Supported capabilities](#appium-endpoint-unsupported-capabilities)
+ [Supported commands](#appium-endpoint-unsupported-commands)

## Supported Appium server versions
<a name="appium-endpoint-supported-versions"></a>

The following table lists the supported Appium server major versions in remote access sessions, and the device operating system (OS) versions that each version supports.


| Appium server version | Supported Android versions | Supported iOS versions | 
| --- | --- | --- | 
|  3  | All versions | 15 and above | 
|  2  | All versions | 15 and above | 

**Note**  
The set of supported versions might change over time. We recommend that you check this page for the current list.

You must set the Appium server version on iOS devices running version 27 or later. On older devices, selecting a version is optional. If you don't specify a version, Device Farm uses server version 2 on those devices.

### Select a server version
<a name="appium-endpoint-selecting-version"></a>

To select a version, set the `appium:version` parameter in your request with the desired major version as the value. If that version isn't available for the device, Device Farm rejects the request.

------
#### [ Console ]

**To create a remote access session with a selected Appium server version**

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, create a project by following the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md).

1. On the **Remote access** tab, choose **Create remote access session**.

1. Choose a device from the list of available devices, or use the search bar at the top of the list to find one.

1. In **Session name**, enter a name for the session.

1. *(Optional)* Under **Select applications**, include your own app or choose the Device Farm Sample App as part of the session. These can be newly uploaded apps, or apps previously uploaded to this project. App uploads [expire after 30 days](data-protection.md#data-protection-retention).

1. Under **Advanced Configuration**, for **Appium server version**, choose the major version that you want to use. If you don't select a version, the Device Farm console uses a pre-selected version for the device. This pre-selected version might change over time.

1. Choose **Confirm and start session**.

------
#### [ AWS CLI ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS CLI v2.

```
$ aws devicefarm create-remote-access-session \
    --project-arn "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}" \
    --device-arn "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}" \
    --configuration '{"parameters":{"appium:version":"{{3}}"}}'
```

------
#### [ Node.js ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS SDK for JavaScript v3 with Node.js 18 or later.

```
import { DeviceFarmClient, CreateRemoteAccessSessionCommand } from "@aws-sdk/client-device-farm";

const client = new DeviceFarmClient({ region: "us-west-2" });

const command = new CreateRemoteAccessSessionCommand({
  projectArn: "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
  deviceArn: "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
  configuration: { parameters: { "appium:version": "{{3}}" } },
});

const resp = await client.send(command);
```

------
#### [ Python ]

The following example creates a remote access session with a selected Appium server version.

```
import boto3

client = boto3.client("devicefarm", region_name="us-west-2")

resp = client.create_remote_access_session(
    projectArn="{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    deviceArn="{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
    configuration={"parameters": {"appium:version": "{{3}}"}},
)
```

------
#### [ Java ]

The following example creates a remote access session with a selected Appium server version.

This example uses the AWS SDK for Java v2.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionConfiguration;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionResponse;

import java.util.Map;

public class SelectAppiumVersionExample {
    public static void main(String[] args) {
        try (DeviceFarmClient client = DeviceFarmClient.builder()
                .region(Region.US_WEST_2)
                .build()) {

            CreateRemoteAccessSessionConfiguration configuration = CreateRemoteAccessSessionConfiguration.builder()
                    .parameters(Map.of("appium:version", "{{3}}"))
                    .build();
            CreateRemoteAccessSessionRequest request = CreateRemoteAccessSessionRequest.builder()
                    .projectArn("{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}")
                    .deviceArn("{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}")
                    .configuration(configuration)
                    .build();

            CreateRemoteAccessSessionResponse resp = client.createRemoteAccessSession(request);
        }
    }
}
```

------
#### [ Ruby ]

The following example creates a remote access session with a selected Appium server version.

```
require 'aws-sdk-devicefarm'

client = Aws::DeviceFarm::Client.new(region: 'us-west-2')

resp = client.create_remote_access_session(
  project_arn: "{{arn:aws:devicefarm:us-west-2:111122223333:project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
  device_arn: "{{arn:aws:devicefarm:us-west-2::device:EXAMPLE123DEVICE456}}",
  configuration: { parameters: { "appium:version" => "{{3}}" } }
)
```

------

## Supported capabilities
<a name="appium-endpoint-unsupported-capabilities"></a>

When creating an Appium session on Device Farm, we recommend having a distinct set of capabilities which exclude any capabilities specific to your local device. On Device Farm, session creation may fail if certain unsupported capabilities are set. This includes device-specific capabilities like `udid` and `platformVersion`. Additionally, certain capabilities related to ChromeDriver on Android and WebDriverAgent on iOS aren't supported, as well as capabilities that are only supported on emulators and simulators.

## Supported commands
<a name="appium-endpoint-unsupported-commands"></a>

Most Appium commands that run properly on real Android and iOS devices will run as-expected on Device Farm, with the following exclusions: 

### Appium device commands (`/appium/device`)
<a name="appium-endpoint-unsupported-device-commands"></a>
+ `install_app`
+ `finger_print`
+ `send_sms`
+ `gsm_call`
+ `gsm_signal`
+ `gsm_voice`
+ `power_ac`
+ `power_capacity`
+ `network_speed`
+ `shake`

### Appium execute methods and scripts (`/execute`)
<a name="appium-endpoint-unsupported-execute-methods"></a>
+ `installApp`
+ `execEmuConsoleCommand`
+ `fingerprint`
+ `gsmCall`
+ `gsmSignal`
+ `sendSms`
+ `gsmVoice`
+ `powerAC`
+ `powerCapacity`
+ `networkSpeed`
+ `sensorSet`
+ `injectEmulatorCameraImage`
+ `isGpsEnabled`
+ `shake`
+ `clearApp`
+ `clearKeychains`
+ `configureLocalization`
+ `enrollBiometric`
+ `getPasteboard`
+ `installXCTestBundle`
+ `listXCTestBundles`
+ `listXCTestsInTestBundle`
+ `runXCTest`
+ `sendBiometricMatch`
+ `setPasteboard`
+ `setPermission`
+ `startAudioRecording`
+ `startLogsBroadcast`
+ `startRecordingScreen`
+ `startScreenStreaming`
+ `startXCTestScreenRecording`
+ `stopAudioRecording`
+ `stopLogsBroadcast`
+ `stopRecordingScreen`
+ `stopScreenStreaming`
+ `stopXCTestScreenRecording`
+ `updateSafariPreferences`