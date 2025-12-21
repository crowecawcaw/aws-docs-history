# Adding an accelerator

when you create a load balancer

When you create an Application Load Balancer or Network Load Balancer in the AWS Management Console, you can optionally
[add an accelerator at the same time](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md"). ELB and Global Accelerator work together to transparently add the accelerator for you.
The accelerator is created in your account, with the load balancer as an endpoint. Using an accelerator provides static IP
addresses and improves the availability and performance of your applications. (Learn more about
accelerators by reading [What is AWS Global Accelerator?](what-is-global-accelerator.md "what-is-global-accelerator.md").)

###### Important

To create an accelerator, you must have the correct permissions in place. For more information,
see [Identity-based policy
examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

##

Configure and view your accelerator

You must update your DNS configuration
to direct traffic to the static IP addresses or DNS name for the accelerator. Traffic won't go through the accelerator to
your load balancer until your configuration changes are complete.

After you create your load balancer by choosing the Global Accelerator add-on on the Amazon EC2 console,
go to the **Integrated services**
tab to see the static IP addresses and Domain Name System (DNS) name for your accelerator. You use this information to
start routing user traffic to the load balancer over the AWS global network. For more information about the DNS name assigned
to your accelerator, see [DNS addressing and custom domains in AWS Global Accelerator](dns-addressing-custom-domains.md "dns-addressing-custom-domains.md").

You can view and configure your accelerator by [navigating to Global Accelerator](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:") in the AWS Management Console. For example, you can see the accelerators that are associated with your account or add additional load balancers to your
accelerator. For more information, see [View your accelerators](about-accelerators.md "about-accelerators.md") and [Create accelerator](about-accelerators.md "about-accelerators.md").

##

Pricing

With AWS Global Accelerator, you pay only for what you use. You are charged an hourly rate and data transfer costs for
each accelerator in your account. For more information, see [AWS Global Accelerator Pricing](https://aws.amazon.com/global-accelerator/pricing "https://aws.amazon.com/global-accelerator/pricing").

##

Stop using the accelerator

If you'd like to stop routing traffic through Global Accelerator to your load balancer, do the following:

1. Update your DNS configuration to point your traffic directly to the load balancer.
2. Delete the load balancer from the accelerator. For more information, see _To remove an
   endpoint_ in
   [Add a standard endpoint](about-endpoints-adding-endpoints.md "about-endpoints-adding-endpoints.md").
3. Delete the accelerator. For more
   information, see [Delete accelerator](about-accelerators.md "about-accelerators.md").
