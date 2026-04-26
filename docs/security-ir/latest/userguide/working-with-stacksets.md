# Working with CloudFormation StackSets

For specific instructions on how to create a StackSet with service-managed permissions, see [Create CloudFormation StackSets with service-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md") in the _AWS CloudFormation User Guide_.

AWS Security Incident Response provides two CloudFormation templates. Both templates create the same two AWS Identity and Access Management roles, `AWSSecurityIncidentResponseContainment` and `AWSSecurityIncidentResponseContainmentExecution`. The **Containment with EC2 Triage** template adds the `AWSSecurityIncidentResponseInvestigationPolicy` to the `AWSSecurityIncidentResponseContainment` role, which grants additional permissions for EC2 Triage. Choose the template that matches your security requirements:

- [Containment only](containment-only-template.md "containment-only-template.md"): Creates the minimum required permissions for containment actions.
- [Containment with EC2 Triage](containment-with-ec2-triage-template.md "containment-with-ec2-triage-template.md"): Includes all containment permissions plus additional permissions for EC2 Triage. This template enables AWS Security Incident Response to execute AWS Systems Manager Run Command on your Amazon Elastic Compute Cloud instances during security investigations.
  For more information about EC2 Triage, see [Detect and Analyze](detect-and-analyze.md "detect-and-analyze.md").
