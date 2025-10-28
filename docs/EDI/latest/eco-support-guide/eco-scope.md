# Scope of changes performed by EDI Cloud Operations

ECO deploys or updates AWS resources only in the following situations through a predefined access model:

- To deploy and update tools and resources required by ECO to service EDI.
- As part of EDI monitoring in response to events and alarms.
- To remediate security issues as part of responses to violations in EDI such as making noncompliant resources conform to
  security best practices.
- During remediation and restoration as part of an incident response.
- During deployment, application patching, and updates for major and minor releases of EDI.
- When conﬁguring the following ECO features:

      + Alarm manager
      + Resource tagger
      + Resource scheduler
      + Backup plans

  ECO doesn't deploy or update resources outside the preceding situations.
