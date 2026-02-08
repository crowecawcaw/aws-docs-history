# Plan ahead with Amazon Connect quotas

Learn how to plan for and manage service quotas during key phases of your contact
center lifecycle.

## Planning for production

launch

Before launching your Amazon Connect contact center, request service quota increases to
ensure sufficient capacity for your agents and concurrent calls. Follow these best
practices:

1. **Include quotas in your migration plan**.
   - Address service quotas during the project design phase.
   - Submit quota increase requests well before final migration
     stages.

2. **Size your production workloads**.
   - Prepare the following data to support your quota requests:
     - Current number of agents
     - Call volume metrics
     - Average call duration

   - Be ready to provide additional metrics as needed so we can process
     your request.

###### Note

The data we ask for is based on the service quota. It is needed to
correctly size the quotas you require.

## Ongoing operations

management

Monitor your contact center's quota utilization by using Amazon CloudWatch. For detailed
metrics, see [Amazon Connect metrics sent to CloudWatch](monitoring-cloudwatch.md#connect-metrics-cloudwatch "monitoring-cloudwatch.md#connect-metrics-cloudwatch").

**Best practice**: Set CloudWatch alarms to monitor service
quota usage:

- Configure alerts at 80% of quota limits.
- Request quota increases when usage consistently exceeds this
  threshold.

## Managing emergency events

If you need urgent support during an emergency:

- Open a high-severity support case through the AWS Support
  Center:
  - Business Support plan: Select **Production system
    down** (1-hour response).
  - Enterprise On-Ramp or Enterprise Support plan: Select
    **Business-critical system down**.
    - Enterprise Support: 15-minute response
    - Enterprise On-Ramp: 30-minute response

- Contact your account team (such as your AWS Technical
  Account Manager and Solutions Architect) to ask for assistance.

During high-volume events, implement these queue management practices:

- Use the [Get metrics](get-queue-metrics.md "get-queue-metrics.md") flow block to communicate wait
  times to your customers.
- Enable [queued callbacks](setup-queued-cb.md "setup-queued-cb.md").
- Balance operational best practices with service quota constraints.

For more information, see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case").
