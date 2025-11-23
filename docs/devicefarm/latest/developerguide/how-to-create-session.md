# Creating a remote access session in AWS Device Farm

For information about remote access sessions, see [Sessions](sessions.md "sessions.md").

- [Prerequisites](#how-to-create-session-prerequisites "#how-to-create-session-prerequisites")
- [Create a remote session](#how-to-create-remote-session "#how-to-create-remote-session")
- [Next steps](#how-to-create-session-next-steps "#how-to-create-session-next-steps")

## Prerequisites

- Create a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md"), and
  then return to this page.

## Create a remote session

Console

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. If you already have a project, choose it from the list. Otherwise, create a project by following the
   instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md").
4. On the **Remote access** tab, choose **Create remote access session**.
5. Choose a device for your session. You can choose from the list of available devices or search for a
   device using the search bar at the top of the list.
6. _(Optional)_ Include an app and auxiliary apps as part of the session. These can be newly uploaded apps, or apps previously uploaded in this project from the past 30 days (after 30 days, app uploads [will expire](data-protection.md#data-protection-retention "data-protection.md#data-protection-retention")).
7. In **Session name**, enter a name for the session.
8. Choose **Confirm and start session**.

AWS CLI
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

First, verify that your AWS CLI version is up-to-date by [downloading and installing the latest version](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Important

Certain commands mentioned in this document aren't available in older versions of the AWS CLI.

Then, you can determine which device you'd like to test on:

```
`$` `aws devicefarm list-devices`
```

This will show output such as the following:

```
`{
 "devices":
 [
 {
 "arn": "arn:aws:devicefarm:us-west-2::device:DE5BD47FF3BD42C3A14BF7A6EFB1BFE7",
 "name": "Google Pixel 8",
 "remoteAccessEnabled": true,
 "availability": "HIGHLY_AVAILABLE"
 ...
 },
 ...
 ]
}`
```

Then, you can create your remote access session with a device ARN of your choice:

```
`$` `aws devicefarm create-remote-access-session \
 --project-arn arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef \
 --device-arn arn:aws:devicefarm:us-west-2::device:DE5BD47FF3BD42C3A14BF7A6EFB1BFE7 \
 --app-arn arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef \
 --configuration '{
 "auxiliaryApps": [
 "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
 "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
 ]
 }'`
```

This will show output such as the following:

```
`{
 "remoteAccessSession": {
 "arn": "arn:aws:devicefarm:us-west-2:111122223333:session:abcdef123456-1234-5678-abcd-abcdef123456/abcdef123456-1234-5678-abcd-abcdef123456/00000",
 "name": "Google Pixel 8",
 "status": "PENDING",
 ...
}`
```

Now, optionally, we can poll and wait for the session to be ready:

```
`$` `POLL_INTERVAL=3
TIMEOUT=600
DEADLINE=$(( $(date +%s) + TIMEOUT ))

while [[ "$(date +%s)" -lt "$DEADLINE" ]]; do

 STATUS=$(aws devicefarm get-remote-access-session \
 --arn "$DEVICE_FARM_SESSION_ARN" \
 --query 'remoteAccessSession.status' \
 --output text)

 case "$STATUS" in
 RUNNING)
 echo "Session is ready with status: $STATUS"
 break
 ;;
 STOPPING|COMPLETED)
 echo "Session ended early with status: $STATUS"
 exit 1
 ;;
 esac

done`
```

Python
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import random
import time
import boto3

client = boto3.client("devicefarm", region_name="us-west-2")

# 1) Gather all matching devices via paginated ListDevices with filters
filters = [
    {"attribute": "MODEL",        "operator": "CONTAINS", "values": ["Pixel"]},
    {"attribute": "AVAILABILITY", "operator": "EQUALS",   "values": ["AVAILABLE"]},
]

matching_arns = []
next_token = None
while True:
    args = {"filters": filters}
    if next_token:
        args["nextToken"] = next_token
    page = client.list_devices(**args)
    for d in page.get("devices", []):
        matching_arns.append(d["arn"])
    next_token = page.get("nextToken")
    if not next_token:
        break

if not matching_arns:
    raise RuntimeError("No available Google Pixel device found.")

# Randomly select one device from the full matching set
device_arn = random.choice(matching_arns)
print("Selected device ARN:", device_arn)

# 2) Create remote access session and wait until RUNNING
resp = client.create_remote_access_session(
    projectArn="arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
    deviceArn=device_arn,
    appArn="arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef",  # optional
    configuration={
        "auxiliaryApps": [  # optional
            "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
            "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1",
        ]
    },
)

session_arn = resp["remoteAccessSession"]["arn"]
print(f"Created Remote Access Session: {session_arn}")

poll_interval = 3
timeout = 600
deadline = time.time() + timeout
terminal_states = ["STOPPING", "COMPLETED"]

while True:
    out = client.get_remote_access_session(arn=session_arn)
    status = out["remoteAccessSession"]["status"]
    print(f"Current status: {status}")

    if status == "RUNNING":
        print(f"Session is ready with status: {status}")
        break
    if status in terminal_states:
        raise RuntimeError(f"Session ended early with status: {status}")
    if time.time() >= deadline:
        raise RuntimeError("Timed out waiting for session to be ready.")
    time.sleep(poll_interval)
```

Java
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

_Note: this example uses the AWS SDK for Java v2, and is compatible with JDK versions 11 and higher._

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.DeviceFarmClient;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionConfiguration;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.CreateRemoteAccessSessionResponse;
import software.amazon.awssdk.services.devicefarm.model.Device;
import software.amazon.awssdk.services.devicefarm.model.DeviceFilter;
import software.amazon.awssdk.services.devicefarm.model.DeviceFilterAttribute;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionRequest;
import software.amazon.awssdk.services.devicefarm.model.GetRemoteAccessSessionResponse;
import software.amazon.awssdk.services.devicefarm.model.ListDevicesRequest;
import software.amazon.awssdk.services.devicefarm.model.ListDevicesResponse;
import software.amazon.awssdk.services.devicefarm.model.RuleOperator;

public class CreateRemoteAccessSession {
  public static void main(String[] args) throws Exception {
    DeviceFarmClient client = DeviceFarmClient.builder()
        .region(Region.US_WEST_2)
        .build();

    String projectArn = "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef";
    String appArn     = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef";
    String aux1       = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0";
    String aux2       = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1";

    // 1) Gather all matching devices via paginated ListDevices with filters
    List<DeviceFilter> filters = Arrays.asList(
        DeviceFilter.builder()
            .attribute(DeviceFilterAttribute.MODEL)
            .operator(RuleOperator.CONTAINS)
            .values("Pixel")
            .build(),
        DeviceFilter.builder()
            .attribute(DeviceFilterAttribute.AVAILABILITY)
            .operator(RuleOperator.EQUALS)
            .values("AVAILABLE")
            .build()
    );

    List<String> matchingDeviceArns = new ArrayList<>();
    String next = null;
    do {
      ListDevicesResponse page = client.listDevices(
          ListDevicesRequest.builder().filters(filters).nextToken(next).build());
      for (Device d : page.devices()) {
        matchingDeviceArns.add(d.arn());
      }
      next = page.nextToken();
    } while (next != null);

    if (matchingDeviceArns.isEmpty()) {
      throw new RuntimeException("No available Google Pixel device found.");
    }

    // Randomly select one device from the full matching set
    String deviceArn = matchingDeviceArns.get(
        ThreadLocalRandom.current().nextInt(matchingDeviceArns.size()));
    System.out.println("Selected device ARN: " + deviceArn);

    // 2) Create Remote Access session and wait until it is RUNNING
    CreateRemoteAccessSessionConfiguration cfg = CreateRemoteAccessSessionConfiguration.builder()
        .auxiliaryApps(Arrays.asList(aux1, aux2))
        .build();

    CreateRemoteAccessSessionResponse res = client.createRemoteAccessSession(
        CreateRemoteAccessSessionRequest.builder()
            .projectArn(projectArn)
            .deviceArn(deviceArn)
            .appArn(appArn)       // optional
            .configuration(cfg)   // optional
            .build());

    String sessionArn = res.remoteAccessSession().arn();
    System.out.println("Created Remote Access Session: " + sessionArn);

    int pollIntervalMs = 3000;
    long timeoutMs = 600_000L;
    long deadline = System.currentTimeMillis() + timeoutMs;

    while (true) {
      GetRemoteAccessSessionResponse get = client.getRemoteAccessSession(
          GetRemoteAccessSessionRequest.builder().arn(sessionArn).build());
      String status = get.remoteAccessSession().statusAsString();
      System.out.println("Current status: " + status);

      if ("RUNNING".equals(status)) {
        System.out.println("Session is ready with status: " + status);
        break;
      }
      if ("STOPPING".equals(status) || "COMPLETED".equals(status)) {
        throw new RuntimeException("Session ended early with status: " + status);
      }
      if (System.currentTimeMillis() >= deadline) {
        throw new RuntimeException("Timed out waiting for session to be ready.");
      }
      Thread.sleep(pollIntervalMs);
    }
  }
}
```

JavaScript
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

_Note: this example uses AWS SDK for JavaScript v3._

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
import {
  DeviceFarmClient,
  ListDevicesCommand,
  CreateRemoteAccessSessionCommand,
  GetRemoteAccessSessionCommand,
} from "@aws-sdk/client-device-farm";

const client = new DeviceFarmClient({ region: "us-west-2" });

// 1) Gather all matching devices via paginated ListDevices with filters
const filters = [
  { attribute: "MODEL",        operator: "CONTAINS", values: ["Pixel"] },
  { attribute: "AVAILABILITY", operator: "EQUALS",   values: ["AVAILABLE"] },
];

let nextToken;
const matching = [];

while (true) {
  const page = await client.send(new ListDevicesCommand({ filters, nextToken }));
  for (const d of page.devices ?? []) {
    matching.push(d.arn);
  }
  nextToken = page.nextToken;
  if (!nextToken) break;
}

if (matching.length === 0) {
  throw new Error("No available Google Pixel device found.");
}

// Randomly select one device from the full matching set
const deviceArn = matching[Math.floor(Math.random() * matching.length)];
console.log("Selected device ARN:", deviceArn);

// 2) Create remote access session and wait until RUNNING
const out = await client.send(new CreateRemoteAccessSessionCommand({
  projectArn: "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
  deviceArn,
  appArn: "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", // optional
  configuration: {
    auxiliaryApps: [ // optional
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1",
    ],
  },
}));

const sessionArn = out.remoteAccessSession?.arn;
console.log("Created Remote Access Session:", sessionArn);

const pollIntervalMs = 3000;
const timeoutMs = 600000;
const deadline = Date.now() + timeoutMs;

while (true) {
  const get = await client.send(new GetRemoteAccessSessionCommand({ arn: sessionArn }));
  const status = get.remoteAccessSession?.status;
  console.log("Current status:", status);

  if (status === "RUNNING") {
    console.log("Session is ready with status:", status);
    break;
  }
  if (status === "STOPPING" || status === "COMPLETED") {
    throw new Error(`Session ended early with status: ${status}`);
  }
  if (Date.now() >= deadline) {
    throw new Error("Timed out waiting for session to be ready.");
  }
  await new Promise((r) => setTimeout(r, pollIntervalMs));
}
```

C#
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Amazon;
using Amazon.DeviceFarm;
using Amazon.DeviceFarm.Model;

class Program
{
    static async Task Main()
    {
        var client = new AmazonDeviceFarmClient(RegionEndpoint.USWest2);

        // 1) Gather all matching devices via paginated ListDevices with filters
        var filters = new List<DeviceFilter>
        {
            new DeviceFilter { Attribute = DeviceAttribute.MODEL,        Operator = RuleOperator.CONTAINS, Values = new List<string>{ "Pixel" } },
            new DeviceFilter { Attribute = DeviceAttribute.AVAILABILITY, Operator = RuleOperator.EQUALS,   Values = new List<string>{ "AVAILABLE" } },
        };

        var matchingArns = new List<string>();
        string nextToken = null;

        do
        {
            var list = await client.ListDevicesAsync(new ListDevicesRequest
            {
                Filters = filters,
                NextToken = nextToken
            });

            foreach (var d in list.Devices)
                matchingArns.Add(d.Arn);

            nextToken = list.NextToken;
        }
        while (nextToken != null);

        if (matchingArns.Count == 0)
            throw new Exception("No available Google Pixel device found.");

        // Randomly select one device from the full matching set
        var rnd = new Random();
        var deviceArn = matchingArns[rnd.Next(matchingArns.Count)];
        Console.WriteLine($"Selected device ARN: {deviceArn}");

        // 2) Create remote access session and wait until RUNNING
        var request = new CreateRemoteAccessSessionRequest
        {
            ProjectArn = "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
            DeviceArn  = deviceArn,
            AppArn     = "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", // optional
            Configuration = new CreateRemoteAccessSessionConfiguration
            {
                AuxiliaryApps = new List<string>
                {
                    "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
                    "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
                }
            }
        };

        request.Configuration.AuxiliaryApps.RemoveAll(string.IsNullOrWhiteSpace);

        var response = await client.CreateRemoteAccessSessionAsync(request);
        var sessionArn = response.RemoteAccessSession.Arn;
        Console.WriteLine($"Created Remote Access Session: {sessionArn}");

        var pollIntervalMs = 3000;
        var timeoutMs = 600000;
        var deadline = DateTime.UtcNow.AddMilliseconds(timeoutMs);

        while (true)
        {
            var get = await client.GetRemoteAccessSessionAsync(new GetRemoteAccessSessionRequest { Arn = sessionArn });
            var status = get.RemoteAccessSession.Status.Value;
            Console.WriteLine($"Current status: {status}");

            if (status == "RUNNING")
            {
                Console.WriteLine($"Session is ready with status: {status}");
                break;
            }
            if (status == "STOPPING" || status == "COMPLETED")
            {
                throw new Exception($"Session ended early with status: {status}");
            }
            if (DateTime.UtcNow >= deadline)
            {
                throw new TimeoutException("Timed out waiting for session to be ready.");
            }

            await Task.Delay(pollIntervalMs);
        }
    }
}
```

Ruby
_Note: these instructions focus only on creating a remote access session. For instructions on how to upload an app for use during your session, please see [automating app uploads.](api-ref.md#upload-example "api-ref.md#upload-example")_

This example first finds any available Google Pixel device on Device Farm, then creates a remote access session with it and waits until the session is running.

```
require 'aws-sdk-devicefarm'

client = Aws::DeviceFarm::Client.new(region: 'us-west-2')

# 1) Gather all matching devices via paginated ListDevices with filters
filters = [
  { attribute: 'MODEL',        operator: 'CONTAINS', values: ['Pixel'] },
  { attribute: 'AVAILABILITY', operator: 'EQUALS',   values: ['AVAILABLE'] },
]

matching_arns = []
next_token = nil
loop do
  resp = client.list_devices(filters: filters, next_token: next_token)
  resp.devices&.each { |d| matching_arns << d.arn }
  next_token = resp.next_token
  break unless next_token
end

abort "No available Google Pixel device found." if matching_arns.empty?

# Randomly select one device from the full matching set
device_arn = matching_arns.sample
puts "Selected device ARN: #{device_arn}"

# 2) Create remote access session and wait until RUNNING
resp = client.create_remote_access_session(
  project_arn: "arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef",
  device_arn:  device_arn,
  app_arn:     "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef", # optional
  configuration: {
    auxiliary_apps: [ # optional
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde0",
      "arn:aws:devicefarm:us-west-2:111122223333:upload:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcde1"
    ].compact
  }
)

session_arn = resp.remote_access_session.arn
puts "Created Remote Access Session: #{session_arn}"

poll_interval = 3
timeout = 600
deadline = Time.now + timeout
terminal = %w[STOPPING COMPLETED]

loop do
  get = client.get_remote_access_session(arn: session_arn)
  status = get.remote_access_session.status
  puts "Current status: #{status}"

  if status == 'RUNNING'
    puts "Session is ready with status: #{status}"
    break
  end

  abort "Session ended early with status: #{status}" if terminal.include?(status)
  abort "Timed out waiting for session to be ready." if Time.now >= deadline
  sleep poll_interval
end
```

## Next steps

Device Farm starts the session as soon as the requested device and infrastructure is available, typically within a few minutes. The
**Device Requested** dialog box appears until the session starts. To cancel the session
request, choose **Cancel request**.

If the selected device is unavailable or busy, the session status shows as **Pending Device**, indicating that you may need to wait for some time before the device is available for testing.

If your account has reached its concurrency limit for public metered or unmetered devices, the session status shows as **Pending concurrency**. For unmetered device slots, you can increase concurrency by [purchasing more device slots](how-to-purchase-device-slots.md "how-to-purchase-device-slots.md"). For metered pay-as-you-go devices, please contact AWS via a support ticket to request [a service quota increase](limits.md "limits.md").

When the session setup begins, it first shows a status of **In-Progress**, then a status of **Connecting** while your local web browser attempts to open a remote connection to the device.

After a session starts, if you should close the browser or browser tab without stopping the session or if
the connection between the browser and the internet is lost, the session remains active for five minutes.
After that, Device Farm ends the session. Your account is charged for the idle time.

After the session starts, you can interact with the device in the web browser, or test the device using [Appium](appium-endpoint.md "appium-endpoint.md").
