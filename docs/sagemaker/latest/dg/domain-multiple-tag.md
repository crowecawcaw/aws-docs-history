# Automatic tag propagation

Tags allow you to categorize and label your resources based on various criteria, such as
project, team, environment (For example, dev, staging, prod), or any other custom metadata.
You can tag resources by your domain automatically when they are created within your
domain. This makes it easier to identify and manage your resources across your
domains. You can also use these tags for cost allocation using
AWS Billing and Cost Management. For more information, see [Using AWS cost allocation
tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").

By default, any SageMaker AI resources that support tagging and are created from within the
Amazon SageMaker Studio or Amazon SageMaker Studio Classic UI after 11/30/2022 are automatically tagged with a
domain ARN tag. The domain ARN tag is based on the domain ID of the domain
that the resource is created in.

To backfill your SageMaker AI resources, you can add the `sagemaker:domain-arn` tag to
untagged resources by following the steps in [Backfill domain tags](domain-multiple-backfill.md "domain-multiple-backfill.md").

The following list describes the only SageMaker AI resources that _do
not_ support automatic tag propagation, as well as the impacted API calls where
the tag is not returned because it was not automatically set.

###### Note

All SageMaker `List` APIs do not support tag-based resource isolation.

The `default` app, which manages the Studio UI, is not automatically
tagged.

| SageMaker AI resource | Affected API calls                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ImageVersionArn       | • [describe-image-version](../../../cli/latest/reference/sagemaker/describe-image-version.md "../../../cli/latest/reference/sagemaker/describe-image-version.md")<br>• [update-image-version](../../../cli/latest/reference/sagemaker/update-image-version.md "../../../cli/latest/reference/sagemaker/update-image-version.md")<br>• [delete-image-version](../../../cli/latest/reference/sagemaker/delete-image-version.md "../../../cli/latest/reference/sagemaker/delete-image-version.md") |
| ModelCardExportJobArn | [describe-model-card-export-job](../../../cli/latest/reference/sagemaker/describe-model-card-export-job.md "../../../cli/latest/reference/sagemaker/describe-model-card-export-job.md")                                                                                                                                                                                                                                                                                                         |
| ModelPackageArn       | [describe-model-package](../../../cli/latest/reference/sagemaker/describe-model-package.md "../../../cli/latest/reference/sagemaker/describe-model-package.md")                                                                                                                                                                                                                                                                                                                                 |
