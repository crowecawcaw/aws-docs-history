End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Monitoring SimSpace Weaver with Amazon CloudWatch

You can monitor SimSpace Weaver using Amazon CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The SimSpace Weaver service reports the following metrics
in the `AWS/simspaceweaver` namespace.

## SimSpace Weaver metrics at the account level

The SimSpace Weaver namespace includes the following metrics related to
activity at the AWS account level.

| Metric            | Description                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `SimulationCount` | The number of simulations for the current account.<br>Units: Count<br>Dimensions: none<br>Statistics: Average, Minimum, Maximum |
