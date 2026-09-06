# Update the TCP idle timeout for your Gateway Load Balancer listener

For each TCP request made through a Gateway Load Balancer, the state of that connection
is tracked. If no data is sent through the connection by either the client or target for
longer than the idle timeout, the connection is closed. The default idle timeout value
for TCP flows is 350 seconds, but can be updated to any value between 60-6000 seconds.

- If you set the idle timeout higher than 350 seconds, verify that
  your targets' ENI connection tracking idle timeout
  (`TcpEstablishedTimeout`) is equal to or greater than the
  Gateway Load Balancer idle timeout value. On Nitro V6+ instances, the default
  connection tracking timeout is 350 seconds. A mismatch causes the
  target's network interface to silently drop connection state before
  the load balancer closes the connection. For more information, see
  [Best
  Practices for TCP Connection Management on EC2](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-tcp-connection-management-on-ec2/ "https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-tcp-connection-management-on-ec2/").

###### To update the TCP idle timeout using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the Gateway Load Balancer.
4. On the listeners tab choose **Actions**, **View listener details**.
5. On the listener details page, in the **Attributes** tab, select
   **Edit**.
6. On the **Edit listener attributes** page, in the **Listener
   attributes** section, enter a value for **TCP idle timeout**.
7. Choose **Save changes**

###### To update the TCP idle timeout using the AWS CLI

Use the [modify-listener-attributes](../../../cli/latest/reference/elbv2/modify-listener-attributes.md "../../../cli/latest/reference/elbv2/modify-listener-attributes.md") command with the
`tcp.idle_timeout.seconds` attribute.

## Send TCP reset on idle timeout

When enabled, the Gateway Load Balancer sends a TCP reset (RST) to the sender of traffic
when the idle timeout expires. This helps signal traffic senders to immediately
terminate idle connections. To control this behavior, use the
`send_tcp_reset.on_idle_timeout.enabled` attribute.

###### To enable Send TCP reset on idle timeout using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select your Gateway Load Balancer.
4. On the **Listeners** tab, choose **Actions**, **View listener details**.
5. On the listener details page, on the **Attributes** tab, choose
   **Edit**.
6. Choose **Send TCP reset on idle timeout**.
7. Choose **Save changes**.

###### To enable Send TCP reset on idle timeout using the AWS CLI

Use the [modify-listener-attributes](../../../cli/latest/reference/elbv2/modify-listener-attributes.md "../../../cli/latest/reference/elbv2/modify-listener-attributes.md") command with the
`send_tcp_reset.on_idle_timeout.enabled` attribute set to
`true`.

```
`aws elbv2 modify-listener-attributes --listener-arn `listener-arn` --attributes Key=send_tcp_reset.on_idle_timeout.enabled,Value=true`
```
