# Modifying the resources that Elastic Beanstalk

creates for your environment

The resources that Elastic Beanstalk creates for your environment have names. You can use these names to
get information about the resources with a [function](ebextensions-functions.md "ebextensions-functions.md"), or modify properties on the resources to customize their behavior. This
topic describes the AWS resources that Elastic Beanstalk uses in the different types of
environments.

###### Note

The previous topic
[Custom resources](environment-resources.md "environment-resources.md")
provides some uses cases and examples for customizing environment
resources. You can also find more examples of configuration files in the later topic [Custom resource examples](customize-environment-resources-examples.md "customize-environment-resources-examples.md").

Web server environments have the following resources.

###### Web server environments

- `AWSEBAutoScalingGroup` ([AWS::AutoScaling::AutoScalingGroup](../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-group.md")) – The Amazon EC2 Auto Scaling group attached to your
  environment.
- One of the following two resources.
  - `AWSEBAutoScalingLaunchConfiguration` ([AWS::AutoScaling::LaunchConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.md")) – The launch configuration
    attached to your environment's Amazon EC2 Auto Scaling group.
  - `AWSEBEC2LaunchTemplate` ([AWS::EC2::LaunchTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md")) – The Amazon EC2 launch template used by your
    environment's Amazon EC2 Auto Scaling group.

###### Note

If your environment uses functionality that requires Amazon EC2 launch templates, and your
user policy lacks the required permissions, creating or updating the environment might
fail. Use the **AdministratorAccess-AWSElasticBeanstalk**
[managed user policy](AWSHowTo.iam.md "AWSHowTo.iam.md"), or add the
required permissions to your [custom
policy](AWSHowTo.iam.md#AWSHowTo.iam.policies "AWSHowTo.iam.md#AWSHowTo.iam.policies").

- `AWSEBEnvironmentName` ([AWS::ElasticBeanstalk::Environment](../../../AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.md")) – Your environment.
- `AWSEBSecurityGroup` ([AWS::EC2::SecurityGroup](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.md")) – The security group attached to your Amazon EC2 Auto Scaling
  group.
- `AWSEBRDSDatabase` ([AWS::RDS::DBInstance](../../../AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.md")) – The Amazon RDS DB instance attached to your
  environment (if applicable).
  In a load-balanced environment, you can access additional resources related to the load
  balancer. Classic load balancers have a resource for the load balancer and one for the security
  group attached to it. Application and network load balancers have additional resources for the
  load balancer's default listener, listener rule, and target group.

###### Load-balanced environments

- `AWSEBLoadBalancer` ([AWS::ElasticLoadBalancing::LoadBalancer](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.md")) – Your environment's classic load
  balancer.
- `AWSEBV2LoadBalancer` ([AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md")) – Your environment's
  application or network load balancer.
- `AWSEBLoadBalancerSecurityGroup` ([AWS::EC2::SecurityGroup](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.md")) – In a custom [Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") (Amazon VPC) only, the name of the security group that Elastic Beanstalk creates for the
  load balancer. In a default VPC or EC2 classic, ELB assigns a default security group to
  the load balancer.
- `AWSEBV2LoadBalancerListener` ([AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.md")) – A listener that allows the load
  balancer to check for connection requests and forward them to one or more target
  groups.
- `AWSEBV2LoadBalancerListenerRule` ([AWS::ElasticLoadBalancingV2::ListenerRule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.md")) – Defines which requests an
  ELB listener takes action on and the action that it takes.
- `AWSEBV2LoadBalancerTargetGroup` ([AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.md")) – An ELB target group that
  routes requests to one or more registered targets, such as Amazon EC2 instances.
  Worker environments have resources for the SQS queue that buffers incoming requests, and a
  Amazon DynamoDB table that the instances use for leader election.

###### Worker environments

- `AWSEBWorkerQueue` ([AWS::SQS::Queue](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.md")) – The Amazon SQS queue from which the daemon pulls requests
  that need to be processed.
- `AWSEBWorkerDeadLetterQueue` ([AWS::SQS::Queue](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.md")) – The
  Amazon SQS queue that stores messages that cannot be delivered or otherwise were not successfully
  processed by the daemon.
- `AWSEBWorkerCronLeaderRegistry` ([AWS::DynamoDB::Table](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md"))
  – The Amazon DynamoDB table that is the internal registry used by the daemon for
  periodic tasks.
