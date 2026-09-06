

# Update the target group for your Gateway Load Balancer listener
<a name="update-target-group"></a>

When you create a listener, you specify a rule for routing requests. This rule forwards requests to the specified target group. You can update the listener rule to forward requests to a different target group.

**To update your listener using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the load balancer and choose **Listeners**.

1. Choose **Edit listener**.

1. For **Forwarding to target group**, choose a target group.

1. Choose **Save**.

**To update your listener using the AWS CLI**  
Use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command.