# Remediating a potentially compromised ECS

cluster

A potentially compromised ECS cluster finding indicates suspicious or malicious activity has been detected within your Amazon ECS environment.
This could include unauthorized access, malware execution, or other malicious behavior that puts your container workloads at risk.

Follow these steps to remediate a potentially compromised Amazon ECS cluster:

1. **Identify the potentially compromised ECS cluster and the detected threat (findings)**

Impacted ECS cluster details are listed in the GuardDuty finding details panel. 2. **Evaluate the source of threat/malware**

Check for malware in container images. If malware is detected, review the container image being used.
Use [ListTasks](../../../AmazonECS/latest/APIReference/API_ListTasks.md "../../../AmazonECS/latest/APIReference/API_ListTasks.md")
to identify all other running tasks that use the same potentially compromised image. 3. **Isolate impacted tasks**

Stop the threat by blocking all network traffic (both incoming and outgoing) to the affected tasks.
This network isolation helps prevent any ongoing attacks by cutting off all connections to the compromised task.
**Note**: If you determine this finding was triggered by expected/legitimate activity in your environment,
you can set up a suppression rule to prevent similar findings from appearing. For additional information, see
[Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").
