# Adding tags to a public repository in Amazon ECR public

You can add tags to a public repository.

For information about names and best practices for tags, see [Tag naming limits
and requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions") and [Best
practices](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _Tagging AWS Resources User
Guide_.

When you select a specific repository in the Amazon ECR console, you can view the tags by
selecting **Tags** in the navigation pane.

AWS Management Console

###### To add a tag to a public repository

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, on the
   **Public** tab, choose the repository to view.
5. On the **Repositories >
   `repository_name`** page, select
   **Tags** from the navigation pane.
6. On the **Tags** page, select **Add tags**,
   **Add tag**.
7. On the **Edit Tags** page, specify the key and value for each
   tag, and then choose **Save**.

AWS CLI
You can add or overwrite one or more tags by using the AWS CLI or an API.

- AWS CLI - [tag-resource](../../../AmazonECRPublic/latest/APIReference/API_TagResource.md "../../../AmazonECRPublic/latest/APIReference/API_TagResource.md")
- API action - [TagResource](../../../AmazonECRPublic/latest/APIReference/API_UntagResource.md "../../../AmazonECRPublic/latest/APIReference/API_UntagResource.md")

The following examples show how to manage tags using the AWS CLI.

###### Example 1: Tag an existing public repository

The following command tags an existing public repository.

```
`aws ecr-public tag-resource \
 --resource-arn arn:aws:ecr-public::`account_id`:repository/`repository_name` \
 --tags Key=`stack`,Value=`dev` \
 --region us-east-1`
```

###### Example 2: Tag an existing public repository with multiple tags

The following command tags an existing repository.

```
`aws ecr-public tag-resource \
 --resource-arn arn:aws:ecr-public::`account_id`:repository/`repository_name` \
 --tags Key=`key1`,Value=`value1` Key=`key2`,Value=`value2` Key=`key3`,Value=`value3` \
 --region us-east-1`
```

###### Example 3: List tags for a public repository

The following command lists the tags that are associated with an existing public
repository.

```
`aws ecr-public list-tags-for-resource \
 --resource-arn arn:aws:ecr-public::`account_id`:repository/`repository_name` \
 --region us-east-1`
```

###### Example 4: Create a public repository and apply a tag

The following command creates a public repository that's named `test-repo` and
adds a tag with key `team` and value `devs`.

```
`aws ecr-public create-repository \
 --repository-name `test-repo` \
 --tags Key=`team`,Value=`devs` \
 --region us-east-1`
```
