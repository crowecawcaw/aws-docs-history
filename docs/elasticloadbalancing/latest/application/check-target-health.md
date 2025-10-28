# Check the health of your Application Load Balancer targets

You can check the health status of the targets registered with your target
groups. For help with health check failures, see [Troubleshooting: A registered target is not in service](load-balancer-troubleshooting.md#target-not-inservice "load-balancer-troubleshooting.md#target-not-inservice").

Console

###### To check the health of your targets

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. The **Details** tab displays the total number of
   targets, plus the number of targets for each health status.
5. On the **Targets** tab, the
   **Status** column indicates the status of each
   target.
6. If the status is any value other than `Healthy`, the
   **Status details** column contains more
   information.

###### To receive email notifications about unhealthy targets

Use CloudWatch alarms to trigger a Lambda function to send details about unhealthy
targets. For step-by-step instructions, see the following blog post: [Identifying unhealthy targets of your load balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/identifying-unhealthy-targets-of-elastic-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/identifying-unhealthy-targets-of-elastic-load-balancer/").

AWS CLI

###### To check the health of your targets

Use the [describe-target-health](../../../cli/latest/reference/elbv2/describe-target-health.md "../../../cli/latest/reference/elbv2/describe-target-health.md") command. This example filters the
output to include only targets that are not healthy. For targets that
are not healthy, the output includes a reason code.

```
aws elbv2 describe-target-health \
    --target-group-arn `target-group-arn` \
    --query "TargetHealthDescriptions[?TargetHealth.State!='healthy'].[Target.Id,TargetHealth.State,TargetHealth.Reason]" \
    --output table
```

The following is example output.

````
----------------------------------------------
|            DescribeTargetHealth            | +--------------+---------+-------------------+
|  172.31.0.57 |  unused |  Target.NotInUse  |
|  172.31.0.50 |  unused |  Target.NotInUse  | +--------------+---------+-------------------+ ``` ## Target states and reason codes The following list shows the possible reason codes for each target state. **Target state is healthy** A reason code is not provided. **Target state is initial** <br>• `Elb.RegistrationInProgress` - The target is in the process of being registered with the load balancer. <br>• `Elb.InitialHealthChecking` - The load balancer is still sending the target the minimum number of health checks required to determine its health status. **Target state is unhealthy** <br>• `Target.ResponseCodeMismatch` - The health checks did not return an expected HTTP code. <br>• `Target.Timeout` - The health check requests timed out. <br>• `Target.FailedHealthChecks` - The load balancer received an error while establishing a connection to the target or the target response was malformed. <br>• `Elb.InternalError` - The health checks failed due to an internal error. **Target state is unused** <br>• `Target.NotRegistered` - The target is not registered with the target group. <br>• `Target.NotInUse` - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer. <br>• `Target.InvalidState` - The target is in the stopped or terminated state. <br>• `Target.IpUnusable` - The target IP address is reserved for use by a load balancer. **Target state is draining** <br>• `Target.DeregistrationInProgress` - The target is in the process of being deregistered and the deregistration delay period has not expired. **Target state is unavailable** <br>• `Target.HealthCheckDisabled` - Health checks are disabled for the target group.
````
