

# `AWSSupport-TroubleshootR53DNSResolution`
<a name="automation-awssupport-troubleshoot-r53-dns-resolution"></a>

 **Description** 

The **`AWSSupport-TroubleshootR53DNSResolution`** runbook helps troubleshoot DNS resolution issues by analyzing the complete resolution path from an Amazon Virtual Private Cloud (Amazon VPC) or Amazon Elastic Compute Cloud (Amazon EC2) instance perspective. It identifies configuration problems across Amazon VPC DNS settings, Amazon Route 53 (Route 53) Resolver, Private Hosted Zones, DNS Firewall, and public DNS delegation chains.

 **Supported scenarios:** 
+ Amazon VPC DNS attributes (DNS Support, DNS Hostnames) and DHCP option sets including custom DNS server detection.
+ Route 53 Resolver rules precedence evaluation and Profile associations.
+ DNS Firewall rule group evaluation including multi-rule group priority, CNAME redirection inspection, and cross-account or AWS-managed domain list detection.
+ Private Hosted Zone record lookup, Amazon VPC Endpoint Private Hosted Zone resolution, and override detection when DNS Hostnames is disabled.
+ Route 53 Resolver Outbound Endpoint network connectivity analysis (security groups, NACLs, route tables) and forwarding loop detection.
+ Public DNS delegation chain validation, nameserver consistency, lame delegation detection, and domain registration status via RDAP.

 **Limitations:** 
+ This runbook performs read-only analysis and does not modify any AWS resources.
+ CNAME records are not chased to their final target for further analysis.
+ AWS-managed Firewall domain lists and cross-account Firewall rule groups are detected but their contents cannot be inspected.
+ Cross-account Route 53 Profiles are detected but cannot be fully analyzed.
+ DNS Firewall fail-open or fail-closed behavior during service unavailability is not evaluated.
+ Custom DNS server responses configured via DHCP options cannot be verified.
+ Domain registration status analysis is not available for all top-level domains.

 **How does it work?** 

The runbook determines the analysis path based on the provided `ResourceId` parameter. If you provide an Amazon EC2 instance ID or Amazon VPC ID, it performs Amazon VPC-specific DNS analysis including Amazon VPC DNS configuration, Route 53 Resolver rules, DNS Firewall evaluation, Private Hosted Zones, and Resolver Outbound Endpoint connectivity. If you don't provide a `ResourceId`, it performs public DNS resolution analysis only. After completion, the runbook generates a comprehensive report with findings, severity levels, and actionable recommendations.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootR53DNSResolution) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ResourceId

  Type: String

  Description: (Optional) The Amazon Elastic Compute Cloud (Amazon EC2) instance ID (`i-xxxxxxxxx`) or Amazon Virtual Private Cloud (Amazon VPC) ID (`vpc-xxxxxxxxx`) for Amazon VPC-specific DNS analysis. If not provided, this runbook will perform public DNS resolution analysis instead of Amazon VPC-specific analysis.

  Allowed Pattern: `^(i-[a-z0-9]{8,17}|vpc-[a-f0-9]{8,17})?$`
+ DnsRecordName

  Type: String

  Description: (Required) The fully qualified domain name (FQDN) to analyze for DNS resolution issues.

  Allowed Pattern: `^([a-zA-Z0-9_]([a-zA-Z0-9_-]*[a-zA-Z0-9_])?\.)*[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}\.?$`
+ RecordType

  Type: String

  Description: (Optional) The DNS record type to query for the specified domain name.

  Valid values: `A | AAAA | CNAME | CAA | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT`

  Default: `A`

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeInstances`
+ `ec2:DescribeVpcs`
+ `ec2:DescribeVpcAttribute`
+ `ec2:DescribeDhcpOptions`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeNetworkAcls`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeSubnets`
+ `ec2:GetManagedPrefixListEntries`
+ `route53:ListHostedZonesByVPC`
+ `route53:ListHostedZonesByName`
+ `route53:GetHostedZone`
+ `route53:ListResourceRecordSets`
+ `route53resolver:GetResolverRule`
+ `route53resolver:ListResolverRuleAssociations`
+ `route53resolver:ListResolverEndpoints`
+ `route53resolver:ListResolverEndpointIpAddresses`
+ `route53resolver:ListFirewallRuleGroupAssociations`
+ `route53resolver:GetFirewallRuleGroup`
+ `route53resolver:ListFirewallRules`
+ `route53resolver:GetFirewallDomainList`
+ `route53resolver:ListFirewallDomains`
+ `route53resolver:GetResolverConfig`
+ `route53resolver:GetResolverDnssecConfig`
+ `route53resolver:GetFirewallConfig`
+ `route53profiles:ListProfileAssociations`
+ `route53profiles:GetProfile`
+ `route53profiles:ListProfileResourceAssociations`

Example Policy: 

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EC2DescribePermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeVpcs",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSubnets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2PrefixListPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:GetManagedPrefixListEntries"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Route53GlobalPermissions",
            "Effect": "Allow",
            "Action": [
                "route53:ListHostedZonesByVPC",
                "route53:ListHostedZonesByName"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Route53HostedZonePermissions",
            "Effect": "Allow",
            "Action": [
                "route53:GetHostedZone",
                "route53:ListResourceRecordSets"
            ],
            "Resource": "arn:aws:route53:::hostedzone/*"
        },
        {
            "Sid": "Route53ResolverListPermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:ListResolverEndpoints",
                "route53resolver:ListResolverRuleAssociations",
                "route53resolver:ListFirewallRuleGroupAssociations"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Route53ResolverEndpointPermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:ListResolverEndpointIpAddresses"
            ],
            "Resource": "arn:aws:route53resolver:*:*:resolver-endpoint/*"
        },
        {
            "Sid": "Route53ResolverSharedResourcePermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:GetResolverRule",
                "route53resolver:GetFirewallRuleGroup",
                "route53resolver:GetFirewallDomainList",
                "route53resolver:ListFirewallDomains"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Route53ResolverFirewallRulePermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:ListFirewallRules"
            ],
            "Resource": "arn:aws:route53resolver:*:*:firewall-rule-group/*"
        },
        {
            "Sid": "Route53ResolverConfigPermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:GetResolverConfig"
            ],
            "Resource": "arn:aws:route53resolver:*:*:resolver-config/*"
        },
        {
            "Sid": "Route53ResolverDnssecConfigPermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:GetResolverDnssecConfig"
            ],
            "Resource": "arn:aws:route53resolver:*:*:resolver-dnssec-config/*"
        },
        {
            "Sid": "Route53ResolverFirewallConfigPermissions",
            "Effect": "Allow",
            "Action": [
                "route53resolver:GetFirewallConfig"
            ],
            "Resource": "arn:aws:route53resolver:*:*:firewall-config/*"
        },
        {
            "Sid": "Route53ProfilesPermissions",
            "Effect": "Allow",
            "Action": [
                "route53profiles:ListProfileAssociations",
                "route53profiles:GetProfile",
                "route53profiles:ListProfileResourceAssociations"
            ],
            "Resource": "*"
        }
    ]
}
```

 **Instructions** 

