**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Troubleshooting AWS Shield network security director

## Unsupported Cross-Account Shared Resources

AWS Shield network security director does not support certain cross-account shared resources. When attempting to scan these resources, you'll receive error messages indicating the resources cannot be analyzed.

| Unsupported Shared Resources and Error Messages | Resource Type                                                             | Error Message |
| ----------------------------------------------- | ------------------------------------------------------------------------- | ------------- |
| Network Firewall FirewallPolicy                 | network-firewall:DescribeFirewallPolicy not supported on shared resources |
| Network Firewall Stateful rule group            | network-firewall:DescribeRuleGroup not supported on shared resources      |
| Network Firewall Stateless rule group           | network-firewall:DescribeRuleGroup not supported on shared resources      |
| EC2 PrefixList                                  | ec2:GetManagedPrefixListEntries not supported on shared resources         |

## Availability of Resources, Findings, and Suppression

If an account leaves an organization or network security director is disabled for an account, the following occurs:

- **Findings and Resources:** Findings from the account will be removed once the service is disabled for the account. This process typically takes a few minutes but could be longer.
- **Suppressions:** Suppressions are deleted within 90 days of disabling the service for an account. If the service is re-enabled for an account within this 90-day period, existing suppressions might still be available, but availability is not guaranteed. Suppressions must be removed before disabling the service for an account to avoid this uncertainty.

## Performance Considerations

AWS Shield network security director is designed to provide daily data refreshes for your organization's network analysis. However, performance can vary based on your organization's size and region.

Organizations with a large number of accounts may experience longer refresh cycles, with data refreshes occurring after multiple days for individual accounts. Additionally, performance can vary significantly by Region, with opt-in regions in particular experiencing slow performance and extended refresh times.

For improved performance and more frequent data refreshes, we recommend enabling network security director for accounts that are specifically relevant to each region. This recommendation is especially critical for opt-in regions.

## Additional Resources

If you encounter issues not addressed in this troubleshooting guide, please contact AWS Support for additional assistance.
