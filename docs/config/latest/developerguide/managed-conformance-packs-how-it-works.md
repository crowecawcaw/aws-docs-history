

# How managed conformance packs work in AWS Config

When you deploy a managed conformance pack, AWS Config deploys the AWS Config rules included in the pack to the selected AWS account and AWS Region. During deployment, you can configure the parameters for the rules in the managed conformance pack. If you don't specify a value for a parameter, AWS Config uses the default value for that parameter.

AWS Config uses the rules in the managed conformance pack to evaluate applicable resources and reports the results as part of the conformance pack. AWS Config recording must be enabled for the corresponding resource types for the rules to properly evaluate your resources. We recommend recording all supported resource types to maximize the benefits of managed conformance packs.

**Note**  
Managed conformance packs are regionalized based on AWS Config rule availability. When you deploy a managed conformance pack to an AWS Region, AWS Config deploys only the rules in the pack that are supported in that Region. As a result, the rules included in a deployed managed conformance pack can vary by Region.

AWS maintains the content of managed conformance packs to keep them aligned with the requirements and best practices they are designed to address. AWS can add, update, or remove rules in response to changes such as updates to regulatory frameworks, the release of new AWS Config rules, or changes to AWS best practices. When AWS adds, updates, or removes rules from a managed conformance pack, you are notified via an Amazon CloudWatch Metric.

When AWS adds a new rule to a managed conformance pack, the rule is deployed to existing deployments of the managed conformance pack using the rule's default parameter values. New rules are evaluated automatically when they are created. When AWS updates an existing rule, for example by changing a parameter value, the rule is evaluated the next time it is successfully triggered.

You can't add or remove the rules included in a managed conformance pack. However, you can configure and update the supported parameters for the rules. If you need to control which rules are included in a conformance pack, create a [custom conformance pack](custom-conformance-packs.md) instead.

## Considerations
<a name="managed-conformance-packs-considerations"></a>

Before you deploy a managed conformance pack, consider the following:
+ Managed conformance packs are deployed to an individual AWS account and Region. Deployment across an organization via Organization Conformance Packs isn't supported.
+ You can't add or remove the rules included in a managed conformance pack.
+ You can configure supported rule parameters when you deploy a managed conformance pack and update them after deployment. If you don't specify a parameter value, the default value is used.
+ AWS maintains the content of managed conformance packs to keep them aligned with the requirements and best practices they are designed to address. AWS can add, update, or remove rules in response to changes such as updates to regulatory frameworks, the release of new AWS Config rules, or changes to AWS best practices. When AWS adds, updates, or removes rules from a managed conformance pack, you are notified via an Amazon CloudWatch Metric.
+ New rules added to a managed conformance pack are deployed to existing deployments using their default parameter values.
+ The rules deployed as part of a managed conformance pack can vary by Region based on AWS Config rule availability.
+ AWS Config recording must be enabled for the corresponding resource types for rules to properly evaluate your resources. We recommend recording all supported resource types to maximize the benefits of managed conformance packs.
+ Deploying a managed conformance pack can result in AWS Config rule evaluations and associated charges.

**Important**  
Managed conformance packs can help you evaluate the configuration of your AWS resources against specified requirements. They don't guarantee compliance with any law, regulation, or industry standard. You are responsible for determining whether your use of AWS services meets applicable legal, regulatory, and compliance requirements.

## Next steps
<a name="managed-conformance-packs-next-steps"></a>
+ To review available managed conformance packs and the rules included in each pack, see [Managed Conformance Pack Catalog for AWS Config](managed-conformance-pack-catalog.md).
+ To deploy a managed conformance pack, see [Deploying Conformance Packs for AWS Config](conformance-pack-deploy.md).