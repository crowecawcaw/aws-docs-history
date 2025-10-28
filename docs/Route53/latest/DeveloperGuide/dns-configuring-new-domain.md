# Configuring DNS routing for a new domain

###### A new domain you purchased from Route 53

When you register a domain with Route 53, we automatically make Route 53 the DNS service for the domain. Route 53 creates a hosted zone
that has the same name as the domain, assigns four name servers to the hosted zone, and updates the domain to use those name servers.

###### A new domain you purchased from another registrar

When you purchase a domain from another registrar, for example, because the top-level
domain (TLD) isn't offered by Route 53, you have two options:

- **Use Route 53 for DNS hosting only:** Keep your current registrar but delegate DNS management to Route 53. Follow the procedure below to create a hosted zone and update your registrar's name servers.
- **Transfer the domain registration to Route 53:** Make Route 53 your registrar and DNS service. See [Pre-transfer checklist for domain transfers](domain-transfer-checklist.md "domain-transfer-checklist.md") for prerequisites and [Transferring registration for a domain to
  Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md") for the transfer process.
  For more information about TLDs supported by Route 53, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

Follow these instructions to create a public hosted zone and then use
the name servers created with the registrar:

###### To create a hosted zone for a non-Route 53 domain

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted
   zones**, and then choose **Create hosted zone**.
3. For the **Name**, enter the name of the domain you want to create a hosted zone for,
   Such as `example.com`, an optional description, choose **Public hosted zone** and then **Create hosted zone**.
4. After you create the hosted zone, note the four name server (NS) records that were created. Each will start with "ns-".

At your domain registrar, enter the name servers from above to delegate the domain management to your Route 53 hosted zone.

###### Route DNS traffic

To specify how you want Route 53 to route internet traffic for the domain, you create records in the hosted zone. For example, if you
want to route requests for example.com to a web server that's running on an Amazon EC2 instance, you create a record in the example.com
hosted zone, and you specify the Elastic IP address for the EC2 instance. For more information, see the following topics:

- For information about how to create records in your hosted zone, see
  [Working with records](rrsets-working-with.md "rrsets-working-with.md").
- For information about how to route traffic to selected AWS resources, see
  [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").
- For information about how DNS works, see
  [How internet traffic is routed to your website or web application](welcome-dns-service.md "welcome-dns-service.md").
- To check DNS repose, see [Checking DNS responses from Route 53](dns-test.md "dns-test.md").
