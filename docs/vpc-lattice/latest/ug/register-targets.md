

# Register targets with a VPC Lattice target group
<a name="register-targets"></a>

Your service serves as a single point of contact for clients and distributes incoming traffic across its healthy registered targets. You can register each target with one or more target groups.

If demand on your application increases, you can register additional targets with one or more target groups to handle the demand. The service starts routing requests to a newly registered target as soon as the registration process completes and the target passes the initial health checks.

If demand on your application decreases, or you need to service your targets, you can deregister targets from your target groups. Deregistering a target removes it from your target group, but does not affect the target otherwise. The service stops routing requests to a target as soon as it is deregistered. The target enters the `DRAINING` state until in-flight requests have completed. You can register the target with the target group again when you are ready for it to resume receiving requests.

The target type of your target group determines how you register targets with that target group. For more information, see [Target type](target-groups.md#target-type).

Use the following console procedures to register or deregister targets. Alternatively, use the [register-targets](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/register-targets.html) and [deregister-targets](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/deregister-targets.html) commands from the AWS CLI.

**Topics**
+ [Register or deregister targets by instance ID](#register-instances)
+ [Register or deregister targets by IP address](#register-ip-addresses)
+ [Register or deregister a Lambda function](#register-lambda-function)
+ [Register or deregister an Application Load Balancer](#register-alb)

## Register or deregister targets by instance ID
<a name="register-instances"></a>

The target instances must be in the virtual private cloud (VPC) that you specified for the target group. The instance must also be in the `running` state when you register it.

When you register targets by instance ID, you can use your service with an Auto Scaling group. After you attach a target group to an Auto Scaling group and the group scales out, the instances that the Auto Scaling group launches are automatically registered with the target group. If you detach the target group from the Auto Scaling group, the instances are automatically deregistered from the target group. For more information, see [Routing traffic to your Auto Scaling group with a VPC Lattice target group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-lattice.html) in the *Amazon EC2 Auto Scaling User Guide*.

**To register or deregister targets by instance ID using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, under **VPC Lattice**, choose **Target groups**.

1. Choose the name of the target group to open its details page.

1. Choose the **Targets** tab.

1. To register instances, choose **Register targets**. Select the instances, enter the instance port, and then choose **Include as pending below**. When you are finished adding instances, choose **Register targets**.

1. To deregister instances, select the instances, and then choose **Deregister**.

## Register or deregister targets by IP address
<a name="register-ip-addresses"></a>

The target IP addresses must be from the subnets of the VPC that you specified for the target group. You can't register the IP addresses of another service in the same VPC. You can't register VPC endpoints or publicly routable IP addresses.

**To register or deregister targets by IP address using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, under **VPC Lattice**, choose **Target groups**.

1. Choose the name of the target group to open its details page.

1. Choose the **Targets** tab.

1. To register IP addresses, choose **Register targets**. For each IP address, select the network, enter the IP address and port, and choose **Include as pending below**. When you are finished specifying addresses, choose **Register targets**.

1. To deregister IP addresses, select the IP addresses and then choose **Deregister**.

## Register or deregister a Lambda function
<a name="register-lambda-function"></a>

You can register a single Lambda function with the target group. If you no longer need to send traffic to your Lambda function, you can deregister it. After you deregister a Lambda function, in-flight requests fail with HTTP 5XX errors. It is better to create a new target group instead of replacing the Lambda function for a target group. 

**To register or deregister a Lambda function using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, under **VPC Lattice**, choose **Target groups**.

1. Choose the name of the target group to open its details page.

1. Choose the **Targets** tab.

1. If there is no Lambda function registered, choose **Register target**. Select the Lambda function and choose **Register target**.

1. To deregister a Lambda function, choose **Deregister**. When prompted for confirmation, enter **confirm** and then choose **Deregister**.

## Register or deregister an Application Load Balancer
<a name="register-alb"></a>

You can register a single Application Load Balancer with each target group. If you no longer need to send traffic to your load balancer, you can deregister it. After you deregister a load balancer, in-flight requests fail with HTTP 5XX errors. It is better to create a new target group instead of replacing the Application Load Balancer for a target group.

**To register or deregister an Application Load Balancer using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, under **VPC Lattice**, choose **Target groups**.

1. Choose the name of the target group to open its details page.

1. Choose the **Targets** tab.

1. If there is no Application Load Balancer registered, choose **Register target**. Select the Application Load Balancer and choose **Register target**.

1. To deregister an Application Load Balancer, choose **Deregister**. When prompted for confirmation, enter **confirm** and then choose **Deregister**.