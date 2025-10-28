# Develop and implement a tagging strategy

Obtaining contextual information on the business use case and relevant internal stakeholders surrounding an AWS resource can be difficult.
One way to do this is in the form of tags, which assign metadata to your AWS resources and consist of a user-defined key and value.
You can create tags to categorize resources by purpose, owner, environment, type of data processed, and other criteria of your choice.

Having a consistent tagging strategy can speed up response times by allowing
you to quickly identify and discern contextual information about an AWS resource.
Tags can also serve as a mechanism to initiate response automations. For further
information on what to tag, refer to the
[documentation on tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").
You’ll want to first define the tags you want to implement across your organization.
After that, you’ll implement and enforce this tagging strategy. Details on
implementation and enforcement can be found in the AWS blog
[Implement
AWS resource tagging strategy using AWS Tag Policies and Service Control Policies (SCPs)](https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/ "https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/").
