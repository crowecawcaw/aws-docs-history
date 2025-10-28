# Using AMS Resource Scheduler

To configure AMS Resource Scheduler after the solution is deployed, use the automated Resource Scheduler CTs to create, delete, update, and describe
(get details on) AMS Resource Scheduler periods (the times when Resource Scheduler runs) and schedules (the configured periods and other options).
For an example of using the AMS Resource Scheduler change types, see
[AMS Resource Scheduler](../ctref/management-ams-resource-scheduler-section.md "../ctref/management-ams-resource-scheduler-section.md").

To select resources to be managed by AMS Resource Scheduler, following deployment and schedule creation, you use the AMS Tag Create CTs to
tag Auto Scaling groups, Amazon RDS stacks, and Amazon EC2 resources with that tag key you provided during deployment, and the defined schedule as the
tag value. After the resources are tagged, the resources are scheduled for start or stop per your defined Resource Scheduler schedule.

There is no additional cost to using AMS Resource Scheduler. However the solution makes use of several AWS services and you're charged for
these resources as they are used. For more details, see
[Architecture overview](../../../solutions/latest/instance-scheduler-on-aws/architecture-overview.md "../../../solutions/latest/instance-scheduler-on-aws/architecture-overview.md").

To opt out of AMS Resource Scheduler:

- For temporary opt-out or disabling: Submit an RFC using the automated Management | AMS Resource Scheduler | State | Disable change type (ct-14v49adibs4db)
- For permanent removal: Submit a Management | Other | Other | Update (review required) (ct-0xdawir96cy7k) RFC requesting removal from the Resource Scheduler release automation system
