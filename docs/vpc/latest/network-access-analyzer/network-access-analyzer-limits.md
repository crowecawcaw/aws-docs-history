# Quotas and considerations for Network Access Analyzer

Your AWS account has default quotas, formerly referred to as limits, for each
AWS service. You can request increases for some quotas, but not for all quotas.

To view the quotas for Network Access Analyzer, open the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services**, and
then select **Network Insights**. To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

Your AWS account has the following quotas related to Network Access Analyzer.

| Name                             | Default | Adjustable                                                                                                                                                                                         |
| -------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access scopes                    | 1,000   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-72DF2E0E "https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-72DF2E0E") |
| Access scope analyses            | 10,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-06B98CB1 "https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-06B98CB1") |
| Concurrent access scope analyses | 25      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-2AC9F231 "https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-2AC9F231") |
| Findings per scope analysis      | 10,000  | No                                                                                                                                                                                                 | ## Analysis runtime All network interfaces in the account and Region are included in every analysis. The running analysis times out after 4 hours. |
