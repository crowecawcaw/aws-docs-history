# Detective security best practices

for Aurora DSQL

In addition to the following ways to securely use Aurora DSQL, see [Security](../../../wellarchitected/latest/framework/security.md "../../../wellarchitected/latest/framework/security.md") in AWS Well-Architected Tool to learn about how cloud technologies improve your
security.

**Amazon CloudWatch Alarms**
Using Amazon CloudWatch alarms, you watch a single
metric over a time period that you specify. If the metric exceeds a given threshold, a notification is sent to an Amazon SNS topic or AWS Auto Scaling policy.
CloudWatch alarms do not invoke actions because they are in a particular state.
Rather the state must have changed and been maintained for a specified number of periods.

**Tag your Aurora DSQL resources for identification and automation**

You can assign metadata to your AWS resources in the form of tags. Each
tag is a simple label consisting of a customer-defined key and an optional
value that can make it easier to manage, search for, and filter resources.

Tagging allows for grouped controls to be implemented. Although there are
no inherent types of tags, they enable you to categorize resources by
purpose, owner, environment, or other criteria. The following are some
examples:

- Security – Used to determine requirements such as
  encryption.
- Confidentiality – An identifier for the specific
  data-confidentiality level a resource supports.
- Environment – Used to distinguish between development,
  test, and production infrastructure.

You can assign metadata to your AWS resources in the form of tags. Each
tag is a simple label consisting of a customer-defined key and an optional
value that can make it easier to manage, search for, and filter
resources.

Tagging allows for grouped controls to be implemented. Although there are
no inherent types of tags, they let you categorize resources by purpose,
owner, environment, or other criteria. The following are some
examples.

- Security – used to determine requirements such as
  encryption.
- Confidentiality – an identifier for the specific
  data-confidentiality level a resource supports.
- Environment – used to distinguish between development,
  test, and production infrastructure.

For more information, see [Best Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").
