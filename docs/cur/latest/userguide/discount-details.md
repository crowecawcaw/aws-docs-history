# Discount details

Columns under the **discount** header are included in
AWS Cost and Usage Reports only when the account has a discount applied during the report's billing
period. This includes the following columns:

## discount/BundledDiscount

The bundled discount applied to the line item. A bundled discount is a usage-based
discount that provides free or discounted usage of a service or feature based on the
usage of another service or feature. Examples of bundled discounts include:

- If you use AWS Shield Advanced, then you don't have to pay for AWS WAF
  separately. AWS WAF usage is bundled with AWS Shield Advanced. For more
  information about AWS Shield Advanced, see [Amazon CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").
- If you create a NAT gateway with AWS Network Firewall, then the standard NAT gateway
  processing and per-hour usage charges are waived on a one-to-one basis with
  the firewall's processing per GB and usage hours. For more information, see
  [AWS Network Firewall
  pricing](https://aws.amazon.com/network-firewall/pricing/ "https://aws.amazon.com/network-firewall/pricing/").
- With Amazon Interactive Video Service (IVS) Chat, for every hour of video input sent, you get
  2,700 sent messages and 270,000 delivered messages at no additional cost.
  For more information, see [Amazon Interactive Video Service pricing](https://aws.amazon.com/ivs/pricing/ "https://aws.amazon.com/ivs/pricing/").

## discount/TotalDiscount

The sum of all the discount columns for the corresponding line item.
