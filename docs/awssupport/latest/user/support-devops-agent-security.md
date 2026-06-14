# Security for AWS DevOps Agent activated from AWS Support

AWS DevOps Agent provides the following security controls:

- Agent spaces are the primary security boundary. Each agent space is isolated
  to a single AWS account.
- Data is encrypted at rest with AWS-managed keys and encrypted in
  transit.
- Agent activity is captured in an immutable agent journal and in AWS CloudTrail
  (CloudTrail).
- AWS DevOps Agent enforces account-boundary, limited-write, and prompt-injection
  protections.
  For the full security posture, including regional processing, integration security,
  network connectivity, and the shared responsibility model, see [AWS DevOps Agent
  Security](../../../devopsagent/latest/userguide/aws-devops-agent-security.md "../../../devopsagent/latest/userguide/aws-devops-agent-security.md") in the _AWS DevOps Agent User Guide_.
