# Resource types and ARN formats

in ARC

When you create a resource set in Amazon Application Recovery Controller (ARC), you specify the type of resource to include in the set and Amazon
Resource Names (ARNs) for each of the resources to include. ARC expects a specific ARN format for each resource type.
This section lists the resource types supported by ARC and the associated ARN formats for each one.

The specific format depends on the resource. When you provide an ARN, replace the `italicized` text
with your resource-specific information.

###### Note

Be aware that the ARN format that ARC requires for resources might differ from the ARN format that a service itself requires for its resources. For
example, the ARN formats that are described in the **Resource type** sections for each service in the [Service Authorization Reference](../../../service-authorization/latest/reference/reference.md "../../../service-authorization/latest/reference/reference.md") might not include the AWS account ID or other
information that ARC needs to support features in the ARC service.

**AWS::ApiGateway::Stage**
An Amazon API Gateway Version 1 stage.

- **ARN format:** `arn:`partition`:apigateway:`region`:`account`:/restapis/`api-id`/stages/`stage-name``

Example: `arn:aws:apigateway:us-east-1:111122223333:/restapis/123456789/stages/ExampleStage`

For more information, see [API Gateway Amazon Resource Name (ARN) reference](../../../apigateway/latest/developerguide/arn-format-reference.md "../../../apigateway/latest/developerguide/arn-format-reference.md").

**AWS::ApiGatewayV2::Stage**
An Amazon API Gateway Version 2 stage.

- **ARN format:** `arn:`partition`:apigateway:`region`:`account`:/apis/`api-id`/stages/`stage-name``

Example: `arn:aws:apigateway:us-east-1:111122223333:/apis/123456789/stages/ExampleStage`

For more information, see [API Gateway Amazon Resource Name (ARN) reference](../../../apigateway/latest/developerguide/arn-format-reference.md "../../../apigateway/latest/developerguide/arn-format-reference.md").

**AWS::CloudWatch::Alarm**
An Amazon CloudWatch alarm.

- **ARN format:** `arn:`partition`:cloudwatch:`region`:`account`:alarm:`alarm-name``

Example: `arn:aws:cloudwatch:us-west-2:111122223333:alarm:test-alarm-1`

