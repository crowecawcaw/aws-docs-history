# Enabling access logs for Amazon ECS Service Connect

Access logs are not enabled by default for Amazon ECS services that use Service Connect. You can enable
access logs in the following ways.

## Enable access logs using the AWS CLI

The following command shows how you can enable access logs for an Amazon ECS
service using the AWS CLI by specifying a `accessLogConfiguration` when you create the service:

```
`aws ecs create-service \
 --cluster my-cluster \
 --service-name my-service \
 --task-definition my-task-def \
 --service-connect-configuration '{
 "enabled": true,
 "namespace": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcdef1234567890",
 "services": [{
 "portName": "web",
 "discoveryName": "my-service",
 "clientAliases": [{
 "port": 80,
 "dnsName": "my-service"
 }]
 }],
 "logConfiguration": {
 "logDriver": "awslogs",
 "options": {
 "awslogs-group": "my-envoy-log-group",
 "awslogs-region": "us-west-2",
 "awslogs-stream-prefix": "myapp-envoy-logs"
 }
 },
 "accessLogConfiguration": {
 "format": "TEXT",
 "includeQueryParameters": "ENABLED"
 }
 }'`
```

## Enable access logs using the console

For
a detailed service creation procedure, see [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md "create-service-console-v2.md").

###### To create a service with a shared namespace using the AWS Management Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster that you
   want to create the service in.
3. Under **Services**, choose
   **Create**.
4. After filling in other details depending on your workload, in the
   **Service Connect** section, choose **Use
   Service Connect**.
5. Configure Service Connect settings as needed for your
   service type (client or client-server).
6. Expand **Access log configuration**. For **Format**, choose either **JSON** or `TEXT`.
7. To include query parameters in access logs, select **Include query parameters**.
8. Complete the service creation process.
