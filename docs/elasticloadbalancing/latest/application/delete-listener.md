

# Delete a listener for your Application Load Balancer
<a name="delete-listener"></a>

Before you delete a listener, consider the impact on your application:
+ The load balancer immediately stops accepting new connections on the listener port.
+ Active connections are closed. Any requests in progress when the listener is deleted will likely fail.

------
#### [ Console ]

**To delete a listener**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer.

1. On the **Listeners and rules** tab, select the check box for the listener and choose **Manage listener**, **Delete listener**.

1. When prompted for confirmation, enter **confirm** and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a listener**  
Use the [delete-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-listener.html) command.

```
aws elbv2 delete-listener \
    --listener-arn {{listener-arn}}
```

------