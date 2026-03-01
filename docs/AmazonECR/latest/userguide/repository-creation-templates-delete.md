# Deleting a repository creation template in Amazon ECR

You can delete a repository creation template if you are finished using it. Once a
repository creation template is deleted, any newly created repositories under the
associated prefix during a pull through cache or replication action will inherit the
default settings, unless another matching template is found, see [How repository creation templates work](repository-creation-templates.md#repository-creation-templates-works "repository-creation-templates.md#repository-creation-templates-works").

###### Important

This doesn't have any effect on any previously created repositories.

AWS Management Console

###### To delete a repository creation template (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region the repository creation
   template to delete is in.
3. In the navigation pane, choose **Private
   registry**, **Repository creation
   templates**.
4. On the **Repository creation templates** page,
   select the repository creation template to delete.
5. From the **Actions** dropdown menu, choose
   **Delete**.

AWS CLI

###### To delete a repository creation template (AWS CLI)

- Use the [delete-repository-creation-template.html](../../../cli/latest/reference/ecr/delete-repository-creation-template.md "../../../cli/latest/reference/ecr/delete-repository-creation-template.md") command to
  delete an existing repository creation template. You must specify
  the `prefix` value of the template. The following example
  deletes a repository creation template with the `prod`
  prefix.

```
`aws ecr delete-repository-creation-template \
 --prefix `prod``
```

The output of the command displays the details of the deleted
repository creation template.
