# How domain registration works

If you want to create a website or a web application, you start by registering the name of your website,
known as a [domain name](route-53-concepts.md#route-53-concepts-domain-name "route-53-concepts.md#route-53-concepts-domain-name"). Your domain name is the name,
such as example.com, that your users enter in a browser to display your website.

Here's an overview of how you register a domain name with Amazon Route 53:

1. You choose a domain name and confirm that it's available, meaning that no one else has registered the
   domain name that you want.

If the domain name you want is already in use, you can try other names or try changing only the
_top-level domain_, such as .com, to another top-level domain, such as .ninja or .hockey.
For a list of the top-level domains that Route 53 supports, see
[Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md"). 2. You register the domain name with Route 53. When you register a domain, you provide names and contact information
for the domain owner and other contacts.

When you register a domain with Route 53, the service automatically makes itself the DNS service for the domain
by doing the following:

    * Creates a [hosted zone](route-53-concepts.md#route-53-concepts-hosted-zone "route-53-concepts.md#route-53-concepts-hosted-zone") that has
     the same name as your domain.
    * Assigns a set of four name servers to the hosted zone. When someone uses a browser to access your website,
     such as www.example.com, these name servers tell the browser where to find your resources, such as a
     web server or an Amazon S3 bucket. ([Amazon S3](../../../s3.md "../../../s3.md") is object storage
     for storing and retrieving any amount of data from anywhere on the web. A bucket is a container for objects
     that you store in S3.)
    * Gets the name servers from the hosted zone and adds them to the domain.

For more information, see [How internet traffic is routed to your website or web application](welcome-dns-service.md "welcome-dns-service.md"). 3. At the end of the registration process, we send your information to the registrar for the domain.
The [domain registrar](route-53-concepts.md#route-53-concepts-domain-registrar "route-53-concepts.md#route-53-concepts-domain-registrar") is either Amazon Registrar, Inc.
or our registrar associate, Gandi. To find out who the registrar is for your domain, see
[Finding your registrar](find-your-registrar.md "find-your-registrar.md"). 4. The registrar sends your information to the _registry_ for the domain. A registry
is a company that sells domain registrations for one or more top-level domains, such as .com. 5. The registry stores the information about your domain in their own database and also stores some of
the information in the public WHOIS database.
For more information about how to register a domain name, see [Registering a new domain](domain-register.md "domain-register.md").

If you already registered a domain name with another registrar, you can choose to transfer the domain registration to
Route 53. This isn't required to use other Route 53 features. For more information, see
[Transferring registration for a domain to
Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").
