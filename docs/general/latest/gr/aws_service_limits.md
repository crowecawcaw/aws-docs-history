# AWS service quotas

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is Region-specific. You can request increases
for some quotas, but not all quotas can be increased.

###### To view service quotas

You can view service quotas by using the following options:

- From the documentation: Open the [Service endpoints and quotas](aws-service-information.md "aws-service-information.md") page in the documentation, search for
  the service name, and then click the link to go to the page for that service. To
  view the service quotas for all AWS services in the documentation without
  switching pages, view the information in the PDF [Service
  endpoints and quotas](aws-general.md#aws-service-information "aws-general.md#aws-service-information") page.
- From the console: Open the [Service Quotas
  console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS
  services**, and then select a service. For more information, see [Viewing service quotas](../../../servicequotas/latest/userguide/gs-request-quota.md "../../../servicequotas/latest/userguide/gs-request-quota.md") in the
  _Service Quotas User Guide_.
- From the AWS CLI: Use the [list-service-quotas](../../../cli/latest/reference/service-quotas/list-service-quotas.md "../../../cli/latest/reference/service-quotas/list-service-quotas.md") and [list-aws-default-service-quotas](../../../cli/latest/reference/service-quotas/list-aws-default-service-quotas.md "../../../cli/latest/reference/service-quotas/list-aws-default-service-quotas.md") AWS CLI commands. For instructions, see
  [Viewing service quotas](../../../servicequotas/latest/userguide/gs-request-quota.md "../../../servicequotas/latest/userguide/gs-request-quota.md") in the _Service Quotas User Guide_.
  Your account's actual quota value may be less than the AWS default quota value
  if the account was recently created or if you use the account minimally.

###### To request a quota increase

Support might approve, deny, or partially approve your quota increase requests.
Increases are not granted immediately. It might take a couple of days for your increase
to take effect.

You can request a quota increase by using one of following options:

- From the console: Open the [Service Quotas
  console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS
  services**. Select a service, select a quota, and follow the directions
  to request a quota increase. For instructions, see [Requesting a
  quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
- From the AWS CLI: Use the [request-service-quota-increase](../../../cli/latest/reference/service-quotas/request-service-quota-increase.md "../../../cli/latest/reference/service-quotas/request-service-quota-increase.md") AWS CLI command. For instructions, see
  [Requesting a
  quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
- From a support case: If a service is not yet available in Service Quotas, use the AWS Support Center Console
  to create a [service quota increase case](https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). If the service is available in Service Quotas, we
  highly recommend that you use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home") instead of creating a support case.
