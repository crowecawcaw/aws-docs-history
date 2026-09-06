

# Use cases
<a name="use-cases"></a>

 **Fleet Management and Optimization** 

Fleet operators use the guidance to monitor vehicle locations, track trips, and optimize routes in real-time. The Fleet Manager provides visibility into fleet utilization, driver behavior, and operational efficiency. Location Services enable route optimization and geofencing for improved logistics.

 **Predictive Maintenance** 

The solution detects maintenance conditions from vehicle sensor data including engine temperature, tire pressure, battery voltage, and diagnostic trouble codes. Flink applications analyze telemetry patterns to predict component failures before they occur, reducing downtime and maintenance costs.

 **Safety and Compliance Monitoring** 

Real-time processing identifies safety events including speeding, harsh braking, rapid acceleration, and sharp turns. Fleet managers receive immediate alerts for safety violations, enabling proactive driver coaching and compliance monitoring. Historical data supports safety audits and regulatory reporting.

 **Usage-Based Insurance** 

Insurance providers integrate with the guidance APIs to access driving behavior data for usage-based insurance programs. The guidance tracks mileage, driving patterns, safety events, and vehicle usage to calculate personalized insurance premiums based on actual driving behavior.

 **Connected Vehicle Services** 

OEMs and service providers use the guidance as a platform for connected vehicle services including remote diagnostics, over-the-air updates, emergency assistance, and vehicle health monitoring. The scalable architecture supports millions of connected vehicles.

 **Electric Vehicle Management** 

The solution monitors EV-specific metrics including battery state of charge, charging status, range estimation, and charging station locations. Fleet managers optimize charging schedules, track energy consumption, and manage charging infrastructure.

 **In-UI Conversational Fleet Operations** 

Fleet drivers and service advisors interact with a conversational assistant embedded in the Fleet Manager application. The assistant routes questions through the AgentCore text runtime to a Bedrock supervisor agent, which can retrieve grounded answers from an automotive knowledge base. Persona context — fleet driver or service advisor — is inferred automatically from Amazon Cognito user claims, so each user receives role-appropriate responses without manual configuration.

 **OEM Cloud-to-Cloud Telemetry Ingestion** 

OEMs that host vehicle telemetry in their own cloud systems integrate with the guidance through configurable transform manifests. The OEM cloud connector ingests data from third-party APIs and lands it on the same Amazon MSK topic used by other telemetry sources, so downstream Flink processors handle OEM data identically to MQTT Direct or FleetWise Edge telemetry without code changes.