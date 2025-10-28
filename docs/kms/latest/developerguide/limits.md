# Quotas

To make AWS KMS responsive and performant for all users, AWS KMS applies two types of quotas,
resource quotas and request quotas. Each quota is calculated independently for each Region of
each AWS account.

All AWS KMS quotas are adjustable, except for the [on-demand rotation resource quota](resource-limits.md#on-demand-rotation-resource-quota "resource-limits.md#on-demand-rotation-resource-quota")
and the [AWS CloudHSM key store request quota](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores"). To request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-increase.md "../../../servicequotas/latest/userguide/request-increase.md") in the _Service Quotas User Guide_. To request a quota decrease, to change a quota that is not listed in Service Quotas, or to change a quota in an AWS Region where Service Quotas for AWS KMS is not available,
please visit [AWS Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and
create a case.

###### Topics

- [Resource quotas](resource-limits.md "resource-limits.md")
- [Request quotas](requests-per-second.md "requests-per-second.md")
- [Throttling AWS KMS requests](throttling.md "throttling.md")
