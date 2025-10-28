# Configure a custom domain name for your Classic Load Balancer

Each Classic Load Balancer receives a default Domain Name System (DNS) name. This DNS name includes
the name of the AWS Region in which the load balancer is created. For example, if you
create a load balancer named `my-loadbalancer` in the US West (Oregon)
Region, your load balancer receives a DNS name such as
`my-loadbalancer-1234567890.us-west-2.elb.amazonaws.com`. To access the
website on your instances, you paste this DNS name into the address field of a web
browser. However, this DNS name is not easy for your customers to remember and
use.

If you'd prefer to use a friendly DNS name for your load balancer, such as
`www.example.com`, instead of the default DNS name, you can create a
custom domain name and associate it with the DNS name for your load balancer. When a
client makes a request using this custom domain name, the DNS server resolves it to the
DNS name for your load balancer.

###### Contents

- [Associating your custom domain name with
  your load balancer name](#dns-associate-custom-elb "#dns-associate-custom-elb")
- [Using Route 53 DNS failover for your load
  balancer](#configure-dns-failover "#configure-dns-failover")
- [Disassociating your custom domain name
  from your load balancer](#dns-disassociate-custom-elb "#dns-disassociate-custom-elb")

## Associating your custom domain name with

your load balancer name

First, if you haven't already done so, register your domain name. The Internet
Corporation for Assigned Names and Numbers (ICANN) manages domain names on the
internet. You register a domain name using a _domain name
registrar_, an ICANN-accredited organization that manages the registry
of domain names. The website for your registrar will provide detailed instructions
and pricing information for registering your domain name. For more information, see
the following resources:

- To use Amazon Route 53 to register a domain name, see [Registering domain names using
  Route 53](../../../Route53/latest/DeveloperGuide/registrar.md "../../../Route53/latest/DeveloperGuide/registrar.md") in the _Amazon Route 53 Developer Guide_.
- For a list of accredited registrars, see the [List of Accredited Registrars](https://www.icann.org/en/accredited-registrars "https://www.icann.org/en/accredited-registrars").

Next, use your DNS service, such as your domain registrar, to create a CNAME
record to route queries to your load balancer. For more information, see the
documentation for your DNS service.

Alternatively, you can use Route 53 as your DNS service. You create a
_hosted zone_, which contains information about how to route
traffic on the internet for your domain, and an _alias resource record
set_, which routes queries for your domain name to your load balancer.
Route 53 doesn't charge for DNS queries for alias record sets, and you can use alias
record sets to route DNS queries to your load balancer for the zone apex of your
domain (for example, `example.com`). For information about transferring
DNS services for existing domains to Route 53, see [Configuring Route 53 as your DNS
service](../../../Route53/latest/DeveloperGuide/dns-configuring.md "../../../Route53/latest/DeveloperGuide/dns-configuring.md") in the _Amazon Route 53 Developer Guide_.

Finally, create a hosted zone and an alias record set for your domain using Route 53.
For more information, see [Routing traffic to a load
balancer](../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md "../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md") in the _Amazon Route 53 Developer Guide_.

## Using Route 53 DNS failover for your load

balancer

If you use Route 53 to route DNS queries to your load balancer, you can also
configure DNS failover for your load balancer using Route 53. In a failover
configuration, Route 53 checks the health of the registered EC2 instances for the load
balancer to determine whether they are available. If there are no healthy EC2
instances registered with the load balancer, or if the load balancer itself is
unhealthy, Route 53 routes traffic to another available resource, such as a healthy
load balancer or a static website in Amazon S3.

For example, suppose that you have a web application for
`www.example.com`, and you want redundant instances running behind
two load balancers residing in different Regions. You want the traffic to be
primarily routed to the load balancer in one Region, and you want to use the load
balancer in the other Region as a backup during failures. If you configure DNS
failover, you can specify your primary and secondary (backup) load balancers. Route 53
directs traffic to the primary load balancer if it is available, or to the secondary
load balancer otherwise.

###### Using evaluate target health

- When evaluate target health is set to `Yes` on an alias
  record for a Classic Load Balancer, Route 53 evaluates the health of the resource specified
  by the `alias target` value. For a Classic Load Balancer, Route 53 uses the instance
  health checks associated with the load balancer.
- When at least one of the registered instances in a Classic Load Balancer is healthy,
  Route 53 marks the alias record as healthy. Route 53 then returns records according
  to your routing policy. If the failover routing policy is used, Route 53 returns
  the primary record.
- When all the registered instances for a Classic Load Balancer are unhealthy, Route 53 marks
  the alias record as unhealthy. Route 53 then returns records according to your
  routing policy. If the failover routing policy is used, then Route 53 returns
  the secondary record.

For more information, see [Configuring DNS failover](../../../Route53/latest/DeveloperGuide/dns-failover-configuring.md "../../../Route53/latest/DeveloperGuide/dns-failover-configuring.md") in the
_Amazon Route 53 Developer Guide_.

## Disassociating your custom domain name

from your load balancer

You can disassociate your custom domain name from a load balancer instance by
first deleting the resource record sets in your hosted zone and then deleting the
hosted zone. For more information, see [Editing records](../../../Route53/latest/DeveloperGuide/resource-record-sets-editing.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-editing.md") and
[Deleting a public hosted
zone](../../../Route53/latest/DeveloperGuide/DeleteHostedZone.md "../../../Route53/latest/DeveloperGuide/DeleteHostedZone.md") in the _Amazon Route 53 Developer Guide_.
