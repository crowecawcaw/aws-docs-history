**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Troubleshooting AWS Shield network security director

## Unsupported Cross-Account Shared Resources

AWS Shield network security director does not support certain cross-account shared resources. When attempting to scan these resources, you'll receive error messages indicating the resources cannot be analyzed.

| Unsupported Shared Resources and Error Messages | Resource Type                                                             | Error Message |
| ----------------------------------------------- | ------------------------------------------------------------------------- | ------------- |
| Network Firewall FirewallPolicy                 | network-firewall:DescribeFirewallPolicy not supported on shared resources |
| Network Firewall Stateful rule group            | network-firewall:DescribeRuleGroup not supported on shared resources      |
| Network Firewall Stateless rule group           | network-firewall:DescribeRuleGroup not supported on shared resources      |
| EC2 PrefixList                                  | ec2:GetManagedPrefixListEntries not supported on shared resources         |

## Availability of Findings and Suppressions

Network security director retains network scan results for 60 days. After this period, you must run a new scan to view current findings.

Suppressions are retained as long as you have an active network scan. If a network scan is no longer available because 60 days have lapsed, you must reapply your suppressions to the next network scan.

## Resource Scan Limitations

When scanning accounts with a large number of resources, you may encounter the following limitations:

- You may receive a message indicating that a scan is already in progress
- The service cannot provide estimated completion times for scans
- Scan duration varies based on the number of resources in your account

###### Note

The scan duration depends on the total number of resources in your account, which is determined during the scanning process itself.

## Additional Resources

If you encounter issues not addressed in this troubleshooting guide, please contact AWS Support for additional assistance.
