AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Adding tags to views

You can add tags to your views to categorize them. Tags are customer-supplied metadata
that take the form of a key name string and an associated optional value string. For general
information about tagging AWS resources, see [Tagging AWS Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
_Amazon Web Services General Reference_.

## Add tags to your views

You can add tags to your Resource Explorer views by using the AWS Management Console or by running AWS CLI commands or their equivalent API
operations in an AWS SDK.

AWS Management Console

###### To add tags to a view

1. Open the Resource Explorer **[Views](https://console.aws.amazon.com/resource-explorer/home#/views "https://console.aws.amazon.com/resource-explorer/home#/views")** page and choose the name of the view
   that you want to tag to display its **Details**
   page.
2. Under **Tags**, choose **Manage
   tags**.
3. To add a tag, choose **Add tag** and then enter a
   tag key name and optional value.

###### Note

You can also delete a tag by choosing the
**X** next to the tag.

You can attach up to 50 user-defined tags to a resource. Any tags
that are created and managed automatically by AWS don't count
against this quota. 4. When you're done with all tag changes, choose **Save
changes**.

AWS CLI

###### To add tags to a view

Run the following command to add tags to a view. The following example
add tags with the key name `environment` and the value
`production` to the specified view.

```
`$` `aws resource-explorer-2 tag-resource \
 --resource-id arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyViewName/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111 \
 --tags environment=production`
```

The preceding command produces no output if it succeeds.

###### Note

To remove an existing tag from a view, use the
`untag-resource` command.

## Controlling permissions with tags

One key use of tagging is to support an [attribute-based access control (ABAC) strategy](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). ABAC can help simplify
permission management by letting you tag resources. Then, you grant permission to users
for resources that are tagged a certain way.

For example, consider this scenario. For a view called `ViewA`, you attach
the tag `environment=prod` (_key
name=value_). Another `ViewB` might be tagged
`environment=beta`. You tag your roles and users with the same tags and
values, based on which environment each role or user should be able to access.

Then, you could assign an AWS Identity and Access Management (IAM) permission policy to your IAM roles,
groups, and users. The policy grants permission to access and search using a view only
if the role or user making the search request has an `environment` tag with
the same value as the `environment` tag attached to the view.

The benefit to this approach is that it's dynamic and doesn't require you to maintain
a list of who has access to which resources. Instead, you ensure that all resources
(your views) and principals (IAM roles and users) are tagged properly. Then, the
permissions update automatically without you having to change any policies.

## Referencing tags in an ABAC policy

After your views are tagged, you can choose to use those tags to control access
dynamically to those views. The following example policy assumes that both your IAM
principals and your views are tagged with the tag key `environment` and some
value. When that is done, you can attach the following example policy to your
principals. Your roles and users can then `Search` using any views that are
tagged with an `environment` tag value that exactly matches the
`environment` tag attached to the principal.

If both the principal and view have the `environment` tag but the values
don't match, or if either is missing the `environment` tag then Resource Explorer denies
the search request.

For more information about using ABAC to securely grant access to your resources, see
[What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
