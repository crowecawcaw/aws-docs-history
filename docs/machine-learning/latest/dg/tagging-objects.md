We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Tagging Your Amazon ML Objects

Organize and manage your Amazon Machine Learning (Amazon ML) objects by assigning metadata to them with tags. A
_tag_ is a key-value pair that you define for an object.

In addition to using tags to organize and manage your Amazon ML objects, you can use them to
categorize and track your AWS costs. When you apply tags to your AWS objects, including ML
models, your AWS cost allocation report includes usage and costs aggregated by tags. By applying
tags that represent business categories (such as cost centers, application names, or owners),
you can organize your costs across multiple services. For more information, see [Use Cost Allocation Tags for Custom Billing
Reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

###### Contents

- [Tag Basics](#tagging-basics "#tagging-basics")
- [Tag Restrictions](#tagging-restrictions "#tagging-restrictions")
- [Tagging Amazon ML Objects (Console)](#tagging-console "#tagging-console")
- [Tagging Amazon ML Objects (API)](#tagging-api "#tagging-api")

## Tag Basics

Use tags to categorize your objects to make it easier to manage them. For example, you
could categorize objects by purpose, owner, or environment. Then, you might define a set of
tags that helps you track models by owner and associated application. Here are several
examples:

- Project: Project name
- Owner: Name
- Purpose: Marketing predictions
- Application: Application name
- Environment: Production

You use the Amazon ML console or API to complete the following tasks:

- Add tags to an object
- View the tags for your objects
- Edit the tags for your objects
- Delete tags from an object

By default, tags applied to an Amazon ML object are copied to objects created using that
object. For example, if an Amazon Simple Storage Service (Amazon S3) datasource has the "Marketing cost: Targeted
marketing campaign" tag, a model created using that datasource would also have the "Marketing
cost: Targeted marketing campaign" tag, as would the evaluation for the model. This allows you
to use tags to track related objects, such as all of the objects used for a marketing
campaign. If there is a conflict between tag sources, such as a model with the tag "Marketing
cost: Targeted marketing campaign" and a datasource with the tag "Marketing cost: Target
marketing customers", Amazon ML applies the tag from the model.

## Tag Restrictions

The following restrictions apply to tags.

Basic restrictions:

- The maximum number of tags per object is 50.
- Tag keys and values are case sensitive.
- You can't change or edit tags for a deleted object.

Tag key restrictions:

- Each tag key must be unique. If you add a tag with a key that's already in use, your
  new tag overwrites the existing key-value pair for that object.
- You can't start a tag key with `aws:` because this prefix is reserved for
  use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't
  edit or delete them.
- Tag keys must be between 1 and 128 Unicode characters in length.
- Tag keys must consist of the following characters: Unicode letters, digits, white
  space, and the following special characters: `_ . / = + - @`.

Tag value restrictions:

- Tag values must be between 0 and 255 Unicode characters in length.
- Tag values can be blank. Otherwise, they must consist of the following characters:
  Unicode letters, digits, white space, and any of the following special characters: `_
. / = + - @`.

## Tagging Amazon ML Objects (Console)

You can view, add, edit, and delete tags using the Amazon ML console.

###### To view the tags for an object (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. In the navigation bar, expand the region selector and choose a region.
3. On the **Objects** page, choose an object.
4. Scroll to the **Tags** section of the chosen object. The tags for that object are listed
   at the bottom of the section.

###### To add a tag to an object (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. In the navigation bar, expand the region selector and choose a region.
3. On the **Objects** page, choose an object.
4. Scroll to the **Tags** section of the chosen object. The tags for that object are listed
   at the bottom of the section.
5. Choose **Add or edit tags**.
6. Under **Add Tag**, specify the tag key in the
   **Key** field, optionally specify a tag value in the
   **Value** field, and then choose **Apply
   changes**.

If the **Apply changes** button isn't enabled, either the tag key or
tag value that you specified doesn't meet the tag restrictions. For more information, see
[Tag Restrictions](#tagging-restrictions "#tagging-restrictions"). 7. To view your new tag in the list in the **Tags** section, refresh the
page.

###### To edit a tag (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. In the navigation bar, expand the region selector and select a region.
3. On the **Objects** page, choose an object.
4. Scroll to the **Tags** section of the chosen object. The tags for that object are listed
   at the bottom of the section.
5. Choose **Add or edit tags**.
6. Under **Applied tags**, edit the a tag value in the
   **Value** field, and then choose **Apply
   changes**.

If the **Apply changes** button is not enabled, the tag value that
you specified doesn't meet the tag restrictions. For more information, see [Tag Restrictions](#tagging-restrictions "#tagging-restrictions"). 7. To view your updated tag in the list in the **Tags** section, refresh
the page.

###### To delete a tag from an object (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. In the navigation bar, expand the region selector and choose a region.
3. On the **Objects** page, choose an object.
4. Scroll to the **Tags** section of the chosen object. The tags for that object are listed
   at the bottom of the section.
5. Choose **Add or edit tags**.
6. Under **Applied tags**, choose the tag that you want to delete, and
   then choose **Apply changes**.

## Tagging Amazon ML Objects (API)

You can add, list, and delete tags using the Amazon ML API. For examples, see the following
documentation:

[AddTags](../APIReference/API_AddTags.md "../APIReference/API_AddTags.md")

Adds or edits tags for the specified object.

[DescribeTags](../APIReference/API_DescribeTags.md "../APIReference/API_DescribeTags.md")

Lists the tags for the specified object.

[DeleteTags](../APIReference/API_DeleteTags.md "../APIReference/API_DeleteTags.md")

Deletes tags from the specified object.
