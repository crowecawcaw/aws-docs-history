# Migrate your Classic Load Balancer

Elastic Load Balancing supports the following types of load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and Classic Load Balancers.
For information about the different features of each load balancer type, see [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/ "https://aws.amazon.com/elasticloadbalancing/features/").

You can also choose to migrate an existing Classic Load Balancer in a VPC, to an Application Load Balancer or a Network Load Balancer.

## Benefits of migrating from a Classic Load Balancer

Each type of load balancer has its own unique features, functions, and configurations.
Review the benefits of each load balancer to help decide which one is best for you.

Application Load Balancer
**Using an Application Load Balancer instead of a Classic Load Balancer has the following benefits:**

Support for:

- [Path conditions](../application/load-balancer-listeners.md#path-conditions "../application/load-balancer-listeners.md#path-conditions"),
  [Host conditions](../application/load-balancer-listeners.md#host-conditions "../application/load-balancer-listeners.md#host-conditions"), and
  [HTTP header conditions](../application/load-balancer-listeners.md#http-header-conditions "../application/load-balancer-listeners.md#http-header-conditions").
- Redirecting requests from one URL to another, and routing requests to multiple applications on a single EC2 instance.
- Returning custom HTTP responses.
- Registering targets by IP address, and registering Lambda functions as targets. Including targets outside the VPC for the load balancer.
- Authenticating users through corporate or social identities.
- Amazon Elastic Container Service (Amazon ECS) containerized applications.
- Independently monitoring the health of each service.

Access logs contain additional information and are stored in a compressed format.

Improved load balancer performance overall.

Network Load Balancer
**Using a Network Load Balancer instead of a Classic Load Balancer has the following benefits:**

Support for:

- Static IP addresses, which allow assigning one Elastic IP address per subnet enabled for the load balancer.
- Registering targets by IP address, including targets outside the VPC
  for the load balancer.
- Routing requests to multiple applications on a single EC2 instance.
- Amazon Elastic Container Service (Amazon ECS) containerized applications.
- Independently monitoring the health of each service.

Ability to handle volatile workloads and scale to millions of requests per second.

## Migrate using migration wizard

Migration wizard uses the configuration of your Classic Load Balancer to create an equivalent Application Load Balancer or Network Load Balancer. It reduces
the time and effort required to migrate a Classic Load Balancer compared to other methods.

###### Note

The wizard creates a new load balancer. The wizard doesn't convert the existing Classic Load Balancer to an Application Load Balancer or Network Load Balancer.
You must manually redirect the traffic to the newly created load balancer.

###### Limitations

- The name of the new load balancer can't be the same as an existing load balancer of the same type, in the same region.
- If the Classic Load Balancer has any tags containing the `aws:` prefix in their key, those tags are not migrated.

###### When migrating to an Application Load Balancer

- If the Classic Load Balancer has only one subnet, you must specify a second subnet.
- If the Classic Load Balancer has HTTP/HTTPS listeners that use TCP health checks, the health check protocol is
  updated to HTTP and the path is set to "/".
- If the Classic Load Balancer has HTTPS listeners using a custom or unsupported security policy, migration
  wizard uses the default security policy for the new load balancer type.

###### When migrating to a Network Load Balancer

- The following instance types will not be registered with the new target group: C1, CC1, CC2,
  CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, T1
- Certain health check settings from your Classic Load Balancer may not be transferrable to the new target group.
  These cases will be indicated as a change in the summary section of the migration wizard.
- If the Classic Load Balancer has SSL listeners, migration wizard creates a TLS listener using the
  certificate and security policy from the SSL listener.

###### To migrate a Classic Load Balancer using migration wizard

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the Classic Load Balancer you want to migrate.
4. In the load balancers **Details** section, choose
   **Launch migration wizard**.
5. Choose **Migrate to Application Load Balancer**, or **Migrate to
   Network Load Balancer**, to open migration wizard.
6. Under **Name new load balancer**, for **Load balancer name**
   enter a name for your new load balancer.
7. Under **Name new target group and review targets**, for
   **Target group name** enter a name for your new target group.
8. (Optional) Under **Targets**, you can review the target instances
   that will be registered with the new target group.
9. (Optional) Under **Review tags**, you can review the tags that
   will be applied to your new load balancer
10. Under **Summary for Application Load Balancer**, or **Summary for Network Load Balancer**,
    review and verify the configuration options assigned by migration wizard.
11. After you're satisfied with the configuration summary, choose
    **Create Application Load Balancer**, or **Create Network Load Balancer**, to start the migration.

## Migrate using the load balancer copy utility

The load balancer copy utilities are available within the Elastic Load Balancing Tools repository, on the AWS GitHub page.

###### Resources

- [Elastic Load Balancing Tools](https://github.com/aws/elastic-load-balancing-tools "https://github.com/aws/elastic-load-balancing-tools")
- [Classic Load Balancer to Application Load Balancer copy utility](https://github.com/aws/elastic-load-balancing-tools/tree/master/application-load-balancer-copy-utility "https://github.com/aws/elastic-load-balancing-tools/tree/master/application-load-balancer-copy-utility")
- [Classic Load Balancer to Network Load Balancer copy utility](https://github.com/aws/elastic-load-balancing-tools/tree/master/network-load-balancer-copy-utility "https://github.com/aws/elastic-load-balancing-tools/tree/master/network-load-balancer-copy-utility")

## Migrate your load balancer manually

The following information provides general instructions for manually creating a
new Application Load Balancer or Network Load Balancer based on an existing Classic Load Balancer in a VPC. You can migrate using the
AWS Management Console, the AWS CLI, or an AWS SDK. For more information, see [Getting started with Elastic Load Balancing](load-balancer-getting-started.md "load-balancer-getting-started.md").

After you have completed the migration process, you can take advantage of the features of
your new load balancer.

###### Step 1: Create a new load balancer

Create a load balancer with a configuration that is equivalent to the Classic Load Balancer to migrate.

1. Create a new load balancer, with the same scheme (internet-facing or
   internal), subnets, and security groups as the Classic Load Balancer.
2. Create one target group for your load balancer, with the same health check settings
   that you have for your Classic Load Balancer.
3. Do one of the following:
   - If your Classic Load Balancer is attached to an Auto Scaling group, attach your target group to the Auto Scaling group.
     This also registers the Auto Scaling instances with the target group.
   - Register your EC2 instances with your target group.

4. Create one or more listeners, each with a default rule that forwards
   requests to the target group. If you create an HTTPS listener, you can
   specify the same certificate that you specified for your Classic Load Balancer. We recommend
   that you use the default security policy.
5. If your Classic Load Balancer has tags, review them and add the relevant tags to your new load
   balancer.

###### Step 2: Gradually redirect traffic to your new load

balancer

After your instances are registered with your new load balancer, you can begin the
process of redirecting traffic from the old load balancer to the new load balancer.
This enables you to test your new load balancer while minimizing risk to the availability
of your application.

###### To redirect traffic gradually to your new load balancer

1. Paste the DNS name of your new load balancer into the address field of an
   internet-connected web browser. If everything is working, the browser displays
   the default page of your application.
2. Create a new DNS record that associates your domain name with your new load
   balancer. If your DNS service supports weighting, specify a weight of 1 in the
   new DNS record and a weight of 9 in the existing DNS record for your old load
   balancer. This directs 10% of the traffic to the new load balancer and 90% of
   the traffic to the old load balancer.
3. Monitor your new load balancer to verify that it is receiving traffic and
   routing requests to your instances.

###### Important

The time-to-live (TTL) in the DNS record is 60 seconds. This means that
any DNS server that resolves your domain name keeps the record information
in its cache for 60 seconds, while the changes propagate. Therefore, these
DNS servers can still route traffic to your old load balancer for up to 60
seconds after you complete the previous step. During propagation, traffic
could be directed to either load balancer. 4. Continue to update the weight of your DNS records until all traffic is
directed to your new load balancer. When you are finished, you can delete the
DNS record for your old load balancer.

###### Step 3: Update policies, scripts, and code

If you migrated your Classic Load Balancer to an Application Load Balancer or Network Load Balancer, be sure to do the following:

- Update IAM policies that use API version 2012-06-01 to use version 2015-12-01.
- Update processes that use CloudWatch metrics in the `AWS/ELB` namespace to use metrics
  from the `AWS/ApplicationELB` or `AWS/NetworkELB` namespace.
- Update scripts that use **aws elb** AWS CLI commands to use
  **aws elbv2** AWS CLI commands.
- Update CloudFormation templates that use the `AWS::ElasticLoadBalancing::LoadBalancer`
  resource to use the `AWS::ElasticLoadBalancingV2` resources.
- Update code that uses Elastic Load Balancing API version 2012-06-01 to use version 2015-12-01.

###### Resources

- [elbv2](../../../cli/latest/reference/elbv2/index.md "../../../cli/latest/reference/elbv2/index.md") in the _AWS CLI Command Reference_
- [Elastic Load Balancing API Reference version 2015-12-01](../APIReference.md "../APIReference.md")
- [Identity and access management
  for Elastic Load Balancing](load-balancer-authentication-access-control.md "load-balancer-authentication-access-control.md")
- [Application Load Balancer metrics](../application/load-balancer-cloudwatch-metrics.md#load-balancer-metrics-alb "../application/load-balancer-cloudwatch-metrics.md#load-balancer-metrics-alb")
  in the _User Guide for Application Load Balancers_
- [Network Load Balancer metrics](../network/load-balancer-cloudwatch-metrics.md#load-balancer-metrics-nlb "../network/load-balancer-cloudwatch-metrics.md#load-balancer-metrics-nlb")
  in the _User Guide for Network Load Balancers_
- [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md")
  in the _AWS CloudFormation User Guide_

###### Step 4: Delete the old load balancer

You can delete the old Classic Load Balancer after:

- You have redirected all traffic from the old load balancer to the new load
  balancer.
- All existing requests that were routed to the old load balancer have
  completed.

## Prevent users from creating Classic Load Balancers

You can create an IAM policy that prevents users from creating Classic Load Balancers in your account.

Both the [Elastic Load Balancing V2](../../../service-authorization/latest/reference/list_awselasticloadbalancingv2.md "../../../service-authorization/latest/reference/list_awselasticloadbalancingv2.md") and
[Elastic Load Balancing V1](../../../service-authorization/latest/reference/list_awselasticloadbalancing.md "../../../service-authorization/latest/reference/list_awselasticloadbalancing.md") APIs provide a
`CreateLoadBalancer` API action. When you create a Classic Load Balancer, you use the V1 API action,
which creates both the load balancer and listeners. When you create an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer,
you use the V2 API action, which creates only the load balancer. The V2 API provides a
`CreateListener` action, which you use to create listeners for a load balancer
after you create it.

The following policy denies users permission to create a load balancer if the listener
protocol is specified. Because you must configure at least one listener when you create a Classic Load Balancer,
this policy prevents users from creating Classic Load Balancers. It does not prevent users from creating
other types of load balancers, because there are separate API actions for creating those
load balancers and their listeners.

```
{
    "Version": "2012-10-17",
    "Effect": "Deny",
    "Action": "elasticloadbalancing:CreateLoadBalancer",
    "Resource": [
        "arn:aws:elasticloadbalancing:*:*:loadbalancer/*"
    ],
    "Condition": {
        "Null": {
            "elasticloadbalancing:ListenerProtocol": false
        }
    }
}
```
