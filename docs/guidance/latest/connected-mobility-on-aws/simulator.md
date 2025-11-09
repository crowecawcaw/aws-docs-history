# Fleet Simulator

The fleet simulator generates realistic vehicle telemetry for testing, demonstration, and load testing without requiring physical vehicles. Built with Python and AWS IoT Core integration, the simulator produces standardized telemetry messages conforming to the Connected Mobility Signal Catalog.

**Simulation Capabilities**:

- **Configurable Fleet Size**: Simulate 1 to 10,000+ vehicles simultaneously
- **Realistic Patterns**: GPS routes, speed variations, battery drain, sensor noise
- **Event Generation**: Simulate safety events, maintenance alerts, and anomalies
- **Load Testing**: Validate system performance under automotive-scale load
- **IoT Certificate Management**: Automatic X.509 certificate creation and management per vehicle
- **REST API Interface**: Control simulations via web UI or programmatic API calls

**Signal Catalog**:

The simulator generates telemetry conforming to the Connected Mobility Signal Catalog with 9 signal groups:

- **Vehicle Identity**: VIN, fleet ID, vehicle type (required)
- **Location**: GPS coordinates (lat/lon), speed, heading, altitude, timestamp (required)
- **Vehicle State**: Odometer, engine hours, gear position, brake/accelerator pedal (required)
- **Driver Behavior**: Harsh braking/acceleration/turning, speeding violations, idle time, driver score, phone usage, seatbelt status
- **Fuel/Energy**: Fuel consumption rate, fuel level (ICE), state of charge, voltage, regenerative braking power (EV)
- **Diagnostics**: Engine temperature, oil pressure/temperature, coolant temperature, transmission temperature, component life percentages
- **Tires**: Pressure for all 4 tires, temperature, tread depth measurements
- **Safety Systems**: AEB status/activation, ABS activation, ESC activation, airbag warnings
- **Electrical**: 12V battery voltage, alternator output
- **Metadata**: Data source identifier, auto-registration flag (required)
  All measurements use imperial units (mph, Fahrenheit, PSI, miles) for consistency. EV-specific fields (soc, volt, regen_pwr) are null for ICE vehicles and vice versa.

**Critical Safety Event Catalog**:

The simulator generates 7 categories of critical safety events that trigger real-time alerts:

- **Imminent Collision**: AEB activation + harsh braking (>0.4g) - CRITICAL severity, <5 second response
- **Rollover Risk**: Sharp turn (>45°) at high speed (>50mph) with heavy cargo - CRITICAL severity
- **Tire Blowout**: Tire pressure <20 PSI or rapid pressure drop (>5 PSI/min) - HIGH severity
- **Engine Overheat**: Engine temperature >240°F or coolant >230°F - HIGH severity
- **Electrical Failure**: Battery voltage <11.5V or alternator output <12.0V - MEDIUM severity
- **Driver Distraction**: Phone usage while moving (speed >25mph) or unbuckled seatbelt - MEDIUM severity
- **Cargo Breach**: Cargo door opens while vehicle in motion - HIGH severity
  Each event includes severity classification, required response time, automated actions (emergency dispatch, hazard light activation, driver coaching), and real-world scenario examples.

**Extensibility**:

- **Custom Scenarios**: Define custom driving scenarios (urban, highway, off-road)
- **Failure Injection**: Simulate network failures, sensor malfunctions, and edge cases
- **Replay Mode**: Replay historical telemetry for debugging and testing
- **Multi-City Routes**: Pre-configured GPS routes for NYC, Munich, San Francisco, and other cities
- **Driver Profiles**: Simulate different driver behaviors (safe, aggressive, distracted)

**Integration with Data Processing**:

The simulator works with the data processing transformation layer to support multiple data sources:

- **IoT Core Native**: Direct telemetry generation in Connected Mobility Signal Catalog format
- **AWS IoT FleetWise**: Simulated FleetWise campaigns with VSS (Vehicle Signal Specification) signals
- **OEM Proprietary**: Custom OEM formats transformed via manifest-based processing
  Transform manifests define field mappings, unit conversions, and data quality rules to normalize all sources into the standard Connected Mobility Signal Catalog format for downstream Flink processing.

**Amazon Location Services Integration**:

The simulator leverages Amazon Location Services for realistic GPS route generation and geocoding:

- **Route Calculator**: Generates realistic driving routes between origin and destination coordinates using Esri data provider
- **Multi-City Routes**: Pre-configured routes for major cities (NYC, Munich, San Francisco, Los Angeles, Chicago)
- **Turn-by-Turn Navigation**: Calculates waypoints along routes with accurate distance and time estimates
- **Route Caching**: Caches generated routes in JSON files (route_cache.json, munich_route_cache.json) to reduce API calls
- **Traffic-Aware Routing**: Optional traffic consideration for realistic speed variations along routes
- **Route Replay**: Vehicles follow calculated routes with configurable speed profiles and stop patterns
  The route calculator (cms-route-calculator) is referenced by the simulator to generate GPS coordinates that match real road networks, ensuring telemetry data reflects actual driving patterns rather than straight-line interpolation.
