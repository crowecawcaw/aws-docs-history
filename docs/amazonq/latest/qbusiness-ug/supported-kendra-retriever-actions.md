# Managing Amazon Kendra

indices

To manage Amazon Kendra indices being used as retrievers, you can take the following
actions:

###### Actions

- [Detaching an Amazon Kendra
  index](#detach-kendra-retriever "#detach-kendra-retriever")
- [Updating an Amazon Kendra index](#edit-kendra-index "#edit-kendra-index")
- [Deleting an Amazon Kendra
  index](#delete-kendra-index "#delete-kendra-index")
- [Deleting an Amazon Kendra
  retriever](#delete-kendra-retriever "#delete-kendra-retriever")
- [Getting properties of an Amazon Kendra retriever](#describe-kendra-retriever "#describe-kendra-retriever")
- [Listing Amazon Kendra
  indices](#list-kendra-retriever "#list-kendra-retriever")
- [Updating an Amazon Kendra
  retriever](#update-kendra-retriever "#update-kendra-retriever")

## Detaching an Amazon Kendra

index

To detach an Amazon Kendra index, you can use the console or the [DeleteRetriever](../api-reference/API_DeleteRetriever.md "../api-reference/API_DeleteRetriever.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To detach an Amazon Kendra
index**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application from the list of applications.
3. From the left navigation menu, choose **Data
   sources**.
4. In the **Data sources** page, from
   **Index**, select
   **Edit**.
5. In **Edit index**, choose to update index
   units provisioned from **Number of units**.
6. Select **Update** to save your
   changes.
7. In **Applications**, choose
   **Actions**.
8. Choose **Detach**.
9. In the dialog box that opens, type
   `confirm` to confirm deletion, and
   then choose **Detach**.

You are returned to the service console while your index
is detached and your retriever is deleted. When the process
is complete, the console displays a message confirming
successful detachment.

AWS CLI
**To detach an Amazon Kendra
index**

```

aws qbusiness delete-retriever \
--application-id `application-id` \
--retriever-id `retriever-id`

```

## Updating an Amazon Kendra index

To update an Amazon Kendra index, you can use the Amazon Q Business console or
the Amazon Kendra [UpdateIndex](../../../kendra/latest/APIReference/API_UpdateIndex.md "../../../kendra/latest/APIReference/API_UpdateIndex.md") API
operation.

###### Note

You can't update an Amazon Kendra Developer edition index. You can only update an
Amazon Kendra Enterprise Edition index or Amazon Kendra GenAI Enterprise Edition
index.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To update an Amazon Kendra
index**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application from the list of applications.
3. From the left navigation menu, choose **Data
   sources**.
4. In the **Data sources** page, from
   **Index**, select
   **Edit**.
5. In **Edit index**, choose between the
   following values to update"
   - **Storage capacity** –
     Update your storage capacity to a value between 1-50
     units. Each unit contains 20,000 documents. Index
     capacity must be more than the data stored in your
     index. If you need to, delete data and re-sync your
     data sources before adjusting capacity.
   - **Query capacity** –
     Update your query capacity between 1-100 units. Each
     unit is 0.1 queries per second (QPS), or about 8000
     queries per day.

6. Select **Update** to save your
   changes.

AWS CLI
**To update an Amazon Kendra
index**

```


aws kendra update-index \
--id `index-id` \
--capacity-units '{"QueryCapacityUnits": `2`, "StorageCapacityUnits": `1`}'

```

## Deleting an Amazon Kendra

index

To detach an Amazon Kendra index, you can use the Amazon Kendra console or the Amazon Kendra [DeleteIndex](../../../kendra/latest/APIReference/API_DeleteIndex.md "../../../kendra/latest/APIReference/API_DeleteIndex.md") API operation.

Deleting an index removes the index and all associated data sources and
document data. Deleting an index doesn't remove the original documents from your
storage.

Deleting an index is an asynchronous operation. When you start deleting an
index, the index status changes to `DELETING`. It remains in the
`DELETING` state until all of the information related to the
index is removed. Once the index is deleted, it no longer appears in the results
of a call to the Amazon Kendra [ListIndices](../../../kendra/latest/APIReference/API_ListIndices.md "../../../kendra/latest/APIReference/API_ListIndices.md")
API. If you call the Amazon Kendra [DescribeIndex](../../../kendra/latest/APIReference/API_DescribeIndex.md "../../../kendra/latest/APIReference/API_DescribeIndex.md") API with the deleted index's identifier, you receive
and `ResourceNotFound` exception.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To delete an Amazon Kendra
index**

1. Sign in to the AWS Management Console and open the Amazon Kendra console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. In the navigation pane, choose
   **Indexes**, and then choose the index
   to delete.
3. Choose **Delete** to delete the selected
   index.

AWS CLI
**To delete an Amazon Kendra
index**

```

aws kendra delete-index \
--id `index-id`

```

## Deleting an Amazon Kendra

retriever

To delete an Amazon Kendra retriever, you can use the console or the [DeleteRetriever](../api-reference/API_DeleteRetriever.md "../api-reference/API_DeleteRetriever.md") API
operation.

If you use the console, the only ways to delete your Amazon Kendra
retriever from your Amazon Q Business application environment is to [detach your Amazon Kendra index](supported-kendra-retriever-actions.md#detach-kendra-retriever "supported-kendra-retriever-actions.md#detach-kendra-retriever") from the Amazon Q Business application or delete your Amazon Q Business
application environment.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI for the second scenario.

Console
**To delete an Amazon Kendra
retriever**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, choose
   **Actions**.
3. Choose **Delete**.
4. In the dialog box that opens, type
   `Delete` to confirm deletion, and
   then choose **Delete**.

You are returned to the service console while your
application environment is deleted. When the deletion process is
complete, the console displays a message confirming
successful deletion.

AWS CLI
**To delete an Amazon Kendra
retriever**

```

aws qbusiness delete-retriever \
--application-id `application-id` \
--retriever-id `retriever-id`

```

## Getting properties of an Amazon Kendra retriever

To get the properties of an Amazon Kendra retriever, you can use the console or the
[GetRetriever](../api-reference/API_AddRetriever.md "../api-reference/API_AddRetriever.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To get the properties of an Amazon Kendra retriever**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of applications.
3. From the left navigation menu, choose **Data
   sources**.
4. On the **Data sources** page, under
   **Index** the following settings are
   available:
   - **Retriever** – The type
     of retriever that you're using.
   - **Document count** – The
     number of documents that are attached to your index.
   - **Last modified time** –
     The time that your index was last modified.
   - **Index ID** – The ID of
     the index attached to your retriever.
   - **Storage used** – The
     amount of storage that your index is using.
   - **Index status** – The
     status of your index.

###### Note

You can't edit or update retriever or index
settings.

AWS CLI
**To get properties of an Amazon Kendra
retriever**

```

aws qbusiness get-retriever \
--application-id `application-id` \
--retriever-id `retriever-id`

```

## Listing Amazon Kendra

indices

To list your Amazon Kendra indices being used as retrievers, you can use the console
or the [ListRetrievers](../api-reference/API_ListRetrievers.md "../api-reference/API_ListRetrievers.md") API
operation.

If you use the console, the list of Amazon Kendra indices being used as retrievers can
be found within the list of data sources that you have created.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To list your Amazon Q Business indices
and retrievers**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application from the list of applications.
3. From the left navigation menu, choose **Data
   sources**.
4. On the **Data sources** page, a list of
   all indices that you have created is available.

AWS CLI
**To list Amazon Kendra
retrivers**

```

aws qbusiness list-retrievers \
--application-id `application-id` \
--max-results `maximum-result-to-display`

```

## Updating an Amazon Kendra

retriever

To update your Amazon Kendra retriever, you can use the [UpdateRetriever](../api-reference/API_UpdateRetriever.md "../api-reference/API_UpdateRetriever.md") API
operation.

You can't update your Amazon Kendra retriever using the console.

The following tab provides code examples for the AWS CLI.

Console
**This action is not supported on the
console.**

AWS CLI
**To update an Amazon Kendra
retriever**

```

aws qbusiness update-retriever \
--application-id `application-id` \
--retriever-id `retriever-id` \
--display-name `display-name` \
--role-arn `roleArn` \
--configuration `kendraIndexConfiguration="{indexId=<kendra-index-d>}"`

```
