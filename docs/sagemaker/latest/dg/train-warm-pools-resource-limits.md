# Request a warm pool quota increase

To get started, you must first request a service limit increase for SageMaker AI managed warm
pools. The default resource limit for warm pools is 0.

If a training job is created with `KeepAlivePeriodInSeconds` specified, but
you did not request a warm pool limit increase, then a warm pool is not retained after
the completion of the training job. A warm pool is only created if your warm pool limit
has sufficient resources. After a warm pool is created, the resources are released when
they move to a matching training job or if the `KeepAlivePeriodInSeconds`
expires (if the warm pool status is `Reused` or
`Terminated`).

Request a warm pool quota increase using the AWS Service Quotas console.

###### Note

All warm pool instance usage counts toward your SageMaker training resource limit.
Increasing your warm pool resource limit does not increase your instance limit,
but allocates a subset of your resource limit to warm pool training.

1. Open the [AWS Service
   Quotas console](https://console.aws.amazon.com/servicequotas/home/ "https://console.aws.amazon.com/servicequotas/home/").
2. On the left-hand navigation panel, choose **AWS
   services**.
3. Search for and choose **Amazon SageMaker AI**.
4. Search for the keyword `warm pool` to see all
   available warm pool service quotas.
5. Find the instance type for which you want to increase your warm pool
   quota, select the warm pool service quota for that instance type, and choose
   **Request quota increase**.
6. Enter your requested instance limit number under **Change quota
   value**. The new value must be greater than the current
   **Applied quota value**.
7. Choose **Request**.
   There is a limit on the number of instances that you can retain for each account,
   which is determined by instance type. You can check your resource limits in the
   [AWS Service Quotas
   console](https://console.aws.amazon.com/servicequotas/home/ "https://console.aws.amazon.com/servicequotas/home/") or directly using the [list-service-quotas](../../../cli/latest/reference/service-quotas/list-service-quotas.md "../../../cli/latest/reference/service-quotas/list-service-quotas.md") AWS CLI command. For more information on AWS
   Service Quotas, see [Requesting a
   quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
   Guide_.

You can also use [AWS Support
Center](https://support.console.aws.amazon.com "https://support.console.aws.amazon.com") to request a warm pool quota increase. For a list of available
instance types according to Region, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") and choose
**Training** in the **On-Demand Pricing**
table.
