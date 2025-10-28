# Creating Amazon Route 53 and Amazon Route 53 Resolver

resources with AWS CloudFormation

Amazon Route 53 and Amazon Route 53 Resolver are integrated with AWS CloudFormation, a service that helps you to model
and set up your AWS resources so that you can spend less time creating and managing your
resources and infrastructure. You create a template that describes all the AWS resources
that you want, and AWS CloudFormation provisions and configures those resources for you.

When you use AWS CloudFormation, you can reuse your template to set up your Route 53 and Route 53 Resolver resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Route 53, Route 53 Resolver, and AWS CloudFormation templates

To provision and configure resources for Route 53, Route 53 Resolver, and related services, you must
understand [AWS CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These templates
describe the resources that you want to provision in your AWS CloudFormation stacks. If you're
unfamiliar with JSON or YAML, you can use AWS CloudFormation Designer to help you get started with
AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

Route 53 supports creating the following resource types in AWS CloudFormation:

- `AWS::Route53::DNSSEC`
- `AWS::Route53::HealthCheck`
- `AWS::Route53::HostedZone`
- `AWS::Route53::KeySigningKey`
- `AWS::Route53::RecordSet`
- `AWS::Route53::RecordSetGroup`

For more information, including examples of JSON and YAML templates
for Route 53 resources, see the [Amazon Route 53 resource type
reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Route53.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Route53.md") in the _AWS CloudFormation User Guide_.

Route 53 Resolver supports creating the following resource types in AWS CloudFormation:

- `AWS::Route53Resolver::FirewallDomainList`
- `AWS::Route53Resolver::FirewallDomainList`
- `AWS::Route53Resolver::FirewallRuleGroupAssociation`
- `AWS::Route53Resolver::ResolverDNSSECConfig`
- `AWS::Route53Resolver::ResolverEndpoint`
- `AWS::Route53Resolver::ResolverQueryLoggingConfig`
- `AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation`
- `AWS::Route53Resolver::ResolverRule`
- `AWS::Route53Resolver::ResolverRuleAssociation`

For more information, including examples of JSON and YAML templates for Route 53 Resolver
resources, see the [Amazon Route 53 Resolver
resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.md") in the _AWS CloudFormation User Guide_.

## Best practices for Route 53 and

AWS CloudFormation

When using AWS CloudFormation to manage Route 53 resources, follow these best practices to avoid
common issues and ensure reliable deployments.

### Understanding eventual

consistency

Route 53 uses an eventually consistent model for DNS changes. This can affect AWS CloudFormation
operations, particularly during rollbacks and rapid successive changes.

###### Important

When AWS CloudFormation attempts to roll back DNS record changes, the rollback might fail
due to the Route 53 eventual consistency model. If AWS CloudFormation tries to recreate a record
that was recently deleted but still appears to exist due to eventual
consistency, you might encounter `InvalidChangeBatch` errors that
leave your DNS in a broken state.

To minimize issues related to eventual consistency:

- **Plan changes carefully** - Avoid making
  rapid successive changes to the same DNS records
- **Test in non-production first** - Always
  test DNS changes in development environments before applying to
  production
- **Monitor deployments** - Watch AWS CloudFormation stack
  events closely during DNS-related deployments. For monitoring guidance, see
  [Monitoring Amazon Route 53](monitoring-overview.md "monitoring-overview.md").
- **Have rollback procedures ready** - Prepare
  manual recovery procedures in case automatic rollbacks fail

### DNS record ordering and

logical IDs

When creating multiple DNS records in AWS CloudFormation, be careful about record ordering and
logical ID assignment.

###### Warning

If you define DNS records in arrays or lists within your AWS CloudFormation template,
inserting new records in the middle of the list can cause AWS CloudFormation to reassign
logical IDs to existing records. This triggers record replacements that can lead
to service disruptions and rollback failures.

Best practices for DNS record management:

- **Use explicit logical IDs** - Always assign
  explicit, meaningful logical IDs to DNS records rather than relying on array
  indices. For more information about AWS CloudFormation logical IDs, see [Resources section structure](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md") in the
  _AWS CloudFormation User Guide_
- **Append new records** - When adding new DNS
  records to existing lists, append them to the end rather than inserting them
  in the middle
- **Group related records** - Consider using
  `AWS::Route53::RecordSetGroup` for managing related records
  together. For more information, see [AWS::Route53::RecordSetGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.md") in the
  _AWS CloudFormation User Guide_.
- **Review change sets** - Always review AWS CloudFormation
  change sets before deployment to identify unexpected record replacements.
  For more information, see [Updating stacks using change sets](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md") in the
  _AWS CloudFormation User Guide_.

### Handling rollback

failures

If a AWS CloudFormation rollback fails due to DNS-related issues, you might need to perform
manual recovery.

###### To perform manual recovery from failed DNS rollbacks

1. Identify the failed DNS records by reviewing AWS CloudFormation stack events and Route 53
   hosted zone records
2. Manually create or update the missing DNS records through the Route 53
   console or API. For information about creating records, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").
3. Once DNS is restored, update your AWS CloudFormation template to match the current
   state
4. Deploy the corrected template to bring AWS CloudFormation back in sync with the actual
   resources

To prevent rollback failures:

- Avoid making changes that could trigger DNS record replacements during
  high-traffic periods
- Implement health checks and monitoring to detect DNS issues quickly. For
  information about health checks, see [Creating and updating health checks](health-checks-creating.md "health-checks-creating.md").
- Consider using blue-green deployment strategies for critical DNS changes.
  For more information about deployment best practices, see [Best practices for Amazon Route 53](best-practices.md "best-practices.md").
- Document emergency procedures for manual DNS recovery

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API
  Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
