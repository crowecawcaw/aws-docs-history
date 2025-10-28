# How DNS resolvers on your network

forward DNS queries to Route 53 Resolver endpoints

To forward DNS queries from your network to Route 53 Resolver, you create inbound endpoints in an
AWS Region. There are two categories of inbound endpoints, **default** and **delegation**.

**Steps for creating default inbound endpoints**

1. You create a default Route 53 Resolver inbound endpoint in a VPC and specify the IP addresses that
   the resolvers on your network forward DNS queries to, along with a VPC
   security group that includes inbound rules allowing TCP and UDP access on
   port 53. For instructions see [Configuring inbound forwarding](resolver-forwarding-inbound-queries-configuring.md "resolver-forwarding-inbound-queries-configuring.md").

For each IP address that you specify for the inbound endpoint, Resolver creates a VPC elastic network interface
in the VPC where you created the inbound endpoint. 2. You configure resolvers on your network to forward DNS queries for the applicable domain names to the IP addresses
that you specified in the inbound endpoint. For more information, see
[Considerations when creating inbound and outbound endpoints](resolver-choose-vpc.md "resolver-choose-vpc.md").
**Here's how Resolver resolves DNS queries that originate on your network via a default inbound endpoint:**

1. A web browser or another application on your network submits a DNS query for a domain name
   that you forwarded to Resolver.
2. A resolver on your network forwards the query to the IP addresses in your inbound endpoint.
3. The inbound endpoint forwards the query to Resolver.
4. Resolver gets the applicable value for the domain name in the DNS query, either internally or by
   performing a recursive lookup against public name servers.
5. Resolver returns the value to the inbound endpoint.
6. The inbound endpoint returns the value to the resolver on your network.
7. The resolver on your network returns the value to the application.
8. Using the value that was returned by Resolver, the application submits a request, for example, a
   request for an object in an Amazon S3 bucket.
   **Steps for creating delegation inbound endpoints**

9. You create a delegation Route 53 Resolver inbound endpoint in a VPC. For instructions see [Configuring inbound forwarding](resolver-forwarding-inbound-queries-configuring.md "resolver-forwarding-inbound-queries-configuring.md").

For each IP address that you specify for the inbound endpoint, Resolver creates a VPC elastic network interface
in the VPC where you created the inbound endpoint. 2. You configure resolvers on your network to delegate DNS queries for the applicable domain
names to Route 53 Resolver. For the glue records you must enter the IP addresses for
the inbound endpoints. For more information, see [Considerations when creating inbound and outbound endpoints](resolver-choose-vpc.md "resolver-choose-vpc.md").
**Here's how Resolver resolves DNS queries that originate on your network via a delegation inbound endpoint:**

1. As a prerequisite, you must delegate the subdomain that is hosted in the private hosted zone
   from on-premises. Because you are delegating the subdomain via the inbound
   delegation endpoint, you use the inbound endpoint IP addresses as the glue
   records for the subdomain that's being delegated.

###### Note

You might also need to include the glue records to make sure the DNS query is resolvable. If
you delegate a subdomain to name servers that are in the same zone as
the parent domain, glue records are needed. 2. A web browser or another application on your network submits a DNS query for a domain name
that you delegated to the Route 53 Resolver. 3. A resolver on your network forwards the query to the IP addresses in your inbound endpoint. 4. The inbound endpoint delegates the query to Resolver. 5. Resolver returns the address to the AWS resource from the private hosted zone to the inbound
endpoint. 6. The inbound endpoint returns the value to the resolver on your network. 7. The resolver on your network returns the value to the application. 8. Using the value that was returned by Resolver, the application submits a request, for example, a
request for an object in an Amazon S3 bucket.
Creating an inbound endpoint doesn't change the behavior of Resolver, it just provides a path from a location
outside the AWS network to Resolver.
