# Z-Wave middleware code

organization

The following shows the Z-wave reference middleware code organization.

###### Topics

- [ACS Z-Wave DPK](#managedintegrations-sdk-middleware-zwavedpk "#managedintegrations-sdk-middleware-zwavedpk")
- [Silicon Labs ZWare and Zip
  Gateway](#managedintegrations-sdk-middleware-zware "#managedintegrations-sdk-middleware-zware")
- [ACS Z-Wave Service](#managedintegrations-sdk-middleware-zwavesvc "#managedintegrations-sdk-middleware-zwavesvc")
- [ACS Z-Wave Adaptor](#managedintegrations-sdk-middleware-zwaveadaptor "#managedintegrations-sdk-middleware-zwaveadaptor")

## ACS Z-Wave DPK

The code for Z-Wave DPK is located inside the
`IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-dpk/`example`/dpk/ace_hal/zwave`
folder.

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
|—       |— zware ``` ## Silicon Labs ZWare and Zip Gateway The code for the Silicon labs ZWare and Zip Gateway is located inside the `IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-z3-gateway` folder. This ACS Z-Wave DPK layer is implemented for Z-Wave C-APIs and Zip gateway. ``` ./IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-z3-gateway/
|— autogen |— config
|— gecko_sdk_4.3.2
|—   |— platform
|—   |— protocol
|—   |— util ``` ## ACS Z-Wave Service The code for the Z-Wave Service is located inside the folder listed in the `IoTmanagedintegrationsMiddlewares/`example`iot-ace-zwave-mw/` folder. The `src` and `include` folders at this location contain all the files related to the ACS Z-Wave service. ``` IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-zwave-mw/src/
|— zwave_mgr.c |— zwave_mgr_cc.c
|— zwave_mgr_ipc_aipc.c |— zwave_svc.c
|— zwave_svc_dispatcher.c |— zwave_svc_hsm.c
|— zwave_svc_ipc_aipc.c |— zwave_svc_main.c
|— zwave_svc_publish.c IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-zwave-mw/include/ |— ace
|—   |— zwave_common_cc.h
|—   |— zwave_common_cc_battery.h
|—   |— zwave_common_cc_doorlock.h
|—   |— zwave_common_cc_firmware.h
|—   |— zwave_common_cc_meter.h
|—   |— zwave_common_cc_notification.h
|—   |— zwave_common_cc_sensor.h
|—   |— zwave_common_cc_switch.h
|—   |— zwave_common_cc_thermostat.h
|—   |— zwave_common_cc_version.h
|—   |— zwave_common_types.h
|—   |— zwave_mgr.h
|—   |— zwave_mgr_cc.h
|— zwave_log.h |— zwave_mgr_internal.h
|— zwave_mgr_ipc.h |— zwave_svc_hsm.h
|— zwave_svc_internal.h |— zwave_utils.h ``` ## ACS Z-Wave Adaptor The code for the ACS Zigbee Adaptor is located inside the `IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-zwave-mw/cli/` folder. The `src` and `include` folder at this location contain all the files related to the ACS Z-Wave Adaptor library. ``` IotManagedIntegrationsDeviceSDK-Middleware/`example`-iot-ace-zwave-mw/cli/
|— include
|—   |— zwave_cli.h
|— src
|—   |— zwave_cli.yaml
|—   |— zwave_cli_cc.c
|—   |— zwave_cli_event_monitor.c
|—   |— zwave_cli_main.c
|—   |— zwave_cli_net.c ```
````
