# Adding tags to a private repository in Amazon ECR

You can add tags to a private repository.

For information about names and best practices for tags, see [Tag naming limits
and requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions") and [Best
practices](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _Tagging AWS Resources User
Guide_.

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, select the region to use.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, select the check box next to the repository
   you want to tag.
5. From the **Action** menu, select **Repository
   tags**.
6. On the **Repository tags** page, select **Add tags**,
   **Add tag**.
7. On the **Edit repository tags** page, specify the key and value for each
   tag, and then choose **Save**.
   You can add or overwrite one or more tags by using the AWS CLI or an API.

- AWS CLI - [tag-resource](../../../cli/latest/reference/ecr/tag-resource.md "../../../cli/latest/reference/ecr/tag-resource.md")
- API action - [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
  The following examples show how to add tags using the AWS CLI.

###### Example 1: Tag a repository

The following command tags a repository.

```
`aws ecr tag-resource \
 --resource-arn arn:aws:ecr:`region`:`account_id`:repository/`repository_name` \
 --tags Key=`stack`,Value=`dev``
```

###### Example 2: Tag a repository with multiple tags

The following command adds three tags to a repository.

```
`aws ecr tag-resource \
 --resource-arn arn:aws:ecr:`region`:`account_id`:repository/`repository_name` \
 --tags Key=`key1`,Value=`value1` Key=`key2`,Value=`value2` Key=`key3`,Value=`value3``
```

###### Example 3: List tags for a repository

The following command lists the tags associated with a repository.

```
`aws ecr list-tags-for-resource \
 --resource-arn arn:aws:ecr:`region`:`account_id`:repository/`repository_name``
```

###### Example 4: Create a repository and add a tag

The following command creates a repository named `test-repo` and adds a
tag with key `team` and value `devs`.

```
`aws ecr create-repository \
 --repository-name `test-repo` \
 --tags Key=`team`,Value=`devs``
```
