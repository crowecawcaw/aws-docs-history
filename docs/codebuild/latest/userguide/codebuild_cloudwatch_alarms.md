# CodeBuild CloudWatch alarms

You can use the CloudWatch console to create alarms based on CodeBuild metrics so you can react
if something goes wrong with your builds. The two metrics that are most useful with
alarms are described in the following bullets. For more information about using CloudWatch
with CodeBuild, see [Monitor CodeBuild builds with CloudWatch](monitoring-builds.md "monitoring-builds.md").

- `FailedBuild`. You can create an alarm that is triggered when a
  certain number of failed builds are detected within a predetermined number of
  seconds. In CloudWatch, you specify the number of seconds and how many failed builds
  trigger an alarm.
- `Duration`. You can create an alarm that is triggered when a build
  takes longer than expected. You specify how many seconds must elapse after a
  build is started and before a build is completed before the alarm is triggered.
  For information about how to create alarms for CodeBuild metrics, see [Monitor CodeBuild builds with CloudWatch alarms](monitoring-alarms.md "monitoring-alarms.md"). For more
  information about alarms, see [Creating Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
