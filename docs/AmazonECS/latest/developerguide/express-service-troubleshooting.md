# Troubleshooting Amazon ECS Express Mode services

This section helps you identify and resolve common issues when deploying and managing Express Mode services.

## Deployment issues

### Service stuck in ACTIVE or DRAINING status

**Symptoms:** DescribeServiceRevisions shows resources are still provisioning or deprovisioning. DescribeServices
shows deployment not stabilized

**Possible causes and solutions:**

- **Insufficient IAM permissions** - Verify that the task execution role and infrastructure role have the
  necessary permissions as shown in their respective managed policies.

```

# Check if the role has the required managed policy
aws iam list-attached-role-policies --role-name ecsTaskExecutionRole

```

- **Image pull failures** - Ensure the container image exists and is accessible.

```

# Test image pull manually
docker pull 123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:latest

```

- **Network connectivity issues** - Check that subnets have internet access or Amazon VPC endpoints for AWS services.
- **Resource limits** - Verify that your account has sufficient Fargate capacity and hasn't reached service quotas.

**Diagnostic steps:**

1. Use DescribeExpressGatewayService to get your current Service Revisionfollowed by DescribeServiceRevisions for the ServiceRevision to get status on
   the provisioning or deprovisioning
2. Check the service events in the Amazon ECS console for detailed error messages.
3. Check the container port was set correctly
4. Check AWS service quotas for Amazon ECS and Fargate.

### Task startup failures

**Symptoms:** Tasks fail to start or immediately stop after starting.

**Common causes:**

- **Application errors** - The container application exits due to configuration or runtime errors.
- **Health check failures** - The application doesn't respond to health checks on the expected port or path.
- **Resource constraints** - Insufficient CPU or memory allocation for the application.
- **Missing environment variables or secrets** - Required configuration is not available to the application.

**Resolution steps:**

1. Check application logs in CloudWatch Logs, obtain the log group name from DescribeServiceRevisions:

```

aws logs describe-log-streams --log-group-name /ecs/express-service-my-app
aws logs get-log-events --log-group-name /ecs/express-service-my-app --log-stream-name stream-name

```

2. Verify that the health check path returns HTTP 200 status.
3. Test the container image locally to ensure it starts correctly.
4. Review and adjust CPU and memory allocations if needed.

## Connectivity issues

### Application unreachable via load balancer

**Symptoms:** The application URL returns timeouts or connection errors.

**Troubleshooting steps:**

1. Validate your resources have finished provisioning
2. Verify that tasks are running and healthy:

```

aws ecs describe-services --cluster my-cluster --services my-express-service

```

3. Check Application Load Balancer target group health:

```

aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:region:account:targetgroup/name/id

```

4. Ensure the application is listening on the correct port inside the container.

## Performance issues

### Slow response times

**Symptoms:** Application responses are slower than expected.

**Diagnostic approach:**

1. Monitor CPU and memory utilization:

```

# Check CloudWatch metrics for the service
aws cloudwatch get-metric-statistics \
    --namespace AWS/ECS \
    --metric-name CPUUtilization \
    --dimensions Name=ServiceName,Value=my-express-service Name=ClusterName,Value=my-cluster \
    --start-time 2024-01-01T00:00:00Z \
    --end-time 2024-01-01T01:00:00Z \
    --period 300 \
    --statistics Average

```

2. Review application logs for errors or performance warnings.
3. Check if auto scaling is responding appropriately to load.
4. Analyze load balancer metrics for request distribution.

**Optimization strategies:**

- Increase CPU or memory allocation if resources are constrained.
- Adjust auto scaling thresholds to scale out earlier.
- Optimize application code and database queries.

### Auto scaling not working as expected

**Symptoms:** The service doesn't scale up during high load or doesn't scale down during low load.

**Troubleshooting steps:**

1. Check auto scaling policies and their configuration:

```

aws application-autoscaling describe-scaling-policies \
    --service-namespace ecs \
    --resource-id service/my-cluster/my-express-service

```

2. Review CloudWatch metrics to ensure scaling triggers are being met.
3. Verify that the service has permission to scale (check IAM roles).
4. Check for any scaling activities and their outcomes.

## Monitoring and debugging tools

### Using CloudWatch Container Insights

Enable Container Insights for comprehensive monitoring:

```

aws ecs put-account-setting --name containerInsights --value enabled

```

Container Insights provides:

- CPU, memory, disk, and network metrics
- Performance monitoring dashboards
- Log correlation and analysis
- Anomaly detection
