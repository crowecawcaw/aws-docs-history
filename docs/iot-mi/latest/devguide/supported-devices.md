# Supported Zigbee and Z-Wave device types

This page lists the hub-connected device types that have been tested with managed integrations and are supported. Managed integrations supports both [Simple setup (SS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow") and
[User guided setup
(UGS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow") for these devices.

This table lists the supported Zigbee devices.

| Zigbee device type                      | Supported capabilities                                           |
| --------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------- |
| Smart bulb / Dimmable light / RGB light | OnOff, LevelControl, ColorControl                                |
| Smart plug                              | OnOff                                                            |
| Smart switch                            | OnOff                                                            |
| LED strip                               | OnOff, LevelControl, ColorControl                                |
| Water valve                             | OnOff                                                            |
| Radiator valve                          | Thermostat, OnOff, Timer                                         |
| Thermostat                              | Thermostat, FanControl, OnOff, Timer                             |
| Garage door opener                      | WindowCovering, OnOff, LevelControl                              |
| Smoke alarm                             | BooleanState, OnOff, TemperatureMeasurement, Timer, SmokeCOAlarm |
| Motion sensor                           | BooleanState                                                     |
| Occupancy/Human presence sensor         | BooleanState, OccupancySensing                                   |
| Door and window sensor                  | BooleanState                                                     |
| Water leak sensor                       | BooleanState                                                     |
| Vibration sensor                        | BooleanState                                                     |
| Temperature and humidity sensor         | TemperatureMeasurement, RelativeHumidityMeasurement              | This table lists the supported Z-Wave devices. |
| Z-Wave device type                      | Supported capabilities                                           |
| ---                                     | ---                                                              |
| Smart bulb / Dimmable light             | OnOff, LevelControl                                              |
| Smart plug                              | OnOff                                                            |
| Garage door controller                  | OnOff, LevelControl                                              |
| Energy meter                            | ElectricalEnergyMeasurement, ElectricalPowerMeasurement          |
| Battery                                 | LevelControl                                                     |
| Siren                                   | LevelControl                                                     |
| Motion sensor                           | BooleanState                                                     |
| Door and window sensor                  | BooleanState                                                     |
| Water leak sensor                       | BooleanState                                                     |
| Temperature sensor                      | TemperatureMeasurement                                           |
| CO sensor                               | SmokeCOAlarm                                                     |
| Smoke sensor                            | SmokeCOAlarm                                                     |
