# Low-level SageMaker APIs for model cards

You can create an Amazon SageMaker Model Card directly through the SageMaker API or the AWS Command Line
Interface (AWS CLI).

###### Note

When creating a model card with the low-level APIs, the content must be in the
model card JSON schema and provided as a string. For more information, see [Model card JSON schema](model-cards.md#model-cards-json-schema "model-cards.md#model-cards-json-schema").

## SageMaker API

Use the following SageMaker API commands to work with Amazon SageMaker Model Cards:

- [CreateModelCard](../APIReference/API_CreateModelCard.md "../APIReference/API_CreateModelCard.md")
- [DescribeModelCard](../APIReference/API_DescribeModelCard.md "../APIReference/API_DescribeModelCard.md")
- [ListModelCards](../APIReference/API_ListModelCards.md "../APIReference/API_ListModelCards.md")
- [ListModelCardVersions](../APIReference/API_ListModelCardVersions.md "../APIReference/API_ListModelCardVersions.md")
- [UpdateModelCard](../APIReference/API_UpdateModelCard.md "../APIReference/API_UpdateModelCard.md")
- [CreateModelCardExportJob](../APIReference/API_CreateModelCardExportJob.md "../APIReference/API_CreateModelCardExportJob.md")
- [DescribeModelCardExportJob](../APIReference/API_DescribeModelCardExportJob.md "../APIReference/API_DescribeModelCardExportJob.md")
- [ListModelCardExportJobs](../APIReference/API_ListModelCardExportJobs.md "../APIReference/API_ListModelCardExportJobs.md")
- [DeleteModelCard](../APIReference/API_DeleteModelCard.md "../APIReference/API_DeleteModelCard.md")

## AWS CLI

Use the following AWS CLI commands to work with Amazon SageMaker Model Cards:

- [create-model-card](../../../cli/latest/reference/sagemaker/create-model-card.md "../../../cli/latest/reference/sagemaker/create-model-card.md")
- [describe-model-card](../../../cli/latest/reference/sagemaker/describe-model-card.md "../../../cli/latest/reference/sagemaker/describe-model-card.md")
- [list-model-cards](../../../cli/latest/reference/sagemaker/list-model-cards.md "../../../cli/latest/reference/sagemaker/list-model-cards.md")
- [list-model-card-versions](../../../cli/latest/reference/sagemaker/list-model-card-versions.md "../../../cli/latest/reference/sagemaker/list-model-card-versions.md")
- [update-model-card](../../../cli/latest/reference/sagemaker/update-model-card.md "../../../cli/latest/reference/sagemaker/update-model-card.md")
- [create-model-card-export-job](../../../cli/latest/reference/sagemaker/create-model-card-export-job.md "../../../cli/latest/reference/sagemaker/create-model-card-export-job.md")
- [describe-model-card-export-job](../../../cli/latest/reference/sagemaker/describe-model-card-export-job.md "../../../cli/latest/reference/sagemaker/describe-model-card-export-job.md")
- [list-model-card-export-jobs](../../../cli/latest/reference/sagemaker/list-model-card-export-jobs.md "../../../cli/latest/reference/sagemaker/list-model-card-export-jobs.md")
- [delete-model-card](../../../cli/latest/reference/sagemaker/delete-model-card.md "../../../cli/latest/reference/sagemaker/delete-model-card.md")
