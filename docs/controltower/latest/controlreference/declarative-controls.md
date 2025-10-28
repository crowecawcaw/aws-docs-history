# Controls implemented with declarative policies

This section provides information about AWS Control Tower controls that are implemented by _declarative policies_ from AWS Organizations. These are _preventive_ controls. For more information about how declarative policies work as preventive controls in AWS Control Tower, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the AWS Organizations documentation.

Declarative policies help you deﬁne and enforce your required conﬁguration for specified AWS services, across your entire organization, at the OU level. When a declarative policy is applied, the conﬁguration is maintained continuously.

Declarative policies are enforced in each AWS service's control plane, which is an important distinction from controls implemented by service control policies (SCPs). While SCPs regulate access to APIs, declarative policies are applied directly at the service level. This approach ensures that the speciﬁed conﬁguration is enforced, even when new features or APIs are introduced by the service.

**Available controls**

###### Topics

- [[CT.EC2.PV.7] Disallow all public sharing of Amazon EBS snapshots](ct-ec2-pv-7.md "ct-ec2-pv-7.md")
- [[CT.EC2.PV.8] Disallow inbound and outbound internet connections to your VPCs through an internet gateway (IGW) or egress-only internet gateway (EIGW)](ct-ec2-pv-8.md "ct-ec2-pv-8.md")
- [[CT.EC2.PV.9] Disallow access to the EC2 serial console for all EC2 instances](ct-ec2-pv-9.md "ct-ec2-pv-9.md")
- [[CT.EC2.PV.11] Disallow public sharing of Amazon Machine Images (AMIs)](ct-ec2-pv-11.md "ct-ec2-pv-11.md")
