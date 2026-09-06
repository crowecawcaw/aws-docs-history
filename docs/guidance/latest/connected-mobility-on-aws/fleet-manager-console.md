

# Fleet Manager console
<a name="fleet-manager-console"></a>

The Fleet Manager console is a React-based web application built with [Cloudscape Design System](https://cloudscape.design/). It provides fleet operators with real-time visibility into vehicle status, trip history, safety events, maintenance alerts, and data collection campaigns. The console connects to the Fleet Management API and Commands API documented in the [Developer guide](developer-guide.md).

## Dashboard
<a name="fm-dashboard"></a>

![Fleet Manager Dashboard](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-dashboard.png)


The dashboard is the landing page after sign-in. It displays configurable widgets for fleet-wide metrics including vehicle utilization, distance driven, driver safety scores, braking events, battery state of health, and vehicle health status. Operators can add, remove, and rearrange widgets to customize their view. Action buttons provide quick access to the fleet map, simulation, and fleet management.

## Fleet management
<a name="fm-fleet-management"></a>

![Fleet Management](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-management.png)


The fleet management page lists all fleets with their vehicle counts and status. Operators can create new fleets, edit fleet details, associate vehicles (via a selection modal), disassociate vehicles, and delete fleets. Clicking a fleet opens the fleet detail page showing the fleet’s vehicles, active campaigns, and performance summary.

Two Cognito user roles govern fleet access. A **platform-admin** user has cross-fleet authority and can perform bulk enrollment and unenrollment operations across all fleets — for example, enrolling a batch of OEM cloud-connected vehicles in a single API call. A **fleet-operator** user is scoped to the fleets listed in their `custom:fleetIds` Cognito claim and can manage vehicles and run bulk operations only within those fleets. Bulk enrollment supports up to four OEM vehicle enrollments per hour per fleet; operations that exceed this quota return a 429 response and can be retried.

![Fleet Detail](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-detail.png)


## Vehicle management
<a name="fm-vehicle-management"></a>

![Vehicle Management](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-vehicle-management.png)


The vehicle management page displays a searchable, sortable table of all registered vehicles with columns for VIN, status, fleet assignment, and last known location. Operators can create new vehicles (which provisions an IoT certificate and thing in AWS IoT Core), edit vehicle attributes, or delete vehicles.

## Vehicle detail
<a name="fm-vehicle-detail"></a>

![Vehicle Detail](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-vehicle-detail.png)


The vehicle detail page is the most information-dense screen in the console. It provides:
+  **Live telemetry** — Real-time signal values served from the Redis Last Known State cache (see [Last Known State pattern](last-known-state-pattern.md)). Includes speed, engine RPM, temperatures, tire pressures, battery state, and all other signals from the signal catalog.
+  **Trips tab** — List of completed and active trips with start/end times, distance, duration, and driver score.
+  **Safety events tab** — Safety events detected during this vehicle’s trips (see [Safety event detection](safety-event-detection.md)).
+  **Remote commands panel** — Send actuator commands to the vehicle (lock doors, flash lights, start engine) and view command history with round-trip latency (see [Remote commands](remote-commands-flow.md)).
+  **Geofence widget** — Configure and monitor geofence boundaries for the vehicle.
+  **Tire pressure widget** — Visual display of per-wheel tire pressure and tread depth.
+  **Campaign table** — Active FleetWise data collection campaigns targeting this vehicle.
+  **FWE log viewer** — Stream FleetWise Edge agent logs when running in FWE simulation mode.

## Trip detail
<a name="fm-trip-detail"></a>

![Trip Detail](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-trip-detail.png)


The trip detail page shows a completed or active trip with a route map visualization, telemetry timeline, safety events that occurred during the trip, and the driver safety score breakdown. The route is plotted on an Amazon Location Service map using the GPS coordinates stored in the trip’s DynamoDB record (see [Trip lifecycle](trip-lifecycle.md)).

## Fleet map
<a name="fm-fleet-map"></a>

![Fleet Map](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-map.png)


The fleet map displays real-time vehicle positions on an interactive map powered by Amazon Location Service. Vehicle locations are read from the Redis geospatial index using `GEOSEARCH` (see [LKS read path](last-known-state-pattern.md#lks-read-path-detail)). Only vehicles with active trips appear on the map. Clicking a vehicle marker shows a card with current speed, heading, driver, and trip status.

## Driver management
<a name="fm-driver-management"></a>

![Driver Management](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-driver-management.png)


The driver management page lists all drivers with their safety scores, trip counts, and fleet assignments. Clicking a driver opens the driver detail page showing trip history, safety event history, and a per-trip score trend.

![Driver Detail](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-driver-detail.png)


## Safety alerts
<a name="fm-safety-alerts"></a>

![Safety Alerts](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-safety-alerts.png)


The safety alerts page displays all safety events across the fleet in a filterable table. Operators can filter by fleet, vehicle, event type, severity, and time range. Each row shows the event type, severity, vehicle, trip, timestamp, and trigger details. Clicking a row opens a location modal showing where the event occurred on a map. Events are generated by the SafetyProcessor (see [Safety event detection](safety-event-detection.md)).

## Service alerts
<a name="fm-service-alerts"></a>

The service alerts page shows maintenance alerts generated by the MaintenanceProcessor (see [Maintenance alert detection](maintenance-alert-detection.md)). Alerts are displayed with type, severity, vehicle, DTC code, trigger signal, and threshold. Operators can filter by fleet and time range to focus on specific maintenance concerns.

## Simulation
<a name="fm-simulation"></a>

![Simulation](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-simulation.png)


The simulation page provides controls to start, configure, and monitor vehicle telemetry simulations. Operators select the number of vehicles, trips per vehicle, city, safety event rate, and telemetry mode (MQTT Direct or FleetWise Edge). Built-in presets (Quick Test, Fleet Demo, Stress Test) provide one-click configurations. The page shows running simulations with status, vehicle count, and elapsed time. For details on how simulation works, see [Simulation platform](simulation-platform.md).

![Single Trip Simulator](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-single-trip-simulator.png)


From the vehicle detail page, operators can launch a single-vehicle simulation directly. This starts a trip for the selected vehicle without leaving the detail view.

![Simulator Logs](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-simulator-logs.png)


The simulator log viewer streams real-time output from the simulation process, showing telemetry publish events, trip start/end events, and safety event injections.

![FleetWise Edge Agent Logs](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fwe-logs.png)


When running in FleetWise Edge mode, the FWE log viewer streams the agent’s stdout showing MQTT connection status, checkin messages, collection scheme receipts, and CAN signal collection activity.

## Data processing
<a name="fm-data-processing"></a>

![Signal Catalog](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-data-processing.png)


The data processing page provides a read-only browser for the signal catalog, event catalog, decoder manifests, and data transformation configurations. Operators can browse all 260\+ signals grouped by category, view signal metadata (VSS path, unit, data type, range), and search for specific signals.

![Event Catalog](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-event-catalog.png)


The event catalog viewer displays all safety and maintenance event detection rules with their trigger signals, operators, thresholds, and severity levels. This is the same catalog used by the SafetyProcessor and MaintenanceProcessor Flink applications (see [Safety event detection](safety-event-detection.md) and [Maintenance alert detection](maintenance-alert-detection.md)).

![Campaigns](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-campaigns.png)


The campaigns view lists all FleetWise data collection campaigns with their status (RUNNING, SUSPENDED, COMPLETED), target vehicles, and signal counts. Operators can create new campaigns, suspend or resume active campaigns, and view campaign details. For details on how campaigns control FWE agent behavior, see [Campaigns](dynamic-data-collection.md#campaigns-overview).

![Campaign Detail](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-campaign-detail.png)


## Analytics
<a name="fm-analytics"></a>

The analytics section provides four views:
+  **Telemetry dashboard** — Real-time and historical telemetry visualization across the fleet.
+  **Driver behavior** — Driver safety score trends, event frequency analysis, and fleet-wide behavior patterns.
+  **Geofence events** — Geofence entry/exit events with map visualization.
+  **Trip analytics** — Trip duration, distance, and efficiency metrics across the fleet.

## Settings
<a name="fm-settings"></a>

![Settings](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-settings.png)


The settings page allows operators to configure application preferences including API endpoint, simulation service endpoint, and display options. Dark mode can be toggled from the user dropdown menu (Switch Theme) or the settings page. The theme preference persists across sessions via localStorage.

## Profile
<a name="fm-profile"></a>

The profile page displays the current user’s account details including email, username, role, and account status. Access it from the user dropdown menu in the top navigation bar.

## Warranty
<a name="fm-warranty"></a>

The warranty page provides warranty claims management with two views:
+  **Warranty-Eligible Failures** — Agent-detected component failures that match warranty coverage rules, with confidence scores, estimated claim amounts, and days remaining on coverage.
+  **Claim Tracking** — Filed claims with status tracking (Submitted, Approved, Paid, Denied), OEM information, and escalation actions for denied claims.

KPIs show total claims, recovered amount year-to-date, open claims, and pending amount. A separate tab tracks recall-related warranty claims.

## Driver Assignment
<a name="fm-driver-assignment"></a>

Each vehicle has a default assigned driver shown on the vehicle detail page. Drivers are assigned round-robin from the active driver pool during fleet setup. Fleet managers can reassign drivers from the vehicle detail page. When a trip is detected, it is attributed to the vehicle’s current driver for safety event tracking and driver scoring. Drivers can also claim a vehicle themselves from the Fleet Manager web interface or the companion iOS application, overriding the current assignment so that trips are attributed to the correct driver without fleet manager intervention.

## In-vehicle assistant
<a name="fm-assistant"></a>

The Fleet Manager console includes a conversational assistant panel that lets users ask questions about their fleet, vehicles, and diagnostic trouble codes in natural language. The assistant is accessible from the navigation bar and opens as a side panel within the Fleet Manager interface.

When a user sends a message, the Fleet Manager web application routes the request to the `/assistant/chat` endpoint of the VSA API, which forwards it to the AgentCore text runtime (`vsa_supervisor_text_staging`). The runtime invokes a Bedrock supervisor agent that coordinates a set of specialist agents to fulfill the request. The supervisor grounds responses in the Automotive Data Platform (ADP) knowledge base, which contains vehicle diagnostic guides, DTC explanations, and maintenance procedures. Responses are streamed back to the chat panel.

The assistant adapts its behavior based on the authenticated user’s Cognito claims. A user with the default `fleet_driver` role receives driving-focused guidance — trip summaries, safety event explanations, and DTC context for their own vehicle. A user with `custom:role=service-advisor` in their Cognito profile receives a service-advisor persona, which provides broader cross-vehicle diagnostic context suited for workshop and service center use cases.

The assistant capability requires the optional `cms-{stage}-bedrock-agents` stack. Deploy it with `make deploy-bedrock-agents` after the core platform is running. If the stack is not deployed, the assistant panel is present in the UI but the `/assistant/chat` endpoint is not available. See [Architecture details](architecture-details.md) for the BedrockAgentsStack configuration and the inference-profile IAM pattern required for cross-region model invocation.