# Hub SDK client

The Hub SDK Client library serves as an interface between the managed integrations Hub SDK and your own protocol stack running on the same hub.
It exposes a set of public APIs to facilitate your protocol stack's interaction with the Device Hub SDK components. The use cases include
custom plugin control, custom plugin provisioner, and local controller.

###### Topics

- [Get your managed integrations Hub SDK](#custom-protocol-plugin-getting-started "#custom-protocol-plugin-getting-started")
- [About the Hub SDK toolkit](#custom-protocol-plugin-toolkit "#custom-protocol-plugin-toolkit")
- [Create your custom application with the Hub SDK client](#custom-protocol-plugin-create-app "#custom-protocol-plugin-create-app")
- [Running your custom application](#custom-protocol-plugin-running-application "#custom-protocol-plugin-running-application")
- [Hub SDK client API reference](hub-sdk-client-api-reference.md "hub-sdk-client-api-reference.md")
- [Data types](#custom-protocol-plugin-data-types "#custom-protocol-plugin-data-types")

## Get your managed integrations Hub SDK

The Hub SDK Client comes with the managed integrations SDK. Contact us from the [managed integrations console](https://console.aws.amazon.com/iot/home#/managed-integrations/intro "https://console.aws.amazon.com/iot/home#/managed-integrations/intro")
to access the hub SDK.

## About the Hub SDK toolkit

After download, you will see a `IotMI-DeviceSDK-Toolkit` folder, which contains all public header files and `.so` files that you can
consume in your application. The managed integrations team also provides an example `main.cpp` for demo purpose, along with the demo application
binary under `bin/` that you can directly execute. You can optionally use this as the starting point for your application.

## Create your custom application with the Hub SDK client

Use the following steps to create your custom application.

1. Include the header files (.h) and shared object files (.so) in your application.

You must include the public header files (.h) and shared object files(.so) in your application.
For the .so files, you can place them in a lib folder. The final layout will be similar to this:

```
├── include
│   ├── iotmi_device_sdk_client
│   │   └── iotmi_device_sdk_client_common_types.h
│   ├── iotmi_device_sdk_client.h
│   └── iotshd_status.h
├── lib
│   ├── libiotmi_devicesdk_client_module.so
│   └── libiotmi_log_c.so
```

2. Create a Hub SDK client in your main application.
   1. In your main application, you must first initialize the Hub SDK client before it can be used to process requests.
      You can simply construct the client with a `clientId`.
   2. After you have the client, you can connect it to the managed integrations Device SDK.

   The following is an example of creating the Hub SDK client and how to connect.

   ```
   #include <cstdlib>
   #include <string>
   #include "iotshd_status.h"
   #include "iotmi_device_sdk_client.h"

   auto client = std::make_unique<DeviceSDKClient>(`your_own_clientId`);
   iotmi_statusCode_t status = client->connect();
   ```

   ###### Note

   `your_own_clientId` must be the same as the one you specify in
   [start-device-discovery](../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md "../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md") in the
   user-guided setup, or for [create-managed-thing](../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md") in the simple setup provisioning flow.

3. Publish and subscribe by doing the following steps.
   1. After the connection is established, you can now subscribe to incoming tasks from the managed integrations Hub SDK.
      The incoming tasks can be control tasks or provision tasks. You also need to define your own callback function upon tasks received, and
      your own custom context for your own tracing purposes.

   ```
         // subscribe to provisioning tasks
         iotmi_statusCode_t status = client->iotmi_provision_subscribe_to_tasks(
         example_subscriber_callback, custom_context);

         // subscribe to control tasks
         iotmi_statusCode_t status = client->iotmi_control_subscribe_to_tasks(
         example_subscriber_callback, custom_context);
   ```

   2. After the connection is established, you can now publish requests from your application to the managed integrations Hub SDK. You can define your own task message type,
      with different payloads for different business purposes. The requests can include both control requests and provision requests, similar to the subscribe flow.
      Finally, you can assign an address for your `rspPayload` to get the response from the managed integrations Hub SDK in a synchronized manner.

   ```
   // publish control request
     iotmi_client_request_t api_payload = {
               .messageType = C2MIMessageType::C2MI_CONTROL_EVENT,
               .reqPayload = (uint8_t *)"`define_your_req_payload`",
               .rspPayload = (uint8_t *)calloc(1000, sizeof(uint8_t))
     };

     status = client->iotmi_control_publish_request(&api_payload);

     // publish provision request
     iotmi_client_request_t api_payload = {
               .messageType = C2MIMessageType::C2MI_DEVICE_ONBOARDED,
               .reqPayload = (uint8_t *)"`define_your_req_payload`",
               .rspPayload = (uint8_t *)calloc(1000, sizeof(uint8_t))
     };
     status = client->iotmi_provision_publish_request(&api_payload);

   ```

4. Build your own `CMakeLists.txt` and build your application from there. The final output could be a executable binary such as `MyFirstApplication`

## Running your custom application

Before you run your custom application, complete the following steps to set up your hub and start the managed integrations Hub SDK:

- Follow the onboarding instructions at [Onboard your hubs to managed integrations](managedintegrations-sdk-v2-cookbook-usinghub.md "managedintegrations-sdk-v2-cookbook-usinghub.md").
- Complete the installation process documented in [Install and validate the managed integrations Hub SDK](managedintegrations-sdk-v2-cookbook-deployment.md "managedintegrations-sdk-v2-cookbook-deployment.md").

Once the prerequisites are met, you can run your custom application. For example:

```
./MyFirstApplication
```

###### Important

You must manually update the start script listed in [Deploy the Hub SDK
with a script](managedintegrations-sdk-v2-cookbook-deployment-nogg.md "managedintegrations-sdk-v2-cookbook-deployment-nogg.md") with a script to start your own application.
The order matters, don't change the order.

Update the following. Change

```
./IotMI-DeviceSDK-Toolkit/bin/DeviceSDKClientDemo >> $LOGS_DIR/logDeviceSDKClientDemo_logs.txt &
```

to

```
./MyFirstApplication >> $LOGS_DIR/MyFirstApplication_logs.txtt &
```

## Data types

This section defines the data types used for the custom protocol plugin.

**iotmi_client_request_t**

Represents a request to be published to the managed integrations components.

**messageType**

The type of the message (CommonTypes::C2MIMessageType). The following list shows the valid values.

- `C2MI_DEVICE_ONBOARDED`: Indicates a device onboarding message with related payload.
- `C2MI_DE_PROVISIONING_PRE_ASSOCIATED_COMPLETE`: Indicates a de-provision task complete notification for a pre-associated device.
- `C2MI_DE_PROVISIONING_ACTIVATED_COMPLETE`: Indicates a de-provision task complete notification for an activated device.
- `C2MI_DE_PROVISIONING_COMPLETE_RESPONSE`: Indicates a de-provision task complete response.
- `C2MI_CONTROL_EVENT`: Indicates a control event with potential device state change.
- `C2MI_CONTROL_SEND_COMMAND`: Indicates a control command from a local controller.
- `C2MI_CONTROL_SEND_DEVICE_STATE_QUERY`: Indicates a control device state query from a local controller.

**reqPayload**

The request payload, typically a JSON-formatted string.

**rspPayload**

The response payload, populated by the managed integrations components.

**iotmi_client_event_t**

Represents an event received from the managed integrations components.

**event_id**

The unique identifier of the event.

**length**

The length of the event data.

**data**

A pointer to the event data, including the `messageType`. The following list shows the possible values.

- `C2MI_PROVISION_UGS_TASK`: Indicates a provision task for the UGS flow.
- `C2MI_PROVISION_SS_TASK`: Indicates a provision task for the SimpleSetup flow.
- `C2MI_DE_PROVISION_PRE_ASSOCIATED_TASK`: Indicates a de-provision task for a pre-associated device.
- `C2MI_DE_PROVISION_ACTIVATED_TASK`: Indicates a de-provision task for an activated device.
- `C2MI_DEVICE_ONBOARDED_RESPONSE`: Indicates a device onboarding response.
- `C2MI_CONTROL_TASK`: Indicates a control task.
- `C2MI_CONTROL_EVENT_NOTIFICATION`: Indicates a control event notification for a local controller.

**ctx**

A custom context associated with the event.
