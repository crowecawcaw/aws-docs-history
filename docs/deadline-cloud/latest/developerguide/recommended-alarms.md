# Recommended alarms

With CloudWatch, you can create alarms that watch metrics and send you a
notification or perform another action when a threshold is breached.
For more information on configuring CloudWatch alarms, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

We recommend that you set alarms for the following Deadline Cloud metrics:

**LicensesInUse**

**Dimensions:**
FleetId, LicenseEndpointId

**Alarm description:** This alarm detects when
the active license sessions for a service-managed fleet or license endpoint are
approaching your account quota.
If this occurs, you can raise the account quota for license sessions.
See your current quotas and request increases using Service Quotas.
To learn more, see the [Service Quotas User Guide](../../../servicequotas/latest/userguide.md "../../../servicequotas/latest/userguide.md").

**Intent:** Prevent license checkout failures
by monitoring usage before it reaches the quota limit.

**Statistic:** Maximum

**Recommended threshold:**
90% of your license session quota

**Threshold justification:**
Set the threshold to a percentage of your quota, so that you can take action before
it reaches the limit.

**Period:** 1 minute

**Datapoints to alarm:** 1

**Evaluation periods:** 1

**Comparison Operator:**
`GREATER_THAN_THRESHOLD`

## Additional resources

- [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md")
- [Service Quotas User Guide](../../../servicequotas/latest/userguide.md "../../../servicequotas/latest/userguide.md")
