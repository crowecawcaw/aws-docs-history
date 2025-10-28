# EDI Cloud Operations features and entitlements

ECO offers the following features:

- **Deployment and upgrades** – ECO deploys EDI on AWS instances in your AWS accounts, provides initial
  setup and configuration support, and deploys maintenance and feature upgrades as necessary.
- **Observability** – ECO monitors the health of your EDI environment. ECO proactively detects and responds to
  alerts and resolves issues in the EDI environment to maintain availability of the data platform and APIs.
- **Incident management** – ECO responds to incidents and resolves issues. You can contact ECO engineers
  24x7 using the AWS Support Center Console, with response times as defined in [Incident management response time](eco-sd.md#incident-response-time "eco-sd.md#incident-response-time").
- **Security** – ECO uses Amazon GuardDuty to identify potentially unauthorized or malicious activity in your
  EDI environment. The ECO team monitors GuardDuty ﬁndings 24x7. ECO also supports Amazon Macie to protect your sensitive data, such as personally
  identiﬁable information (PII) and ﬁnancial data. ECO also monitors and triages all Amazon Route 53 Resolver ALERT and BLOCK events generated in EDI accounts
  to further inspect network traffic and augment its detective capabilities.
- **Backup management** – ECO uses backup management to take snapshots of your resources and data. ECO creates,
  monitors, and stores snapshots for AWS services that AWS Backup supports. The ECO team creates AWS Backup plans during EDI deployment and onboarding that deﬁne the
  backup schedules, frequency, and retention period. ECO tracks all backup jobs and alerts our team to run remediation when a backup job fails. If needed, ECO
  uses your snapshots to perform restoration actions during incidents. ECO provides you with a backup coverage report and a backup status report.
- **Problem management** – ECO performs trend analyses to identify and investigate problems.
  Problems are remediated either with a workaround or a permanent solution that prevents the recurrence of similar future service incidents. After the incident is
  resolved, you can request a post incident report (PIR). The PIR captures the root cause and actions taken, including preventative measures.
- **Designated experts** – ECO designates an EDI Solutions Delivery Manager (E-SDM) to partner with your organization
  and drive operational and security excellence. Your E-SDM provides you with guidance during and after conﬁguration and onboarding. The E-SDM is your point of
  contact for EDI operational needs and collaborates with your AWS account team to deliver a monthly report of your operational metrics.
- **Logging and reporting** – ECO aggregates and stores logs that are generated because of operations in Amazon CloudWatch, AWS CloudTrail,
  and Amazon Virtual Private Cloud (Amazon VPC) Flow Logs. Logging helps the ECO team more quickly resolve incidents and audit systems. Your designated E-SDM provides you with a monthly service
  report that summarizes key performance metrics of EDI. The service report includes an executive summary and insights, operational metrics, EDI API service level
  agreement (SLA) adherence, and spending and savings metrics.
- **Service request management** – Use the AWS Support Center Console to request information about your EDI instances.
  You can submit a service request for "How to" questions about EDI features or to request additional EDI support.
- **Application management** – ECO performs EDI deployment on your behalf, updates and upgrades
  your EDI instances, and supports EDI instance deletion and offboarding.
