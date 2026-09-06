# Schedule standby workers for a Deadline Cloud fleet with CloudFormation

The fleet\_standby\_scheduling CloudFormation template schedules
[standby
worker count](../userguide/auto-scaling-configuration.md "../userguide/auto-scaling-configuration.md") changes on a Deadline Cloud fleet based on a time schedule.
Standby workers are a warm pool of idle workers that can start processing
jobs immediately without waiting for new instances to launch. By scheduling
standby workers during business hours and not during off-hours, you reduce
job start latency when your team is active while avoiding the cost of idle
workers overnight and on weekends. For the template source, see
[fleet\_standby\_scheduling](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/fleet_standby_scheduling "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/fleet_standby_scheduling")
on the GitHub website.

The template works with any existing Deadline Cloud fleet, including
service-managed and customer-managed fleets. By default, it sets the
standby worker count to 2 at 8:00 AM UTC Monday through Friday and resets
it to 0 at 5:00 PM UTC.

The template creates the following resources:

- A Lambda function that calls the Deadline Cloud
  `UpdateFleet` API. The function reads the fleet's current
  configuration first to avoid overwriting other settings.
- IAM roles for the Lambda function and the EventBridge
  scheduler.
- Two EventBridge schedules that trigger the Lambda function at the
  start and end of business hours.
  To customize the schedule, update the
  `BusinessHoursStartCron`,
  `BusinessHoursEndCron`, and
  `ScheduleTimezone` parameters. To schedule multiple fleets,
  deploy one stack per fleet.
