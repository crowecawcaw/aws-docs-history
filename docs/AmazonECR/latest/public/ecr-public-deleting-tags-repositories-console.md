# Deleting tags from a public repository in Amazon ECR public

You can delete tags from an individual resource.

AWS Management Console

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, select the Region to use.
3. On the **Repositories** page, on the
   **Public** tab, choose the repository to view.
4. On the **Repositories >
   `repository_name`** page, select
   **Tags** from the navigation pane.
5. On the **Tags** page, select
   **Edit**.
6. On the **Edit tags** page, select **Remove**
   for each tag you want to delete, and choose **Save**.

AWS CLIYou can delete one or more tags by using the AWS CLI or an API.

- AWS CLI - [untag-resource](../../../cli/latest/reference/ecr-public/untag-resource.md "../../../cli/latest/reference/ecr-public/untag-resource.md")
- API action - [UntagResource](../../../AmazonECRPublic/latest/APIReference/API_UntagResource.md "../../../AmazonECRPublic/latest/APIReference/API_UntagResource.md")

The following example shows how to delete a tag from an existing public repository.

```
`aws ecr-public untag-resource \
 --resource-arn arn:aws:ecr-public::`account_id`:repository/`repository_name` \
 --tag-keys `tag_key` \
 --region us-east-1`
```
