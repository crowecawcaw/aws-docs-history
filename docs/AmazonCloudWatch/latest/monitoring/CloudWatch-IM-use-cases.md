# Internet Monitor example use cases

This section describes several specific examples of use cases for Internet Monitor, with links to blog posts with more details. These examples
illustrate how you can use the capabilities of Internet Monitor to monitor your application health and improve latency to enhance your users' experience.

**Set up alerts and decide on actions to take**

You can use Internet Monitor to get insights about average internet performance metrics over time, and about health events by city-network
(client location and ASN, typically an internet service provider). Using Internet Monitor, you can identify the events that are
impacting end user experience for applications hosted on Amazon Virtual Private Clouds (VPCs), Network Load Balancers, Amazon WorkSpaces, or Amazon CloudFront.

After you create a monitor, you have several options for how to be alerted about Internet Monitor health events. These include notifications
based on CloudWatch Alarms using event metrics or Amazon EventBridge rules to filter for health events. You can choose different options for
notifications or actions based on alarms, including, for example, AWS SMS notifications or updates to a CloudWatch log group.

To see an example with detailed guidance, see the following blog post: [Introducing Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-cloudwatch-internet-monitor/ "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-cloudwatch-internet-monitor/").

**Identify latency issues and improve TTFB to improve multiplayer gameplay experience**

Use Internet Monitor to help you to quickly identify where game players in global cloud gaming apps are experiencing latency issues globally,
and provide insights into improving performance. By identifying where the most players currently have the slowest time to first byte
(TTFB), you know how to improve latency to make your biggest player base happier.

Now, when you're ready to deploy the next EC2 server for your game, choose the AWS Region that Internet Monitor suggests will lower TTFB in the area with
the high latency and large group of players.

For details about setting up and using Internet Monitor for this use case, see the following blog post: [Using Internet Monitor for a Better Gaming
Experience](https://aws.amazon.com/blogs/gametech/using-cloudwatch-internet-monitor-for-a-better-gaming-experience/ "https://aws.amazon.com/blogs/gametech/using-cloudwatch-internet-monitor-for-a-better-gaming-experience/").

**Identify potential performance and internet connection issues for users on Amazon WorkSpaces**

Internet Monitor provides you with the IP prefixes and ASN (typically, the internet service provider or ISP) for your users,
which can be helpful to diagnose performance and internet connection issues for users to their WorkSpaces. You can also use this data to view your
fleet as a whole and monitor your WorkSpaces user connections.

For more information about how to use Internet Monitor for this use case, see the following blog post: [Using Internet Monitor
with Amazon WorkSpaces Personal](https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/").
