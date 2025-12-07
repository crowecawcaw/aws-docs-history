# Configure and manage DNS Firewall rules

## Creating and viewing firewall rules

Firewall rules define how Route 53 Global Resolver handles DNS queries based on domain lists, managed domain lists, content categories, or advanced threat protection. Each rule specifies a priority, target domains, and an action to take.

**Best practices for rule priority:**

- Use priority 100-999 for high-priority allow rules (trusted domains)
- Use priority 1000-4999 for block rules (known threats)
- Use priority 5000-9999 for alert rules (monitoring and analysis)
- Leave gaps between priorities to allow for future rule insertion

**To create a DNS Firewall rule**

1. In the Route 53 Global Resolver console, navigate to your DNS view.
2. Choose the **Firewall rules** tab.
3. Choose **Create firewall rule**.
4. In the **Rule details** section:
   1. For **Rule name**, enter a descriptive name for the rule (up to 128 characters).
   2. (Optional) For **Rule description**, enter a description for the rule (up to 255 characters).

5. In the **Rule configuration** section, choose the **Rule configuration type**:
   - **Customer managed domain lists** - Use a domain list that you create and manage
   - **AWS managed domain lists** - Use domain lists provided by Amazon that you can utilize
   - **DNS Firewall Advanced protections** - Choose from a range of managed protections and specify a confidence threshold

6. For **Rule action**, choose the action to take when the rule matches:
   - **Allow** - The DNS query is resolved
   - **Alert** - Allows the DNS query but creates an alert
   - **Block** - The DNS query is blocked

7. Choose **Create firewall rule**.

Use the following procedure to view the rules assigned to them. You can also update the rule and rule settings.

**To view and update a rule**

1. In the Route 53 Global Resolver console, navigate to your DNS View.
2. Choose the **DNS Firewall rules** tab.
3. Choose the rule you want to view or edit, and choose **Edit**.
4. In the **Rule** page, you can view and edit settings.

For information about the values for rules, see [Rule settings in DNS Firewall](#gr-rule-settings-dns-firewall "#gr-rule-settings-dns-firewall").

**To delete a rule**

1. In the Route 53 Global Resolver console, navigate to your DNS View.
2. Choose the **DNS Firewall rules** tab.
3. Choose the rule you want to delete, and choose **Delete**, and confirm the deletion.

## Rule settings in DNS Firewall

When you create or edit a DNS Firewall rule in your DNS View, you specify the following values:

Name

A unique identifier for the rule in the DNS View.

(Optional) Description

A short description that provides more information about the rule.

Domain list

The list of domains that the rule inspects for. You can create and manage your own domain list or you can subscribe to a domain list that AWS manages for you.

A rule can contain ether a domain list or a DNS Firewall Advanced protection, but not both.

Query type (domain lists only)

The list of DNS query types that the rule inspects for. The following are the valid values:

- A: Returns an IPv4 address.
- AAAA: Returns an Ipv6 address.
- CAA: Restricts CAs that can create SSL/TLS certifications for the domain.
- CNAME: Returns another domain name.
- DS: Record that identifies the DNSSEC signing key of a delegated zone.
- MX: Specifies mail servers.
- NAPTR: Regular-expression-based rewriting of domain names.
- NS: Authoritative name servers.
- PTR: Maps an IP address to a domain name.
- SOA: Start of authority record for the zone.
- SPF: Lists the servers authorized to send emails from a domain.
- SRV: Application specific values that identify servers.
- TXT: Verifies email senders and application-specific values.

A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPE`NUMBER`, where the `NUMBER` can be 1-65334, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types "https://en.wikipedia.org/wiki/List_of_DNS_record_types").

You can create one query type per rule.

DNS Firewall Advanced protection

Detects suspicious DNS queries based on known threat signatures in DNS queries. You can choose protection from:

- Domain Generation Algorithms (DGAs)

DGAs are used by attackers to generate a large number of domains to launch malware attacks.

- DNS tunneling

DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.

In a DNS Firewall Advanced rule you can choose to either block, or alert on a query that matches the threat.

For more information, see DNS Firewall Advanced protections.

A rule can contain ether a DNS Firewall Advanced protection or a domain list, but not both.

Confidence threshold (DNS Firewall Advanced only)

The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean:

- High – Detects only the most well corroborated threats with a low rate of false positives.
- Medium – Provides a balance between detecting threats and false positives.
- Low – Provides the highest detection rate for threats, but also increases false positives.

For more information, see Rule settings in DNS Firewall.

Action

How you want DNS Firewall to handle a DNS query whose domain name matches the specifications in the rule's domain list. For more information, see [Rule actions in DNS Firewall](#gr-rule-actions-dns-firewall "#gr-rule-actions-dns-firewall").

Priority

Unique positive integer setting for the rule within the DNS View that determines processing order. DNS Firewall inspects DNS queries against the rules in a DNS View starting with the lowest numeric priority setting and going up. You can change a rule's priority at any time, for example to change the order of processing or make space for other rules.

## Rule actions in DNS Firewall

When DNS Firewall finds a match between a DNS query and a domain specification in a rule, it applies the action that's specified in the rule to the query.

You are required to specify one of the following options in each rule that you create:

- **Allow** – Stop inspecting the query and permit it to go through. Not available for DNS Firewall Advanced.
- **Alert** – Stop inspecting the query, permit it to go through, and log an alert for the query in the Route 53 Resolver logs.
- **Block** – Discontinue inspection of the query, block it from going to its intended destination, and log the block action for the query in the Route 53 Resolver logs.

Reply with the configured block response, from the following:

    + **NODATA** – Respond indicating that the query was successful, but no response is available for it.
    + **NXDOMAIN**– Respond indicating that the query's domain name doesn't exist.
    + **OVERRIDE**– Provide a custom override in the response. This option requires the following additional settings:




    	- **Record value** – The custom DNS record to send back in response to the query.
    	- **Record type**– The DNS record's type. This determines the format of the record value. This must be `CNAME`.
    	- **Time to live in seconds**– The recommended amount of time for the DNS resolver or web browser to cache the override record and use it in response to this query, if it is received again. By default, this is zero, and the record isn't cached.
