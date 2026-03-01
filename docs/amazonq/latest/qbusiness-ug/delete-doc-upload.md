# Deleting documents uploaded in an Amazon Q Business application

To delete documents that have been directly uploaded to an application environment, you can
use the console or the [BatchDeleteDocument](../api-reference/API_BatchDeleteDociment.md "../api-reference/API_BatchDeleteDociment.md") API operation.
You can delete specific documents or all documents.

The following tabs provide a procedure for the AWS Management Console and code examples for the
AWS CLI.

Console
**To delete specific directly uploaded
documents**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of the
   application environment that your uploaded files belong to.
3. From your applications page, from **Data
   sources**, choose **Uploaded
   files**.
4. In **Uploaded files**, choose
   **Document name**, and then select the
   documents that you want to delete.

###### Note

You can choose up to 10 files at a time. 5. Choose **Delete files**.

You are returned to the service console while your
application environment is deleted. When the deletion process is complete,
the console displays a message confirming successful
deletion.

AWS CLI
**To delete documents**

```

aws qbusiness batch-delete-document \
--application-id `application-id` \
--index-id `index-id` \
--documents `documents-to-delete` \
--data-source-sync-id `data-source-sync-id`

```
