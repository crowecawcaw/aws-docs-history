# AWS IP address ranges

AWS publishes its current IP address ranges in JSON format. With this information, you can
identify traffic from AWS. You can also use this information to allow or deny traffic to or from
some AWS services.

###### Considerations

- We publish the IP address ranges for services that customers commonly use to perform egress
  filtering. We don't publish the IP address ranges for all services.
- Services use their IP address ranges to communicate with other services or
  to communicate with a customer network.
- The IP address ranges that you bring to AWS through bring your own IP
  addresses (BYOIP) are not included in the `.json` file. For more information,
  see [Advertise your address range through AWS](../../../AWSEC2/latest/UserGuide/byoip-onboard.md#byoip-advertise "../../../AWSEC2/latest/UserGuide/byoip-onboard.md#byoip-advertise")
  in the _Amazon EC2 User Guide_.
  Some services publish their address ranges using AWS-managed prefix lists.
  For more information, see [Available AWS-managed prefix lists](working-with-aws-managed-prefix-lists.md#available-aws-managed-prefix-lists "working-with-aws-managed-prefix-lists.md#available-aws-managed-prefix-lists").

###### Contents

- [Download](#aws-ip-download "#aws-ip-download")
- [Egress control](#aws-ip-egress-control "#aws-ip-egress-control")
- [Geolocation feed](#aws-ip-geo-ip-feed "#aws-ip-geo-ip-feed")
- [Find address ranges](aws-ip-work-with.md "aws-ip-work-with.md")
- [Syntax](aws-ip-syntax.md "aws-ip-syntax.md")
- [Subscribe to notifications](subscribe-notifications.md "subscribe-notifications.md")

## Download the JSON file

To view the current address ranges, download [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json").
To maintain history, save successive versions of the JSON file on your own computer.
To determine whether there have been changes since the last time that you saved the file,
check the publication time in the current file and compare it to the publication time in
the last file that you saved.

The following is an example **curl** command that saves the JSON file
to the current directory.

```
curl -O https://ip-ranges.amazonaws.com/ip-ranges.json
```

If you access this file programmatically, it is your responsibility to ensure that the
application downloads the file only after successfully verifying the TLS certificate
presented by the server.

To receive notifications of updates to the JSON file, see
[AWS IP address ranges notifications](subscribe-notifications.md "subscribe-notifications.md").

## Egress control

To allow resources you've created with one AWS service to only access other AWS
services, you can use the IP address range information in the ip-ranges.json file to
perform egress filtering. Ensure that the security group rules allow outbound traffic to
the CIDR blocks in the AMAZON list. There are [quotas for security groups](amazon-vpc-limits.md#vpc-limits-security-groups "amazon-vpc-limits.md#vpc-limits-security-groups"). Depending on the number of IP address ranges in
each Region, you might need multiple security groups per Region.

###### Note

Some AWS services are built on EC2 and use EC2 IP address space. If you block traffic to EC2 IP
address space, you block traffic to these non-EC2 services as well.

## Geolocation feed

The IP address ranges in `ip-ranges.json` are by AWS Region. However,
a Local Zone is not in the same physical location as its parent Region. The geolocation
data published in [geo-ip-feed.csv](https://ip-ranges.amazonaws.com/geo-ip-feed.csv "https://ip-ranges.amazonaws.com/geo-ip-feed.csv")
accounts for Local Zones. The data follows [RFC 8805](https://datatracker.ietf.org/doc/html/rfc8805 "https://datatracker.ietf.org/doc/html/rfc8805").
