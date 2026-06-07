# Quotas

The following quotas apply to multi-turn reinforcement learning jobs. These quotas
are adjustable. To request an increase, open the [Service
Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas "https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas"). For more information, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

| Quota                                                                     | Default value | Adjustable |
| ------------------------------------------------------------------------- | ------------- | ---------- |
| Maximum number of concurrent multi-turn reinforcement fine tuning<br>jobs | 1             | Yes        |
| Maximum number of concurrent multi-turn reinforcement evaluation<br>jobs  | 1             | Yes        |

API throttling limits for `CreateJob`, `DescribeJob`, and
other management APIs are not adjustable. For the full list of Amazon SageMaker AI quotas, see
[Amazon SageMaker AI endpoints
and quotas](../../../general/latest/gr/sagemaker.md#limits_sagemaker "../../../general/latest/gr/sagemaker.md#limits_sagemaker") in the _AWS General Reference_.
