# Quotas for Amazon Bedrock

Your AWS account has default quotas, formerly referred to as limits, for Amazon Bedrock. To view
service quotas for Amazon Bedrock, do one of the following:

- Follow the steps at [Viewing service
  quotas](../../../servicequotas/latest/userguide/gs-request-quota.md "../../../servicequotas/latest/userguide/gs-request-quota.md") and select **Amazon Bedrock** as the service.
- Refer to the [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") in the AWS General Reference.
  Model inference in Amazon Bedrock is controlled by quotas on token usage. Some models utilize tokens at a higher rate. For more information about these rates and how to optimize your token usage, see [How tokens are counted in Amazon Bedrock](quotas-token-burndown.md "quotas-token-burndown.md").

To maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock, the
default quotas assigned to an account might be updated depending on regional factors,
payment history, fraudulent usage, and/or approval of a [quota increase request](quotas-increase.md "quotas-increase.md").

###### Topics

- [How tokens are counted in Amazon Bedrock](quotas-token-burndown.md "quotas-token-burndown.md")
- [Monitor your token usage by counting tokens before running inference](count-tokens.md "count-tokens.md")
- [Request an increase for Amazon Bedrock quotas](quotas-increase.md "quotas-increase.md")
