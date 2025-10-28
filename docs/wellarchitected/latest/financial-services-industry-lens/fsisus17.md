# FSISUS17: How do you minimize your test, staging, sandbox instances?

## FSISUS17-BP01 Use infrastructure as code (IaC) code base to snapshot your

environment allowing you to decommission test infrastructure

**Prescriptive guidance**

Reducing the number, frequency, and use of test and staging environments can reduce
your environmental impact. If you use [Infrastructure as Code (IaC)](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md") — with [AWS Event Engine](https://mng.workshop.aws/ssm/capability_hands-on_labs/eventengine.html "https://mng.workshop.aws/ssm/capability_hands-on_labs/eventengine.html") or Workshop Studio — to snapshot your environments, you
can break down the infrastructure once your testing is complete. This allows you to
reduce the unneeded resources. If the test environment is required later, you can use
IaC to restore it when needed.

Instead of creating separate instances to test several environments, use snapshots
to test only the required workload using the same instance. You can queue your testing
based on development priorities to reduce the use of test and staging instances.
