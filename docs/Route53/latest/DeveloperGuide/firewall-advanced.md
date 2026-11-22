

# DNS Firewall Advanced Rules

DNS Firewall Advanced Rule tier provides you with protections to help you detect and monitor for more advanced DNS threats (for example, Domain Generation Algorithms (DGA) or DNS Tunneling) or with more granular protections based on threat and web-content (for example, gambling, social networking).

There are four main types of advanced rules:
+ Advanced Protections that help detect suspicious DNS queries based on known threat signatures (for example, DGA) in DNS queries.
+ Advanced DNS threat and content categories that provide more granular control to block DNS queries based on the type of DNS threats (for example, spam, phishing) or web content (for example, adult content, social networking, gambling sites).
+ Partner Managed DNS protections from Palo Alto Networks Advanced DNS Security and Infoblox (requires AWS Marketplace subscription).
+ Automated Allowlists that help you build an allowlist of domains from the DNS query traffic of your VPCs, so that you can block all other domains (`*`) and move to a walled-garden setup. For more information, see [Automated Allowlists](firewall-advanced-automated-allowlists.md).