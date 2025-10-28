# DNS configuration for

AWS Management Console and AWS Sign-In

To route your network traffic to respective VPC endpoints, configure DNS
records in the network from which your users will be accessing the AWS Management Console. These
DNS records will direct your users browser traffic toward the VPC endpoints
you created.

You can create a single hosted zone. However, endpoints such as
`health.aws.amazon.com` and `docs.aws.amazon.com` won't be
accessible because they don't have VPC endpoints. You will need to route these domains to
the public internet. We recommend that you create two private hosted zones per Region, one
for `signin.aws.amazon.com` and one for `console.aws.amazon.com` with
the following CNAME records:

- Sign-In
  - `region`.signin.aws.amazon.com pointing to the AWS Sign-In VPC endpoint in the signin
    DNS zone where `region` is the desired Region
  - signin.aws.amazon.com pointing to AWS Sign-In VPC endpoint in US East (N. Virginia) (us-east-1)

- Console

      + `region`.console.aws.amazon.com pointing to the AWS Management Console VPC endpoint in the console
       DNS zone where `region` is the desired Region
      + \*.`region`.console.aws.amazon.com pointing to the AWS Management Console VPC endpoint in the console
       DNS zone where `region` is the desired Region
      + \*.`region`.console.aws.amazon.com pointing to the AWS Management Console VPC endpoint in the console
       DNS zone
      + Regionless CNAME records for the US East (N. Virginia) Region only. You
       always have to set up the US East (N. Virginia) Region.




      	- signin.aws.amazon.com pointing to AWS Sign-In VPC endpoint in US East (N. Virginia)
      	 (us-east-1)
      	- \*.console.aws.amazon.com pointing to AWS Management Console VPC endpoint in US East (N. Virginia)
      	 (us-east-1)

  For instructions on creating a CNAME record, see [Working
  with records](../../../Route53/latest/DeveloperGuide/rrsets-working-with.md "../../../Route53/latest/DeveloperGuide/rrsets-working-with.md") in the _Amazon Route 53 Developer Guide_.

Some AWS consoles, including Amazon S3, use different patterns for their DNS
names. The following are two examples:

    + support.console.aws.amazon.com
    + s3.console.aws.amazon.com

To be able to direct this traffic to your AWS Management Console VPC endpoint, you need to add those
names individually. We recommend that you configure routing for all endpoints for a fully
private experience. However, this isn't required to use AWS Management Console Private Access.

The following `json` files contain the full list of AWS services and
console endpoints to configure per Region. Use the `PrivateIpv4DnsNames` field
under the `com.amazonaws.`region`.console` endpoint for
the DNS names.

    + [https://configuration.private-access.console.amazonaws.com/us-east-1.config.json](https://configuration.private-access.console.amazonaws.com/us-east-1.config.json "https://configuration.private-access.console.amazonaws.com/us-east-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/us-east-2.config.json](https://configuration.private-access.console.amazonaws.com/us-east-2.config.json "https://configuration.private-access.console.amazonaws.com/us-east-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/us-west-2.config.json](https://configuration.private-access.console.amazonaws.com/us-west-2.config.json "https://configuration.private-access.console.amazonaws.com/us-west-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-northeast-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-northeast-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-southeast-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-southeast-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json](https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json "https://configuration.private-access.console.amazonaws.com/ap-south-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json](https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json "https://configuration.private-access.console.amazonaws.com/ap-south-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json](https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json "https://configuration.private-access.console.amazonaws.com/ca-central-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json]( https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json " https://configuration.private-access.console.amazonaws.com/eu-central-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json](https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json "https://configuration.private-access.console.amazonaws.com/eu-west-1.config.json")
    + [https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json](https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json "https://configuration.private-access.console.amazonaws.com/eu-west-2.config.json")
    + [https://configuration.private-access.console.amazonaws.com/il-central-1.config.json](https://configuration.private-access.console.amazonaws.com/il-central-1.config.json "https://configuration.private-access.console.amazonaws.com/il-central-1.config.json")

###### Note

This list is updated each month as we add additional endpoints to the scope of
AWS Management Console Private Access. To keep your private hosted zones updated, periodically pull the
preceding list of files.

If you use Route 53 to configure your DNS, go to
https://console.aws.amazon.com/route53/v2/hostedzones# to verify the DNS
setup. For each Private Hosted Zone in Route 53, verify that the following record sets are
present.

    + console.aws.amazon.com
    + signin.aws.amazon.com
    + \*.`region`.console.aws.amazon.com
    + `region`.console.aws.amazon.com
    + \*.`region`.console.aws.amazon.com
    + signin.aws.amazon.com
    + `region`.signin.aws.amazon.com
    + Additional records present in the previously listed JSON files
