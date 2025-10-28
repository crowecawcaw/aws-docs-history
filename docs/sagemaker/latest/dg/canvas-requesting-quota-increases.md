# Request a Quota Increase

Your users might use AWS resources in amounts that exceed those specified by their
quotas. If your users are resource constrained and encounter errors in SageMaker Canvas, you can request
a quota increase for them.

For more details about SageMaker AI quotas and how to request a quota increase, see [Quotas](regions-quotas.md#regions-quotas-quotas "regions-quotas.md#regions-quotas-quotas").

Amazon SageMaker Canvas uses the following services to process the requests of your users:

- Amazon SageMaker Autopilot
- Amazon SageMaker Studio Classic domain
  For a list of the available quotas for SageMaker Canvas operations, see
  [Amazon SageMaker AI
  endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").

## Request an increase for

instances to build custom models

When building a custom model, if you encounter an error during post-building analysis
that tells you to increase your quota for `ml.m5.2xlarge` instances, use the
following information to resolve the issue.

You must increase the SageMaker AI Hosting endpoint quota for the `ml.m5.2xlarge`
instance type to a non-zero value in your AWS account. After building a model, SageMaker Canvas hosts
the model on a SageMaker AI Hosting endpoint and uses the endpoint to generate the post-building
analysis. If you don't increase the default account quota of 0 for
`ml.m5.2xlarge` instances, SageMaker Canvas cannot complete this step and generates an
error during post-building analysis.

For the procedure to increase the quota, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
