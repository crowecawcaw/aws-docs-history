# How monitoring and incident management for Amazon EKS works in AMS Accelerate

**Generation:** As part of onboarding monitoring and incident management for EKS, AMS configures baseline monitoring for the Amazon EKS
clusters that you selected in your managed account. AMS uses a combination of Amazon Managed Service for Prometheus alert manager rules and Amazon CloudWatch event rules to configure baseline monitoring. An
AMS-configured Prometheus server in your cluster scrapes and remote-writes your Prometheus metrics to an Amazon Managed Service for Prometheus endpoint in the same Region. The baseline monitoring
configuration generates an alert when a Prometheus alert manager rule is triggered or a CloudWatch event is generated.

**Aggregation:** AMS sends all alerts that your resources generate to the AMS monitoring system by directing them to an Amazon Simple Notification Service topic
that's managed by AMS.

**Processing and impact analysis:** AMS analyzes the alerts and then processes them based on their potential for impact. AMS classifies t
he alerts as follows:

- **Alerts with known customer impact:** For these alerts, AMS creates a new incident report using the
  [incident management](acc-manage-incidents.md "acc-manage-incidents.md") process.
- **Alerts with uncertain customer impact:** For these alerts, AMS sends an incident report. In many cases, these alerts ask you to
  verify the
  impact before AMS can take action. For such alerts, AMS sends an [alert notification](acc-baseline-eks-alerts.md#acc-alerts-and-actions "acc-baseline-eks-alerts.md#acc-alerts-and-actions") with the details and checks whether the alert needs
  a mitigating action. AMS provides options for mitigating actions in the notification. If your reply confirms that the alert is an incident, AMS then triggers the creation of a
  new incident report and initiates the incident management process. Any service notification that receives a response of "no customer impact" or no response at all for three days is
  marked as resolved. Also, the corresponding alert is marked as resolved.
- **Alerts with no customer impact:** If, after evaluation, AMS determines that the alert doesn't have any customer impact, the alert is closed.

## AMS responsibility matrix (RACI)

The AMS responsible, accountable, consulted, and informed, or RACI matrix assigns the primary responsibility to either the customer or AMS for a variety of activities. The f
ollowing table provides an overview of the responsibilities of customer and AMS for activities in an application that uses Monitoring and Incident Management for Amazon EKS.

- **R** stands for the responsible party that does the work to achieve the task.
- **A** stands for the accountable party.
- **C** stands for consulted; the party whose opinions are sought, typically as subject matter experts; and with whom there is bilateral communication.
- **I** stands for informed; the party which is informed on progress, often only on completion of the task or deliverable.

| Activity                                                                                                                                  | Customer | AMS |
| ----------------------------------------------------------------------------------------------------------------------------------------- | -------- | --- |
| Discovery for AMS requirements                                                                                                            | I        | R   |
| Enable AMS permissions (RBAC) for cluster access                                                                                          | R        | C   |
| Install Amazon EC2 Systems Manager Agent on worker nodes if it isn't already present                                                      | R        | C   |
| Deploy AMS on-cluster components, such as Prometheus, Prometheus Node Exporter, and<br>kube-state-metrics in an AMS namespace, as needed. | C        | R   |
| Provision Amazon Managed Service for Prometheus in the AMS control plane                                                                  | I        | R   |
| Configure Prometheus alert manager in the AMS control plane                                                                               | I        | R   |
| Provide Amazon Managed Grafana template and assist with configuration                                                                     | C        | R   |
| Enable GuardDuty EKS Audit Log Monitoring                                                                                                 | C        | R   |
| Enable Amazon EKS control plane logging                                                                                                   | I        | R   |
| Monitor the health and performance of the Amazon EKS control plane                                                                        | I        | R   |
| Monitor the health and performance of your Amazon EKS cluster (cluster, node, workload, pod, API Server and CoreDNS)                      | I        | R   |
| Triage alerts and provide incident response for Amazon EKS                                                                                | I        | R   |
| Run diagnostic commands during incidents                                                                                                  | I        | R   |
| Analyze logs during incidents (control plane and pod logs)                                                                                | I        | R   |
| Incident response for AWS network issues                                                                                                  | I        | R   |
| Respond to GuardDuty EKS Audit Log Monitoring findings                                                                                    | I        | R   |
| Provide customer guidance on actions to remediate incidents when possible                                                                 | I        | R   |
