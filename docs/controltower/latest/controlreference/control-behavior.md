# Control behavior and guidance

Controls are categorized according to their _behavior_ and their _guidance_.

The _behavior_ of each control is one of preventive, detective, or proactive. Control _guidance_ refers to the recommended practice for how to apply each control to your OUs. The guidance of a control is independent of whether its behavior is preventive, detective, or proactive.

###### Control behavior

- **Preventive** – A preventive control ensures that your accounts maintain compliance, because it disallows actions that lead to policy violations. The status of a preventive control is either **enforced** or **not enabled**. Preventive controls are supported in all AWS Regions.
- **Detective** – A detective control detects noncompliance of resources within your accounts, such as policy violations, and provides alerts through the dashboard. The status of a detective control is either **clear**, **in violation**, or **not enabled**. Detective controls apply only in those AWS Regions supported by AWS Control Tower.
- **Proactive** – A proactive control scans your resources before they are provisioned, and makes sure that the resources are compliant with that control. Resources that are not compliant will not be provisioned. Proactive controls are implemented by means of AWS CloudFormation hooks, and they apply to resources that would be provisioned by AWS CloudFormation. The status of a proactive control is PASS, FAIL, or SKIP. For more information about AWS CloudFormation hooks, see [Characteristics of hooks](../../../cloudformation-cli/latest/userguide/hooks.md#hooks-characteristics "../../../cloudformation-cli/latest/userguide/hooks.md#hooks-characteristics") in the AWS CloudFormation documentation.
  **Implementation of control behavior**

- The preventive controls are implemented using Service Control Policies (SCPs), Resource Control Policies (RCPs), and declarative policies, which are part of AWS Organizations.
- The detective controls are implemented using AWS Config rules.
- The proactive controls are implemented using AWS CloudFormation hooks.
- Certain mandatory controls are implemented by means of a single SCP that performs multiple actions, rather than as unique SCPs. Therefore, the same SCP is shown in the control reference, under each mandatory control to which that SCP applies.
- The integrated, detective Security Hub controls are implemented using AWS Config rules, similarly to all Security Hub controls. These controls are owned by the **Service-Managed Standard: AWS Control Tower**, which is part of Security Hub.
- The integrated AWS Config controls that are available in the control catalog are owned by AWS Config and implemented as Config rules, exactly as any other AWS Config controls.
  **Control guidance**

AWS Control Tower provides three categories of guidance: _mandatory_, _strongly recommended_, and _elective_ controls.

- Mandatory controls are enforced in your landing zone depending on what you may have enabled in your environment. These controls protect AWS Control Tower-deployed resources.
- Strongly recommended controls are designed to enforce some common best practices for well-architected, multi-account environments. These controls apply at the OU level, for all accounts in that OU.
- Elective controls enable you to track or lock down actions that are commonly restricted in an AWS enterprise environment. These controls apply at the OU level, for all accounts in that OU.
  **Starting with AWS Control Tower Landing Zone version 4.0, mandatory controls are no longer applied by default.**
