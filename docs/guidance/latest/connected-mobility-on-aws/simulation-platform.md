

# Simulation platform
<a name="simulation-platform"></a>

The solution provides two simulation modes: a local service for development and a cloud service for automated testing and demos.

## Local simulation
<a name="local-simulation"></a>

The local simulation service is a Python Flask application (`services/simulation/simulation_api.py`) that runs on the developer’s machine and exposes a REST API on port 5001. The Fleet Manager UI connects to this service to start, stop, and monitor simulations.

 **How it works:** 

1. The developer starts the service with `./manage_simulation.sh start`.

1. The Fleet Manager UI (or a direct API call) sends a POST to `/api/simulation/start` with configuration: number of vehicles, trips per vehicle, city, safety event rate, telemetry mode (MQTT Direct or FWE), and driver selection.

1. The service spawns a background thread running `realtime_telemetry_simulator.py`.

1. For each vehicle, the simulator:

   1. Retrieves the vehicle’s IoT certificate from DynamoDB (if using real vehicles).

   1. Generates a realistic GPS route for the selected city using waypoints and interpolation.

   1. Simulates an ignition ON event (trip start).

   1. Publishes telemetry messages every 1-3 seconds with realistic signal values: speed following the route, engine RPM correlated to speed, tire pressure with gradual drift, battery voltage, fuel consumption, and all 75 CAN signals.

   1. Randomly injects safety events (hard braking, speeding, harsh cornering) based on the configured safety rate.

   1. Randomly injects maintenance conditions (low oil pressure, high engine temp, low tire tread) for maintenance alert testing.

   1. After the configured trip duration, simulates an ignition OFF event (trip end).

   1. Repeats for the configured number of trips.

1. In **MQTT Direct** mode, the simulator compresses each telemetry JSON with gzip, base64-encodes it, and publishes to `cms/telemetry/{vehicleId}` via IoT Core MQTT.

1. In **FleetWise Edge** mode, the simulator:

   1. Starts a per-vehicle FWE agent Docker container (`fwe-{vin}`).

   1. Creates virtual CAN bus interfaces (`vcan0`, `vcan1`, etc.) — one per vehicle for isolation.

   1. Writes CAN frames to the virtual bus using the DBC signal definitions.

   1. Injects GPS coordinates through a Unix domain socket.

   1. The FWE agent collects signals based on active campaigns and uploads protobuf to IoT Core.

## Cloud simulation
<a name="cloud-simulation"></a>

The cloud simulation service runs on AWS infrastructure, eliminating the need for a local development environment.

 **Architecture:** 
+  **API Lambda** — A Lambda function (`simulation_lambda.py`) serves as the orchestrator. It receives simulation requests through API Gateway and manages ECS tasks.
+  **ECS Cluster** — An ECS cluster runs simulation tasks using Fargate (MQTT Direct) or EC2-backed capacity (FleetWise Edge). EC2 instances are t4g.small ARM64 with Amazon Linux 2023 ECS-optimized AMI.
+  **Worker Tasks** — In MQTT Direct mode, a single Fargate task runs the simulator. In FleetWise Edge mode, two separate EC2-backed tasks run on the same host: `fwe-agent` (FleetWise Edge Agent) and `fwe-simulator` (Python simulator with python-can). Both share virtual CAN interfaces (vcan0, vcan1…​) via HOST network mode for per-vehicle isolation.
+  **DynamoDB** — A simulations table tracks task state (running, completed, stopped) with task ARN references.

 **How it works:** 

1. The Fleet Manager UI sends a POST to `/api/simulation/start` (routed to the Lambda via API Gateway).

1. The Lambda builds the simulator command-line arguments from the request configuration.

1. The Lambda calls `ecs:RunTask` to launch ECS tasks:

   1. In **MQTT Direct** mode: a single Fargate task (`sim-worker`) runs the simulator with network access to IoT Core.

   1. In **FleetWise Edge** mode: two separate EC2-backed tasks — `fwe-agent` (long-lived, runs the FleetWise Edge Agent binary) and `fwe-simulator` (per-trip, generates CAN signals on the assigned vcan interface). The Lambda retrieves the vehicle’s IoT certificate from DynamoDB and passes it to the FWE agent container. Each vehicle gets a unique vcan interface (vcan0, vcan1, vcan2…​) to prevent cross-contamination.

1. The Lambda stores the simulation ID, task ARN, configuration, and status in DynamoDB.

1. The worker task runs autonomously, publishing telemetry to IoT Core.

1. The UI polls `/api/simulation/status/{id}` to track progress. The Lambda checks the ECS task status and fetches recent logs from CloudWatch.

1. When the simulation completes (all trips finished), the Fargate task exits. The Lambda detects the `STOPPED` status on the next poll and marks the simulation as `completed`.

1. The UI can stop a simulation early via POST `/api/simulation/stop/{id}`, which calls `ecs:StopTask`.

 **Presets:** 

The cloud simulation includes built-in presets:
+  **Quick Test** — 1 vehicle, 1 trip (for smoke testing)
+  **Fleet Demo** — 5 vehicles, 3 trips each (for demonstrations)
+  **Stress Test** — 10 vehicles, 5 trips, 50% safety event rate (for load testing)

 **Forced scenarios:** 

The API supports flags to force specific maintenance conditions for testing:
+  `force_tire_blowout` — Simulates sudden tire pressure drop
+  `force_engine_overheat` — Simulates engine temperature spike
+  `force_battery_critical` — Simulates battery voltage drop
+  `force_brake_failure` — Simulates brake wear critical
+  `force_oil_pressure_low` — Simulates oil pressure drop