Follow these steps to configure the automation:

1. Navigate to the [AWSSupport-TroubleshootR53DNSResolution](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootR53DNSResolution/description) in the AWS Systems Manager console.

1. For the input parameters enter the following:
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your permissions.
   + **ResourceId (Optional):**

     The Amazon EC2 instance ID (`i-xxxxxxxxx`) or Amazon VPC ID (`vpc-xxxxxxxxx`) for Amazon VPC-specific DNS analysis. If not provided, the runbook performs public DNS resolution analysis only.
   + **DnsRecordName (Required):**

     The fully qualified domain name (FQDN) to analyze for DNS resolution issues. For example, `www.example.com`.
   + **RecordType (Optional):**

     The DNS record type to query for the specified domain name. Default is `A`. Supported values include: `A`, `AAAA`, `CNAME`, `MX`, `NS`, `PTR`, `SOA`, `TXT`, and others.

1. Select **Execute**.

1. The automation initiates.

1. The automation runbook performs the following steps:
   + **BranchOnResourceType:**

     Determines the analysis path based on the `ResourceId` type. Branches to instance lookup, Amazon VPC parameter set, or directly to public DNS analysis.
   + **GetVpcIdFromInstance:**

     Retrieves the Amazon VPC ID from the specified Amazon EC2 instance. Only executed when `ResourceId` is an instance ID.
   + **GatherVpcConfiguration:**

     Gathers Amazon VPC configuration including Amazon VPC details, DHCP options, and DNS attributes (enableDnsSupport, enableDnsHostnames).
   + **GatherRoute53ResolverConfiguration:**

     Gathers all Route 53 Resolver configuration including Resolver settings, endpoints, Route 53 Profiles, and DNS Firewall rule groups.
   + **GatherDnsResolutionSources:**

     Gathers all DNS resolution sources including matching Resolver Rules, Private Hosted Zones, DNS records, and Auto-Defined Rules.
   + **AnalyzeDnsServerConfiguration:**

     Analyzes Amazon VPC DNS server configuration from DHCP Options. Determines whether AmazonProvidedDNS or custom DNS servers are in use.
   + **EvaluateFirewallBlocking:**

     Evaluates DNS Firewall rule groups to determine if they are blocking or redirecting the target domain.
   + **DeterminePrecedence:**

     Determines which DNS resolution path takes precedence based on the matching Resolver Rules, Private Hosted Zones, and Auto-Defined Rules.
   + **BranchOnResolutionPath:**

     Routes to the appropriate analysis path based on the determined resolution path (Resolver Rule, Private Hosted Zone, Public DNS, or Auto-Defined Rule).
   + **GatherResolverNetworkConfiguration:**

     Gathers network configuration for the Resolver Outbound Endpoint including security groups, network ACLs, route tables, and prefix lists.
   + **AnalyzeResolverConnectivity:**

     Analyzes connectivity between the Resolver Outbound Endpoint and target DNS servers. Evaluates security groups, network ACLs, and route tables to identify connectivity issues.
   + **AnalyzePrivateHostedZone:**

     Analyzes Private Hosted Zone configuration and records for the target domain.
   + **AnalyzeDelegationChain:**

     Analyzes the complete DNS delegation chain from root servers. Validates nameserver consistency, detects missing delegation levels, and collects RDAP data for domain registration information.
   + **AnalyzePublicDnsResolution:**

     Performs public DNS resolution, checks for matching Route 53 public hosted zones, and compares hosted zone nameservers with the delegation chain to detect mismatches.
   + **GenerateFinalReport:**

     Generates a comprehensive DNS analysis report consolidating results from all executed analysis steps.

1. After completion, review the Outputs section for the detailed results of the execution.

 **References** 

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootR53DNSResolution)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/)

AWS service documentation
+ [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)
+ [Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)
+ [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)
+ [DNS attributes for your Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html)