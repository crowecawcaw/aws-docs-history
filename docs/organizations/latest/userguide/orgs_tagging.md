# Tagging AWS Organizations resources

A _tag_ is a custom attribute label that you add to an AWS resource
to make it easier to identify, organize, and search for resources. Each tag has two
parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, or `Project`). Tag keys can be up to 128
  characters in length and are case sensitive.
- A _tag value_ (for example, `111122223333`
  or `Production`). Tag values can be up to 256 characters in length, and
  like tag keys, are case sensitive. You can set the value of a tag to an empty
  string, but you can't set the value of a tag to null. Omitting the tag value is the
  same as using an empty string.
  For more information about what characters are allowed in a tag key or value, see the
  [Tags
  parameter of the Tag API](../../../ARG/latest/APIReference/API_Tag.md#ARG-Tag-request-Tags "../../../ARG/latest/APIReference/API_Tag.md#ARG-Tag-request-Tags") in the _Resource Groups Tagging API Reference_.

You can use tags to categorize resources by purpose, owner, environment, or other
criteria. For more information, see [Best
Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").

###### Tip

Use [tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md") to help
standardize your implementation of tags across the resources in your organization's
accounts.

###### Topics

- [Considerations](#orgs_tagging_considerations "#orgs_tagging_considerations")
- [Using tags](use-tags.md "use-tags.md")
- [Adding, updating, and removing tags](add-tag.md "add-tag.md")

## Considerations

AWS Organizations supports the following tagging operations when you are logged in to
the management account:

**You can add tags to the following organization resources**

- AWS accounts
- Organizational units
- The organization's root
- Policies

**You can add tags at the following times**

- [When you create the resource](add-tag.md#add-tag-new "add-tag.md#add-tag-new") — Specify
  the tags in either the Organizations console, or use the `Tags` parameter with one
  of the `Create` API operations. This isn't applicable to the
  organization's root.
- [After you create the resource](add-tag.md#add-tag-existing "add-tag.md#add-tag-existing") — Use
  the Organizations console, or call the `TagResource`
  operation.

**Other considerations**

You can view the tags on any of the taggable resources in AWS Organizations by using the console or
by calling the `ListTagsForResource`
operation.

You can remove tags from a resource by specifying the keys to remove by using the console
or by calling the `UntagResource`
operation.
