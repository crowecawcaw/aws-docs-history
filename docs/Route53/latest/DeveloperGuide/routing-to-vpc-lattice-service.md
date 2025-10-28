# Routing traffic to Amazon VPC Lattice service domain endpoint

Amazon VPC Lattice is a fully managed application networking service that you use to connect, secure, and monitor
the services and resources for your application. You can use VPC Lattice with a single virtual private cloud (VPC) or
across multiple VPCs from one or more accounts. For more information, see [What is Amazon VPC Lattice](../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md "../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md") in the _Amazon VPC Lattice User
Guide_.

## Prerequisites

To get started, you need the following:

A VPC Lattice service domain that has a custom domain name, such as example.com that matches the name of
the Route 53 record that you want to create.

For more information, see [Associate a custom domain name with your service](../../../vpc-lattice/latest/ug/service-custom-domain-name.md "../../../vpc-lattice/latest/ug/service-custom-domain-name.md") in the
_Amazon VPC Lattice User Guide_.

## Configuring Amazon Route 53 to route

traffic to a VPC Lattice service domain endpoint

To use Route 53 to route traffic to Amazon VPC Lattice service domain, you first get the domain service endpoint provided by VPC Lattice.
For more information, see [Associate a custom domain name with your service](../../../vpc-lattice/latest/ug/service-custom-domain-name.md "../../../vpc-lattice/latest/ug/service-custom-domain-name.md") in the
_Amazon VPC Lattice User Guide_.

###### To route traffic to VPC Lattice service domain endpoint

1. Go to [https://aws.amazon.com](https://aws.amazon.com "https://aws.amazon.com") and
   choose **Sign In to the Console**.
2. Under **Networking & Content Delivery**, choose
   **VPC**.
3. Under **PrivateLink and Lattice** choose **Lattice Services**.
4. Create a VPC Lattice service or select an existing VPC Lattice service.

###### Note

When creating a VPC Lattice service, you must specify a custom domain configuration and supply
a custom domain name. If you choose an existing service, it must also have a custom domain. 5. Under **Domain configuration**, copy the value for the custom domain name. 6. Open the Route 53 console at
[https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/"). 7. In the navigation pane, choose **Hosted zones**. 8. Choose the linked name of the hosted zone for the domain that you want to use to route
traffic to your VPC Lattice service domain endpoint. The domain name must match the custom domain endpoint
defined in VPC Lattice. 9. Choose **Create record**.

You can use the wizard to create the records or choose **Switch to
quick create**. 10. Specify the following values:

**Routing policy**

Choose the applicable routing policy. For more information,
see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to
your VPC Lattice service domain endpoint. The default value is the name of the
hosted zone.

For example, if the name of the hosted zone is example.com and
you want to use **acme.example.com** to route
traffic to your distribution, enter
**acme**.

**Alias**

If you are using the **Quick create** record
creation method, turn on **Alias**.

**Value/Route traffic to**

Choose **Alias to VPC Lattice service**. Choose the Region that the
VPC Lattice service domain was created in, and choose the value that you got
in step 5.

**Record type**

Choose **A – IPv4 address**, **AAAA – IPv6 address**, or
both for dual-stack.

**Evaluate target health**

Choose **No**. For information about
evaluating target health, see [Evaluate target
health](resource-record-sets-values-alias.md#rrsets-values-alias-evaluate-target-health "resource-record-sets-values-alias.md#rrsets-values-alias-evaluate-target-health"). 11. Choose **Create records**.
