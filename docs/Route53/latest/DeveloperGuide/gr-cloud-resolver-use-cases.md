# DNS security and split-horizon use cases for

Route 53 Global Resolver

Route 53 Global Resolver addresses three primary DNS challenges for organizations:

Enabling split-traffic between public and private DNS resolution

Enable global access to private hosted zones (PHZs) on Amazon Route 53 from any location while
simultaneously resolving public domains on the internet. Allow remote locations and branch
offices to resolve internal application names without complex VPN configurations or
Region-specific forwarding. Implement split-horizon DNS to provide different DNS responses
based on the client making the query, helping remote clients resolve queries for private and
public domains.

Securing DNS traffic from DNS exfiltration attacks

Protect remote locations and branch offices from DNS-based data exfiltration attacks by filtering queries to malicious domains. Improve privacy by encrypting DNS traffic in-transit using DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) to
ensure only authorized clients can access your DNS services. Apply security policies to block
threats like DNS tunneling and Domain Generation Algorithms (DGAs). Validate DNS response
authenticity using DNSSEC (Domain Name System Security Extensions) for DNSSEC-signed domains
to protect against DNS spoofing and cache poisoning attacks.

High availability and global presence

Achieve high availability through global deployment and maintain consistent DNS
configuration worldwide from a single management interface. Route 53 Global Resolver runs across
the AWS Regions you choose, using anycast IP addresses that automatically route queries to the
nearest available Region for optimal performance and reliability. Global enterprises can
configure and manage DNS policies centrally while providing clients with a single set of IP
addresses that work globally with automatic geographic optimization. Built-in redundancy
ensures service continuity even if individual Regions become unavailable.

Additional capabilities support these primary use cases:

Implementing DNS filtering and content policies

Govern internet access across multiple locations by creating custom domain lists or using
AWS Managed Domain Lists. To help you implement filtering and content policies according to your needs, Managed Domain Lists include multiple categories of DNS threats that cover several domains. Configure Access Source using IP allowlists or Access Tokens, and set up different
filtering policies for different office locations or client groups.

Flexible authentication for different deployment scenarios

Choose the authentication method that works best for your deployment: token-based
authentication or IP based authentication using the source CIDR range
allowlists.

Maintaining visibility and compliance

Monitor DNS activity across your organization by delivering logs to Amazon CloudWatch, Firehose, or
Amazon Simple Storage Service. Choose a single destination Region for centralized log storage to support security
audits, compliance requirements, and threat investigation.
