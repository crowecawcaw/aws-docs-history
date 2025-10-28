# Routing traffic to an AWS Global Accelerator

AWS Global Accelerator is a service in which you create accelerators to improve the performance of your
applications for local and global users. The service reacts instantly to changes in
health or configuration to ensure that internet traffic from clients is always directed
to healthy endpoints. Global Accelerator includes a fault tolerant architecture, and incorporates
AWS Shield Standard, for automated in-line mitigation from DDoS attacks. For more information,
see [What is
Global Accelerator](../../../global-accelerator/latest/dg/what-is-global-accelerator.md "../../../global-accelerator/latest/dg/what-is-global-accelerator.md") in the AWS Global Accelerator Developer Guide.

By default, Global Accelerator provides you with static IP addresses that you associate with your accelerator.
The static IP addresses are anycast from the AWS edge network. Accelerators include a deafult DNS name,
but in most scenarios, you can configure DNS to use your custom domain name (such as www.example.com) with your
accelerator, instead of using the assigned static IP addresses or the default DNS name.

###### Note

Route 53 doesn't charge for alias queries to Global Accelerator or other AWS
resources.

## Prerequisites

To get started, you need the following:

- An accelerator. You can create either a standard accelerator, or a custom routing
  accelerator. For more information, see [Create a standard accelerator](../../../global-accelerator/latest/dg/about-accelerators.md "../../../global-accelerator/latest/dg/about-accelerators.md") and [Create a custom routing accelerator](../../../global-accelerator/latest/dg/about-custom-routing-accelerators.md "../../../global-accelerator/latest/dg/about-custom-routing-accelerators.md").
- A registered domain name. You can use Amazon Route 53 as your domain registrar,
  or you can use a different registrar.
- Route 53 as the DNS service for the domain. If you register your domain name
  by using Route 53, we automatically configure Route 53 as the DNS service for the
  domain.

For information about using Route 53 as the DNS service provider for your
domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").

## Configuring Amazon Route 53 to route

traffic to an accelerator

To configure Amazon Route 53 to route traffic to an accelerator, perform the following
procedure.

###### To route traffic to an

accelerator

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the name of the hosted zone that matches the name of the domain
   that you want to route traffic for.
4. Choose **Create record**.
5. Specify the following values:

**Routing policy**

Choose the applicable routing policy. For more information,
see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to your accelerator. The
default value is the name of the hosted zone.

For example, if the name of the hosted zone is example.com and
you want to use acme.example.com to route traffic to your Global Accelerator, enter **acme**.

**Value/Route traffic to**

Choose **Alias to Global Accelerator**, then choose
the AWS Region. Choose the DNS name for the accelerator.

You can enter the DNS name of an accelerator that you created using the current AWS account
or using a different AWS account.

**Record type**

Accept the default value, **A – IPv4
address**.

**Evaluate target health**

Accept the default value of **Yes**. 6. Choose **Create records**.

Changes generally propagate to all Route 53 servers within 60 seconds. When propagation is
done, you'll be able to route traffic to your accelerator by using the name
of the alias record that you created in this procedure.
