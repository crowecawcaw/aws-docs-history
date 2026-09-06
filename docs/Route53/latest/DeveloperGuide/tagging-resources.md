

# Tagging Amazon Route 53 resources
<a name="tagging-resources"></a>

A tag is a label that you assign to an AWS resource. Each tag consists of a *key* and a *value*, both of which you define. For example, the key might be "domain" and the value might be "example.com". Tags serve many purposes. One common use is to categorize and track your Amazon Route 53 costs. When you apply tags to Route 53 hosted zones, domains, and health checks, AWS generates a cost allocation report as a CSV file. This report shows your usage and costs grouped by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information about using tags for cost allocation, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the [AWS Billing User Guide](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).

For best results, use Tag Editor in the AWS Management Console. Tag Editor provides a central way to create and manage your tags. For more information, see [Working with Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html) in [Getting Started with the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html). You can also use the Route 53 console to apply tags for some resources:
+ **Health checks** – For more information, see [Naming and tagging health checks](health-checks-tagging.md).
+ **Route 53 VPC Resolver inbound endpoints** – For more information, see [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md).
+ **Resolver outbound endpoints** – For more information, see [Values that you specify when you create or edit outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md).
+ **Resolver rules** – For more information, see [Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md).
+ **Hosted zones** – For more information, see [Working with hosted zones](hosted-zones-working-with.md).

**Note**  
Charges for Resolver endpoints are allocated per VPC Resolver network interface. You can't tag VPC Resolver network interfaces, so tag-based cost allocation isn't supported for Resolver endpoints. For information about pricing for VPC Resolver, see [Amazon Route 53 pricing](https://aws.amazon.com/route53/pricing/).

You can also apply tags to resources by using the Route 53 API. For more information, see the actions related to tags in the topic [Route 53 API actions by function](https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html) in the *Amazon Route 53 API Reference*.