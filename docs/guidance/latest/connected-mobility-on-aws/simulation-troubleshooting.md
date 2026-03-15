# Simulation troubleshooting

## Problem: Simulation service not starting

### Resolution

1. Check if port 5001 is already in use:

```
lsof -i :5001
# Kill the process if needed
kill -9 <PID>
```

2. Ensure Python dependencies are installed:

```
cd services/simulation
pip install flask flask-cors boto3 requests
```

3. Make the management script executable:

```
chmod +x manage_simulation.sh
```

4. Start the service and check logs:

```
./manage_simulation.sh start
./manage_simulation.sh logs
```

## Problem: No vehicles available for simulation

The simulation UI shows no vehicles when "Real Vehicles" is selected.

### Resolution

1. Vehicles must have IoT certificates to be used in simulations. Create vehicles in the Fleet Manager UI with "Create IoT Core certificate" enabled.
2. Verify vehicles have certificates in DynamoDB:

```
aws dynamodb scan --table-name cms-dev-storage-vehicles \
  --filter-expression "has_certificate = :t" \
  --expression-attribute-values '{":t": {"BOOL": true}}' \
  --select COUNT
```

3. If using FleetWise Edge mode, verify the vehicle VIN exists in the vehicles table and has a valid IoT thing registered.

## Problem: FWE agent Docker container not starting

The simulation service fails to start FWE agent containers in FleetWise Edge mode.

### Resolution

1. Verify Docker is running:

```
docker info
```

2. Check if the FWE Docker image is built:

```
docker images | grep fwe
```

3. If the image is missing, build it:

```
cd services/simulation
./build_sim_image.sh
```

4. Check the FWE container logs for startup errors:

```
docker logs fwe-YOUR_VIN --tail 50
```

5. Verify the FWE persistency files are generated correctly:

```
ls -la services/simulation/fwe_config/persistency/
```

## Problem: Simulation running but telemetry not appearing in dashboard

### Resolution

1. Check the simulation logs for MQTT publish errors:

```
tail -f services/simulation/simulation_service.log
```

2. Verify the IoT endpoint is reachable:

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

3. Verify the vehicle’s IoT certificate is activated:

```
# Get certificate ARN from DynamoDB, then check status
aws iot describe-certificate --certificate-id YOUR_CERT_ID \
  --query "certificateDescription.status"
```

4. Check the full pipeline: IoT Core → MSK → SimulatorPreprocessor → EventDrivenTelemetryProcessor → DynamoDB/Redis. Any stopped Flink processor in this chain will break the pipeline (see [Problem: Telemetry reaching MSK but not appearing in DynamoDB](telemetry-pipeline-troubleshooting.md#problem-telemetry-not-reaching-dynamodb "telemetry-pipeline-troubleshooting.md#problem-telemetry-not-reaching-dynamodb")).
