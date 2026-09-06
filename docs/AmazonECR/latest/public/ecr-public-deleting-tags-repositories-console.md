

# Deleting tags from a public repository in Amazon ECR public
<a name="ecr-public-deleting-tags-repositories-console"></a>

You can delete tags from an individual resource.

------
#### [ AWS Management Console ]

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, select the Region to use.

1. On the **Repositories** page, on the **Public** tab, choose the repository to view.

1. On the **Repositories > {{repository\_name}}** page, select **Tags** from the navigation pane.

1. On the **Tags** page, select **Edit**.

1. On the **Edit tags** page, select **Remove** for each tag you want to delete, and choose **Save**.

------
#### [  AWS CLI ]

You can delete one or more tags by using the AWS CLI or an API.
+ AWS CLI - [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecr-public/untag-resource.html)
+ API action - [UntagResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UntagResource.html)

The following example shows how to delete a tag from an existing public repository.

```
aws ecr-public untag-resource \
      --resource-arn arn:aws:ecr-public::{{account_id}}:repository/{{repository_name}} \
      --tag-keys {{tag_key}} \
      --region us-east-1
```

------