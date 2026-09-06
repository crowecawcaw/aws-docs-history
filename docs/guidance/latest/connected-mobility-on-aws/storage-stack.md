

# Data storage
<a name="storage-stack"></a>

The data storage layer deploys all storage resources including DynamoDB tables and S3 buckets.

## DynamoDB tables
<a name="dynamodb-tables"></a>

Seven tables store different types of data with optimized access patterns.

### Vehicles table
<a name="vehicles-table"></a>

Stores vehicle profiles and current status.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| vin | String (PK) | Vehicle Identification Number | 
| make | String | Vehicle manufacturer | 
| model | String | Vehicle model | 
| year | Number | Model year | 
| status | String | active, inactive, maintenance | 
| lastSeen | String | ISO 8601 timestamp | 
| location | Map | Current GPS coordinates | 
| odometer | Number | Current mileage | 
| batteryLevel | Number | Battery percentage (EV) | 
| fuelLevel | Number | Fuel percentage (ICE) | 

 **Indexes:** 
+ GSI1: status-lastSeen-index (query by status)
+ GSI2: make-model-index (query by vehicle type)

### Trips table
<a name="trips-table"></a>

Stores trip history with start/end locations and metrics.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| tripId | String (PK) | UUID for trip | 
| vin | String (SK) | Vehicle Identification Number | 
| startTime | String | ISO 8601 timestamp | 
| endTime | String | ISO 8601 timestamp | 
| startLocation | Map | GPS coordinates | 
| endLocation | Map | GPS coordinates | 
| distance | Number | Miles traveled | 
| duration | Number | Seconds | 
| avgSpeed | Number | Average speed (mph) | 
| maxSpeed | Number | Maximum speed (mph) | 
| fuelConsumed | Number | Gallons or kWh | 
| safetyEvents | List | Speeding, harsh braking, etc. | 

 **Indexes:** 
+ GSI1: vin-startTime-index (query trips by vehicle)
+ GSI2: startTime-index (query trips by date range)

### Alerts table
<a name="alerts-table"></a>

Stores maintenance and safety alerts.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| alertId | String (PK) | UUID for alert | 
| vin | String | Vehicle Identification Number | 
| type | String | maintenance, safety, diagnostic | 
| severity | String | low, medium, high, critical | 
| message | String | Alert description | 
| timestamp | String | ISO 8601 timestamp | 
| acknowledged | Boolean | Alert acknowledgment status | 
| resolvedAt | String | Resolution timestamp | 
| metadata | Map | Additional alert data | 

 **Indexes:** 
+ GSI1: vin-timestamp-index (query alerts by vehicle)
+ GSI2: type-severity-index (query by alert type)

### Drivers table
<a name="drivers-table"></a>

Stores driver profiles and behavior metrics.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| driverId | String (PK) | UUID for driver | 
| name | String | Driver name | 
| email | String | Contact email | 
| phone | String | Contact phone | 
| licenseNumber | String | Driver’s license number | 
| assignedVehicles | List | VINs of assigned vehicles | 
| safetyScore | Number | 0-100 safety rating | 
| totalTrips | Number | Lifetime trip count | 
| totalMiles | Number | Lifetime miles driven | 
| safetyEvents | Map | Count by event type | 

### Commands table
<a name="commands-table"></a>

Stores remote command history with status tracking and latency measurement.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| commandId | String (PK) | Unique command identifier | 
| vehicleId | String | Target vehicle ID | 
| commandName | String | Command name from catalog | 
| value | String | Command value | 
| status | String | SENT, IN\_PROGRESS, SUCCEEDED, FAILED, TIMEOUT | 
| issuedAt | String | ISO 8601 timestamp | 
| timestamp | Number | Issued time in epoch milliseconds | 
| respondedAt | String | Response timestamp | 
| latencyMs | Number | Round-trip latency in milliseconds | 
| reason | String | Failure reason | 
| topic | String | MQTT topic the command was published to | 
| ttl | Number | DynamoDB TTL (7 days) | 

 **Indexes:** 
+ GSI1: vehicleId-index (query commands by vehicle)

### Geofences table
<a name="geofences-table"></a>

Stores geofence definitions for real-time boundary evaluation.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| geofenceId | String (PK) | Unique geofence identifier | 
| vehicleId | String | Target vehicle ID or ALL for global | 
| name | String | Human-readable name | 
| centerLat | Number | Center latitude | 
| centerLng | Number | Center longitude | 
| radiusKm | Number | Radius in kilometers | 
| type | String | Geofence shape (CIRCLE) | 
| action | String | Action on violation (ALERT) | 
| active | Boolean | Whether geofence is active | 
| createdAt | String | ISO 8601 creation timestamp | 
| ttl | Number | DynamoDB TTL (90 days) | 

 **Indexes:** 
+ GSI1: vehicleId-index (query geofences by vehicle)

### Signal catalog table
<a name="signal-catalog-table"></a>

Stores the standardized signal definitions used throughout the guidance.

 **Schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| json\_field | String (PK) | JSON field name (for example, `speed`) | 
| signal\_name | String | Human-readable signal name | 
| vss\_path | String | COVESA VSS path (for example, `Vehicle.Speed`) | 
| signal\_group | String | Signal group (engine, tire, safety, etc.) | 
| data\_type | String | float, int, boolean, string | 
| unit | String | Unit of measurement | 
| min | Number | Minimum valid value | 
| max | Number | Maximum valid value | 
| actuator | Map | Actuator definition (if signal is commandable) | 

## S3 buckets
<a name="s3-buckets"></a>

Two buckets store telemetry archives and web application assets.

### Telemetry archive bucket
<a name="telemetry-archive-bucket"></a>

Stores raw telemetry data for long-term analysis.

 **Configuration:** 
+ Versioning: Enabled
+ Encryption: AES-256
+ Lifecycle policy: Transition to Glacier after 90 days
+ Intelligent-Tiering: Enabled for cost optimization

 **Data structure:** 

```
s3://cms-telemetry-archive/
├── year=2024/
│   ├── month=10/
│   │   ├── day=13/
│   │   │   ├── hour=12/
│   │   │   │   └── telemetry-{timestamp}.json.gz
```

### UI assets bucket
<a name="ui-assets-bucket"></a>

Hosts the Fleet Manager React application.

 **Configuration:** 
+ Versioning: Enabled
+ Encryption: AES-256
+ CloudFront origin access identity
+ Block public access: Enabled