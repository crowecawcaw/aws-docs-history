

# FleetWise Edge agent controls
<a name="fwe-agent-controls"></a>

When running in FleetWise Edge mode, the simulation service manages per-vehicle FWE agent Docker containers. The Fleet Manager UI provides controls to start, stop, and monitor these agents.

## Starting and stopping agents
<a name="agent-start-stop"></a>

From the simulation panel in the Fleet Manager UI, operators can:
+  **Select telemetry mode** — Choose between "MQTT Direct" (JSON telemetry published directly to IoT Core) and "FleetWise Edge" (CAN signals collected by FWE agent, encoded as protobuf). The FWE mode description notes that Docker is required.
+  **Start an agent** — The simulation service calls the `/api/agent/start` endpoint with the vehicle ID. The service:

  1. Resolves the vehicle’s VIN from DynamoDB

  1. Retrieves the vehicle’s IoT certificate

  1. Generates FWE persistency files (static config, decoder manifest, collection schemes)

  1. Starts a Docker container named `fwe-{vin}` with the FWE agent image

  1. Configures a virtual CAN bus interface (`vcan0`) inside the container

  1. The agent connects to IoT Core, publishes a checkin, receives campaigns, and begins collecting
+  **Stop an agent** — Stops and removes the Docker container for the specified vehicle
+  **View agent status** — The `/api/agent/status` endpoint returns all running FWE containers with their VINs, uptime, and campaign sync state
+  **Stream agent logs** — The `/api/agent/logs/{vin}` endpoint streams the FWE container’s stdout, showing checkin messages, scheme receipts, and signal collection activity

## Cloud simulation with FWE
<a name="agent-cloud-mode"></a>

In cloud simulation mode, the FWE agent and simulator run as separate EC2-backed ECS tasks on the same host:
+ The `fwe-simulator` task generates CAN frames and writes them to the assigned virtual CAN interface (e.g., `vcan0`)
+ The `fwe-agent` task reads from the same vcan interface, collects signals per campaign, and uploads protobuf to IoT Core
+ Each vehicle gets a unique vcan interface to prevent cross-contamination between simultaneous simulations
+ The simulation Lambda assigns vcan interfaces using `_next_vcan_index()` and passes the interface name to both tasks
+ The FWE agent health check uses `pgrep aws-iot-fleetwise-edge` — once healthy, the simulator task starts