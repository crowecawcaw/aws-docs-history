**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Use Amazon Pinpoint tags in IAM policies and API operations

After you start implementing tags, you can apply tag-based, resource-level permissions
to AWS Identity and Access Management (IAM) policies and API operations. This includes operations that support
adding tags to resources when resources are created. By using tags in this way, you can
implement granular control of which groups and users in your AWS account have
permission to create and tag resources, and which groups and users have permission to
create, update, and remove tags more generally.

For example, you can create a policy that allows a user to have full access to all the
Amazon Pinpoint resources where their name is a value in the `Owner` tag for the
resource:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ModifyResourceIfOwner",
 "Effect": "Allow",
 "Action": "mobiletargeting:*",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/Owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

If you define tag-based, resource-level permissions, the permissions take effect
immediately. This means that your resources are more secure as soon as they're created,
and you can quickly start enforcing the use of tags for new resources. You can also use
resource-level permissions to control which tag keys and values can be associated with
new and existing resources. For more information, see [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_AWS IAM User Guide_.
