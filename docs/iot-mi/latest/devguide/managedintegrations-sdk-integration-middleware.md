# Integrate middleware with SDK

The middleware integration on the new hub is discussed in the following sections.

###### Topics

- [Device porting kit (DPK) API integration](#smarthome-sdk-v2-integration-dpk "#smarthome-sdk-v2-integration-dpk")
- [Reference implementation and code
  organization](#managedintegrations-sdk-integration-code "#managedintegrations-sdk-integration-code")

## Device porting kit (DPK) API integration

To integrate any chipset vendor SDK with the middleware, a standard API interface is
provided by the DPK (Device porting kit) layer of the middle. The managed integrations service
providers or ODMs need to implement these APIs based on the vendor SDK supported by the
Zigbee/Z-wave/Wi-Fi chipsets used on their IoT Hubs.

## Reference implementation and code

organization

Except the middleware, all other Device SDK components, such as the managed integrations Device
Agent and Common Data Model Bridge (CDMB) can be used without any modifications and only
need to be cross compiled.

The implementation of the middleware is based on the Silicon Labs SDK for Zigbee and
Z-Wave. If the Z-Wave and Zigbee chipsets used in the new hub are supported by the Silicon
Labs SDK present in the middleware, then the reference middleware can be used without any
modifications. You only need to cross-compile the middleware and it can then be run on the
new hub.

DPK (Device porting kit) APIs for Zigbee can be found in `acehal_zigbee.c`, and the reference
implementation of the DPK APIs is present inside the `zigbee` folder.

```
IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-dpk/`example`/dpk/ace_hal/zigbee/
|— CMakeLists.txt
|— include
|—   |— zigbee_log.h
|— src
|—   |— acehal_zigbee.c
|— zigbeed
|—   |— CMakeLists.txt
|—   |— ember
|—   |—   |— ace_ember_common.c
|—   |—   |— ace_ember_ctrl.c
|—   |—   |— ace_ember_hal_callbacks.c
|—   |—   |— ace_ember_network_creator.c
|—   |—   |— ace_ember_power_settings.c
|—   |—   |— ace_ember_zts.c
|—   |— include
|—   |—   |— zbd_api.h
|—   |—   |— zbd_callbacks.h
|—   |—   |— zbd_common.h
|—   |—   |— zbd_network_creator.h
|—   |—   |— zbd_power_settings.h
|—   |—   |— zbd_zts.h
```

DPK APIs for Z-Wave can be found in the `acehal_zwave.c` and reference
implementation of the DPK APIs is present inside the `zwaved` folder.

```
IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-dpk/`example`/dpk/ace_hal/zwave/
|— CMakeLists.txt
|— include
|—   |— zwave_log.h
|— src
|—   |— acehal_zwave.c
|— zwaved
|—   |— CMakeLists.txt
|—   |— fxnZwaveClient
|—   |—   |— zwave_client.c
|—   |—   |— zwave_client.h
|—   |— include
|—   |—   |— zwaved_cc_intf_api.h
|—   |—   |— zwaved_common_utils.h
|—   |—   |— zwaved_ctrl_api.h
|—   |— zware
|—   |—   |— ace_zware_cc_intf.c
|—   |—   |— ace_zware_common_utils.c
|—   |—   |— ace_zware_ctrl.c
|—   |—   |— ace_zware_debug.c
|—   |—   |— ace_zware_debug.h
|—   |—   |— ace_zware_internal.h
```

As a starting point to implement the DPK layer for a different vendor SDK, the reference
implementation can be used and modified. Following two modifications will be needed to support
a different vendor SDK:

1. Replace the current vendor SDK with the new vendor SDK in the repository.
2. Implement the middleware DPK (Device porting kit) APIs according to the new vendor
   SDK.
