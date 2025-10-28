# Anti-patterns for automated compliance and guardrails

- **Manual policy enforcement**: Relying on manual checks and
  balances to enforce policies and standards. It's difficult to maintain consistent
  governance and mitigate risks with manual methods, especially when dealing with
  high-velocity, constantly changing environments and systems. Use automated tools that
  enforce, monitor, and audit compliance standards consistently across environments.
- **Static compliance
  checks**: Only validating compliance during
  specific phases of the development lifecycle, such as at
  the end of development, instead of continuously throughout
  the lifecycle. This can lead to late-stage discoveries of
  non-compliance, which are costlier and more time-consuming
  to address. Implement continuous compliance checks
  throughout the development, including both during and
  after deployment.
- **Relying on manual
  remediation**: Manual remediation can lead to
  delays in identifying and resolving issues, extending
  vulnerability windows. It can also be an inefficient use
  of resources, leading to higher costs and increased risk
  of human error. Build auto-remediation processes that not
  only detect but also resolve non-compliant findings in
  real-time.
- **Over-reliance on preventative
  guardrails**: Solely relying on preventive
  measures and not considering detective or responsive
  controls. It's impossible to predict and prevent every
  potential non-compliance issue making it important to have
  a balanced mix of detective, preventive, and responsive
  controls in place.
- **Manual change
  validation**: With traditional change management,
  a Change Advisory Board (CAB) meeting would precede a
  release approval. The CAB verifies that proper actions
  have been taken to remediate change risk. This includes
  ensuring that a group of subject matter experts reviewed
  the change and that organizational requirements for
  quality assurance and governance are being followed, such
  as ensuring expected tests were run and that deployments
  occur within approved change windows. Traditional CAB
  approval could take from days to weeks to schedule and
  debate the changes. Use automated governance capabilities
  to automate these checks as part of the development
  lifecycle and continuously within your environment.
