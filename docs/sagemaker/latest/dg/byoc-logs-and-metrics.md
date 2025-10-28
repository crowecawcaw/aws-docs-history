# How Amazon SageMaker Processing Provides Logs and Metrics for Your

Processing Container

When your processing container writes to `stdout` or
`stderr`, Amazon SageMaker Processing saves the output from each processing
container and puts it in Amazon CloudWatch logs. For information about logging, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md "logging-cloudwatch.md").

Amazon SageMaker Processing also provides CloudWatch metrics for each instance running your processing
container. For information about metrics, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
