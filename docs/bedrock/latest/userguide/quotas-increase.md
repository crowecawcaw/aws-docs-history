# Request an increase for Amazon Bedrock quotas

The steps for requesting a quota increase for your account depend on the value in the
**Adjustable** column in the quotas table in
[Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock"):

- If a quota is marked as **Yes**, you can adjust it by
  following the steps at [Requesting
  a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the Service Quotas User Guide.
- For any model, you can request an increase for the following quotas
  together:

      + Cross-Region InvokeModel tokens per minute for
       `${model}`
      + Cross-Region InvokeModel requests per minute for
       `${model}`
      + On-demand InvokeModel tokens per minute for
       `${model}`
      + On-demand InvokeModel requests per minute for
       `${model}`
      + Model invocation max tokens per day for
       `${model}`

  To request an increase for any combination of these quotas, request an
  increase for the **Cross-Region InvokeModel tokens per minute for
  `${model}`** quota by following the
  steps at [Requesting
  a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the Service Quotas User Guide. After you do so, the
  support team will reach out and offer you the option of also increasing the
  other four quotas.

###### Note

Due to overwhelming demand, priority will be given to customers who
generate traffic that consumes their existing quota allocation. Your request
might be denied if you don't meet this condition.
