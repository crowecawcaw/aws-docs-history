# Uploading files

To upload documents directly to an Amazon Q Business application environment, you can use
the AWS Management Console or the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation.

If you use an Amazon Kendra index to retrieve your documents, you can't directly
upload documents.

###### Note

This procedure is available if you chose to create a new Amazon Q Business index for your
application environment. Files can only be uploaded after the Amazon Q Business index
and retriever creation process has completed.

The following tabs provide a procedure for the AWS Management Console and code examples for the
AWS CLI.

Console
**To upload files**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. Complete the steps to create your Amazon Q Business
   application.
3. Complete the steps for [creating an Amazon Q Business
   index](select-retriever.md#native-retriever "select-retriever.md#native-retriever").
4. Then, from the left navigation menu, choose **Data
   sources**.
5. From the **Data sources** page, choose
   **Add data source**.
6. Then, on the **Add data sources** page, from
   **Data sources** choose **Upload
   files**.
7. Then, in **Upload files**, select one of the
   following methods to add your files:
   - Drag and drop the document files that you want to
     upload.
   - Add your documents to the application environment, and then select
     **Choose files**.

8. After choosing your files, choose
   **Upload**.

You are returned to the Amazon Q Business console while your
documents are uploaded. The console displays a confirmation message
when your documents are successfully uploaded.

AWS CLI
**To upload documents directly**

```

aws qbusiness batch-put-document \
--application-id `application-id` \
--index-id `index-id` \
--documents `documents-to-add` \
--data-source-sync-id `data-source-sync-id` \
--role-arn `roleArn`

```
