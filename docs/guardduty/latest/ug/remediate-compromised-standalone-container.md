# Remediating a potentially

compromised standalone container

When GuardDuty generates [finding
types that indicate potentially compromised container](guardduty_finding-types-active.md#findings-table "guardduty_finding-types-active.md#findings-table"), your
**Resource type** will be **Container**.
If the behavior that caused the finding was
expected in your environment, then consider using [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

To remediate potentially compromised credentials in
your AWS environment, perform the following steps:

1. **Isolate the potentially compromised
   container**

The following steps will help you identify the potentially malicious
container workload:

    * Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
    * On the **Findings** page, choose the corresponding
     finding to view the findings panel.
    * In the findings panel, under the **Resource
     affected** section, you can view the container's
     **ID** and **Name**.

Isolate this container from other container workloads. 2. **Pause the container**

Suspend all the processes in your container.

For information about freezing your container, see
[Pause a container](https://docs.docker.com/engine/api/v1.35/#tag/Container/operation/ContainerPause "https://docs.docker.com/engine/api/v1.35/#tag/Container/operation/ContainerPause").

**Stop the container**.

If the step above fails, and the container doesn't pause, stop the container
from running. If you've enabled the [Snapshots retention](malware-protection-customizations.md#mp-snapshots-retention "malware-protection-customizations.md#mp-snapshots-retention") feature, GuardDuty will retain the
snapshots of your EBS volumes that contain malware.

For information about stopping the container, see
[Stop a container](https://docs.docker.com/engine/api/v1.35/#tag/Container "https://docs.docker.com/engine/api/v1.35/#tag/Container"). 3. **Evaluate the presence of malware**

Evaluate if malware was in the container's image.
If the access was authorized, you can ignore the finding. The [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/")
console allows you to set up rules to entirely suppress individual findings so that they
no longer appear. The GuardDuty console allows you to set up rules to entirely suppress
individual findings so that they no longer appear. For more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").
