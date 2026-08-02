# Configuring DNS routing for a new domain

To route internet traffic to your website or web application, you configure DNS routing for
your domain. The steps depend on whether you purchased your domain from Route 53 or from
another registrar.

## Set up DNS for a domain you purchased from Route 53

When you register a domain with Route 53, Route 53 makes itself the DNS service for the domain. It creates a hosted zone
with the same name as the domain, assigns four name servers to the zone, and updates the domain to use those name servers.

## Set up DNS for a domain you purchased from another registrar

When you buy a domain from another registrar, for example, because the top-level
domain (TLD) isn't offered by Route 53, you have two options:

- **Use Route 53 for DNS hosting only:** Keep your current registrar but let Route 53 handle DNS. Follow the steps below to create a hosted zone and update your registrar's name servers.
- **Transfer the domain to Route 53:** Make Route 53 your registrar and DNS service. See [Pre-transfer checklist for domain transfers](domain-transfer-checklist.md "domain-transfer-checklist.md") for what to do first, and [Transferring registration for a domain to Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md") for the transfer steps.

For more information about TLDs supported by Route 53, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

### Create a hosted zone and delegate DNS

Follow these steps to create a public hosted zone and then add the name
servers to your registrar:

###### To create a hosted zone for a non-Route 53 domain

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted
   zones**, and then choose **Create hosted zone**.
3. For the **Name**, enter the name of the domain you want to create a hosted zone for,
   such as `example.com`, add a description if you want, choose **Public hosted zone**, and then choose **Create hosted zone**.
4. After you create the hosted zone, note the four name server (NS) records. Each starts with "ns-".

At your domain registrar, enter these name servers to point the domain to your Route 53 hosted zone.

### Route DNS traffic

To tell Route 53 how to route internet traffic for the domain, you create records in the hosted zone. For example, if you
want to route requests for example.com to a web server on an Amazon EC2 instance, you create a record in the example.com
hosted zone and specify the Elastic IP address for that instance. For more information, see the following topics:

- For information about how to create records in your hosted zone, see
  [Working with records](rrsets-working-with.md "rrsets-working-with.md").
- For information about how to route traffic to selected AWS resources, see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").
- For information about how DNS works, see
  [How internet traffic is routed to your website or web application](welcome-dns-service.md "welcome-dns-service.md").
- To check DNS repose, see [Checking DNS responses from Route 53](dns-test.md "dns-test.md").
