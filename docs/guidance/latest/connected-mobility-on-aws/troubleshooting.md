# Troubleshooting

## Common deployment issues

### CDK Bootstrap Error

- Ensure AWS CLI is configured with sufficient permissions
- Verify the target region supports all required services
- Run `cdk bootstrap` manually if automated bootstrap fails

### IoT Policy Conflicts

- Delete existing IoT policies with conflicting names
- Use unique deployment stage names to avoid conflicts
- Check IoT Core quotas in your region

### MSK Cluster Creation Timeout

- Verify VPC and subnet configuration
- Check service quotas for MSK in your region
- Ensure KMS key permissions are correctly configured

## Performance optimization

### High Latency Issues

- Monitor CloudWatch metrics for processing delays
- Scale Flink application parallelism
- Optimize DynamoDB read/write capacity

### Cost Optimization

- Use DynamoDB on-demand pricing for variable workloads
- Configure MSK cluster auto-scaling
- Implement data lifecycle policies for S3 storage
