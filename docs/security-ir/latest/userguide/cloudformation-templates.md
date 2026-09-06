

# Select a CloudFormation template for your containment roles
<a name="cloudformation-templates"></a>

AWS Security Incident Response provides two AWS CloudFormation templates. Both templates create the same two AWS Identity and Access Management roles: `AWSSecurityIncidentResponseContainment` and `AWSSecurityIncidentResponseContainmentExecution`. The **Containment with EC2 Triage** template adds the `AWSSecurityIncidentResponseInvestigationPolicy` to the `AWSSecurityIncidentResponseContainment` role, which grants additional permissions for EC2 Triage. Choose the template that matches your security requirements:
+ [Containment only](containment-only-template.md): Creates the minimum required permissions for containment actions.
+ [Containment with EC2 Triage](containment-with-ec2-triage-template.md): Includes all containment permissions plus additional permissions for EC2 Triage. This template enables AWS Security Incident Response to execute AWS Systems Manager Run Command on your Amazon Elastic Compute Cloud instances during security investigations.