# Design principles

- **Automatically recover from
  failure:** By monitoring Amazon WorkSpaces and
  AppStream for key performance indicators (KPIs), you can run
  automation when a threshold is breached. These KPIs should be
  a measure of business value, not just technical aspects of the
  service operation. This allows for automatic notification and
  tracking of failures, as well as automated recovery processes
  that remediate the failure. For example, you can use Amazon CloudWatch to set alarms and Amazon EventBridge to route these
  events to AWS Lambda or AWS Systems Manager, which can run
  recovery actions automatically.
- **Test recovery procedures:**
  Enable the simulation of various failure modes or the
  replication of historical failure scenarios. This approach
  facilitates the identification and exploration of potential
  failure pathways, allowing for preemptive testing and
  remediation. Addressing common and previously experienced
  vulnerabilities proactively helps you reduce the risk of
  encountering actual failures in production environments.
  Regularly test Amazon WorkSpaces and AppStream recovery using
  AWS Fault Injection Service or other DR tools to validate
  recovery procedures.
- **Scale horizontally to increase
  aggregate workload availability:** Replace one large
  resource with multiple small resources to reduce the impact of
  a single failure on the overall workload. Distribute requests
  across multiple, smaller resources to verify that they don't
  share a common point of failure. For Amazon WorkSpaces, this
  means deploying instances across multiple Availability Zones
  and using service-specific load balancing to distribute user
  connections, enhancing availability and fault tolerance.
- **Stop guessing capacity:** A
  common cause of failure in on-premises workloads is resource
  saturation. This occurs when the demand placed on a workload
  exceeds its capacity. In the cloud, you can monitor demand and
  workload utilization and adjust the number of WorkSpaces to
  maintain the optimal level to satisfy demand without
  over-provisioning or under-provisioning.
