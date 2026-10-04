

# Alarms the Guidance deploys
<a name="mon-alarms"></a>


| Stack | Alarms | Publishes to | Subscribed on deploy | 
| --- | --- | --- | --- | 
|  `cms-{stage}-flink`  | 40 | Flink alarms topic | Only if you set `FLINK_ALARM_EMAIL`  | 
|  `cms-{stage}-simulation`  | 3 | Simulation alarms topic | No | 
|  `cms-{stage}-fleetwise`  | 1 | Manifest alarm topic | No | 
|  `cms-{stage}-ui`  | 0 by default | Security operators topic | No | 

## Stream processing
<a name="mon-flink-alarms"></a>

The stream processing stack carries the great majority of the alarms, because it is where a silent failure does the most damage: a stopped processor does not reject telemetry, it simply stops producing trips, safety events and alerts while every other component continues to report healthy.

Seven alarm families cover the ten Managed Service for Apache Flink applications. The richer five are applied to the six domain-tier and OEM-path processors.


| Alarm suffix | Count | Fires when | 
| --- | --- | --- | 
|  `-down`  | 7 |  `downtime` exceeds 60,000 ms — the application has not been running for over a minute. | 
|  `-down-new`  | 6 |  `downtime` exceeds 0 — a stricter form of the same condition, on the domain-tier processors. | 
|  `-idle`  | 2 | The application processed zero records in 10 minutes. Distinct from being down: the job is running and consuming nothing, which is what a broken source or an empty topic looks like. | 
|  `-lag-high`  | 6 |  `records_lag_max` sustained above 10,000 for three periods — the consumer is falling behind its Kafka partitions. | 
|  `-restarts`  | 6 |  `fullRestarts` above 2 within 15 minutes — a crash loop rather than a single restart. | 
|  `-failed-checkpoints`  | 6 |  `numberOfFailedCheckpoints` above 0 — a state or sink health problem. Worth treating as urgent: an application that cannot checkpoint will reprocess from an older offset when it next restarts. | 
|  `-cpu-high`  | 6 |  `containerCPUUtilization` above 75% for three periods. A capacity-planning signal rather than an outage. | 
|  `-unmatched-topic`  | 1 | Telemetry arrived on a Kafka topic the OEM-path processor has no mapping for, so those records are being dropped rather than transformed. | 

**Note**  
The `-unmatched-topic` alarm does not self-clear in this release. It evaluates a rate over a cumulative Flink counter that never decrements, so once it fires it stays in `ALARM` even after the condition is resolved — which means it cannot signal a second occurrence. Treat its first firing as the signal, investigate, and set the alarm state manually once resolved. Tracked as a known limitation.

The distinction between `-down` and `-idle` is the one most worth internalizing. A processor that is down is visibly broken. A processor that is **idle** looks entirely healthy in the console — the application state is `RUNNING`, there are no errors in the log — and produces nothing. See [Troubleshooting](troubleshooting.md) for the diagnosis path.

## Simulation
<a name="mon-simulation-alarms"></a>

Three alarms cover conditions that waste money or produce misleading demonstrations rather than outages:
+  **Orphaned agent** — FleetWise Edge agents running with no matching active simulation session. These continue to consume compute and publish telemetry for vehicles nobody is simulating.
+  **Stale revision agent** — an agent running on a superseded task-definition revision, so it is not running the configuration you think you deployed.
+  **Agent-counter errors** — the Lambda that counts running agents failed on two consecutive runs, which means the other two alarms are evaluating stale input.

The third alarm is the one to wire first. It is the alarm that tells you the other two have stopped being trustworthy.

## Telemetry decoder manifest
<a name="mon-fleetwise-alarms"></a>

One alarm fires when the campaign-sync processor cannot fetch the decoder manifest. Without a manifest the processor cannot map CAN signal identifiers to signal names, so protobuf telemetry arrives and cannot be decoded. See [Decoder manifest](dynamic-data-collection.md#decoder-manifest-overview).

## Account provisioning (conditional)
<a name="mon-provisioning-alarms"></a>

The Fleet Manager stack defines alarms on its Amazon Cognito trigger functions and on sign-up denials, gated behind the account-provisioning feature. With that feature disabled — the default — the stack synthesizes zero alarms. If you enable it, subscribe the security operators topic before doing so, since these alarms cover authentication paths.

These alarms also set an OK action as well as an alarm action, so the topic receives recovery notifications and not only failures.