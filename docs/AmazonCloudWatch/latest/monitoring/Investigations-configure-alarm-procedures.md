# Configure an alarm to

create investigations

After you have an investigation group set up in your account, you can configure
existing CloudWatch alarms to automatically create investigations when they enter the
ALARM state. This eliminates the need to manually start investigations and ensures
consistent response to operational issues. You can configure alarms using the AWS
Management Console, AWS CLI, CloudFormation, or AWS SDKs.

Console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**,
   and select an existing alarm.
3. Choose **Actions**,
   **Edit**.
4. In the **Alarm actions** section, choose
   **Add alarm action**.
5. Under the **Configure actions**,
   **Investigation action** section, choose
   the investigation group ARN.
6. (Optional) Add a deduplication string to group related
   alarms.
7. Choose **Update alarm**.

CLI
This command requires that you specify an ARN for the
`alarm-actions` parameter. For information about how to
create the ARN, see [ARN format and parameters](Investigations-configure-alarms.md#Investigations-arn-format "Investigations-configure-alarms.md#Investigations-arn-format").

###### To configure a CloudWatch alarm with InvestigationGroup action

(AWS CLI)

1. Install and configure the AWS CLI, if you haven't already. For
   information, see [Installing or updating the latest version of the
   AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Run the following command to collect information about the
   alarm that you want to configure.

```
aws cloudwatch describe-alarms --alarm-names "alarm name"
```

3. Run the following command to update an alarm. Replace each
   `example resource placeholder` with
   your own information.

```
aws cloudwatch put-metric-alarm --alarm-name name \
--alarm-description "description" \
--metric-name name --namespace namespace \
--statistic statistic --period value --threshold value \
--comparison-operator value \
--dimensions "dimensions" --evaluation-periods value \
--alarm-actions "arn:aws:aiops:region:{account-id}:investigation-group/{investigationGroupIdentifier}#DEDUPE_STRING={my-dedupe-string}"
```

Here's an example.

```
//Without deduplication string
aws cloudwatch put-metric-alarm --alarm-name cpu-mon \
--alarm-description "Alarm when CPU exceeds 70 percent" \
--metric-name CPUUtilization --namespace AWS/EC2 \
--statistic Average --period 300 --threshold 70 \
--comparison-operator GreaterThanThreshold \
--dimensions "Name=InstanceId,Value=i-12345678" --evaluation-periods 2 \
--alarm-actions arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ \
--unit Percent

//With deduplication string
aws cloudwatch put-metric-alarm --alarm-name cpu-mon \
--alarm-description "Alarm when CPU exceeds 70 percent" \
--metric-name CPUUtilization --namespace AWS/EC2 \
--statistic Average --period 300 --threshold 70 \
--comparison-operator GreaterThanThreshold \
--dimensions "Name=InstanceId,Value=i-12345678" --evaluation-periods 2 \
--alarm-actions arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ#DEDUPE_STRING=performance \
--unit Percent
```

CloudFormation
This section includes CloudFormation templates that you can use to configure
CloudWatch alarms to automatically create or update investigations. Each
template requires that you specify an ARN for the
`AlarmActions` parameter. For information about how to
create the ARN, see [ARN format and parameters](Investigations-configure-alarms.md#Investigations-arn-format "Investigations-configure-alarms.md#Investigations-arn-format").

```
//Without deduplication string
Resources:
  MyAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmActions:
        - !Sub "arn:aws:aiops:${AWS::Region}:${AWS::AccountId}:investigation-group/{investigationGroupIdentifier}"

//With deduplication string
Resources:
  MyAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmActions:
        - !Sub "arn:aws:aiops:${AWS::Region}:${AWS::AccountId}:investigation-group/{investigationGroupIdentifier}#DEDUPE_STRING={my-dedupe-string}"
```

SDK
This section includes Java code snippets that you can use to configure CloudWatch alarms to automatically create or update investigations. Each snippet requires that you specify an ARN for the `investigationGroupArn` parameter. For information about how to create the ARN, see [ARN format and parameters](Investigations-configure-alarms.md#Investigations-arn-format "Investigations-configure-alarms.md#Investigations-arn-format").

```
import com.amazonaws.services.cloudwatch.AmazonCloudWatch;
import com.amazonaws.services.cloudwatch.AmazonCloudWatchClientBuilder;
import com.amazonaws.services.cloudwatch.model.ComparisonOperator;
import com.amazonaws.services.cloudwatch.model.Dimension;
import com.amazonaws.services.cloudwatch.model.PutMetricAlarmRequest;
import com.amazonaws.services.cloudwatch.model.PutMetricAlarmResult;
import com.amazonaws.services.cloudwatch.model.StandardUnit;
import com.amazonaws.services.cloudwatch.model.Statistic;

//Without deduplication string
private void putMetricAlarmWithCloudWatchInvestigationAction() {
        final AmazonCloudWatch cloudWatchClient =
                AmazonCloudWatchClientBuilder.defaultClient();

        Dimension dimension = new Dimension()
                .withName("InstanceId")
                .withValue("i-12345678");
        String investigationGroupArn = "arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ";

        PutMetricAlarmRequest request = new PutMetricAlarmRequest()
                    .withAlarmName("cpu-mon")
                    .withComparisonOperator(
                        ComparisonOperator.GreaterThanThreshold)
                    .withEvaluationPeriods(2)
                    .withMetricName("CPUUtilization")
                    .withNamespace("AWS/EC2")
                    .withPeriod(300)
                    .withStatistic(Statistic.Average)
                    .withThreshold(70.0)
                    .withActionsEnabled(true)
                    .withAlarmDescription("Alarm when CPU exceeds 70 percent")
                    .withUnit(StandardUnit.Percent)
                    .withDimensions(dimension)
                    .withAlarmActions(investigationGroupArn);

        PutMetricAlarmResult response = cloudWatchClient.putMetricAlarm(request);
}

//With deduplication string
private void putMetricAlarmWithCloudWatchInvestigationActionWithDedupeString() {
        final AmazonCloudWatch cloudWatchClient =
                AmazonCloudWatchClientBuilder.defaultClient();

        Dimension dimension = new Dimension()
                .withName("InstanceId")
                .withValue("i-12345678");
        String investigationGroupArn = "arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ#DEDUPE_STRING=performance";

        PutMetricAlarmRequest request = new PutMetricAlarmRequest()
                    .withAlarmName("cpu-mon")
                    .withComparisonOperator(
                        ComparisonOperator.GreaterThanThreshold)
                    .withEvaluationPeriods(2)
                    .withMetricName("CPUUtilization")
                    .withNamespace("AWS/EC2")
                    .withPeriod(300)
                    .withStatistic(Statistic.Average)
                    .withThreshold(70.0)
                    .withActionsEnabled(true)
                    .withAlarmDescription("Alarm when CPU exceeds 70 percent")
                    .withUnit(StandardUnit.Percent)
                    .withDimensions(dimension)
                    .withAlarmActions(investigationGroupArn);

        PutMetricAlarmResult response = cloudWatchClient.putMetricAlarm(request);
}
```
