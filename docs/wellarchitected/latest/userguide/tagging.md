# Tagging your AWS WA Tool resources

To help you manage your AWS WA Tool resources, you can assign your own metadata to each resource in the form of
_tags_. This topic describes tags and shows you how to create them.

###### Contents

- [Tag basics](#tag-basics "#tag-basics")
- [Tagging your resources](#tag-resources "#tag-resources")
- [Tag restrictions](#tag-restrictions "#tag-restrictions")
- [Working with tags using the console](#tag-resources-console "#tag-resources-console")
- [Working with tags using the API](#tag-resources-api-sdk "#tag-resources-api-sdk")

## Tag basics

A tag is a label that you assign to an AWS resource. Each tag consists of a _key_ and an
optional _value_, both of which you define.

Tags enable you to categorize your AWS resources by, for example, purpose, owner, or environment. When you
have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned
to it. For example, you can define a set of tags for your AWS WA Tool services to help you track each service's owner and
stack level. We recommend that you devise a consistent set of tag keys for each resource
type.

Tags are not automatically assigned to your resources. After you add a tag, you can edit tag keys and values or
remove tags from a resource at any time. If you delete a resource, any tags for the resource are also deleted.

Tags don't have any semantic meaning to AWS WA Tool and are interpreted strictly as a string of characters. You can
set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has
the same key as an existing tag on that resource, the new value overwrites the old value.

You can work with tags using the AWS Management Console, the AWS CLI, and the AWS WA Tool API.

If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create,
edit, or delete tags.

## Tagging your resources

You can tag new or existing AWS WA Tool resources.

If you're using the AWS WA Tool console, you can apply tags to new resources when they are created
or to existing resources at any time. For existing workloads you can apply tags through the
**Properties** tab. For existing custom lenses, profiles, and review templates
you can apply tags through the **Overview** tab.

If you're using the AWS WA Tool API, the AWS CLI, or an AWS SDK, you can apply tags to new
resources using the `tags` parameter on the relevant API action or to existing
resources using the `TagResource` API action. For more information, see [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md").

Some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags
cannot be applied during resource creation, the resource creation process fails. This ensures that resources you
intended to tag on creation are either created with specified tags or not created at all. If you tag resources at the
time of creation, you don't need to run custom tagging scripts after resource creation.

The following table describes the AWS WA Tool resources that can be tagged, and the resources that can be tagged on
creation.

| Tagging support for AWS WA Tool resources | Resource | Supports tags | Supports tag propagation | Supports tagging on creation (AWS WA Tool API, AWS CLI, AWS SDK) |
| ----------------------------------------- | -------- | ------------- | ------------------------ | ---------------------------------------------------------------- |
| AWS WA Tool workloads                     | Yes      | No            | Yes                      |
| AWS WA Tool custom lenses                 | Yes      | No            | Yes                      |
| AWS WA Tool profiles                      | Yes      | No            | Yes                      |
| AWS WA Tool review templates              | Yes      | No            | Yes                      |

## Tag restrictions

The following basic restrictions apply to tags:

- Maximum number of tags per resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple AWS services and resources, remember that other services may
  have restrictions on allowed characters. Generally allowed characters are letters, numbers, spaces representable in
  UTF-8, and the following characters: + - = . \_ : / @.
- Tag keys and values are case sensitive.
- Don't use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for
  either keys or values, as it is reserved for AWS use. You can't edit or delete tag keys or values with this
  prefix. Tags with this prefix do not count against your tags-per-resource limit.

## Working with tags using the console

Using the AWS WA Tool console, you can manage the tags associated with new or existing
resources.

### Adding tags on an individual resource on

creation

You can add tags to AWS WA Tool resources when you create them.

### Adding and deleting tags on an individual resource

AWS WA Tool allows you to add or delete tags associated with your resources directly from the
**Properties** tab for a workload, and from the **Overview**
tab for custom lenses, profiles, and review templates.

###### To add or delete a tag on a workload

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. From the navigation bar, choose the Region to use.
3. In the navigation pane, choose **Workloads**.
4. Select the workload to modify and choose **Properties**.
5. In the **Tags** section, choose **Manage tags**.
6. Add or delete your tags as necessary.
   - To add a tag, choose **Add new tag** and fill in the
     **Key** and **Value** fields.
   - To delete a tag, choose **Remove**.

7. Repeat this process for each tag you want to add, modify, or delete. Choose
   **Save** to save your changes.

###### To add or delete a tag on a custom lens

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. From the navigation bar, choose the Region to use.
3. In the navigation pane, choose **Custom lenses**.
4. Select the name of the custom lens to modify.
5. In the **Tags** section of the **Overview** tab, choose
   **Manage tags**.
6. Add or delete your tags as necessary.
   - To add a tag, choose **Add new tag** and fill in the
     **Key** and **Value** fields.
   - To delete a tag, choose **Remove**.

7. Repeat this process for each tag you want to add, modify, or delete. Choose
   **Save** to save your changes.

###### To add or delete a tag on a profile

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. From the navigation bar, choose the Region to use.
3. In the navigation pane, choose **Profiles**.
4. Select the name of the profile to modify.
5. In the **Tags** section of the **Overview** tab, choose
   **Manage tags**.
6. Add or delete your tags as necessary.
   - To add a tag, choose **Add new tag** and fill in the
     **Key** and **Value** fields.
   - To delete a tag, choose **Remove**.

7. Repeat this process for each tag you want to add, modify, or delete. Choose
   **Save** to save your changes.

###### To add or delete a tag on a review template

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. From the navigation bar, choose the Region to use.
3. In the navigation pane, choose **Review templates**.
4. Select the name of the review template to modify.
5. In the **Tags** section of the **Overview** tab, choose
   **Manage tags**.
6. Add or delete your tags as necessary.
   - To add a tag, choose **Add new tag** and fill in the
     **Key** and **Value** fields.
   - To delete a tag, choose **Remove**.

7. Repeat this process for each tag you want to add, modify, or delete. Choose
   **Save** to save your changes.

## Working with tags using the API

Use the following AWS WA Tool API operations to add, update, list, and delete the tags for your
resources.

| Tagging support for AWS WA Tool resources | Task                                                                                                           | API action |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------- |
| Add or overwrite one or more tags.        | [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")                         |
| Delete one or more tags.                  | [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                   |
| List tags for a resource.                 | [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") |

Some resource-creating actions enable you to specify tags when you create the resource. The following actions
support tagging on creation.

| Task                     | API action                                                                                                        |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Create a workload        | [CreateWorkload](../APIReference/API_CreateWorkload.md "../APIReference/API_CreateWorkload.md")                   |
| Import a new lens        | [ImportLens](../APIReference/API_ImportLens.md "../APIReference/API_ImportLens.md")                               |
| Create a profile         | [CreateProfile](../APIReference/API_CreateProfile.md "../APIReference/API_CreateProfile.md")                      |
| Create a review template | [CreateReviewTemplate](../APIReference/API_CreateReviewTemplate.md "../APIReference/API_CreateReviewTemplate.md") |
