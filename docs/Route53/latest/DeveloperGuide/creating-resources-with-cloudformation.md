

# Creating Amazon Route 53 and Route 53 VPC Resolver resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Amazon Route 53 and Route 53 VPC Resolver are integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Route 53 and VPC Resolver resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Route 53, VPC Resolver, and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Route 53, VPC Resolver, and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

Route 53 supports creating the following resource types in CloudFormation:
+ `AWS::Route53::DNSSEC`
+ `AWS::Route53::HealthCheck`
+ `AWS::Route53::HostedZone`
+ `AWS::Route53::KeySigningKey`
+ `AWS::Route53::RecordSet`
+ `AWS::Route53::RecordSetGroup`

 For more information, including examples of JSON and YAML templates for Route 53 resources, see the [Amazon Route 53 resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53.html) in the *AWS CloudFormation User Guide*.

VPC Resolver supports creating the following resource types in CloudFormation:
+ `AWS::Route53Resolver::FirewallDomainList`
+ `AWS::Route53Resolver::FirewallDomainList`
+ `AWS::Route53Resolver::FirewallRuleGroupAssociation`
+ `AWS::Route53Resolver::ResolverDNSSECConfig`
+ `AWS::Route53Resolver::ResolverEndpoint`
+ `AWS::Route53Resolver::ResolverQueryLoggingConfig`
+ `AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation`
+ `AWS::Route53Resolver::ResolverRule`
+ `AWS::Route53Resolver::ResolverRuleAssociation`

 For more information, including examples of JSON and YAML templates for VPC Resolver resources, see the [Route 53 VPC Resolver resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.html) in the *AWS CloudFormation User Guide*.

## Best practices for Route 53 and CloudFormation
<a name="cloudformation-route53-best-practices"></a>

When using CloudFormation to manage Route 53 resources, follow these best practices to avoid common issues and ensure reliable deployments.

### Understanding eventual consistency
<a name="cloudformation-route53-eventual-consistency"></a>

Route 53 uses an eventually consistent model for DNS changes. This can affect CloudFormation operations, particularly during rollbacks and rapid successive changes.

**Important**  
When CloudFormation attempts to roll back DNS record changes, the rollback might fail due to the Route 53 eventual consistency model. If CloudFormation tries to recreate a record that was recently deleted but still appears to exist due to eventual consistency, you might encounter `InvalidChangeBatch` errors that leave your DNS in a broken state.

To minimize issues related to eventual consistency:
+ **Plan changes carefully** - Avoid making rapid successive changes to the same DNS records
+ **Test in non-production first** - Always test DNS changes in development environments before applying to production
+ **Monitor deployments** - Watch CloudFormation stack events closely during DNS-related deployments. For monitoring guidance, see [Monitoring Amazon Route 53](monitoring-overview.md).
+ **Have rollback procedures ready** - Prepare manual recovery procedures in case automatic rollbacks fail

### DNS record ordering and logical IDs
<a name="cloudformation-route53-record-ordering"></a>

When creating multiple DNS records in CloudFormation, be careful about record ordering and logical ID assignment.

**Warning**  
If you define DNS records in arrays or lists within your CloudFormation template, inserting new records in the middle of the list can cause CloudFormation to reassign logical IDs to existing records. This triggers record replacements that can lead to service disruptions and rollback failures.

Best practices for DNS record management:
+ **Use explicit logical IDs** - Always assign explicit, meaningful logical IDs to DNS records rather than relying on array indices. For more information about CloudFormation logical IDs, see [Resources section structure](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) in the *AWS CloudFormation User Guide*
+ **Append new records** - When adding new DNS records to existing lists, append them to the end rather than inserting them in the middle
+ **Group related records** - Consider using `AWS::Route53::RecordSetGroup` for managing related records together. For more information, see [AWS::Route53::RecordSetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html) in the *AWS CloudFormation User Guide*.
+ **Review change sets** - Always review CloudFormation change sets before deployment to identify unexpected record replacements. For more information, see [Updating stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) in the *AWS CloudFormation User Guide*.

### Handling rollback failures
<a name="cloudformation-route53-rollback-failures"></a>

If a CloudFormation rollback fails due to DNS-related issues, you might need to perform manual recovery.

**To perform manual recovery from failed DNS rollbacks**

1. Identify the failed DNS records by reviewing CloudFormation stack events and Route 53 hosted zone records

1. Manually create or update the missing DNS records through the Route 53 console or API. For information about creating records, see [Working with records](rrsets-working-with.md).

1. After DNS is restored, update your CloudFormation template to match the current state

1. Deploy the corrected template to bring CloudFormation back in sync with the actual resources

To prevent rollback failures:
+ Avoid making changes that could trigger DNS record replacements during high-traffic periods
+ Implement health checks and monitoring to detect DNS issues quickly. For information about health checks, see [Creating and updating health checks](health-checks-creating.md).
+ Consider using blue-green deployment strategies for critical DNS changes. For more information about deployment best practices, see [Best practices for Amazon Route 53](best-practices.md).
+ Document emergency procedures for manual DNS recovery

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)