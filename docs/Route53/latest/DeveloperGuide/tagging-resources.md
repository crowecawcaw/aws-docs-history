# Tagging Amazon Route 53 resources

A tag is a label that you assign to an AWS resource. Each tag consists of a _key_ and a _value_,
both of which you define. For example, the key might be "domain" and the value might be "example.com". You can use tags
for a variety of purposes; one common use is to categorize and track your Amazon Route 53 costs. When you apply tags to Route 53 hosted zones, domains,
and health checks, AWS generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs
aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners)
to organize your costs across multiple services. For more information about using tags for cost allocation, see
[Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
in the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").

For ease of use and best results, use Tag Editor in the AWS Management Console, which provides a central, unified way to create and manage your tags.
For more information, see [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in
[Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md"). You can also use the Route 53 console to apply tags for some resources:

- **Health checks** – For more information, see
  [Naming and tagging health checks](health-checks-tagging.md "health-checks-tagging.md").
- **Route 53 VPC Resolver inbound endpoints** – For more information, see
  [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md").
- **Resolver outbound endpoints** – For more information, see
  [Values that you specify when you create or edit
  outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md "resolver-forwarding-outbound-queries-endpoint-values.md").
- **Resolver rules** – For more information, see
  [Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md "resolver-forwarding-outbound-queries-rule-values.md").
- **Hosted zones** – For more information, see
  [Working with hosted zones](hosted-zones-working-with.md "hosted-zones-working-with.md").

###### Note

Charges for Resolver endpoints are allocated per VPC Resolver network interface. As it isn't
currently possible to tag VPC Resolver network interfaces, tag-based cost allocation isn't
currently supported for Resolver endpoints. For information about pricing for VPC Resolver,
see [Amazon Route 53 pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

You can also apply tags to resources by using the Route 53 API. For more information, see the actions related to tags
in the topic [Route 53 API actions by function](../APIReference/API-actions-by-function.md "../APIReference/API-actions-by-function.md") in the
_Amazon Route 53 API Reference_.
