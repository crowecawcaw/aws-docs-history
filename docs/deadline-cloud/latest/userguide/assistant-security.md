# Security

The Deadline Cloud assistant operates within the existing Deadline Cloud security
model:

- **Read-only access** – The assistant only
  performs read operations (Get, List, Search) on Deadline Cloud resources and CloudWatch
  logs. It cannot modify your resources.
- **Customer-account execution** – All
  model invocations occur in your AWS account using your credentials
  and service quotas.
- **Scoped permissions** – The policy is
  scoped to cross-region inference profiles for your geographic region. Monitor users
  cannot access actions beyond
  `InvokeModelWithResponseStream`.
- **Session isolation** – Conversations are
  isolated to individual browser sessions and are not persisted or shared.
- **Fail closed** – If the assistant cannot
  determine whether it is enabled (for example, if the `GetMonitorSettings`
  call fails), the assistant UI is not displayed.
- **Admin control** – Only administrators can
  enable or disable the assistant. Monitor users cannot self-escalate access.
- **Abuse detection** – abuse detection
  capabilities apply to assistant usage. For more information, see [Abuse
  detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md") in the _User Guide_.
