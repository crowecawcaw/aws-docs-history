# Zigbee middleware code

organization

The following shows the Zigbee reference middleware code organization.

###### Topics

- [ACS Zigbee DPK](#managedintegrations-sdk-middleware-zigbeedpk "#managedintegrations-sdk-middleware-zigbeedpk")
- [Silicon Labs Zigbee SDK](#managedintegrations-sdk-middleware-silabssdk "#managedintegrations-sdk-middleware-silabssdk")
- [ACS Zigbee Service](#managedintegrations-sdk-middleware-zigbeesvc "#managedintegrations-sdk-middleware-zigbeesvc")
- [ACS Zigbee Adaptor](#managedintegrations-sdk-middleware-zigbeeadaptor "#managedintegrations-sdk-middleware-zigbeeadaptor")

## ACS Zigbee DPK

The code for Zigbee DPK is located inside the directory listed in the example below:

````
./IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-dpk/`example`/dpk/ace_hal/
|— common
|—   |— fxnDbusClient
|—   |— include
|— kvs |— log
|— wifi
|—   |— include
|—   |— src
|—   |— wifid
|—       |— fxnWifiClient
|—       |— include
|— zibgee
|—   |— include
|—   |— src
|—   |— zigbeed
|—       |— ember
|—       |— include
|— zwave
|—   |— include
|—   |— src
|—   |— zwaved
|—       |— fxnZwaveClient
|—       |— include
|—       |— zware ``` ## Silicon Labs Zigbee SDK The Silicon Labs SDK is presented inside the `IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-z3-gateway` folder. This ACS Zigbee DPK layer is implemented for this Silicon Labs SDK. ``` ./IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-zz3-gateway/
|— autogen |— config
|— gecko_sdk_4.3.2
|—   |— platform
|—   |— protocol
|—   |— util ``` ## ACS Zigbee Service The code for the Zigbee Service is located inside the `IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/` folder. The `src` and `include` subfolders at this location contain all the files related to the ACS Zigbee service. ``` IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/src/
|— zb_alloc.c |— zb_callbacks.c
|— zb_database.c |— zb_discovery.c
|— zb_log.c |— zb_main.c
|— zb_region_info.c |— zb_server.c
|— zb_svc.c |— zb_svc_pwr.c
|— zb_timer.c |— zb_util.c
|— zb_zdo.c |— zb_zts.c IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/include/
|— init.zigbeeservice.rc |— zb_ace_log_uml.h
|— zb_alloc.h |— zb_callbacks.h
|— zb_client_aipc.h |— zb_client_event_handler.h
|— zb_database.h |— zb_discovery.h
|— zb_log.h |— zb_region_info.h
|— zb_server.h |— zb_svc.h
|— zb_svc_pwr.h |— zb_timer.h
|— zb_util.h |— zb_zdo.h
|— zb_zts.h ``` ## ACS Zigbee Adaptor The code for the ACS Zigbee Adaptor is located inside the `IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/api` folder. The `src` and `include` subfolders at this location contain all the files related to the ACS Zigbee Adaptor library. ``` IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/api/src/ |— zb_client_aipc.c
|— zb_client_api.c |— zb_client_event_handler.c
|— zb_client_zcl.c IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-general/middleware/zigbee/api/include/ |— ace
|—   |— zb_adapter.h
|—   |— zb_command.h
|—   |— zb_network.h
|—   |— zb_types.h
|—   |— zb_zcl.h
|—   |— zb_zcl_cmd.h
|—   |— zb_zcl_color_control.h
|—   |— zb_zcl_hvac.h
|—   |— zb_zcl_id.h
|—   |— zb_zcl_identify.h
|—   |— zb_zcl_level.h
|—   |— zb_zcl_measure_and_sensing.h
|—   |— zb_zcl_onoff.h
|—   |— zb_zcl_power.h ```
````
