# Key concepts and components for Route 53 Global Resolver

Route 53 Global Resolver uses several key components that work together to provide split-traffic DNS
resolution, high availability through global anycast architecture, and comprehensive DNS security
for your organization. Understanding these Route 53 Global Resolver concepts helps you design and deploy solutions
that enable seamless access to both private and public resources, ensure service continuity across
multiple Regions, and protect against DNS-based threats.

## DNS resolver for clients at

on-premises and remote locations

To deploy Route 53 Global Resolver for your distributed workloads, customer locations, and users, configure these key
components:

Global resolver

The main service instance that provides DNS resolution and filtering for your
organization across multiple AWS Regions. Your _global resolver_ uses
anycast technology to automatically route DNS queries to the nearest available Region,
ensuring fast response times for all clients regardless of their location.

Anycast IP addresses

Two unique IPv4 or IPv6 addresses assigned to your global resolver that you configure on client
devices and network equipment. These _anycast IP addresses_ are the same
globally, which simplifies DNS configuration across all your locations. Anycast IP addressing
enables automatic routing of DNS requests to the nearest global resolver, optimizing response
times and improving service reliability.

DNS views

Configuration templates that let you apply different DNS policies to different groups of
clients in your network. Use _DNS views_ to implement split-horizon DNS—for
example, apply strict filtering and token authentication for remote locations, while using
IP-based access and different security policies for branch offices.

## DNS client authentication

Select the authentication method that works best for your deployment:

Token based authentication

Secure DNS connections using encrypted tokens for DNS-over-HTTPS (DoH) and DNS-over-TLS
(DoT). You can generate unique access tokens for individual clients or device groups, set
expiration periods, and revoke tokens as needed.

Access source-based authentication

Control access using IP address and CIDR range allowlists. You can configure your branch
office public IP addresses or network ranges, then specify which DNS protocols
(DNS-over-port-53, DoT, or DoH) each location can use based on your security requirements.

DNS protocol selection

Choose the appropriate _DNS protocol_ based on your security and
compatibility needs:

- **DNS-over-port-53 (Do53)** - Use for
  maximum compatibility with existing network infrastructure
- **DNS-over-TLS (DoT)** - Use when you need encrypted DNS
  with dedicated port separation for network monitoring
- **DNS-over-HTTPS (DoH)** - Use when you need to
  bypass network restrictions, as traffic appears as regular HTTPS

## Split-traffic DNS resolution

Route 53 Global Resolver enables organizations to seamlessly resolve both private and public domains from
any location, eliminating the need for complex VPN configurations or Region-specific DNS
settings.

Hybrid DNS resolution

_Hybrid DNS resolution_ allows Route 53 Global Resolver to simultaneously resolve
queries from on-premises users and applications to private applications on AWS.

Global private zone access

_Global private zone access_ extends the reach of Amazon Route 53 private
hosted zones beyond VPC boundaries. Authorized clients anywhere on the internet can resolve
private domain names, enabling distributed teams to access internal resources without
traditional network connectivity requirements.

Seamless failover

_Seamless failover_ ensures continuous access to both private and
public resources even when individual AWS Regions become unavailable. The anycast
architecture automatically routes queries to healthy regions while maintaining consistent
resolution behavior.

## High availability and global presence

Route 53 Global Resolver provides enterprise-grade availability through distributed architecture and
automatic failover capabilities.

Multi-region deployment

_Multi-region deployment_ distributes Route 53 Global Resolver instances across at least 2 AWS Regions to ensure high availability and allow failover during service outages. You can
select specific Regions based on your geographic requirements and compliance needs.

Automatic geographic optimization

_Automatic geographic optimization_ routes DNS queries to the nearest
available AWS Region based on network topology and latency. This reduces response times and
improves user experience for globally distributed organizations.

Built-in redundancy

_Built-in redundancy_ ensures service continuity through automatic
failover to alternate regions when primary regions become unavailable. Clients continue to use
the same anycast IP addresses while traffic is transparently rerouted.

## DNS resolution and forwarding

Private hosted zone resolution

_Private hosted zone resolution_ enables Route 53 Global Resolver to resolve DNS
queries for Route 53 private hosted zones across AWS Regions. This allows authorized clients
to resolve domains for applications and resources hosted by Route 53 from anywhere on the
internet.

Split-horizon DNS

