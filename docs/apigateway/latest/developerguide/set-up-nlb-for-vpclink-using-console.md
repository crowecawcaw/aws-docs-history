# Set up a Network Load Balancer

for API Gateway private integrations

The following procedure outlines the steps to set up a Network Load Balancer (NLB)
for API Gateway private integrations using the Amazon EC2 console and provides references for
detailed instructions for each step.

For each VPC you have resources in, you only need to configure one NLB and one
VPCLink. The NLB supports multiple [listeners](../../../elasticloadbalancing/latest/network/load-balancer-listeners.md "../../../elasticloadbalancing/latest/network/load-balancer-listeners.md") and [target groups](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md") per NLB. You can configure each service as a specific
listener on the NLB and use a single VPCLink to connect to the NLB. When creating the
private integration in API Gateway you then define each service using the
specific port that is assigned for each service. For more information, see [Tutorial: Create a REST API with a private integration](getting-started-with-private-integration.md "getting-started-with-private-integration.md").

###### Note

The Network Load Balancer and API must be owned by the same AWS account.

###### To create a Network Load Balancer for private integration using the API Gateway

console

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Set up a web server on an Amazon EC2 instance. For an example setup, see [Installing a LAMP Web Server on Amazon Linux 2](../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md "../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md").
3. Create a Network Load Balancer, register the EC2 instance with a target
   group, and add the target group to a listener of the Network Load Balancer. For
   details, follow the instructions in [Getting Started with Network Load Balancers](../../../elasticloadbalancing/latest/network/network-load-balancer-getting-started.md "../../../elasticloadbalancing/latest/network/network-load-balancer-getting-started.md").
4. After the Network Load Balancer is created, do the following:
   1. Note the ARN of the Network Load Balancer. You will need it to
      create a VPC link in API Gateway for integrating the API with the VPC resources behind
      the Network Load Balancer.
   2. Turn off security group evaluation for PrivateLink.
      - To turn off security group evaluation for PrivateLink traffic using the console, you can choose the
        **Security** tab, and then **Edit**. In the **Security
        settings**, clear **Enforce inbound rules on PrivateLink traffic**.
      - Use the following [set-security-groups](../../../cli/latest/reference/elbv2/set-security-groups.md "../../../cli/latest/reference/elbv2/set-security-groups.md") command to turn
        off security group evaluation for PrivateLink traffic:

      ```
      aws elbv2 set-security-groups --load-balancer-arn `arn:aws:elasticloadbalancing:us-east-2:111122223333:loadbalancer/net/my-loadbalancer/abc12345` \
        --security-groups `sg-123345a` --enforce-security-group-inbound-rules-on-private-link-traffic off
      ```

###### Note

Do not add any dependencies to API Gateway CIDRs as they are bound to change without notice.
