

# Create an alarm that uses a warm-up period
<a name="Create_WarmUp_Alarm"></a>

Create a metric alarm or log alarm with a warm-up period to delay evaluation after creation. For more information about warm-up periods, see [Alarm warm-up periods](alarm-warm-up.md).

Set the warm-up period with the `WarmUpConfiguration` parameter on the [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) API. Log alarms use the [PutLogAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutLogAlarm.html) API.

## Creating a warm-up alarm with the AWS CLI
<a name="warm-up-alarm-create-cli"></a>

The following examples create and manage alarms with warm-up periods.

**Example Create a metric alarm with a 30-minute warm-up period**  
This alarm uses default early-termination behavior: it ends warm-up and begins to evaluate as soon as enough data fills the evaluation window.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyServiceStartupAlarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --warm-up-configuration '{"WarmUpPeriodDurationInMinutes":30}'
```

**Example Wait the entire warm-up period before evaluating**  
Set `OnlyStartEvaluatingAfterWarmUpPeriodEnds` to `true` to prevent evaluation until the full warm-up duration elapses. The alarm waits the full 60 minutes before it evaluates, even if data arrives sooner.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyServiceStartupAlarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --warm-up-configuration '{"WarmUpPeriodDurationInMinutes":60,"OnlyStartEvaluatingAfterWarmUpPeriodEnds":true}'
```

**Example Change the warm-up period while the alarm is warming up**  
You can update the warm-up configuration while the alarm is still in its warm-up period. This example sets the warm-up duration to 45 minutes.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyServiceStartupAlarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --warm-up-configuration '{"WarmUpPeriodDurationInMinutes":45}'
```
After the warm-up period ends, you can update the warm-up configuration. However, the update does not start a new warm-up period. The alarm continues to evaluate normally.

## View the warm-up configuration
<a name="warm-up-alarm-view"></a>

Use the [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) API to retrieve an alarm's warm-up configuration.

```
aws cloudwatch describe-alarms \
  --alarm-names MyServiceStartupAlarm
```

During warm-up, the alarm state remains `INSUFFICIENT_DATA` and the evaluation state is `IN_WARM_UP`.