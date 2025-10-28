# Manage AWS Config costs in AWS Control Tower

This section describes how AWS Config records and bills you for changes to resources in your
AWS Control Tower accounts. This information may help you understand how to manage the costs associated
with AWS Config, when you're utilizing AWS Control Tower. AWS Control Tower adds no additional cost.

###### Note

**If your landing zone version is 3.0 or later**: AWS Control Tower
limits AWS Config recording for global resources, such as IAM users, groups, roles, and
customer-managed polices, to your home Region only. Therefore, some of the information in
this section may not apply to your landing zone.

AWS Config is designed to record each change to each resource, in each Region where an account
operates, as a configuration item (CI). AWS Config bills you for each configuration item that it
generates.

**How AWS Config operates**

AWS Config records resources in each Region, separately. Some global resources, such as IAM
roles, are recorded once per Region. For example, if you create a new IAM role in an
enrolled account that is operating in five Regions, AWS Config generates five CIs, one for each
Region. Other global resources, such as Route 53 hosted zones, are recorded only once across all
Regions. For example, if you create a new Route 53 hosted zone in an enrolled account, AWS Config
generates one CI, regardless of how many Regions are selected for that account. For a list
that helps you distinguish these types of resources, see [The same resource is recorded multiple
times](monitoring-with-config.md#duplicate-configuration-items "monitoring-with-config.md#duplicate-configuration-items").

###### Note

When AWS Control Tower works with AWS Config, a Region may be governed by AWS Control Tower, or ungoverned, and
AWS Config still records the changes if the account operates in that Region.

**AWS Config detects two types of relationships in
resources**

AWS Config makes a distinction between _direct_ and _indirect_ relationships among resources. If a resource is returned
in another resource's **Describe** API call, those resources are recorded as
a direct relationship. When you change a resource in a direct relationship with another
resource, AWS Config does not make a CI for both resources.

For example, if you create an Amazon EC2 instance, and the API requires you to create a network
interface, AWS Config considers the Amazon EC2 instance to have a direct relationship with the network
interface. As a result, AWS Config generates only one CI.

AWS Config records separate changes for resource relationships that are _indirect_ relationships. For example, AWS Config generates two CIs if you create a
security group and add an associated Amazon EC2 instance that's part of the security group.

For more information about direct and indirect relationships, see [What is a direct and
an indirect relationship with respect to a resource?](../../../config/latest/developerguide/faq.md#faq-0 "../../../config/latest/developerguide/faq.md#faq-0")

You can find [a list of resource
relationships](../../../config/latest/developerguide/resource-config-reference.md "../../../config/latest/developerguide/resource-config-reference.md") in the AWS Config documentation.
