

# DRHCSEC04-BP02 Grant least privilege access with a strong focus on actions that enable the storage of data
<a name="drhcsec04-bp02"></a>

 Restricting access to actions which store data should be a strong focus of least privilege access analysis. 

 **Desired outcome:** Principals are only allowed to perform actions that are required within that specific account. 

 **Common anti-patterns:** 

1.  Implementing policies that deny specific services but allow all other services, as the policies would need to be maintained whenever new services are released. 

1.  Attaching the `AWSPowerUser` or `AdministratorAccess` AWS-managed policy to roles. 

1.  Allowing actions that store or move data when these actions are not required. 

 Benefits of establishing this best practice: Least privilege minimizes options to store data, which reduces the risk of noncompliant storage locations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-22"></a>
+  While allowing access only to required services is part of [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html), it is even more important in data residency scenarios, as there are many services that store data in Regions. 
+  Grant the `ec2:CreateSubnet` action only to principals that have complete knowledge of the data residency requirements, and set expectations to only create subnets in locations where instances are expected to be aligned with data residency requirements. There are two reasons for this: instances can't exist in locations without subnets, and the location of attached EBS volumes is controlled by the location of the instances. Where possible, add conditions to the granted permissions to allow creation of resources only in Regions aligned with data residency requirements. 
+  Deny `ram:AcceptResourceShareInvitation`, `ram:AssociateResourceShare*`, `ram:Create*`, and `ram:Update*` when not required, as performing these actions combined with other actions where the resource element is `*` enables storage to resources that may be in unapproved locations. 
+  Deny `ec2:ExportImage`, `ec2:ImportImage`, `ec2:ImportInstance`, and `ec2:CreateTrafficMirror*` unless you have an approved use case that requires these actions. 
+  Implement permission guardrails for which include each of the applicable restrictions defined in this best practice. 

## Resources
<a name="resources-8"></a>

 **Related best practices:** 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html) 

 [Detection](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-detective-controls.html) 