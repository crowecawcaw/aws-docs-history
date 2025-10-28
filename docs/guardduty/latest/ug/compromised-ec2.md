# Remediating a potentially compromised Amazon EC2

instance

When GuardDuty generates [finding
types that indicate potentially compromised Amazon EC2 resources](guardduty_finding-types-active.md#findings-table "guardduty_finding-types-active.md#findings-table"), then your
**Resource** will be **Instance**. Potential finding types
could be [EC2 finding types](guardduty_finding-types-ec2.md "guardduty_finding-types-ec2.md"), [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md"), or
[Malware Protection for EC2 finding types](findings-malware-protection.md "findings-malware-protection.md").
If the behavior that caused the finding was
expected in your environment, then consider using [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

Perform the following steps to remediate the potentially compromised Amazon EC2
instance:

1. **Identify the potentially compromised Amazon EC2
   instance**

Investigate the potentially compromised instance for malware and remove any
discovered malware. You may use [On-demand malware scan in GuardDuty](on-demand-malware-scan.md "on-demand-malware-scan.md") to identify malware in the
potentially compromised EC2 instance, or check [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") to see if there are
helpful partner products to identify and remove malware. 2. **Isolate the potentially compromised Amazon EC2
instance**

If possible, use the following steps to isolate the potentially compromised
instance:

    1. Create a dedicated **Isolation** security group. An
     isolation security group should only have inbound and outbound access
     from specific IP addresses. Make sure that there is no inbound or
     outbound rule that allows traffic for `0.0.0.0/0
     (0-65535)`.
    2. Associate the **Isolation** security group with this
     instance.
    3. Remove all security group associations other than the newly created
     **Isolation** security group from the potentially
     compromised instance.


    ###### Note

    The existing tracked connections won't be terminated as a
     result of changing security groups - only future traffic will be
     effectively blocked by the new security group.

    For information
     about blocking further traffic from suspicious
     existing connections, see [Enforce NACLs based on network IoCs to prevent further
     traffic](https://github.com/aws-samples/aws-customer-playbook-framework/blob/main/docs/Ransom_Response_EC2_Linux.md#enforce-nacls-based-on-network-iocs-to-prevent-further-traffic "https://github.com/aws-samples/aws-customer-playbook-framework/blob/main/docs/Ransom_Response_EC2_Linux.md#enforce-nacls-based-on-network-iocs-to-prevent-further-traffic") in the *Incident Response
     Playbook*.

3. **Identify the source of the suspicious
   activity**

If malware is detected, then based on the finding type in your account,
identify and stop the potentially unauthorized activity on your EC2 instance.
This may require actions such as closing any open ports, changing access
policies, and upgrading applications to correct vulnerabilities.

If you are unable to identify and stop unauthorized activity on your
potentially compromised EC2 instance, we recommend that you terminate the
compromised EC2 instance and replace it with a new instance as needed. The
following are additional resources for securing your EC2 instances:

    * Security and Networking sections in [Best practices
     for Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")
    * [Amazon EC2
     security groups for Linux instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md").
    * [Security in
     Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md")
    * [Tips for
     securing your EC2 instances (Linux)](https://aws.amazon.com/articles/tips-for-securing-your-ec2-instance/ "https://aws.amazon.com/articles/tips-for-securing-your-ec2-instance/").
    * [AWS security best practices](https://aws.amazon.com//architecture/security-identity-compliance/ "https://aws.amazon.com//architecture/security-identity-compliance/")
    * [AWS Security Incident Response Technical Guide](../../../security-ir/latest/userguide/security-incident-response-guide.md "../../../security-ir/latest/userguide/security-incident-response-guide.md").

4. **Browse AWS re:Post**

Browse [AWS re:Post](https://repost.aws/ "https://repost.aws/") for further
assistance. 5. **Submit a technical support request**

If you are a premium support package subscriber, you can submit a [technical support](https://console.aws.amazon.com/support/home#/case/create?issueType=technical "https://console.aws.amazon.com/support/home#/case/create?issueType=technical") request.
