# Error: Limit exceeded

## Scenario

You receive "**`You have reached the limit on the number of resources you
 can share`**" or
"**`ResourceShareLimitExceededException`**" when trying to
share resources.

## Cause

These errors occur when you reach the maximum number of resources you can share
using either the AWS RAM service or the AWS service that created the resource you're
trying to share. This quota (formerly referred to as a limit) can affect both the
sharing account or the account you're sharing the resource with.

## Solution

1. To view your quotas, in the AWS account where you are seeing the error,
   navigate to one of the following pages, depending on the type of quota
   you're reaching:
   - The [AWS RAM page in the
     Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas")
   - The [page
     for the AWS service](https://console.aws.amazon.com/servicequotas/home/services "https://console.aws.amazon.com/servicequotas/home/services") whose resources are impacted by
     the quota

2. Scroll down and choose the relevant quota.
3. If it's available for this quota, choose **Request quota
   increase**.
4. Enter a new value for the quota, and then choose
   **Request**.
5. The request appears on the [Quota request history](https://console.aws.amazon.com/servicequotas/home/requests "https://console.aws.amazon.com/servicequotas/home/requests") page,
   where you can check on the status of the request until it's
   finalized.
