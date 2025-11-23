# Release: Elastic Beanstalk adds support for Internet Protocol Version 6 (IPv6) inbound traffic on September 4, 2024

AWS Elastic Beanstalk adds support for inbound Internet Protocol Version 6 (IPv6) traffic.

**Release date:** September 4, 2024

## Changes

Elastic Beanstalk now supports dual-stack public service endpoints and dual-stack VPC endpoints, including VPC endpoints integrated with [AWS PrivateLink](https://aws.amazon.com//privatelink/ "https://aws.amazon.com//privatelink/").

This capability allows you to configure your Elastic Beanstalk VPC endpoints to accept dual-stack incoming traffic (via IPv6 and IPV4). You can also send requests
to the Elastic Beanstalk service using the [AWS CLI](../../../cli/latest/reference/elasticbeanstalk.md "../../../cli/latest/reference/elasticbeanstalk.md") or the [AWS SDK](https://aws.amazon.com//developer/tools/ "https://aws.amazon.com//developer/tools/") specifying an IPv4 endpoint or a dual-stack endpoint. For a list of public endpoints, see [Elastic Beanstalk service endpoints](../../../general/latest/gr/elasticbeanstalk.md "../../../general/latest/gr/elasticbeanstalk.md") in the
_Amazon Web Services General Reference_.

This functionality is available in all of the AWS Commercial Regions and AWS GovCloud (US) Regions that Elastic Beanstalk supports. At this time Elastic Beanstalk dual-stack
support is not available in the AWS China Regions. You can view the list of [AWS Services Available by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") on the _AWS
Regional Services_ website.

For more information about Elastic Beanstalk dual-stack traffic support, see [IPV6 support](../dg/vpc-vpce.md#vpc-vpce.ipv6 "../dg/vpc-vpce.md#vpc-vpce.ipv6") in the _AWS Elastic Beanstalk Developer Guide_. To learn more about
adopting IPv6 on AWS see the whitepaper [IPv6 on AWS](../../../whitepapers/latest/ipv6-on-aws/IPv6-on-AWS.md "../../../whitepapers/latest/ipv6-on-aws/IPv6-on-AWS.md").
