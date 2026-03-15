# Remote commands troubleshooting

## Problem: Command stuck in SENT status

A command was sent but never transitions to SUCCEEDED or FAILED.

### Resolution

1. Verify the vehicle (or simulator) is connected and subscribed to the command request topic:

```
# Test by publishing a message to the IoT Core MQTT test client
# Topic: cms/commands/VEH-0049/request
# The vehicle must be subscribed to this topic to receive commands
```

2. Verify the Command Response Handler IoT Rule exists and is enabled:

```
aws iot get-topic-rule --rule-name cms_dev_command_response_rule
```

3. Check the Command Response Handler Lambda logs:

```
aws logs tail /aws/lambda/cms-dev-commands-response-handler --since 30m
```

4. If the vehicle is not connected, the command will remain in SENT status indefinitely. Commands have a 7-day TTL in DynamoDB and will be automatically cleaned up.

## Problem: Command catalog returns empty

The `/api/commands/catalog` endpoint returns no actuatable signals.

### Resolution

1. Verify the signal catalog table has entries with the `actuator` attribute:

```
aws dynamodb scan --table-name cms-dev-signal-catalog \
  --filter-expression "attribute_exists(actuator)" \
  --select COUNT
```

2. If the count is zero, the signal catalog needs to be seeded. Run the data processing deployment:

```
cd deployment && make data-processing
```

## Problem: Geofence violations not triggering

Geofences are created but no safety events are generated when vehicles cross boundaries.

### Resolution

1. Verify the GeofenceProcessor Flink application is running:

```
aws kinesisanalyticsv2 describe-application \
  --application-name cms-dev-flink-geofence-processor \
  --query "ApplicationDetail.ApplicationStatus"
```

2. Verify the geofence is active in DynamoDB:

```
aws dynamodb scan --table-name cms-dev-storage-geofences \
  --filter-expression "active = :t" \
  --expression-attribute-values '{":t": {"BOOL": true}}'
```

3. Check that the geofence `vehicleId` matches the vehicle being tracked, or is set to `ALL` for global geofences.
4. The GeofenceProcessor deduplicates events — it only fires once per boundary crossing direction. If the vehicle was already inside the geofence when it was created, no entry event will fire until the vehicle exits and re-enters.
