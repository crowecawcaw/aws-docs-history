# Delete a project

The act of deleting a project is final. Deletion irrevocably deletes the project’s
contents, including compute instances, data sources, queries, and more, and all the content
within those project resources. Deleting a project does not delete non-Amazon SageMaker Unified Studio AWS
resources that Amazon SageMaker Unified Studio might have helped you create. If you no longer need these AWS
resources, delete them in their respective AWS service and account. For example, if you
create Amazon Bedrock model evaluation jobs in Amazon Bedrock in SageMaker Unified Studio, the jobs that aren't automatically
deleted when you delete the project. You will need to use the Amazon Bedrock console to delete the
model evaluation jobs. Contact your administrator if you don't have access to the
Amazon Bedrock in SageMaker Unified Studio console.

To delete an Amazon SageMaker Unified Studio project, you must be an owner of the project.

To delete an existing project, complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select a project**.
3. If you don't see the name of your project under **Recently updated
   projects**, choose **Browse all projects**.
4. Choose the project that you want to delete. If you don't readily see it in the list of
   projects, you can search for it by specifying the project name in the **Search
   projects** field.
5. On the **Project overview** page, expand **Actions**
   and choose **Delete project**.

Review the informational warnings about the potential impact of deleting the
project. 6. If you accept the warnings, then type in the confirmation text and choose
**Delete project**.

###### Important

Deleting a project is an irrevocable action that cannot be undone by you or by
AWS.
