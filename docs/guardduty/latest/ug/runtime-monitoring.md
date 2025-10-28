# GuardDuty Runtime Monitoring

Runtime Monitoring observes and analyzes operating system-level, networking, and file events to help
you detect potential threats in specific AWS workloads in your environment.

**Supported AWS resources in Runtime Monitoring** – GuardDuty had
initially released Runtime Monitoring to support only Amazon Elastic Kubernetes Service (Amazon EKS) resources. Now, you can use the
Runtime Monitoring feature to provide threat detection for your AWS Fargate Amazon Elastic Container Service (Amazon ECS) and
Amazon Elastic Compute Cloud (Amazon EC2) resources as well.

GuardDuty doesn't support Amazon EKS clusters running on AWS Fargate.

In this document and other sections related to Runtime Monitoring, GuardDuty uses the terminology of
**resource type** to refer to Amazon EKS, Fargate Amazon ECS, and Amazon EC2
resources.

Runtime Monitoring uses a GuardDuty security agent that adds visibility into runtime behavior, such as file
access, process execution, command line arguments, and network connections. For each resource type
that you want to monitor for potential threats, you can manage the security agent for that
specific resource type either automatically or manually (with an exception to Fargate (Amazon ECS
only)). Managing the security agent automatically means that you permit GuardDuty to install and
update the security agent on your behalf. On the other hand, when you manage the security agent
for your resources manually, you are responsible for installing and updating the security agent,
as needed.

With this extended capability, GuardDuty can help you identify and respond to potential threats
that may target applications and data running in your individual workloads and instances. For
example, a threat can potentially start by compromising a single container that runs a vulnerable
web application. This web application might have access permissions to the underlying containers
and workloads. In this scenario, incorrectly configured credentials could potentially lead to a
broader access to the account, and the data stored within it.

By analyzing the runtime events of the individual containers and workloads, GuardDuty can
potentially identify compromise of a container and associated AWS credentials in an initial
phase, and detect attempts to escalate privileges, suspicious API requests, and malicious access
to the data in your environment.

###### Contents

- [How it works](how-does-runtime-monitoring-work.md "how-does-runtime-monitoring-work.md")
- [How does 30-day free trial work in
  Runtime Monitoring](runtime-monitoring-free-trial-works.md "runtime-monitoring-free-trial-works.md")
- [Prerequisites to enabling Runtime Monitoring](runtime-monitoring-prerequisites.md "runtime-monitoring-prerequisites.md")
- [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md")
- [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md")
- [Reviewing runtime coverage statistics and
  troubleshooting issues](runtime-monitoring-assessing-coverage.md "runtime-monitoring-assessing-coverage.md")
- [Setting up CPU and memory
  monitoring](runtime-monitoring-setting-cpu-mem-monitoring.md "runtime-monitoring-setting-cpu-mem-monitoring.md")
- [Using shared VPC with Runtime Monitoring](runtime-monitoring-shared-vpc.md "runtime-monitoring-shared-vpc.md")
- [Using Infrastructure as
  Code (IaC) with GuardDuty automated security agents](using-iac-with-gdu-automated-agents-runtime-monitoring.md "using-iac-with-gdu-automated-agents-runtime-monitoring.md")
- [Collected runtime event types that GuardDuty
  uses](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md")
- [Amazon ECR repository hosting GuardDuty
  agent](runtime-monitoring-ecr-repository-gdu-agent.md "runtime-monitoring-ecr-repository-gdu-agent.md")
- [Two security agents on same
  underlying host](two-security-agents-installed-on-ec2-node.md "two-security-agents-installed-on-ec2-node.md")
- [EKS Runtime Monitoring in GuardDuty](eks-runtime-monitoring-guardduty.md "eks-runtime-monitoring-guardduty.md")
- [GuardDuty security agent release
  versions](runtime-monitoring-agent-release-history.md "runtime-monitoring-agent-release-history.md")
- [Disabling, uninstalling, and
  cleaning up resources in Runtime Monitoring](runtime-monitoring-agent-resource-clean-up.md "runtime-monitoring-agent-resource-clean-up.md")
