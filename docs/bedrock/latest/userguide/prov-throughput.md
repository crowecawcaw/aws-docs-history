# Provisioned Throughput

When you configure Provisioned Throughput for a model, you receive a level of
throughput at a fixed cost.

You can use Provisioned Throughput with Amazon and third-party base models, and with
customized models.

Provisioned Throughput pricing varies depending on the model that you use and the level of commitment you choose. You receive a discounted rate when you commit to a longer period of time. For details about pricing for each model, see
the [Model providers](https://console.aws.amazon.com/bedrock/home#/providers "https://console.aws.amazon.com/bedrock/home#/providers")
page in the Amazon Bedrock console.

Your options for throughput for a model differ depending on whether you run inference on a base
model or a custom model.

###### Note

In the AWS GovCloud (US) region, you can only purchase Provisioned Throughput for custom models with no commitment.

| Pricing option                                         | Base model    | Custom model                                              |
| ------------------------------------------------------ | ------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Provisioned Throughput, no commitment (hourly pricing) | Not available | Available (maximum 2 Provisioned Throughputs per account) |
| Provisioned Throughput, 1 month commitment             | Available     | Available                                                 |
| Provisioned Throughput, 6 month commitment             | Available     | Available                                                 | You specify Provisioned Throughput in Model Units (MU). A model unit delivers a specific throughput level for the specified model. The throughput level of a MU for a given Text model specifies the following: <br>• **The total number of input tokens per minute** – The number of input tokens that an MU can process across all requests within a span of one minute. <br>• **The total number of output tokens per minute** – The number of output tokens that an MU can generate across all requests within a span of one minute. Model unit quotas depend on the level of commitment you specify for the Provisioned Throughput. <br>• For custom models with no commitment, a quota of one model unit is available for each Provisioned Throughput. You can create up to two Provisioned Throughputs per account. <br>• For base or custom models with commitment, there is a default quota of 0 model units. To request an increase, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). ###### Topics <br>• [Supported Region and models for Provisioned Throughput](pt-supported.md "pt-supported.md") <br>• [Procedures](prov-thru-workflow.md "prov-thru-workflow.md") <br>• [Permissions](prov-thru-permissions.md "prov-thru-permissions.md") <br>• [Provisioned Throughput console procedures](prov-cap-console.md "prov-cap-console.md") <br>• [Using the Provisioned Throughput API](prov-thru-api.md "prov-thru-api.md") |
