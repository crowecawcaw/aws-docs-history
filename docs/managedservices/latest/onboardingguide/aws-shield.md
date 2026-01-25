# Use AMS SSP to provision AWS Shield Advanced in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Shield Advanced capabilities directly in your AMS managed account. AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service that safeguards
applications running on AWS. Shield Advanced provides always-on detection and automatic inline mitigations
that minimize application downtime and latency, so there is no need to engage AWS Support to benefit
from DDoS protection. There are two tiers of AWS Shield - Standard and Advanced; AMS offers Shield Advanced.
To learn more, see [Shield Advanced](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/").

All AWS customers benefit from the automatic protections of AWS Shield Standard, at no
additional charge. AWS Shield Standard defends against most common, frequently occurring,
network and transport layer DDoS attacks that target your website or applications. When
you use AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive
comprehensive availability protection against all known infrastructure (Layer 3 and 4)
attacks.

For higher levels of protection against attacks targeting your applications running on
Amazon Elastic Compute Cloud (Amazon EC2), Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 resources, you can subscribe to
AWS Shield Advanced.

In addition to the network and transport layer protections that come with
AWS Shield Standard, AWS Shield Advanced provides additional detection and mitigation against large
and sophisticated DDoS attacks, near real-time visibility into attacks, and integration
with AWS WAF, a web application firewall. AWS Shield Advanced also gives you 24x7 access to the
AWS Shield Response Team (SRT) and protection against DDoS related spikes in your Amazon Elastic Compute Cloud (Amazon EC2), Elastic Load Balancing (Elastic Load Balancing),
Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 charges.

## Shield Advanced in AWS Managed Services FAQ

**Q: How do I request access to Shield Advanced in my AMS account?**

Request access to Shield Advanced by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account: `customer_shield_role`
and `aws_drt_shield_role`. Once provisioned in your account, you must onboard
the roles in your federation solution.

After the roles are deployed into your account, you can use the `customer_shield_role`
to confirm your subscription to AWS Shield Advanced in your account.

###### Note

Note that there is a monthly fee and a one-year commitment associated with the use of
AWS Shield Advanced. Additionally, using AWS Shield Advanced in AMS authorizes
AMS to escalate to the AWS Shield (SRT), who may make
changes to your web application firewall (AWS WAF) rules during escalated
distributed denial of service (DDoS) incidents. These changes will be
made in coordination with AMS.

**Q: What are the restrictions to using Shield Advanced in my AMS account?**

Although not a restriction, you should understand that using Shield Advanced deploys the
`aws_drt_shield_role`, which allows AWS Shield teams (SRT)
to make emergency changes to AWS WAF rules inside of AMS accounts during escalated DDoS
incidents. This is recommended by AMS for the fastest remediation of DDoS attacks,
and would occur after an AMS escalation to the SRT.

**Q: What are the prerequisites or dependencies to using Shield Advanced in my AMS account?**

There are no prerequisites or dependencies to use Shield Advanced in your AMS account.
