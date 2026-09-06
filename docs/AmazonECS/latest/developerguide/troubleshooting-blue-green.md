

# Troubleshooting Amazon ECS blue/green deployments
<a name="troubleshooting-blue-green"></a>

This following provides solutions for common issues you might encounter when using blue/green deployments with Amazon ECS. Blue/green deployment errors can occur during the following phases:
+ *Synchronous path*: Errors that appear immediately in response to `CreateService` or `UpdateService` API calls.
+ *Asynchronous path*: Errors that appear in the `statusReason` field of `DescribeServiceDeployments` and cause a deployment rollback

**Tip**  
You can use the [Amazon ECS MCP server](ecs-mcp-introduction.md) with AI assistants to monitor deployments and troubleshoot deployment issues using natural language.

## Load balancer configuration issues
<a name="troubleshooting-blue-green-load-balancer"></a>

Load balancer configuration is a critical component of blue/green deployments in Amazon ECS. Proper configuration of listener rules, target groups, and load balancer types is essential for successful deployments. This section covers common load balancer configuration issues that can cause blue/green deployments to fail.

When troubleshooting load balancer issues, it's important to understand the relationship between listener rules and target groups. In a blue/green deployment:
+ The production listener rule directs traffic to the currently active (blue) service revision
+ The test listener rule can be used to validate the new (green) service revision before shifting production traffic
+ Target groups are used to register the container instances from each service revision
+ During deployment, traffic is gradually shifted from the blue service revision to the green service revision by adjusting the weights of the target groups in the listener rules

### Listener rule configuration errors
<a name="troubleshooting-blue-green-listener-rules"></a>

The following issues relate to incorrect listener rule configuration for blue/green deployments.

Using an Application Load Balancer listener ARN instead of a listener rule ARN  
*Error message*: `productionListenerRule has an invalid ARN format. Must be RuleArn for ALB or ListenerArn for NLB. Got: arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-alb/abc123/def456`  
*Solution*: When using an Application Load Balancer, you must specify a listener rule ARN for `productionListenerRule` and `testListenerRule`, not a listener ARN. For Network Load Balancers, you must use the listener ARN.  
 For information about how to find the listener ARN, see [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) in the *Application Load Balancer User Guide*. The ARN for a rule has the format `{{arn:aws:elasticloadbalancing:region:account-id:listener-rule/app/...}}`.

Using the same rule for both production and test listeners  
*Error message*: `The following rules cannot be used as both production and test listener rules: arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-alb/abc123/def456/ghi789`  
*Solution*: You must use different listener rules for production and test traffic. Create a separate listener rule for test traffic that routes to your test target group.

Target group not associated with listener rules  
*Error message*: `Service deployment rolled back because of invalid networking configuration: Target group arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/myAlternateTG/abc123 is not associated with either productionListenerRule or testListenerRule.`  
*Solution*: Both the primary target group and alternate target group must be associated with either the production listener rule or the test listener rule. Update your load balancer configuration to ensure both target groups are properly associated with your listener rules.

Missing test listener rule with an Application Load Balancer  
*Error message*: `For Application LoadBalancer, testListenerRule is required when productionListenerRule is not associated with both targetGroup and alternateTargetGroup`  
*Solution*: When you use an Application Load Balancer, if both target groups are not associated with the production listener rule, you must specify a test listener rule. Add a `testListenerRule` to your configuration and ensure both target groups are associated with either the production or test listener rule. For more information, see [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) in the *Application Load Balancer User Guide*.

### Target group configuration errors
<a name="troubleshooting-blue-green-target-groups"></a>

The following issues relate to incorrect target group configuration for blue/green deployments.

Multiple target groups with traffic in listener rule  
*Error message*: `Service deployment rolled back because of invalid networking configuration. productionListenerRule arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-alb/abc123/def456/ghi789 should have exactly one target group serving traffic but found 2 target groups which are serving traffic`  
*Solution*: Before starting a blue/green deployment, ensure that only one target group is receiving traffic (has a non-zero weight) in your listener rule. Update your listener rule configuration to set the weight to zero for any target group that should not be receiving traffic.

Duplicate target groups across load balancer entries  
*Error message*: `Duplicate targetGroupArn found: arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/myecs-targetgroup/abc123`  
*Solution*: Each target group ARN must be unique across all load balancer entries in your service definition. Review your configuration and ensure you're using different target groups for each load balancer entry.

