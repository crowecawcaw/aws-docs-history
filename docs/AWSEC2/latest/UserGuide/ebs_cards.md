# EBS cards

Most instance types support one EBS card. Instance types that support multiple EBS cards
provide higher EBS-optimized performance, both in EBS throughput and IOPS. Your Amazon EC2 instance
maximum performance is spread equally across each EBS card. For example, on an EC2 instance
that supports `1,000,000` total IOPS with 2 EBS cards, each EBS card can support up to `500,000`
IOPS. For information about the supported Amazon EBS performance of your Amazon EC2 instance, see
[Amazon EBS-optimized instance types](ebs-optimized.md "ebs-optimized.md").

When you attach an Amazon EBS volume to an instance that supports multiple EBS cards, you can
select the EBS card for the volume by specifying the EBS card index. The root volume must
be attached to EBS card index 0.

## Instance types with multiple EBS cards

The following instance types support multiple EBS cards. For information about the number
of Amazon EBS volumes that an instance type supports, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").

| Instance Type     | Number of EBS cards |
| ----------------- | ------------------- |
| `c8gb.48xlarge`   | 2                   |
| `c8gb.metal-48xl` | 2                   |
| `m8gb.48xlarge`   | 2                   |
| `r8gb.48xlarge`   | 2                   |
| `r8gb.metal-48xl` | 2                   |
