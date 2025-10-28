# Hub control

Hub control is an extension to the managed integrations End device SDK that allows it to interface with the `MQTTProxy` component in the Hub SDK.
With hub control, you can implement code using the End device SDK and control your hub through the managed integrations cloud as a separate device.
The hub control SDK will be provided as a separate package with-in the Hub SDK, labeled as `iot-managed-integrations-hub-control-x.x.x`.

###### Topics

- [Prerequisites](#getting-started-tutorial-prequisites "#getting-started-tutorial-prequisites")
- [End device SDK components](#device-sdk-components "#device-sdk-components")
- [Integrate with the End device SDK](#device-sdk-integration "#device-sdk-integration")
- [Example: Build hub control](#build-hub-control "#build-hub-control")
- [Supported examples](#hub-control-examples "#hub-control-examples")
- [Supported platforms](#hub-control-platforms "#hub-control-platforms")

## Prerequisites

To set up hub control, you need the following:

- A hub onboarded to the [Hub SDK](managedintegrations-sdk-v2.md "managedintegrations-sdk-v2.md"), version 0.4.0 or greater.
- Download the latest version of the [End device SDK](managedintegrations-sdk-devices.md "managedintegrations-sdk-devices.md") from the AWS Management Console.
- An [MQTT proxy](managedintegrations-sdk-v2.md "managedintegrations-sdk-v2.md") component running on the hub, version 0.5.0 or greater.

## End device SDK components

Use the following components from the [End device SDK](managedintegrations-sdk-devices.md "managedintegrations-sdk-devices.md"):

- Code generator for the data model
- Data model handler

Since the Hub SDK already has an onboarding process and a connection to the cloud, you don't need the following components:

- Provisionee
- PKCS interface
- Jobs handler
- MQTT Agent

## Integrate with the End device SDK

1.  Follow the instructions in [Code generator for Data Model](managedintegrations-sdk-device-codegen.md "managedintegrations-sdk-device-codegen.md") to generate the low level C code.
2.  Follow the instructions in [Integrating the
    End device SDK](managedintegrations-sdk-device-onboarding.md "managedintegrations-sdk-device-onboarding.md") to:
    1. ###### Set up the build environment

    Build the code on Amazon Linux 2023/x86_64 as your development host. Install the necessary
    build dependencies:

    ```
    dnf install make gcc gcc-c++ cmake
    ```

    2. ###### Develop hardware callback functions

    Before implementing the hardware callback functions, understand how the API works.
    This example uses the On/Off cluster and OnOff attribute to control a device function. For
    API details, see [Low level C-Function APIs](managedintegrations-sdk-device-api.md "managedintegrations-sdk-device-api.md").

    ```
    struct DeviceState
    {
      struct iotmiDev_Agent *agent;
      struct iotmiDev_Endpoint *endpointLight;
      /* This simulates the HW state of OnOff */
      bool hwState;
    };

    /* This implementation for OnOff getter just reads
       the state from the DeviceState */
    iotmiDev_DMStatus exampleGetOnOff(bool *value, void *user)
    {
       struct DeviceState *state = (struct DeviceState *)(user);
      *value = state->hwState;
      return iotmiDev_DMStatusOk;
    }
    ```

    3. ###### Set up endpoints and hook hardware callback functions

    After implementing the functions, create endpoints and register your callbacks.
    Complete these tasks:

        1. Create a device agent
        2. Fill callback function points for each cluster struct you want to support
        3. Set up endpoints and register supported clusters

    ```
    struct DeviceState
    {
        struct iotmiDev_Agent * agent;
        struct iotmiDev_Endpoint *endpoint1;

        /* OnOff cluster states*/
        bool hwState;
    };


    /* This implementation for OnOff getter just reads
       the state from the DeviceState */
    iotmiDev_DMStatus exampleGetOnOff( bool * value, void * user )
    {
        struct DeviceState * state = ( struct DeviceState * ) ( user );
        *value = state->hwState;
        printf( "%s(): state->hwState: %d\n", __func__, state->hwState );
        return iotmiDev_DMStatusOk;
    }

    iotmiDev_DMStatus exampleGetOnTime( uint16_t * value, void * user )
    {
        *value = 0;
        printf( "%s(): OnTime is %u\n", __func__, *value );
        return iotmiDev_DMStatusOk;
    }

    iotmiDev_DMStatus exampleGetStartUpOnOff( iotmiDev_OnOff_StartUpOnOffEnum * value, void * user )
    {
        *value = iotmiDev_OnOff_StartUpOnOffEnum_Off;
        printf( "%s(): StartUpOnOff is %d\n", __func__, *value );
        return iotmiDev_DMStatusOk;
    }

    void setupOnOff( struct DeviceState *state )
    {
        struct iotmiDev_clusterOnOff clusterOnOff = {
            .getOnOff = exampleGetOnOff,
            .getOnTime = exampleGetOnTime,
            .getStartUpOnOff = exampleGetStartUpOnOff,
        };
        iotmiDev_OnOffRegisterCluster( state->endpoint1,
                                        &clusterOnOff,
                                        ( void * ) state);
    }


    /* Here is the sample setting up an endpoint 1 with OnOff
       cluster. Note all error handling code is omitted. */
    void setupAgent(struct DeviceState *state)
    {
        struct iotmiDev_Agent_Config config = {
            .thingId = IOTMI_DEVICE_MANAGED_THING_ID,
            .clientId = IOTMI_DEVICE_CLIENT_ID,
        };
        iotmiDev_Agent_InitDefaultConfig(&config);

        /* Create a device agent before calling other SDK APIs */
        state->agent = iotmiDev_Agent_new(&config);

        /* Create endpoint#1 */
        state->endpoint1 = iotmiDev_Agent_addEndpoint( state->agent,
                                                        1,
                                                        "Data Model Handler Test Device",
                                                        (const char*[]){ "Camera" },
                                                        1 );
        setupOnOff(state);
    }

    ```

## Example: Build hub control

Hub control is provided as part of the Hub SDK package. The hub control sub-package is labeled with
`iot-managed-integrations-hub-control-x.x.x` and contains different libraries than the unmodified device SDK.

1. Move the code generated files to the `example` folder:

```
cp codegen/out/* example/dm
```

2. To build hub control, run the following commands:

```
cd <hub-control-root-folder>
```

```
mkdir build
```

```
cd build
```

```
cmake -DBUILD_EXAMPLE_WITH_MQTT_PROXY=ON -DIOTMI_USE_MANAGED_INTEGRATIONS_DEVICE_LOG=ON ..
```

```
cmake -build .
```

3. Run the examples with the `MQTTProxy` component on the hub, with the `HubOnboarding` and `MQTTProxy` components running.

```
./examples/iotmi_device_sample_camera/iotmi_device_sample_camera
```

See [Managed integrations data model](managedintegrations-data-model.md "managedintegrations-data-model.md") for the data model.
Follow Step 5 in [Get started with End device SDK](managedintegrations-sdk-device-onboarding.md "managedintegrations-sdk-device-onboarding.md") to
set up endpoints and manage communications between the end-user and iot-managed-integrations.

## Supported examples

The following examples have been built and tested:

- iotmi_device_dm_air_purifier_demo
- iotmi_device_basic_diagnostics
- iotmi_device_dm_camera_demo

## Supported platforms

The following table displays the supported platforms for hub control.

| Architecture | Operating system | GCC version | Binutils version |
| ------------ | ---------------- | ----------- | ---------------- |
| X86_64       | Linux            | 10.5.0      | 2.37             |
| aarch64      | Linux            | 10.5.0      | 2.37             |
