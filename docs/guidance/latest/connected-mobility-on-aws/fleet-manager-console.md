

# What it can do
<a name="fleet-manager-console"></a>

The Fleet Intelligence portal is a React web application built with [Cloudscape Design System](https://cloudscape.design/). The navigation groups its screens by job: **Operations** (vehicles, vehicle map, fleets, drivers, service), **Data products**, **Cost**, **Compliance** (safety, recalls and coverage, preventive-maintenance compliance), **Assets** (lifecycle), and **Setup** (data source catalog, users, simulation, and system monitoring). Every screen respects the fleet selector at the top of the page, and every list is filtered server-side to the fleets the signed-in user may see. The portal calls the Fleet Management API and the Commands API documented in the [Developer guide](developer-guide.md).

Each section below shows a screen, what an operator does there, and how the platform produces what the screen shows.

## Fleets
<a name="fm-fleet-management"></a>

![Fleet Management page: totals for fleets](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-management.png)


 **What you can do.** See every fleet with its vehicle count, connected count, and operational city; create, edit, and delete fleets; and open a fleet to see its vehicles, campaigns, and performance. From a fleet you can associate and disassociate vehicles, and enroll or unenroll vehicles in bulk.

![Fleet detail page](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-detail.png)


 **How it works.** Fleets and their memberships are held in the `cms-{stage}-storage-fleets` and fleet-enrollment DynamoDB tables. Two Cognito roles govern access. A `platform-admin` user acts across all fleets. A `fleet-operator` user is limited to the fleets in their `custom:fleetIds` claim, and every fleet, vehicle, trip, and alert route checks that claim before it returns data. Vehicles that report through an OEM cloud are enrolled through the connector’s admin routes, which apply the OEM’s enrollment rate limit and return HTTP 429 when it is exceeded. See [OEM cloud connector](connector-stack.md).

## Vehicles
<a name="fm-vehicle-management"></a>

![Vehicle Management page: totals for registered](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-vehicle-management.png)


 **What you can do.** Search, sort, and filter every vehicle you can see by fleet, VIN, make, model, plate, or data source (**Onboard** for vehicles that connect directly, **Offboard** for vehicles that report through an OEM cloud). Create, edit, unenroll, and delete vehicles, and switch to the map view.

 **How it works.** Creating an onboard vehicle provisions an AWS IoT Core thing and X.509 certificate for it, and records the vehicle in `cms-{stage}-storage-vehicles`. Connection status and last-seen time come from the Last Known State cache, so the **Connected** count reflects telemetry that is arriving now (see [Last Known State pattern](fip-how-it-works.md#last-known-state-pattern)).

## Vehicle detail
<a name="fm-vehicle-detail"></a>

![Vehicle detail page](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-vehicle-detail.png)


Vehicle detail is the portal’s working screen for one vehicle. A header shows the vehicle, its fleet, its data source, and a single status line for connection and last-seen time. Seven tabs hold the rest:


| Tab | What it shows | 
| --- | --- | 
| Overview | A snapshot: key figures, current location, the vehicle health score, tire pressures, cost of ownership, the last trip and recent activity, and the vehicle’s open findings. | 
| Trips & Safety | Every trip for the vehicle, followed by its safety events, paged. Each event opens its location on a map. See [Trips](#fm-trip-detail). | 
| Diagnostics | Remote vehicle diagnostics: a vehicle health strip, on-demand fault-code scans, freeze frames, safety-classified diagnostic routines, diagnostic sessions, and dispatch to a dealer. See [Remote vehicle diagnostics](remote-diagnostics.md). | 
| Service & Recalls | Service history, open recalls for the VIN, warranty coverage, and dealer repair orders, with service scheduling for users who may change the vehicle. | 
| Remote Commands | The command panel and command history. Shown only to users who may act on the vehicle. See [Remote commands](#fm-remote-commands). | 
| Details | The full vehicle record, OEM enrollment, the Connected Services subscription card, and the data collection campaigns that target the vehicle. | 
| Simulation | For onboard vehicles: start and stop the vehicle’s edge agent, run a single-trip simulation, and stream the simulator and edge agent logs. See [Simulation](#fm-simulation). | 

 **How it works.** Each tab loads its own data when it is first opened, so the page opens quickly even for a vehicle with a long history. Write controls (remote commands, scheduling, simulation) appear only for a `platform-admin` user or a `fleet-operator` on the vehicle’s fleet; the API enforces the same rule, so hiding a control is a convenience, not the security boundary. Recall status is read once per page and shared by the header, the Overview tile, and the Service & Recalls tab, so the three always agree.

## Trips
<a name="fm-trip-detail"></a>

![Trip detail page: a trip summary with start and end time](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-trip-detail.png)


 **What you can do.** Open any trip from a vehicle’s Trips & Safety tab or from a driver to see its summary (times, duration, distance, average and maximum speed, energy used, and the driver score), the safety events recorded during it with their speed and severity, and its route on a map with the event locations marked.

 **How it works.** The TripProcessor Flink application detects trip start and end from ignition transitions, assigns a trip ID, and writes the trip record with its GPS track to DynamoDB. A sweeper closes trips whose vehicle stops reporting. The driver score starts at 100, takes deductions for each safety event, and is recalculated 30 seconds after the trip ends to catch late events. The route is drawn with Amazon Location Service. See [Trip lifecycle](fip-how-it-works.md#trip-lifecycle) and [Driver scoring](fip-how-it-works.md#driver-scoring).

## Vehicle map and geofences
<a name="fm-fleet-map"></a>

![Fleet map](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fleet-map.png)


 **What you can do.** See every reporting vehicle on a live map, filter by fleet and status, overlay safety and maintenance heatmaps, and draw geofences. Selecting a vehicle shows its speed, heading, driver, and trip status.

 **How it works.** Positions are read from the Redis geospatial index in the Last Known State cache, and the map refreshes as new telemetry arrives over the WebSocket fan-out. Geofences are stored per vehicle, and the GeofenceProcessor Flink application raises an event when a vehicle crosses a boundary. See [Remote commands and geofences](fip-architecture-details.md#commands-stack).

## Drivers
<a name="fm-driver-management"></a>

![Driver Management page: totals for drivers](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-driver-management.png)


 **What you can do.** Manage the driver roster: add, edit, and remove drivers, see who is on duty or on leave, which fleet each belongs to, and whose license expires soon. A driver’s detail page shows their trips, safety events, and score trend.

![Driver detail page](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-driver-detail.png)


 **How it works.** Each trip is attributed to the vehicle’s assigned driver when it starts. Drivers can also claim a vehicle themselves from the portal or the [companion application](companion-app.md), so trips are attributed correctly without an operator. See [Driver assignment](#fm-driver-assignment).

## Safety
<a name="fm-safety-alerts"></a>

![Safety Management page: 30-day safety event totals](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-safety-alerts.png)


 **What you can do.** See every safety event across your fleets in the last 30 days, with the high and critical share, the most common event type, and the riskiest driver. Tabs rank risky drivers and risky vehicles. Each event shows its type, severity, detection source, and description, and opens its location on a map.

 **How it works.** The SafetyProcessor Flink application evaluates telemetry against the catalog-driven safety rules (harsh braking, harsh acceleration, harsh cornering, speeding, phone use, seat belt unbuckled while moving, and others) and writes each event to DynamoDB and the `cms-alerts` topic. A per-vehicle cooldown stops the same event type from firing again within five minutes. See [Safety event detection](fip-how-it-works.md#safety-event-detection).

## Service
<a name="fm-service-alerts"></a>

![Service page: open alerts](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-service.png)


 **What you can do.** Work the fleet’s maintenance queue: open alerts by severity with estimated cost, critical safety alerts that need immediate action, active recalls with affected-vehicle counts, and agent activity. Filter by status, vehicle, or type, and schedule service from a row.

 **How it works.** The MaintenanceProcessor Flink application detects ICE and EV maintenance conditions and diagnostic trouble codes and writes alerts to DynamoDB. Service history is read live from the dealer management system where it is connected; if the dealer system can’t be reached, the page shows the rows it holds in its cache and says how old they are. See [Maintenance alert detection](fip-how-it-works.md#maintenance-alert-detection).

## Remote commands
<a name="fm-remote-commands"></a>

![Remote Commands tab: a Vehicle State panel showing door](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-remote-commands.png)


![All Commands: the command catalog grouped into Charging](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-remote-commands-catalog.png)


 **What you can do.** From a vehicle’s Remote Commands tab, lock and unlock doors, flash lights, sound the horn, start and stop the engine, control climate, windows, and trunk, and see the command history with each command’s result and round-trip time.

 **How it works.** The command catalog is derived from the actuatable signals in the signal catalog. The Commands API authorizes the caller against the vehicle’s fleet, records the command, and publishes it to the vehicle over AWS IoT Core. The vehicle’s acknowledgement returns through an IoT rule that updates the command record, so the history shows what the vehicle did, not only what was sent. See [Remote commands](fip-how-it-works.md#remote-commands-flow).

## Simulation
<a name="fm-simulation"></a>

![Fleet Simulation page: a new-simulation form with mode](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-simulation.png)


 **What you can do.** Generate realistic telemetry without real vehicles. Choose the mode (MQTT Direct, or FleetWise Edge Agent over a simulated CAN bus), the city, trips per vehicle, route length, and which safety and maintenance events to inject, then select vehicles and start. The table lists running and past simulations with their logs.

![Single trip simulator](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-single-trip-simulator.png)


From a vehicle’s Simulation tab you can run one trip for that vehicle, and start or stop its edge agent.

![Simulator logs](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-simulator-logs.png)


The simulator log shows telemetry publishes, trip starts and ends, and injected events.

![FleetWise Edge Agent logs](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-fwe-logs.png)


In FleetWise Edge mode, the agent log shows its MQTT connection, check-ins, the collection schemes it received, and CAN signal collection.

 **How it works.** Simulations run as Amazon ECS tasks in your account. In FleetWise Edge mode, each vehicle runs an edge agent and a simulated vehicle bus, so the data takes the same path a real vehicle’s would, through AWS IoT Core, Amazon MSK, and the Flink processors. See [Simulation platform](simulation-platform.md).

## Signal and event catalog, and campaigns
<a name="fm-data-processing"></a>

![Signal and Event Catalog page: tabs for signal catalog](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-data-processing.png)


 **What you can do.** Browse the signals vehicles can report, grouped by category, with their units, types, and ranges; the vehicle models; the event catalog; decoder and transform manifests; and data collection campaigns.

![Event catalog: every safety and maintenance event with its category](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-event-catalog.png)


The event catalog lists every safety and maintenance event the platform detects, with its severity, and which vehicle models can emit it. The SafetyProcessor and MaintenanceProcessor read the same catalog, so the screen shows exactly the rules that run.

![Campaigns: data collection campaigns with type](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-campaigns.png)


Campaigns decide what each vehicle collects and how often. Operators create campaigns, see each one’s collection scheme, status, and target vehicles and signals, and open a campaign for detail.

![Campaign detail](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-campaign-detail.png)


 **How it works.** The signal catalog, decoder manifest, and campaign layers are described in [Dynamic data collection](csp-how-it-works.md#dynamic-data-collection), and campaign management in [Campaign management](fip-how-it-works.md#campaign-management-ui).

## Recalls and coverage
<a name="fm-warranty"></a>

![Recalls and Coverage page: totals for warranty claims](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-recalls-coverage.png)


 **What you can do.** See warranty claims and recoveries, and the failures that are still under warranty: each with its component, fault code, mileage against the warranty limit, coverage remaining, estimated claim value, and confidence. A second tab tracks recall-related claims. Claims are filed and recovered in the dealer management system. See [Recall and warranty management](recall-warranty-management.md).

## Settings and profile
<a name="fm-settings"></a>

![Settings page: appearance](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fm-settings.png)


Settings holds the theme (light or dark), the simulator mode (local, or the Amazon ECS service in your account), and your account’s email and Region. The theme can also be switched from the user menu and is remembered in the browser.

<a name="fm-profile"></a>The profile page, from the user menu, shows your email, username, role, and account status.

## Driver assignment
<a name="fm-driver-assignment"></a>

Each vehicle has an assigned driver shown on its detail page. Drivers are assigned from the active driver pool when a fleet is set up, and operators can reassign them. When a trip starts it is attributed to the vehicle’s current driver for safety event tracking and driver scoring. Drivers can also claim a vehicle themselves from the portal or the companion iOS application.

## In-vehicle assistant
<a name="fm-assistant"></a>

The Fleet Intelligence portal includes a conversational assistant panel that lets users ask questions about their fleet, vehicles, and diagnostic trouble codes in natural language. The assistant is accessible from the navigation bar and opens as a side panel within the Fleet Intelligence portal interface.

When a user sends a message, the Fleet Intelligence portal routes the request to the `/assistant/chat` endpoint of the AVX API, which forwards it to the AgentCore text runtime (`vsa_supervisor_text_staging`). The runtime invokes a Bedrock supervisor agent that coordinates a set of specialist tools to fulfill the request. The supervisor grounds responses in the Automotive Data Platform (ADP) knowledge base, which contains vehicle diagnostic guides, DTC explanations, and maintenance procedures. Responses are streamed back to the chat panel.

The assistant adapts its behavior based on the authenticated user’s Cognito claims. A user with the default `fleet_driver` role receives driving-focused guidance — trip summaries, safety event explanations, and DTC context for their own vehicle. A user with `custom:role=service-advisor` in their Cognito profile receives a service-advisor persona, which provides broader cross-vehicle diagnostic context suited for workshop and service center use cases.

The assistant is served by the companion Agentic Vehicle Experience (AVX) accelerator, not by any stack in this repository. Populate the `vsaApiEndpoint` field in `runtimeConfig.json` at UI deploy time to point to a deployed AVX API Gateway stage. If `vsaApiEndpoint` is unset (or AVX has not been deployed), the assistant panel is present in the UI but reports the assistant as not configured; the rest of the Fleet Intelligence portal operates normally. See [Architecture details](architecture-details.md) for the CMS-side integration surface.

## Fleet intelligence
<a name="fm-fleet-intelligence"></a>

The `/fleet-intelligence/*` screens turn fleet data into decisions. The overview, `/fleet-intelligence/overview`, is the landing page. The screens cover:
+  **Overview** — `/fleet-intelligence/overview`, the landing page, which shows what is waiting on the operator and how each feature is doing. Four headline KPIs with charts sit at the top: cost per mile against its 90-day baseline, fleet utilization against target, recall completion, and warranty recovered this year. Below them, from top to bottom: the Action Queue summary, which lists recommendations from all three agents by priority and marks the ones no approval rule may approve (grounding a vehicle, a safety recall, filing a warranty claim); safety recalls, with vehicles confirmed by telemetry shown next to vehicles matched by VIN only; cost; utilization; warranty recovery; lifecycle; and agent activity. Each tile shows its source’s own "as of" time and links to its full screen. A tile whose source is not connected reads "Unavailable" with a reason, never zero.  
![Fleet Intelligence overview: four KPI cards with charts (cost per mile against its 90-day baseline](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fi-overview.png)
+  **Fleet cost intelligence** — total cost of ownership, cost per mile, preventive-maintenance compliance, cost outliers, and per-vehicle sell timing. See [Fleet cost intelligence](fleet-cost-intelligence.md).
+  **Dynamic fleet rebalancing** — utilization by location, supply-demand gaps, demand forecasts, and costed vehicle moves. See [Dynamic fleet rebalancing](dynamic-fleet-rebalancing.md).
+  **Recall and warranty management** — active recalls matched to the fleet, completion tracking, warranty-eligible failures, and claim recovery. See [Recall and warranty management](recall-warranty-management.md).