

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing Amazon Q Business indices
<a name="supported-native-retriever-actions"></a>

To manage Amazon Q Business indexes, you can take the following actions:

**Topics**
+ [Deleting an Amazon Q Business index](#delete-native-retriever)
+ [Getting properties of an Amazon Q Business index](#describe-native-retriever)
+ [Listing Amazon Q Business indices and retrievers](#list-native-retriever)
+ [Editing Amazon Q Business indices](#update-native-retriever)

## Deleting an Amazon Q Business index
<a name="delete-native-retriever"></a>

To delete a Amazon Q Business index, you can use the console or the [DeleteIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIndex.html) API operation.

If you use the console, deleting an index automatically deletes the retriever attached to it. If you use the API, you must also use the [DeleteRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteRetriever.html) API operation to delete the Amazon Q Business retriever attached to your index.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To delete an Amazon Q Business index**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. Complete the steps to create your Amazon Q Business application.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, from **Index**, select **Delete**.

1. In the dialog box that opens, type **Confirm** to confirm deletion, and then choose **Delete**.

   You are returned to the service console while your application environment is deleted. When the deletion process is complete, the console displays a message confirming successful deletion.

------
#### [ AWS CLI ]

**To delete an Amazon Q Business index**

```
aws qbusiness delete-index \
--application-id {{application-id}} \
--retriever-id {{index-id}}
```

**To delete an Amazon Q Business retriever**

```
aws qbusiness delete-retriever \
--application-id {{application-id}} \
--retriever-id {{retriever-id}}
```

------

## Getting properties of an Amazon Q Business index
<a name="describe-native-retriever"></a>

To get the properties of an Amazon Q Business index and retriever, you can use the console or the [GetIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetIndex.html) and [GetRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html) API operation.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To get properties of an Amazon Q Business index and retriever** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. On the **Data sources** page, under **Index** the following settings are available:
   + **Index name** – The name of the index.
   + **Index status** – The status of your index.
   + **Index provisioning** – The number of index units provisioned for your index.
   + **Document count** – The number of documents that are attached to your index. 
   + **Storage used** – The amount of storage that your index is using. 
   + **Index ID** – The ID of the index attached to your retriever. 
   + **Retriever ID** – The ID of the retriever that you're using. 
   + **Retriever** – The retriever type that you're using. 
   + **Last modified** – The time that your index was last modified. 

------
#### [ AWS CLI ]

**To get properties of an Amazon Q Business index and retriever**

```
aws qbusiness get-index \
--application-id {{application-id}} \
--index-id {{index-id}}
```

```
aws qbusiness get-retriever \
--application-id {{application-id}} \
--retriever-id {{retriever-id}}
```

------

## Listing Amazon Q Business indices and retrievers
<a name="list-native-retriever"></a>

To list your native Amazon Q Business indices and retrievers, you can use the console or the [ListIndices](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListIndices.html) API operation and the [ListRetrievers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListRetrievers.html) API operation.

If you use the console, the list of Amazon Q Business indices and retrievers can be found within the list of data sources that you have created.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To list your Amazon Q Business indices and retrievers**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. On the **Data sources** page, a list of all indices that you have created is available.

------
#### [ AWS CLI ]

**To list your Amazon Q Business indices and retrievers**

```
aws qbusiness list-indices \
--application-id {{application-id}} \
--max-results {{maximum-result-to-display}}
```

```
aws qbusiness list-retrievers \
--application-id {{application-id}} \
--max-results {{maximum-result-to-display}}
```

------

## Editing Amazon Q Business indices
<a name="update-native-retriever"></a>

To edit your Amazon Q Business index, you can use the console or the [UpdateIndices](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndices.html) API operation.

**Note**  
When you update a native index, you can only update the number of storage units you provisioned for it. You can't change any other settings.

The following tab provides code examples for the AWS Management Console and AWS CLI.

------
#### [ Console ]

**To update your Amazon Q Business retriever**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. In the **Data sources** page, from **Index**, select **Edit**.

1. In **Edit index**, choose to update index units provisioned from **Number of units**. 

1. Select **Update** to save your changes.

------
#### [ AWS CLI ]

**To update your Amazon Q Business index**

```
aws qbusiness update-index \
--application-id {{application-id}} \
--index-id {{index-id}} \
--display-name {{display-name}} \
--role-arn {{roleArn}} \
--capacity-configuration {{IndexCapacityConfiguration="{indexId=<index-id>}"}}
```

------