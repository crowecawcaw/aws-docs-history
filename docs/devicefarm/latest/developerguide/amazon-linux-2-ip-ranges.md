# Supported IP ranges for the Amazon Linux 2 test environment in

Device Farm

Customers often need to know the IP range from which Device Farm's traffic originates, particularly for
configuring their firewalls and security settings. For Amazon EC2 test hosts, the IP range encompasses the entire
`us-west-2` region. For Amazon Linux 2 test hosts, which is the default option for new
Android runs, the ranges have been restricted. The traffic now originates from a specific set of NAT
gateways, restricting the IP range to the following addresses:

| IP Ranges          |
| ------------------ |
| **44.236.137.143** |
| **52.13.151.244**  |
| **52.35.189.191**  |
| **54.201.250.26**  |

For more information about Android test environments in Device Farm, see [Test environment for Android devices](custom-test-environments-hosts-android.md "custom-test-environments-hosts-android.md").
