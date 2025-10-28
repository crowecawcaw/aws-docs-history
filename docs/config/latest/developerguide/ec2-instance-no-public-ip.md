# ec2-instance-no-public-ip

Checks if EC2 instances have a public IP association. The rule is NON_COMPLIANT if the publicIp field is present in the EC2 instance configuration item. The rule applies only to IPv4.

**Context**: Public IP addresses can make EC2 instances directly accessible from the internet,
which might not always be desirable from a security or compliance standpoint:

- **Security**: In many cases, you might not want your EC2 instances to have public IP addresses unless they need to be publicly accessible.
  Having a public IP address can expose your EC2 instance to potential security risks, such as unauthorized access or attacks.
- **Compliance**: Various compliance standards such as PCI, DSS, or HIPAA
  have specific requirements regarding network segmentation and access controls. Ensuring that EC2 instances do not have unnecessary public
  IP addresses can help ensure compliance with these requirements.
- **Cost Management**: Public IP addresses can incur additional costs, especially if there are EC2 instances continuously associated with them.
  By identifying EC2 instances with public IPs which do not need them, you can potentially reduce costs.
  **Identifier:** EC2_INSTANCE_NO_PUBLIC_IP

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