_Split-horizon DNS_ provides different DNS responses based on the
client making the query. Route 53 Global Resolver can resolve public domains on the internet while
simultaneously resolving private domains, providing seamless access to both public and private
resources.

DNSSEC validation

_DNSSEC validation_ verifies the authenticity and integrity of DNS
responses from public nameservers for DNSSEC-signed domains. This validation ensures DNS
responses haven't been tampered with during transmission, providing protection against DNS
spoofing and cache poisoning attacks.

EDNS Client Subnet (ECS)

_EDNS Client Subnet_ is an optional feature that forwards client
subnet information in DNS queries to authoritative nameservers. This enables more accurate
geographic-based DNS responses, potentially reducing latency by directing clients to nearer
content delivery networks or servers. For DNS-over-TLS (DoT) and DNS-over-HTTPS (DoH)
connections, you can use EDNS0 to pass the client IP address information. When ECS is enabled
on Global Resolver, the service automatically injects the client IP if not provided in the
query.

## DNS filtering and domain lists

Route 53 Global Resolver provides domain-based filtering using domain lists managed by AWS to block or
allow specific domains.

DNS filtering rules

_DNS filtering rules_ define how Route 53 Global Resolver handles DNS queries based on
domain matching criteria. Rules are evaluated in priority order and can specify actions
(ALLOW, BLOCK, or ALERT) for queries to specific domains or domain categories.

Domain lists

_Domain lists_ are collections of domains used in filtering rules.
They can be:

- **Custom domain lists** - Domain collections you create
  and maintain
- **AWS managed domain lists** - Pre-configured threat lists and content categories
  maintained by AWS that leverage threat intelligence to identify malicious domains.
  Available threat lists include:

      + Malware domains - Domains known to host or distribute malware
      + Botnet command and control - Domains used by botnets for command and control
       communications
      + Spam - Domains associated with spam and unwanted email campaigns
      + Phishing - Domains used in phishing attacks to steal credentials and personal
       information
      + Amazon GuardDuty threat list - Domains identified by GuardDuty threat intelligence

  Available content categories include social media, gambling, and other categories that
  help organizations control access to specific types of content.

Individual domain specifications in managed lists cannot be viewed or edited to protect
intellectual property and maintain security effectiveness.

## Advanced DNS threat detection

Route 53 Global Resolver uses dynamic algorithmic analysis to detect advanced DNS threats such as DNS
tunneling and Domain Generation Algorithms. Unlike domain lists that match known bad domains,
algorithmic detection analyzes DNS query patterns in real-time to identify suspicious
behavior.

DNS tunneling detection

DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS
tunnel without making a network connection to the client.

Domain Generation Algorithm (DGA) detection

Domain Generation Algorithms (DGAs) are used by attackers to create large numbers of domain names for its command-and-control servers.

Confidence thresholds

Each detection algorithm outputs a confidence score that determines rule triggering.
Higher confidence thresholds reduce false positives but may miss sophisticated attacks. Lower
thresholds increase detection sensitivity but require additional alert analysis to filter
false positives.

Action limitations

Advanced threat protection rules support only `ALERT` and `BLOCK`
actions. The `ALLOW` action is not supported because algorithmic detection cannot
definitively classify benign traffic, only identify potentially malicious patterns.

## Monitoring and logging

Query logs

_Query logs_ provide detailed information about DNS queries processed
by Route 53 Global Resolver, including source IP, queried domain, response code, policy actions taken, and
timestamps. Logs can be delivered to Amazon CloudWatch, Amazon Data Firehose, or Amazon Simple Storage Service for analysis and
compliance reporting.

OCSF format

_Open Cybersecurity Schema Framework (OCSF) format_ is a standardized
logging format used by Route 53 Global Resolver for DNS query logs. This format provides consistent,
structured data that integrates easily with security information and event management (SIEM)
systems and other security tools.

Log destinations

_Log destinations_ determine where DNS query logs are delivered, each
with different characteristics:

- **Amazon Simple Storage Service** - Cost-effective long-term storage ideal for
  compliance and batch analysis. Integrates with analytics tools like Amazon Athena and Amazon EMR.
- **Amazon CloudWatch Logs** - Real-time monitoring and alerting with
  integration to Amazon CloudWatch alarms and dashboards. Supports log insights for ad-hoc queries.
- **Amazon Data Firehose** - Real-time streaming to external systems
  with built-in data transformation capabilities. Supports automatic scaling and buffering.

Observability Region

The _Observability Region_ determines where DNS query logs are delivered.
