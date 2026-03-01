# Amazon ECR repository metrics

Amazon ECR sends repository pull count metrics to Amazon CloudWatch. Amazon ECR metric data is
automatically sent to CloudWatch in 1-minute periods. For more information about CloudWatch, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Topics

- [Enabling CloudWatch metrics](#enable_cloudwatch "#enable_cloudwatch")
- [Available metrics and dimensions](#available_cloudwatch_metrics "#available_cloudwatch_metrics")
- [Viewing Amazon ECR metrics using the CloudWatch console](#viewing_metrics_console "#viewing_metrics_console")

## Enabling CloudWatch metrics

Amazon ECR sends repository metrics automatically for all repositories. There is no
need to take any manual steps.

## Available metrics and dimensions

The following sections list the metrics and dimensions that Amazon ECR sends to
Amazon CloudWatch.

### Amazon ECR metrics

Amazon ECR provides metrics for you to monitor your repositories. You can measure
the pull count.

The `AWS/ECR` namespace includes the following metrics.

`RepositoryPullCount`

The total number of pulls for the images in the repository.

Valid dimensions: `RepositoryName`.

Valid statistics: Average, Minimum, Maximum, Sum, Sample Count.
The most useful statistic is Sum.

Unit: Integer.

### Dimensions for Amazon ECR metrics

Amazon ECR metrics use the `AWS/ECR` namespace and provide metrics for
the following dimensions.

`RepositoryName`

This dimension filters the data that you request for all container
images in a specified repository.

## Viewing Amazon ECR metrics using the CloudWatch console

You can view Amazon ECR repository metrics on the CloudWatch console. The CloudWatch console
provides a fine-grained and customizable display of your resources. For more
information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
