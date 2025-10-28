# Delete a listener for your Network Load Balancer

Before you delete a listener, consider the impact on your application:

- [TCP and TLS listeners] The load balancer immediately stops accepting new
  connections on the listener. Any TLS handshakes in progress might fail. Existing
  connections remain open until they naturally close or time out. In-flight
  requests on existing connections complete successfully.
- [UDP listeners] Any packets in transit might not reach their
  destination.

Console

###### To delete a listener

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the check box for load balancer.
4. On the **Listeners** tab, select the check box for the listener,
   and then choose **Actions**, **Delete listener**.
5. When prompted for confirmation, enter `confirm` and choose
   **Delete**.

AWS CLI

###### To delete a listener

Use the [delete-listener](../../../cli/latest/reference/elbv2/delete-listener.md "../../../cli/latest/reference/elbv2/delete-listener.md") command.

```
aws elbv2 delete-listener \
    --listener-arn `listener-arn`
```
