# EDI Cloud Operations terminology

ECO uses the following general terms:

- Managed environment or EDI environment: The AWS accounts where EDI on AWS is deployed (only EDI resources).
- Billing start date: The next business day after AWS receives the information that's requested in your EDI onboarding email. The EDI
  onboarding email is the email that AWS sends to you to collect the necessary information to activate EDI.
- Service termination: The process of cancelling EDI on AWS, which permanently removes all EDI-related services, OSDU® instances,
  and associated data from your account. This action is irreversible but doesn't affect account ownership.
- Event: A change in your EDI environment.
- Alert: When an event from a supported AWS service within your EDI environment exceeds a threshold and triggers an alarm, an alert
  is created. A notice is then sent to the ECO team, and an incident is added to your incident list.
- Incident: An unplanned interruption or performance degradation that affects your EDI environment and is reported by ECO or you.
- Problem: A shared underlying root cause of one or more incidents.
- Incident resolution:
  - ECO has restored all unavailable EDI services or resources that pertain to the incident to an available state.
  - Or ECO has determined that they can't restore unavailable stacks or resources to an available state.

- Incident response time: The difference in time between when you create an incident, and when ECO provides an initial response through
  the console, email, Support Center, or telephone.
- Incident resolution time: The difference in time between when either ECO or you create an incident and when the incident is resolved.
- Incident priority: How you or ECO prioritizes incidents as either Low, Medium, or High. For definitions, see
  [Incident priority](incident-mgmt.md#incident-mgmt-priority "incident-mgmt.md#incident-mgmt-priority").

ECO might recategorize incidents in accordance with the guidelines.

- Infrastructure restore: When an incident resolution isn't possible, ECO initiates a data restore based on the last known restore point,
  unless you specify otherwise.
- CSAT: EDI customer satisfaction (CSAT) is based on deep analytics that include quarterly surveys, Case Correspondence Ratings (CCR) on every
  case, and case correspondence when given.
- ITIL: Information Technology Infrastructure Library (ITIL) is an IT service management (ITSM) framework that's designed to standardize the lifecycle
  of IT services. ITIL is arranged in ﬁve stages of the IT service lifecycle: service strategy, service design, service transition, service operation, and
  service improvement.
- ITSM: A set of practices that align IT services with the needs of your business.
- MMS: Managed Monitoring Services (MMS) is a monitoring system that ECO operates that consumes AWS Health events and aggregates data from CloudWatch
  and other AWS services. Then, MMS uses an Amazon Simple Notification Service (Amazon SNS) topic to notify ECO operators (online 24x7) of alarms.
  ECO uses the following infrastructure terms:

- Managed production environment: The account where your production applications are.
- Managed non-production environment: The account that contains only non-production applications, such as applications for development
  and testing.
- EDI stack: A group of AWS resources that ECO manages as a single unit.
- SLAs: The service-level agreement (SLA) defines the level of service you can expect from EDI.
  ECO uses the following security terms:

- Detective controls: A library of EDI-created or enabled monitors that provides ongoing oversight of your EDI environment that
  doesn't align with security, operational, or customer controls. Detective controls notify owners and proactively modify or terminate resources.
- Service request: A request by you for an action that you want ECO to take on your behalf.
- Alert notiﬁcation: A notice that ECO posts to your service requests list page when an EDI alert is initiated.
