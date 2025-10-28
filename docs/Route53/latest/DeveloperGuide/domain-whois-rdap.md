# Viewing information about domains that are

registered with Route 53

###### Note

Effective January 28, 2025, some domain registries may transition from WHOIS to the Registration Data Access Protocol (RDAP) for domain registration data queries.
If you access domain registration information directly from registries via WHOIS,
you may need to update your applications to use RDAP endpoints if the relevant registry discontinues WHOIS support.

Route 53 domains service functionality remains unchanged. This notice applies only to direct registry WHOIS queries performed outside of Route 53 services.

You can view information about domains that were registered using Route 53. This information includes details such as
when the domain was originally registered and contact information for the domain
owner and for the technical, administrative, and billing contacts.

###### WHOIS

WHOIS is a free, publicly available directory containing information about domains
sponsored by domain registrars and registries. It is provided as both a service
that accepts queries on port 43, and as a website, each accessible via both IPv4
and IPv6. WHOIS is a distributed hierarchical lookup. For more information, see
[About WHOIS](https://whois.icann.org/en/about-whois "https://whois.icann.org/en/about-whois").

A WHOIS request to different levels of the hierarchy can provide different information:

- A request to the root WHOIS (whois.iana.org) provides information about the registry.
- A request to registry WHOIS provides information about the registrar, and some public information about the domain.
- A request to registrar WHOIS provides all public information about the domain.
  Because there are multiple levels of WHOIS, including WHOIS lookups operated by the TLD
  registry and the domain registrar, turning your privacy protection off on the Route 53
  console may only turn it off on the registrar-provided WHOIS. Some registries
  intentionally maintain privacy protection or redaction services for their WHOIS
  lookup services regardless of whether you have turned it off with Route 53. To get full
  information about your domain, we recommend that you use the registrar-provided
  WHOIS.

Note the following:

**Emailing domain contacts when privacy protection is enabled**

If privacy protection is enabled for the domain, contact information for the registrant,
technical, and administrative contacts is replaced with contact
information for the Amazon Registrar privacy service. For example, if
the example.com domain is registered with Amazon Registrar and if
privacy protection is enabled, the value of **Registrant
Email** in the response to a WHOIS query would be similar
to owner1234@example.com.identity-protect.org.

To contact one or more domain contacts when privacy protection is
enabled, send an email to the corresponding email addresses. We
automatically forward your email to the applicable contact.

**Reporting abuse**

To report any illegal activity or violation of the [Acceptable Use Policy](https://aws.amazon.com/route53/amazon-registrar-policies/#acceptable-use-policy "https://aws.amazon.com/route53/amazon-registrar-policies/#acceptable-use-policy"), including inappropriate content,
phishing, malware, or spam, send an email to trustandsafety@support.aws.com.

###### To view information about domains that

are registered with Route 53

1. In a web browser, go to one of the following websites:
   - **Amazon Registrar WHOIS:**
     [https://registrar.amazon.com/whois](https://registrar.amazon.com/whois "https://registrar.amazon.com/whois")
   - **Amazon Registrar RDAP:**
     [https://registrar.amazon.com/rdap](https://registrar.amazon.com/rdap "https://registrar.amazon.com/rdap")
   - **Gandi WHOIS:**
     [https://whois.gandi.net](https://whois.gandi.net "https://whois.gandi.net")

2. Enter the name of the domain that you want to view information about, and
   choose **Search**.
