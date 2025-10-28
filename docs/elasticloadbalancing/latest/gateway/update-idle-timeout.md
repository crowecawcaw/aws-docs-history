# Update the TCP idle timeout for your Gateway Load Balancer listener

For each TCP request made through a Gateway Load Balancer, the state of that connection
is tracked. If no data is sent through the connection by either the client or target for
longer than the idle timeout, the connection is closed. The default idle timeout value
for TCP flows is 350 seconds, but can be updated to any value between 60-6000 seconds.

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
