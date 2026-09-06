

# Stop conditions for AWS FIS
<a name="stop-conditions"></a>

AWS Fault Injection Service (AWS FIS) provides controls and guardrails for you to run experiments safely on AWS workloads. A *stop condition* is a mechanism to stop an experiment if it reaches a threshold that you define as an Amazon CloudWatch alarm. If a stop condition is triggered during an experiment, AWS FIS stops the experiment. You cannot resume a stopped experiment.

To create a stop condition, first define the steady state for your application or service. The steady state is when your application is performing optimally, defined in terms of business or technical metrics. For example, latency, CPU load, or number of retries. You can use the steady state to create a CloudWatch alarm that you can use to stop an experiment if your application or service reaches a state where its performance is not acceptable. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

Your account has a quota on the number of stop conditions that you can specify in an experiment template. For more information, see [Quotas and limitations for AWS Fault Injection Service](fis-quotas.md).

## Stop condition syntax
<a name="stop-condition-syntax"></a>

When you create an experiment template, you specify one or more stop conditions by specifying the CloudWatch alarms that you created.

```
{
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:{{region}}:{{123456789012}}:alarm:{{alarm-name}}"
        }
    ]
}
```

The following example indicates that the experiment template does not specify a stop condition.

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
<a name="stop-condition-learn-more"></a>

For a tutorial that demonstrates how to create a CloudWatch alarm and add a stop condition to an experiment template, see [Run CPU stress on an instance](fis-tutorial-run-cpu-stress.md).

For more information about the CloudWatch metrics that are available for the resource types supported by AWS FIS, see the following:
+ [Monitor your instances using CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html)
+ [Amazon ECS CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)
+ [Monitoring Amazon RDS metrics using CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html)
+ [Monitoring Run Command metrics using CloudWatch](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudwatch-metrics.html)