

# Configuring AWS Organizations integration (optional)
<a name="next-gen-configuring-organizations"></a>

If you use AWS Organizations, you can optionally configure the next generation of Resilience Hub to provide centralized governance across your organization. The following is a quick setup summary:

1. The management account enables trusted access for `resiliencehub.amazonaws.com`.

1. Service-Linked Roles (`AWSServiceRoleForResilienceHub`) are automatically created in all member accounts.

1. The management account registers a delegated administrator.

1. The delegated administrator selects a home Region for data aggregation.

Individual service owners in member accounts still create their own invoker roles for their services. The SLR provides read-only cross-account visibility to the delegated administrator.

**Setting a home Region**

If you use AWS Organizations, the delegated administrator selects a home Region where organization-level data is aggregated. The home Region is the AWS Region where all organization-level summary data is collected for centralized reporting and dashboards.

When selecting a home Region, choose a Region that:
+ Is close to your primary operations team.
+ Meets your data residency requirements.

Service summary data (identifiers, compliance scores, status) replicates from all Regions and accounts into the home Region for fast, centralized queries. Full details such as topology, findings, and dependencies remain in their source Regions and are accessed on demand.

For detailed setup instructions, see [AWS Organizations integration](next-gen-organizations.md).