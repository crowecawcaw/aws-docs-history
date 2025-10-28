# Appendix – Manufacturer Module Datasheet Requirements

The following is a summary of commands and features that are listed as optional for implementation by the manufacturer. Their availability must be explicitly documented on the device datasheet:

- _EVENT!_ – long polling, support host communication purely over the serial interface (see [8.2.2 EVENT! time   »Wait (blocking) for the next event or timeout«](elpg-event-handling.md#elpg-eventq-time "elpg-event-handling.md#elpg-eventq-time"))
- _DIAG_ – command group for enhanced diagnostic and debugging purposes (see [8.3.1 DIAG {command} [optional parameters]   »Perform a diagnostic command«](elpg-event-handling.md#elpg-diag-command "elpg-event-handling.md#elpg-diag-command") )
- _OTW_ – over the wire, proprietary firmware update protocol (see [9.13.1 OTW   »Enter firmware update mode«](elpg-ota-updates.md#elpg-otw-firmware-update-enter "elpg-ota-updates.md#elpg-otw-firmware-update-enter") )
- _WHERE?_ – request module location information (see [11.1.2 WHERE?   »Request location information«](elpg-additional-services.md#elpg-additional-services-where-command "elpg-additional-services.md#elpg-additional-services-where-command"))
- _Workshop Wi-Fi Credentials_ – default Workshop connectivity credential (see [12.2.1 Workshop Default Wi-Fi Credentials (Optional)](elpg-provisioning.md#elpg-provisioning-evaluation-kits-quick-connect "elpg-provisioning.md#elpg-provisioning-evaluation-kits-quick-connect"))
- _BLE_ – command group exposing additional Bluetooth Low Energy wireless connectivity (see section 13)

Modules implementing this command group should also document in the device datasheet the following parameters:

    + MaxBLECentral – the maximum number of Central role configurations supported
    + MaxBLEGATT – the maximum number of Peripheral role configurations supported
    + MaxBLECharLen – length of the BLE characteristic buffer
    + MaxBLESubscriptions – the maximum number of subscriptions

- _GPIO_ – command group exposing I/O control for modules with digital and analog I/O expansion (see [14 GPIO control (new with v1.3)](elpg-gpio-control.md "elpg-gpio-control.md") )

Modules implementing this command group should also document in the device datasheet the following parameters:

    + MaxIO – the number of I/O pins available, their physical location and DC electrical characteristics (for example, sink and source current and voltage thresholds)
    + IOMaxInt – largest integer value representation of the pin value

The following implementation parameters must be documented by all ExpressLink modules as part of the mandatory command set:

- MaxExec – Maximum command execution time (<= 120 seconds)
- MaxEvent – Depth of the Event queue
- MaxOTARead – Maximum number of bytes that can be requested at once with an OTA READ command
- MaxShadow – Maximum number of Shadow objects the module can handle
  Additional documentation is provided in the device datasheet for the following commands:

- SLEEP# – a list of available low power modes, their operating conditions and expected power consumption (see [4.7.4 SLEEP[#] [duration]   »Request to enter a low power mode«](elpg-commands.md#elpg-sleeph-command "elpg-commands.md#elpg-sleeph-command") )
- CONNECT – a list of Hint Codes (see [4.7.2 CONNECT   »Establish a connection to an AWS IoT Core Endpoint«](elpg-commands.md#elpg-connect-command "elpg-commands.md#elpg-connect-command") )
- Device Defender – list of Custom Metrics reported (see [10.1 AWS IoT Device Defender](elpg-iot-services.md#elpg-device-defender "elpg-iot-services.md#elpg-device-defender") )
- BLE EXCEPTION – list of Hint Codes (see section [8.2.1 EVENT?   »Request the next event in the queue«](elpg-event-handling.md#elpg-eventq-command "elpg-event-handling.md#elpg-eventq-command"))
- BLE DISCOVER ERROR – list of Hint Codes (see section [13.2.1 BLE[#] DISCOVER [duration|CANCEL]   »Scanning and Advertisement«](elpg-ble.md#elpg-ble-discover-command "elpg-ble.md#elpg-ble-discover-command") )
