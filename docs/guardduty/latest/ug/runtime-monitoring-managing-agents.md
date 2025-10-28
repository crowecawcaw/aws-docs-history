# Managing GuardDuty security agents

You can manage the GuardDuty security agent for the resource that you want to monitor. If you
want to monitor more than one resource type, make sure to manage the GuardDuty agent for that
resource.

The following topics will help you with the next steps to manage the security
agent.

###### Contents

- [Enabling automated security agent for
  Amazon EC2 instance](managing-gdu-agent-ec2-automated.md "managing-gdu-agent-ec2-automated.md")
- [Managing security agent manually for Amazon EC2 resource](managing-gdu-agent-ec2-manually.md "managing-gdu-agent-ec2-manually.md")
- [Managing automated security agent for
  Fargate (Amazon ECS only)](managing-gdu-agent-ecs-automated.md "managing-gdu-agent-ecs-automated.md")
- [Managing security agent automatically
  for Amazon EKS resources](managing-gdu-agent-eks-automatically.md "managing-gdu-agent-eks-automatically.md")
- [Managing security agent manually for
  Amazon EKS cluster](managing-gdu-agent-eks-manually.md "managing-gdu-agent-eks-manually.md")
- [Configure GuardDuty security agent
  (add-on) parameters for Amazon EKS](guardduty-configure-security-agent-eks-addon.md "guardduty-configure-security-agent-eks-addon.md")
- [Validating VPC
  endpoint configuration](validate-vpc-endpoint-config-runtime-monitoring.md "validate-vpc-endpoint-config-runtime-monitoring.md")
  The following list includes good to know items after you install or update the security
  agent.

**Assess runtime coverage**

The next step after installing or updating your security agent is to assess
runtime coverage of your resources. If the runtime coverage status is
**Unhealthy**, then you must troubleshoot the issue. For
more information, see [Runtime coverage issues and
troubleshooting](runtime-monitoring-assessing-coverage.md "runtime-monitoring-assessing-coverage.md").

If the status of the runtime coverage shows as **Healthy**,
it indicates that Runtime Monitoring is able to collect and receive runtime events. For a
list of these events, see [Collected runtime event
types](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md").

**Private DNS name for endpoint**

After you install the GuardDuty security agent for your resources, by default, it
will resolve and connect to the private DNS name of the VPC endpoint. For a non-FIPS
endpoint, the private DNS will appear in the following format:

`guardduty-data.`us-east-1`.amazonaws.com`

The AWS Region, `us-east-1`, will change based on
your Region.

**A host may get installed with two security
agents**

When working with GuardDuty security agent for an Amazon EC2 instance, you might
install and use the agent on the underlying host within an Amazon EKS cluster. If you
had already deployed a security agent on that EKS cluster, the same host could
have two security agents running on it at the same time. For information about
how GuardDuty works in this scenario, see [Security agents on
same host](two-security-agents-installed-on-ec2-node.md "two-security-agents-installed-on-ec2-node.md").
