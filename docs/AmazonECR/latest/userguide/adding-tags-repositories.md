

# Adding tags to a private repository in Amazon ECR
<a name="adding-tags-repositories"></a>

You can add tags to a private repository.

For information about names and best practices for tags, see [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions) and [Best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *Tagging AWS Resources User Guide*.

## Adding tags to a repository (AWS Management Console)
<a name="tag-resources-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, select the region to use.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, select the check box next to the repository you want to tag.

1. From the **Action** menu, select **Repository tags**.

1. On the **Repository tags** page, select **Add tags**, **Add tag**.

1. On the **Edit repository tags** page, specify the key and value for each tag, and then choose **Save**.

## Adding tags to a repository (AWS CLI or API)
<a name="tag-resources-api-sdk"></a>

You can add or overwrite one or more tags by using the AWS CLI or an API.
+ AWS CLI - [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecr/tag-resource.html)
+ API action - [TagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TagResource.html)

The following examples show how to add tags using the AWS CLI.

**Example 1: Tag a repository**  
The following command tags a repository.

```
aws ecr tag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tags Key={{stack}},Value={{dev}}
```

**Example 2: Tag a repository with multiple tags**  
The following command adds three tags to a repository.

```
aws ecr tag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tags Key={{key1}},Value={{value1}} Key={{key2}},Value={{value2}} Key={{key3}},Value={{value3}}
```

**Example 3: List tags for a repository**  
The following command lists the tags associated with a repository.

```
aws ecr list-tags-for-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}}
```

**Example 4: Create a repository and add a tag**  
The following command creates a repository named `test-repo` and adds a tag with key `team` and value `devs`.

```
aws ecr create-repository \
     --repository-name {{test-repo}} \
     --tags Key={{team}},Value={{devs}}
```