

# Signal catalog reference
<a name="signal-catalog-reference"></a>

The signal catalog defines the standard telemetry format used throughout the guidance. All data sources (MQTT Direct simulator, FleetWise Edge Agent, OEM APIs) transform their data to match this catalog before entering the processing pipeline.

The catalog is stored in the `cms-dev-signal-catalog` DynamoDB table and loaded into Redis by the SignalCatalogLoader on Flink startup. The signal catalog maps between three representations:
+  **DBC Signal** — The CAN bus signal name as defined in the DBC file (`services/simulation/can/cms-fleet.dbc`)
+  **JSON Field** — The field name used in standard telemetry JSON messages
+  **VSS Path** — The COVESA Vehicle Signal Specification path used by FleetWise

## SignalCatalogLoader
<a name="signal-catalog-loader"></a>

The SignalCatalogLoader is a utility class used by the EventDrivenTelemetryProcessor on startup. It reads the signal catalog from DynamoDB and writes two Redis hashes:
+  `signal_catalog:map` — Maps JSON field names to numeric signal IDs (for example, `speed` → `1`)
+  `signal_catalog:reverse` — Maps signal IDs to metadata strings: `name|vssPath|unit|dataType` (for example, `1` → `speed|Vehicle.Speed|mph|float`)

The loader checks a version key in Redis and only refreshes the catalog when the version changes, enabling hot-reload without restarting the Flink application.