For more information, see [Resource types defined by
Amazon CloudWatch](../../../service-authorization/latest/reference/list_amazoncloudwatch.md#amazoncloudwatch-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazoncloudwatch.md#amazoncloudwatch-resources-for-iam-policies").

**AWS::DynamoDB::Table**
An Amazon DynamoDB table.

- **ARN format:** `arn:`partition`:dynamodb:`region`:`account`:table/`table-name``

Example: `arn:aws:dynamodb:us-west-2:111122223333:table/BigTable`

For more information, see [DynamoDB resources and operations](../../../amazondynamodb/latest/developerguide/access-control-overview.md#access-control-resources "../../../amazondynamodb/latest/developerguide/access-control-overview.md#access-control-resources").

**AWS::EC2::CustomerGateway**
A customer gateway device.

- **ARN format:** `arn:`partition`:ec2:`region`:`account`:customer-gateway/`CustomerGatewayId``

Example: `arn:aws:ec2:us-west-2:111122223333:customer-gateway/vcg-123456789`

For more information, see [Resource types
defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

**AWS::EC2::Volume**
An Amazon EBS volume.

- **ARN format:** `arn:`partition`:ec2:`region`:`account`:volume/`VolumeId``

Example: `arn:aws:ec2:us-west-2:111122223333:volume/volume-of-cylinder-is-pi`

For more information, see [API Gateway Amazon Resource Name (ARN) reference](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

**AWS::ElasticLoadBalancing::LoadBalancer**
A Classic Load Balancer.

- **ARN format:** `arn:`partition`:elasticloadbalancing:`region`:`account`:loadbalancer/`LoadBalancerName``

Example: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/123456789abcbdeCLB`

For more information, see [Elastic Load Balancing resources](../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources "../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources").

**AWS::ElasticLoadBalancingV2::LoadBalancer**
A Network Load Balancer or an Application Load Balancer.

- **ARN format for Network Load Balancer:** `arn:`partition`:elasticloadbalancing:`region`:`account`:loadbalancer/net/`LoadBalancerName``

Example for Network Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/net/sandbox-net/123456789acbdeNLB`

- **ARN format for Application Load Balancer:** `arn:`partition`:elasticloadbalancing:`region`:`account`:loadbalancer/app/`LoadBalancerName``

Example for Application Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/app/sandbox-alb/123456789acbdeALB`

For more information, see [Elastic Load Balancing resources](../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources "../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources").

**AWS::Lambda::Function**
An AWS Lambda function.

- **ARN format:** `arn:`partition`:lambda:`region`:`account`:function:`FunctionName``

Example: `arn:aws:lambda:us-west-2:111122223333:function:my-function`

For more information, see [Resources and conditions for Lambda actions](../../../lambda/latest/dg/lambda-api-permissions-ref.md "../../../lambda/latest/dg/lambda-api-permissions-ref.md").

**AWS::MSK::Cluster**
An Amazon MSK cluster.

- **ARN format:** `arn:`partition`:kafka:`region`:`account`:cluster/`ClusterName`/`UUID``

Example: `arn:aws:kafka:us-east-1:111122223333:cluster/demo-cluster-1/123456-1111-2222-3333`

For more information, see [Resource
types defined by Amazon Managed Streaming for Apache Kafka](../../../service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.md#amazonmanagedstreamingforapachekafka-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.md#amazonmanagedstreamingforapachekafka-resources-for-iam-policies").

**AWS::RDS::DBCluster**
An Aurora DB cluster.

- **ARN format:** `arn:`partition`:rds:`region`:`account`:cluster:`DbClusterInstanceName``

Example: `arn:aws:rds:us-west-2:111122223333:cluster:database-1`

For more information, see [Working with Amazon Resource Names (ARNs) in Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md").

**AWS::Route53::HealthCheck**
An Amazon Route 53 health check.

- **ARN format:** `arn:`partition`:route53:::healthcheck/`Id``

Example: `arn:aws:route53:::healthcheck/123456-1111-2222-3333`

**AWS::SQS::Queue**
An Amazon SQS queue.

- **ARN format:** `arn:`partition`:sqs:`region`:`account`:`QueueName``

Example: `arn:aws:sqs:us-west-2:111122223333:StandardQueue`

For more information, see [Amazon Simple Queue Service resource and operations](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.md#sqs-resource-and-operations "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.md#sqs-resource-and-operations").

**AWS::SNS::Topic**
An Amazon SNS topic.

- **ARN format:** `arn:`partition`:sns:`region`:`account`:`TopicName``

Example: `arn:aws:sns:us-west-2:111122223333:TopicName`

For more information, see [Amazon SNS resource ARN format](../../../sns/latest/dg/sns-using-identity-based-policies.md#sns-arn-format "../../../sns/latest/dg/sns-using-identity-based-policies.md#sns-arn-format").

**AWS::SNS::Subscription**
An Amazon SNS subscription.

- **ARN format:** `arn:`partition`:sns:`region`:`account`:`TopicName`:`SubscriptionId``

Example: `arn:aws:sns:us-west-2:111122223333:TopicName:123456789012345567890`

**AWS::EC2::VPC**
A virtual private cloud (VPC).

- **ARN format:** `arn:`partition`:ec2:`region`:`account`:vpc/`VpcId``

Example: `arn:aws:ec2:us-west-2:111122223333:vpc/vpc-123456789`

For more information, see [VPC Resources](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

**AWS::EC2::VPNConnection**
A virtual private network (VPN) connection.

- **ARN format:** `arn:`partition`:ec2:`region`:`account`:vpn-connection/`VpnConnectionId``

Example: `arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-123456789`

For more information, see [Resource types
defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

**AWS::EC2::VPNGateway**
A virtual private network (VPN) gateway.

- **ARN format:** `arn:`partition`:ec2:`region`:`account`:vpn-gateway/`VpnGatewayId``

Example: `arn:aws:ec2:us-west-2:111122223333:vpn-gateway/vgw-123456789acbdefgh`

For more information, see [Resource types defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

**AWS::Route53RecoveryReadiness::DNSTargetResource**
A DNS target resource for readiness checks includes the DNS record type, domain name, Route 53 hosted zone ARN, and Network Load Balancer ARN or Route 53 record set ID.

- **ARN format for hosted zone:** `arn:`partition`:route53::`account`:hostedzone/`Id``

Example for a hosted zone: `arn:aws:route53::111122223333:hostedzone/abcHostedZone`

NOTE: You must include the account ID in hosted zone ARNs, as specified here. The account ID is required so
that ARC can poll the resource. The format is intentionally different from the ARN format
that Amazon Route 53 requires, described in the Route 53 service [Resource types](../../../service-authorization/latest/reference/list_amazonroute53.md#amazonroute53-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonroute53.md#amazonroute53-resources-for-iam-policies")
in the _Service Authorization Reference_.

- **ARN format for Network Load Balancer:** `arn:`partition`:elasticloadbalancing:`region`:`account`:loadbalancer/net/`LoadBalancerName``

Example for Network Load Balancer: `arn:aws:elasticloadbalancing:us-west-2:111122223333:loadbalancer/net/sandbox-net/123456789acbdefgh`

For more information, see [Elastic Load Balancing resources](../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources "../../../elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.md#elb-resources").
