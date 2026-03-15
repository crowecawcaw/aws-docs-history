# FleetWise Edge agent controls

When running in FleetWise Edge mode, the simulation service manages per-vehicle FWE agent Docker containers. The Fleet Manager UI provides controls to start, stop, and monitor these agents.

## Starting and stopping agents

From the simulation panel in the Fleet Manager UI, operators can:

- **Select telemetry mode** — Choose between "MQTT Direct" (JSON telemetry published directly to IoT Core) and "FleetWise Edge" (CAN signals collected by FWE agent, encoded as protobuf). The FWE mode description notes that Docker is required.
- **Start an agent** — The simulation service calls the `/api/agent/start` endpoint with the vehicle ID. The service:
  1.  Resolves the vehicle’s VIN from DynamoDB
  2.  Retrieves the vehicle’s IoT certificate
  3.  Generates FWE persistency files (static config, decoder manifest, collection schemes)
  4.  Starts a Docker container named `fwe-{vin}` with the FWE agent image
  5.  Configures a virtual CAN bus interface (`vcan0`) inside the container
  6.  The agent connects to IoT Core, publishes a checkin, receives campaigns, and begins collecting

- **Stop an agent** — Stops and removes the Docker container for the specified vehicle
- **View agent status** — The `/api/agent/status` endpoint returns all running FWE containers with their VINs, uptime, and campaign sync state
- **Stream agent logs** — The `/api/agent/logs/{vin}` endpoint streams the FWE container’s stdout, showing checkin messages, scheme receipts, and signal collection activity

## Cloud simulation with FWE

In cloud simulation mode (ECS Fargate), the FWE agent runs as a sidecar container alongside the simulator container in the same Fargate task:

- The `fwe-simulator` container generates CAN frames and writes them to a virtual CAN bus
- The `fwe-agent` container reads from the CAN bus, collects signals per campaign, and uploads protobuf to IoT Core
- The simulation Lambda passes the vehicle’s IoT certificate and endpoint to the FWE agent container as environment variables
- GPS coordinates are injected into the FWE agent through a shared Unix domain socket
