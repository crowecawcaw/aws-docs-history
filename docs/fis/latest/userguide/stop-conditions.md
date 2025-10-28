# Stop conditions for AWS FIS

AWS Fault Injection Service (AWS FIS) provides controls and guardrails for you to run experiments safely on
AWS workloads. A _stop condition_ is a mechanism to stop an experiment
if it reaches a threshold that you define as an Amazon CloudWatch alarm. If a stop condition is
triggered during an experiment, AWS FIS stops the experiment. You cannot resume a stopped
experiment.

To create a stop condition, first define the steady state for your application or service.
The steady state is when your application is performing optimally, defined in terms of
business or technical metrics. For example, latency, CPU load, or number of retries. You can
use the steady state to create a CloudWatch alarm that you can use to stop an experiment if your
application or service reaches a state where its performance is not acceptable. For more
information, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
in the _Amazon CloudWatch User Guide_.

Your account has a quota on the number of stop conditions that you can specify in an
experiment template. For more information, see [Quotas and limitations for AWS Fault Injection Service](fis-quotas.md "fis-quotas.md").

## Stop condition syntax

When you create an experiment template, you specify one or more stop conditions by
specifying the CloudWatch alarms that you created.

```
{
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:`region`:`123456789012`:alarm:`alarm-name`"
        }
    ]
}
```

The following example indicates that the experiment template does not specify a stop
condition.

```
{
    "stopConditions": [
        {
            "source": "none"
        }
    ]
}
```

## Learn more

For a tutorial that demonstrates how to create a CloudWatch alarm and add a stop condition
to an experiment template, see [Run CPU stress on an
instance](fis-tutorial-run-cpu-stress.md "fis-tutorial-run-cpu-stress.md").

For more information about the CloudWatch metrics that are available for the resource types
supported by AWS FIS, see the following:

- [Monitor your instances using CloudWatch](../../../AWSEC2/latest/UserGuide/using-cloudwatch.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch.md")
- [Amazon ECS CloudWatch metrics](../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md "../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md")
- [Monitoring Amazon RDS metrics using CloudWatch](../../../AmazonRDS/latest/UserGuide/monitoring-cloudwatch.md "../../../AmazonRDS/latest/UserGuide/monitoring-cloudwatch.md")
- [Monitoring Run Command metrics using CloudWatch](../../../systems-manager/latest/userguide/monitoring-cloudwatch-metrics.md "../../../systems-manager/latest/userguide/monitoring-cloudwatch-metrics.md")
