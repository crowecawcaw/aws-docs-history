

# Uninstalling security agent for ECS-EC2 Bottlerocket resources
<a name="uninstalling-gdu-bottlerocket-agent-runtime-monitoring"></a>

Perform the following steps to uninstall the GuardDuty security agent from your Bottlerocket ECS-EC2 instances.

**To uninstall the GuardDuty security agent**

1. To uninstall the GuardDuty security agent, use [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) (in the *AWS Systems Manager User Guide*) and set the action parameter to **Uninstall**.

   In the **Targets** section, make sure that the impact is only on those Bottlerocket instances from which you want to uninstall the security agent.

   Use the following GuardDuty document and distributor:
   + Document name: `AmazonGuardDuty-ConfigureRuntimeMonitoringSsmPlugin`.
   + Distributor: `AmazonGuardDuty-RuntimeMonitoringSsmPlugin`.

1. After you provide all the details and choose **Run**, GuardDuty removes the security agent from the targeted Bottlerocket instances.

1. To also delete the VPC endpoint associated with this security agent, see [To delete a VPC endpoint](clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint).