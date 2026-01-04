# [QA.TEM.1] Establish dedicated testing environments

**Category:** FOUNDATIONAL

Use testing environments to detect and correct issues earlier
on in the development lifecycle. Deploy integrated changes
into these environments before they are deployed to
production. These environments are as production-like as
possible, providing the ability to simulate real-world
conditions which can validate that changes are ready for
production deployment.

Design your testing environments to mimic production qualities
that you need to test, such as monitoring settings or regional
variants. At a minimum, have a staging environment that you
monitor closely to catch potential issues early. More testing
environments, such as beta or zeta, can be added as needed.
Infrastructure as code (IaC) should be used for managing and
deploying these environments, ensuring consistent and
predictable provisioning. Minimize direct human intervention
in these environments, similar to how you would treat
production environments. Instead, rely on automated delivery
pipelines with stages that deploy to the testing environment.
Human access should be strictly controlled, auditable, and
granted only in exceptional circumstances.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS06-BP04 Use
  managed device farms for testing](../sustainability-pillar/sus_sus_dev_a5.md "../sustainability-pillar/sus_sus_dev_a5.md")
- [Development
  and Test on Amazon Web Services](../../../whitepapers/latest/development-and-test-on-aws/testing-phase.md "../../../whitepapers/latest/development-and-test-on-aws/testing-phase.md")
- [Test
  environments in AWS Device Farm](../../../devicefarm/latest/developerguide/test-environments.md "../../../devicefarm/latest/developerguide/test-environments.md")
- [Deployment
  Pipeline Reference Architecture](https://pipelines.devops.aws.dev/application-pipeline/index.html#test-gamma "https://pipelines.devops.aws.dev/application-pipeline/index.html#test-gamma")
