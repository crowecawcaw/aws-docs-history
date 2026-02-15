# Amazon ECR usage metrics

You can use CloudWatch usage metrics to provide visibility into your account's usage of
resources. Use these metrics to visualize your current service usage on CloudWatch graphs and
dashboards.

Amazon ECR usage metrics correspond to AWS service quotas. You can configure alarms that
alert you when your usage approaches a service quota. For more information about Amazon ECR
service quotas, see [Amazon ECR service quotas](service-quotas.md "service-quotas.md").

Amazon ECR publishes the following metrics in the `AWS/Usage`
namespace.

| Metric          | Description                                                                                                                                                                                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CallCount`     | The number of API action calls from your account. The resources<br>are defined by the dimensions associated with the metric.<br>The most useful statistic for this metric is `SUM`,<br>which represents the sum of the values from all contributors during<br>the period defined. |
| `ResourceCount` | The number of the specified resources in your account. The resources<br>are defined by the dimensions associated with the metric.<br>The most useful statistic for this metric is `MAXIMUM`,<br>which represents the maximum number of resources used during the 5-minute period. |

The following dimensions are used to refine the API usage metrics that are published by
Amazon ECR.

| Dimension  | Description                                                                                                                                                                                                                                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`  | The name of the AWS service containing the resource. For Amazon ECR<br>usage metrics, the value for this dimension is<br>`ECR`.                                                                                                                                                                                                                     |
| `Type`     | The type of entity that is being reported. Currently, the only<br>valid value for Amazon ECR API usage metrics is `API`.                                                                                                                                                                                                                            |
| `Resource` | The type of resource that is running. Currently, Amazon ECR returns<br>information on your API usage for the following API actions.<br>• `GetAuthorizationToken`<br>• `BatchCheckLayerAvailability`<br>• `InitiateLayerUpload`<br>• `UploadLayerPart`<br>• `CompleteLayerUpload`<br>• `PutImage`<br>• `BatchGetImage`<br>• `GetDownloadUrlForLayer` |
| `Class`    | The class of resource being tracked. Currently, Amazon ECR does not use<br>the class dimension.                                                                                                                                                                                                                                                     |

The following dimensions are used to refine the Resource usage metrics that are published by
Amazon ECR.

| Dimension    | Description                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`    | The name of the AWS service containing the resource. For Amazon ECR<br>usage metrics, the value for this dimension is<br>`ECR`.                                                                                                                                                                         |
| `Type`       | The type of entity that is being reported. Currently, the only<br>valid value for Amazon ECR resource usage metrics is `RESOURCE`.                                                                                                                                                                      |
| `Resource`   | The type of resource that is running. Currently, Amazon ECR returns<br>information on your resource usage for the following metrics.<br>• `RepositoryCount`<br>• `ImagesPerRepositoryCount`                                                                                                             |
| `ResourceId` | The identifier for the resource that incurred the usage.<br>Currently, ResourceId is only relevant to `ImagesPerRepositoryCount`<br>and its value is formatted as repository/your_repository_name. For example:<br>"repository/my-repo" returns the number of images in repository with name "my-repo". |
