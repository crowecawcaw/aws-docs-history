# Selection

| PER 1: How have you optimized the performance of your serverless<br>application? |
| -------------------------------------------------------------------------------- |
|                                                                                  |

Run performance tests on your serverless application using steady and burst rates. Using
the result, try tuning capacity units and the provisioning model, and load test after changes
to help you select the best configuration:

- **[Amazon API Gateway](amazon-api-gateway.md "amazon-api-gateway.md"):** Use Edge endpoints for geographically
  dispersed customers. Use Regional for regional customers and when using other AWS
  services within the same Region.
- **[AWS Lambda](aws-lambda.md "aws-lambda.md"):** Test different memory settings since CPU,
  network, and storage IOPS are allocated proportionally. Optimize static initialization and
  consider provisioned concurrency.
- **[AWS Step Functions](aws-step-functions.md "aws-step-functions.md")**: Test Standard and Express Workflows, consider
  the per second rates for both execution start rate and state transition rate.
- **Amazon DynamoDB:** Use on-demand for unpredictable application
  traffic, otherwise provisioned mode for consistent traffic.
- **Amazon Kinesis:** Use enhanced-fan-out for dedicated input/output
  channels per consumer in multiple consumer scenarios. Use an extended batch window for low
  volume transactions with Lambda.