Unexpected target group in production listener rule  
*Error message*: `Service deployment rolled back because of invalid networking configuration. Production listener rule is forwarding traffic to unexpected target group arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/random-nlb-tg/abc123. Expected traffic to be forwarded to either targetGroupArn: arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/nlb-targetgroup/def456 or alternateTargetGroupArn: arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/nlb-tg-alternate/ghi789`  
*Solution*: The production listener rule is forwarding traffic to a target group that is not specified in your service definition. Ensure that the listener rule is configured to forward traffic only to the target groups specified in your service definition.   
For more information, see [forward actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#forward-actions) in the *Application Load Balancer User Guide*.

### Load balancer type configuration errors
<a name="troubleshooting-blue-green-load-balancer-types"></a>

The following issues relate to incorrect load balancer type configuration for blue/green deployments.

Mixing Classic Load Balancer and Application Load Balancer or Network Load Balancer configurations  
*Error message*: `All loadBalancers must be strictly either ELBv1 (defining loadBalancerName) or ELBv2 (defining targetGroupArn)`  
Classic Load Balancers are the previous generation of load balancers from Elastic Load Balancing. We recommend that you migrate to a current generation load balancer. For more information, see [Migrate your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/migrate-classic-load-balancer.html).
*Solution*: . Use either all Classic Load Balancers or all Application Load Balancers and Network Load Balancers.  
For Application Load Balancers and Network Load Balancers, specify only the `targetGroupArn` field.

Using advanced configuration with a Classic Load Balancer  
*Error message*: `advancedConfiguration field is not allowed with ELBv1 loadBalancers`  
*Solution*: Advanced configuration for blue/green deployments is only supported with Application Load Balancers and Network Load Balancers. If you use a Classic Load Balancer (specified with `loadBalancerName`), you cannot use the `advancedConfiguration` field. Either switch to an Application Load Balancer, or remove the `advancedConfiguration` field.

Inconsistent advanced configuration across load balancers  
*Error message*: `Either all or none of the provided loadBalancers must have advancedConfiguration defined`  
*Solution*: If you're using multiple load balancers, you must either define `advancedConfiguration` for all of them or for none of them. Update your configuration to ensure consistency across all load balancer entries.

Missing advanced configuration with blue/green deployment  
*Error message*: `advancedConfiguration field is required for all loadBalancers when using a non-ROLLING deployment strategy`  
*Solution*: When using a blue/green deployment strategy with Application Load Balancers, you must specify the `advancedConfiguration` field for all load balancer entries. Add the required `advancedConfiguration` to your load balancer configuration.

## Permission issues
<a name="troubleshooting-blue-green-permissions"></a>

The following issues relate to insufficient permissions for blue/green deployments.

Missing trust policy on infrastructure role  
*Error message*: `Service deployment rolled back because of invalid networking configuration. ECS was unable to manage the ELB resources due to missing permissions on ECS Infrastructure Role 'arn:aws:iam::123456789012:role/Admin'.`  
*Solution*: The IAM role specified for managing load balancer resources does not have the correct trust policy. Update the role's trust policy to allow the service to assume the role. The trust policy must include:    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Missing read permissions on load balancer role  
*Error message*: `service myService failed to describe target health on target-group myTargetGroup with (error User: arn:aws:sts::123456789012:assumed-role/myELBRole/ecs-service-scheduler is not authorized to perform: elasticloadbalancing:DescribeTargetHealth because no identity-based policy allows the elasticloadbalancing:DescribeTargetHealth action)`  
*Solution*: The IAM role used for managing load balancer resources does not have permission to read target health information. Add the `elasticloadbalancing:DescribeTargetHealth` permission to the role's policy. For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md).

Missing write permissions on load balancer role  
*Error message*: `service myService failed to register targets in target-group myTargetGroup with (error User: arn:aws:sts::123456789012:assumed-role/myELBRole/ecs-service-scheduler is not authorized to perform: elasticloadbalancing:RegisterTargets on resource: arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/myTargetGroup/abc123 because no identity-based policy allows the elasticloadbalancing:RegisterTargets action)`  
*Solution*: The IAM role used for managing load balancer resources does not have permission to register targets. Add the `elasticloadbalancing:RegisterTargets` permission to the role's policy. For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md).

Missing permission to modify listener rules  
*Error message*: `Service deployment rolled back because TEST_TRAFFIC_SHIFT lifecycle hook(s) failed. User: arn:aws:sts::123456789012:assumed-role/myELBRole/ECSNetworkingWithELB is not authorized to perform: elasticloadbalancing:ModifyListener on resource: arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-alb/abc123/def456 because no identity-based policy allows the elasticloadbalancing:ModifyListener action`  
*Solution*: The IAM role used for managing load balancer resources does not have permission to modify listeners. Add the `elasticloadbalancing:ModifyListener` permission to the role's policy. For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md).

For blue/green deployments, we recommend attaching the `AmazonECS-ServiceLinkedRolePolicy` managed policy to your infrastructure role, which includes all the necessary permissions for managing load balancer resources.

## Lifecycle hook issues
<a name="troubleshooting-blue-green-lifecycle-hooks"></a>

The following issues relate to lifecycle hooks in blue/green deployments.

Incorrect trust policy on Lambda hook role  
*Error message*: `Service deployment rolled back because TEST_TRAFFIC_SHIFT lifecycle hook(s) failed. ECS was unable to assume role arn:aws:iam::123456789012:role/Admin`  
*Solution*: The IAM role specified for the Lambda lifecycle hook does not have the correct trust policy. Update the role's trust policy to allow the service to assume the role. The trust policy must include:    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Lambda hook returns FAILED status  
*Error message*: `Service deployment rolled back because TEST_TRAFFIC_SHIFT lifecycle hook(s) failed. Lifecycle hook target arn:aws:lambda:us-west-2:123456789012:function:myHook returned FAILED status.`  
*Solution*: The Lambda function specified as a lifecycle hook returned a FAILED status. Check the Lambda function logs in Amazon CloudWatch logs to determine the failure reason, and update the function to handle the deployment event correctly.

Missing permission to invoke Lambda function  
*Error message*: `Service deployment rolled back because TEST_TRAFFIC_SHIFT lifecycle hook(s) failed. ECS was unable to invoke hook target arn:aws:lambda:us-west-2:123456789012:function:myHook due to User: arn:aws:sts::123456789012:assumed-role/myLambdaRole/ECS-Lambda-Execution is not authorized to perform: lambda:InvokeFunction on resource: arn:aws:lambda:us-west-2:123456789012:function:myHook because no identity-based policy allows the lambda:InvokeFunction action`  
*Solution*: The IAM role used for the Lambda lifecycle hook does not have permission to invoke the Lambda function. Add the `lambda:InvokeFunction` permission to the role's policy for the specific Lambda function ARN. For information about Lambda permissions, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md).

Lambda function timeout or invalid response  
*Error message*: `Service deployment rolled back because TEST_TRAFFIC_SHIFT lifecycle hook(s) failed. ECS was unable to parse the response from arn:aws:lambda:us-west-2:123456789012:function:myHook due to HookStatus must not be null`  
*Solution*: The Lambda function either timed out or returned an invalid response. Ensure that your Lambda function returns a valid response with a `hookStatus` field set to either `SUCCEEDED` or `FAILED`. Also, check that the Lambda function timeout is set appropriately for your validation logic. For more information, see [Lifecycle hooks for Amazon ECS service deployments](deployment-lifecycle-hooks.md).  
Example of a valid Lambda response:  

```
{
  "hookStatus": "SUCCEEDED",
  "reason": "Validation passed"
}
```

Invalid targetType for lifecycle hook  
*Error message*: `Invalid targetType. Valid values are: AWS_LAMBDA, PAUSE`  
*Solution*: Check the `targetType` field in your lifecycle hook configuration. Valid values are `AWS_LAMBDA` and `PAUSE`.

Invalid lifecycle stage for pause hook  
*Error message*: `Invalid lifecycle stage provided for Pause Hook`  
*Solution*: Pause hooks can only be configured at `PRE_SCALE_UP`, `POST_SCALE_UP`, `POST_TEST_TRAFFIC_SHIFT`, `PRE_PRODUCTION_TRAFFIC_SHIFT`, or `POST_PRODUCTION_TRAFFIC_SHIFT`. You cannot use `TEST_TRAFFIC_SHIFT` or `PRODUCTION_TRAFFIC_SHIFT` for pause hooks.

Pause hook timed out  
*Error message*: `Service deployment rolled back because POST_TEST_TRAFFIC_SHIFT pause hook timed out.`  
*Solution*: The pause hook timed out before a `ContinueServiceDeployment` call was received. Verify that your automation or approval workflow is calling `ContinueServiceDeployment` before the configured timeout expires. Check the `expiresAt` field in `DescribeServiceDeployments` to see when the hook was set to expire. If you need more time, increase the `timeoutInMinutes` value in the pause hook configuration (maximum 20,160 minutes / 14 days). If you want the deployment to continue automatically on timeout instead of rolling back, set the `timeoutConfiguration.action` to `CONTINUE`.

Invalid hookId format  
*Error message*: `Invalid hookId: hookId must follow the format: ecs-{hookType}-{id}`  
*Solution*: The `hookId` provided to `ContinueServiceDeployment` does not match the expected format. Retrieve the correct `hookId` by calling `DescribeServiceDeployments` and checking the `lifecycleHookDetails` array. Do not construct hookIds manually.

hookId not found or expired  
*Error message*: `Provided hookId is either completed, unavailable, or not associated with the given Resource ARN`  
*Solution*: The `hookId` is no longer valid. This can happen if the hook already timed out, was already continued or rolled back, a new deployment was triggered (invalidating previous hookIds), or the hookId belongs to a different service deployment ARN. Retrieve the current `hookId` by calling `DescribeServiceDeployments` on the active deployment.

Deployment in terminal state  
*Error message*: `Continuing a service deployment is not allowed for service deployment in terminal states.`  
*Solution*: The deployment has already completed, rolled back, or stopped. You can only call `ContinueServiceDeployment` on a deployment that is `IN_PROGRESS` with a pause hook in `AWAITING_ACTION` status. Use `DescribeServiceDeployments` to check the current deployment status.

Service deployment not found  
*Error message*: `The service deployment does not exist.`  
*Solution*: The `serviceDeploymentArn` provided does not match any existing service deployment. Use `ListServiceDeployments` to find the correct ARN.