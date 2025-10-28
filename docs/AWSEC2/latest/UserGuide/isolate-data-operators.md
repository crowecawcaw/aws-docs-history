# Isolate data from your own operators

The AWS Nitro System has [zero operator access](../../../whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.md "../../../whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.md"). There is no mechanism for any AWS system or person to log in to Amazon EC2 Nitro hosts,
access the memory of EC2 instances, or access any customer data stored on local encrypted instance storage
or remote encrypted Amazon EBS volumes.

When processing highly sensitive data, you might consider restricting access to that data by preventing
even your own operators from accessing the EC2 instance.

You can create custom Attestable AMIs that are configured to provide an isolated compute environment. The AMI
configuration depends on your workload and application requirements. Consider these best practices when building
your AMI to create an isolated compute environment.

- **Remove all interactive access** to prevent your operators or users access
  to the instance.
- **Ensure that only trusted software and code** is included in the AMI.
- **Configure a network firewall** within the instance to block access.
- **Ensure read-only and immutable states** for all storage and file systems.
- **Restrict instance access** to authenticated, authorized, and logged API
  calls.
