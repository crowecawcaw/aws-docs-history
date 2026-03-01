# Locations and IP address ranges of CloudFront edge servers

For a list of the locations of CloudFront edge servers, see the [Amazon CloudFront Global Edge
Network](https://aws.amazon.com/cloudfront/features/#Global_Edge_Network "https://aws.amazon.com/cloudfront/features/#Global_Edge_Network") page.

Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. To view the
current ranges, download [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json"). For more information, see [AWS IP address
ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the _Amazon Web Services General Reference_.

To find the IP address ranges that are associated with CloudFront edge servers, search
ip-ranges.json for the following string:

```
`"region": "GLOBAL",`
`"service": "CLOUDFRONT"`
```

Alternatively, you can view only the CloudFront IP ranges at [https://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips](https://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips "https://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips").

## Use the CloudFront managed prefix list

The CloudFront managed prefix list contains the IP address ranges of all of CloudFront's
globally distributed origin-facing servers. If your origin is hosted on AWS and
protected by an Amazon VPC [security group](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md"),
you can use the CloudFront managed prefix list to allow inbound traffic to your origin
only from CloudFront's origin-facing servers, preventing any non-CloudFront traffic from
reaching your origin. CloudFront maintains the managed prefix list so it's always up to
date with the IP addresses of all of CloudFront's global origin-facing servers. With the
CloudFront managed prefix list, you don't need to read or maintain a list of IP address
ranges yourself.

For example, imagine that your origin is an Amazon EC2 instance in the Europe (London) Region
(`eu-west-2`). If the instance is in a VPC, you can create a security
group rule that allows inbound HTTPS access from the CloudFront managed prefix list. This
allows all of CloudFront's global origin-facing servers to reach the instance. If you
remove all other inbound rules from the security group, you prevent any non-CloudFront
traffic from reaching the instance.

The CloudFront managed prefix lists are as follows:

- `com.amazonaws.global.cloudfront.origin-facing` (IPv4)
- `com.amazonaws.global.ipv6.cloudfront.origin-facing` (IPv6)

For more
information, see [Use an AWS-managed prefix list](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#use-aws-managed-prefix-list "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#use-aws-managed-prefix-list") in the _Amazon VPC User Guide_.

###### Important

The CloudFront managed prefix list is unique in how it applies to Amazon VPC quotas. For
more information, see [AWS-managed prefix list weight](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#aws-managed-prefix-list-weights "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#aws-managed-prefix-list-weights") in the _Amazon VPC User Guide_.
