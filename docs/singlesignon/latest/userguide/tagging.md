# Tagging AWS IAM Identity Center resources

A *tag* is a custom attribute label that you add to an AWS resource
 to make it easier to identify, organize, and search for resources. Each tag has two
 parts:


* A *tag key* (for example, `CostCenter`,
 `Environment`, or `Project`). Tag keys can be up to 128
 characters in length and are case sensitive.
* A *tag value* (for example, `111122223333`
 or `Production`). Tag values can be up to 256 characters in length, and
 like tag keys, are case sensitive. You can set the value of a tag to an empty
 string, but you cannot set the value of a tag to null. Omitting the tag value is the
 same as using an empty string.
Tags help you identify and organize your AWS resources. Many AWS services support
 tagging, so you can assign the same tag to resources from different services to indicate
 that the resources are related. For example, you can assign the same tag to a specific
 permission set in your instance of IAM Identity Center. For more information about tagging strategies, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html")
 in the *AWS General Reference Guide* and [Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html "https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html").

In addition to identifying, organizing, and tracking your AWS resources with tags, you can use
 tags in IAM policies to help control who can view and interact with your resources. To
 learn more about using tags to control access, see [Controlling access to AWS resources using
 tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html") in the *IAM User Guide*. For example,
 you can allow a user to update an IAM Identity Center permission set, but only if the IAM Identity Center permission set
 has an `owner` tag with a value of that user's name.

You can apply tags to permission sets only. You cannot apply tags to the corresponding
 roles that IAM Identity Center creates in AWS accounts. You can use the IAM Identity Center console, AWS CLI or the
 IAM Identity Center APIs to add, edit, or delete tags for a permission set.

The following sections provide more information about tags for IAM Identity Center.

###### Topics

* [Tag restrictions](#tagging-restrictions "#tagging-restrictions")
* [Manage tags by using the IAM Identity Center console](tagging-console.md "tagging-console.md")
* [AWS CLI examples](tagging-cli-examples.md "tagging-cli-examples.md")
* [Manage tags using the IAM Identity Center API](tagging-api.md "tagging-api.md")

## Tag restrictions


The following basic restrictions apply to tags on IAM Identity Center resources:



* The maximum number of tags that you can assign to a resource is 50.
* The maximum key length is 128 Unicode characters.
* The maximum value length is 256 Unicode characters.
* Valid characters for a tag key and value are: 


a-z, A-Z, 0-9, space, and the
 following characters: \_ . : / = + - and @
* Keys and values are case sensitive.
* Don't use `aws:` as a prefix for keys; it is reserved for AWS
 use
