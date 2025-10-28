# Quotas for AppFabric

Your AWS account has default quotas, formerly referred to as limits, for each
AWS service. Unless otherwise noted, each quota is Region-specific. You can request
increases for some quotas, and other quotas cannot be increased.

To view the quotas for AppFabric, open the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **AppFabric**.

To request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. If the quota is not yet
available in Service Quotas, use the [limit increase
form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

The quotas related to AppFabric that are in your AWS account are shown in the following
table.

| Name                       | Default                   | Adjustable                                                                         | Description                                                                                                             |
| -------------------------- | ------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --- |
| Application bundles        | Each supported Region: 1  | No                                                                                 | The maximum number of application bundles that you can create in an account in the current AWS Region.                  |
| Application authorizations | Each supported Region: 50 | No                                                                                 | The maximum number of application authorizations that you can create in an account in the current AWS Region.           |
| Ingestions                 | Each supported Region: 50 | No                                                                                 | The maximum number of ingestions that you can create in an account in the current AWS Region.                           |
| Ingestion destinations     | Each supported Region: 5  | No                                                                                 | The maximum number of ingestion destinations that you can create per ingestion in an account in the current AWS Region. |
| AppClient                  | Each supported Region: 1  | No                                                                                 | The maximum number of AppClients that you can create in an account in the current AWS Region.                           |     |
| ---                        |                           | The AWS AppFabric for productivity feature is in preview and is subject to change. |                                                                                                                         |
