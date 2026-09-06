

# Delete a listener for your Network Load Balancer
<a name="delete-listener"></a>

Before you delete a listener, consider the impact on your application:
+ [TCP and TLS listeners] The load balancer immediately stops accepting new connections on the listener. Any TLS handshakes in progress might fail. Existing connections remain open until they naturally close or time out. In-flight requests on existing connections complete successfully.
+ [UDP and QUIC listeners] Any packets in transit might not reach their destination.

------
#### [ Console ]

**To delete a listener**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the check box for load balancer.

1. On the **Listeners and rules** tab, select the check box for the listener, and then choose **Actions**, **Delete listener**.

1. When prompted for confirmation, enter **confirm** and choose **Delete**.

------
#### [ AWS CLI ]

**To delete a listener**  
Use the [delete-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-listener.html) command.

```
aws elbv2 delete-listener \
    --listener-arn {{listener-arn}}
```

------