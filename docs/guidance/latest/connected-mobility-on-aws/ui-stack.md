

# Fleet Manager application
<a name="ui-stack"></a>

The Fleet Manager application provides the web interface and backend APIs.

## CloudFront distribution
<a name="cloudfront-distribution"></a>

Delivers the React application globally with low latency.

 **Configuration:** 
+ Origin: S3 bucket (UI assets)
+ Price class: Use all edge locations
+ TLS: Minimum TLS 1.2
+ Compression: Enabled (gzip, brotli)
+ Caching: Optimized for SPA

 **Cache behaviors:** 
+  `/`: Serve index.html (no cache)
+  `/static/*`: Cache for 1 year
+  `/api/*`: Forward to API Gateway (no cache)

## API Gateway
<a name="api-gateway"></a>

RESTful APIs for fleet management operations.

 **Endpoints:** 


| Method | Path | Description | 
| --- | --- | --- | 
| GET | /vehicles | List all vehicles | 
| GET | /vehicles/{vin} | Get vehicle details | 
| PUT | /vehicles/{vin} | Update vehicle | 
| GET | /vehicles/{vin}/trips | Get vehicle trips | 
| GET | /vehicles/{vin}/alerts | Get vehicle alerts | 
| POST | /alerts/{id}/acknowledge | Acknowledge alert | 
| GET | /drivers | List all drivers | 
| GET | /drivers/{id} | Get driver details | 
| GET | /location/geocode | Geocode address | 
| GET | /location/route | Calculate route | 
| POST | /api/commands/{vehicleId} | Send remote command to vehicle | 
| GET | /api/commands/{vehicleId} | Get command history for vehicle | 
| GET | /api/commands/catalog | List available actuatable commands | 
| POST | /api/geofences | Create a geofence | 
| GET | /api/geofences/{vehicleId} | List geofences for vehicle | 
| DELETE | /api/geofences/{geofenceId} | Deactivate a geofence | 

 **Authorization:** 
+ Cognito User Pool authorizer
+ JWT validation on all requests
+ IAM roles for service-to-service

## Lambda functions
<a name="lambda-functions"></a>

Backend logic for API operations.

 **Functions:** 
+  `vehicles-handler`: CRUD operations on vehicles
+  `trips-handler`: Query trip history
+  `alerts-handler`: Manage alerts
+  `drivers-handler`: Manage drivers
+  `location-handler`: Location Service integration
+  `cache-handler`: ElastiCache operations

 **Configuration:** 
+ Runtime: Python 3.11
+ Memory: 512 MB
+ Timeout: 30 seconds
+ VPC: Private subnets (for ElastiCache access)

## Cognito configuration
<a name="cognito-configuration"></a>

User authentication and authorization.

 **User pool:** 
+ Sign-up: Email verification required
+ MFA: Optional (TOTP)
+ Password policy: 8\+ characters, mixed case, numbers
+ Account recovery: Email

 **Identity pool:** 
+ Authenticated role: Access to API Gateway
+ Unauthenticated role: Denied

## Location Service
<a name="location-service"></a>

Mapping and geocoding capabilities.

 **Resources:** 
+ Map: Esri Street Map
+ Place index: Esri geocoding
+ Route calculator: Esri routing

 **Features:** 
+ Real-time vehicle tracking
+ Historical route visualization
+ Address geocoding
+ Route calculation
+ Geofencing (future)

## Fleet Manager UI
<a name="fleet-manager-ui"></a>

React-based web application.

 **Pages:** 
+ Dashboard: Fleet overview with key metrics
+ Vehicles: List and manage vehicles
+ Map: Real-time vehicle tracking
+ Trips: Trip history and analytics
+ Alerts: Maintenance and safety alerts
+ Drivers: Driver management and scoring

 **Technologies:** 
+ React 18
+ TypeScript
+ AWS Amplify
+ CloudScape Design System
+ MapLibre GL JS (for maps)