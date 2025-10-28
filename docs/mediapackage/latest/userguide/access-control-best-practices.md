# Access control best practices for

AWS Elemental MediaPackage

MediaPackage provides a variety of security features and tools. The following topics describe some
tools and settings that you might want to use to help control access when performing certain
tasks or operating in specific environments. Proper application of these tools can help maintain
the integrity of your data and help ensure that your resources are accessible to the intended
users.

###### Topics

- [Creating new resources](#access-control-best-practices-new-resources "#access-control-best-practices-new-resources")
- [Sharing resources](#access-control-best-practices-groups "#access-control-best-practices-groups")
- [Protecting data](#access-control-best-practices-groups "#access-control-best-practices-groups")

## Creating new resources

When creating new resources, you should apply the following tools and settings to help
ensure that your MediaPackage resources are protected.

###### Grant access with IAM identities

When setting up accounts for new team members who require MediaPackage access, use IAM users and
roles to ensure least privileges. You can also implement a form of IAM multi-factor
authentication (MFA) to support a strong identity foundation. Using IAM identities, you
can grant unique permissions to users and specify what resources they can access and what
actions they can take. IAM identities provide increased capabilities, including the
ability to require users to enter login credentials before accessing shared resources and
apply permission hierarchies to different objects within a single bucket.

For more information, see [Identity and Access Management for AWS Elemental MediaPackage](security-iam.md "security-iam.md").

###### Resource policies

With resource policies, you can personalize channel and origin endpoint access to help ensure that only those
users you have approved can access resources and perform actions within them. In addition to
resource policies, you should use resource-level Block Public Access settings to further limit
public access to your data.

For more information, see [Resource-based policy examples](using-iam-policies.md "using-iam-policies.md").

When creating policies, avoid the use of wildcard characters in the `Principal`
element because it effectively allows anyone to access your MediaPackage resources. It's better to
explicitly list users or groups that are allowed to access the resource. Rather than including a
wildcard for their actions, grant them specific permissions when applicable.

To further maintain the practice of least privileges, `Deny` statements in the
`Effect` element should be as broad as possible and `Allow` statements
should be as narrow as possible. `Deny` effects paired with the "`mediapackagev2:*`"
action are another good way to implement opt-in best practices for the users included in
policy condition statements.

## Sharing resources

There are several different ways that you can share resources with a specific group of
users. You can use the following tools to share a set of documents or other resources to a
single group of users, department, or an office. Although they can all be used to accomplish
the same goal, some tools might pair better than others with your existing settings.

###### User policies

You can share resources with a limited group of people using IAM groups and user
policies. When creating a new IAM user, you are prompted to create and add them to a
group. However, you can create and add users to groups at any point. If the individuals you
intend to share these resources with are already set up within IAM, you can add them to a
common group and share the bucket with their group within the user policy. You can also use
IAM user policies to share individual objects within a bucket.

For more information, see [Identity-based policy
examples for MediaPackage](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### Tagging

If you use object tagging to categorize storage, you can share objects that have been
tagged with a specific value with specified users. Resource tagging allows you to control
access to objects based on the tags associated with the resource that a user is trying to
access. To do this, use the `ResourceTag/key-name` condition within an IAM user
policy to allow access to the tagged resources.

For more information, see [Controlling access to AWS resources using
resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

## Protecting data

Use the following tools to help protect data in transit and at rest, both of which are
crucial in maintaining the integrity and accessibility of your data.

###### Signing methods

AWS Signature Version 4 is the process of adding authentication information to AWS
requests sent by HTTP. For security, most requests to AWS must be signed with an access
key, which consists of an access key ID and secret access key. These two keys are commonly
referred to as your security credentials. For more information, see [Authenticating Requests (AWS Signature Version 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md")
and [Signing AWS
API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User Guide_.
