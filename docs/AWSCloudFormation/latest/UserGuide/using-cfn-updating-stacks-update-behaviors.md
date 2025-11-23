# Understand update behaviors of stack

resources

When you submit an update, CloudFormation updates resources based on differences between what you
submit and the stack's current template. Resources that haven't changed run without disruption
during the update process. For updated resources, CloudFormation uses one of the following update
behaviors:

**Update with No Interruption**

CloudFormation updates the resource without disrupting operation of that resource and
without changing the resource's physical ID. For example, if you update certain
properties on an [AWS::CloudTrail::Trail](../TemplateReference/aws-resource-cloudtrail-trail.md "../TemplateReference/aws-resource-cloudtrail-trail.md") resource, CloudFormation updates the trail without
disruption.

**Updates with Some Interruption**

CloudFormation updates the resource with some interruption. For example, if you update
certain properties on an [AWS::EC2::Instance](../TemplateReference/aws-resource-ec2-instance.md "../TemplateReference/aws-resource-ec2-instance.md") resource, the instance might have some interruption
while CloudFormation and Amazon EC2 reconfigure the instance.

**Replacement**

CloudFormation recreates the resource during an update, which also generates a new physical
ID. CloudFormation usually creates the replacement resource first, changes references from
other dependent resources to point to the replacement resource, and then deletes the
old resource. For example, if you update the `AvailabilityZone` property
of an [AWS::EC2::Instance](../TemplateReference/aws-resource-ec2-instance.md "../TemplateReference/aws-resource-ec2-instance.md") resource type, CloudFormation creates a new resource and
replaces the current EC2 Instance resource with the new one.

If you're adding or removing a property that requires a replacement, it will also
trigger an update. The update will happen even if the real value of the property doesn't change.

The method CloudFormation uses depends on which property you update for a given resource type. The
update behavior for each property is described in the [AWS resource and property types reference](../TemplateReference/aws-template-resource-type-ref.md "../TemplateReference/aws-template-resource-type-ref.md").

Depending on the update behavior, you can decide when to modify resources to reduce the
impact of these changes on your application. In particular, you can plan when resources must
be _replaced_ during an update. For example, if you update the
`Port` property of an [AWS::RDS::DBInstance](../TemplateReference/aws-resource-rds-dbinstance.md "../TemplateReference/aws-resource-rds-dbinstance.md") resource type, CloudFormation replaces the DB instance by creating a
new DB instance with the updated port setting and deletes the old DB instance. Before the
update, you might plan to do the following to prepare for the database replacement:

- Take a snapshot of the current databases.
- Prepare a strategy for how applications that use that DB instance will handle an
  interruption while the DB instance is being replaced.
- Ensure that the applications that use that DB instance considers the updated port
  setting and any other updates you have made.
- Use the DB snapshot to restore the databases on the new DB instance.
  This example isn't exhaustive, but it's meant to give you an idea of the things to plan for
  when a resource is replaced during an update.

###### Note

If the template includes one or more [nested
stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md"), CloudFormation also initiates an update for every nested stack. This is necessary to
determine whether the nested stacks have been modified. CloudFormation updates only those resources
in the nested stacks that have changes specified in corresponding templates.
