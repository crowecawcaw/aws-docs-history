# Definitions

The following are operational excellence-specific definitions that
complement this lens' general definitions.

- **Preventative controls**: These
  [controls](../../../prescriptive-guidance/latest/aws-security-controls/preventative-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/preventative-controls.md")
  are designed to block an event from occurring. For example,
  [this
  service control policy (SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_ec2.md#example-ec2-1 "../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_ec2.md#example-ec2-1") denies launch of an EC2
  instance type unless they are of type t2.micro.
- **Proactive controls**: These
  [controls](../../../prescriptive-guidance/latest/aws-security-controls/proactive-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/proactive-controls.md")
  are designed to block the creation of noncompliant resources.
  For example,
  [this
  AWS CloudFormation Guard rule](https://github.com/aws-cloudformation/aws-guard-rules-registry/blob/main/rules/aws/amazon_ec2/restricted_ssh.guard "https://github.com/aws-cloudformation/aws-guard-rules-registry/blob/main/rules/aws/amazon_ec2/restricted_ssh.guard") blocks an EC2 instance from
  being deployed if its security group allows SSH ingress.
- **Detective controls**: These
  [controls](../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/detective-controls.md")
  are designed to detect, log, and alert after an event has
  occurred. For example, AWS Config provides a wide selection of
  [detective
  controls](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") for you to use.
- **Responsive controls**: These
  [controls](../../../prescriptive-guidance/latest/aws-security-controls/responsive-controls.md "../../../prescriptive-guidance/latest/aws-security-controls/responsive-controls.md")
  are designed to drive remediation of adverse events or
  deviations from your security baseline.
- **Privacy-aware workload**: A
  privacy-aware workload is designed and implemented with privacy
  as a core principle throughout its entire lifecycle. It
  proactively protects user data and respects individual privacy
  rights through technical, organizational, and design measures.
