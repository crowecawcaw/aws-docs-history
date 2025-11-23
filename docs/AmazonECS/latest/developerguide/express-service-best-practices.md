# Best practices for Amazon ECS Express Mode services

Learn about best practices and recommendations for using Express Mode service effectively in production environments.

## Security best practices

### Secrets management

- **Use Secrets Manager for secrets** - Store sensitive data in Secrets Manager (e.g. private repository or database
  credentials).

For more information Secrets Manager best practices, see [Secrets Manager best practices](secretsmanager/latest/userguide/best-practices.md "secretsmanager/latest/userguide/best-practices.md")
in the _Secrets Manager User Guide_

- **Enable encryption at rest** - Ensure secrets are encrypted when stored in AWS services.

Using a service such as Secrets Manager allows you to encrypt using either an AWS managed or customer provided key.

- **Implement secret rotation** - Use automatic rotation for database passwords and API keys.

Using a service such as Secrets Manager can manage secret rotation for services like Amazon Aurora and Amazon RDS

Example of using secrets in Express Mode service:

```

aws ecs update-express-gateway-service \
    --primary-container \
        ‘{“environment”=[{“name”=“DB_PASSWORD”,”value”=“arn:aws:secretsmanager:us-west-2:123456789012:secret:prod/db/password”}, \
        {“name”=“API_KEY”,”value”=“arn:aws:ssm:us-west-2:123456789012:parameter/prod/api-key”}]}’ \

```

### Network security

- **Use private subnets for sensitive applications** - Deploy applications that don't need direct internet access in private subnets.

For more information on recommended architectures, refer to [Connect Amazon ECS application to the internet.](AmazonECS/latest/developerguide/networking-outbound.md "AmazonECS/latest/developerguide/networking-outbound.md")

- **Configure security groups to be minimally permissive** - Restrict inbound and outbound traffic to only necessary ports and sources.

To restrict the outbound traffic of the Express Mode Service Security Group, you can edit this directly in Amazon EC2 Security Groups Console by modifying the Outbound
rules, or use the following commands:

```

aws ec2 authorize-security-group-egress
    --group-id sg-xxxxxxxx \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0

aws ec2 revoke-security-group-egress
    --group-id sg-xxxxxxxx \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0

```

- **Enable Amazon VPC Flow Logs** - Monitor network traffic for security analysis and troubleshooting.

You can enable this in each subnet in use by your Express Mode applications in the VPC Subnet Console, or use `aws ec2 create-flow-logs --resource-ids subnet-xxx`

- **Use AWS WAF for web applications** - Protect against common web exploits and attacks.

You can enable this by creating a Web ACL and then associating it to the Application Load Balancer used by your Express Mode service. In Console, Create a web ACL in the WAF & Shield
Service and associate to your Application Load Balancer. Or, use `aws wafv2 create-web-acl` and `aws wafv2 associate-web-acl --resource-arn <alb>`.

## Performance and Compute optimization

### Resource sizing

- **Right-size CPU and memory** - Monitor application performance and adjust CPU and memory allocations based on actual usage patterns.

AWS Compute Optimizer generates recommendations for Amazon ECS task and container sizes. For more information, see [What is
AWS Compute Optimizer?](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md") in the _AWS Compute Optimizer User Guide_.

- **Performance test your application** - To ensure your application operates at scale and with the given scaling thresholds and resources
  allocations, perform load testing.

### Auto scaling configuration

- **Set appropriate scaling thresholds** - Configure CPU or memory thresholds that trigger scaling before performance degrades.

You can modify the service metric's target value in your Express Mode service console.

Consider adding a predictive scaling policy, especially if your traffic follows a time-based pattern. See [Predictive Auto Scaling](AWSEC2ContainerServiceDocs/latest/shared/predictive-auto-scaling.md "AWSEC2ContainerServiceDocs/latest/shared/predictive-auto-scaling.md") for more information.

- **Use multiple scaling metrics** - Consider using both CPU or Memory and request-based scaling for more responsive scaling.

You can add multiple policies to a service. Express Mode adds one by default, but you can attach addtional policies to your service directly.

- **Configure minimum and maximum limits of tasks** - Set reasonable bounds to control costs and ensure availability.

For production workloads, once initial testing is complete - we recommend running in three availability zones to follow availability best practices.
You can update the **Minimum number of tasks** in the Express Mode Console, or by using `update-express-gateway-service 
 --scaling-target '{“minTaskCount”=3}'`.

### Health checks

- **Implement meaningful health checks** - Create health check endpoints that verify critical application dependencies.

You can update the **Health check path** in the Express Mode Console. Or by using `update-express-gateway-service --health-check-path "/health"`.

For more information on forming health checks for your application, refer to [Implementing Health Checks](https://d1.awsstatic.com/builderslibrary/pdfs/implementing-health-checks.pdf "https://d1.awsstatic.com/builderslibrary/pdfs/implementing-health-checks.pdf")

- **Keep health checks lightweight** - Avoid expensive operations in health check endpoints.

Examples might include external API calls, CPU or memory intensive opeartions, or long running operations with the potention to timeout.

- **Use appropriate timeouts** - Configure health check timeouts that allow for normal response times while detecting failures quickly.

Health check timeouts for Express Mode can be configured on the Application Load Balancer target group. In the Amazon EC2 Console, Navigate to the **Target Groups** section and
select your Express Mode target group. Select the **Health Checks** Tab and click **Edit**, under **Advanced health
check settings** you can adjust the timeout. Or, use `aws elbv2 modify-target-group --target-group-arn <targetgroup> --health-check-timeout`.

- **Return proper HTTP status codes** - Use 200 for healthy and 4xx/5xx for unhealthy states.

## Operational best practices

### Monitoring and logging

- **Enable Enhanced Container Insights** - Use CloudWatch; Enhanced Container Insights for comprehensive monitoring of your Express Mode service applications.

See [Setting up Container Insights on Amazon ECS](AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md "AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md") for more information.

- **Set up custom metrics** - Publish application-specific metrics to CloudWatch; for business logic monitoring.

See [Public custom metrics](AmazonCloudWatch/latest/monitoring/publishingMetrics.md "AmazonCloudWatch/latest/monitoring/publishingMetrics.md") in the _CloudWatch User Guide_ for more information.

- **Configure log retention** - Set appropriate log retention periods to balance cost and compliance requirements.

CloudWatch Log Groups created by Express Mode are configured to never expire and are retained when the Express Mode service is deleted. You can adjust this setting in the CloudWatch Log Group.

- **Create dashboards and alerts** - Set up CloudWatch; dashboards and alarms for proactive monitoring.

### Deployment strategies

- **Implement bake times** - Express Mode implements a canary bake time to ensure deployments have time to stabilize
  while reducing blast radius of problematic deployments. If your application needs more time to stabilize, this can be configured in the Amazon ECS Service definition of your
  Express Mode service. Refer to [Creating an Amazon ECS canary deployment](AmazonECS/latest/developerguide/deploy-canary-service.md "AmazonECS/latest/developerguide/deploy-canary-service.md") for more details.
- **Implement rollback procedures** - Have a plan to quickly revert to previous versions if issues occur.

Meaningful health checks and alarm based rollbacks can both help with rollback. Express Mode's canary deployment strategy combined with alarm based rollbacks
on 4xx and 5xx traffic sets up your deployments for fast rollbacks in the event of faulty application code or configuration.
