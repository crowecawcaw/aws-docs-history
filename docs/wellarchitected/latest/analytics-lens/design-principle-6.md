# 6 – Design resilience for analytics

workload

How do you design analytics workloads to withstand and mitigate
failures?

| **ID**
| **Priority**
| **Best practice**
|
| --- | --- | --- |
| ☐ BP 6.1 | Required | Create an illustration of data flow dependencies. |
| ☐ BP 6.2 | Required | Monitor analytics systems to detect analytics or extract, transform and load (ETL) job failures. |
| ☐ BP 6.3 | Required | Notify stakeholders about analytics or ETL job failures. |
| ☐ BP 6.4 | Recommended | Automate the recovery of analytics and ETL job failures. |
| ☐ BP 6.5 | Recommended | Build a disaster recovery (DR) plan for the analytics infrastructure and the data. | For more details, refer to the following documentation: <br>• AWS Glue Developer Guide: [Running and Monitoring AWS Glue](../../../glue/latest/dg/monitor-glue.md "../../../glue/latest/dg/monitor-glue.md") <br>• AWS Glue Developer Guide: [Monitoring with Amazon CloudWatch](../../../glue/latest/dg/monitor-cloudwatch.md "../../../glue/latest/dg/monitor-cloudwatch.md") <br>• AWS Glue Developer Guide: [Monitoring AWS Glue Using Amazon CloudWatch Metrics](../../../glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.md "../../../glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.md") <br>• AWS Prescriptive Guidance – Patterns: [Orchestrate an ETL pipeline with validation, transformation, and](../../../prescriptive-guidance/latest/patterns/orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions.md "../../../prescriptive-guidance/latest/patterns/orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions.md") [partitioning using AWS Step Functions](../../../prescriptive-guidance/latest/patterns/orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions.md "../../../prescriptive-guidance/latest/patterns/orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions.md") <br>• AWS Support Knowledge Center: [How can I use a Lambda function to receive SNS alerts](https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-fail-retry-lambda-sns-alerts/ "https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-fail-retry-lambda-sns-alerts/") [when an AWS Glue job fails a retry?](https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-fail-retry-lambda-sns-alerts/ "https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-fail-retry-lambda-sns-alerts/") <br>• AWS Glue Developer Guide: [Repairing and Resuming a Workﬂow Run](../../../glue/latest/dg/resuming-workflow.md "../../../glue/latest/dg/resuming-workflow.md")
