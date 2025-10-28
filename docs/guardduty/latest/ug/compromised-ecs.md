# Remediating a potentially compromised ECS

cluster

When GuardDuty generates [finding
types that indicate potentially compromised Amazon ECS resources](guardduty_finding-types-active.md#findings-table "guardduty_finding-types-active.md#findings-table"), then your
**Resource** will be **ECSCluster**. Potential finding types
could be [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md") or
[Malware Protection for EC2 finding types](findings-malware-protection.md "findings-malware-protection.md").
If the behavior that caused the finding was
expected in your environment, then consider using [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

Follow these recommended steps to remediate a potentially compromised Amazon ECS cluster in
your AWS environment:

1. **Identify the potentially compromised ECS
   cluster.**

The GuardDuty Malware Protection for EC2 finding for ECS provides the **ECS cluster
details** in the finding's details panel. 2. **Evaluate the source of malware**

Evaluate if the detected malware was in the container's image. If malware was
in the image, identify all other tasks which are running using this image. For
information about running tasks, see [ListTasks](../../../AmazonECS/latest/APIReference/API_ListTasks.md "../../../AmazonECS/latest/APIReference/API_ListTasks.md"). 3. **Isolate the potentially impacted tasks**

Isolate the impacted tasks by denying all ingress and egress traffic to the
task. A deny all traffic rule may help you stop an attack that is already
underway, by severing all the connections to the task.
If the access was authorized, you can ignore the finding. The [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/")
console allows you to set up rules to entirely suppress individual findings so that they
no longer appear. For more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").
