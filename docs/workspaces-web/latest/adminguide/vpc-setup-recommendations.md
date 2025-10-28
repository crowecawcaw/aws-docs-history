# VPC best practices for WorkSpaces Secure Browser

The following recommendations can help you configure your VPC more effectively and
securely.

**Overall VPC Configuration**

- Make sure that your VPC configuration can support your scaling needs.
- Make sure that your WorkSpaces Secure Browser service quotas (also referred to as limits) are sufficient
  to support your anticipated demand. To request a quota increase, you can use the Service
  Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For information about default WorkSpaces Secure Browser
  quotas, see [Managing service quotas for your portal in Amazon WorkSpaces Secure Browser](request-service-quota.md "request-service-quota.md").
- If you plan to provide your streaming sessions with access to the internet, we
  recommend that you configure a VPC with a NAT gateway in a public subnet.
  **Elastic Network Interfaces**

- Each WorkSpaces Secure Browser session requires its own elastic network interface during the streaming
  duration. WorkSpaces Secure Browser creates as many [elastic
  network interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") (ENIs) as the maximum desired capacity of your fleet. By
  default, the limit for ENIs per Region is 5000. For more information, see [Network interfaces](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-enis "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-enis").

When planning capacity for very large deployments, for example, thousands of
concurrent streaming sessions, consider the number of ENIs that might be required for
your peak usage. We recommend that you keep your ENI limit at or above the max
concurrent usage limit you configure for your web portal.
**Subnets**

- As you develop your plan to scale up users, keep in mind that each WorkSpaces Secure Browser session
  requires a unique client IP address from your configured subnets. Therefore, the size of
  the client IP address space configured on your subnets determines the number of users
  who can stream concurrently.
- We recommend each subnet is configured with a subnet mask that allows for enough
  client IP addresses to account for the maximum number of expected concurrent users. In
  addition, consider adding additional IP addresses to account for anticipated growth. For
  more information, see [VPC and
  Subnet Sizing for IPv4](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4").
- We recommend that you configure a subnet in each unique Availability Zone that WorkSpaces Secure Browser
  supports in your desired region for availability and scaling consideration. For more
  information, see [Creating a new VPC for Amazon WorkSpaces Secure Browser](create-vpc.md "create-vpc.md").
- Make sure that the network resources required for your web applications are
  accessible through your subnets.
  **Security Groups**

- Use security groups to provide additional access control to your VPC.

Security groups that belong to your VPC let you control the network traffic between
WorkSpaces Secure Browser streaming instances and network resources required by web applications. Make sure
that the security groups provide access to the network resources that your web
applications require.
