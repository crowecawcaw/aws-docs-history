

# Actions, resources, and condition keys for Amazon GroundTruth Labeling
<a name="list_groundtruthlabeling"></a>

Amazon GroundTruth Labeling (service prefix: `groundtruthlabeling`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/groundtruthlabeling/groundtruthlabeling.json) for this service.

**Topics**
+ [Actions defined by Amazon GroundTruth Labeling](#list_groundtruthlabeling-actions-as-permissions)
+ [Permission-only actions for Amazon GroundTruth Labeling](#list_groundtruthlabeling-permission-only-actions)
+ [Resource types defined by Amazon GroundTruth Labeling](#list_groundtruthlabeling-resources-for-iam-policies)
+ [Condition keys for Amazon GroundTruth Labeling](#list_groundtruthlabeling-policy-keys)

## Actions defined by Amazon GroundTruth Labeling
<a name="list_groundtruthlabeling-actions-as-permissions"></a>

Amazon GroundTruth Labeling has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Amazon GroundTruth Labeling
<a name="list_groundtruthlabeling-permission-only-actions"></a>

The following actions are defined by Amazon GroundTruth Labeling but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssociatePatchToManifestJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to associate a patch file with the manifest file to update the manifest file |  |   | Write | 
|   [CreateBatch](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to create a GT\+ Batch |  |   | Write | 
|   [CreateIntakeForm](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to create intake form |  |   | Write | 
|   [CreateProject](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to create a GT\+ Project |  |   | Write | 
|   [CreateWorkflowDefinition](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to create a GT\+ Workflow Definition |  |   | Write | 
|   [DescribeConsoleJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to get status of GroundTruthLabeling Jobs |  |   | Read | 
|   [GenerateLIDARPreviewTaskConfigJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to generate LiDAR Preview Task |  |   | Write | 
|   [GetBatch](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to get a GT\+ Batch |  |   | Read | 
|   [GetIntakeFormStatus](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to get a intake forms |  |   | Read | 
|   [ListBatches](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to list a GT\+ Batchs |  |   | Read | 
|   [ListDatasetObjects](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to list dataset objects in a manifest file |  |   | Read | 
|   [ListProjects](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to list a GT\+ Projects |  |   | Read | 
|   [RunFilterOrSampleDatasetJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-data-filtering)  | Grants permission to filter records from a manifest file using S3 select. Get sample entries based on random sampling |  |   | Write | 
|   [RunGenerateManifestByCrawlingJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to list a S3 prefix and create manifest files from objects in that location |  |   | Write | 
|   [RunGenerateManifestMetricsJob](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to generate metrics from objects in manifest |  |   | Write | 
|   [UpdateBatch](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html#sms-console-create-manifest-file)  | Grants permission to update a GT\+ Batch |  |   | Write | 

## Resource types defined by Amazon GroundTruth Labeling
<a name="list_groundtruthlabeling-resources-for-iam-policies"></a>

Amazon GroundTruth Labeling does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon GroundTruth Labeling
<a name="list_groundtruthlabeling-policy-keys"></a>

Amazon GroundTruth Labeling has no service-specific condition keys that can be used in the `Condition` element of policy statements.