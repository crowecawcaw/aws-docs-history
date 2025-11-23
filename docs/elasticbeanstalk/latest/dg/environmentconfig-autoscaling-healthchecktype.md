# Amazon EC2 Auto Scaling health check setting for your Elastic Beanstalk environment

Amazon EC2 Auto Scaling monitors the health of each Amazon Elastic Compute Cloud (Amazon EC2) instance that it launches. If any instance terminates unexpectedly, Amazon EC2 Auto Scaling detects the termination and
launches a replacement instance. By default, the Amazon EC2 Auto Scaling group created for your environment uses [Amazon EC2 status
checks](../../../autoscaling/latest/userguide/healthcheck.md "../../../autoscaling/latest/userguide/healthcheck.md"). If an instance in your environment fails an Amazon EC2 status check, Amazon EC2 Auto Scaling takes it down and replaces it.

Amazon EC2 status checks only cover an instance's health, not the health of your application, server, or any Docker containers running on the instance. If your
application crashes, but the instance that it runs on is still healthy, it may be kicked out of the load balancer, but Amazon EC2 Auto Scaling won't replace it automatically.
The default behavior is good for troubleshooting. If Amazon EC2 Auto Scaling replaced the instance as soon as the application crashed, you might not realize that anything went
wrong, even if it crashed quickly after starting up.

If you want Amazon EC2 Auto Scaling to replace instances whose application has stopped responding, you can use a [configuration file](ebextensions.md "ebextensions.md")
to configure the Amazon EC2 Auto Scaling group to use ELB health checks. The following example sets the group to use the load balancer's health checks, in addition to the
Amazon EC2 status check, to determine an instance's health.

###### Example .ebextensions/autoscaling.config

```
Resources:
  AWSEBAutoScalingGroup:
    Type: "AWS::AutoScaling::AutoScalingGroup"
    Properties:
      HealthCheckType: `ELB`
      HealthCheckGracePeriod: `300`
```

For more information about the `HealthCheckType` and `HealthCheckGracePeriod` properties, see [AWS::AutoScaling::AutoScalingGroup](../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-as-group.md") in the _AWS CloudFormation User Guide_ and [Health Checks for Amazon EC2 Auto Scaling Instances](../../../autoscaling/ec2/userguide/healthcheck.md "../../../autoscaling/ec2/userguide/healthcheck.md") in the _Amazon EC2 Auto Scaling User Guide_.

By default, the ELB health check is configured to attempt a TCP connection to your instance over port 80. This confirms that the web server running on
the instance is accepting connections. However, you might want to [customize the load balancer health
check](using-features.managing.md "using-features.managing.md") to ensure that your application, and not just the web server, is in a good state. The grace period setting sets the number of seconds that an
instance can fail the health check without being terminated and replaced. Instances can recover after being kicked out of the load balancer, so give the
instance an amount of time that is appropriate for your application.
