# High-level steps for using Route 53 Profiles

To implement Amazon Route 53 Profiles in your Amazon Virtual Private Cloud VPCs, you perform the following high-level steps.

1.  **Create an empty Profile** –
    The first step is to create an empty Profile to which you can associate DNS resources.
    For more information, see [Creating Route 53 Profiles](profile-create.md "profile-create.md").
2.  **Associate DNS resources to the Profile** – The
    resources you can currently associate to a Profile are private hosted zones,
    Resolver rules, both forwarding and system, DNS Firewall rule groups, VPC Resolver query
    logging configurations, and interface VPC endpoints. For more information, see
    [Associate DNS Firewall rule groups to a
    Route 53 Profile](profile-associate-dns-firewall.md "profile-associate-dns-firewall.md"), [Associate private hosted zones to a
    Route 53 Profile](profile-associate-private-hz.md "profile-associate-private-hz.md"), [Associate Resolver rules to a
    Route 53 Profile](profile-associate-resolver-rules.md "profile-associate-resolver-rules.md"), [Associate VPC Resolver query logging
    configurations to a Route 53 Profile](profile-associate-query-logging.md "profile-associate-query-logging.md"), and [Associate interface VPC endpoints
    to a Route 53 Profile](profile-associate-vpc-endpoints.md "profile-associate-vpc-endpoints.md").
3.  **Configure some of the VPC settings for the Profile**
    – Some of the DNS settings, like hosted zones associated to the Profile,
    are applied to the VPCs immediately. For DNSSEC validation, Resolver reverse DNS
    lookup, and DNS Firewall failure mode configurations you can choose one of the
    following options:

        * For DNSSEC validation, you can choose to use the local VPC configuration (default), enable the
         validation, or disable the validation for all the VPCs associated to the
         Profile.
        * For Resolver reverse DNS lookup configuration you can enable it, disable it, or use the auto
         defined rules defined for the VPC locally (default).
        * For DNS Firewall failure mode configuration you can enable it, disable it, or use the failure
         mode configuration defined for the VPC locally (default).

    For more information, see [Edit Route 53 Profile configurations](profile-edit-configurations.md "profile-edit-configurations.md").

4.  **Associate the Profile to one or more VPCs** –
    To begin using your Profile, associate it with one or more VPCs. For more information, see
    [Associate a Route 53 Profile to VPCs](profile-associate-vpcs.md "profile-associate-vpcs.md").