## Engine signals
<a name="engine-signals"></a>

 **ECM\_Engine\_1 (CAN ID 0x100, 100ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| VehicleSpeed | speed | Vehicle.Speed | mph | 0–655 | 
| EngineRPM | engineRPM | Vehicle.Powertrain.Engine.RPM | rpm | 0–8000 | 
| EngineTemp | engineTemp | Vehicle.Powertrain.Engine.Temperature | °F | -40–370 | 
| IgnitionOn | ignitionOn | Vehicle.Powertrain.IgnitionOn | bool | 0/1 | 

 **ECM\_Engine\_2 (CAN ID 0x101, 500ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| OilPressure | oilPressure | Vehicle.Powertrain.Engine.OilPressure | PSI | 0–102 | 
| EngineLoad | engineLoad | Vehicle.Powertrain.Engine.Load | % | 0–128 | 
| ThrottlePosition | throttle | Vehicle.Powertrain.Engine.ThrottlePosition | % | 0–102 | 
| CoolantTemp | coolant\_temp | Vehicle.Powertrain.Engine.CoolantTemperature | °F | -40–370 | 
| IntakeAirTemp | intakeAirTemp | Vehicle.Powertrain.Engine.IntakeAirTemperature | °F | -40–62 | 
| EngineHoursTotal | engine\_hours\_total | Vehicle.Powertrain.Engine.HoursTotal | hrs | 0–16383 | 

 **ECM\_Engine\_3 (CAN ID 0x102, 100ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| Acceleration | acceleration | Vehicle.Acceleration | m/s² | -20–21 | 
| Deceleration | deceleration | Vehicle.Deceleration | m/s² | -20–21 | 
| Odometer | odometer | Vehicle.Odometer | miles | 0–16M | 
| FuelRate | fuel\_rate | Vehicle.Powertrain.FuelSystem.FuelRate | L/h | 0–51 | 

## Transmission signals
<a name="transmission-signals"></a>

 **TCM\_Transmission (CAN ID 0x110, 200ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| TransmissionTemp | transmissionTemp | Vehicle.Powertrain.Transmission.Temperature | °F | -40–472 | 
| GearPosition | gearPosition | Vehicle.Powertrain.Transmission.GearPosition | enum | 0–7 | 
| CruiseControl | cruise\_control | Vehicle.ADAS.CruiseControl.Active | bool | 0/1 | 
| ParkingBrake | parking\_brake | Vehicle.Chassis.ParkingBrake.Active | bool | 0/1 | 

## Body control signals
<a name="body-control-signals"></a>

 **BCM\_Body\_1 (CAN ID 0x120, 500ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| SeatbeltStatus | seatbeltStatus | Vehicle.Cabin.Seatbelt.Driver.Fastened | bool | 0/1 | 
| PhoneConnected | phoneConnected | Vehicle.Cabin.Infotainment.PhoneConnected | bool | 0/1 | 
| WindowsUp | windows\_up | Vehicle.Cabin.Windows.AllClosed | bool | 0/1 | 
| TrunkLocked | trunk\_locked | Vehicle.Body.Trunk.Locked | bool | 0/1 | 
| AlarmArmed | alarm\_armed | Vehicle.Body.Alarm.Armed | bool | 0/1 | 
| KeylessEntry | keyless\_entry | Vehicle.Body.KeylessEntry.Proximity | bool | 0/1 | 
| Headlights | headlights | Vehicle.Body.Lights.Headlights.Mode | enum | 0–2 | 
| HazardLights | hazard\_lights | Vehicle.Body.Lights.Hazard.Active | bool | 0/1 | 
| TurnSignalActive | turn\_signal\_active | Vehicle.Body.Lights.TurnSignal.Active | bool | 0/1 | 
| WifiConnected | wifi\_connected | Vehicle.Connectivity.WiFi.Connected | bool | 0/1 | 
| BluetoothDevices | bluetooth\_devices | Vehicle.Connectivity.Bluetooth.DeviceCount | count | 0–7 | 
| NavigationActive | navigation\_active | Vehicle.Cabin.Infotainment.Navigation.Active | bool | 0/1 | 

## Tire signals
<a name="tire-signals"></a>

 **TPMS\_Pressure (CAN ID 0x130, 1000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| TirePressureFL | tire\_fl | Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure | PSI | 0–102 | 
| TirePressureFR | tire\_fr | Vehicle.Chassis.Axle.Row1.Wheel.Right.Tire.Pressure | PSI | 0–102 | 
| TirePressureRL | tire\_rl | Vehicle.Chassis.Axle.Row2.Wheel.Left.Tire.Pressure | PSI | 0–102 | 
| TirePressureRR | tire\_rr | Vehicle.Chassis.Axle.Row2.Wheel.Right.Tire.Pressure | PSI | 0–102 | 
| TireTempMax | tire\_temp\_max | Vehicle.Chassis.Tire.TemperatureMax | °F | 0–255 | 

 **TPMS\_Tread (CAN ID 0x131, 5000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| TireTreadFL | tire\_tread\_fl | Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.TreadDepth | mm | 0–25.5 | 
| TireTreadFR | tire\_tread\_fr | Vehicle.Chassis.Axle.Row1.Wheel.Right.Tire.TreadDepth | mm | 0–25.5 | 
| TireTreadRL | tire\_tread\_rl | Vehicle.Chassis.Axle.Row2.Wheel.Left.Tire.TreadDepth | mm | 0–25.5 | 
| TireTreadRR | tire\_tread\_rr | Vehicle.Chassis.Axle.Row2.Wheel.Right.Tire.TreadDepth | mm | 0–25.5 | 

## Safety signals
<a name="safety-signals"></a>

 **ADAS\_Safety\_1 (CAN ID 0x140, 100ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| LongitudinalAcceleration | deceleration | Vehicle.Acceleration.Longitudinal | m/s² | -10–10 | 
| LongitudinalAcceleration | acceleration | Vehicle.Acceleration.Longitudinal | m/s² | -10–10 | 
| LateralAcceleration | lateralAcceleration | Vehicle.Acceleration.Lateral | m/s² | -10–10 | 
| LaneDepartureWarning | laneDepartureWarning | Vehicle.ADAS.LaneDepartureDetection.IsWarning | bool | 0/1 | 
| ForwardCollisionDistance | forwardCollisionDistance | Vehicle.ADAS.ForwardCollisionWarning.Distance | m | 0–100 | 
| DriverDrowsinessLevel | driverDrowsinessLevel | Vehicle.Driver.DrowsinessLevel | level | 0–3 | 
| AEBActivation | aeb\_act | Vehicle.ADAS.AEB.IsActive | bool | 0/1 | 
| ABSActivation | abs\_act | Vehicle.ADAS.ABS.IsActive | bool | 0/1 | 
| ESCActivation | esc\_act | Vehicle.ADAS.ESC.IsActive | bool | 0/1 | 
| AirbagWarning | airbag\_warn | Vehicle.Safety.Airbag.IsWarning | bool | 0/1 | 

 **ADAS\_Safety\_2 (CAN ID 0x141, 100ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| PhoneUsage | phone\_use | Vehicle.Safety.Driver.PhoneUsage | bool | 0/1 | 
| SeatbeltViolation | seatbelt | Vehicle.Safety.Driver.SeatbeltViolation | bool | 0/1 | 
| LateralG | lateralG | Vehicle.Acceleration.Lateral | g | -5–5.2 | 
| FollowingDistance | followingDistance | Vehicle.ADAS.FollowingDistance | m | 0–102 | 

## Battery and fuel signals
<a name="battery-signals"></a>

 **BMS\_Battery (CAN ID 0x150, 1000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| BatteryVoltage | batteryVoltage | Vehicle.Powertrain.Battery.Voltage | V | 0–20.5 | 
| AlternatorOutput | alternator\_output | Vehicle.Powertrain.Alternator.Voltage | V | 0–20.5 | 
| FuelLevel | fuelLevel | Vehicle.Powertrain.FuelSystem.Level | % | 0–128 | 

 **BMS\_EV (CAN ID 0x151, 1000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| IsEV | is\_ev | Vehicle.Powertrain.Type.IsEV | bool | 0/1 | 
| StateOfCharge | soc | Vehicle.Powertrain.Battery.StateOfCharge | % | 0–128 | 
| HVBatteryVoltage | volt | Vehicle.Powertrain.Battery.HVVoltage | V | 0–410 | 
| RegenPower | regen\_pwr | Vehicle.Powertrain.Battery.RegenPower | kW | -50–155 | 

## Instrument and climate signals
<a name="instrument-signals"></a>

 **ICM\_Instrument (CAN ID 0x160, 200ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| Heading | heading | Vehicle.Navigation.Heading | deg | 0–410 | 
| DTCCodesActive | dtc\_codes\_active | Vehicle.Diagnostics.DTCActive | bool | 0/1 | 

 **HVAC\_Climate (CAN ID 0x170, 2000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| HVACOn | hvac\_on | Vehicle.Cabin.HVAC.Active | bool | 0/1 | 
| TargetTemp | target\_temp | Vehicle.Cabin.HVAC.TargetTemperature | °F | 40–168 | 
| CabinTemp | cabin\_temp | Vehicle.Cabin.HVAC.CabinTemperature | °F | 40–168 | 
| SeatHeatDriver | seat\_heat\_driver | Vehicle.Cabin.Seat.Driver.HeatingLevel | level | 0–3 | 

## Maintenance signals
<a name="maintenance-signals"></a>

 **MAINT\_Indicators (CAN ID 0x180, 5000ms cycle):** 


| DBC Signal | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| OilLife | oil\_life | Vehicle.Maintenance.OilLife | % | 0–128 | 
| BrakeWear | brake\_wear | Vehicle.Maintenance.BrakeWear | % | 0–128 | 
| FilterLife | filter\_life | Vehicle.Maintenance.FilterLife | % | 0–128 | 
| IdleHoursTotal | idle\_hours\_total | Vehicle.Powertrain.Engine.IdleHoursTotal | hrs | 0–16383 | 
| AirPressure | air\_pressure | Vehicle.Chassis.Brake.AirPressure | PSI | 0–128 | 
| HydraulicPressure | hydraulic\_pressure | Vehicle.Chassis.Brake.HydraulicPressure | PSI | 0–4095 | 

## GPS signals (separate interface)
<a name="gps-signals"></a>

GPS coordinates are not transmitted on the CAN bus. In MQTT Direct mode, the simulator includes them in the JSON payload. In FleetWise Edge mode, the simulator injects GPS coordinates into the FWE agent through a Unix domain socket.


| Field | JSON Field | VSS Path | Unit | Range | 
| --- | --- | --- | --- | --- | 
| Latitude | lat | Vehicle.CurrentLocation.Latitude | deg | -90–90 | 
| Longitude | lng | Vehicle.CurrentLocation.Longitude | deg | -180–180 | 

## Safety event detection thresholds
<a name="safety-event-thresholds"></a>

The SafetyProcessor evaluates every telemetry message against the event catalog rules stored in the `cms-{stage}-event-catalog` DynamoDB table. Detection uses real CAN bus signals — not synthetic derived values — so the same rules work for both simulated and production vehicles.


| Event Type | Trigger Signal | Threshold | Detection | 
| --- | --- | --- | --- | 
| HARSH\_BRAKING | deceleration (m/s²) | < -3.9 (0.4g) | Cloud | 
| HARSH\_ACCELERATION | acceleration (m/s²) | > 3.5 (0.35g) | Cloud | 
| HARSH\_CORNERING | lateralAcceleration (m/s²) | > 4.4 (0.45g) | Cloud | 
| SPEEDING | speed (mph) | > 80 | Cloud | 
| SEATBELT\_UNFASTENED | seatbeltStatus | = false while driving | Cloud | 
| PHONE\_USAGE | phone\_use | = 1 while driving | Cloud | 
| LANE\_DEPARTURE | laneDepartureWarning | = 1 | Cloud or Edge | 
| TAILGATING | forwardCollisionDistance (m) | < 2.0 | Cloud | 
| DROWSY\_DRIVING | driverDrowsinessLevel | >= 1 | Cloud | 
| AEB\_ACTIVATION | aeb\_act | = 1 | Edge | 
| ESC\_ACTIVATION | esc\_act | = 1 | Edge | 

Cloud detection evaluates rules in the SafetyProcessor Flink application against every telemetry message on the `cms-telemetry-safety` Kafka topic. Edge detection uses FleetWise condition-based campaigns where the FWE agent detects the event on the vehicle and reports it directly. Both detection methods write to the same `cms-{stage}-storage-safety-events` DynamoDB table.

The event catalog is seeded by `make seed-event-catalog` and can be modified at runtime — the SafetyProcessor reloads the catalog every 5 minutes without requiring a restart.

## Maintenance alert detection thresholds
<a name="maintenance-alert-thresholds"></a>

The MaintenanceProcessor uses the following thresholds to generate maintenance alerts:


| Alert Type | Trigger Signal | Threshold | DTC Code | 
| --- | --- | --- | --- | 
| LOW\_OIL\_PRESSURE | OilPressure | < 15 PSI | P0520 | 
| HIGH\_ENGINE\_TEMP | EngineTemp | > 230°F | P0217 | 
| LOW\_BATTERY | BatteryVoltage | < 11.5V | P0562 | 
| ENGINE\_OVERSPEED | EngineRPM | > 6000 | P0219 | 
| LOW\_FUEL | FuelLevel | < 5% | P0461 | 
| BRAKE\_WEAR | BrakeWear | < 20% | P0301 | 
| TIRE\_PRESSURE | TirePressureXX | < 25 PSI | C1234 | 
| OIL\_LIFE\_LOW | OilLife | < 10% | P0524 | 
| FILTER\_REPLACEMENT | FilterLife | < 15% | P0102 | 
| TIRE\_TREAD\_LOW | TireTreadXX | < 3mm | C1235 | 

## Decoder manifest
<a name="decoder-manifest-reference"></a>

The decoder manifest maps CAN signal IDs to human-readable signal names and is pushed to the FleetWise Edge Agent alongside collection schemes. The FWTelemetryProcessor also uses the decoder manifest to decode protobuf telemetry uploaded by the agent.

The manifest maps all 75 CAN signals across 15 CAN messages, plus 2 GPS signals on a separate custom interface. Each entry includes:
+  **Signal ID** — Numeric identifier used in protobuf encoding
+  **Signal name** — Human-readable name (for example, `Vehicle.Speed`)
+  **CAN message ID** — The CAN frame ID (for example, `0x100`)
+  **Bit position and length** — Position within the CAN frame
+  **Factor and offset** — Scaling values for raw-to-physical conversion
+  **Unit** — Physical unit (mph, PSI, °F, etc.)

The decoder manifest is generated by the CampaignSyncProcessor from the signal catalog in DynamoDB and serialized as a protobuf message for delivery to the FWE agent.