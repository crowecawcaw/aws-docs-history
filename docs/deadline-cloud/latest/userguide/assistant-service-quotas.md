# Service quotas and throttling

The assistant uses on-demand inference, which is subject to your
account's service quotas. The two primary constraints are:

- **Requests per minute (RPM)** – The number of
  model invocation requests allowed per minute.
- **Tokens per minute (TPM)** – The total number
  of input and output tokens processed per minute.
  Default quotas vary by Region. Some Regions have lower default limits (as low as 20
  RPM), which might result in throttling during heavy assistant usage.

## Requesting a quota increase

If you experience throttling errors when using the assistant, you can request a
service quota increase:

###### To request a quota increase

1. Open the [Service Quotas
   console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose **AWS services**, then choose
   .
3. Find the quota for the model used by the assistant (look for quotas related to
   `InvokeModelWithResponseStream` for the relevant model).
4. Choose the quota name, then choose **Request increase at account
   level**.
5. Enter your desired quota value and submit the request.

For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

###### Note

If your Region uses cross-region inference, the service quotas in the destination
Regions also apply. Cross-region inference profiles support a minimum of 200 RPM, which
can help alleviate throttling in Regions with lower single-Region limits.

## Monitoring quota usage

You can monitor your quota usage through CloudWatch metrics. Set up CloudWatch
alarms on throttling metrics to proactively identify when you are approaching your
quota limits. For more information, see [Monitoring](../../../bedrock/latest/userguide/monitoring-overview.md "../../../bedrock/latest/userguide/monitoring-overview.md") in the
_User Guide_.
