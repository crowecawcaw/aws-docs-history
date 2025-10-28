# Deleting tags from a private repository in Amazon ECR

You can delete tags from a private repository.

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, select the region to use.
3. On the **Repositories** page, select the check box next to the repository
   you want to remove a tag from.
4. From the **Action** menu, select **Repository
   tags**.
5. On the **Repository tags** page, select **Edit**.
6. On the **Edit repository tags** page, select **Remove**
   for each tag you want to delete, and choose **Save**.
   You can delete one or more tags by using the AWS CLI or an API.

- AWS CLI - [untag-resource](../../../cli/latest/reference/ecr/untag-resource.md "../../../cli/latest/reference/ecr/untag-resource.md")
- API action - [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

The following example shows how to delete a tag from a repository using the
AWS CLI.

```
`aws ecr untag-resource \
 --resource-arn arn:aws:ecr:`region`:`account_id`:repository/`repository_name` \
 --tag-keys `tag_key``
```
