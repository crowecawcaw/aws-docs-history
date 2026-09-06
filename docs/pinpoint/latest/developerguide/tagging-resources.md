

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Manage Amazon Pinpoint resource tags
<a name="tagging-resources"></a>

A *tag* is a label that you optionally define and associate with AWS resources, including certain types of Amazon Pinpoint resources. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. For example, you can use tags to apply policies or automation, or to identify resources that are subject to certain compliance requirements. You can add tags to the following types of Amazon Pinpoint resources:
+ Campaigns
+ Message templates
+ Projects (applications)
+ Segments

A resource can have as many as 50 tags. Each tag consists of a required *tag key* and an optional *tag value*, both of which you define. A *tag key* is a general label that acts as a category for more specific tag values. A *tag value* acts as a descriptor for a tag key.

A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, numbers, white space, or one of the following symbols: \_ . : / = \+ -. The following additional restrictions apply to tags:
+ Tag keys and values are case sensitive.
+ For each associated resource, each tag key must be unique and it can have only one value.
+ The `aws:` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can't edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the quota of 50 tags per resource.
+ You can't update or delete a resource based only on its tags. You must also specify the Amazon Resource Name (ARN) or resource ID, depending on the operation that you use.
+ You can associate tags with public or shared resources. However, the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

To add, display, update, and remove tag keys and values from Amazon Pinpoint resources, you can use the AWS Command Line Interface (AWS CLI), the Amazon Pinpoint API, the AWS Resource Groups Tagging API, or an AWS SDK. To manage tag keys and values across all the AWS resources that are located in a specific AWS Region for your AWS account (including Amazon Pinpoint resources), use the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html).

For more information about the CLI commands that you can use to manage Amazon Pinpoint resources, see the Amazon Pinpoint section of the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/).

For more information about resources in the Amazon Pinpoint API, including supported HTTP(S) methods, parameters, and schemas, see the [Amazon Pinpoint API Reference](https://docs.aws.amazon.com/pinpoint/latest/apireference/).